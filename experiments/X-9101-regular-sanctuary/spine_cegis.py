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
    models_checked_cumulative: int
    elapsed_seconds_cumulative: float
    batch_history: tuple[dict[str, int], ...]


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
    batch_history: Sequence[dict[str, int]],
    batches_before_run: int,
    resume_source: str | None,
    last_candidate: DFA | None,
    last_verification: VerificationResult | None,
    solver_reason: str | None = None,
) -> dict[str, object]:
    learned_list = list(learned)
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
        "models_checked_this_run": models_checked_this_run,
        "models_checked_cumulative": (
            models_checked_before_run + models_checked_this_run
        ),
        "elapsed_seconds": round(elapsed_seconds_this_run, 6),
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
    raw_items = data.get("learned_implications")
    if not isinstance(raw_items, list):
        raise ValueError("checkpoint has no learned implication list")

    machine = shortcut_transducer() if transducer is None else transducer
    learned: list[LearnedImplication] = []
    seen: set[tuple[Word, Word]] = set()
    for raw in raw_items:
        if not isinstance(raw, dict):
            raise ValueError("malformed checkpoint implication")
        input_word = _canonical_checkpoint_word(
            raw.get("input_lsd"), "input_lsd"
        )
        output_word = _canonical_checkpoint_word(
            raw.get("output_lsd"), "output_lsd"
        )
        if machine.transduce(input_word) != output_word:
            raise ValueError("checkpoint implication is not an exact T image")
        key = (input_word, output_word)
        if key in seen:
            raise ValueError("checkpoint contains a duplicate learned implication")
        seen.add(key)
        learned.append(LearnedImplication(input_word, output_word))

    declared_learned = _checkpoint_nonnegative_int(
        data, "learned_implications_cumulative"
    )
    if declared_learned != len(learned):
        raise ValueError("checkpoint learned implication count is inconsistent")

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
            raise ValueError("checkpoint batch gate disagrees with fixed partition")
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

    return LoadedCheckpoint(
        tuple(learned), models_checked, float(elapsed), tuple(batches)
    )


def load_checkpoint(
    path: Path, config: SpineSearchConfig, transducer=None
) -> list[LearnedImplication]:
    """Load validated learned obligations from a matching checkpoint."""

    return list(_load_checkpoint_state(path, config, transducer).learned)


def run_spine_cegis(
    config: SpineSearchConfig,
    *,
    checkpoint_path: Path | None = None,
    result_path: Path | None = None,
    resume_path: Path | None = None,
) -> dict[str, object]:
    """Run exact-oracle CEGIS within one declared spine/gate partition."""

    transducer = shortcut_transducer()
    encoding = SpineEncoding(config)
    loaded = (
        _load_checkpoint_state(resume_path, config, transducer)
        if resume_path is not None
        else LoadedCheckpoint((), 0, 0.0, ())
    )
    learned = list(loaded.learned)
    batch_history = list(loaded.batch_history)
    models_checked_before_run = loaded.models_checked_cumulative
    elapsed_seconds_before_run = loaded.elapsed_seconds_cumulative
    learned_before_run = len(learned)
    batches_before_run = len(batch_history)
    # Preserve the user-supplied path rather than embedding an environment-
    # specific absolute workspace path in a result intended for version control.
    resume_source = None if resume_path is None else resume_path.as_posix()
    learned_keys = {
        (item.input_word, item.output_word) for item in learned
    }
    for implication in learned:
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
            if key in learned_keys:
                raise AssertionError(
                    "exact relation repeated an already-enforced closure violation"
                )
            learned_keys.add(key)
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
        "--dry-diagnostic",
        action="store_true",
        help="run a five-state engine diagnostic, not a scientific search",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
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
        )
    except RuntimeError as exc:
        print(json.dumps({"status": "missing_optional_dependency", "error": str(exc)}))
        return 2
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["status"] in {"verified_candidate", "solver_unsat"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
