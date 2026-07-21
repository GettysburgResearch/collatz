"""Exact CEGIS for the conditional odd-suffix floor normal form.

An odd canonical word has the unique form ``1x``.  This module synthesizes a
complete DFA ``A`` that reads only the suffix ``x``.  The main 71-state search
implements the necessary exact-floor conditions recorded in L-9111; smaller
state counts are useful only as engine diagnostics.

At 71 states, suffix gate ``h`` corresponds to gate ``h+1`` in the raw
72-state shortcut lift.  This structured lift neither covers shortcut gate 0
nor every generic raw 72-state machine.

Z3 is a proposal engine.  Every model is converted to the ordinary odd-word
language ``{1x : A accepts x}`` and checked under the fully accelerated map
``U`` by the exact product-graph verifier.  A model is reported as a candidate
only if its one-state dyadic lift is also accepted by the unchanged shortcut
verifier.  Time/model limits and solver ``unknown`` are explicitly incomplete.
The default and scientific target is ``3n+1``; ``3n-1`` is exposed only as a
nonstandard positive-control diagnostic.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import tempfile
import time
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Sequence

from automata import DFA, Word, is_canonical_positive, normalize_word, word_text
from odd_core import lift_odd_suffix_dfa_to_shortcut, odd_core_transducer
from spine_cegis import load_implication_bank as load_shortcut_implication_bank
from transducer import shortcut_transducer
from verify import VerificationResult, terminal_relation, verify_candidate


SCHEMA = "x-9101-odd-suffix-cegis-v1"
INCOMPLETE_DISCLAIMER = (
    "This is an incomplete bounded run in one declared odd-suffix spine/gate "
    "partition. It is not UNSAT, not a convergence result, and says nothing "
    "about other gates, larger suffix DFAs, or template-external languages. "
    "The wall-time deadline is soft: an exact candidate/relation verification "
    "already in progress runs atomically and may finish after the deadline."
)
SOLVER_UNSAT_DISCLAIMER = (
    "solver_unsat is a solver report only for this declared odd-suffix "
    "spine/gate partition. No independently checkable UNSAT proof is emitted."
)
NONSTANDARD_MAP_DISCLAIMER = (
    "The -1 map is a nonstandard positive-control diagnostic only; it makes "
    "no claim about the standard +1 Collatz map. "
)
NORMALIZED_DIGEST_SERIALIZATION = (
    "SHA-256 of UTF-8 canonical JSON (ASCII, sorted object keys, no whitespace) "
    "for unique implications ordered by input length/bits then output "
    "length/bits, with keys input_suffix_lsd and output_suffix_lsd"
)


@dataclass(frozen=True)
class OddSuffixSearchConfig:
    """One conditional suffix-spine partition and its operational limits."""

    state_count: int = 71
    gate: int = 2
    # +1 is the scientific target.  -1 exists only for positive-control tests.
    odd_offset: int = 1
    solver_seed: int = 0
    max_models: int | None = None
    time_limit_seconds: float | None = None

    def __post_init__(self) -> None:
        if type(self.state_count) is not int or self.state_count < 3:
            raise ValueError("state_count must be an integer at least 3")
        if type(self.gate) is not int or not 2 <= self.gate < self.state_count:
            raise ValueError("gate must be an integer in [2, state_count)")
        if type(self.odd_offset) is not int or self.odd_offset not in (-1, 1):
            raise ValueError("odd_offset must be -1 or +1")
        if type(self.solver_seed) is not int or self.solver_seed < 0:
            raise ValueError("solver_seed must be a nonnegative integer")
        if self.max_models is not None and (
            type(self.max_models) is not int or self.max_models < 1
        ):
            raise ValueError("max_models must be a positive integer when supplied")
        if self.time_limit_seconds is not None and (
            isinstance(self.time_limit_seconds, bool)
            or not isinstance(self.time_limit_seconds, (int, float))
            or not math.isfinite(float(self.time_limit_seconds))
            or self.time_limit_seconds <= 0
        ):
            raise ValueError("time_limit_seconds must be finite and positive")

    def logical_signature(self) -> dict[str, int]:
        """Fields that must agree for accounting-preserving resume."""

        return {
            "state_count": self.state_count,
            "gate": self.gate,
            "odd_offset": self.odd_offset,
            "solver_seed": self.solver_seed,
        }


@dataclass(frozen=True)
class SuffixImplication:
    """Necessary closure clause ``A(x) = gate -> A(U(1x)[1:]) = gate``."""

    input_suffix: Word
    output_suffix: Word

    def to_dict(self) -> dict[str, str]:
        return {
            "input_suffix_lsd": word_text(self.input_suffix),
            "output_suffix_lsd": word_text(self.output_suffix),
        }


@dataclass(frozen=True)
class LoadedCheckpoint:
    learned: tuple[SuffixImplication, ...]
    imported: tuple[SuffixImplication, ...]
    models_checked_cumulative: int
    elapsed_seconds_cumulative: float
    batch_history: tuple[dict[str, int], ...]
    bank_imports: tuple[dict[str, object], ...]


@dataclass(frozen=True)
class TranslatedShortcutBank:
    """Validated odd-suffix clauses and their shortcut-bank provenance."""

    implications: tuple[SuffixImplication, ...]
    provenance: dict[str, object]


def _require_z3():
    try:
        import z3  # type: ignore[import-not-found]
    except ImportError as exc:  # pragma: no cover - optional dependency path
        raise RuntimeError(
            "odd-suffix synthesis requires the optional 'z3-solver' package"
        ) from exc
    return z3


def _atomic_json_write(path: Path, payload: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary_name: str | None = None
    try:
        with tempfile.NamedTemporaryFile(
            "w",
            encoding="utf-8",
            newline="\n",
            dir=path.parent,
            prefix=f".{path.name}.",
            suffix=".tmp",
            delete=False,
        ) as handle:
            temporary_name = handle.name
            json.dump(payload, handle, indent=2, sort_keys=True, allow_nan=False)
            handle.write("\n")
        os.replace(temporary_name, path)
        temporary_name = None
    finally:
        if temporary_name is not None:
            try:
                os.unlink(temporary_name)
            except FileNotFoundError:
                pass


def _canonical_json_bytes(value: object) -> bytes:
    return json.dumps(
        value,
        ensure_ascii=True,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")


def _portable_display_path(path: Path) -> str:
    """Avoid serializing an environment-specific absolute workspace path."""

    return path.name if path.is_absolute() else path.as_posix()


def _ordered_suffix_implications(
    implications: Sequence[SuffixImplication],
) -> list[SuffixImplication]:
    return sorted(
        implications,
        key=lambda item: (
            len(item.input_suffix),
            item.input_suffix,
            len(item.output_suffix),
            item.output_suffix,
        ),
    )


def suffix_implication_digest(
    implications: Sequence[SuffixImplication],
) -> str:
    """Canonical digest described by ``NORMALIZED_DIGEST_SERIALIZATION``."""

    items = [item.to_dict() for item in _ordered_suffix_implications(implications)]
    return hashlib.sha256(_canonical_json_bytes(items)).hexdigest()


def _is_sha256(value: object) -> bool:
    return (
        isinstance(value, str)
        and len(value) == 64
        and all(character in "0123456789abcdef" for character in value)
    )


def _odd_part_word(word: Sequence[int] | str) -> tuple[Word, int]:
    """Strip every initial LSD zero and return (canonical odd part, count)."""

    bits = normalize_word(word)
    if not is_canonical_positive(bits):
        raise ValueError("shortcut-bank word must be canonical positive")
    low_zeros = 0
    while bits[low_zeros] == 0:
        low_zeros += 1
    return bits[low_zeros:], low_zeros


def translate_shortcut_implication_bank(path: Path) -> TranslatedShortcutBank:
    """Validate and normalize a standard shortcut implication bank.

    ``spine_cegis.load_implication_bank`` first validates the bank envelope and
    each exact ``w -> T(w)`` pair.  Both words are then reduced to their odd
    parts by stripping *all* initial LSD zeros.  Removing the first odd marker
    yields a suffix clause.  Even-source steps must preserve odd part and are
    omitted as saturation identities.  Nontrivial odd-source clauses are
    admitted only when the normalized output is exactly ``U`` of the
    normalized input.  Tautologies are harmless and omitted.
    """

    bank = load_shortcut_implication_bank(path)
    odd_machine = odd_core_transducer(1)
    active: dict[tuple[Word, Word], SuffixImplication] = {}
    tautologies = 0
    duplicates = 0
    inputs_with_low_zeros = 0
    outputs_with_low_zeros = 0
    outputs_with_multiple_low_zeros = 0
    for item in bank.implications:
        input_odd, input_low_zeros = _odd_part_word(item.input_word)
        output_odd, output_low_zeros = _odd_part_word(item.output_word)
        if input_low_zeros:
            inputs_with_low_zeros += 1
        if output_low_zeros:
            outputs_with_low_zeros += 1
        if output_low_zeros > 1:
            outputs_with_multiple_low_zeros += 1
        input_suffix = _strip_odd_marker(input_odd)
        output_suffix = _strip_odd_marker(output_odd)
        if input_low_zeros:
            # An even shortcut step removes one power of two and preserves the
            # odd part.  Its saturated-language clause is therefore an exact
            # identity, not a U step.
            if input_odd != output_odd:
                raise ValueError(
                    "normalized even shortcut implication changes odd part"
                )
        elif odd_machine.transduce(input_odd) != output_odd:
            raise ValueError(
                "normalized odd shortcut implication is not an exact U image"
            )
        if input_suffix == output_suffix:
            tautologies += 1
            continue
        key = (input_suffix, output_suffix)
        if key in active:
            duplicates += 1
            continue
        active[key] = SuffixImplication(input_suffix, output_suffix)

    implications = tuple(_ordered_suffix_implications(list(active.values())))
    provenance: dict[str, object] = {
        "source_path": _portable_display_path(path),
        "source_bank_sha256": bank.bank_sha256,
        "source_bank_file_sha256": bank.provenance["bank_file_sha256"],
        "source_checkpoint_sha256": bank.provenance[
            "source_checkpoint_sha256"
        ],
        "source_status": bank.provenance["source_status"],
        "source_implications": bank.provenance["declared_implications"],
        "normalization": (
            "strip_all_initial_lsd_zeros_to_each_odd_part_then_remove_first_one"
        ),
        "normalized_digest_serialization": NORMALIZED_DIGEST_SERIALIZATION,
        "normalized_implications_sha256": suffix_implication_digest(implications),
        "normalized_active_implications": len(implications),
        "tautologies_skipped": tautologies,
        "duplicates_skipped": duplicates,
        "inputs_with_low_zeros": inputs_with_low_zeros,
        "outputs_with_low_zeros": outputs_with_low_zeros,
        "outputs_with_multiple_low_zeros": outputs_with_multiple_low_zeros,
    }
    return TranslatedShortcutBank(implications, provenance)


def suffix_to_odd_dfa(suffix_dfa: DFA) -> DFA:
    """Recognize exactly the canonical odd words ``1x`` accepted by ``A``.

    State zero waits for the mandatory low odd bit, state one is the rejecting
    even-input sink, and the remaining states are an unmodified copy of ``A``.
    The first ``1`` selects ``A.start`` without being consumed by ``A``.
    """

    odd_start = 0
    even_sink = 1
    offset = 2
    transitions: list[tuple[int, int]] = [
        (even_sink, offset + suffix_dfa.start),
        (even_sink, even_sink),
    ]
    transitions.extend(
        (
            offset + suffix_dfa.step(state, 0),
            offset + suffix_dfa.step(state, 1),
        )
        for state in range(suffix_dfa.state_count)
    )
    accepting = frozenset(offset + state for state in suffix_dfa.accepting)
    return DFA(tuple(transitions), accepting, odd_start)


def _strip_odd_marker(word: Sequence[int] | str) -> Word:
    bits = normalize_word(word)
    if not is_canonical_positive(bits) or bits[0] != 1:
        raise ValueError("odd-core witness must be a canonical odd word")
    return bits[1:]


def _normalize_suffix(raw: object, field: str) -> Word:
    if not isinstance(raw, str):
        raise ValueError(f"checkpoint {field} must be a string")
    if any(character not in "01" for character in raw):
        raise ValueError(f"checkpoint {field} must be binary")
    suffix = normalize_word(raw)
    if suffix and suffix[-1] != 1:
        raise ValueError(
            f"checkpoint {field} must be empty or end in canonical terminal 1"
        )
    return suffix


def _full_odd_word(suffix: Word) -> Word:
    return (1,) + suffix


class OddSuffixEncoding:
    """Z3 encoding of one q-state conditional odd-suffix normal form."""

    def __init__(self, config: OddSuffixSearchConfig):
        self.config = config
        self.z3 = _require_z3()
        z3 = self.z3
        q = config.state_count
        self.delta = (
            z3.Array("odd_suffix_delta_0", z3.IntSort(), z3.IntSort()),
            z3.Array("odd_suffix_delta_1", z3.IntSort(), z3.IntSort()),
        )
        self.gate = z3.IntVal(config.gate)
        self.solver = z3.Solver()
        self.solver.set(random_seed=config.solver_seed)

        for bit in (0, 1):
            for state in range(q):
                target = z3.Select(self.delta[bit], state)
                self.solver.add(0 <= target, target < q)

        for state in range(q - 1):
            zero_target = z3.Select(self.delta[0], state)
            one_target = z3.Select(self.delta[1], state)
            self.solver.add(zero_target <= state + 1)
            self.solver.add(one_target <= state + 1)
            self.solver.add(
                z3.Or(zero_target == state + 1, one_target == state + 1)
            )
            self.solver.add(one_target != self.gate)

        # Full least word starts ``11``: the first 1 is consumed by the lift,
        # and the first suffix symbol is the unique advancing 1 from r_0.
        self.solver.add(z3.Select(self.delta[1], 0) == 1)
        self.solver.add(z3.Select(self.delta[0], 0) != 1)
        # The suffix is canonical only when its last symbol is 1.
        self.solver.add(z3.Select(self.delta[1], q - 1) == self.gate)

    def run_expression(self, suffix: Sequence[int] | str):
        state = self.z3.IntVal(0)
        for bit in normalize_word(suffix):
            state = self.z3.Select(self.delta[bit], state)
        return state

    def add_implication(self, implication: SuffixImplication) -> None:
        self.solver.add(
            self.z3.Implies(
                self.run_expression(implication.input_suffix) == self.gate,
                self.run_expression(implication.output_suffix) == self.gate,
            )
        )

    def add_implications_batch(
        self, implications: Sequence[SuffixImplication]
    ) -> None:
        """Assert implications with one shared LSD-prefix expression trie."""

        expressions: dict[Word, object] = {(): self.z3.IntVal(0)}

        def shared_run(suffix: Word):
            prefix: Word = ()
            for bit in suffix:
                next_prefix = prefix + (bit,)
                if next_prefix not in expressions:
                    expressions[next_prefix] = self.z3.Select(
                        self.delta[bit], expressions[prefix]
                    )
                prefix = next_prefix
            return expressions[prefix]

        for implication in implications:
            self.solver.add(
                self.z3.Implies(
                    shared_run(implication.input_suffix) == self.gate,
                    shared_run(implication.output_suffix) == self.gate,
                )
            )

    def extract_candidate(self, model) -> DFA:
        transitions = tuple(
            tuple(
                model.eval(
                    self.z3.Select(self.delta[bit], state),
                    model_completion=True,
                ).as_long()
                for bit in (0, 1)
            )
            for state in range(self.config.state_count)
        )
        return DFA(transitions, frozenset({self.config.gate}), 0)


def verify_suffix_candidate(
    suffix_dfa: DFA, *, odd_offset: int = 1
) -> tuple[VerificationResult, VerificationResult, DFA, DFA]:
    """Run the odd oracle and mandatory unchanged shortcut lift verifier."""

    odd_dfa = suffix_to_odd_dfa(suffix_dfa)
    odd_result = verify_candidate(
        odd_dfa,
        odd_core_transducer(odd_offset),
        forbidden_words=("1",),
    )
    lifted = lift_odd_suffix_dfa_to_shortcut(suffix_dfa)
    lift_result = verify_candidate(
        lifted,
        shortcut_transducer(odd_offset),
    )
    return odd_result, lift_result, odd_dfa, lifted


def _verification_dict(result: VerificationResult) -> dict[str, object]:
    return result.to_dict()


def _checkpoint_nonnegative_int(data: dict[str, object], field: str) -> int:
    value = data.get(field, 0)
    if type(value) is not int or value < 0:
        raise ValueError(f"checkpoint {field} must be a nonnegative integer")
    return value


def _displayed_config_matches(
    raw: object, expected: OddSuffixSearchConfig
) -> bool:
    if not isinstance(raw, dict):
        return False
    for field, value in expected.logical_signature().items():
        if field not in raw or type(raw[field]) is not type(value) or raw[field] != value:
            return False
    for limit in ("max_models", "time_limit_seconds"):
        if limit not in raw:
            return False
        displayed = raw[limit]
        # Operational limits may change on resume, so only require valid types.
        if limit == "max_models" and displayed is not None and (
            type(displayed) is not int or displayed < 1
        ):
            return False
        if limit == "time_limit_seconds" and displayed is not None and (
            isinstance(displayed, bool)
            or not isinstance(displayed, (int, float))
            or not math.isfinite(float(displayed))
            or displayed <= 0
        ):
            return False
    return True


def _parse_suffix_implications(
    raw_items: object,
    machine,
    *,
    label: str,
    seen: set[tuple[Word, Word]] | None = None,
) -> list[SuffixImplication]:
    if not isinstance(raw_items, list):
        raise ValueError(f"checkpoint has no {label} implication list")
    known = set() if seen is None else seen
    parsed: list[SuffixImplication] = []
    for raw in raw_items:
        if not isinstance(raw, dict) or set(raw) != {
            "input_suffix_lsd",
            "output_suffix_lsd",
        }:
            raise ValueError(f"checkpoint contains a malformed {label} implication")
        input_suffix = _normalize_suffix(
            raw.get("input_suffix_lsd"), "input_suffix_lsd"
        )
        output_suffix = _normalize_suffix(
            raw.get("output_suffix_lsd"), "output_suffix_lsd"
        )
        exact_output = machine.transduce(_full_odd_word(input_suffix))
        if _strip_odd_marker(exact_output) != output_suffix:
            raise ValueError(f"checkpoint {label} implication is not an exact U image")
        key = (input_suffix, output_suffix)
        if key in known:
            raise ValueError(f"checkpoint contains a duplicate {label} implication")
        known.add(key)
        parsed.append(SuffixImplication(input_suffix, output_suffix))
    return parsed


def _validate_bank_import_metadata(
    raw_imports: object,
    imported: Sequence[SuffixImplication],
) -> tuple[dict[str, object], ...]:
    if not isinstance(raw_imports, list):
        raise ValueError("checkpoint shortcut_bank_imports must be a list")
    if not raw_imports:
        if imported:
            raise ValueError("checkpoint imported clauses lack bank provenance")
        return ()
    if len(raw_imports) != 1:
        raise ValueError("checkpoint supports exactly one shortcut bank")
    raw = raw_imports[0]
    fields = {
        "source_path",
        "source_bank_sha256",
        "source_bank_file_sha256",
        "source_checkpoint_sha256",
        "source_status",
        "source_implications",
        "normalization",
        "normalized_digest_serialization",
        "normalized_implications_sha256",
        "normalized_active_implications",
        "tautologies_skipped",
        "duplicates_skipped",
        "inputs_with_low_zeros",
        "outputs_with_low_zeros",
        "outputs_with_multiple_low_zeros",
    }
    if not isinstance(raw, dict) or set(raw) != fields:
        raise ValueError("checkpoint shortcut-bank provenance is malformed")
    if not isinstance(raw["source_path"], str):
        raise ValueError("checkpoint shortcut-bank source path is invalid")
    for field in (
        "source_bank_sha256",
        "source_bank_file_sha256",
        "source_checkpoint_sha256",
        "normalized_implications_sha256",
    ):
        if not _is_sha256(raw[field]):
            raise ValueError(f"checkpoint shortcut-bank {field} is invalid")
    if raw["source_status"] not in {
        "running",
        "model_limit",
        "time_limit",
        "solver_unknown",
        "solver_unsat",
        "verified_candidate",
    }:
        raise ValueError("checkpoint shortcut-bank source status is invalid")
    for field in (
        "source_implications",
        "normalized_active_implications",
        "tautologies_skipped",
        "duplicates_skipped",
        "inputs_with_low_zeros",
        "outputs_with_low_zeros",
        "outputs_with_multiple_low_zeros",
    ):
        if type(raw[field]) is not int or raw[field] < 0:
            raise ValueError(f"checkpoint shortcut-bank {field} is invalid")
    if raw["normalization"] != (
        "strip_all_initial_lsd_zeros_to_each_odd_part_then_remove_first_one"
    ):
        raise ValueError("checkpoint shortcut-bank normalization is invalid")
    if raw["normalized_digest_serialization"] != NORMALIZED_DIGEST_SERIALIZATION:
        raise ValueError("checkpoint shortcut-bank digest serialization is invalid")
    if raw["normalized_active_implications"] != len(imported):
        raise ValueError("checkpoint shortcut-bank normalized count is inconsistent")
    if raw["source_implications"] != (
        len(imported) + raw["tautologies_skipped"] + raw["duplicates_skipped"]
    ):
        raise ValueError("checkpoint shortcut-bank source count is inconsistent")
    if (
        raw["inputs_with_low_zeros"] > raw["source_implications"]
        or raw["outputs_with_low_zeros"] > raw["source_implications"]
        or raw["outputs_with_multiple_low_zeros"]
        > raw["outputs_with_low_zeros"]
    ):
        raise ValueError("checkpoint shortcut-bank valuation count is inconsistent")
    if raw["normalized_implications_sha256"] != suffix_implication_digest(imported):
        raise ValueError("checkpoint shortcut-bank normalized digest mismatch")
    return (dict(raw),)


def _load_checkpoint_state(
    path: Path, config: OddSuffixSearchConfig
) -> LoadedCheckpoint:
    raw_data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(raw_data, dict):
        raise ValueError("checkpoint root must be an object")
    data: dict[str, object] = raw_data
    if data.get("schema") != SCHEMA:
        raise ValueError("checkpoint schema mismatch")
    signature = data.get("logical_signature")
    expected_signature = config.logical_signature()
    if not isinstance(signature, dict):
        raise ValueError("checkpoint has no logical signature")
    if set(signature) != set(expected_signature) or any(
        type(signature[field]) is not type(value) or signature[field] != value
        for field, value in expected_signature.items()
    ):
        raise ValueError("checkpoint logical configuration does not match")
    if not _displayed_config_matches(data.get("config"), config):
        raise ValueError("checkpoint displayed config is invalid or inconsistent")

    machine = odd_core_transducer(config.odd_offset)
    seen: set[tuple[Word, Word]] = set()
    imported = _parse_suffix_implications(
        data.get("imported_implications", []),
        machine,
        label="imported",
        seen=seen,
    )
    learned = _parse_suffix_implications(
        data.get("learned_implications"),
        machine,
        label="learned",
        seen=seen,
    )
    bank_imports = _validate_bank_import_metadata(
        data.get("shortcut_bank_imports", []), imported
    )
    if bank_imports and config.odd_offset != 1:
        raise ValueError("shortcut-bank imports require odd_offset=+1")

    if _checkpoint_nonnegative_int(
        data, "learned_implications_cumulative"
    ) != len(learned):
        raise ValueError("checkpoint learned implication count is inconsistent")
    if _checkpoint_nonnegative_int(
        data, "imported_implications_cumulative"
    ) != len(imported):
        raise ValueError("checkpoint imported implication count is inconsistent")
    declared_enforced = data.get(
        "enforced_implications_cumulative", len(imported) + len(learned)
    )
    if (
        type(declared_enforced) is not int
        or declared_enforced != len(imported) + len(learned)
    ):
        raise ValueError("checkpoint enforced implication count is inconsistent")
    models_checked = _checkpoint_nonnegative_int(
        data, "models_checked_cumulative"
    )
    elapsed = data.get("elapsed_seconds_cumulative", 0.0)
    if (
        isinstance(elapsed, bool)
        or not isinstance(elapsed, (int, float))
        or not math.isfinite(float(elapsed))
        or elapsed < 0
    ):
        raise ValueError("checkpoint cumulative elapsed time is invalid")

    raw_batches = data.get("batch_history", [])
    if not isinstance(raw_batches, list):
        raise ValueError("checkpoint batch_history must be a list")
    required_fields = (
        "model_number_this_run",
        "model_number_cumulative",
        "gate",
        "relation_edges",
        "product_states",
        "violating_endpoint_pairs",
        "new_implications",
        "shortest_full_witness_length",
        "longest_full_witness_length",
    )
    batches: list[dict[str, int]] = []
    for raw_batch in raw_batches:
        if not isinstance(raw_batch, dict):
            raise ValueError("checkpoint contains a malformed batch record")
        batch: dict[str, int] = {}
        for field in required_fields:
            value = raw_batch.get(field)
            if type(value) is not int or value < 0:
                raise ValueError(f"checkpoint batch field {field} is invalid")
            batch[field] = value
        for field in required_fields:
            if field != "gate" and batch[field] == 0:
                raise ValueError(f"checkpoint batch field {field} must be positive")
        if batch["gate"] != config.gate:
            raise ValueError("checkpoint batch gate differs from fixed partition")
        if batch["new_implications"] != batch["violating_endpoint_pairs"]:
            raise ValueError("checkpoint batch implication count is inconsistent")
        if (
            batch["shortest_full_witness_length"]
            > batch["longest_full_witness_length"]
        ):
            raise ValueError("checkpoint batch witness lengths are inconsistent")
        if batches and (
            batch["model_number_cumulative"]
            <= batches[-1]["model_number_cumulative"]
        ):
            raise ValueError("checkpoint cumulative model numbers are unordered")
        batches.append(batch)

    if _checkpoint_nonnegative_int(data, "batches_cumulative") != len(batches):
        raise ValueError("checkpoint batch count is inconsistent")
    if sum(batch["new_implications"] for batch in batches) != len(learned):
        raise ValueError("checkpoint batches do not account for implications")
    if batches and batches[-1]["model_number_cumulative"] > models_checked:
        raise ValueError("checkpoint batch model exceeds checked-model count")
    return LoadedCheckpoint(
        tuple(learned),
        tuple(imported),
        models_checked,
        float(elapsed),
        tuple(batches),
        bank_imports,
    )


def load_checkpoint(
    path: Path, config: OddSuffixSearchConfig
) -> list[SuffixImplication]:
    """Load every exact enforced obligation from a matching partition."""

    loaded = _load_checkpoint_state(path, config)
    return list(loaded.imported + loaded.learned)


def _payload(
    *,
    config: OddSuffixSearchConfig,
    status: str,
    models_this_run: int,
    models_before: int,
    elapsed_this_run: float,
    elapsed_before: float,
    learned: Sequence[SuffixImplication],
    learned_before: int,
    imported: Sequence[SuffixImplication],
    imported_before: int,
    bank_imports: Sequence[dict[str, object]],
    batches: Sequence[dict[str, int]],
    batches_before: int,
    resume_source: str | None,
    last_suffix: DFA | None,
    last_odd: VerificationResult | None,
    last_lift: VerificationResult | None,
    verified_lift: DFA | None,
    solver_reason: str | None = None,
) -> dict[str, object]:
    bounded = status in {"running", "model_limit", "time_limit", "solver_unknown"}
    base_disclaimer = (
        INCOMPLETE_DISCLAIMER
        if bounded
        else SOLVER_UNSAT_DISCLAIMER
        if status == "solver_unsat"
        else "Candidate accepted by both exact odd-core and shortcut-lift verifiers."
    )
    if config.odd_offset == -1:
        base_disclaimer = NONSTANDARD_MAP_DISCLAIMER + base_disclaimer
    result: dict[str, object] = {
        "schema": SCHEMA,
        "program": "conditional-odd-suffix-floor-cegis",
        "status": status,
        "config": asdict(config),
        "logical_signature": config.logical_signature(),
        "scope": (
            "one conditional q-state odd-suffix spine/gate partition; at q=71 "
            "suffix gate h maps to shortcut gate h+1; this structured lift "
            "does not cover shortcut gate 0 or every generic q=72 machine; "
            "the q=71 interpretation depends on L-9111 and its external premise"
        ),
        "suffix_gate": config.gate,
        "corresponding_shortcut_lift_gate": config.gate + 1,
        "covers_shortcut_gate_zero": False,
        "map_classification": (
            "standard_3n_plus_1_search"
            if config.odd_offset == 1
            else "nonstandard_3n_minus_1_positive_control_only"
        ),
        "models_checked": models_this_run,
        "models_checked_this_run": models_this_run,
        "models_checked_cumulative": models_before + models_this_run,
        "elapsed_seconds": round(elapsed_this_run, 6),
        "elapsed_seconds_this_run": round(elapsed_this_run, 6),
        "elapsed_seconds_cumulative": round(elapsed_before + elapsed_this_run, 6),
        "resumed": resume_source is not None,
        "resume_source": resume_source,
        "learned_implications_before_run": learned_before,
        "learned_implications_this_run": len(learned) - learned_before,
        "learned_implications_cumulative": len(learned),
        "learned_implications": [item.to_dict() for item in learned],
        "imported_implications_before_run": imported_before,
        "imported_implications_this_run": len(imported) - imported_before,
        "imported_implications_cumulative": len(imported),
        "imported_implications": [item.to_dict() for item in imported],
        "enforced_implications_cumulative": len(imported) + len(learned),
        "shortcut_bank_imports": list(bank_imports),
        "batches_before_run": batches_before,
        "batches_this_run": len(batches) - batches_before,
        "batches_cumulative": len(batches),
        "batch_history": list(batches),
        "bounded_or_incomplete": bounded,
        "independently_checkable_unsat_proof_emitted": False,
        "candidate_requires_odd_and_lift_verification": True,
        "disclaimer": base_disclaimer,
    }
    if last_suffix is not None:
        result["last_suffix_candidate"] = last_suffix.to_dict()
    if last_odd is not None:
        result["last_odd_verification"] = _verification_dict(last_odd)
    if last_lift is not None:
        result["last_lift_verification"] = _verification_dict(last_lift)
    if verified_lift is not None:
        result["verified_shortcut_lift"] = verified_lift.to_dict()
    if solver_reason is not None:
        result["solver_reason"] = solver_reason
    return result


def _is_timeout_reason(reason: str) -> bool:
    lowered = reason.lower()
    return "timeout" in lowered or "canceled" in lowered


def run_odd_suffix_cegis(
    config: OddSuffixSearchConfig,
    *,
    checkpoint_path: Path | None = None,
    result_path: Path | None = None,
    resume_path: Path | None = None,
    shortcut_bank_path: Path | None = None,
) -> dict[str, object]:
    """Run one exact-oracle CEGIS partition with resumable implications."""

    if resume_path is not None and shortcut_bank_path is not None:
        raise ValueError(
            "resume embeds imported clauses; do not supply the shortcut bank again"
        )
    if shortcut_bank_path is not None and config.odd_offset != 1:
        raise ValueError("shortcut-bank import is permitted only for odd_offset=+1")
    machine = odd_core_transducer(config.odd_offset)
    encoding = OddSuffixEncoding(config)
    loaded = (
        _load_checkpoint_state(resume_path, config)
        if resume_path is not None
        else LoadedCheckpoint((), (), 0, 0.0, (), ())
    )
    learned = list(loaded.learned)
    imported = list(loaded.imported)
    bank_imports = list(loaded.bank_imports)
    if shortcut_bank_path is not None:
        translated = translate_shortcut_implication_bank(shortcut_bank_path)
        imported.extend(translated.implications)
        bank_imports.append(translated.provenance)
    learned_keys = {
        (item.input_suffix, item.output_suffix) for item in imported + learned
    }
    if len(learned_keys) != len(imported) + len(learned):
        raise ValueError("imported and locally learned implications overlap")
    encoding.add_implications_batch(tuple(imported + learned))
    batches = list(loaded.batch_history)
    models_before = loaded.models_checked_cumulative
    elapsed_before = loaded.elapsed_seconds_cumulative
    learned_before = len(learned)
    imported_before = len(loaded.imported)
    batches_before = len(batches)
    resume_source = (
        None if resume_path is None else _portable_display_path(resume_path)
    )

    models = 0
    last_suffix: DFA | None = None
    last_odd: VerificationResult | None = None
    last_lift: VerificationResult | None = None
    verified_lift: DFA | None = None
    started = time.monotonic()

    def finish(status: str, reason: str | None = None) -> dict[str, object]:
        payload = _payload(
            config=config,
            status=status,
            models_this_run=models,
            models_before=models_before,
            elapsed_this_run=time.monotonic() - started,
            elapsed_before=elapsed_before,
            learned=learned,
            learned_before=learned_before,
            imported=imported,
            imported_before=imported_before,
            bank_imports=bank_imports,
            batches=batches,
            batches_before=batches_before,
            resume_source=resume_source,
            last_suffix=last_suffix,
            last_odd=last_odd,
            last_lift=last_lift,
            verified_lift=verified_lift,
            solver_reason=reason,
        )
        if checkpoint_path is not None:
            _atomic_json_write(checkpoint_path, payload)
        if result_path is not None:
            _atomic_json_write(result_path, payload)
        return payload

    while True:
        elapsed = time.monotonic() - started
        if config.time_limit_seconds is not None:
            remaining = config.time_limit_seconds - elapsed
            if remaining <= 0:
                return finish("time_limit")
            encoding.solver.set(timeout=max(1, int(remaining * 1000)))
        if config.max_models is not None and models >= config.max_models:
            return finish("model_limit")

        solver_status = encoding.solver.check()
        if solver_status == encoding.z3.unsat:
            return finish("solver_unsat")
        if solver_status != encoding.z3.sat:
            reason = encoding.solver.reason_unknown()
            if config.time_limit_seconds is not None and _is_timeout_reason(reason):
                return finish("time_limit", reason)
            return finish("solver_unknown", reason)

        suffix_candidate = encoding.extract_candidate(encoding.solver.model())
        odd_candidate = suffix_to_odd_dfa(suffix_candidate)
        odd_verification = verify_candidate(
            odd_candidate,
            machine,
            forbidden_words=("1",),
        )
        models += 1
        last_suffix = suffix_candidate
        last_odd = odd_verification
        last_lift = None
        verified_lift = None

        if odd_verification.valid:
            lifted = lift_odd_suffix_dfa_to_shortcut(suffix_candidate)
            lift_verification = verify_candidate(
                lifted,
                shortcut_transducer(config.odd_offset),
            )
            last_lift = lift_verification
            if not lift_verification.valid:
                raise AssertionError(
                    "odd verifier accepted a suffix candidate but the mandatory "
                    f"shortcut lift rejected it: {lift_verification.to_dict()}"
                )
            verified_lift = lifted
            return finish("verified_candidate")

        if (
            odd_verification.reason != "language is not forward invariant"
            or odd_verification.closure_input is None
            or odd_verification.closure_output is None
        ):
            raise AssertionError(
                "suffix normal form produced a non-closure verifier failure: "
                f"{odd_verification.reason}"
            )

        relation = terminal_relation(odd_candidate, machine, with_witnesses=True)
        source_gate = 2 + config.gate
        violating_edges = sorted(
            (
                edge
                for edge in relation.edges
                if edge[0] == source_gate and edge[1] not in odd_candidate.accepting
            ),
            key=lambda edge: (
                len(relation.witnesses[edge]),
                relation.witnesses[edge],
                edge,
            ),
        )
        if not violating_edges:
            raise AssertionError(
                "odd verifier reported closure failure without a violating endpoint"
            )

        primary = (
            odd_verification.closure_input,
            odd_verification.closure_output,
        )
        primary_seen = False
        batch: list[SuffixImplication] = []
        for source, target in violating_edges:
            input_full = relation.witnesses[(source, target)]
            output_full = machine.transduce(input_full)
            if (input_full, output_full) == primary:
                primary_seen = True
            input_suffix = _strip_odd_marker(input_full)
            output_suffix = _strip_odd_marker(output_full)
            if suffix_candidate.run(input_suffix) != config.gate:
                raise AssertionError("input witness does not reach suffix gate")
            if suffix_candidate.run(output_suffix) == config.gate:
                raise AssertionError("output witness unexpectedly reaches suffix gate")
            implication = SuffixImplication(input_suffix, output_suffix)
            key = (input_suffix, output_suffix)
            if key in learned_keys:
                raise AssertionError("solver repeated an enforced suffix violation")
            learned_keys.add(key)
            batch.append(implication)
        if not primary_seen:
            raise AssertionError("primary odd closure witness is absent from relation")

        learned.extend(batch)
        encoding.add_implications_batch(batch)
        full_lengths = [1 + len(item.input_suffix) for item in batch]
        batches.append(
            {
                "model_number_this_run": models,
                "model_number_cumulative": models_before + models,
                "gate": config.gate,
                "relation_edges": len(relation.edges),
                "product_states": relation.product_states,
                "violating_endpoint_pairs": len(violating_edges),
                "new_implications": len(batch),
                "shortest_full_witness_length": min(full_lengths),
                "longest_full_witness_length": max(full_lengths),
            }
        )

        if checkpoint_path is not None:
            _atomic_json_write(
                checkpoint_path,
                _payload(
                    config=config,
                    status="running",
                    models_this_run=models,
                    models_before=models_before,
                    elapsed_this_run=time.monotonic() - started,
                    elapsed_before=elapsed_before,
                    learned=learned,
                    learned_before=learned_before,
                    imported=imported,
                    imported_before=imported_before,
                    bank_imports=bank_imports,
                    batches=batches,
                    batches_before=batches_before,
                    resume_source=resume_source,
                    last_suffix=last_suffix,
                    last_odd=last_odd,
                    last_lift=last_lift,
                    verified_lift=verified_lift,
                ),
            )


def diagnostic_config(seed: int = 0) -> OddSuffixSearchConfig:
    """Small engine diagnostic with no 71-state scientific interpretation."""

    return OddSuffixSearchConfig(
        state_count=5,
        gate=2,
        solver_seed=seed,
        max_models=50,
        time_limit_seconds=10.0,
    )


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--states", type=int, default=71)
    parser.add_argument("--gate", type=int, default=2)
    parser.add_argument(
        "--odd-offset",
        type=int,
        choices=(-1, 1),
        default=1,
        help="+1 standard search (default); -1 nonstandard positive-control diagnostic",
    )
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--max-models", type=int)
    parser.add_argument("--time-limit", type=float)
    parser.add_argument("--checkpoint", type=Path)
    parser.add_argument("--result", type=Path)
    parser.add_argument("--resume", type=Path)
    parser.add_argument(
        "--import-shortcut-bank",
        type=Path,
        help=(
            "validate a spine_cegis shortcut bank, normalize both sides to "
            "odd suffixes, and seed this fresh +1 partition"
        ),
    )
    parser.add_argument(
        "--dry-diagnostic",
        action="store_true",
        help="run a five-state engine diagnostic, not a 71-state search",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    config = (
        diagnostic_config(args.seed)
        if args.dry_diagnostic
        else OddSuffixSearchConfig(
            state_count=args.states,
            gate=args.gate,
            odd_offset=args.odd_offset,
            solver_seed=args.seed,
            max_models=args.max_models,
            time_limit_seconds=args.time_limit,
        )
    )
    try:
        result = run_odd_suffix_cegis(
            config,
            checkpoint_path=args.checkpoint,
            result_path=args.result,
            resume_path=args.resume,
            shortcut_bank_path=args.import_shortcut_bank,
        )
    except RuntimeError as exc:
        print(json.dumps({"status": "missing_optional_dependency", "error": str(exc)}))
        return 2
    print(json.dumps(result, indent=2, sort_keys=True, allow_nan=False))
    return 0 if result["status"] in {"verified_candidate", "solver_unsat"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
