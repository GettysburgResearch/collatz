"""Symbolic closure of one forced minimum-length odd-suffix spine word.

Concrete CEGIS implications can always be dodged by changing which minimum
word reaches the accepting gate.  This module instead chooses one advancing
spine word *symbolically*, computes ``U`` of that entire word with a Boolean
ripple-carry circuit, and requires the image to return to the gate.

The output path does not need a costly symbolic array walk.  Exact-distance
constraints imply only two possibilities: an equal-length image advances at
every preterminal step, while a one-bit-longer image has exactly one stall and
otherwise advances.  Both are encoded with constant-state transition reads.

The constraint is necessary, not sufficient, for full forward invariance.
SAT models are therefore rechecked concretely and are not sanctuary
candidates unless the unchanged exact odd and shortcut-lift verifiers agree.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
import math
import os
import platform
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

from automata import DFA, Word, word_text
from odd_core import odd_core_transducer
from odd_suffix_cegis import (
    OddSuffixEncoding,
    OddSuffixSearchConfig,
    verify_suffix_candidate,
)


SCHEMA = "x-9101-symbolic-minimum-closure-v1"
PROGRAM = "symbolic-minimum-odd-suffix-audit"
DISCLAIMER = (
    "The symbolic minimum-length-image constraint is necessary but not "
    "sufficient for odd-core closure. SAT records are exactly rechecked "
    "countermodels, not sanctuaries. Solver UNSAT is not used as a proof "
    "artifact; gate 2 is supported separately by the carry-induction "
    "argument in L-9114."
)


@dataclass(frozen=True)
class SymbolicMinimumHandles:
    """Z3 handles exposed only for tests and diagnostic model inspection."""

    spine_bits: tuple[object, ...]
    product_bits: tuple[object, ...]
    carry_bits: tuple[object, ...]
    long_image: object
    stall_index: object


def _canonical_json_bytes(value: object) -> bytes:
    return json.dumps(
        value,
        ensure_ascii=True,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")


def _payload_digest(payload_without_digest: dict[str, object]) -> str:
    return hashlib.sha256(_canonical_json_bytes(payload_without_digest)).hexdigest()


def _strict_json_loads(raw: str) -> object:
    def reject_constant(value: str) -> object:
        raise ValueError(f"nonfinite JSON constant {value} is forbidden")

    def reject_duplicates(pairs: list[tuple[str, object]]) -> dict[str, object]:
        result: dict[str, object] = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"duplicate JSON key {key!r} is forbidden")
            result[key] = value
        return result

    return json.loads(
        raw,
        parse_constant=reject_constant,
        object_pairs_hook=reject_duplicates,
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


def _transition_for_symbol(encoding: OddSuffixEncoding, state: int, one):
    z3 = encoding.z3
    return z3.If(
        one,
        z3.Select(encoding.delta[1], state),
        z3.Select(encoding.delta[0], state),
    )


def add_symbolic_minimum_closure(
    encoding: OddSuffixEncoding,
    *,
    namespace: str = "symbolic_minimum",
) -> SymbolicMinimumHandles:
    """Add exact closure for one deterministically chosen advancing word.

    At state ``i < q-1`` choose spine bit 1 whenever its transition advances
    to ``i+1``; otherwise choose 0.  The normal form guarantees that the
    selected bit advances.  The full odd input bits are then

    ``1, c_0, ..., c_(q-2), 1``.

    Because ``c_0=1``, the full input is 3 modulo 4 and
    ``U(m)=(3m+1)/2``.  A Boolean full-adder computes ``3m+1=m+2m+1`` without
    a monolithic bit-vector multiplication.
    """

    if not namespace or any(character.isspace() for character in namespace):
        raise ValueError("namespace must be a nonempty whitespace-free string")
    z3 = encoding.z3
    q = encoding.config.state_count

    spine_bits: list[object] = []
    for state in range(q - 1):
        chosen = z3.Bool(f"{namespace}_spine_bit_{state}")
        encoding.solver.add(
            chosen == (z3.Select(encoding.delta[1], state) == state + 1)
        )
        spine_bits.append(chosen)

    # Full input bits b_0,...,b_q.  b_0 is the removed odd marker and b_q is
    # the canonical high bit appended after the q-1 advancing choices.
    input_bits = [z3.BoolVal(True), *spine_bits, z3.BoolVal(True)]

    # P = 3m+1 = m + 2m + 1.  P_0=0 and the carry into position one is 1.
    carry = z3.BoolVal(True)
    previous_input = input_bits[0]
    product_bits: list[object] = [z3.BoolVal(False)]
    carry_bits: list[object] = [carry]
    for position in range(1, q + 3):
        current_input = (
            input_bits[position]
            if position <= q
            else z3.BoolVal(False)
        )
        product_bit = z3.Bool(f"{namespace}_product_bit_{position}")
        next_carry = z3.Bool(f"{namespace}_carry_into_{position + 1}")
        encoding.solver.add(
            product_bit == z3.Xor(current_input, z3.Xor(previous_input, carry))
        )
        encoding.solver.add(
            next_carry
            == z3.Or(
                z3.And(current_input, previous_input),
                z3.And(current_input, carry),
                z3.And(previous_input, carry),
            )
        )
        product_bits.append(product_bit)
        carry_bits.append(next_carry)
        carry = next_carry
        previous_input = current_input

    # U bit k is P bit k+1.  Its low bit must be the odd marker.
    encoding.solver.add(product_bits[1])
    long_image = product_bits[q + 2]

    # Equal full length q+1: the suffix has q symbols.  Its first q-1
    # symbols must advance 0->1->...->q-1; the final high 1 reaches the gate.
    short_constraints = [z3.Not(long_image), product_bits[q + 1]]
    for state in range(q - 1):
        output_suffix_bit = product_bits[state + 2]
        short_constraints.append(
            _transition_for_symbol(encoding, state, output_suffix_bit)
            == state + 1
        )
    short_case = z3.And(*short_constraints)

    # One-bit-longer full image q+2: before the final high 1 there are q
    # transitions to cover graph distance q-1.  With every transition bounded
    # above by current+1, exactly one transition stalls and all others advance.
    stall = z3.Int(f"{namespace}_stall_index")
    long_constraints = [long_image, 0 <= stall, stall < q]
    for position in range(q):
        output_suffix_bit = product_bits[position + 2]
        cases = [
            z3.And(
                stall == position,
                _transition_for_symbol(encoding, position, output_suffix_bit)
                == position,
            )
        ]
        if position < q - 1:
            cases.append(
                z3.And(
                    stall > position,
                    _transition_for_symbol(
                        encoding, position, output_suffix_bit
                    )
                    == position + 1,
                )
            )
        if position > 0:
            cases.append(
                z3.And(
                    stall < position,
                    _transition_for_symbol(
                        encoding, position - 1, output_suffix_bit
                    )
                    == position,
                )
            )
        long_constraints.append(z3.Or(*cases))
    long_case = z3.And(*long_constraints)
    encoding.solver.add(z3.Or(short_case, long_case))

    return SymbolicMinimumHandles(
        tuple(spine_bits),
        tuple(product_bits),
        tuple(carry_bits),
        long_image,
        stall,
    )


def validate_suffix_normal_form(dfa: DFA, gate: int) -> None:
    """Validate exactly the syntactic constraints used by the encoding."""

    q = dfa.state_count
    if q < 3 or not 2 <= gate < q:
        raise ValueError("gate is outside the odd-suffix normal form")
    if dfa.start != 0 or dfa.accepting != frozenset({gate}):
        raise ValueError("DFA start or singleton gate is invalid")
    for state in range(q - 1):
        zero_target = dfa.step(state, 0)
        one_target = dfa.step(state, 1)
        if zero_target > state + 1 or one_target > state + 1:
            raise ValueError("transition violates the upper-Hessenberg bound")
        if state + 1 not in (zero_target, one_target):
            raise ValueError("state has no advancing transition")
        if one_target == gate:
            raise ValueError("an early one-transition enters the gate")
    if dfa.step(0, 1) != 1 or dfa.step(0, 0) == 1:
        raise ValueError("forced initial suffix transition is invalid")
    if dfa.step(q - 1, 1) != gate:
        raise ValueError("final canonical one does not enter the gate")


def chosen_advancing_suffix(dfa: DFA, gate: int) -> Word:
    """Return the concrete word represented by the symbolic spine choices."""

    validate_suffix_normal_form(dfa, gate)
    bits: list[int] = []
    for state in range(dfa.state_count - 1):
        bit = 1 if dfa.step(state, 1) == state + 1 else 0
        if dfa.step(state, bit) != state + 1:
            raise AssertionError("chosen symbolic spine bit does not advance")
        bits.append(bit)
    bits.append(1)
    suffix = tuple(bits)
    if dfa.run(suffix) != gate:
        raise AssertionError("chosen symbolic spine word does not reach the gate")
    return suffix


def _state_trace(dfa: DFA, word: Word) -> tuple[int, ...]:
    states = [dfa.start]
    state = dfa.start
    for bit in word:
        state = dfa.step(state, bit)
        states.append(state)
    return tuple(states)


def concrete_minimum_profile(dfa: DFA, gate: int) -> dict[str, object]:
    """Recompute the chosen input, exact U image, and distance profile."""

    suffix = chosen_advancing_suffix(dfa, gate)
    q = dfa.state_count
    full_input = (1,) + suffix
    full_output = odd_core_transducer(1).transduce(full_input)
    if full_output[0] != 1:
        raise AssertionError("fully accelerated odd image is not odd")
    output_suffix = full_output[1:]
    if len(full_output) not in (q + 1, q + 2):
        raise AssertionError("minimum image has an impossible bit length")
    trace = _state_trace(dfa, output_suffix)
    accepted = trace[-1] == gate

    path_class: str | None = None
    stall_index: int | None = None
    if accepted:
        if output_suffix[-1] != 1:
            raise AssertionError("accepted image suffix is not canonical")
        prefix_trace = trace[:-1]
        # prefix_trace includes the start and state before the final high one.
        if prefix_trace[-1] != q - 1:
            raise AssertionError("accepted image does not reach the final state")
        deltas = [
            prefix_trace[index + 1] - prefix_trace[index]
            for index in range(len(prefix_trace) - 1)
        ]
        if len(full_output) == q + 1:
            if deltas != [1] * (q - 1):
                raise AssertionError("equal-length image does not always advance")
            path_class = "equal_length_all_advance"
        else:
            if deltas.count(0) != 1 or any(delta != 1 for delta in deltas if delta):
                raise AssertionError("long image lacks the unique-stall profile")
            path_class = "one_bit_longer_one_stall"
            stall_index = deltas.index(0)

    return {
        "input_full_lsd": word_text(full_input),
        "input_suffix_lsd": word_text(suffix),
        "output_full_lsd": word_text(full_output),
        "output_suffix_lsd": word_text(output_suffix),
        "input_full_length": len(full_input),
        "output_full_length": len(full_output),
        "accepted_by_symbolic_constraint": accepted,
        "path_class": path_class,
        "stall_index": stall_index,
    }


def gate_two_carry_certificate(state_count: int) -> dict[str, object]:
    """Return the finite data underlying L-9114's carry induction."""

    if type(state_count) is not int or state_count < 3:
        raise ValueError("state_count must be an integer at least 3")
    q = state_count
    # The induction forces c_0=1 and c_i=0 for every i>=1 before meeting the
    # fixed final high bit.  Evaluating that word displays the terminal length
    # contradiction.  q=3 reaches the contradiction one carry earlier.
    suffix = (1,) + (0,) * (q - 2) + (1,)
    full_input = (1,) + suffix
    full_output = odd_core_transducer(1).transduce(full_input)
    return {
        "state_count": q,
        "gate": 2,
        "forced_spine_suffix_lsd": word_text(suffix),
        "forced_input_full_lsd": word_text(full_input),
        "forced_output_full_lsd": word_text(full_output),
        "forced_output_full_length": len(full_output),
        "short_case_first_output_suffix_bit": full_output[1],
        "induction_scope": (
            "q=3 contradicts the required post-stall advance directly; "
            "q>=4 forces c_2,...,c_(q-2)=0 and then removes the assumed top bit"
        ),
    }


def _verification_payload(result) -> dict[str, object]:
    return result.to_dict()


def _sat_record(encoding: OddSuffixEncoding) -> dict[str, object]:
    model = encoding.solver.model()
    candidate = encoding.extract_candidate(model)
    gate = encoding.config.gate
    profile = concrete_minimum_profile(candidate, gate)
    if not profile["accepted_by_symbolic_constraint"]:
        raise AssertionError("symbolic SAT model fails its concrete minimum image")
    odd_result, lift_result, _, _ = verify_suffix_candidate(candidate)
    return {
        "gate": gate,
        "constraint_status": "satisfiable_countermodel",
        "candidate": candidate.to_dict(),
        "minimum_profile": profile,
        "odd_exact_verification": _verification_payload(odd_result),
        "lift_exact_verification": _verification_payload(lift_result),
    }


def run_audit(
    *,
    state_count: int = 71,
    gate_min: int = 2,
    gate_max: int | None = None,
    solver_seed: int = 0,
    timeout_seconds: float = 10.0,
) -> dict[str, object]:
    """Audit the symbolic minimum-image condition over a gate interval."""

    if type(state_count) is not int or state_count < 3:
        raise ValueError("state_count must be an integer at least 3")
    if gate_max is None:
        gate_max = state_count - 1
    if (
        type(gate_min) is not int
        or type(gate_max) is not int
        or not 2 <= gate_min <= gate_max < state_count
    ):
        raise ValueError("gate interval is outside [2, state_count)")
    if type(solver_seed) is not int or solver_seed < 0:
        raise ValueError("solver_seed must be a nonnegative integer")
    if (
        isinstance(timeout_seconds, bool)
        or not isinstance(timeout_seconds, (int, float))
        or not math.isfinite(float(timeout_seconds))
        or timeout_seconds <= 0
    ):
        raise ValueError("timeout_seconds must be finite and positive")

    records: list[dict[str, object]] = []
    for gate in range(gate_min, gate_max + 1):
        encoding = OddSuffixEncoding(
            OddSuffixSearchConfig(
                state_count=state_count,
                gate=gate,
                solver_seed=solver_seed,
            )
        )
        add_symbolic_minimum_closure(encoding, namespace=f"minimum_g{gate}")
        encoding.solver.set(timeout=max(1, int(timeout_seconds * 1000)))
        status = encoding.solver.check()
        if status == encoding.z3.sat:
            records.append(_sat_record(encoding))
        elif status == encoding.z3.unsat:
            records.append(
                {
                    "gate": gate,
                    "constraint_status": "solver_unsat",
                    "independently_checkable_solver_proof_emitted": False,
                    "gate_two_carry_certificate": (
                        gate_two_carry_certificate(state_count)
                        if gate == 2
                        else None
                    ),
                }
            )
        else:
            records.append(
                {
                    "gate": gate,
                    "constraint_status": "solver_unknown",
                    "solver_reason": encoding.solver.reason_unknown(),
                }
            )

    status_counts: dict[str, int] = {}
    exact_valid = 0
    for record in records:
        status_text = str(record["constraint_status"])
        status_counts[status_text] = status_counts.get(status_text, 0) + 1
        if status_text == "satisfiable_countermodel":
            odd = record["odd_exact_verification"]
            lift = record["lift_exact_verification"]
            if isinstance(odd, dict) and isinstance(lift, dict):
                exact_valid += int(bool(odd.get("valid") and lift.get("valid")))

    payload: dict[str, object] = {
        "schema": SCHEMA,
        "program": PROGRAM,
        "scope": {
            "state_count": state_count,
            "gate_min": gate_min,
            "gate_max": gate_max,
            "gate_count": gate_max - gate_min + 1,
            "map": "fully_accelerated_odd_3n_plus_1",
            "bit_order": "lsd_first",
            "constraint": "one_symbolically_chosen_minimum_length_spine_image_is_accepted",
        },
        "solver": {
            "seed": solver_seed,
            "timeout_seconds_per_gate": float(timeout_seconds),
            "z3_version": importlib.metadata.version("z3-solver"),
        },
        "environment": {
            "python": platform.python_version(),
            "platform": platform.platform(),
        },
        "records": records,
        "aggregate": {
            "status_counts": dict(sorted(status_counts.items())),
            "exact_full_candidates": exact_valid,
        },
        "disclaimer": DISCLAIMER,
    }
    payload["payload_sha256"] = _payload_digest(payload)
    return payload


def validate_audit(payload: dict[str, object]) -> dict[str, object]:
    """Strictly reconstruct every SAT witness and every stable count."""

    root_fields = {
        "schema",
        "program",
        "scope",
        "solver",
        "environment",
        "records",
        "aggregate",
        "disclaimer",
        "payload_sha256",
    }
    if not isinstance(payload, dict) or set(payload) != root_fields:
        raise ValueError("symbolic minimum audit root is malformed")
    if payload["schema"] != SCHEMA or payload["program"] != PROGRAM:
        raise ValueError("symbolic minimum audit schema or program mismatch")
    digest = payload["payload_sha256"]
    if (
        not isinstance(digest, str)
        or len(digest) != 64
        or any(character not in "0123456789abcdef" for character in digest)
    ):
        raise ValueError("symbolic minimum audit digest is malformed")
    unsigned = dict(payload)
    del unsigned["payload_sha256"]
    if _payload_digest(unsigned) != digest:
        raise ValueError("symbolic minimum audit payload digest mismatch")
    if payload["disclaimer"] != DISCLAIMER:
        raise ValueError("symbolic minimum audit disclaimer mismatch")

    scope = payload["scope"]
    scope_fields = {
        "state_count",
        "gate_min",
        "gate_max",
        "gate_count",
        "map",
        "bit_order",
        "constraint",
    }
    if not isinstance(scope, dict) or set(scope) != scope_fields:
        raise ValueError("symbolic minimum audit scope is malformed")
    q = scope.get("state_count")
    gate_min = scope.get("gate_min")
    gate_max = scope.get("gate_max")
    gate_count = scope.get("gate_count")
    if (
        type(q) is not int
        or type(gate_min) is not int
        or type(gate_max) is not int
        or type(gate_count) is not int
        or q < 3
        or not 2 <= gate_min <= gate_max < q
        or gate_count != gate_max - gate_min + 1
    ):
        raise ValueError("symbolic minimum audit gate scope is inconsistent")
    if (
        scope["map"] != "fully_accelerated_odd_3n_plus_1"
        or scope["bit_order"] != "lsd_first"
        or scope["constraint"]
        != "one_symbolically_chosen_minimum_length_spine_image_is_accepted"
    ):
        raise ValueError("symbolic minimum audit semantics mismatch")

    solver = payload["solver"]
    if not isinstance(solver, dict) or set(solver) != {
        "seed",
        "timeout_seconds_per_gate",
        "z3_version",
    }:
        raise ValueError("symbolic minimum audit solver metadata is malformed")
    timeout = solver["timeout_seconds_per_gate"]
    if (
        type(solver["seed"]) is not int
        or solver["seed"] < 0
        or isinstance(timeout, bool)
        or not isinstance(timeout, (int, float))
        or not math.isfinite(float(timeout))
        or timeout <= 0
        or not isinstance(solver["z3_version"], str)
        or not solver["z3_version"]
    ):
        raise ValueError("symbolic minimum audit solver metadata is invalid")
    environment = payload["environment"]
    if (
        not isinstance(environment, dict)
        or set(environment) != {"python", "platform"}
        or not all(
            isinstance(environment[field], str) and environment[field]
            for field in environment
        )
    ):
        raise ValueError("symbolic minimum audit environment is malformed")

    raw_records = payload["records"]
    if not isinstance(raw_records, list) or len(raw_records) != gate_count:
        raise ValueError("symbolic minimum audit record count is inconsistent")
    expected_gates = list(range(gate_min, gate_max + 1))
    if [record.get("gate") for record in raw_records if isinstance(record, dict)] != expected_gates:
        raise ValueError("symbolic minimum audit gates are malformed or unordered")

    status_counts: dict[str, int] = {}
    exact_valid = 0
    for record in raw_records:
        if not isinstance(record, dict):
            raise ValueError("symbolic minimum audit record is malformed")
        gate = record["gate"]
        status = record.get("constraint_status")
        if not isinstance(status, str):
            raise ValueError("symbolic minimum audit status is malformed")
        status_counts[status] = status_counts.get(status, 0) + 1
        if status == "satisfiable_countermodel":
            expected_fields = {
                "gate",
                "constraint_status",
                "candidate",
                "minimum_profile",
                "odd_exact_verification",
                "lift_exact_verification",
            }
            if set(record) != expected_fields:
                raise ValueError("symbolic minimum SAT record is malformed")
            candidate_data = record["candidate"]
            candidate_fields = {
                "alphabet",
                "bit_order",
                "start",
                "transitions",
                "accepting",
            }
            if not isinstance(candidate_data, dict) or set(candidate_data) != candidate_fields:
                raise ValueError("symbolic minimum candidate fields are malformed")
            candidate = DFA.from_dict(candidate_data)
            if candidate.to_dict() != candidate_data:
                raise ValueError("symbolic minimum candidate is not in canonical DFA form")
            if candidate.state_count != q:
                raise ValueError(
                    "symbolic minimum candidate state count differs from scope"
                )
            profile = concrete_minimum_profile(candidate, gate)
            if profile != record["minimum_profile"]:
                raise ValueError("symbolic minimum concrete profile mismatch")
            odd_result, lift_result, _, _ = verify_suffix_candidate(candidate)
            if odd_result.to_dict() != record["odd_exact_verification"]:
                raise ValueError("symbolic minimum odd verification mismatch")
            if lift_result.to_dict() != record["lift_exact_verification"]:
                raise ValueError("symbolic minimum lift verification mismatch")
            exact_valid += int(odd_result.valid and lift_result.valid)
        elif status == "solver_unsat":
            expected_fields = {
                "gate",
                "constraint_status",
                "independently_checkable_solver_proof_emitted",
                "gate_two_carry_certificate",
            }
            if set(record) != expected_fields:
                raise ValueError("symbolic minimum UNSAT record is malformed")
            if record["independently_checkable_solver_proof_emitted"] is not False:
                raise ValueError("symbolic minimum UNSAT proof flag is invalid")
            if gate == 2:
                if record["gate_two_carry_certificate"] != gate_two_carry_certificate(q):
                    raise ValueError("gate-two carry certificate mismatch")
            elif record["gate_two_carry_certificate"] is not None:
                raise ValueError("unexpected gate-two certificate")
        elif status == "solver_unknown":
            if set(record) != {"gate", "constraint_status", "solver_reason"}:
                raise ValueError("symbolic minimum unknown record is malformed")
            if not isinstance(record["solver_reason"], str):
                raise ValueError("symbolic minimum solver reason is malformed")
        else:
            raise ValueError("symbolic minimum audit status is unknown")

    expected_aggregate = {
        "status_counts": dict(sorted(status_counts.items())),
        "exact_full_candidates": exact_valid,
    }
    if payload["aggregate"] != expected_aggregate:
        raise ValueError("symbolic minimum audit aggregate mismatch")
    return expected_aggregate


def load_and_validate(path: Path) -> dict[str, object]:
    raw = _strict_json_loads(path.read_text(encoding="utf-8"))
    if not isinstance(raw, dict):
        raise ValueError("symbolic minimum audit root must be an object")
    validate_audit(raw)
    return raw


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--states", type=int, default=71)
    parser.add_argument("--gate-min", type=int, default=2)
    parser.add_argument("--gate-max", type=int)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--timeout", type=float, default=10.0)
    parser.add_argument("--result", type=Path)
    parser.add_argument("--validate", type=Path)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    if args.validate is not None:
        payload = load_and_validate(args.validate)
        print(
            json.dumps(
                {
                    "status": "valid_symbolic_minimum_audit",
                    "path": args.validate.as_posix(),
                    "payload_sha256": payload["payload_sha256"],
                    "aggregate": payload["aggregate"],
                },
                indent=2,
                sort_keys=True,
            )
        )
        return 0
    try:
        payload = run_audit(
            state_count=args.states,
            gate_min=args.gate_min,
            gate_max=args.gate_max,
            solver_seed=args.seed,
            timeout_seconds=args.timeout,
        )
    except RuntimeError as exc:
        print(json.dumps({"status": "missing_optional_dependency", "error": str(exc)}))
        return 2
    validate_audit(payload)
    if args.result is not None:
        _atomic_json_write(args.result, payload)
    print(json.dumps(payload, indent=2, sort_keys=True, allow_nan=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
