"""Reset-pattern spines exposing a concrete-clause blind spot.

For ``q >= 3``, ``2 <= h < q``, and every length-``q-1`` bit pattern ``c``
with ``c[0]=1`` and ``c[h-1]=0``, the pattern spine advances on ``c[i]`` and
resets to the start on the other bit.  Its final state returns to gate ``h``
on ``1``.  Every accepted canonical suffix contains ``c+1`` as a contiguous
length-``q`` factor.  Thus there are ``2^(q-3)`` independently addressable
models at each gate, and a bank containing fewer distinct antecedent factors
from canonical suffixes cannot eliminate the gate.  Symbolic transition-cube
clauses are outside this bound.

The distinguished reset spine takes every free label to be one.  These 69
``q=71`` machines satisfy the conditional odd-suffix normal-form syntax, but
exact odd-core and shortcut-lift verification reject them immediately.

The scientific audit is deliberately frozen at ``q=71`` and all gates
``h=2,...,70``.  It checks the 213 translated shortcut-bank clauses and the 11
locally learned clauses in the seeded gate-2 artifact.  Every antecedent is
inactive on every distinguished reset spine.  This proves a blind spot in the
finite clause corpus; it does not produce a sanctuary or eliminate any gate.

No Z3 operation is used.  The optional solver package need not be installed.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import tempfile
from collections import deque
from pathlib import Path
from typing import Iterable, Sequence

from automata import DFA, Word, encode_lsd, shortest_canonical_word, word_text
from odd_core import (
    direct_fully_accelerated_odd,
    lift_odd_suffix_dfa_to_shortcut,
    odd_core_transducer,
)
from odd_suffix_cegis import (
    SuffixImplication,
    suffix_implication_digest,
    suffix_to_odd_dfa,
    translate_shortcut_implication_bank,
)
from transducer import shortcut_transducer
from verify import verify_candidate


SCHEMA = "x-9101-reset-spine-audit-v1"
PROGRAM = "odd-suffix-reset-spine-bank-blind-spot"
SEMANTIC_DIGEST_SERIALIZATION = (
    "sha256(utf8(json.dumps(semantic,sort_keys=True,separators=(',',':'),"
    "ensure_ascii=True,allow_nan=False)))"
)
SCIENTIFIC_Q = 71
EXPECTED_BANK_COUNT = 213
EXPECTED_LOCAL_COUNT = 11
EXPECTED_BANK_NORMALIZED_SHA256 = (
    "ea4dc231df8840bfe8369702b45b2bc1ba4f6bdc9a158da170b8c8a0bf8ce1cc"
)
DISCLAIMER = (
    "The 69 distinguished reset spines are exactly rejected countermodels, "
    "not Collatz sanctuaries. Arbitrary reset patterns selected by the "
    "factor-count argument are finite-clause evasion witnesses only; exact "
    "closure is not claimed for them. The audit eliminates no gate."
)


def _require_int(value: object, field: str) -> int:
    if type(value) is not int:
        raise ValueError(f"{field} must be an integer")
    return value


def _validate_parameters(q: int, h: int) -> None:
    _require_int(q, "q")
    _require_int(h, "h")
    if q < 3:
        raise ValueError("q must be at least 3")
    if not 2 <= h < q:
        raise ValueError("h must lie in [2, q)")


def _validate_reset_labels(q: int, h: int, labels: Sequence[int]) -> Word:
    _validate_parameters(q, h)
    word = tuple(labels)
    if len(word) != q - 1:
        raise ValueError("reset labels must have length q-1")
    if any(type(bit) is not int or bit not in (0, 1) for bit in word):
        raise ValueError("reset labels must be bits")
    if word[0] != 1:
        raise ValueError("the first reset label c[0] must be one")
    if word[h - 1] != 0:
        raise ValueError("the gate-entry reset label c[h-1] must be zero")
    return word


def reset_spine_labels(q: int, h: int) -> Word:
    """Return the ``q-1`` advancing labels before the final terminal one."""

    _validate_parameters(q, h)
    return tuple(0 if index == h - 1 else 1 for index in range(q - 1))


def reset_pattern_dfa(q: int, h: int, labels: Sequence[int]) -> DFA:
    """Construct the q-state reset-pattern spine with accepting gate h."""

    word = _validate_reset_labels(q, h, labels)
    transitions: list[tuple[int, int]] = []
    for state, advancing_bit in enumerate(word):
        row = [0, 0]
        row[advancing_bit] = state + 1
        transitions.append(tuple(row))
    transitions.append((0, h))
    return DFA(tuple(transitions), frozenset({h}), 0)


def reset_spine_dfa(q: int, h: int) -> DFA:
    """Construct the complete q-state reset spine with accepting gate h."""

    return reset_pattern_dfa(q, h, reset_spine_labels(q, h))


def reset_pattern_word(q: int, h: int, labels: Sequence[int]) -> Word:
    """Return the unique terminal-q acceptance pattern ``c+1``."""

    return _validate_reset_labels(q, h, labels) + (1,)


def contains_reset_pattern(
    q: int,
    h: int,
    labels: Sequence[int],
    canonical_suffix: Sequence[int],
) -> bool:
    """Return whether a canonical suffix contains the necessary factor.

    Acceptance implies this predicate, but the converse need not hold because
    symbols before the occurrence can leave the machine away from its start.
    In particular every canonical suffix shorter than ``q`` is rejected.
    """

    pattern = reset_pattern_word(q, h, labels)
    suffix = tuple(canonical_suffix)
    if any(type(bit) is not int or bit not in (0, 1) for bit in suffix):
        raise ValueError("canonical suffix must contain only bits")
    if suffix and suffix[-1] != 1:
        raise ValueError("a nonempty canonical suffix must end in one")
    return any(
        suffix[offset : offset + q] == pattern
        for offset in range(len(suffix) - q + 1)
    )


def indexed_reset_labels(q: int, h: int, index: int) -> Word:
    """Decode an index in ``[0, 2^(q-3))`` into the fixed-gate family."""

    _validate_parameters(q, h)
    _require_int(index, "index")
    pattern_count = 1 << (q - 3)
    if not 0 <= index < pattern_count:
        raise ValueError("reset-pattern index lies outside [0, 2^(q-3))")
    labels = [0] * (q - 1)
    labels[0] = 1
    free_index = 0
    for position in range(1, q - 1):
        if position == h - 1:
            continue
        labels[position] = (index >> free_index) & 1
        free_index += 1
    return tuple(labels)


def first_uncovered_reset_labels(
    q: int,
    h: int,
    antecedents: Sequence[Sequence[int]],
) -> Word:
    """Choose a reset pattern absent from every canonical antecedent.

    At most one member of the fixed-gate family can be covered by each
    distinct length-q antecedent factor.  The bounded loop is therefore a
    constructive pigeonhole proof whenever fewer than ``2^(q-3)`` distinct
    factors are supplied.
    """

    _validate_parameters(q, h)
    factors: set[Word] = set()
    for raw in antecedents:
        word = tuple(raw)
        if any(type(bit) is not int or bit not in (0, 1) for bit in word):
            raise ValueError("antecedents must contain only bits")
        if word and word[-1] != 1:
            raise ValueError("antecedents must be canonical suffixes")
        factors.update(
            word[offset : offset + q]
            for offset in range(len(word) - q + 1)
        )
    pattern_count = 1 << (q - 3)
    if len(factors) >= pattern_count:
        raise ValueError("too many distinct factors for the pigeonhole bound")
    for index in range(len(factors) + 1):
        labels = indexed_reset_labels(q, h, index)
        if labels + (1,) not in factors:
            return labels
    raise AssertionError("pigeonhole search failed")  # pragma: no cover


def least_suffix_word(q: int, h: int) -> Word:
    """The unique spine word ``1^(h-1) 0 1^(q-h)`` of length q."""

    return reset_pattern_word(q, h, reset_spine_labels(q, h))


def least_odd_integer(q: int, h: int) -> int:
    """Return the integer encoded by the odd marker followed by the spine."""

    _validate_parameters(q, h)
    return (1 << (q + 1)) - 1 - (1 << h)


def least_odd_image_formula(q: int, h: int) -> int:
    """Closed form for U(2^(q+1)-1-2^h)."""

    _validate_parameters(q, h)
    return 3 * (1 << q) - 1 - 3 * (1 << (h - 1))


def targeted_implication(q: int, h: int) -> SuffixImplication:
    """The exact missing clause generated by the reset spine's least word."""

    input_suffix = least_suffix_word(q, h)
    full_input = (1,) + input_suffix
    full_output = odd_core_transducer().transduce(full_input)
    if full_output[0] != 1:
        raise AssertionError("fully accelerated image is not odd")
    return SuffixImplication(input_suffix, full_output[1:])


def _graph_distances(dfa: DFA) -> tuple[int | None, ...]:
    distances: list[int | None] = [None] * dfa.state_count
    distances[dfa.start] = 0
    queue = deque([dfa.start])
    while queue:
        state = queue.popleft()
        distance = distances[state]
        if distance is None:  # pragma: no cover - queue invariant
            raise AssertionError("missing BFS distance")
        for bit in (0, 1):
            target = dfa.step(state, bit)
            if distances[target] is None:
                distances[target] = distance + 1
                queue.append(target)
    return tuple(distances)


def normal_form_checks(
    dfa: DFA,
    q: int,
    h: int,
    labels: Sequence[int] | None = None,
) -> dict[str, bool]:
    """Check every syntactic conclusion in L-9111 for this construction."""

    _validate_parameters(q, h)
    word = (
        reset_spine_labels(q, h)
        if labels is None
        else _validate_reset_labels(q, h, labels)
    )
    distances = _graph_distances(dfa)
    checks = {
        "q_states": dfa.state_count == q,
        "start_is_r0": dfa.start == 0,
        "gate_in_required_range": 2 <= h < q,
        "sole_accepting_gate": dfa.accepting == frozenset({h}),
        "first_suffix_one_advances": dfa.step(0, 1) == 1,
        "first_suffix_zero_does_not_advance": dfa.step(0, 0) != 1,
        "spine_states_exhaust_dfa": set(range(q)) == set(range(dfa.state_count)),
        "exact_spine_distances": distances == tuple(range(q)),
        "upper_hessenberg": all(
            dfa.step(state, bit) <= state + 1
            for state in range(q - 1)
            for bit in (0, 1)
        ),
        "each_spine_state_advances": all(
            state + 1 in dfa.transitions[state] for state in range(q - 1)
        ),
        "declared_spine_labels_advance": all(
            dfa.step(state, word[state]) == state + 1
            for state in range(q - 1)
        ),
        "final_one_enters_gate": dfa.step(q - 1, 1) == h,
        "earlier_ones_avoid_gate": all(
            dfa.step(state, 1) != h for state in range(q - 1)
        ),
        "gate_entry_spine_label_is_zero": word[h - 1] == 0
        and dfa.step(h - 1, 0) == h,
        "accepting_gate_has_odd_canonical_preimage": dfa.run(
            reset_pattern_word(q, h, word)
        )
        == h,
        "least_canonical_suffix_is_declared": shortest_canonical_word(dfa)
        == reset_pattern_word(q, h, word),
    }
    return checks


def _canonical_json_bytes(value: object) -> bytes:
    return json.dumps(
        value,
        ensure_ascii=True,
        separators=(",", ":"),
        sort_keys=True,
        allow_nan=False,
    ).encode("utf-8")


def _sha256_value(value: object) -> str:
    return hashlib.sha256(_canonical_json_bytes(value)).hexdigest()


def _sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _strict_json_load(path: Path) -> object:
    def reject_constant(raw: str):
        raise ValueError(f"nonstandard JSON constant: {raw}")

    return json.loads(
        path.read_text(encoding="utf-8"),
        parse_constant=reject_constant,
    )


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
            json.dump(
                payload,
                handle,
                indent=2,
                sort_keys=True,
                allow_nan=False,
            )
            handle.write("\n")
        os.replace(temporary_name, path)
        temporary_name = None
    finally:
        if temporary_name is not None:
            try:
                os.unlink(temporary_name)
            except FileNotFoundError:
                pass


def _parse_suffix_implication(raw: object) -> SuffixImplication:
    fields = {"input_suffix_lsd", "output_suffix_lsd"}
    if not isinstance(raw, dict) or set(raw) != fields:
        raise ValueError("malformed local suffix implication")
    values: list[Word] = []
    for field in ("input_suffix_lsd", "output_suffix_lsd"):
        text = raw[field]
        if not isinstance(text, str) or any(bit not in "01" for bit in text):
            raise ValueError(f"malformed {field}")
        word = tuple(int(bit) for bit in text)
        if word and word[-1] != 1:
            raise ValueError(f"{field} is not a canonical suffix")
        values.append(word)
    implication = SuffixImplication(values[0], values[1])
    exact = odd_core_transducer().transduce((1,) + implication.input_suffix)
    if exact != (1,) + implication.output_suffix:
        raise ValueError("local implication is not an exact U image")
    return implication


def _frozen_paths() -> tuple[Path, Path]:
    root = Path(__file__).resolve().parent / "results"
    return (
        root / "spine-q72-gate0-bank.json",
        root / "odd-suffix-q71-gate2-seeded-scout.json",
    )


def load_frozen_corpus() -> tuple[
    tuple[SuffixImplication, ...],
    tuple[SuffixImplication, ...],
    dict[str, object],
]:
    """Strictly load the 213 imported and 11 locally learned clauses."""

    bank_path, seeded_path = _frozen_paths()
    bank = translate_shortcut_implication_bank(bank_path)
    if len(bank.implications) != EXPECTED_BANK_COUNT:
        raise ValueError("frozen translated bank count changed")
    if (
        bank.provenance["normalized_implications_sha256"]
        != EXPECTED_BANK_NORMALIZED_SHA256
    ):
        raise ValueError("frozen translated bank semantic digest changed")

    raw = _strict_json_load(seeded_path)
    if not isinstance(raw, dict):
        raise ValueError("seeded scout root must be an object")
    if raw.get("schema") != "x-9101-odd-suffix-cegis-v1":
        raise ValueError("seeded scout schema changed")
    if raw.get("status") != "time_limit":
        raise ValueError("seeded scout status changed")
    config = raw.get("config")
    if not isinstance(config, dict) or any(
        config.get(field) != value
        for field, value in {
            "state_count": 71,
            "gate": 2,
            "odd_offset": 1,
            "solver_seed": 0,
        }.items()
    ):
        raise ValueError("seeded scout logical configuration changed")
    raw_imported = raw.get("imported_implications")
    expected_imported = [item.to_dict() for item in bank.implications]
    if raw_imported != expected_imported:
        raise ValueError("seeded scout imported ledger differs from frozen bank")
    raw_local = raw.get("learned_implications")
    if not isinstance(raw_local, list) or len(raw_local) != EXPECTED_LOCAL_COUNT:
        raise ValueError("seeded scout local ledger count changed")
    local = tuple(_parse_suffix_implication(item) for item in raw_local)
    keys = {
        (item.input_suffix, item.output_suffix) for item in bank.implications
    }
    for item in local:
        key = (item.input_suffix, item.output_suffix)
        if key in keys:
            raise ValueError("local and imported implication ledgers overlap")
        keys.add(key)
    if len(keys) != EXPECTED_BANK_COUNT + EXPECTED_LOCAL_COUNT:
        raise ValueError("frozen implication corpus contains duplicates")
    if raw.get("learned_implications_cumulative") != len(local):
        raise ValueError("seeded scout local accounting changed")
    if raw.get("imported_implications_cumulative") != len(bank.implications):
        raise ValueError("seeded scout imported accounting changed")
    if raw.get("enforced_implications_cumulative") != len(keys):
        raise ValueError("seeded scout enforced accounting changed")
    provenance = {
        "bank_file": bank_path.name,
        "bank_file_sha256": _sha256_file(bank_path),
        "bank_normalized_implications_sha256": EXPECTED_BANK_NORMALIZED_SHA256,
        "seeded_scout_file": seeded_path.name,
        "seeded_scout_file_sha256": _sha256_file(seeded_path),
    }
    return tuple(bank.implications), local, provenance


def _terminal_window_zero_counts(
    implications: Sequence[SuffixImplication], q: int
) -> tuple[int, ...]:
    counts: list[int] = []
    for implication in implications:
        word = implication.input_suffix
        if len(word) < q:
            raise ValueError("corpus antecedent is shorter than the audit window")
        counts.append(sum(bit == 0 for bit in word[-q:]))
    return tuple(counts)


def _length_q_factors(
    implications: Sequence[SuffixImplication], q: int
) -> frozenset[Word]:
    factors: set[Word] = set()
    for implication in implications:
        word = implication.input_suffix
        factors.update(
            word[offset : offset + q]
            for offset in range(len(word) - q + 1)
        )
    return frozenset(factors)


def _terminal_q_windows(
    implications: Sequence[SuffixImplication], q: int
) -> frozenset[Word]:
    return frozenset(
        implication.input_suffix[-q:]
        for implication in implications
        if len(implication.input_suffix) >= q
    )


def _eligible_reset_patterns(
    factors: Iterable[Word], q: int, h: int
) -> int:
    _validate_parameters(q, h)
    return sum(
        len(factor) == q
        and factor[0] == 1
        and factor[-1] == 1
        and factor[h - 1] == 0
        for factor in factors
    )


def _verification_record(q: int, h: int) -> dict[str, object]:
    suffix = reset_spine_dfa(q, h)
    checks = normal_form_checks(suffix, q, h)
    if not all(checks.values()):
        failed = sorted(key for key, value in checks.items() if not value)
        raise AssertionError(f"reset spine failed normal-form checks: {failed}")
    m = least_odd_integer(q, h)
    expected_image = least_odd_image_formula(q, h)
    direct_image = direct_fully_accelerated_odd(m)
    if direct_image != expected_image:
        raise AssertionError("closed-form U image is incorrect")
    implication = targeted_implication(q, h)
    if implication.input_suffix != least_suffix_word(q, h):
        raise AssertionError("targeted implication has the wrong antecedent")
    encoded_image = encode_lsd(expected_image)
    if (1,) + implication.output_suffix != encoded_image:
        raise AssertionError("targeted implication has the wrong exact image")
    if len(encoded_image) != q + 2:
        raise AssertionError("closed-form U image has the wrong bit length")
    image_zero_positions = tuple(
        index for index, bit in enumerate(encoded_image) if bit == 0
    )
    if image_zero_positions != (h - 1, h, q):
        raise AssertionError("closed-form U image has the wrong zero positions")
    if contains_reset_pattern(
        q, h, reset_spine_labels(q, h), implication.output_suffix
    ):
        raise AssertionError("fixed reset pattern occurs in its exact image")

    odd = suffix_to_odd_dfa(suffix)
    odd_result = verify_candidate(
        odd,
        odd_core_transducer(),
        forbidden_words=("1",),
    )
    lifted = lift_odd_suffix_dfa_to_shortcut(suffix)
    lift_result = verify_candidate(lifted, shortcut_transducer())
    expected_word = encode_lsd(m)
    expected_output = encode_lsd(expected_image)
    for label, result in (("odd", odd_result), ("lift", lift_result)):
        if result.valid or result.reason != "language is not forward invariant":
            raise AssertionError(f"{label} verifier did not reject by closure")
        if result.closure_input != expected_word:
            raise AssertionError(f"{label} verifier found an unexpected input")
        if result.closure_output != expected_output:
            raise AssertionError(f"{label} verifier found an unexpected output")
    return {
        "gate": h,
        "least_suffix_lsd": word_text(least_suffix_word(q, h)),
        "least_odd_integer": m,
        "least_odd_image": expected_image,
        "least_odd_image_suffix_lsd": word_text(implication.output_suffix),
        "least_odd_image_bit_length": len(encoded_image),
        "least_odd_image_zero_positions": list(image_zero_positions),
        "suffix_dfa_sha256": _sha256_value(suffix.to_dict()),
        "normal_form_checks": checks,
        "odd_verification": odd_result.to_dict(),
        "shortcut_lift_verification": lift_result.to_dict(),
    }


def build_audit() -> dict[str, object]:
    """Recompute the deterministic q=71 reset-family semantic audit."""

    q = SCIENTIFIC_Q
    bank, local, provenance = load_frozen_corpus()
    bank_zero_counts = _terminal_window_zero_counts(bank, q)
    local_zero_counts = _terminal_window_zero_counts(local, q)
    if min(bank_zero_counts) < 2 or min(local_zero_counts) < 2:
        raise AssertionError("the one-zero reset-family blind spot disappeared")

    corpus = bank + local
    corpus_keys = {
        (item.input_suffix, item.output_suffix) for item in corpus
    }
    bank_factors = _length_q_factors(bank, q)
    local_factors = _length_q_factors(local, q)
    corpus_factors = _length_q_factors(corpus, q)
    bank_terminal_windows = _terminal_q_windows(bank, q)
    local_terminal_windows = _terminal_q_windows(local, q)
    corpus_terminal_windows = _terminal_q_windows(corpus, q)
    factor_occurrences = sum(
        max(0, len(item.input_suffix) - q + 1) for item in corpus
    )
    pattern_count = 1 << (q - 3)
    if len(corpus_factors) >= pattern_count:
        raise AssertionError("frozen corpus exceeds the factor-count bound")

    records: list[dict[str, object]] = []
    targeted: list[SuffixImplication] = []
    for h in range(2, q):
        suffix = reset_spine_dfa(q, h)
        active_bank = sum(
            suffix.run(item.input_suffix) == h for item in bank
        )
        active_local = sum(
            suffix.run(item.input_suffix) == h for item in local
        )
        if active_bank or active_local:
            raise AssertionError("a frozen antecedent is active on a reset spine")
        implication = targeted_implication(q, h)
        if suffix.run(implication.input_suffix) != h:
            raise AssertionError("targeted reset antecedent is not active")
        if suffix.run(implication.output_suffix) == h:
            raise AssertionError("targeted reset image unexpectedly accepts")
        targeted.append(implication)
        record = _verification_record(q, h)
        record["active_imported_antecedents"] = active_bank
        record["active_local_antecedents"] = active_local
        records.append(record)

    targeted_keys = {
        (item.input_suffix, item.output_suffix) for item in targeted
    }
    if len(targeted_keys) != q - 2:
        raise AssertionError("targeted reset implications are not unique")
    overlap = len(targeted_keys & corpus_keys)
    if overlap:
        raise AssertionError("targeted reset implications already occur in corpus")

    targeted_tuple = tuple(targeted)
    augmented = corpus + targeted_tuple
    augmented_factors = _length_q_factors(augmented, q)
    if len(augmented_factors) >= pattern_count:
        raise AssertionError("augmented corpus exceeds the factor-count bound")
    targeted_factor_overlap = len(
        {item.input_suffix for item in targeted} & corpus_factors
    )

    evasion_records: list[dict[str, object]] = []
    antecedents = tuple(item.input_suffix for item in augmented)
    for h in range(2, q):
        labels = first_uncovered_reset_labels(q, h, antecedents)
        pattern = reset_pattern_word(q, h, labels)
        if pattern in augmented_factors:
            raise AssertionError("selected reset pattern occurs in an antecedent")
        suffix = reset_pattern_dfa(q, h, labels)
        checks = normal_form_checks(suffix, q, h, labels)
        if not all(checks.values()):
            raise AssertionError("selected evasion witness violates normal form")
        active_frozen = sum(
            suffix.run(item.input_suffix) == h for item in corpus
        )
        active_targeted = sum(
            suffix.run(item.input_suffix) == h for item in targeted
        )
        if active_frozen or active_targeted:
            raise AssertionError("factor-avoiding antecedent became active")
        evasion_records.append(
            {
                "gate": h,
                "covered_patterns_by_frozen_factors": _eligible_reset_patterns(
                    corpus_factors, q, h
                ),
                "covered_patterns_by_augmented_factors": _eligible_reset_patterns(
                    augmented_factors, q, h
                ),
                "selected_advance_labels_lsd": word_text(labels),
                "selected_required_factor_lsd": word_text(pattern),
                "selected_suffix_dfa_sha256": _sha256_value(suffix.to_dict()),
                "active_frozen_antecedents": active_frozen,
                "active_targeted_antecedents": active_targeted,
                "normal_form_checks": checks,
                "classification": "FINITE_CLAUSE_EVASION_WITNESS_ONLY",
            }
        )

    terminal_counterexample = reset_pattern_dfa(3, 2, (1, 0))
    if terminal_counterexample.run((1, 0, 1, 1)) != 2:
        raise AssertionError("terminal-window counterexample changed")

    semantic: dict[str, object] = {
        "q": q,
        "gate_range": [2, q - 1],
        "gate_count": q - 2,
        "reset_pattern_family": {
            "advance_labels": "c in {0,1}^{q-1}, c_0=1, c_(h-1)=0",
            "spine_transition": "delta(i,c_i)=i+1 for i<q-1",
            "reset_transition": "delta(i,1-c_i)=0 for i<q-1",
            "last_state": "delta(q-1,0)=0; delta(q-1,1)=h",
            "accepting": "{h}",
            "free_bits": q - 3,
            "patterns_per_gate": pattern_count,
            "antecedent_domain": "canonical suffixes: epsilon or binary words ending in 1",
            "necessary_accepted_antecedent_condition": (
                "the antecedent contains c_0...c_(q-2)1 as a contiguous "
                "length-q factor"
            ),
            "shorter_than_q_antecedents_reject": True,
            "terminal_window_condition_is_not_claimed": True,
            "terminal_window_counterexample": {
                "q": 3,
                "gate": 2,
                "advance_labels_lsd": "10",
                "accepted_suffix_lsd": "1011",
                "required_factor_lsd": "101",
                "terminal_q_window_lsd": "011",
            },
        },
        "distinguished_rejected_family": {
            "advance_label": "c_i = 0 iff i = h-1; otherwise c_i = 1",
            "members": q - 2,
            "exact_odd_and_shortcut_lift_verification": True,
        },
        "corpus": {
            "imported_implications": len(bank),
            "local_implications": len(local),
            "combined_implications": len(corpus),
            "imported_implications_sha256": suffix_implication_digest(bank),
            "local_implications_sha256": suffix_implication_digest(local),
            "combined_implications_sha256": suffix_implication_digest(corpus),
            "minimum_imported_terminal_window_zeros": min(bank_zero_counts),
            "minimum_local_terminal_window_zeros": min(local_zero_counts),
            "antecedents_shorter_than_q": sum(
                len(item.input_suffix) < q for item in corpus
            ),
            "length_q_factor_occurrences": factor_occurrences,
            "distinct_imported_length_q_factors": len(bank_factors),
            "distinct_local_length_q_factors": len(local_factors),
            "distinct_combined_length_q_factors": len(corpus_factors),
            "distinct_imported_terminal_q_windows": len(bank_terminal_windows),
            "distinct_local_terminal_q_windows": len(local_terminal_windows),
            "distinct_combined_terminal_q_windows": len(corpus_terminal_windows),
        },
        "gate_records": records,
        "targeted_implications": [
            {"gate": h, **item.to_dict()}
            for h, item in zip(range(2, q), targeted, strict=True)
        ],
        "targeted_implications_sha256": suffix_implication_digest(targeted),
        "targeted_overlap_with_frozen_corpus": overlap,
        "targeted_antecedent_factor_overlap_with_frozen_corpus": (
            targeted_factor_overlap
        ),
        "concrete_factor_bound": {
            "necessary_distinct_length_q_factors_per_fixed_gate": pattern_count,
            "frozen_distinct_length_q_factors": len(corpus_factors),
            "fixed_targeted_implications_added": len(targeted),
            "augmented_distinct_length_q_factors": len(augmented_factors),
            "all_gates_evade_augmented_concrete_bank": True,
            "scope_excludes_symbolic_transition_cube_clauses": True,
            "gate_evasion_records": evasion_records,
        },
        "conclusion": {
            "all_normal_form_checks_pass": True,
            "all_frozen_antecedents_inactive": True,
            "all_reset_spines_rejected_by_odd_verifier": True,
            "all_reset_spines_rejected_by_shortcut_lift_verifier": True,
            "reported_sanctuaries": 0,
            "gates_eliminated_by_frozen_clauses": 0,
            "gates_eliminated_by_augmented_concrete_clauses": 0,
        },
    }
    payload: dict[str, object] = {
        "schema": SCHEMA,
        "program": PROGRAM,
        "classification": "EXACT_AUDIT_WITH_FINITE_CLAUSE_EVASION_WITNESSES",
        "disclaimer": DISCLAIMER,
        "sources": provenance,
        "semantic": semantic,
        "semantic_digest_serialization": SEMANTIC_DIGEST_SERIALIZATION,
        "semantic_sha256": _sha256_value(semantic),
    }
    return payload


def validate_audit(path: Path) -> dict[str, object]:
    """Strictly compare an audit JSON with a fresh semantic recomputation."""

    observed = _strict_json_load(path)
    expected = build_audit()
    if not isinstance(observed, dict) or set(observed) != set(expected):
        raise ValueError("reset-spine audit root is malformed")
    digest = observed.get("semantic_sha256")
    if not isinstance(digest, str) or digest != _sha256_value(observed.get("semantic")):
        raise ValueError("reset-spine semantic digest mismatch")
    if observed != expected:
        raise ValueError("reset-spine audit differs from exact recomputation")
    return {
        "status": "valid",
        "schema": SCHEMA,
        "semantic_sha256": expected["semantic_sha256"],
        "gate_count": expected["semantic"]["gate_count"],  # type: ignore[index]
    }


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--validate",
        type=Path,
        help="strictly validate an existing audit against fresh recomputation",
    )
    group.add_argument(
        "--output",
        type=Path,
        help="atomically write the deterministic audit instead of stdout",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        if args.validate is not None:
            receipt = validate_audit(args.validate)
            print(json.dumps(receipt, indent=2, sort_keys=True, allow_nan=False))
            return 0
        payload = build_audit()
        if args.output is not None:
            _atomic_json_write(args.output, payload)
            receipt = {
                "status": "written",
                "path": args.output.as_posix(),
                "semantic_sha256": payload["semantic_sha256"],
            }
            print(json.dumps(receipt, indent=2, sort_keys=True, allow_nan=False))
        else:
            print(json.dumps(payload, indent=2, sort_keys=True, allow_nan=False))
        return 0
    except (OSError, ValueError, AssertionError) as exc:
        print(
            json.dumps(
                {"status": "invalid", "error": str(exc)},
                indent=2,
                sort_keys=True,
            )
        )
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
