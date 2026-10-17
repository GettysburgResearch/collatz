"""Durable paired census for exact-floor suffix and raw gate partitions.

The default generation-zero wave covers the natural pairs

    suffix (q=71, gate h) <-> raw shortcut (q=72, gate h+1),
    h = 2, ..., 70.

Every partition starts from the same frozen shortcut implication bank.  Local
clauses learned in one partition are deliberately *not* shared during the
wave: cross-gate sharing is sound only after a generation barrier freezes a
new, independently revalidated bank.  Z3 remains only a proposal engine.  The
compact wrapper stores every proposed transition table and enough local
evidence for ``--validate`` to reconstruct all exact verifications and batches
without importing Z3.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import platform
import subprocess
import tempfile
import time
from collections import Counter
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path
from typing import Iterable, Sequence

from automata import DFA, Word, decode_lsd, is_canonical_positive, normalize_word
from independent_check import verify_candidate_via_preimage
from odd_core import lift_odd_suffix_dfa_to_shortcut, odd_core_transducer
from odd_suffix_cegis import (
    NORMALIZED_DIGEST_SERIALIZATION,
    OddSuffixEncoding,
    OddSuffixSearchConfig,
    SuffixImplication,
    suffix_implication_digest,
    suffix_to_odd_dfa,
    translate_shortcut_implication_bank,
)
from spine_cegis import (
    BANK_SCHEMA,
    BANK_SEMANTICS,
    LearnedImplication,
    SpineEncoding,
    SpineSearchConfig,
    load_implication_bank,
)
from transducer import shortcut_transducer
from verify import terminal_relation, verify_candidate


SCHEMA = "x-9101-paired-gate-census-v1"
PROGRAM = "paired-exact-floor-gate-census"
DEFAULT_BANK = Path(__file__).resolve().parent / "results/spine-q72-gate0-bank.json"
INCOMPLETE_DISCLAIMER = (
    "Every non-candidate result is bounded and partition-specific. A timeout, "
    "zero-model stall, model quota, solver unknown, or solver-level UNSAT is "
    "not a convergence result. No independently checkable UNSAT proof is "
    "emitted. Exact candidate checks and witness batches finish atomically."
)

TOP_FIELDS = {
    "schema",
    "program",
    "status",
    "disclaimer",
    "plan",
    "plan_sha256",
    "baseline",
    "environment",
    "partitions",
    "aggregate",
    "failure",
    "semantic_sha256",
    "payload_sha256",
}
PARTITION_FIELDS = {
    "partition_id",
    "task_index",
    "lane",
    "suffix_gate",
    "gate",
    "state_count",
    "solver_seed",
    "model_quota",
    "watchdog_seconds",
    "status",
    "classification",
    "solver_reason",
    "bounded_or_incomplete",
    "models_checked",
    "batches",
    "imported_implication_count",
    "imported_implications_sha256",
    "local_implication_count",
    "local_implications_sha256",
    "local_implications",
    "enforced_implication_count",
    "model_records",
    "setup_seconds",
    "external_wall_seconds",
    "semantic_sha256",
    "payload_sha256",
}
MODEL_RECORD_FIELDS = {
    "model_number",
    "candidate",
    "verification",
    "lift_verification",
    "batch",
}
BATCH_FIELDS = {
    "relation_edges",
    "product_states",
    "violating_endpoint_pairs",
    "new_implications",
    "local_offset",
    "shortest_witness_length",
    "longest_witness_length",
}


def _canonical_json_bytes(value: object) -> bytes:
    return json.dumps(
        value,
        ensure_ascii=True,
        allow_nan=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")


def _sha256_object(value: object) -> str:
    return hashlib.sha256(_canonical_json_bytes(value)).hexdigest()


def _sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _is_sha256(value: object) -> bool:
    return (
        isinstance(value, str)
        and len(value) == 64
        and all(character in "0123456789abcdef" for character in value)
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
        for attempt in range(12):
            try:
                os.replace(temporary_name, path)
                break
            except PermissionError:
                # OneDrive and antivirus indexers can hold a just-replaced
                # JSON target briefly on Windows. Preserve atomic replacement
                # semantics while tolerating that bounded transient lock.
                if attempt == 11:
                    raise
                time.sleep(0.05 * (attempt + 1))
        temporary_name = None
    finally:
        if temporary_name is not None:
            try:
                os.unlink(temporary_name)
            except FileNotFoundError:
                pass


def outside_in_schedule(first_gate: int, last_gate: int) -> list[int]:
    """Return ``first, last, first+1, last-1, ...`` exactly once each."""

    if type(first_gate) is not int or type(last_gate) is not int:
        raise ValueError("gate bounds must be integers")
    if first_gate > last_gate:
        raise ValueError("first gate must not exceed last gate")
    order: list[int] = []
    low = first_gate
    high = last_gate
    while low <= high:
        order.append(low)
        if high != low:
            order.append(high)
        low += 1
        high -= 1
    return order


def _relative_artifact_path(target: Path, wrapper_path: Path) -> str:
    relative = os.path.relpath(target.resolve(), wrapper_path.parent.resolve())
    return Path(relative).as_posix()


def _require_relative_path_text(value: object, field: str) -> str:
    if not isinstance(value, str) or not value:
        raise ValueError(f"{field} must be a nonempty relative path")
    path = Path(value)
    if path.is_absolute():
        raise ValueError(f"{field} must not contain an absolute path")
    return value


def _git_metadata(base: Path) -> dict[str, object]:
    try:
        commit = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=base,
            check=True,
            capture_output=True,
            text=True,
        ).stdout.strip()
        dirty = bool(
            subprocess.run(
                ["git", "status", "--porcelain"],
                cwd=base,
                check=True,
                capture_output=True,
                text=True,
            ).stdout
        )
    except (OSError, subprocess.CalledProcessError):
        commit = None
        dirty = None
    return {"git_commit": commit, "working_tree_dirty": dirty}


def _implementation_hashes(base: Path) -> dict[str, str]:
    names = (
        "automata.py",
        "transducer.py",
        "verify.py",
        "independent_check.py",
        "odd_core.py",
        "spine_cegis.py",
        "odd_suffix_cegis.py",
        "paired_gate_census.py",
    )
    return {name: _sha256_file(base / name) for name in names}


def _raw_implication_dict(item: LearnedImplication) -> dict[str, str]:
    return item.to_dict()


def _suffix_implication_dict(item: SuffixImplication) -> dict[str, str]:
    return item.to_dict()


def _ordered_raw_implications(
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


def _raw_implication_digest(implications: Iterable[LearnedImplication]) -> str:
    return _sha256_object(
        [_raw_implication_dict(item) for item in _ordered_raw_implications(implications)]
    )


def _trace_digest(items: Sequence[dict[str, str]]) -> str:
    return _sha256_object(list(items))


def _baseline_identity(bank_path: Path, wrapper_path: Path) -> dict[str, object]:
    bank = load_implication_bank(bank_path)
    for implication in bank.implications:
        if not _is_direct_shortcut_pair(
            implication.input_word, implication.output_word
        ):
            raise ValueError("baseline implication fails direct shortcut arithmetic")
    translated = translate_shortcut_implication_bank(bank_path)
    for implication in translated.implications:
        if not _is_direct_suffix_pair(
            implication.input_suffix, implication.output_suffix
        ):
            raise ValueError("normalized baseline fails direct odd arithmetic")
    normalized = translated.provenance
    raw_bank = json.loads(bank_path.read_text(encoding="utf-8"))
    source = raw_bank["source"]
    return {
        "shortcut_bank_path": _relative_artifact_path(bank_path, wrapper_path),
        "bank_file_sha256": bank.provenance["bank_file_sha256"],
        "bank_payload_sha256": bank.bank_sha256,
        "bank_schema": BANK_SCHEMA,
        "semantics": BANK_SEMANTICS,
        "source_checkpoint_sha256": bank.provenance[
            "source_checkpoint_sha256"
        ],
        "source_checkpoint_schema": bank.provenance[
            "source_checkpoint_schema"
        ],
        "source_logical_signature": bank.provenance[
            "source_logical_signature"
        ],
        "source_status": bank.provenance["source_status"],
        "source_locally_learned_implications": source[
            "locally_learned_implications"
        ],
        "source_inherited_imported_implications": source[
            "inherited_imported_implications"
        ],
        "raw_implication_count": len(bank.implications),
        "raw_implications_sha256": _raw_implication_digest(bank.implications),
        "suffix_normalization": normalized["normalization"],
        "suffix_digest_serialization": NORMALIZED_DIGEST_SERIALIZATION,
        "suffix_implication_count": len(translated.implications),
        "suffix_implications_sha256": suffix_implication_digest(
            translated.implications
        ),
        "normalization_tautologies_skipped": normalized[
            "tautologies_skipped"
        ],
        "normalization_duplicates_skipped": normalized[
            "duplicates_skipped"
        ],
        "normalization_inputs_with_low_zeros": normalized[
            "inputs_with_low_zeros"
        ],
        "normalization_outputs_with_low_zeros": normalized[
            "outputs_with_low_zeros"
        ],
        "normalization_outputs_with_multiple_low_zeros": normalized[
            "outputs_with_multiple_low_zeros"
        ],
    }


def _direct_odd_map(value: int) -> int:
    result = 3 * value + 1
    while result % 2 == 0:
        result //= 2
    return result


def _is_direct_shortcut_pair(input_word: Word, output_word: Word) -> bool:
    source = decode_lsd(input_word)
    expected = source // 2 if source % 2 == 0 else (3 * source + 1) // 2
    return decode_lsd(output_word) == expected


def _is_direct_suffix_pair(input_suffix: Word, output_suffix: Word) -> bool:
    source = decode_lsd((1,) + input_suffix)
    return decode_lsd((1,) + output_suffix) == _direct_odd_map(source)


def _validate_census_parameters(
    *,
    suffix_state_count: int,
    raw_state_count: int,
    first_suffix_gate: int,
    last_suffix_gate: int,
    solver_seed: int,
    model_quota: int,
    watchdog_seconds: float,
    workers: int,
) -> None:
    if type(suffix_state_count) is not int or suffix_state_count < 3:
        raise ValueError("suffix_state_count must be an integer at least 3")
    if type(raw_state_count) is not int or raw_state_count != suffix_state_count + 1:
        raise ValueError("raw_state_count must equal suffix_state_count + 1")
    if (
        type(first_suffix_gate) is not int
        or type(last_suffix_gate) is not int
        or not 2 <= first_suffix_gate <= last_suffix_gate < suffix_state_count
    ):
        raise ValueError("suffix gate range must lie in [2, suffix_state_count)")
    if last_suffix_gate + 1 >= raw_state_count:
        raise ValueError("paired raw gate lies outside raw_state_count")
    if type(solver_seed) is not int or solver_seed < 0:
        raise ValueError("solver_seed must be a nonnegative integer")
    if type(model_quota) is not int or model_quota < 1:
        raise ValueError("model_quota must be a positive integer")
    if (
        isinstance(watchdog_seconds, bool)
        or not isinstance(watchdog_seconds, (int, float))
        or not math.isfinite(float(watchdog_seconds))
        or watchdog_seconds <= 0
    ):
        raise ValueError("watchdog_seconds must be finite and positive")
    if type(workers) is not int or workers < 1:
        raise ValueError("workers must be a positive integer")


def _plan(
    *,
    suffix_state_count: int,
    raw_state_count: int,
    first_suffix_gate: int,
    last_suffix_gate: int,
    solver_seed: int,
    model_quota: int,
    watchdog_seconds: float,
    workers: int,
) -> dict[str, object]:
    schedule = outside_in_schedule(first_suffix_gate, last_suffix_gate)
    tasks: list[dict[str, object]] = []
    for suffix_gate in schedule:
        pair_index = schedule.index(suffix_gate)
        for lane, gate in (("suffix", suffix_gate), ("raw", suffix_gate + 1)):
            task_index = 2 * pair_index + int(lane == "raw")
            tasks.append(
                {
                    "partition_id": (
                        f"suffix-q{suffix_state_count}-g{suffix_gate:03d}"
                        if lane == "suffix"
                        else f"raw-q{raw_state_count}-g{gate:03d}"
                    ),
                    "task_index": task_index,
                    "lane": lane,
                    "suffix_gate": suffix_gate,
                    "gate": gate,
                    "state_count": (
                        suffix_state_count if lane == "suffix" else raw_state_count
                    ),
                }
            )
    return {
        "generation": 0,
        "fresh_partitions": True,
        "pair_rule": "raw_gate = suffix_gate + 1",
        "suffix_state_count": suffix_state_count,
        "raw_state_count": raw_state_count,
        "first_suffix_gate": first_suffix_gate,
        "last_suffix_gate": last_suffix_gate,
        "pair_count": len(schedule),
        "partition_count": len(tasks),
        "outside_in_suffix_gate_order": schedule,
        "tasks": tasks,
        "solver_seed": solver_seed,
        "model_quota_per_partition": model_quota,
        "watchdog_seconds_per_partition": float(watchdog_seconds),
        "worker_count": workers,
        "z3_threads_per_partition": 1,
        "python_hash_seed_for_workers": "0",
        "cross_gate_clause_policy": "generation_barrier_only",
        "source_conclusion_policy": "never_import",
        "exact_verification_atomic": True,
    }


def _timeout_reason(reason: str) -> bool:
    lowered = reason.lower()
    return "timeout" in lowered or "canceled" in lowered


def _word_pair_key(item: LearnedImplication | SuffixImplication) -> tuple[Word, Word]:
    if isinstance(item, LearnedImplication):
        return item.input_word, item.output_word
    return item.input_suffix, item.output_suffix


def _raw_batch(candidate: DFA) -> tuple[list[LearnedImplication], dict[str, int]]:
    machine = shortcut_transducer()
    relation = terminal_relation(candidate, machine, with_witnesses=True)
    gate = next(iter(candidate.accepting))
    edges = sorted(
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
    implications: list[LearnedImplication] = []
    for source, target in edges:
        input_word = relation.witnesses[(source, target)]
        output_word = machine.transduce(input_word)
        if candidate.run(input_word) != source or candidate.run(output_word) != target:
            raise AssertionError("raw relation witness is internally inconsistent")
        implications.append(LearnedImplication(input_word, output_word))
    lengths = [len(item.input_word) for item in implications]
    return implications, {
        "relation_edges": len(relation.edges),
        "product_states": relation.product_states,
        "violating_endpoint_pairs": len(edges),
        "new_implications": len(implications),
        "shortest_witness_length": min(lengths),
        "longest_witness_length": max(lengths),
    }


def _suffix_batch(
    suffix_candidate: DFA, gate: int
) -> tuple[list[SuffixImplication], dict[str, int]]:
    machine = odd_core_transducer(1)
    odd_candidate = suffix_to_odd_dfa(suffix_candidate)
    relation = terminal_relation(odd_candidate, machine, with_witnesses=True)
    source_gate = 2 + gate
    edges = sorted(
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
    implications: list[SuffixImplication] = []
    for source, target in edges:
        input_full = relation.witnesses[(source, target)]
        output_full = machine.transduce(input_full)
        if not input_full or input_full[0] != 1:
            raise AssertionError("accepted odd relation witness is not odd")
        if not output_full or output_full[0] != 1:
            raise AssertionError("odd transducer produced a non-odd output")
        input_suffix = input_full[1:]
        output_suffix = output_full[1:]
        if suffix_candidate.run(input_suffix) != gate:
            raise AssertionError("suffix input witness does not reach its gate")
        if suffix_candidate.run(output_suffix) == gate:
            raise AssertionError("suffix output witness unexpectedly reaches its gate")
        implications.append(SuffixImplication(input_suffix, output_suffix))
    lengths = [1 + len(item.input_suffix) for item in implications]
    return implications, {
        "relation_edges": len(relation.edges),
        "product_states": relation.product_states,
        "violating_endpoint_pairs": len(edges),
        "new_implications": len(implications),
        "shortest_witness_length": min(lengths),
        "longest_witness_length": max(lengths),
    }


def _require_primary_preimage_agreement(
    candidate: DFA,
    machine,
    primary,
    *,
    forbidden_words: Sequence[Sequence[int] | str] = ("1", "01"),
) -> None:
    """Cross-check the endpoint verifier through the regular-preimage route."""

    independent = verify_candidate_via_preimage(
        candidate,
        machine,
        forbidden_words=forbidden_words,
    )
    if (
        independent.valid != primary.valid
        or independent.reason != primary.reason
        or independent.accepted_witness != primary.accepted_witness
        or independent.closure_input != primary.closure_input
        or independent.closure_output != primary.closure_output
    ):
        raise ValueError("primary and preimage candidate verifiers disagree")


def _classification(status: str, models_checked: int) -> tuple[str, bool]:
    if status == "verified_candidate":
        return "verified_candidate", False
    if status == "model_limit":
        return "bounded_model_quota", True
    if status in {"time_limit", "solver_unknown"} and models_checked == 0:
        return "zero_model_stall", True
    if status in {"time_limit", "solver_unknown"}:
        return "bounded_incomplete", True
    if status == "solver_unsat":
        return "solver_unsat_without_independent_proof", True
    raise ValueError(f"unknown partition status: {status}")


def _partition_semantic_view(partition: dict[str, object]) -> dict[str, object]:
    return {
        key: partition[key]
        for key in (
            "partition_id",
            "task_index",
            "lane",
            "suffix_gate",
            "gate",
            "state_count",
            "solver_seed",
            "model_quota",
            "watchdog_seconds",
            "status",
            "classification",
            "solver_reason",
            "bounded_or_incomplete",
            "models_checked",
            "batches",
            "imported_implication_count",
            "imported_implications_sha256",
            "local_implication_count",
            "local_implications_sha256",
            "local_implications",
            "enforced_implication_count",
            "model_records",
        )
    }


def _seal_partition(partition: dict[str, object]) -> dict[str, object]:
    sealed = dict(partition)
    sealed["semantic_sha256"] = _sha256_object(_partition_semantic_view(sealed))
    unsigned = dict(sealed)
    unsigned.pop("payload_sha256", None)
    sealed["payload_sha256"] = _sha256_object(unsigned)
    return sealed


def _worker(task: dict[str, object]) -> dict[str, object]:
    """Run one fresh partition and return compact, fully replayable evidence."""

    started = time.monotonic()
    lane = str(task["lane"])
    gate = int(task["gate"])
    state_count = int(task["state_count"])
    seed = int(task["solver_seed"])
    quota = int(task["model_quota"])
    watchdog = float(task["watchdog_seconds"])
    bank_path = Path(str(task["bank_path"]))

    if lane == "raw":
        bank = load_implication_bank(bank_path)
        imported: list[LearnedImplication | SuffixImplication] = list(
            bank.implications
        )
        imported_digest = _raw_implication_digest(bank.implications)
        config = SpineSearchConfig(
            state_count=state_count,
            gate=gate,
            force_zero_loop=True,
            force_11_prefix=True,
            solver_seed=seed,
        )
        encoding = SpineEncoding(config)
    elif lane == "suffix":
        translated = translate_shortcut_implication_bank(bank_path)
        imported = list(translated.implications)
        imported_digest = suffix_implication_digest(translated.implications)
        config = OddSuffixSearchConfig(
            state_count=state_count,
            gate=gate,
            odd_offset=1,
            solver_seed=seed,
        )
        encoding = OddSuffixEncoding(config)
    else:
        raise ValueError(f"unknown lane: {lane}")

    # Both encodings build one LSD-prefix trie for a batch.  Keeping the
    # frozen bank in a single batch is especially important for the q=71/72
    # wave: it avoids rebuilding the same long Select prefixes 213 times in
    # every fresh worker without changing a single asserted clause.
    encoding.add_implications_batch(imported)
    encoding.solver.set(threads=1)
    setup_seconds = time.monotonic() - started

    known = {_word_pair_key(item) for item in imported}
    local: list[LearnedImplication | SuffixImplication] = []
    records: list[dict[str, object]] = []
    status: str
    solver_reason: str | None = None

    while True:
        if len(records) >= quota:
            status = "model_limit"
            break
        elapsed = time.monotonic() - started
        remaining = watchdog - elapsed
        if remaining <= 0:
            status = "time_limit"
            solver_reason = "watchdog_elapsed_before_solver_check"
            break
        encoding.solver.set(timeout=max(1, int(remaining * 1000)))
        solver_status = encoding.solver.check()
        if solver_status == encoding.z3.unsat:
            status = "solver_unsat"
            break
        if solver_status != encoding.z3.sat:
            solver_reason = encoding.solver.reason_unknown()
            status = (
                "time_limit"
                if _timeout_reason(solver_reason)
                else "solver_unknown"
            )
            break

        candidate = encoding.extract_candidate(encoding.solver.model())
        model_number = len(records) + 1
        if lane == "raw":
            verification = verify_candidate(candidate, shortcut_transducer())
            lift_verification = None
        else:
            odd_candidate = suffix_to_odd_dfa(candidate)
            verification = verify_candidate(
                odd_candidate,
                odd_core_transducer(1),
                forbidden_words=("1",),
            )
            lifted = lift_odd_suffix_dfa_to_shortcut(candidate)
            lift_result = verify_candidate(lifted, shortcut_transducer())
            if verification.valid and not lift_result.valid:
                raise AssertionError(
                    "odd verifier accepted a candidate rejected by its raw lift"
                )
            lift_verification = lift_result.to_dict()

        record: dict[str, object] = {
            "model_number": model_number,
            "candidate": candidate.to_dict(),
            "verification": verification.to_dict(),
            "lift_verification": lift_verification,
            "batch": None,
        }
        records.append(record)
        if verification.valid:
            status = "verified_candidate"
            break
        if (
            verification.reason != "language is not forward invariant"
            or verification.closure_input is None
            or verification.closure_output is None
        ):
            raise AssertionError(
                "normal-form model failed for a reason other than closure: "
                f"{verification.reason}"
            )

        if lane == "raw":
            batch, metrics = _raw_batch(candidate)
            primary = LearnedImplication(
                verification.closure_input,
                verification.closure_output,
            )
        else:
            batch, metrics = _suffix_batch(candidate, gate)
            primary = SuffixImplication(
                verification.closure_input[1:],
                verification.closure_output[1:],
            )
        if not batch or _word_pair_key(primary) not in {
            _word_pair_key(item) for item in batch
        }:
            raise AssertionError("primary closure witness is absent from exact batch")
        offset = len(local)
        for implication in batch:
            key = _word_pair_key(implication)
            if key in known:
                raise AssertionError("solver repeated an enforced implication")
            known.add(key)
            local.append(implication)
        encoding.add_implications_batch(batch)
        record["batch"] = {
            **metrics,
            "local_offset": offset,
        }

    if lane == "raw":
        local_dicts = [
            _raw_implication_dict(item)
            for item in local
            if isinstance(item, LearnedImplication)
        ]
    else:
        local_dicts = [
            _suffix_implication_dict(item)
            for item in local
            if isinstance(item, SuffixImplication)
        ]
    if len(local_dicts) != len(local):
        raise AssertionError("partition mixed implication representations")
    classification, bounded = _classification(status, len(records))
    partition: dict[str, object] = {
        "partition_id": task["partition_id"],
        "task_index": task["task_index"],
        "lane": lane,
        "suffix_gate": task["suffix_gate"],
        "gate": gate,
        "state_count": state_count,
        "solver_seed": seed,
        "model_quota": quota,
        "watchdog_seconds": watchdog,
        "status": status,
        "classification": classification,
        "solver_reason": solver_reason,
        "bounded_or_incomplete": bounded,
        "models_checked": len(records),
        "batches": sum(record["batch"] is not None for record in records),
        "imported_implication_count": len(imported),
        "imported_implications_sha256": imported_digest,
        "local_implication_count": len(local_dicts),
        "local_implications_sha256": _trace_digest(local_dicts),
        "local_implications": local_dicts,
        "enforced_implication_count": len(imported) + len(local_dicts),
        "model_records": records,
        "setup_seconds": round(setup_seconds, 6),
        "external_wall_seconds": round(time.monotonic() - started, 6),
    }
    return _seal_partition(partition)


def _aggregate(
    partitions: Sequence[dict[str, object]], expected: int
) -> dict[str, object]:
    statuses = Counter(str(item["status"]) for item in partitions)
    classes = Counter(str(item["classification"]) for item in partitions)
    return {
        "expected_partitions": expected,
        "completed_partitions": len(partitions),
        "models_checked": sum(int(item["models_checked"]) for item in partitions),
        "local_implications": sum(
            int(item["local_implication_count"]) for item in partitions
        ),
        "status_counts": dict(sorted(statuses.items())),
        "classification_counts": dict(sorted(classes.items())),
        "zero_model_stalls": classes.get("zero_model_stall", 0),
        "verified_candidates": classes.get("verified_candidate", 0),
    }


def _wrapper_semantic_view(wrapper: dict[str, object]) -> dict[str, object]:
    baseline = dict(wrapper["baseline"])
    baseline.pop("shortcut_bank_path", None)
    baseline.pop("bank_file_sha256", None)
    return {
        "schema": wrapper["schema"],
        "program": wrapper["program"],
        "status": wrapper["status"],
        "plan": wrapper["plan"],
        "plan_sha256": wrapper["plan_sha256"],
        "baseline": baseline,
        "partition_semantic_sha256": [
            item["semantic_sha256"] for item in wrapper["partitions"]
        ],
        "aggregate": wrapper["aggregate"],
        "failure": wrapper["failure"],
    }


def _seal_wrapper(wrapper: dict[str, object]) -> dict[str, object]:
    sealed = dict(wrapper)
    sealed["semantic_sha256"] = _sha256_object(_wrapper_semantic_view(sealed))
    unsigned = dict(sealed)
    unsigned.pop("payload_sha256", None)
    sealed["payload_sha256"] = _sha256_object(unsigned)
    return sealed


def _write_wrapper(path: Path, wrapper: dict[str, object]) -> dict[str, object]:
    partitions = sorted(wrapper["partitions"], key=lambda item: item["task_index"])
    updated = {
        **wrapper,
        "partitions": partitions,
        "aggregate": _aggregate(partitions, int(wrapper["plan"]["partition_count"])),
    }
    sealed = _seal_wrapper(updated)
    _atomic_json_write(path, sealed)
    return sealed


def run_census(
    *,
    bank_path: Path,
    output_path: Path,
    suffix_state_count: int = 71,
    raw_state_count: int = 72,
    first_suffix_gate: int = 2,
    last_suffix_gate: int = 70,
    solver_seed: int = 0,
    model_quota: int = 1,
    watchdog_seconds: float = 10.0,
    workers: int | None = None,
) -> dict[str, object]:
    """Run one fresh generation-barrier census and atomically write its wrapper."""

    if workers is None:
        workers = min(8, os.cpu_count() or 1)
    _validate_census_parameters(
        suffix_state_count=suffix_state_count,
        raw_state_count=raw_state_count,
        first_suffix_gate=first_suffix_gate,
        last_suffix_gate=last_suffix_gate,
        solver_seed=solver_seed,
        model_quota=model_quota,
        watchdog_seconds=watchdog_seconds,
        workers=workers,
    )
    bank_path = bank_path.resolve()
    output_path = output_path.resolve()
    if output_path == bank_path:
        raise ValueError("census output must not overwrite the shortcut bank")
    if not bank_path.is_file():
        raise ValueError(f"shortcut bank does not exist: {bank_path}")
    base = Path(__file__).resolve().parent
    plan = _plan(
        suffix_state_count=suffix_state_count,
        raw_state_count=raw_state_count,
        first_suffix_gate=first_suffix_gate,
        last_suffix_gate=last_suffix_gate,
        solver_seed=solver_seed,
        model_quota=model_quota,
        watchdog_seconds=watchdog_seconds,
        workers=workers,
    )
    # Force the optional dependency check before creating a "running" artifact.
    from spine_cegis import _require_z3

    z3 = _require_z3()
    environment = {
        "python": platform.python_version(),
        "platform": platform.platform(),
        "z3": z3.get_version_string(),
        "python_hash_seed_for_workers": "0",
        "logical_processors": os.cpu_count(),
        "implementation_sha256": _implementation_hashes(base),
        **_git_metadata(base),
    }
    wrapper: dict[str, object] = {
        "schema": SCHEMA,
        "program": PROGRAM,
        "status": "running",
        "disclaimer": INCOMPLETE_DISCLAIMER,
        "plan": plan,
        "plan_sha256": _sha256_object(plan),
        "baseline": _baseline_identity(bank_path, output_path),
        "environment": environment,
        "partitions": [],
        "aggregate": _aggregate([], int(plan["partition_count"])),
        "failure": None,
    }
    wrapper = _write_wrapper(output_path, wrapper)

    worker_tasks = []
    for task in plan["tasks"]:
        worker_tasks.append(
            {
                **task,
                "solver_seed": solver_seed,
                "model_quota": model_quota,
                "watchdog_seconds": float(watchdog_seconds),
                "bank_path": str(bank_path),
            }
        )

    # ``spawn``-based workers read this before their interpreter initializes.
    os.environ["PYTHONHASHSEED"] = "0"
    try:
        with ProcessPoolExecutor(max_workers=workers) as executor:
            futures = {executor.submit(_worker, task): task for task in worker_tasks}
            for future in as_completed(futures):
                task = futures[future]
                try:
                    partition = future.result()
                except BaseException as exc:
                    for pending in futures:
                        pending.cancel()
                    wrapper = {
                        **wrapper,
                        "status": "failed",
                        "failure": {
                            "partition_id": task["partition_id"],
                            "error_type": type(exc).__name__,
                            "error_message": str(exc),
                        },
                    }
                    _write_wrapper(output_path, wrapper)
                    raise
                wrapper = {
                    **wrapper,
                    "partitions": [*wrapper["partitions"], partition],
                }
                wrapper = _write_wrapper(output_path, wrapper)
    except KeyboardInterrupt:
        wrapper = {
            **wrapper,
            "status": "failed",
            "failure": {
                "partition_id": None,
                "error_type": "KeyboardInterrupt",
                "error_message": "census interrupted",
            },
        }
        _write_wrapper(output_path, wrapper)
        raise

    wrapper = {**wrapper, "status": "complete", "failure": None}
    return _write_wrapper(output_path, wrapper)


def _require_exact_fields(raw: object, fields: set[str], label: str) -> dict[str, object]:
    if not isinstance(raw, dict) or set(raw) != fields:
        raise ValueError(f"{label} fields are malformed")
    return raw


def _nonnegative_int(value: object, field: str) -> int:
    if type(value) is not int or value < 0:
        raise ValueError(f"{field} must be a nonnegative integer")
    return value


def _positive_int(value: object, field: str) -> int:
    result = _nonnegative_int(value, field)
    if result == 0:
        raise ValueError(f"{field} must be positive")
    return result


def _finite_nonnegative(value: object, field: str) -> float:
    if (
        isinstance(value, bool)
        or not isinstance(value, (int, float))
        or not math.isfinite(float(value))
        or value < 0
    ):
        raise ValueError(f"{field} must be finite and nonnegative")
    return float(value)


def _parse_raw_local(raw: object) -> list[LearnedImplication]:
    if not isinstance(raw, list):
        raise ValueError("raw local implications must be a list")
    parsed: list[LearnedImplication] = []
    seen: set[tuple[Word, Word]] = set()
    machine = shortcut_transducer()
    for item in raw:
        data = _require_exact_fields(
            item, {"input_lsd", "output_lsd"}, "raw local implication"
        )
        for field in ("input_lsd", "output_lsd"):
            value = data[field]
            if not isinstance(value, str) or not value or any(c not in "01" for c in value):
                raise ValueError(f"raw {field} is not a canonical binary word")
        input_word = normalize_word(data["input_lsd"])
        output_word = normalize_word(data["output_lsd"])
        if not is_canonical_positive(input_word) or not is_canonical_positive(output_word):
            raise ValueError("raw local implication is noncanonical")
        if machine.transduce(input_word) != output_word:
            raise ValueError("raw local implication is not an exact T image")
        if not _is_direct_shortcut_pair(input_word, output_word):
            raise ValueError("raw local implication fails direct T arithmetic")
        key = (input_word, output_word)
        if key in seen:
            raise ValueError("raw local implications contain a duplicate")
        seen.add(key)
        parsed.append(LearnedImplication(input_word, output_word))
    return parsed


def _parse_suffix_local(raw: object) -> list[SuffixImplication]:
    if not isinstance(raw, list):
        raise ValueError("suffix local implications must be a list")
    parsed: list[SuffixImplication] = []
    seen: set[tuple[Word, Word]] = set()
    machine = odd_core_transducer(1)
    for item in raw:
        data = _require_exact_fields(
            item,
            {"input_suffix_lsd", "output_suffix_lsd"},
            "suffix local implication",
        )
        words: list[Word] = []
        for field in ("input_suffix_lsd", "output_suffix_lsd"):
            value = data[field]
            if not isinstance(value, str) or any(c not in "01" for c in value):
                raise ValueError(f"suffix {field} must be binary")
            word = normalize_word(value)
            if word and word[-1] != 1:
                raise ValueError(f"suffix {field} is not canonical")
            words.append(word)
        input_suffix, output_suffix = words
        exact = machine.transduce((1,) + input_suffix)
        if exact != (1,) + output_suffix:
            raise ValueError("suffix local implication is not an exact U image")
        if not _is_direct_suffix_pair(input_suffix, output_suffix):
            raise ValueError("suffix local implication fails direct U arithmetic")
        key = (input_suffix, output_suffix)
        if key in seen:
            raise ValueError("suffix local implications contain a duplicate")
        seen.add(key)
        parsed.append(SuffixImplication(input_suffix, output_suffix))
    return parsed


def _validate_raw_normal_form(candidate: DFA, state_count: int, gate: int) -> None:
    if candidate.state_count != state_count or candidate.start != 0:
        raise ValueError("raw candidate state accounting is invalid")
    if candidate.accepting != frozenset({gate}):
        raise ValueError("raw candidate accepting gate is invalid")
    if candidate.step(state_count - 1, 1) != gate:
        raise ValueError("raw candidate terminal gate transition is invalid")
    for state in range(state_count - 1):
        zero = candidate.step(state, 0)
        one = candidate.step(state, 1)
        if zero > state + 1 or one > state + 1:
            raise ValueError("raw candidate violates upper-Hessenberg form")
        if zero != state + 1 and one != state + 1:
            raise ValueError("raw candidate does not realize the next spine state")
        if one == gate:
            raise ValueError("raw candidate reaches its gate too early")
    if candidate.step(0, 0) != 0 or candidate.step(0, 1) != 1:
        raise ValueError("raw candidate violates the forced zero loop")
    if candidate.step(1, 0) == 2 or candidate.step(1, 1) != 2:
        raise ValueError("raw candidate violates the forced 11 prefix")


def _validate_suffix_normal_form(candidate: DFA, state_count: int, gate: int) -> None:
    if candidate.state_count != state_count or candidate.start != 0:
        raise ValueError("suffix candidate state accounting is invalid")
    if candidate.accepting != frozenset({gate}):
        raise ValueError("suffix candidate accepting gate is invalid")
    if candidate.step(state_count - 1, 1) != gate:
        raise ValueError("suffix candidate terminal gate transition is invalid")
    for state in range(state_count - 1):
        zero = candidate.step(state, 0)
        one = candidate.step(state, 1)
        if zero > state + 1 or one > state + 1:
            raise ValueError("suffix candidate violates upper-Hessenberg form")
        if zero != state + 1 and one != state + 1:
            raise ValueError("suffix candidate does not realize the next spine state")
        if one == gate:
            raise ValueError("suffix candidate reaches its gate too early")
    if candidate.step(0, 1) != 1 or candidate.step(0, 0) == 1:
        raise ValueError("suffix candidate violates the forced first suffix bit")


def _candidate_enforces(
    candidate: DFA,
    gate: int,
    implications: Sequence[LearnedImplication | SuffixImplication],
) -> bool:
    for item in implications:
        source, target = _word_pair_key(item)
        if candidate.run(source) == gate and candidate.run(target) != gate:
            return False
    return True


def _validate_batch_metrics(
    stored: object,
    expected: dict[str, int],
    local_offset: int,
) -> dict[str, object]:
    data = _require_exact_fields(stored, BATCH_FIELDS, "model batch")
    if data != {**expected, "local_offset": local_offset}:
        raise ValueError("stored batch does not match exact relation recomputation")
    return data


def _validate_partition(
    raw: object,
    task: dict[str, object],
    baseline_raw: Sequence[LearnedImplication],
    baseline_suffix: Sequence[SuffixImplication],
    baseline: dict[str, object],
    plan: dict[str, object],
) -> dict[str, object]:
    data = _require_exact_fields(raw, PARTITION_FIELDS, "partition")
    for field in ("partition_id", "lane"):
        if data[field] != task[field]:
            raise ValueError(f"partition {field} does not match plan")
    for field in ("task_index", "suffix_gate", "gate", "state_count"):
        if type(data[field]) is not int or data[field] != task[field]:
            raise ValueError(f"partition {field} does not match plan")
    if data["solver_seed"] != plan["solver_seed"]:
        raise ValueError("partition solver seed does not match plan")
    if data["model_quota"] != plan["model_quota_per_partition"]:
        raise ValueError("partition model quota does not match plan")
    if data["watchdog_seconds"] != plan["watchdog_seconds_per_partition"]:
        raise ValueError("partition watchdog does not match plan")
    _finite_nonnegative(data["setup_seconds"], "partition setup_seconds")
    _finite_nonnegative(data["external_wall_seconds"], "partition external_wall_seconds")
    if data["setup_seconds"] > data["external_wall_seconds"]:
        raise ValueError("partition setup time exceeds external wall time")
    models_checked = _nonnegative_int(data["models_checked"], "models_checked")
    batches = _nonnegative_int(data["batches"], "batches")
    lane = str(data["lane"])
    gate = int(data["gate"])
    state_count = int(data["state_count"])
    if lane == "raw":
        baseline_items: Sequence[LearnedImplication | SuffixImplication] = baseline_raw
        local = _parse_raw_local(data["local_implications"])
        expected_import_count = baseline["raw_implication_count"]
        expected_import_digest = baseline["raw_implications_sha256"]
    elif lane == "suffix":
        baseline_items = baseline_suffix
        local = _parse_suffix_local(data["local_implications"])
        expected_import_count = baseline["suffix_implication_count"]
        expected_import_digest = baseline["suffix_implications_sha256"]
    else:
        raise ValueError("partition lane is invalid")
    if data["imported_implication_count"] != expected_import_count:
        raise ValueError("partition imported implication count is inconsistent")
    if data["imported_implications_sha256"] != expected_import_digest:
        raise ValueError("partition imported implication digest is inconsistent")
    local_dicts = [
        _raw_implication_dict(item)
        if isinstance(item, LearnedImplication)
        else _suffix_implication_dict(item)
        for item in local
    ]
    if data["local_implication_count"] != len(local):
        raise ValueError("partition local implication count is inconsistent")
    if data["local_implications_sha256"] != _trace_digest(local_dicts):
        raise ValueError("partition local implication digest is inconsistent")
    if data["enforced_implication_count"] != len(baseline_items) + len(local):
        raise ValueError("partition enforced implication count is inconsistent")
    if {_word_pair_key(item) for item in baseline_items} & {
        _word_pair_key(item) for item in local
    }:
        raise ValueError("partition local and imported implications overlap")

    records = data["model_records"]
    if not isinstance(records, list) or len(records) != models_checked:
        raise ValueError("partition model record count is inconsistent")
    local_cursor = 0
    observed_batches = 0
    prior: list[LearnedImplication | SuffixImplication] = list(baseline_items)
    valid_seen = False
    for index, raw_record in enumerate(records, start=1):
        record = _require_exact_fields(
            raw_record, MODEL_RECORD_FIELDS, "model record"
        )
        if record["model_number"] != index:
            raise ValueError("model numbers are not consecutive")
        if not isinstance(record["candidate"], dict):
            raise ValueError("model candidate is malformed")
        if set(record["candidate"]) != {
            "alphabet",
            "bit_order",
            "start",
            "transitions",
            "accepting",
        }:
            raise ValueError("model candidate fields are malformed")
        candidate = DFA.from_dict(record["candidate"])
        if candidate.to_dict() != record["candidate"]:
            raise ValueError("model candidate is not in canonical DFA form")
        if lane == "raw":
            _validate_raw_normal_form(candidate, state_count, gate)
            verification = verify_candidate(candidate, shortcut_transducer())
            _require_primary_preimage_agreement(
                candidate,
                shortcut_transducer(),
                verification,
            )
            expected_lift = None
        else:
            _validate_suffix_normal_form(candidate, state_count, gate)
            odd_candidate = suffix_to_odd_dfa(candidate)
            verification = verify_candidate(
                odd_candidate,
                odd_core_transducer(1),
                forbidden_words=("1",),
            )
            _require_primary_preimage_agreement(
                odd_candidate,
                odd_core_transducer(1),
                verification,
                forbidden_words=("1",),
            )
            lifted = lift_odd_suffix_dfa_to_shortcut(candidate)
            lift_primary = verify_candidate(lifted, shortcut_transducer())
            _require_primary_preimage_agreement(
                lifted,
                shortcut_transducer(),
                lift_primary,
            )
            expected_lift = lift_primary.to_dict()
            if verification.valid and not expected_lift["valid"]:
                raise ValueError("valid suffix candidate has an invalid raw lift")
        if record["verification"] != verification.to_dict():
            raise ValueError("stored verification disagrees with exact recomputation")
        if record["lift_verification"] != expected_lift:
            raise ValueError("stored lift verification disagrees with recomputation")
        if not _candidate_enforces(candidate, gate, prior):
            raise ValueError("model violates a previously enforced implication")
        if verification.valid:
            if record["batch"] is not None:
                raise ValueError("verified candidate must not have a rejection batch")
            valid_seen = True
            if index != len(records):
                raise ValueError("models appear after a verified candidate")
            continue
        if verification.reason != "language is not forward invariant":
            raise ValueError("normal-form candidate failed outside closure")
        if lane == "raw":
            expected_batch, metrics = _raw_batch(candidate)
        else:
            expected_batch, metrics = _suffix_batch(candidate, gate)
        end = local_cursor + len(expected_batch)
        if [_word_pair_key(item) for item in local[local_cursor:end]] != [
            _word_pair_key(item) for item in expected_batch
        ]:
            raise ValueError("local clauses disagree with exact batch recomputation")
        _validate_batch_metrics(record["batch"], metrics, local_cursor)
        prior.extend(expected_batch)
        local_cursor = end
        observed_batches += 1
    if local_cursor != len(local) or observed_batches != batches:
        raise ValueError("partition batches do not account for local implications")

    status = data["status"]
    if not isinstance(status, str):
        raise ValueError("partition status must be a string")
    expected_class, expected_bounded = _classification(status, models_checked)
    if data["classification"] != expected_class:
        raise ValueError("partition classification is inconsistent")
    if data["bounded_or_incomplete"] is not expected_bounded:
        raise ValueError("partition bounded flag is inconsistent")
    if status == "model_limit" and models_checked != data["model_quota"]:
        raise ValueError("model-limit partition did not attain its quota")
    if status == "verified_candidate" and not valid_seen:
        raise ValueError("verified status lacks a verified model")
    if status != "verified_candidate" and valid_seen:
        raise ValueError("verified model has a non-verified status")
    if status in {"solver_unsat", "model_limit", "verified_candidate"}:
        if data["solver_reason"] is not None:
            raise ValueError("terminal status has an unexpected solver reason")
    else:
        if not isinstance(data["solver_reason"], str) or not data["solver_reason"]:
            raise ValueError("bounded solver stop must have a nonempty reason")
        if models_checked >= data["model_quota"]:
            raise ValueError("bounded solver stop already attained its model quota")
    if not _is_sha256(data["semantic_sha256"]):
        raise ValueError("partition semantic digest is malformed")
    if data["semantic_sha256"] != _sha256_object(_partition_semantic_view(data)):
        raise ValueError("partition semantic digest mismatch")
    unsigned = dict(data)
    observed_payload = unsigned.pop("payload_sha256")
    if not _is_sha256(observed_payload) or observed_payload != _sha256_object(unsigned):
        raise ValueError("partition payload digest mismatch")
    return data


def _expected_baseline(
    wrapper_path: Path, stored: dict[str, object]
) -> tuple[dict[str, object], list[LearnedImplication], list[SuffixImplication]]:
    path_text = _require_relative_path_text(
        stored.get("shortcut_bank_path"), "baseline shortcut_bank_path"
    )
    bank_path = (wrapper_path.parent / path_text).resolve()
    if not bank_path.is_file():
        raise ValueError("baseline shortcut bank is unavailable")
    expected = _baseline_identity(bank_path, wrapper_path)
    if stored != expected:
        raise ValueError("baseline identity does not match the shortcut bank")
    bank = load_implication_bank(bank_path)
    translated = translate_shortcut_implication_bank(bank_path)
    return expected, list(bank.implications), list(translated.implications)


def _reject_nonfinite_json(token: str):
    raise ValueError(f"nonfinite JSON constant is forbidden: {token}")


def _reject_duplicate_json_keys(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON object key is forbidden: {key}")
        result[key] = value
    return result


def validate_census(path: Path) -> dict[str, object]:
    """Strictly validate a compact wrapper without instantiating Z3."""

    raw = json.loads(
        path.read_text(encoding="utf-8"),
        parse_constant=_reject_nonfinite_json,
        object_pairs_hook=_reject_duplicate_json_keys,
    )
    data = _require_exact_fields(raw, TOP_FIELDS, "census wrapper")
    if data["schema"] != SCHEMA or data["program"] != PROGRAM:
        raise ValueError("census schema or program mismatch")
    if data["status"] not in {"running", "complete", "failed"}:
        raise ValueError("census status is invalid")
    if data["disclaimer"] != INCOMPLETE_DISCLAIMER:
        raise ValueError("census disclaimer is invalid")
    plan = data["plan"]
    if not isinstance(plan, dict):
        raise ValueError("census plan must be an object")
    required_plan_fields = set(
        _plan(
            suffix_state_count=3,
            raw_state_count=4,
            first_suffix_gate=2,
            last_suffix_gate=2,
            solver_seed=0,
            model_quota=1,
            watchdog_seconds=1.0,
            workers=1,
        )
    )
    if set(plan) != required_plan_fields:
        raise ValueError("census plan fields are malformed")
    _validate_census_parameters(
        suffix_state_count=plan["suffix_state_count"],
        raw_state_count=plan["raw_state_count"],
        first_suffix_gate=plan["first_suffix_gate"],
        last_suffix_gate=plan["last_suffix_gate"],
        solver_seed=plan["solver_seed"],
        model_quota=plan["model_quota_per_partition"],
        watchdog_seconds=plan["watchdog_seconds_per_partition"],
        workers=plan["worker_count"],
    )
    expected_plan = _plan(
        suffix_state_count=plan["suffix_state_count"],
        raw_state_count=plan["raw_state_count"],
        first_suffix_gate=plan["first_suffix_gate"],
        last_suffix_gate=plan["last_suffix_gate"],
        solver_seed=plan["solver_seed"],
        model_quota=plan["model_quota_per_partition"],
        watchdog_seconds=plan["watchdog_seconds_per_partition"],
        workers=plan["worker_count"],
    )
    if plan != expected_plan:
        raise ValueError("census plan is not the canonical outside-in plan")
    if data["plan_sha256"] != _sha256_object(plan):
        raise ValueError("census plan digest mismatch")
    baseline = data["baseline"]
    if not isinstance(baseline, dict):
        raise ValueError("census baseline must be an object")
    _, raw_baseline, suffix_baseline = _expected_baseline(path, baseline)

    environment = data["environment"]
    environment_fields = {
        "python",
        "platform",
        "z3",
        "python_hash_seed_for_workers",
        "logical_processors",
        "implementation_sha256",
        "git_commit",
        "working_tree_dirty",
    }
    if not isinstance(environment, dict) or set(environment) != environment_fields:
        raise ValueError("census environment fields are malformed")
    if not all(
        isinstance(environment[field], str)
        for field in ("python", "platform", "z3", "python_hash_seed_for_workers")
    ):
        raise ValueError("census environment version strings are malformed")
    if environment["python_hash_seed_for_workers"] != "0":
        raise ValueError("census worker hash seed is invalid")
    if environment["logical_processors"] is not None and (
        type(environment["logical_processors"]) is not int
        or environment["logical_processors"] < 1
    ):
        raise ValueError("census logical processor count is invalid")
    hashes = environment["implementation_sha256"]
    if not isinstance(hashes, dict) or not hashes or any(
        not isinstance(name, str) or not _is_sha256(digest)
        for name, digest in hashes.items()
    ):
        raise ValueError("census implementation hashes are malformed")
    current_hashes = _implementation_hashes(Path(__file__).resolve().parent)
    if hashes != current_hashes:
        raise ValueError("census implementation hashes do not match current sources")
    if environment["git_commit"] is not None and not _is_sha256(
        environment["git_commit"]
    ):
        # Git SHA-1 remains common; accept its exact lowercase 40-hex form.
        commit = environment["git_commit"]
        if not (
            isinstance(commit, str)
            and len(commit) == 40
            and all(c in "0123456789abcdef" for c in commit)
        ):
            raise ValueError("census git commit is malformed")
    if environment["working_tree_dirty"] not in {None, True, False}:
        raise ValueError("census working-tree flag is invalid")

    tasks = plan["tasks"]
    if not isinstance(tasks, list):
        raise ValueError("census task list is malformed")
    task_by_id = {task["partition_id"]: task for task in tasks}
    if len(task_by_id) != len(tasks):
        raise ValueError("census plan repeats a partition")
    partitions = data["partitions"]
    if not isinstance(partitions, list):
        raise ValueError("census partitions must be a list")
    if [item.get("task_index") for item in partitions if isinstance(item, dict)] != sorted(
        item.get("task_index") for item in partitions if isinstance(item, dict)
    ):
        raise ValueError("census partitions are not in deterministic task order")
    seen: set[str] = set()
    validated: list[dict[str, object]] = []
    for partition in partitions:
        if not isinstance(partition, dict):
            raise ValueError("census contains a malformed partition")
        partition_id = partition.get("partition_id")
        if not isinstance(partition_id, str) or partition_id not in task_by_id:
            raise ValueError("census partition is absent from the plan")
        if partition_id in seen:
            raise ValueError("census repeats a partition result")
        seen.add(partition_id)
        validated.append(
            _validate_partition(
                partition,
                task_by_id[partition_id],
                raw_baseline,
                suffix_baseline,
                baseline,
                plan,
            )
        )
    if data["status"] == "complete" and len(validated) != len(tasks):
        raise ValueError("complete census is missing partitions")
    if data["status"] == "running" and data["failure"] is not None:
        raise ValueError("running census has failure metadata")
    if data["status"] == "failed":
        failure = data["failure"]
        if not isinstance(failure, dict) or set(failure) != {
            "partition_id",
            "error_type",
            "error_message",
        }:
            raise ValueError("failed census lacks strict failure metadata")
    elif data["failure"] is not None:
        raise ValueError("nonfailed census has failure metadata")
    expected_aggregate = _aggregate(validated, len(tasks))
    if data["aggregate"] != expected_aggregate:
        raise ValueError("census aggregate is inconsistent")
    if data["semantic_sha256"] != _sha256_object(_wrapper_semantic_view(data)):
        raise ValueError("census semantic digest mismatch")
    unsigned = dict(data)
    observed_payload = unsigned.pop("payload_sha256")
    if not _is_sha256(observed_payload) or observed_payload != _sha256_object(unsigned):
        raise ValueError("census payload digest mismatch")
    return {
        "valid": True,
        "schema": SCHEMA,
        "status": data["status"],
        "partitions_validated": len(validated),
        "models_reverified": sum(item["models_checked"] for item in validated),
        "local_implications_recomputed": sum(
            item["local_implication_count"] for item in validated
        ),
        "zero_model_stalls": expected_aggregate["zero_model_stalls"],
        "verified_candidates": expected_aggregate["verified_candidates"],
        "semantic_sha256": data["semantic_sha256"],
        "payload_sha256": data["payload_sha256"],
    }


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--validate", type=Path, metavar="WRAPPER")
    parser.add_argument("--bank", type=Path, default=DEFAULT_BANK)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--suffix-states", type=int, default=71)
    parser.add_argument("--raw-states", type=int, default=72)
    parser.add_argument("--first-suffix-gate", type=int, default=2)
    parser.add_argument("--last-suffix-gate", type=int, default=70)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--max-models", type=int, default=1)
    parser.add_argument("--watchdog", type=float, default=10.0)
    parser.add_argument("--workers", type=int)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    if args.validate is not None:
        if args.output is not None:
            raise SystemExit("--validate and --output are mutually exclusive")
        try:
            report = validate_census(args.validate.resolve())
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            print(
                json.dumps(
                    {"valid": False, "error": str(exc)},
                    sort_keys=True,
                    allow_nan=False,
                )
            )
            return 2
        print(json.dumps(report, indent=2, sort_keys=True, allow_nan=False))
        return 0
    if args.output is None:
        raise SystemExit("--output is required when running a census")
    try:
        result = run_census(
            bank_path=args.bank,
            output_path=args.output,
            suffix_state_count=args.suffix_states,
            raw_state_count=args.raw_states,
            first_suffix_gate=args.first_suffix_gate,
            last_suffix_gate=args.last_suffix_gate,
            solver_seed=args.seed,
            model_quota=args.max_models,
            watchdog_seconds=args.watchdog,
            workers=args.workers,
        )
    except RuntimeError as exc:
        print(json.dumps({"status": "missing_optional_dependency", "error": str(exc)}))
        return 2
    print(
        json.dumps(
            {
                "status": result["status"],
                "output": args.output.as_posix(),
                "aggregate": result["aggregate"],
                "semantic_sha256": result["semantic_sha256"],
                "payload_sha256": result["payload_sha256"],
            },
            indent=2,
            sort_keys=True,
            allow_nan=False,
        )
    )
    return 0 if result["status"] == "complete" else 1


if __name__ == "__main__":
    raise SystemExit(main())
