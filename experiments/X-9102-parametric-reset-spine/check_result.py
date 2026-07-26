"""Independent standard-library checker for X-9102 result artifacts.

This file deliberately imports neither ``symbolic_closure.py`` nor X-9101.
It reconstructs:

* the five-state shortcut table and its terminal carry invariant;
* the canonical reset-spine lift;
* the compact guarded parametric witness trace and its exact terminal test;
* the elementary factor-alignment obstruction; and
* any materialized SAT DFA through a separate concrete product traversal.

An independently implemented decision diagram also replays the uncompressed
guarded trace in the exhaustive small-q tests.

For an UNSAT record, both the symbolic trace and the algebraic obstruction
must cover all ``2**(q-3)`` parameter assignments.  Merely reporting a solver
status, a digest, or an existential set of selected product states is not
accepted as a proof.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import deque
from pathlib import Path
from typing import Iterable, Mapping, Sequence


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


# The table is restated rather than imported.  Outputs are LSD-first strings.
TRANSITIONS: dict[tuple[int, int], tuple[int, str]] = {
    (0, 0): (1, ""),
    (0, 1): (4, ""),
    (1, 0): (1, "0"),
    (1, 1): (1, "1"),
    (2, 0): (2, "0"),
    (2, 1): (3, "1"),
    (3, 0): (2, "1"),
    (3, 1): (4, "0"),
    (4, 0): (3, "0"),
    (4, 1): (4, "1"),
}
TERMINAL: dict[int, str | None] = {
    0: None,
    1: "",
    2: "",
    3: "1",
    4: "01",
}


def _json_bytes(value: object) -> bytes:
    return json.dumps(
        value,
        ensure_ascii=True,
        separators=(",", ":"),
        sort_keys=True,
        allow_nan=False,
    ).encode("utf-8")


def _digest(value: object) -> str:
    return hashlib.sha256(_json_bytes(value)).hexdigest()


def _load_strict(path: Path) -> object:
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


class Diagram:
    """Independent canonical Shannon-diagram implementation."""

    def __init__(self, variables: int):
        if type(variables) is not int or variables < 0:
            raise ValueError("invalid independent diagram variable count")
        self.variables = variables
        self.table: list[tuple[int, int, int]] = [
            (variables, 0, 0),
            (variables, 1, 1),
        ]
        self.intern: dict[tuple[int, int, int], int] = {}
        self.binary_cache: dict[tuple[bool, int, int], int] = {}
        self.complement_cache: dict[int, int] = {0: 1, 1: 0}

    def node(self, variable: int, low: int, high: int) -> int:
        if low == high:
            return low
        key = (variable, low, high)
        result = self.intern.get(key)
        if result is None:
            result = len(self.table)
            self.table.append(key)
            self.intern[key] = result
        return result

    def variable(self, index: int) -> int:
        return self.node(index, 0, 1)

    def complement(self, root: int) -> int:
        result = self.complement_cache.get(root)
        if result is not None:
            return result
        variable, low, high = self.table[root]
        result = self.node(
            variable, self.complement(low), self.complement(high)
        )
        self.complement_cache[root] = result
        self.complement_cache[result] = root
        return result

    def combine(self, disjoin: bool, first: int, second: int) -> int:
        if first > second:
            first, second = second, first
        key = (disjoin, first, second)
        prior = self.binary_cache.get(key)
        if prior is not None:
            return prior

        if disjoin:
            if second == 1:
                return 1
            if first == 0:
                return second
            if first == second:
                return first
        else:
            if first == 0:
                return 0
            if first == 1:
                return second
            if first == second:
                return first

        first_variable = self.table[first][0]
        second_variable = self.table[second][0]
        split = min(first_variable, second_variable)
        if first_variable == split:
            first_low, first_high = self.table[first][1:]
        else:
            first_low = first_high = first
        if second_variable == split:
            second_low, second_high = self.table[second][1:]
        else:
            second_low = second_high = second
        result = self.node(
            split,
            self.combine(disjoin, first_low, second_low),
            self.combine(disjoin, first_high, second_high),
        )
        self.binary_cache[key] = result
        return result

    def both(self, *roots: int) -> int:
        result = 1
        for root in roots:
            result = self.combine(False, result, root)
        return result

    def either(self, roots: Iterable[int]) -> int:
        result = 0
        for root in roots:
            result = self.combine(True, result, root)
        return result

    def count(self, root: int) -> int:
        memo: dict[tuple[int, int], int] = {}

        def descend(node: int, next_variable: int) -> int:
            key = (node, next_variable)
            if key in memo:
                return memo[key]
            if node == 0:
                return 0
            if node == 1:
                return 1 << (self.variables - next_variable)
            variable, low, high = self.table[node]
            value = (1 << (variable - next_variable)) * (
                descend(low, variable + 1) + descend(high, variable + 1)
            )
            memo[key] = value
            return value

        return descend(root, 0)

    def structural_digest(self, root: int) -> str:
        memo = {
            0: hashlib.sha256(b"BDD:false").hexdigest(),
            1: hashlib.sha256(b"BDD:true").hexdigest(),
        }

        def descend(node: int) -> str:
            if node in memo:
                return memo[node]
            variable, low, high = self.table[node]
            raw = (
                f"BDD:node:{variable}:{descend(low)}:{descend(high)}"
            ).encode("ascii")
            memo[node] = hashlib.sha256(raw).hexdigest()
            return memo[node]

        return descend(root)


def _validate_transducer_table() -> None:
    if set(TRANSITIONS) != {
        (state, bit) for state in range(5) for bit in (0, 1)
    }:
        raise AssertionError("independent shortcut table is incomplete")
    if TRANSITIONS[(0, 0)] != (1, ""):
        raise AssertionError("even branch does not delete the low zero")
    if TRANSITIONS[(0, 1)] != (4, ""):
        raise AssertionError("odd branch does not initialize carry two")
    for bit in (0, 1):
        target, output = TRANSITIONS[(1, bit)]
        if target != 1 or output != str(bit):
            raise AssertionError("even branch is not an exact copier")
    for carry in range(3):
        state = carry + 2
        for bit in (0, 1):
            target, output = TRANSITIONS[(state, bit)]
            value = 3 * bit + carry
            if output != str(value & 1) or target != 2 + value // 2:
                raise AssertionError("odd carry transition identity failed")
        flush = TERMINAL[state]
        if flush is None:
            raise AssertionError("odd carry state has no terminal flush")
        decoded = sum(int(bit) << i for i, bit in enumerate(flush))
        if decoded != carry:
            raise AssertionError("terminal carry flush has the wrong value")


class Family:
    def __init__(self, q: int, gate: int):
        if type(q) is not int or q < 3:
            raise ValueError("q must be an integer at least three")
        if type(gate) is not int or not 2 <= gate < q:
            raise ValueError("gate must lie in [2,q)")
        self.q = q
        self.gate = gate
        self.free = tuple(
            position
            for position in range(q - 1)
            if position not in (0, gate - 1)
        )
        self.variable_index = {
            position: variable for variable, position in enumerate(self.free)
        }

    @property
    def variables(self) -> int:
        return self.q - 3

    @property
    def accepting(self) -> int:
        return self.gate + 1

    def label_guards(self, diagram: Diagram, position: int) -> tuple[int, int]:
        if position == 0:
            return 0, 1
        if position == self.gate - 1:
            return 1, 0
        one = diagram.variable(self.variable_index[position])
        return diagram.complement(one), one


def _step_options(
    family: Family,
    diagram: Diagram,
    state: int,
    bit: int,
) -> tuple[tuple[int, int], ...]:
    if state == 0:
        return ((0 if bit == 0 else 1, 1),)
    suffix = state - 1
    if suffix == family.q - 1:
        return ((1 if bit == 0 else family.accepting, 1),)
    zero, one = family.label_guards(diagram, suffix)
    advance = one if bit else zero
    reset = zero if bit else one
    result = []
    if advance:
        result.append((state + 1, advance))
    if reset:
        result.append((1, reset))
    return tuple(result)


def _advance_output(
    family: Family,
    diagram: Diagram,
    state: int,
    output: str,
) -> tuple[tuple[int, int], ...]:
    partition = {state: 1}
    for character in output:
        bit = int(character)
        following: dict[int, int] = {}
        for source, source_guard in partition.items():
            for target, edge_guard in _step_options(
                family, diagram, source, bit
            ):
                guard = diagram.both(source_guard, edge_guard)
                following[target] = diagram.combine(
                    True, following.get(target, 0), guard
                )
        partition = following
    return tuple(sorted(partition.items()))


def _monitor(monitor: int, output: str) -> int:
    for bit in output:
        monitor = 1 if bit == "0" else 2
    return monitor


def _partition_summary(
    diagram: Diagram,
    partition: Mapping[tuple[int, int, int, int, int], int],
) -> dict[str, object]:
    entries = [
        {
            "state": list(state),
            "guard_sha256": diagram.structural_digest(root),
            "assignments": diagram.count(root),
        }
        for state, root in sorted(partition.items())
        if root
    ]
    coverage = diagram.either(partition.values())
    return {
        "configurations": len(entries),
        "coverage_assignments": diagram.count(coverage),
        "partition_sha256": _digest(entries),
    }


def _add(
    diagram: Diagram,
    partition: dict[tuple[int, int, int, int, int], int],
    state: tuple[int, int, int, int, int],
    guard: int,
) -> None:
    if guard:
        partition[state] = diagram.combine(
            True, partition.get(state, 0), guard
        )


def _template(family: Family) -> list[tuple[str, int]]:
    return [
        ("constant", 1),
        *[("label", position) for position in range(family.q - 1)],
        ("constant", 1),
    ]


def _template_text(family: Family) -> list[str]:
    return ["1", *[f"c[{i}]" for i in range(family.q - 1)], "1"]


def _independent_trace(family: Family) -> dict[str, object]:
    diagram = Diagram(family.variables)
    partition: dict[tuple[int, int, int, int, int], int] = {
        (0, 0, 0, 0, 0): 1
    }
    layers = []
    peak = 1
    universe = 1 << family.variables

    for position, symbol in enumerate(_template(family)):
        if symbol[0] == "constant":
            zero, one = ((1, 0) if symbol[1] == 0 else (0, 1))
            symbol_text = str(symbol[1])
        else:
            zero, one = family.label_guards(diagram, symbol[1])
            symbol_text = f"c[{symbol[1]}]"
        following: dict[tuple[int, int, int, int, int], int] = {}
        for state, state_guard in partition.items():
            input_state, machine, output_state, _, output_monitor = state
            for bit, symbol_guard in ((0, zero), (1, one)):
                enabled = diagram.both(state_guard, symbol_guard)
                if not enabled:
                    continue
                next_machine, emitted = TRANSITIONS[(machine, bit)]
                for next_input, input_guard in _step_options(
                    family, diagram, input_state, bit
                ):
                    for next_output, output_guard in _advance_output(
                        family, diagram, output_state, emitted
                    ):
                        guard = diagram.both(
                            enabled, input_guard, output_guard
                        )
                        _add(
                            diagram,
                            following,
                            (
                                next_input,
                                next_machine,
                                next_output,
                                1 if bit == 0 else 2,
                                _monitor(output_monitor, emitted),
                            ),
                            guard,
                        )
        partition = following
        peak = max(peak, len(partition))
        summary = _partition_summary(diagram, partition)
        summary["position"] = position
        summary["symbol"] = symbol_text
        if summary["coverage_assignments"] != universe:
            raise ValueError("independent trace lost parameter assignments")
        layers.append(summary)

    final: dict[tuple[int, int, int, int, int], int] = {}
    accepted = 0
    bad = 0
    for state, source_guard in partition.items():
        input_state, machine, output_state, input_monitor, output_monitor = state
        if input_monitor != 2:
            continue
        terminal = TERMINAL[machine]
        if terminal is None:
            raise ValueError("canonical trace has no terminal transducer output")
        final_monitor = _monitor(output_monitor, terminal)
        if final_monitor != 2:
            raise ValueError("transducer output is not canonical")
        for next_output, edge_guard in _advance_output(
            family, diagram, output_state, terminal
        ):
            guard = diagram.both(source_guard, edge_guard)
            target = (
                input_state,
                machine,
                next_output,
                input_monitor,
                final_monitor,
            )
            _add(diagram, final, target, guard)
            if input_state == family.accepting:
                accepted = diagram.combine(True, accepted, guard)
                if next_output != family.accepting:
                    bad = diagram.combine(True, bad, guard)

    terminal_summary = _partition_summary(diagram, final)
    trace_sha256 = _digest(
        {
            "layers": layers,
            "terminal": terminal_summary,
            "accepted_input_guard_sha256": diagram.structural_digest(accepted),
            "bad_guard_sha256": diagram.structural_digest(bad),
        }
    )
    if diagram.count(accepted) != universe or diagram.count(bad) != universe:
        raise ValueError(
            "parametric witness does not independently cover every assignment"
        )
    return {
        "method": "least_guarded_product_reachability",
        "input_template": _template_text(family),
        "input_length": family.q + 1,
        "layers": len(layers),
        "peak_configurations": peak,
        "terminal_configurations": terminal_summary["configurations"],
        "accepted_input_assignments": universe,
        "closure_violation_assignments": universe,
        "parameter_assignments": universe,
        "bdd_nonterminal_nodes": len(diagram.table) - 2,
        "layer_partitions_sha256": _digest(layers),
        "terminal_partition_sha256": terminal_summary["partition_sha256"],
        "trace_sha256": trace_sha256,
    }


def _encoding(family: Family) -> dict[str, object]:
    transitions = [
        {
            "state": state,
            "bit": bit,
            "target": TRANSITIONS[(state, bit)][0],
            "output_lsd": TRANSITIONS[(state, bit)][1],
        }
        for state in range(5)
        for bit in (0, 1)
    ]
    terminal = [
        {"state": state, "output_lsd": TERMINAL[state]}
        for state in range(5)
    ]
    return {
        "q": family.q,
        "gate": family.gate,
        "free_positions": list(family.free),
        "variable_order": [f"c[{position}]" for position in family.free],
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
            "name": "shortcut_3n+1",
            "state_count": 5,
            "start": 0,
            "transitions": transitions,
            "terminal_outputs": terminal,
        },
        "parametric_witness": _template_text(family),
    }


def _compact_trace_descriptor(family: Family) -> dict[str, object]:
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


def _proof(family: Family) -> dict[str, object]:
    """Reconstruct the algebraic certificate without symbolic execution."""

    q = family.q
    lower = 1 << q
    upper = (1 << (q + 1)) - 1
    if lower <= 3:
        raise AssertionError("the low-alignment exceptional value is in range")
    if (3 * lower + 1) // 2 < 1 << q:
        raise AssertionError("shortcut image can be shorter than q+1 bits")
    if (3 * upper + 1) // 2 >= 1 << (q + 2):
        raise AssertionError("shortcut image can exceed q+2 bits")

    def solve_shortcut_equality(
        output_multiple: int, output_constant: int
    ) -> int:
        # Independently solve
        # (3m+1)/2 = output_multiple*m + output_constant.
        numerator = 2 * output_constant - 1
        denominator = 3 - 2 * output_multiple
        if denominator == 0 or numerator % denominator:
            raise AssertionError("alignment equation has no integral solution")
        return numerator // denominator

    # The word is accepted because each c_i takes the unique advancing edge
    # and the final one enters r_h.  Every accepted suffix contains the same
    # q-bit pattern: backward from the final one at r_(q-1), each nonzero
    # state has its unique advancing predecessor; visits to r_h through the
    # final return can be unwound until the finite run reaches the spine entry.
    #
    # c_0=1 gives m == 3 (mod 4), hence T(m) is odd.  Since m has q+1 bits,
    # T(m) has q+1 or q+2 bits, leaving q or q+1 suffix bits.  There are only
    # the four alignments below.  Solving each equality excludes it.
    cases = [
        {
            "case": "equal_length_only_factor",
            "implied_output": "T(m)=m",
            "equation_solution_m": solve_shortcut_equality(1, 0),
            "contradicts_bounds": True,
        },
        {
            "case": "long_output_factor_at_suffix_offset_0",
            "implied_output": f"T(m)=m+2^{q + 1}",
            "equation_solution_m": solve_shortcut_equality(
                1, 1 << (q + 1)
            ),
            "contradicts_bounds": True,
        },
        {
            "case": "long_output_factor_at_suffix_offset_1_low_bit_0",
            "implied_output": "T(m)=2m-1",
            "equation_solution_m": solve_shortcut_equality(2, -1),
            "contradicts_bounds": True,
        },
        {
            "case": "long_output_factor_at_suffix_offset_1_low_bit_1",
            "implied_output": "T(m)=2m+1",
            "equation_solution_m": solve_shortcut_equality(2, 1),
            "contradicts_bounds": True,
        },
    ]
    for case in cases:
        solution = case["equation_solution_m"]
        if not isinstance(solution, int) or lower <= solution <= upper:
            raise AssertionError("factor-alignment solution falls in input range")
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
        "alignment_cases": cases,
        "conclusion": (
            "the accepted input's exact shortcut image is rejected for every "
            "parameter assignment"
        ),
    }


def _compact_trace(family: Family) -> dict[str, object]:
    descriptor = _compact_trace_descriptor(family)
    proof = _proof(family)
    assignments = 1 << family.variables
    return {
        "method": (
            "guarded_parametric_product_trace_with_exact_factor_alignment"
        ),
        "input_template": _template_text(family),
        "input_length": family.q + 1,
        "layers": family.q + 1,
        "guard_obligations": family.q + 1,
        "all_input_path_guards_tautological": True,
        "terminal_flush_included": True,
        "accepted_input_assignments": assignments,
        "closure_violation_assignments": assignments,
        "parameter_assignments": assignments,
        "symbolic_trace_sha256": _digest(descriptor),
        "factor_alignment_sha256": _digest(proof),
        "trace_sha256": _digest(
            {"descriptor": descriptor, "factor_alignment": proof}
        ),
    }


def _parse_dfa(raw: object) -> tuple[tuple[tuple[int, int], ...], frozenset[int], int]:
    if not isinstance(raw, dict) or set(raw) != {
        "alphabet",
        "bit_order",
        "start",
        "transitions",
        "accepting",
    }:
        raise ValueError("materialized DFA schema is malformed")
    if raw["alphabet"] != [0, 1] or raw["bit_order"] != "lsd_first":
        raise ValueError("materialized DFA alphabet or bit order is invalid")
    rows = raw["transitions"]
    accepting = raw["accepting"]
    start = raw["start"]
    if (
        not isinstance(rows, list)
        or not rows
        or not isinstance(accepting, list)
        or type(start) is not int
    ):
        raise ValueError("materialized DFA data is malformed")
    transitions: list[tuple[int, int]] = []
    for row in rows:
        if (
            not isinstance(row, list)
            or len(row) != 2
            or any(type(target) is not int for target in row)
        ):
            raise ValueError("materialized DFA transition row is malformed")
        transitions.append((row[0], row[1]))
    count = len(transitions)
    if not 0 <= start < count or any(
        type(state) is not int or not 0 <= state < count for state in accepting
    ):
        raise ValueError("materialized DFA state is outside its table")
    if any(
        not 0 <= target < count for row in transitions for target in row
    ):
        raise ValueError("materialized DFA target is outside its table")
    if len(set(accepting)) != len(accepting) or accepting != sorted(accepting):
        raise ValueError("materialized DFA accepting list is not canonical")
    return tuple(transitions), frozenset(accepting), start


def _run_dfa(
    dfa: tuple[tuple[tuple[int, int], ...], frozenset[int], int],
    word: Sequence[int],
) -> int:
    transitions, _, state = dfa
    for bit in word:
        state = transitions[state][bit]
    return state


def _transduce(word: Sequence[int]) -> tuple[int, ...]:
    state = 0
    output: list[int] = []
    for bit in word:
        state, emitted = TRANSITIONS[(state, bit)]
        output.extend(int(character) for character in emitted)
    flush = TERMINAL[state]
    if flush is None:
        raise ValueError("canonical word has no independent terminal flush")
    output.extend(int(character) for character in flush)
    return tuple(output)


def _independent_concrete_closure(
    dfa: tuple[tuple[tuple[int, int], ...], frozenset[int], int],
) -> bool:
    transitions, accepting, start_dfa = dfa
    # Product: input DFA, transducer, output DFA, input monitor, output monitor.
    start = (start_dfa, 0, start_dfa, 0, 0)
    queue = deque([start])
    seen = {start}
    while queue:
        input_state, machine, output_state, input_monitor, output_monitor = (
            queue.popleft()
        )
        if input_monitor == 2:
            flush = TERMINAL[machine]
            if flush is None:
                raise ValueError("independent product found a missing flush")
            final_output = output_state
            final_monitor = output_monitor
            for character in flush:
                bit = int(character)
                final_output = transitions[final_output][bit]
                final_monitor = 1 if bit == 0 else 2
            if final_monitor != 2:
                raise ValueError("independent product found noncanonical output")
            if input_state in accepting and final_output not in accepting:
                return False
        for bit in (0, 1):
            next_machine, emitted = TRANSITIONS[(machine, bit)]
            next_output = output_state
            next_monitor = output_monitor
            for character in emitted:
                output_bit = int(character)
                next_output = transitions[next_output][output_bit]
                next_monitor = 1 if output_bit == 0 else 2
            target = (
                transitions[input_state][bit],
                next_machine,
                next_output,
                1 if bit == 0 else 2,
                next_monitor,
            )
            if target not in seen:
                seen.add(target)
                queue.append(target)
    return True


def _check_sat_record(record: dict[str, object], family: Family) -> None:
    fallback = record.get("fallback")
    if not isinstance(fallback, dict) or fallback.get("status") != "SAT":
        raise ValueError("SAT record lacks a fixed-point SAT payload")
    candidate = fallback.get("candidate")
    if not isinstance(candidate, dict) or set(candidate) != {
        "advance_labels_lsd",
        "suffix_dfa",
        "lifted_dfa",
        "x9101_verify_candidate",
    }:
        raise ValueError("SAT candidate payload is malformed")
    labels = candidate["advance_labels_lsd"]
    if (
        not isinstance(labels, str)
        or len(labels) != family.q - 1
        or any(bit not in "01" for bit in labels)
        or labels[0] != "1"
        or labels[family.gate - 1] != "0"
    ):
        raise ValueError("SAT candidate labels violate the family")
    assignment = fallback.get("assignment")
    if (
        not isinstance(assignment, list)
        or len(assignment) != family.variables
        or any(type(bit) is not int or bit not in (0, 1) for bit in assignment)
    ):
        raise ValueError("SAT assignment is malformed")
    expected_labels = ["0"] * (family.q - 1)
    expected_labels[0] = "1"
    expected_labels[family.gate - 1] = "0"
    for position, variable in family.variable_index.items():
        expected_labels[position] = str(assignment[variable])
    if labels != "".join(expected_labels):
        raise ValueError("SAT assignment and materialized labels differ")

    suffix = _parse_dfa(candidate["suffix_dfa"])
    expected_suffix_rows: list[tuple[int, int]] = []
    for state, character in enumerate(labels):
        row = [0, 0]
        row[int(character)] = state + 1
        expected_suffix_rows.append((row[0], row[1]))
    expected_suffix_rows.append((0, family.gate))
    expected_suffix = (
        tuple(expected_suffix_rows),
        frozenset({family.gate}),
        0,
    )
    if suffix != expected_suffix:
        raise ValueError("materialized SAT suffix DFA differs from its labels")

    lifted = _parse_dfa(candidate["lifted_dfa"])
    expected_lift_rows = [(0, 1)]
    expected_lift_rows.extend(
        (zero + 1, one + 1) for zero, one in expected_suffix_rows
    )
    expected_lift = (
        tuple(expected_lift_rows),
        frozenset({family.accepting}),
        0,
    )
    if lifted != expected_lift:
        raise ValueError("materialized SAT lift differs from its suffix DFA")
    witness = (1,) + tuple(int(bit) for bit in labels) + (1,)
    if _run_dfa(lifted, witness) not in lifted[1]:
        raise ValueError("materialized SAT DFA is semantically empty")
    if not _independent_concrete_closure(lifted):
        raise ValueError("materialized SAT DFA fails independent closure")
    if _run_dfa(lifted, (1,)) in lifted[1] or _run_dfa(
        lifted, (0, 1)
    ) in lifted[1]:
        raise ValueError("materialized SAT DFA accepts the trivial cycle")
    x9101 = candidate["x9101_verify_candidate"]
    if not isinstance(x9101, dict) or x9101.get("valid") is not True:
        raise ValueError("materialized SAT DFA lacks a valid X-9101 receipt")


def check_payload(payload: dict[str, object]) -> dict[str, object]:
    _validate_transducer_table()
    root_fields = {
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
    if not isinstance(payload, dict) or set(payload) != root_fields:
        raise ValueError("X-9102 result root is malformed")
    if (
        payload["schema"] != SCHEMA
        or payload["experiment"] != EXPERIMENT
        or payload["program"] != PROGRAM
        or payload["agent"] != AGENT
        or payload["issue"] != ISSUE
        or payload["classification"] != "EXACT_FINITE_SYMBOLIC_COMPUTATION"
    ):
        raise ValueError("X-9102 identity or classification differs")
    if (
        payload["disclaimer"] != DISCLAIMER
        or payload["result_digest_serialization"]
        != RESULT_DIGEST_SERIALIZATION
    ):
        raise ValueError("X-9102 disclaimer or digest convention differs")
    unsigned = dict(payload)
    observed_digest = unsigned.pop("result_sha256")
    if (
        not isinstance(observed_digest, str)
        or observed_digest != _digest(unsigned)
    ):
        raise ValueError("X-9102 result digest mismatch")

    scope = payload["scope"]
    expected_scope_fields = {
        "q",
        "gate_min",
        "gate_max",
        "gate_count",
        "free_bits_per_gate",
        "assignments_per_gate",
        "map",
        "bit_order",
        "family",
    }
    if not isinstance(scope, dict) or set(scope) != expected_scope_fields:
        raise ValueError("X-9102 scope is malformed")
    q = scope["q"]
    gate_min = scope["gate_min"]
    gate_max = scope["gate_max"]
    if (
        type(q) is not int
        or type(gate_min) is not int
        or type(gate_max) is not int
        or q < 3
        or not 2 <= gate_min <= gate_max < q
        or scope["gate_count"] != gate_max - gate_min + 1
        or scope["free_bits_per_gate"] != q - 3
        or scope["assignments_per_gate"] != 1 << (q - 3)
        or scope["map"] != "shortcut_3n_plus_1"
        or scope["bit_order"] != "lsd_first"
        or scope["family"]
        != "canonical_lift_of_L-9113_reset_pattern_suffix_DFAs"
    ):
        raise ValueError("X-9102 scope values are inconsistent")

    backend = payload["backend"]
    expected_backend_fields = {
        "method",
        "reachable_set_semantics",
        "arbitrary_reachable_state_omission_possible",
        "full_robdd_least_fixed_point_fallback_implemented",
        "explicit_robdd_trace_available_for_differential_tests",
        "node_limit",
        "update_limit",
        "external_dependencies",
        "sat_solver_used",
        "cnf_emitted",
        "cnf_sha256",
        "cnf_reason",
    }
    if not isinstance(backend, dict) or set(backend) != expected_backend_fields:
        raise ValueError("X-9102 backend is malformed")
    node_limit = backend["node_limit"]
    update_limit = backend["update_limit"]
    if (
        backend.get("method")
        != (
            "guarded parametric product trace with exact "
            "factor-alignment terminal decision"
        )
        or backend.get("reachable_set_semantics")
        != (
            "start with the full parameter cube at the product start and "
            "add only guarded forward images"
        )
        or backend.get("arbitrary_reachable_state_omission_possible") is not False
        or backend.get("full_robdd_least_fixed_point_fallback_implemented")
        is not True
        or backend.get("explicit_robdd_trace_available_for_differential_tests")
        is not True
        or not (
            node_limit is None
            or (type(node_limit) is int and node_limit > 0)
        )
        or not (
            update_limit is None
            or (type(update_limit) is int and update_limit > 0)
        )
        or backend.get("external_dependencies") != []
        or backend.get("sat_solver_used") is not False
        or backend.get("cnf_emitted") is not False
        or backend.get("cnf_sha256") is not None
        or backend.get("cnf_reason")
        != (
            "the guarded reachability witness is a smaller exact proof; "
            "no SAT encoding was needed"
        )
    ):
        raise ValueError("X-9102 backend contract differs")

    records = payload["records"]
    if not isinstance(records, list) or len(records) != scope["gate_count"]:
        raise ValueError("X-9102 record count is inconsistent")
    counts = {"SAT": 0, "UNSAT": 0, "UNKNOWN": 0}
    proof_count = 0
    for expected_gate, record in zip(
        range(gate_min, gate_max + 1), records, strict=True
    ):
        if not isinstance(record, dict) or record.get("gate") != expected_gate:
            raise ValueError("X-9102 gate records are malformed or unordered")
        family = Family(q, expected_gate)
        if record.get("free_positions") != list(family.free):
            raise ValueError("X-9102 free parameter positions differ")
        if record.get("encoding_sha256") != _digest(_encoding(family)):
            raise ValueError("X-9102 guarded encoding digest differs")
        status = record.get("status")
        if status not in counts:
            raise ValueError("X-9102 record has an unknown status")
        counts[status] += 1
        if status == "UNSAT":
            if record.get("fallback") is not None:
                raise ValueError("witness-proved UNSAT unexpectedly has fallback")
            expected_trace = _compact_trace(family)
            if record.get("guarded_reachability") != expected_trace:
                raise ValueError(
                    "X-9102 guarded trace differs from independent reconstruction"
                )
            expected_proof = _proof(family)
            if record.get("proof") != expected_proof:
                raise ValueError(
                    "X-9102 factor-alignment proof differs from reconstruction"
                )
            if record.get("reason") != (
                "every parameter assignment has the guarded parametric "
                "canonical closure-violation witness"
            ):
                raise ValueError("X-9102 UNSAT reason differs")
            proof_count += 1
        elif status == "SAT":
            _check_sat_record(record, family)
        else:
            if record.get("proof") is not None:
                raise ValueError("UNKNOWN record cannot carry an UNSAT proof")
            if not isinstance(record.get("reason"), str):
                raise ValueError("UNKNOWN record lacks a reason")

    expected_aggregate = {
        "status_counts": counts,
        "all_requested_gates_decided": counts["UNKNOWN"] == 0,
        "materialized_sat_candidates": counts["SAT"],
        "independently_checkable_unsat_records": proof_count,
    }
    if payload["aggregate"] != expected_aggregate:
        raise ValueError("X-9102 aggregate differs")
    return {
        "status": "independently_verified",
        "result_sha256": observed_digest,
        "gate_count": scope["gate_count"],
        "status_counts": counts,
        "unsat_proofs_checked": proof_count,
    }


def check_file(path: Path) -> dict[str, object]:
    payload = _load_strict(path)
    if not isinstance(payload, dict):
        raise ValueError("X-9102 result root must be an object")
    return check_payload(payload)


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("result", type=Path)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        receipt = check_file(args.result)
        receipt["path"] = args.result.as_posix()
        print(json.dumps(receipt, indent=2, sort_keys=True, allow_nan=False))
        return 0
    except (OSError, ValueError, AssertionError) as exc:
        print(
            json.dumps(
                {"status": "invalid", "error": str(exc)},
                indent=2,
                sort_keys=True,
                allow_nan=False,
            )
        )
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
