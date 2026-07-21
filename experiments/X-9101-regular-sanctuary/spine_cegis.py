"""Counterexample-guided synthesis for the exact-floor spine normal form.

This is an optional search driver, not part of the standard-library trusted
checker.  Z3 proposes transition tables.  Every proposed table is converted
to :class:`automata.DFA` and checked by :func:`verify.verify_candidate`; a
reported candidate is never accepted on the strength of the SMT model alone.

The encoded q-state normal form is the one forced when the shortest accepted
canonical word has length exactly q:

* states are numbered by their unique BFS depths ``0, ..., q - 1``;
* from state i < q - 1, neither transition jumps beyond i + 1 and at least
  one transition advances to i + 1;
* the only state whose terminal ``1`` transition may reach the accepting gate
  is q - 1;
* the sole accepting state is ``gate = delta(q - 1, 1)``.

For the conditional 72-state application, closure additionally forces the
zero loop ``delta(0, 0) = 0, delta(0, 1) = 1``.  A least-seed argument forces
the next spine bit to be one as well.  Both constraints are configurable so
the generic small-state encoding can be diagnosed; the ``11`` constraint
intentionally requires the zero-loop constraint.

Important result boundary: reaching a time or model limit is only an
incomplete bounded run.  It is not evidence of UNSAT and is never serialized
as such.  Even ``solver_unsat`` is only a solver report for the declared
normal-form partition; this prototype emits no independently checkable UNSAT
proof artifact.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import platform
import tempfile
import time
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Iterable, Sequence

from automata import (
    DFA,
    Word,
    is_canonical_positive,
    normalize_word,
    word_text,
)
from transducer import shortcut_transducer
from verify import VerificationResult, terminal_relation, verify_candidate


SCHEMA = "x-9101-spine-cegis-v2"
BANK_SCHEMA = "x-9101-spine-implication-bank-v1"
BANK_SEMANTICS = {
    "map": "shortcut_3n+1",
    "domain": "canonical_positive_finite_binary",
    "bit_order": "lsd_first",
    "obligation": "accepted_w_implies_accepted_T_w",
}
INCOMPLETE_DISCLAIMER = (
    "A time-limited, model-limited, or solver-unknown run is incomplete and is "
    "not an UNSAT proof, a convergence result, or evidence against larger/"
    "template-external automata. The solver deadline is soft: exact candidate "
    "verification and witness batching finish atomically and may overrun it."
)
RUNNING_DISCLAIMER = (
    "Intermediate checkpoint: all stored implications are exact necessary "
    "closure obligations, but the search is incomplete."
)
SOLVER_UNSAT_DISCLAIMER = (
    "solver_unsat is a solver report for this exact encoded normal-form "
    "partition. This prototype does not emit an independently checkable "
    "UNSAT proof artifact."
)


@dataclass(frozen=True)
class SpineSearchConfig:
    """Configuration whose logical fields define one synthesis partition."""

    state_count: int
    gate: int | None = None
    force_zero_loop: bool = True
    force_11_prefix: bool = True
    solver_seed: int = 0
    max_models: int | None = None
    time_limit_seconds: float | None = None

    def __post_init__(self) -> None:
        if type(self.state_count) is not int or self.state_count < 2:
            raise ValueError("state_count must be at least 2")
        if self.gate is not None and (
            type(self.gate) is not int
            or not 0 <= self.gate < self.state_count
        ):
            raise ValueError("gate is outside the DFA")
        if type(self.force_zero_loop) is not bool:
            raise ValueError("force_zero_loop must be Boolean")
        if type(self.force_11_prefix) is not bool:
            raise ValueError("force_11_prefix must be Boolean")
        if self.force_11_prefix and self.state_count < 3:
            raise ValueError("force_11_prefix requires at least three states")
        if self.force_11_prefix and not self.force_zero_loop:
            raise ValueError("force_11_prefix requires force_zero_loop")
        if type(self.solver_seed) is not int or self.solver_seed < 0:
            raise ValueError("solver_seed must be a nonnegative integer")
        if self.max_models is not None and (
            type(self.max_models) is not int or self.max_models < 1
        ):
            raise ValueError("max_models must be positive when supplied")
        if self.time_limit_seconds is not None and (
            isinstance(self.time_limit_seconds, bool)
            or not isinstance(self.time_limit_seconds, (int, float))
            or not math.isfinite(float(self.time_limit_seconds))
            or self.time_limit_seconds <= 0
        ):
            raise ValueError("time_limit_seconds must be positive when supplied")

    def logical_signature(self) -> dict[str, object]:
        """Fields that must agree before a checkpoint can be resumed."""

        return {
            "state_count": self.state_count,
            "gate": self.gate,
            "force_zero_loop": self.force_zero_loop,
            "force_11_prefix": self.force_11_prefix,
            "solver_seed": self.solver_seed,
        }


@dataclass(frozen=True)
class LearnedImplication:
    input_word: Word
    output_word: Word

    def to_dict(self) -> dict[str, str]:
        return {
            "input_lsd": word_text(self.input_word),
            "output_lsd": word_text(self.output_word),
        }


@dataclass(frozen=True)
class LoadedCheckpoint:
    learned: tuple[LearnedImplication, ...]
    imported: tuple[LearnedImplication, ...]
    models_checked_cumulative: int
    elapsed_seconds_cumulative: float
    batch_history: tuple[dict[str, int], ...]
    bank_imports: tuple[dict[str, object], ...]


@dataclass(frozen=True)
class ImplicationBank:
    implications: tuple[LearnedImplication, ...]
    bank_sha256: str
    provenance: dict[str, object]


def _require_z3():
    try:
        import z3  # type: ignore[import-not-found]
    except ImportError as exc:  # pragma: no cover - exercised without optional dep
        raise RuntimeError(
            "spine synthesis requires the optional 'z3-solver' package; "
            "the exact candidate checker itself does not"
        ) from exc
    return z3


def _is_timeout_reason(reason: str) -> bool:
    """Recognize timeout spellings emitted by supported Z3 builds."""

    lowered = reason.lower()
    return "timeout" in lowered or "canceled" in lowered


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
            json.dump(payload, handle, indent=2, sort_keys=True)
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


def _sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _sha256_file(path: Path) -> str:
    return _sha256_bytes(path.read_bytes())


def _ordered_implications(
    implications: Iterable[LearnedImplication],
) -> list[LearnedImplication]:
    return sorted(
        implications,
        key=lambda item: (
            len(item.input_word),
            item.input_word,
            len(item.output_word),
            item.output_word,
        ),
    )


def _implication_digest(implications: Iterable[LearnedImplication]) -> str:
    items = [item.to_dict() for item in _ordered_implications(implications)]
    return _sha256_bytes(_canonical_json_bytes(items))


def _bank_payload_digest(payload_without_digest: dict[str, object]) -> str:
    return _sha256_bytes(_canonical_json_bytes(payload_without_digest))


def _verification_dict(result: VerificationResult) -> dict[str, object]:
    return result.to_dict()


class SpineEncoding:
    """Z3 encoding of the complete exact-length-q spine/gate normal form."""

    def __init__(self, config: SpineSearchConfig):
        self.config = config
        self.z3 = _require_z3()
        z3 = self.z3
        q = config.state_count

        self.delta = (
            z3.Array("spine_delta_0", z3.IntSort(), z3.IntSort()),
            z3.Array("spine_delta_1", z3.IntSort(), z3.IntSort()),
        )
        self.solver = z3.Solver()
        self.solver.set(random_seed=config.solver_seed)
        self.gate = z3.Select(self.delta[1], q - 1)

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

        if config.gate is not None:
            self.solver.add(self.gate == config.gate)

        if config.force_zero_loop:
            self.solver.add(z3.Select(self.delta[0], 0) == 0)
            self.solver.add(z3.Select(self.delta[1], 0) == 1)

        if config.force_11_prefix:
            self.solver.add(z3.Select(self.delta[0], 1) != 2)
            self.solver.add(z3.Select(self.delta[1], 1) == 2)

        # These are implied by the q >= 3 spine normal form, but retaining the
        # explicit safety clauses makes relaxed two-state diagnostics honest.
        self.solver.add(self.run_expression((1,)) != self.gate)
        self.solver.add(self.run_expression((0, 1)) != self.gate)

    def run_expression(self, word: Sequence[int] | str):
        state = self.z3.IntVal(0)
        for bit in normalize_word(word):
            state = self.z3.Select(self.delta[bit], state)
        return state

    def add_implication(self, implication: LearnedImplication) -> None:
        self.solver.add(
            self.z3.Implies(
                self.run_expression(implication.input_word) == self.gate,
                self.run_expression(implication.output_word) == self.gate,
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
        gate = model.eval(self.gate, model_completion=True).as_long()
        return DFA(transitions, frozenset({gate}))


def _checkpoint_payload(
    *,
    config: SpineSearchConfig,
    status: str,
    models_checked_this_run: int,
    models_checked_before_run: int,
    elapsed_seconds_this_run: float,
    elapsed_seconds_before_run: float,
    learned: Iterable[LearnedImplication],
    learned_before_run: int,
    imported: Iterable[LearnedImplication],
    imported_before_run: int,
    bank_imports: Sequence[dict[str, object]],
    batch_history: Sequence[dict[str, int]],
    batches_before_run: int,
    resume_source: str | None,
    last_candidate: DFA | None,
    last_verification: VerificationResult | None,
    solver_reason: str | None = None,
) -> dict[str, object]:
    learned_list = list(learned)
    imported_list = list(imported)
    bounded = status in {
        "running",
        "model_limit",
        "time_limit",
        "solver_unknown",
    }
    payload: dict[str, object] = {
        "schema": SCHEMA,
        "program": "exact-floor-spine-cegis",
        "map": {
            "name": "shortcut_3n_plus_1",
            "bit_order": "lsd_first",
            "transducer": "shortcut_3n+1",
        },
        "environment": {
            "python": platform.python_version(),
            "platform": platform.platform(),
            "z3": _require_z3().get_version_string(),
        },
        "status": status,
        "config": asdict(config),
        "logical_signature": config.logical_signature(),
        # The unsuffixed fields are retained as this-run aliases for simple
        # consumers; cumulative fields make resumed work explicit.
        "models_checked": models_checked_this_run,
        "models_checked_before_run": models_checked_before_run,
        "models_checked_this_run": models_checked_this_run,
        "models_checked_cumulative": (
            models_checked_before_run + models_checked_this_run
        ),
        "elapsed_seconds": round(elapsed_seconds_this_run, 6),
        "elapsed_seconds_before_run": round(elapsed_seconds_before_run, 6),
        "elapsed_seconds_this_run": round(elapsed_seconds_this_run, 6),
        "elapsed_seconds_cumulative": round(
            elapsed_seconds_before_run + elapsed_seconds_this_run, 6
        ),
        "resumed": resume_source is not None,
        "resume_source": resume_source,
        "learned_implications_before_run": learned_before_run,
        "learned_implications_this_run": len(learned_list) - learned_before_run,
        "learned_implications_cumulative": len(learned_list),
        "learned_implications": [item.to_dict() for item in learned_list],
        # Imported obligations are exact T-images but are not credited to this
        # partition's models or batches.  Keeping the ledgers disjoint prevents
        # portable banks from importing another run's untrusted accounting.
        "imported_implications_before_run": imported_before_run,
        "imported_implications_this_run": len(imported_list) - imported_before_run,
        "imported_implications_cumulative": len(imported_list),
        "imported_implications": [item.to_dict() for item in imported_list],
        "enforced_implications_cumulative": len(learned_list) + len(imported_list),
        "implication_bank_imports": list(bank_imports),
        "batches_before_run": batches_before_run,
        "batches_this_run": len(batch_history) - batches_before_run,
        "batches_cumulative": len(batch_history),
        "batch_history": list(batch_history),
        "bounded_or_incomplete": bounded,
        "independently_checkable_unsat_proof_emitted": False,
        "disclaimer": (
            RUNNING_DISCLAIMER
            if status == "running"
            else INCOMPLETE_DISCLAIMER
            if bounded
            else SOLVER_UNSAT_DISCLAIMER
            if status == "solver_unsat"
            else "A found candidate is reported only after verify_candidate accepts it."
        ),
    }
    if last_candidate is not None:
        payload["last_candidate"] = last_candidate.to_dict()
    if last_verification is not None:
        payload["last_verification"] = _verification_dict(last_verification)
    if solver_reason is not None:
        payload["solver_reason"] = solver_reason
    return payload


def _canonical_checkpoint_word(raw: object, field: str) -> Word:
    if not isinstance(raw, str):
        raise ValueError(f"checkpoint {field} must be a string")
    if not raw or any(character not in "01" for character in raw):
        raise ValueError(f"checkpoint {field} must be a nonempty binary string")
    word = normalize_word(raw)
    if not is_canonical_positive(word):
        raise ValueError(f"checkpoint {field} must be canonical (terminal bit 1)")
    return word


def _checkpoint_nonnegative_int(data: dict[str, object], field: str) -> int:
    value = data.get(field, 0)
    if type(value) is not int or value < 0:
        raise ValueError(f"checkpoint {field} must be a nonnegative integer")
    return value


def _parse_implication_items(
    raw_items: object, machine, *, label: str
) -> list[LearnedImplication]:
    if not isinstance(raw_items, list):
        raise ValueError(f"{label} must be a list")
    implications: list[LearnedImplication] = []
    seen: set[tuple[Word, Word]] = set()
    for raw in raw_items:
        if not isinstance(raw, dict):
            raise ValueError(f"{label} contains a malformed implication")
        if set(raw) != {"input_lsd", "output_lsd"}:
            raise ValueError(f"{label} implication fields are invalid")
        input_word = _canonical_checkpoint_word(
            raw.get("input_lsd"), "input_lsd"
        )
        output_word = _canonical_checkpoint_word(
            raw.get("output_lsd"), "output_lsd"
        )
        if machine.transduce(input_word) != output_word:
            raise ValueError(f"{label} implication is not an exact T image")
        key = (input_word, output_word)
        if key in seen:
            raise ValueError(f"{label} contains a duplicate implication")
        seen.add(key)
        implications.append(LearnedImplication(input_word, output_word))
    return implications


def _is_sha256(value: object) -> bool:
    return (
        isinstance(value, str)
        and len(value) == 64
        and all(character in "0123456789abcdef" for character in value)
    )


def _validate_logical_signature(raw: object) -> dict[str, object]:
    fields = {
        "state_count",
        "gate",
        "force_zero_loop",
        "force_11_prefix",
        "solver_seed",
    }
    if not isinstance(raw, dict) or set(raw) != fields:
        raise ValueError("implication provenance logical signature is malformed")
    state_count = raw["state_count"]
    gate = raw["gate"]
    zero_loop = raw["force_zero_loop"]
    prefix = raw["force_11_prefix"]
    seed = raw["solver_seed"]
    if type(state_count) is not int or state_count < 2:
        raise ValueError("implication provenance state_count is invalid")
    if gate is not None and (type(gate) is not int or not 0 <= gate < state_count):
        raise ValueError("implication provenance gate is invalid")
    if type(zero_loop) is not bool or type(prefix) is not bool:
        raise ValueError("implication provenance normal-form flags are invalid")
    if prefix and not zero_loop:
        raise ValueError("implication provenance normal-form flags are incoherent")
    if type(seed) is not int or seed < 0:
        raise ValueError("implication provenance solver seed is invalid")
    return {
        "state_count": state_count,
        "gate": gate,
        "force_zero_loop": zero_loop,
        "force_11_prefix": prefix,
        "solver_seed": seed,
    }


def _load_checkpoint_state(
    path: Path, config: SpineSearchConfig, transducer=None
) -> LoadedCheckpoint:
    """Load strictly validated obligations and cumulative run metadata."""

    raw_data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(raw_data, dict):
        raise ValueError("checkpoint root must be an object")
    data: dict[str, object] = raw_data
    if data.get("schema") != SCHEMA:
        raise ValueError("checkpoint schema mismatch")
    expected_signature = config.logical_signature()
    stored_signature = data.get("logical_signature")
    if not isinstance(stored_signature, dict) or set(stored_signature) != set(
        expected_signature
    ):
        raise ValueError("checkpoint logical configuration does not match")
    for field, value in expected_signature.items():
        observed = stored_signature[field]
        if type(observed) is not type(value) or observed != value:
            raise ValueError("checkpoint logical configuration does not match")
    displayed_config = data.get("config")
    if not isinstance(displayed_config, dict):
        raise ValueError("checkpoint config must be an object")
    for field, value in expected_signature.items():
        observed = displayed_config.get(field)
        if (
            field not in displayed_config
            or type(observed) is not type(value)
            or observed != value
        ):
            raise ValueError(
                f"checkpoint displayed config disagrees on logical field {field}"
            )
    machine = shortcut_transducer() if transducer is None else transducer
    learned = _parse_implication_items(
        data.get("learned_implications"),
        machine,
        label="checkpoint learned_implications",
    )

    declared_learned = _checkpoint_nonnegative_int(
        data, "learned_implications_cumulative"
    )
    if declared_learned != len(learned):
        raise ValueError("checkpoint learned implication count is inconsistent")

    imported = _parse_implication_items(
        data.get("imported_implications", []),
        machine,
        label="checkpoint imported_implications",
    )
    declared_imported = _checkpoint_nonnegative_int(
        data, "imported_implications_cumulative"
    )
    if declared_imported != len(imported):
        raise ValueError("checkpoint imported implication count is inconsistent")
    local_keys = {(item.input_word, item.output_word) for item in learned}
    imported_keys = {(item.input_word, item.output_word) for item in imported}
    if local_keys & imported_keys:
        raise ValueError("checkpoint local and imported implication ledgers overlap")
    declared_enforced = data.get(
        "enforced_implications_cumulative", len(learned) + len(imported)
    )
    if (
        type(declared_enforced) is not int
        or declared_enforced != len(learned) + len(imported)
    ):
        raise ValueError("checkpoint enforced implication count is inconsistent")

    models_checked = _checkpoint_nonnegative_int(
        data, "models_checked_cumulative"
    )
    elapsed = data.get("elapsed_seconds_cumulative", 0.0)
    if (
        isinstance(elapsed, bool)
        or not isinstance(elapsed, (int, float))
        or elapsed < 0
        or not math.isfinite(float(elapsed))
    ):
        raise ValueError("checkpoint cumulative elapsed time is invalid")

    raw_batches = data.get("batch_history", [])
    if not isinstance(raw_batches, list):
        raise ValueError("checkpoint batch_history must be a list")
    batches: list[dict[str, int]] = []
    required_batch_fields = (
        "model_number_this_run",
        "model_number_cumulative",
        "gate",
        "relation_edges",
        "product_states",
        "violating_endpoint_pairs",
        "new_implications",
        "shortest_witness_length",
        "longest_witness_length",
    )
    for raw_batch in raw_batches:
        if not isinstance(raw_batch, dict):
            raise ValueError("checkpoint contains a malformed batch record")
        batch: dict[str, int] = {}
        for field in required_batch_fields:
            value = raw_batch.get(field)
            if type(value) is not int or value < 0:
                raise ValueError(f"checkpoint batch field {field} is invalid")
            batch[field] = value
        for field in (
            "model_number_this_run",
            "model_number_cumulative",
            "relation_edges",
            "product_states",
            "violating_endpoint_pairs",
            "new_implications",
            "shortest_witness_length",
            "longest_witness_length",
        ):
            if batch[field] == 0:
                raise ValueError(f"checkpoint batch field {field} must be positive")
        if batch["gate"] >= config.state_count:
            raise ValueError("checkpoint batch gate is outside the DFA")
        if config.gate is not None and batch["gate"] != config.gate:
            raise ValueError("checkpoint batch gate does not match its fixed partition")
        if batch["new_implications"] != batch["violating_endpoint_pairs"]:
            raise ValueError("checkpoint batch implication count is inconsistent")
        if batch["shortest_witness_length"] > batch["longest_witness_length"]:
            raise ValueError("checkpoint batch witness lengths are inconsistent")
        if (
            batches
            and batch["model_number_cumulative"]
            <= batches[-1]["model_number_cumulative"]
        ):
            raise ValueError("checkpoint cumulative batch model numbers are unordered")
        batches.append(batch)

    declared_batches = _checkpoint_nonnegative_int(data, "batches_cumulative")
    if declared_batches != len(batches):
        raise ValueError("checkpoint batch count is inconsistent")
    if sum(batch["new_implications"] for batch in batches) != len(learned):
        raise ValueError("checkpoint batch totals do not match learned implications")
    if batches and batches[-1]["model_number_cumulative"] > models_checked:
        raise ValueError("checkpoint batch model number exceeds checked models")

    raw_bank_imports = data.get("implication_bank_imports", [])
    if not isinstance(raw_bank_imports, list):
        raise ValueError("checkpoint implication_bank_imports must be a list")
    bank_imports: list[dict[str, object]] = []
    bank_digests: set[str] = set()
    bank_fields = {
        "bank_sha256",
        "bank_file_sha256",
        "source_checkpoint_sha256",
        "source_checkpoint_schema",
        "source_logical_signature",
        "source_status",
        "declared_implications",
        "new_implications",
        "duplicate_implications",
    }
    allowed_statuses = {
        "running",
        "model_limit",
        "time_limit",
        "solver_unknown",
        "solver_unsat",
        "verified_candidate",
    }
    for raw_import in raw_bank_imports:
        if not isinstance(raw_import, dict) or set(raw_import) != bank_fields:
            raise ValueError("checkpoint contains malformed bank provenance")
        for field in (
            "bank_sha256",
            "bank_file_sha256",
            "source_checkpoint_sha256",
        ):
            if not _is_sha256(raw_import[field]):
                raise ValueError(f"checkpoint bank provenance {field} is invalid")
        bank_sha = raw_import["bank_sha256"]
        if bank_sha in bank_digests:
            raise ValueError("checkpoint repeats an implication bank")
        bank_digests.add(bank_sha)
        if raw_import["source_checkpoint_schema"] != SCHEMA:
            raise ValueError("checkpoint bank source schema is invalid")
        signature = _validate_logical_signature(
            raw_import["source_logical_signature"]
        )
        if raw_import["source_status"] not in allowed_statuses:
            raise ValueError("checkpoint bank source status is invalid")
        counts: dict[str, int] = {}
        for field in (
            "declared_implications",
            "new_implications",
            "duplicate_implications",
        ):
            value = raw_import[field]
            if type(value) is not int or value < 0:
                raise ValueError(f"checkpoint bank provenance {field} is invalid")
            counts[field] = value
        if (
            counts["new_implications"] + counts["duplicate_implications"]
            != counts["declared_implications"]
        ):
            raise ValueError("checkpoint bank provenance counts are inconsistent")
        bank_imports.append(
            {
                **raw_import,
                "source_logical_signature": signature,
            }
        )
    if sum(item["new_implications"] for item in bank_imports) != len(imported):
        raise ValueError("checkpoint bank provenance does not account for imports")

    return LoadedCheckpoint(
        tuple(learned),
        tuple(imported),
        models_checked,
        float(elapsed),
        tuple(batches),
        tuple(bank_imports),
    )


def load_checkpoint(
    path: Path, config: SpineSearchConfig, transducer=None
) -> list[LearnedImplication]:
    """Load every validated obligation enforced by a matching checkpoint.

    Locally learned obligations come first, followed by portable imports.  The
    private state loader retains the two ledgers separately for accounting.
    """

    loaded = _load_checkpoint_state(path, config, transducer)
    return [*loaded.learned, *loaded.imported]


def _config_from_checkpoint_data(data: dict[str, object]) -> SpineSearchConfig:
    raw = data.get("config")
    fields = {
        "state_count",
        "gate",
        "force_zero_loop",
        "force_11_prefix",
        "solver_seed",
        "max_models",
        "time_limit_seconds",
    }
    if not isinstance(raw, dict) or set(raw) != fields:
        raise ValueError("checkpoint config is malformed")
    signature = _validate_logical_signature(
        {field: raw[field] for field in SpineSearchConfig(3).logical_signature()}
    )
    max_models = raw["max_models"]
    if max_models is not None and (type(max_models) is not int or max_models < 1):
        raise ValueError("checkpoint max_models is invalid")
    time_limit = raw["time_limit_seconds"]
    if time_limit is not None and (
        isinstance(time_limit, bool)
        or not isinstance(time_limit, (int, float))
        or time_limit <= 0
    ):
        raise ValueError("checkpoint time_limit_seconds is invalid")
    return SpineSearchConfig(
        **signature,
        max_models=max_models,
        time_limit_seconds=None if time_limit is None else float(time_limit),
    )


def export_implication_bank(checkpoint_path: Path, bank_path: Path) -> dict[str, object]:
    """Export only universally sound closure obligations from a checkpoint.

    Model counts, batches, elapsed time, candidates, and solver conclusions are
    deliberately excluded.  They are not needed to reuse ``w -> T(w)`` across
    gate partitions and are not trusted by an importing search.
    """

    raw = json.loads(checkpoint_path.read_text(encoding="utf-8"))
    if not isinstance(raw, dict):
        raise ValueError("checkpoint root must be an object")
    config = _config_from_checkpoint_data(raw)
    loaded = _load_checkpoint_state(checkpoint_path, config)
    status = raw.get("status")
    allowed_statuses = {
        "running",
        "model_limit",
        "time_limit",
        "solver_unknown",
        "solver_unsat",
        "verified_candidate",
    }
    if status not in allowed_statuses:
        raise ValueError("checkpoint status is invalid for bank provenance")

    implications = _ordered_implications((*loaded.learned, *loaded.imported))
    implication_dicts = [item.to_dict() for item in implications]
    source = {
        "checkpoint_sha256": _sha256_file(checkpoint_path),
        "checkpoint_schema": SCHEMA,
        "logical_signature": config.logical_signature(),
        "status": status,
        "locally_learned_implications": len(loaded.learned),
        "inherited_imported_implications": len(loaded.imported),
    }
    payload: dict[str, object] = {
        "schema": BANK_SCHEMA,
        "program": "exact-floor-spine-cegis",
        "semantics": BANK_SEMANTICS,
        "source": source,
        "implication_count": len(implications),
        "implications_sha256": _implication_digest(implications),
        "implications": implication_dicts,
    }
    payload["bank_sha256"] = _bank_payload_digest(payload)
    _atomic_json_write(bank_path, payload)
    return payload


def load_implication_bank(path: Path, transducer=None) -> ImplicationBank:
    """Load a portable bank, validating integrity and every exact T-image."""

    raw_bytes = path.read_bytes()
    raw = json.loads(raw_bytes.decode("utf-8"))
    root_fields = {
        "schema",
        "program",
        "semantics",
        "source",
        "implication_count",
        "implications_sha256",
        "implications",
        "bank_sha256",
    }
    if not isinstance(raw, dict) or set(raw) != root_fields:
        raise ValueError("implication bank root is malformed")
    if raw["schema"] != BANK_SCHEMA or raw["program"] != "exact-floor-spine-cegis":
        raise ValueError("implication bank schema or program mismatch")
    if raw["semantics"] != BANK_SEMANTICS:
        raise ValueError("implication bank semantics mismatch")
    bank_sha = raw["bank_sha256"]
    if not _is_sha256(bank_sha):
        raise ValueError("implication bank payload digest is malformed")
    unsigned = dict(raw)
    del unsigned["bank_sha256"]
    if _bank_payload_digest(unsigned) != bank_sha:
        raise ValueError("implication bank payload digest mismatch")

    source = raw["source"]
    source_fields = {
        "checkpoint_sha256",
        "checkpoint_schema",
        "logical_signature",
        "status",
        "locally_learned_implications",
        "inherited_imported_implications",
    }
    if not isinstance(source, dict) or set(source) != source_fields:
        raise ValueError("implication bank source provenance is malformed")
    if not _is_sha256(source["checkpoint_sha256"]):
        raise ValueError("implication bank source checkpoint digest is malformed")
    if source["checkpoint_schema"] != SCHEMA:
        raise ValueError("implication bank source checkpoint schema is invalid")
    signature = _validate_logical_signature(source["logical_signature"])
    allowed_statuses = {
        "running",
        "model_limit",
        "time_limit",
        "solver_unknown",
        "solver_unsat",
        "verified_candidate",
    }
    if source["status"] not in allowed_statuses:
        raise ValueError("implication bank source status is invalid")
    for field in (
        "locally_learned_implications",
        "inherited_imported_implications",
    ):
        if type(source[field]) is not int or source[field] < 0:
            raise ValueError(f"implication bank source {field} is invalid")

    machine = shortcut_transducer() if transducer is None else transducer
    implications = _parse_implication_items(
        raw["implications"], machine, label="implication bank"
    )
    declared = raw["implication_count"]
    if type(declared) is not int or declared != len(implications):
        raise ValueError("implication bank count is inconsistent")
    if (
        source["locally_learned_implications"]
        + source["inherited_imported_implications"]
        != declared
    ):
        raise ValueError("implication bank source counts are inconsistent")
    if not _is_sha256(raw["implications_sha256"]):
        raise ValueError("implication bank implication digest is malformed")
    if _implication_digest(implications) != raw["implications_sha256"]:
        raise ValueError("implication bank implication digest mismatch")
    ordered_dicts = [item.to_dict() for item in _ordered_implications(implications)]
    if raw["implications"] != ordered_dicts:
        raise ValueError("implication bank entries are not canonically ordered")

    provenance = {
        "bank_sha256": bank_sha,
        "bank_file_sha256": _sha256_bytes(raw_bytes),
        "source_checkpoint_sha256": source["checkpoint_sha256"],
        "source_checkpoint_schema": source["checkpoint_schema"],
        "source_logical_signature": signature,
        "source_status": source["status"],
        "declared_implications": declared,
    }
    return ImplicationBank(tuple(implications), bank_sha, provenance)


def run_spine_cegis(
    config: SpineSearchConfig,
    *,
    checkpoint_path: Path | None = None,
    result_path: Path | None = None,
    resume_path: Path | None = None,
    implication_bank_paths: Sequence[Path] = (),
) -> dict[str, object]:
    """Run exact-oracle CEGIS within one declared spine/gate partition."""

    transducer = shortcut_transducer()
    encoding = SpineEncoding(config)
    loaded = (
        _load_checkpoint_state(resume_path, config, transducer)
        if resume_path is not None
        else LoadedCheckpoint((), (), 0, 0.0, (), ())
    )
    learned = list(loaded.learned)
    imported = list(loaded.imported)
    batch_history = list(loaded.batch_history)
    bank_imports = list(loaded.bank_imports)
    models_checked_before_run = loaded.models_checked_cumulative
    elapsed_seconds_before_run = loaded.elapsed_seconds_cumulative
    learned_before_run = len(learned)
    imported_before_run = len(imported)
    batches_before_run = len(batch_history)
    # Preserve the user-supplied path rather than embedding an environment-
    # specific absolute workspace path in a result intended for version control.
    resume_source = (
        None if resume_path is None else _portable_display_path(resume_path)
    )
    enforced_keys = {
        (item.input_word, item.output_word) for item in learned
    }
    enforced_keys.update(
        (item.input_word, item.output_word) for item in imported
    )
    known_bank_digests = {item["bank_sha256"] for item in bank_imports}
    for bank_path in implication_bank_paths:
        bank = load_implication_bank(bank_path, transducer)
        if bank.bank_sha256 in known_bank_digests:
            continue
        new_count = 0
        duplicate_count = 0
        for implication in bank.implications:
            key = (implication.input_word, implication.output_word)
            if key in enforced_keys:
                duplicate_count += 1
                continue
            enforced_keys.add(key)
            imported.append(implication)
            new_count += 1
        bank_imports.append(
            {
                **bank.provenance,
                "new_implications": new_count,
                "duplicate_implications": duplicate_count,
            }
        )
        known_bank_digests.add(bank.bank_sha256)

    for implication in (*learned, *imported):
        encoding.add_implication(implication)

    started = time.monotonic()
    models_checked = 0
    last_candidate: DFA | None = None
    last_verification: VerificationResult | None = None

    def finish(status: str, solver_reason: str | None = None) -> dict[str, object]:
        payload = _checkpoint_payload(
            config=config,
            status=status,
            models_checked_this_run=models_checked,
            models_checked_before_run=models_checked_before_run,
            elapsed_seconds_this_run=time.monotonic() - started,
            elapsed_seconds_before_run=elapsed_seconds_before_run,
            learned=learned,
            learned_before_run=learned_before_run,
            imported=imported,
            imported_before_run=imported_before_run,
            bank_imports=bank_imports,
            batch_history=batch_history,
            batches_before_run=batches_before_run,
            resume_source=resume_source,
            last_candidate=last_candidate,
            last_verification=last_verification,
            solver_reason=solver_reason,
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
            # Z3 timeout is per check.  A minimum of one millisecond avoids
            # accidentally translating a small positive remainder to infinity.
            encoding.solver.set(timeout=max(1, int(remaining * 1000)))

        if config.max_models is not None and models_checked >= config.max_models:
            return finish("model_limit")

        solver_status = encoding.solver.check()
        if solver_status == encoding.z3.unsat:
            return finish("solver_unsat")
        if solver_status != encoding.z3.sat:
            reason = encoding.solver.reason_unknown()
            # Z3 4.16 reports an elapsed per-check timeout as ``canceled`` on
            # some platforms and as ``timeout`` on others.  Both are the
            # configured solver deadline, not a logically different UNKNOWN.
            # Exact verification/batching between checks is deliberately
            # atomic, so the overall wall time is a soft bound.
            if config.time_limit_seconds is not None and _is_timeout_reason(reason):
                return finish("time_limit", reason)
            return finish("solver_unknown", reason)

        candidate = encoding.extract_candidate(encoding.solver.model())
        verification = verify_candidate(candidate, transducer)
        models_checked += 1
        last_candidate = candidate
        last_verification = verification

        if verification.valid:
            return finish("verified_candidate")

        if (
            verification.reason != "language is not forward invariant"
            or verification.closure_input is None
            or verification.closure_output is None
        ):
            raise AssertionError(
                "normal-form solver produced a non-closure verifier failure: "
                f"{verification.reason}"
            )

        # verify_candidate remains the mandatory arbiter.  Once it rejects a
        # model, recompute the exact endpoint relation to batch one shortest
        # BFS witness for every violating endpoint pair in that same model.
        relation = terminal_relation(candidate, transducer, with_witnesses=True)
        gate = next(iter(candidate.accepting))
        violating_edges = sorted(
            (
                edge
                for edge in relation.edges
                if edge[0] == gate and edge[1] != gate
            ),
            key=lambda edge: (
                len(relation.witnesses[edge]),
                relation.witnesses[edge],
                edge,
            ),
        )
        if not violating_edges:
            raise AssertionError(
                "verify_candidate reported a closure failure but the exact "
                "terminal relation has no violating endpoint pair"
            )

        primary = (
            verification.closure_input,
            verification.closure_output,
        )
        batch: list[LearnedImplication] = []
        primary_seen = False
        for source, target in violating_edges:
            input_word = relation.witnesses[(source, target)]
            output_word = transducer.transduce(input_word)
            if candidate.run(input_word) != source:
                raise AssertionError("terminal-relation input witness is inconsistent")
            if candidate.run(output_word) != target:
                raise AssertionError("terminal-relation output witness is inconsistent")
            if (input_word, output_word) == primary:
                primary_seen = True
            implication = LearnedImplication(input_word, output_word)
            key = (implication.input_word, implication.output_word)
            if key in enforced_keys:
                raise AssertionError(
                    "exact relation repeated an already-enforced closure violation"
                )
            enforced_keys.add(key)
            batch.append(implication)

        if not primary_seen:
            raise AssertionError(
                "verify_candidate's primary closure witness is absent from the "
                "recomputed exact terminal relation"
            )

        for implication in batch:
            learned.append(implication)
            encoding.add_implication(implication)

        witness_lengths = [len(item.input_word) for item in batch]
        batch_history.append(
            {
                "model_number_this_run": models_checked,
                "model_number_cumulative": (
                    models_checked_before_run + models_checked
                ),
                "gate": gate,
                "relation_edges": len(relation.edges),
                "product_states": relation.product_states,
                "violating_endpoint_pairs": len(violating_edges),
                "new_implications": len(batch),
                "shortest_witness_length": min(witness_lengths),
                "longest_witness_length": max(witness_lengths),
            }
        )

        if checkpoint_path is not None:
            _atomic_json_write(
                checkpoint_path,
                _checkpoint_payload(
                    config=config,
                    status="running",
                    models_checked_this_run=models_checked,
                    models_checked_before_run=models_checked_before_run,
                    elapsed_seconds_this_run=time.monotonic() - started,
                    elapsed_seconds_before_run=elapsed_seconds_before_run,
                    learned=learned,
                    learned_before_run=learned_before_run,
                    imported=imported,
                    imported_before_run=imported_before_run,
                    bank_imports=bank_imports,
                    batch_history=batch_history,
                    batches_before_run=batches_before_run,
                    resume_source=resume_source,
                    last_candidate=last_candidate,
                    last_verification=last_verification,
                ),
            )


def diagnostic_config(seed: int = 0) -> SpineSearchConfig:
    """A deliberately tiny engine diagnostic; it makes no 72-state claim."""

    return SpineSearchConfig(
        state_count=5,
        force_zero_loop=True,
        force_11_prefix=True,
        solver_seed=seed,
        max_models=50,
        time_limit_seconds=10.0,
    )


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--states", type=int, default=72)
    parser.add_argument("--gate", type=int)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--max-models", type=int)
    parser.add_argument("--time-limit", type=float)
    parser.add_argument("--relax-zero-loop", action="store_true")
    parser.add_argument("--relax-11-prefix", action="store_true")
    parser.add_argument("--checkpoint", type=Path)
    parser.add_argument("--result", type=Path)
    parser.add_argument("--resume", type=Path)
    parser.add_argument(
        "--import-bank",
        action="append",
        type=Path,
        default=[],
        help="import a portable exact implication bank; may be repeated",
    )
    parser.add_argument(
        "--export-bank",
        nargs=2,
        type=Path,
        metavar=("CHECKPOINT", "BANK"),
        help="export validated implications without running synthesis",
    )
    parser.add_argument(
        "--dry-diagnostic",
        action="store_true",
        help="run a five-state engine diagnostic, not a scientific search",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    if args.export_bank is not None:
        checkpoint_path, bank_path = args.export_bank
        payload = export_implication_bank(checkpoint_path, bank_path)
        print(
            json.dumps(
                {
                    "status": "implication_bank_exported",
                    "path": bank_path.as_posix(),
                    "bank_sha256": payload["bank_sha256"],
                    "implication_count": payload["implication_count"],
                },
                indent=2,
                sort_keys=True,
            )
        )
        return 0
    config = (
        diagnostic_config(args.seed)
        if args.dry_diagnostic
        else SpineSearchConfig(
            state_count=args.states,
            gate=args.gate,
            force_zero_loop=not args.relax_zero_loop,
            force_11_prefix=not args.relax_11_prefix,
            solver_seed=args.seed,
            max_models=args.max_models,
            time_limit_seconds=args.time_limit,
        )
    )
    try:
        result = run_spine_cegis(
            config,
            checkpoint_path=args.checkpoint,
            result_path=args.result,
            resume_path=args.resume,
            implication_bank_paths=args.import_bank,
        )
    except RuntimeError as exc:
        print(json.dumps({"status": "missing_optional_dependency", "error": str(exc)}))
        return 2
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["status"] in {"verified_candidate", "solver_unsat"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
