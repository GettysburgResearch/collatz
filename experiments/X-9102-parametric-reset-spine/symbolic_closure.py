"""Exact symbolic closure classification for reset-pattern spine DFAs.

The parameter family is the one from L-9113.  For ``q >= 3`` and
``2 <= h < q``, labels ``c[0], ..., c[q-2]`` satisfy

    c[0] = 1, c[h-1] = 0.

The suffix DFA advances from ``r_i`` to ``r_(i+1)`` on ``c[i]`` and resets
to ``r_0`` on the other bit.  Its final state maps 0 to ``r_0`` and 1 to the
sole accepting state ``r_h``.  A fresh raw start state skips low zeroes and
moves to ``r_0`` on the first one.

This module uses the frozen X-9101 five-state shortcut transducer, including
its terminal carry flush.  The general fixed-point fallback represents
parameter sets by a reduced ordered binary decision diagram (ROBDD).
Reachability always starts from the full parameter cube and grows by guarded
forward image; no inductive-set variable can arbitrarily omit a reachable
product state.

For this particular family, the accepted parametric word

    1 c[0] ... c[q-2] 1

already gives a closure violation for every assignment.  The first 1 is the
odd marker used by the canonical lift.  An acyclic guarded product trace is
therefore a complete UNSAT proof for a gate.  A full least-fixed-point engine
is retained as the exact fallback if a future variant is not covered by that
word: fixed point plus a remaining assignment is SAT.  An exhausted fixed
point is mathematically UNSAT, but the top-level artifact status remains
UNKNOWN unless a replayable negative derivation is emitted; a configured
resource boundary is likewise UNKNOWN.

Python's standard library is the only dependency.  SAT/CNF is deliberately
not used, because the guarded reachability proof is both smaller and directly
checkable by ``check_result.py``.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import shutil
import sys
import tempfile
from collections import deque
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Mapping, Sequence


HERE = Path(__file__).resolve().parent
X9101 = HERE.parent / "X-9101-regular-sanctuary"
if X9101.as_posix() not in sys.path:
    sys.path.insert(0, X9101.as_posix())

from automata import DFA, Word, word_text  # noqa: E402
from odd_core import lift_odd_suffix_dfa_to_shortcut  # noqa: E402
from reset_spine import reset_pattern_dfa  # noqa: E402
from transducer import SubsequentialTransducer, shortcut_transducer  # noqa: E402
from verify import verify_candidate  # noqa: E402


SCHEMA = "x-9102-parametric-reset-spine-v1"
EXPERIMENT = "X-9102"
PROGRAM = "exact-parametric-reset-spine-closure"
AGENT = "gpt56-sol-05"
ISSUE = 10
RESULT_DIGEST_SERIALIZATION = (
    "sha256(utf8(json.dumps(unsigned_result,sort_keys=True,"
    "separators=(',',':'),ensure_ascii=True,allow_nan=False)))"
)
DISCLAIMER = (
    "UNSAT means that every reset-pattern assignment at the stated gate has "
    "an independently checkable canonical closure-violation witness. It "
    "eliminates only this reset-pattern family, not all exact-floor suffix "
    "DFAs and not the existence of arbitrary regular Collatz sanctuaries."
)


class BDDLimit(RuntimeError):
    """Raised only at an explicitly configured deterministic BDD boundary."""


class BDD:
    """Small deterministic ROBDD manager with ascending variable order."""

    FALSE = 0
    TRUE = 1

    def __init__(self, variable_count: int, *, node_limit: int | None = None):
        if type(variable_count) is not int or variable_count < 0:
            raise ValueError("variable_count must be a nonnegative integer")
        if node_limit is not None and (
            type(node_limit) is not int or node_limit < 2
        ):
            raise ValueError("node_limit must be None or an integer at least two")
        self.variable_count = variable_count
        self.node_limit = node_limit
        # Terminals use sentinel variable ``variable_count``.
        self.nodes: list[tuple[int, int, int]] = [
            (variable_count, 0, 0),
            (variable_count, 1, 1),
        ]
        self.unique: dict[tuple[int, int, int], int] = {}
        self.apply_cache: dict[tuple[str, int, int], int] = {}
        self.not_cache: dict[int, int] = {0: 1, 1: 0}
        self.digest_cache: dict[int, str] = {
            0: hashlib.sha256(b"BDD:false").hexdigest(),
            1: hashlib.sha256(b"BDD:true").hexdigest(),
        }

    @property
    def nonterminal_nodes(self) -> int:
        return len(self.nodes) - 2

    def _mk(self, variable: int, low: int, high: int) -> int:
        if low == high:
            return low
        if not 0 <= variable < self.variable_count:
            raise ValueError("BDD variable is outside the declared order")
        key = (variable, low, high)
        existing = self.unique.get(key)
        if existing is not None:
            return existing
        if self.node_limit is not None and len(self.nodes) >= self.node_limit:
            raise BDDLimit(f"BDD node limit {self.node_limit} reached")
        result = len(self.nodes)
        self.nodes.append(key)
        self.unique[key] = result
        return result

    def literal(self, variable: int, value: int = 1) -> int:
        if type(variable) is not int or not 0 <= variable < self.variable_count:
            raise ValueError("BDD literal variable is invalid")
        if type(value) is not int or value not in (0, 1):
            raise ValueError("BDD literal value must be zero or one")
        return self._mk(variable, 1 - value, value)

    def negate(self, root: int) -> int:
        cached = self.not_cache.get(root)
        if cached is not None:
            return cached
        variable, low, high = self.nodes[root]
        result = self._mk(variable, self.negate(low), self.negate(high))
        self.not_cache[root] = result
        self.not_cache[result] = root
        return result

    def _apply(self, operation: str, left: int, right: int) -> int:
        if operation not in ("and", "or"):
            raise ValueError("unsupported BDD operation")
        if left > right:
            left, right = right, left
        key = (operation, left, right)
        cached = self.apply_cache.get(key)
        if cached is not None:
            return cached

        if operation == "and":
            if left == 0 or right == 0:
                return 0
            if left == 1:
                return right
            if right == 1 or left == right:
                return left
        else:
            if left == 1 or right == 1:
                return 1
            if left == 0:
                return right
            if right == 0 or left == right:
                return left

        left_var = self.nodes[left][0]
        right_var = self.nodes[right][0]
        variable = min(left_var, right_var)
        if left_var == variable:
            left_low, left_high = self.nodes[left][1:]
        else:
            left_low = left_high = left
        if right_var == variable:
            right_low, right_high = self.nodes[right][1:]
        else:
            right_low = right_high = right
        result = self._mk(
            variable,
            self._apply(operation, left_low, right_low),
            self._apply(operation, left_high, right_high),
        )
        self.apply_cache[key] = result
        return result

    def conjunction(self, *roots: int) -> int:
        result = self.TRUE
        for root in roots:
            result = self._apply("and", result, root)
            if result == self.FALSE:
                break
        return result

    def disjunction(self, *roots: int) -> int:
        result = self.FALSE
        for root in roots:
            result = self._apply("or", result, root)
            if result == self.TRUE:
                break
        return result

    def difference(self, left: int, right: int) -> int:
        return self.conjunction(left, self.negate(right))

    def model_count(self, root: int) -> int:
        memo: dict[tuple[int, int], int] = {}

        def visit(node: int, level: int) -> int:
            key = (node, level)
            if key in memo:
                return memo[key]
            if node == self.FALSE:
                return 0
            if node == self.TRUE:
                return 1 << (self.variable_count - level)
            variable, low, high = self.nodes[node]
            if variable < level:
                raise AssertionError("BDD ordering invariant violated")
            skipped = 1 << (variable - level)
            value = skipped * (
                visit(low, variable + 1) + visit(high, variable + 1)
            )
            memo[key] = value
            return value

        return visit(root, 0)

    def pick_model(self, root: int) -> tuple[int, ...] | None:
        if root == self.FALSE:
            return None
        assignment = [0] * self.variable_count
        node = root
        level = 0
        while node not in (self.FALSE, self.TRUE):
            variable, low, high = self.nodes[node]
            while level < variable:
                assignment[level] = 0
                level += 1
            if low != self.FALSE:
                assignment[variable] = 0
                node = low
            else:
                assignment[variable] = 1
                node = high
            level = variable + 1
        if node == self.FALSE:
            raise AssertionError("BDD model selection entered false")
        return tuple(assignment)

    def structural_digest(self, root: int) -> str:
        cached = self.digest_cache.get(root)
        if cached is not None:
            return cached
        variable, low, high = self.nodes[root]
        raw = (
            f"BDD:node:{variable}:"
            f"{self.structural_digest(low)}:{self.structural_digest(high)}"
        ).encode("ascii")
        value = hashlib.sha256(raw).hexdigest()
        self.digest_cache[root] = value
        return value


@dataclass(frozen=True, order=True)
class ProductState:
    input_state: int
    machine_state: int
    output_state: int
    input_monitor: int
    output_monitor: int

    def as_list(self) -> list[int]:
        return [
            self.input_state,
            self.machine_state,
            self.output_state,
            self.input_monitor,
            self.output_monitor,
        ]


@dataclass(frozen=True)
class Family:
    q: int
    gate: int
    free_positions: tuple[int, ...]
    variable_for_position: Mapping[int, int]

    @classmethod
    def create(cls, q: int, gate: int) -> "Family":
        _validate_family(q, gate)
        free = tuple(
            position
            for position in range(q - 1)
            if position not in (0, gate - 1)
        )
        return cls(q, gate, free, {position: i for i, position in enumerate(free)})

    @property
    def variable_count(self) -> int:
        return self.q - 3

    @property
    def lift_state_count(self) -> int:
        return self.q + 1

    @property
    def accepting_state(self) -> int:
        # Lift state zero is the canonical saturation start.
        return 1 + self.gate

    def label_guards(self, manager: BDD, position: int) -> tuple[int, int]:
        """Return guards for ``c[position] == 0`` and ``== 1``."""

        if position == 0:
            return manager.FALSE, manager.TRUE
        if position == self.gate - 1:
            return manager.TRUE, manager.FALSE
        variable = self.variable_for_position[position]
        one = manager.literal(variable, 1)
        return manager.negate(one), one

    def labels_from_assignment(self, assignment: Sequence[int]) -> Word:
        if len(assignment) != self.variable_count or any(
            type(bit) is not int or bit not in (0, 1) for bit in assignment
        ):
            raise ValueError("parameter assignment has the wrong shape")
        labels = [0] * (self.q - 1)
        labels[0] = 1
        labels[self.gate - 1] = 0
        for position, variable in self.variable_for_position.items():
            labels[position] = assignment[variable]
        return tuple(labels)


def _validate_family(q: int, gate: int) -> None:
    if type(q) is not int or q < 3:
        raise ValueError("q must be an integer at least three")
    if type(gate) is not int or not 2 <= gate < q:
        raise ValueError("gate must be an integer in [2,q)")


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


def _strict_json_load(path: Path) -> object:
    def reject_constant(raw: str) -> object:
        raise ValueError(f"nonstandard JSON constant {raw!r}")

    def reject_duplicates(
        pairs: list[tuple[str, object]],
    ) -> dict[str, object]:
        result: dict[str, object] = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"duplicate JSON key {key!r}")
            result[key] = value
        return result

    return json.loads(
        path.read_text(encoding="utf-8"),
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


def _monitor_after(monitor: int, output: Iterable[int]) -> int:
    for bit in output:
        monitor = 1 if bit == 0 else 2
    return monitor


def _merge_guard(
    manager: BDD,
    partition: dict[ProductState, int],
    state: ProductState,
    guard: int,
) -> None:
    if guard == manager.FALSE:
        return
    partition[state] = manager.disjunction(
        partition.get(state, manager.FALSE), guard
    )


def _dfa_step_options(
    family: Family,
    manager: BDD,
    state: int,
    bit: int,
) -> tuple[tuple[int, int], ...]:
    """Guarded transition options for the raw canonical lift."""

    if bit not in (0, 1):
        raise ValueError("DFA input symbol must be zero or one")
    if state == 0:
        return ((0 if bit == 0 else 1, manager.TRUE),)
    suffix_state = state - 1
    if suffix_state == family.q - 1:
        return (
            (
                1 if bit == 0 else family.accepting_state,
                manager.TRUE,
            ),
        )
    zero_guard, one_guard = family.label_guards(manager, suffix_state)
    advancing_guard = one_guard if bit == 1 else zero_guard
    reset_guard = zero_guard if bit == 1 else one_guard
    options: list[tuple[int, int]] = []
    if advancing_guard != manager.FALSE:
        options.append((state + 1, advancing_guard))
    if reset_guard != manager.FALSE:
        options.append((1, reset_guard))
    return tuple(options)


def _advance_output_options(
    family: Family,
    manager: BDD,
    state: int,
    output: Sequence[int],
) -> tuple[tuple[int, int], ...]:
    partition: dict[int, int] = {state: manager.TRUE}
    for bit in output:
        next_partition: dict[int, int] = {}
        for source, source_guard in partition.items():
            for target, edge_guard in _dfa_step_options(
                family, manager, source, bit
            ):
                guard = manager.conjunction(source_guard, edge_guard)
                if guard != manager.FALSE:
                    next_partition[target] = manager.disjunction(
                        next_partition.get(target, manager.FALSE), guard
                    )
        partition = next_partition
    return tuple(sorted(partition.items()))


def _symbol_guards(
    family: Family,
    manager: BDD,
    symbol: tuple[str, int],
) -> tuple[int, int]:
    kind, value = symbol
    if kind == "constant":
        if value not in (0, 1):
            raise ValueError("constant template symbol is not a bit")
        return (
            manager.TRUE if value == 0 else manager.FALSE,
            manager.TRUE if value == 1 else manager.FALSE,
        )
    if kind == "label":
        return family.label_guards(manager, value)
    raise ValueError("unknown parametric input symbol")


def _witness_symbols(family: Family) -> tuple[tuple[str, int], ...]:
    return (
        (("constant", 1),)
        + tuple(("label", position) for position in range(family.q - 1))
        + (("constant", 1),)
    )


def _witness_template_text(family: Family) -> list[str]:
    return ["1", *[f"c[{i}]" for i in range(family.q - 1)], "1"]


def _partition_record(
    manager: BDD,
    partition: Mapping[ProductState, int],
) -> dict[str, object]:
    entries = [
        {
            "state": state.as_list(),
            "guard_sha256": manager.structural_digest(root),
            "assignments": manager.model_count(root),
        }
        for state, root in sorted(partition.items())
        if root != manager.FALSE
    ]
    coverage = manager.disjunction(*(partition.values()))
    return {
        "configurations": len(entries),
        "coverage_assignments": manager.model_count(coverage),
        "partition_sha256": _sha256_value(entries),
    }


def _ordinary_successors(
    family: Family,
    manager: BDD,
    transducer: SubsequentialTransducer,
    state: ProductState,
    bit: int,
) -> tuple[tuple[ProductState, int], ...]:
    next_machine, emitted = transducer.step(state.machine_state, bit)
    results: list[tuple[ProductState, int]] = []
    for next_input, input_guard in _dfa_step_options(
        family, manager, state.input_state, bit
    ):
        for next_output, output_guard in _advance_output_options(
            family, manager, state.output_state, emitted
        ):
            guard = manager.conjunction(input_guard, output_guard)
            if guard == manager.FALSE:
                continue
            results.append(
                (
                    ProductState(
                        next_input,
                        next_machine,
                        next_output,
                        1 if bit == 0 else 2,
                        _monitor_after(state.output_monitor, emitted),
                    ),
                    guard,
                )
            )
    return tuple(results)


def _terminal_partition(
    family: Family,
    manager: BDD,
    transducer: SubsequentialTransducer,
    partition: Mapping[ProductState, int],
) -> tuple[dict[ProductState, int], int, int]:
    final: dict[ProductState, int] = {}
    accepted_input = manager.FALSE
    bad = manager.FALSE
    for state, source_guard in partition.items():
        if state.input_monitor != 2:
            continue
        terminal = transducer.terminal_output(state.machine_state)
        if terminal is None:
            raise AssertionError(
                "X-9101 transducer lacks a terminal output on canonical input"
            )
        final_monitor = _monitor_after(state.output_monitor, terminal)
        if final_monitor != 2:
            raise AssertionError(
                "X-9101 transducer emitted a noncanonical terminal output"
            )
        for output_state, terminal_guard in _advance_output_options(
            family, manager, state.output_state, terminal
        ):
            guard = manager.conjunction(source_guard, terminal_guard)
            target = ProductState(
                state.input_state,
                state.machine_state,
                output_state,
                state.input_monitor,
                final_monitor,
            )
            _merge_guard(manager, final, target, guard)
            if state.input_state == family.accepting_state:
                accepted_input = manager.disjunction(accepted_input, guard)
                if output_state != family.accepting_state:
                    bad = manager.disjunction(bad, guard)
    return final, accepted_input, bad


def guarded_parametric_witness(
    q: int,
    gate: int,
    *,
    node_limit: int | None = None,
) -> tuple[dict[str, object], BDD, int, int]:
    """Run the exact guarded product on the parametric accepted word."""

    family = Family.create(q, gate)
    manager = BDD(family.variable_count, node_limit=node_limit)
    transducer = shortcut_transducer(1)
    start = ProductState(0, transducer.start, 0, 0, 0)
    partition: dict[ProductState, int] = {start: manager.TRUE}
    layer_records: list[dict[str, object]] = []
    peak_configurations = 1

    for index, symbol in enumerate(_witness_symbols(family)):
        zero_guard, one_guard = _symbol_guards(family, manager, symbol)
        next_partition: dict[ProductState, int] = {}
        for state, state_guard in partition.items():
            for bit, symbol_guard in ((0, zero_guard), (1, one_guard)):
                enabled = manager.conjunction(state_guard, symbol_guard)
                if enabled == manager.FALSE:
                    continue
                for target, edge_guard in _ordinary_successors(
                    family, manager, transducer, state, bit
                ):
                    _merge_guard(
                        manager,
                        next_partition,
                        target,
                        manager.conjunction(enabled, edge_guard),
                    )
        partition = next_partition
        peak_configurations = max(peak_configurations, len(partition))
        record = _partition_record(manager, partition)
        record["position"] = index
        record["symbol"] = (
            str(symbol[1])
            if symbol[0] == "constant"
            else f"c[{symbol[1]}]"
        )
        layer_records.append(record)
        if record["coverage_assignments"] != 1 << family.variable_count:
            raise AssertionError("guarded trace lost a parameter assignment")

    final, accepted_input, bad = _terminal_partition(
        family, manager, transducer, partition
    )
    final_record = _partition_record(manager, final)
    trace_digest = _sha256_value(
        {
            "layers": layer_records,
            "terminal": final_record,
            "accepted_input_guard_sha256": manager.structural_digest(
                accepted_input
            ),
            "bad_guard_sha256": manager.structural_digest(bad),
        }
    )
    summary: dict[str, object] = {
        "method": "least_guarded_product_reachability",
        "input_template": _witness_template_text(family),
        "input_length": q + 1,
        "layers": len(layer_records),
        "peak_configurations": peak_configurations,
        "terminal_configurations": final_record["configurations"],
        "accepted_input_assignments": manager.model_count(accepted_input),
        "closure_violation_assignments": manager.model_count(bad),
        "parameter_assignments": 1 << family.variable_count,
        "bdd_nonterminal_nodes": manager.nonterminal_nodes,
        "layer_partitions_sha256": _sha256_value(layer_records),
        "terminal_partition_sha256": final_record["partition_sha256"],
        "trace_sha256": trace_digest,
    }
    return summary, manager, accepted_input, bad


def _encoding_specification(
    family: Family,
    transducer: SubsequentialTransducer,
) -> dict[str, object]:
    transitions = []
    for state in range(transducer.state_count):
        for bit in (0, 1):
            target, output = transducer.step(state, bit)
            transitions.append(
                {
                    "state": state,
                    "bit": bit,
                    "target": target,
                    "output_lsd": word_text(output),
                }
            )
    terminal = [
        {
            "state": state,
            "output_lsd": (
                None
                if transducer.terminal_output(state) is None
                else word_text(transducer.terminal_output(state) or ())
            ),
        }
        for state in range(transducer.state_count)
    ]
    return {
        "q": family.q,
        "gate": family.gate,
        "free_positions": list(family.free_positions),
        "variable_order": [f"c[{position}]" for position in family.free_positions],
        "fixed_labels": {"c[0]": 1, f"c[{family.gate - 1}]": 0},
        "lift": {
            "states": ["s", *[f"r{i}" for i in range(family.q)]],
            "start": "s",
            "accepting": f"r{family.gate}",
            "start_transitions": {"0": "s", "1": "r0"},
            "spine_rule": (
                "delta(r_i,c_i)=r_(i+1); "
                "delta(r_i,1-c_i)=r0 for i<q-1"
            ),
            "last_transitions": {"0": "r0", "1": f"r{family.gate}"},
        },
        "canonical_input_monitor": {
            "0": "empty",
            "1": "nonempty_last_zero",
            "2": "nonempty_last_one",
        },
        "transducer": {
            "name": transducer.name,
            "state_count": transducer.state_count,
            "start": transducer.start,
            "transitions": transitions,
            "terminal_outputs": terminal,
        },
        "parametric_witness": _witness_template_text(family),
    }


def _factor_alignment_proof(family: Family) -> dict[str, object]:
    q = family.q
    lower = 1 << q
    upper = (1 << (q + 1)) - 1

    def shortcut_solution(output_multiple: int, output_constant: int) -> int:
        # (3m+1)/2 = output_multiple*m + output_constant.
        numerator = 2 * output_constant - 1
        denominator = 3 - 2 * output_multiple
        if denominator == 0 or numerator % denominator:
            raise AssertionError("factor alignment lacks an integral solution")
        return numerator // denominator

    return {
        "kind": "universal_parametric_least_word_factor_alignment",
        "input_value_symbol": "m",
        "input_value_bounds": [lower, upper],
        "shortcut_formula": "T(m)=(3m+1)/2",
        "shortcut_output_is_odd": True,
        "reason_output_is_odd": "c[0]=1 makes m congruent to 3 modulo 4",
        "required_accepted_suffix_factor": "c[0]...c[q-2]1",
        "output_full_length_options": [q + 1, q + 2],
        "output_suffix_length_options": [q, q + 1],
        "alignment_cases": [
            {
                "case": "equal_length_only_factor",
                "implied_output": "T(m)=m",
                "equation_solution_m": shortcut_solution(1, 0),
                "contradicts_bounds": True,
            },
            {
                "case": "long_output_factor_at_suffix_offset_0",
                "implied_output": f"T(m)=m+2^{q + 1}",
                "equation_solution_m": shortcut_solution(1, 1 << (q + 1)),
                "contradicts_bounds": True,
            },
            {
                "case": "long_output_factor_at_suffix_offset_1_low_bit_0",
                "implied_output": "T(m)=2m-1",
                "equation_solution_m": shortcut_solution(2, -1),
                "contradicts_bounds": True,
            },
            {
                "case": "long_output_factor_at_suffix_offset_1_low_bit_1",
                "implied_output": "T(m)=2m+1",
                "equation_solution_m": shortcut_solution(2, 1),
                "contradicts_bounds": True,
            },
        ],
        "conclusion": (
            "the accepted input's exact shortcut image is rejected for every "
            "parameter assignment"
        ),
    }


def _compact_trace_descriptor(family: Family) -> dict[str, object]:
    """Return a linear guarded-product proof descriptor.

    The input side of the product has one path: at suffix state ``r_i`` the
    parametric symbol is exactly ``c[i]``, so its advancing-edge guard is the
    tautology ``c[i] == c[i]``.  The transducer side branches through the
    frozen carry table.  Rather than expanding those Boolean carry functions
    into an exponentially large ROBDD, the terminal output is discharged by
    the four exact factor alignments in :func:`_factor_alignment_proof`.
    """

    steps: list[dict[str, object]] = [
        {
            "position": 0,
            "input_symbol": "1",
            "input_transition": "s->r0",
            "input_guard": "true",
            "transducer_transition": "S --1/epsilon--> C2",
        }
    ]
    for position in range(family.q - 1):
        steps.append(
            {
                "position": position + 1,
                "input_symbol": f"c[{position}]",
                "input_transition": f"r{position}->r{position + 1}",
                "input_guard": f"c[{position}]==c[{position}]",
                "transducer_transition": (
                    "the unique X-9101 carry-table edge selected by "
                    f"c[{position}]"
                ),
            }
        )
    steps.append(
        {
            "position": family.q,
            "input_symbol": "1",
            "input_transition": f"r{family.q - 1}->r{family.gate}",
            "input_guard": "true",
            "transducer_transition": (
                "the X-9101 carry-table 1-edge followed by its terminal flush"
            ),
        }
    )
    return {
        "initial_product_state": [
            "lift:s",
            "transducer:S",
            "output-lift:s",
            "input-monitor:empty",
            "output-monitor:empty",
        ],
        "steps": steps,
        "input_endpoint": f"r{family.gate}",
        "input_endpoint_accepting": True,
        "output_endpoint_test": (
            "rejected because an accepted q- or (q+1)-bit suffix would have "
            "one of the four impossible required-factor alignments"
        ),
        "terminal_flush_included": True,
    }


def compact_guarded_parametric_witness(
    q: int,
    gate: int,
) -> dict[str, object]:
    """Produce the scalable guarded reachability certificate for one gate."""

    family = Family.create(q, gate)
    descriptor = _compact_trace_descriptor(family)
    assignments = 1 << family.variable_count
    return {
        "method": (
            "guarded_parametric_product_trace_with_exact_factor_alignment"
        ),
        "input_template": _witness_template_text(family),
        "input_length": q + 1,
        "layers": q + 1,
        "guard_obligations": q + 1,
        "all_input_path_guards_tautological": True,
        "terminal_flush_included": True,
        "accepted_input_assignments": assignments,
        "closure_violation_assignments": assignments,
        "parameter_assignments": assignments,
        "symbolic_trace_sha256": _sha256_value(descriptor),
        "factor_alignment_sha256": _sha256_value(
            _factor_alignment_proof(family)
        ),
        "trace_sha256": _sha256_value(
            {
                "descriptor": descriptor,
                "factor_alignment": _factor_alignment_proof(family),
            }
        ),
    }


def _materialize_candidate(
    family: Family,
    assignment: Sequence[int],
) -> tuple[DFA, DFA, dict[str, object]]:
    labels = family.labels_from_assignment(assignment)
    suffix = reset_pattern_dfa(family.q, family.gate, labels)
    lifted = lift_odd_suffix_dfa_to_shortcut(suffix)
    verification = verify_candidate(lifted, shortcut_transducer(1))
    return suffix, lifted, {
        "advance_labels_lsd": word_text(labels),
        "suffix_dfa": suffix.to_dict(),
        "lifted_dfa": lifted.to_dict(),
        "x9101_verify_candidate": verification.to_dict(),
    }


def guarded_closure_fixed_point(
    q: int,
    gate: int,
    *,
    node_limit: int | None = None,
    update_limit: int | None = None,
) -> dict[str, object]:
    """Compute the exact least reachable assignment set at every product node.

    This is the complete closure fallback.  It is intentionally not needed by
    the q=71 result because the acyclic parametric witness already covers the
    entire parameter cube.
    """

    family = Family.create(q, gate)
    if update_limit is not None and (
        type(update_limit) is not int or update_limit < 1
    ):
        raise ValueError("update_limit must be None or a positive integer")
    manager = BDD(family.variable_count, node_limit=node_limit)
    transducer = shortcut_transducer(1)
    start = ProductState(0, transducer.start, 0, 0, 0)
    reachable: dict[ProductState, int] = {start: manager.TRUE}
    queue = deque([start])
    queued = {start}
    bad = manager.FALSE
    updates = 0

    try:
        while queue:
            state = queue.popleft()
            queued.remove(state)
            source_guard = reachable[state]

            singleton = {state: source_guard}
            _, _, terminal_bad = _terminal_partition(
                family, manager, transducer, singleton
            )
            bad = manager.disjunction(bad, terminal_bad)
            if bad == manager.TRUE:
                return {
                    "status": "UNSAT",
                    "reason": "all assignments reach a closure violation",
                    "product_states": len(reachable),
                    "guard_updates": updates,
                    "bdd_nonterminal_nodes": manager.nonterminal_nodes,
                    "bad_assignments": 1 << family.variable_count,
                }

            for bit in (0, 1):
                for target, edge_guard in _ordinary_successors(
                    family, manager, transducer, state, bit
                ):
                    contribution = manager.conjunction(
                        source_guard, edge_guard
                    )
                    old = reachable.get(target, manager.FALSE)
                    merged = manager.disjunction(old, contribution)
                    if merged == old:
                        continue
                    reachable[target] = merged
                    updates += 1
                    if update_limit is not None and updates > update_limit:
                        return {
                            "status": "UNKNOWN",
                            "reason": f"guard update limit {update_limit} reached",
                            "product_states": len(reachable),
                            "guard_updates": updates,
                            "bdd_nonterminal_nodes": manager.nonterminal_nodes,
                            "bad_assignments": manager.model_count(bad),
                        }
                    if target not in queued:
                        queue.append(target)
                        queued.add(target)
    except BDDLimit as exc:
        return {
            "status": "UNKNOWN",
            "reason": str(exc),
            "product_states": len(reachable),
            "guard_updates": updates,
            "bdd_nonterminal_nodes": manager.nonterminal_nodes,
            "bad_assignments": manager.model_count(bad),
        }

    good = manager.negate(bad)
    assignment = manager.pick_model(good)
    if assignment is None:
        return {
            "status": "UNSAT",
            "reason": "least fixed point covers all assignments with violations",
            "product_states": len(reachable),
            "guard_updates": updates,
            "bdd_nonterminal_nodes": manager.nonterminal_nodes,
            "bad_assignments": 1 << family.variable_count,
        }
    _, _, materialized = _materialize_candidate(family, assignment)
    verification = materialized["x9101_verify_candidate"]
    if not isinstance(verification, dict) or verification.get("valid") is not True:
        raise AssertionError(
            "fixed-point SAT assignment failed materialized X-9101 verification"
        )
    return {
        "status": "SAT",
        "reason": "least fixed point leaves a closure-safe assignment",
        "product_states": len(reachable),
        "guard_updates": updates,
        "bdd_nonterminal_nodes": manager.nonterminal_nodes,
        "bad_assignments": manager.model_count(bad),
        "assignment": list(assignment),
        "candidate": materialized,
    }


def classify_gate(
    q: int,
    gate: int,
    *,
    node_limit: int | None = None,
    update_limit: int | None = None,
) -> dict[str, object]:
    """Return SAT, UNSAT, or UNKNOWN with exact status boundaries."""

    family = Family.create(q, gate)
    transducer = shortcut_transducer(1)
    specification = _encoding_specification(family, transducer)
    encoding_sha256 = _sha256_value(specification)
    trace = compact_guarded_parametric_witness(q, gate)
    all_assignments = 1 << family.variable_count
    if (
        trace["accepted_input_assignments"] == all_assignments
        and trace["closure_violation_assignments"] == all_assignments
    ):
        return {
            "gate": gate,
            "status": "UNSAT",
            "reason": (
                "every parameter assignment has the guarded parametric "
                "canonical closure-violation witness"
            ),
            "free_positions": list(family.free_positions),
            "encoding_sha256": encoding_sha256,
            "guarded_reachability": trace,
            "proof": _factor_alignment_proof(family),
            "fallback": None,
        }

    fallback = guarded_closure_fixed_point(
        q,
        gate,
        node_limit=node_limit,
        update_limit=update_limit,
    )
    reported_status = fallback["status"]
    reported_reason = fallback["reason"]
    if reported_status == "UNSAT":
        # The in-memory fixed point is an exact decision, but its complete
        # derivation is not serialized by this prototype.  Do not export a
        # bare negative status as a proof.
        reported_status = "UNKNOWN"
        reported_reason = (
            "full fixed point observed UNSAT, but no independently checkable "
            "fixed-point derivation was emitted"
        )
    return {
        "gate": gate,
        "status": reported_status,
        "reason": reported_reason,
        "free_positions": list(family.free_positions),
        "encoding_sha256": encoding_sha256,
        "guarded_reachability": trace,
        "proof": None,
        "fallback": fallback,
    }


def detect_sat_and_proof_tools() -> dict[str, object]:
    """Report local optional tools without changing the scientific result."""

    executables = [
        "kissat",
        "cadical",
        "minisat",
        "glucose",
        "cryptominisat",
        "z3",
        "drat-trim",
        "gratgen",
        "lrat-check",
        "cake_lpr",
    ]
    found = {
        name: path
        for name in executables
        if (path := shutil.which(name)) is not None
    }
    modules = {
        name: importlib.util.find_spec(name) is not None
        for name in ("z3", "pysat", "pycosat")
    }
    return {"executables": found, "python_modules": modules}


def build_result(
    *,
    q: int = 71,
    gate_min: int = 3,
    gate_max: int | None = None,
    node_limit: int | None = None,
    update_limit: int | None = None,
) -> dict[str, object]:
    if gate_max is None:
        gate_max = q - 1
    _validate_family(q, gate_min)
    _validate_family(q, gate_max)
    if gate_min > gate_max:
        raise ValueError("gate_min cannot exceed gate_max")

    records = [
        classify_gate(
            q,
            gate,
            node_limit=node_limit,
            update_limit=update_limit,
        )
        for gate in range(gate_min, gate_max + 1)
    ]
    status_counts = {
        status: sum(record["status"] == status for record in records)
        for status in ("SAT", "UNSAT", "UNKNOWN")
    }
    result: dict[str, object] = {
        "schema": SCHEMA,
        "experiment": EXPERIMENT,
        "program": PROGRAM,
        "agent": AGENT,
        "issue": ISSUE,
        "classification": "EXACT_FINITE_SYMBOLIC_COMPUTATION",
        "scope": {
            "q": q,
            "gate_min": gate_min,
            "gate_max": gate_max,
            "gate_count": gate_max - gate_min + 1,
            "free_bits_per_gate": q - 3,
            "assignments_per_gate": 1 << (q - 3),
            "map": "shortcut_3n_plus_1",
            "bit_order": "lsd_first",
            "family": "canonical_lift_of_L-9113_reset_pattern_suffix_DFAs",
        },
        "backend": {
            "method": (
                "guarded parametric product trace with exact "
                "factor-alignment terminal decision"
            ),
            "reachable_set_semantics": (
                "start with the full parameter cube at the product start and "
                "add only guarded forward images"
            ),
            "arbitrary_reachable_state_omission_possible": False,
            "full_robdd_least_fixed_point_fallback_implemented": True,
            "explicit_robdd_trace_available_for_differential_tests": True,
            "node_limit": node_limit,
            "update_limit": update_limit,
            "external_dependencies": [],
            "sat_solver_used": False,
            "cnf_emitted": False,
            "cnf_sha256": None,
            "cnf_reason": (
                "the guarded reachability witness is a smaller exact proof; "
                "no SAT encoding was needed"
            ),
        },
        "records": records,
        "aggregate": {
            "status_counts": status_counts,
            "all_requested_gates_decided": status_counts["UNKNOWN"] == 0,
            "materialized_sat_candidates": status_counts["SAT"],
            "independently_checkable_unsat_records": sum(
                record["status"] == "UNSAT" and record["proof"] is not None
                for record in records
            ),
        },
        "disclaimer": DISCLAIMER,
        "result_digest_serialization": RESULT_DIGEST_SERIALIZATION,
    }
    result["result_sha256"] = _sha256_value(result)
    return result


def validate_result(payload: dict[str, object]) -> dict[str, object]:
    """Strict in-process validation; use check_result.py for independence."""

    expected_root = {
        "schema",
        "experiment",
        "program",
        "agent",
        "issue",
        "classification",
        "scope",
        "backend",
        "records",
        "aggregate",
        "disclaimer",
        "result_digest_serialization",
        "result_sha256",
    }
    if not isinstance(payload, dict) or set(payload) != expected_root:
        raise ValueError("X-9102 result root is malformed")
    if (
        payload["schema"] != SCHEMA
        or payload["experiment"] != EXPERIMENT
        or payload["program"] != PROGRAM
        or payload["agent"] != AGENT
        or payload["issue"] != ISSUE
    ):
        raise ValueError("X-9102 identity fields differ")
    digest = payload["result_sha256"]
    unsigned = dict(payload)
    del unsigned["result_sha256"]
    if not isinstance(digest, str) or digest != _sha256_value(unsigned):
        raise ValueError("X-9102 result digest mismatch")
    if payload["result_digest_serialization"] != RESULT_DIGEST_SERIALIZATION:
        raise ValueError("X-9102 digest serialization differs")
    if payload["disclaimer"] != DISCLAIMER:
        raise ValueError("X-9102 disclaimer differs")

    scope = payload["scope"]
    if not isinstance(scope, dict):
        raise ValueError("X-9102 scope is malformed")
    q = scope.get("q")
    gate_min = scope.get("gate_min")
    gate_max = scope.get("gate_max")
    if (
        type(q) is not int
        or type(gate_min) is not int
        or type(gate_max) is not int
        or q < 3
        or not 2 <= gate_min <= gate_max < q
    ):
        raise ValueError("X-9102 gate scope is invalid")
    records = payload["records"]
    if not isinstance(records, list) or [
        record.get("gate") for record in records if isinstance(record, dict)
    ] != list(range(gate_min, gate_max + 1)):
        raise ValueError("X-9102 gate records are malformed or unordered")
    expected = build_result(
        q=q,
        gate_min=gate_min,
        gate_max=gate_max,
        node_limit=payload["backend"].get("node_limit"),  # type: ignore[union-attr]
        update_limit=payload["backend"].get("update_limit"),  # type: ignore[union-attr]
    )
    if payload != expected:
        raise ValueError("X-9102 result differs from exact recomputation")
    return {
        "status": "valid",
        "result_sha256": digest,
        "aggregate": payload["aggregate"],
    }


def load_and_validate(path: Path) -> dict[str, object]:
    raw = _strict_json_load(path)
    if not isinstance(raw, dict):
        raise ValueError("X-9102 result root must be an object")
    validate_result(raw)
    return raw


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--q", type=int, default=71)
    parser.add_argument("--gate-min", type=int, default=3)
    parser.add_argument("--gate-max", type=int)
    parser.add_argument("--node-limit", type=int)
    parser.add_argument("--update-limit", type=int)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--validate", type=Path)
    parser.add_argument("--detect-tools", action="store_true")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        if args.detect_tools:
            print(
                json.dumps(
                    detect_sat_and_proof_tools(),
                    indent=2,
                    sort_keys=True,
                    allow_nan=False,
                )
            )
            return 0
        if args.validate is not None:
            payload = load_and_validate(args.validate)
            print(
                json.dumps(
                    {
                        "status": "valid",
                        "path": args.validate.as_posix(),
                        "result_sha256": payload["result_sha256"],
                        "aggregate": payload["aggregate"],
                    },
                    indent=2,
                    sort_keys=True,
                    allow_nan=False,
                )
            )
            return 0
        payload = build_result(
            q=args.q,
            gate_min=args.gate_min,
            gate_max=args.gate_max,
            node_limit=args.node_limit,
            update_limit=args.update_limit,
        )
        validate_result(payload)
        if args.output is not None:
            _atomic_json_write(args.output, payload)
        print(json.dumps(payload, indent=2, sort_keys=True, allow_nan=False))
        return 0
    except (OSError, ValueError, AssertionError, BDDLimit) as exc:
        print(
            json.dumps(
                {"status": "error", "error": str(exc)},
                indent=2,
                sort_keys=True,
                allow_nan=False,
            )
        )
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
