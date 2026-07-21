#!/usr/bin/env python3
"""Build and audit finite Collatz safety automata without a transducer.

For the shortcut map

    T(n) = n / 2                 (n even)
           (3n + 1) / 2         (n odd),

the depth-d safety language consists of canonical positive LSD-first binary
words whose values avoid {1, 2} for orbit times 0 through d.  Its complement
inside the canonical language is the finite reverse Collatz tree of {1, 2}
through depth d.

This experiment builds the minimal DFA directly from that finite exception
set.  It then removes the inevitable two-state canonical tail component and
profiles the remaining acyclic boundary.  No finite-horizon result is treated
as evidence for an infinite Collatz orbit.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
import sys
from collections import Counter, deque
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


BitWord = tuple[int, ...]


def encode_lsd(value: int) -> BitWord:
    """Return the canonical least-significant-bit-first encoding of value."""
    if value <= 0:
        raise ValueError("canonical positive encoding requires value > 0")
    return tuple(int(char) for char in reversed(bin(value)[2:]))


def direct_shortcut(value: int) -> int:
    if value <= 0:
        raise ValueError("the shortcut map is restricted to positive integers")
    return value // 2 if value % 2 == 0 else (3 * value + 1) // 2


def direct_avoids(value: int, depth: int) -> bool:
    """Whether orbit states 0, ..., depth all avoid the trivial cycle."""
    if depth < 0:
        raise ValueError("depth must be nonnegative")
    for _ in range(depth + 1):
        if value in (1, 2):
            return False
        value = direct_shortcut(value)
    return True


def shortcut_preimages(value: int) -> frozenset[int]:
    """All positive integer preimages of value under the shortcut map."""
    if value <= 0:
        raise ValueError("preimages are restricted to positive integers")
    result = {2 * value}
    if value % 3 == 2:
        result.add((2 * value - 1) // 3)
    return frozenset(result)


def forbidden_levels(max_depth: int) -> list[frozenset[int]]:
    """Finite sets hitting {1, 2} within each requested horizon."""
    if max_depth < 0:
        raise ValueError("max_depth must be nonnegative")
    seen = {1, 2}
    frontier = {1, 2}
    levels = [frozenset(seen)]
    for _ in range(max_depth):
        next_frontier: set[int] = set()
        for value in frontier:
            next_frontier.update(shortcut_preimages(value))
        next_frontier.difference_update(seen)
        seen.update(next_frontier)
        frontier = next_frontier
        levels.append(frozenset(seen))
    return levels


@dataclass(frozen=True)
class DFA:
    """A complete binary DFA."""

    transitions: tuple[tuple[int, int], ...]
    accepting: frozenset[int]
    start: int = 0

    def __post_init__(self) -> None:
        state_count = len(self.transitions)
        if state_count == 0:
            raise ValueError("a DFA needs at least one state")
        if not 0 <= self.start < state_count:
            raise ValueError("start state is outside the DFA")
        for row in self.transitions:
            if len(row) != 2 or any(
                not 0 <= target < state_count for target in row
            ):
                raise ValueError("invalid transition table")
        if any(not 0 <= state < state_count for state in self.accepting):
            raise ValueError("accepting state is outside the DFA")

    @property
    def state_count(self) -> int:
        return len(self.transitions)

    def run(self, word: Iterable[int]) -> int:
        state = self.start
        for bit in word:
            if bit not in (0, 1):
                raise ValueError(f"invalid input bit: {bit!r}")
            state = self.transitions[state][bit]
        return state

    def accepts_word(self, word: BitWord) -> bool:
        return self.run(word) in self.accepting

    def accepts_value(self, value: int) -> bool:
        return self.accepts_word(encode_lsd(value))

    def digest(self) -> str:
        payload = {
            "start": self.start,
            "transitions": self.transitions,
            "accepting": sorted(self.accepting),
        }
        encoded = json.dumps(payload, sort_keys=True, separators=(",", ":"))
        return hashlib.sha256(encoded.encode("utf-8")).hexdigest()


def minimize_dfa(dfa: DFA) -> tuple[DFA, tuple[int, ...]]:
    """Moore-minimize a reachable DFA and return the old-to-new state map."""
    reachable: list[int] = []
    seen = {dfa.start}
    queue = deque([dfa.start])
    while queue:
        state = queue.popleft()
        reachable.append(state)
        for target in dfa.transitions[state]:
            if target not in seen:
                seen.add(target)
                queue.append(target)

    rejecting = frozenset(state for state in reachable if state not in dfa.accepting)
    accepting = frozenset(state for state in reachable if state in dfa.accepting)
    partition = [block for block in (rejecting, accepting) if block]

    while True:
        block_of = {
            state: index
            for index, block in enumerate(partition)
            for state in block
        }
        refined: list[frozenset[int]] = []
        for block in partition:
            buckets: dict[tuple[int, int], set[int]] = {}
            for state in sorted(block):
                signature = tuple(
                    block_of[target] for target in dfa.transitions[state]
                )
                buckets.setdefault(signature, set()).add(state)
            refined.extend(
                frozenset(bucket)
                for _, bucket in sorted(
                    buckets.items(), key=lambda item: min(item[1])
                )
            )
        if refined == partition:
            break
        partition = refined

    block_of = {
        state: index
        for index, block in enumerate(partition)
        for state in block
    }
    block_transitions = tuple(
        tuple(block_of[dfa.transitions[min(block)][bit]] for bit in (0, 1))
        for block in partition
    )
    start_block = block_of[dfa.start]

    block_order: list[int] = []
    seen_blocks = {start_block}
    queue = deque([start_block])
    while queue:
        block = queue.popleft()
        block_order.append(block)
        for target in block_transitions[block]:
            if target not in seen_blocks:
                seen_blocks.add(target)
                queue.append(target)
    rename = {old: new for new, old in enumerate(block_order)}

    minimized = DFA(
        transitions=tuple(
            tuple(rename[target] for target in block_transitions[block])
            for block in block_order
        ),
        accepting=frozenset(
            rename[block]
            for block in block_order
            if min(partition[block]) in dfa.accepting
        ),
        start=0,
    )
    old_to_new = tuple(
        rename[block_of[state]] if state in seen else -1
        for state in range(dfa.state_count)
    )
    return minimized, old_to_new


@dataclass(frozen=True)
class SafetyAutomaton:
    dfa: DFA
    tail_states: frozenset[int]
    raw_state_count: int


def build_safety_dfa(forbidden_values: Iterable[int]) -> SafetyAutomaton:
    """Minimal DFA for canonical positives minus finite forbidden values."""
    children: list[dict[int, int]] = [{}]
    last_bit: list[int | None] = [None]
    exact_forbidden: set[int] = set()

    values = sorted(set(forbidden_values))
    if not values or any(value <= 0 for value in values):
        raise ValueError("forbidden_values must be nonempty positive integers")

    for value in values:
        state = 0
        for bit in encode_lsd(value):
            target = children[state].get(bit)
            if target is None:
                target = len(children)
                children[state][bit] = target
                children.append({})
                last_bit.append(bit)
            state = target
        exact_forbidden.add(state)

    free_zero = len(children)
    free_one = free_zero + 1
    transitions: list[tuple[int, int]] = []
    for state, edges in enumerate(children):
        transitions.append(
            (
                edges.get(0, free_zero),
                edges.get(1, free_one),
            )
        )
    transitions.extend(((free_zero, free_one), (free_zero, free_one)))

    accepting = {
        state
        for state in range(1, len(children))
        if last_bit[state] == 1 and state not in exact_forbidden
    }
    accepting.add(free_one)
    raw = DFA(tuple(transitions), frozenset(accepting))
    minimized, old_to_new = minimize_dfa(raw)
    tail_states = frozenset(
        (old_to_new[free_zero], old_to_new[free_one])
    )
    if len(tail_states) != 2:
        raise AssertionError("canonical zero/one tail residuals unexpectedly merged")
    return SafetyAutomaton(minimized, tail_states, raw.state_count)


def strongly_connected_components(dfa: DFA) -> list[frozenset[int]]:
    """Kosaraju SCC decomposition with deterministic component ordering."""
    sys.setrecursionlimit(max(10_000, 4 * dfa.state_count))
    seen: set[int] = set()
    order: list[int] = []

    def forward(state: int) -> None:
        seen.add(state)
        for target in dfa.transitions[state]:
            if target not in seen:
                forward(target)
        order.append(state)

    for state in range(dfa.state_count):
        if state not in seen:
            forward(state)

    reverse: list[set[int]] = [set() for _ in range(dfa.state_count)]
    for state, row in enumerate(dfa.transitions):
        for target in row:
            reverse[target].add(state)

    components: list[frozenset[int]] = []
    seen.clear()

    def backward(state: int, component: set[int]) -> None:
        seen.add(state)
        component.add(state)
        for source in reverse[state]:
            if source not in seen:
                backward(source, component)

    for state in reversed(order):
        if state not in seen:
            component: set[int] = set()
            backward(state, component)
            components.append(frozenset(component))
    return components


def distance_to_tail(dfa: DFA, tail_states: frozenset[int]) -> dict[int, int]:
    """Shortest transition distance from each state to the tail component."""
    reverse: list[set[int]] = [set() for _ in range(dfa.state_count)]
    for state, row in enumerate(dfa.transitions):
        for target in row:
            reverse[target].add(state)
    distance = {state: 0 for state in tail_states}
    queue = deque(sorted(tail_states))
    while queue:
        target = queue.popleft()
        for source in sorted(reverse[target]):
            if source not in distance:
                distance[source] = distance[target] + 1
                queue.append(source)
    return distance


def audit_depth(depth: int, forbidden: frozenset[int]) -> dict[str, object]:
    safety = build_safety_dfa(forbidden)
    dfa = safety.dfa
    components = strongly_connected_components(dfa)
    component_of = {
        state: index
        for index, component in enumerate(components)
        for state in component
    }
    tail_component = components[component_of[next(iter(safety.tail_states))]]
    if not safety.tail_states <= tail_component:
        raise AssertionError("tail residuals are not strongly connected")

    cyclic_components = [
        component
        for component in components
        if len(component) > 1
        or any(dfa.transitions[state][bit] == state for state in component for bit in (0, 1))
    ]
    if cyclic_components != [tail_component]:
        raise AssertionError("a non-tail cycle survived in a cofinite automaton")
    if any(
        target not in tail_component
        for state in tail_component
        for target in dfa.transitions[state]
    ):
        raise AssertionError("the canonical tail component is not terminal")

    distances = distance_to_tail(dfa, tail_component)
    if len(distances) != dfa.state_count:
        raise AssertionError("some minimized state cannot reach the tail")
    boundary_states = set(range(dfa.state_count)) - set(tail_component)
    distance_profile = Counter(distances[state] for state in boundary_states)

    max_forbidden = max(forbidden)
    expected_max = 1 << (depth + 1)
    if max_forbidden != expected_max:
        raise AssertionError((depth, max_forbidden, expected_max))

    safe_power = 1 << (depth + 2)
    unsafe_image = direct_shortcut(safe_power)
    if not direct_avoids(safe_power, depth):
        raise AssertionError("the advertised safe power is not depth-safe")
    if direct_avoids(unsafe_image, depth):
        raise AssertionError("the advertised image is unexpectedly depth-safe")
    if not dfa.accepts_value(safe_power) or dfa.accepts_value(unsafe_image):
        raise AssertionError("DFA disagrees on the exact one-step witness")

    return {
        "depth": depth,
        "forbidden_count": len(forbidden),
        "max_forbidden": max_forbidden,
        "cofinite_threshold": max_forbidden + 1,
        "minimal_states": dfa.state_count,
        "raw_trie_states": safety.raw_state_count,
        "tail_component_states": len(tail_component),
        "boundary_states": len(boundary_states),
        "boundary_is_acyclic": True,
        "max_shortest_distance_to_tail": max(
            (distances[state] for state in boundary_states), default=0
        ),
        "boundary_distance_profile": {
            str(distance): count
            for distance, count in sorted(distance_profile.items())
        },
        "one_step_nonclosure_witness": {
            "input": safe_power,
            "input_lsd": "".join(map(str, encode_lsd(safe_power))),
            "output": unsafe_image,
            "output_lsd": "".join(map(str, encode_lsd(unsafe_image))),
        },
        "dfa_sha256": dfa.digest(),
    }


def build_summary(max_depth: int) -> dict[str, object]:
    rows = [
        audit_depth(depth, forbidden)
        for depth, forbidden in enumerate(forbidden_levels(max_depth))
    ]
    return {
        "experiment": "X-9201",
        "classification": "exact finite computation; no counterexample claim",
        "issue_path": "#8 safety-automata widening",
        "agent": "gpt56-sol-01",
        "map": "shortcut 3n+1",
        "bit_order": "lsd_first",
        "inspected_orbit_times": "0 through depth, inclusive",
        "max_depth": max_depth,
        "environment": {
            "python": platform.python_version(),
            "platform": platform.platform(),
        },
        "rows": rows,
        "aggregate": {
            "all_tail_components_have_two_states": all(
                row["tail_component_states"] == 2 for row in rows
            ),
            "all_sink_stripped_boundaries_are_acyclic": all(
                row["boundary_is_acyclic"] for row in rows
            ),
            "all_approximants_have_explicit_one_step_nonclosure_witnesses": True,
        },
        "interpretation": [
            "Each finite safety approximant is canonical-positive minus a finite reverse tree.",
            "Its only recurrent input component is the universal two-state canonical tail.",
            "Retaining that cofinite tail cannot yield a safe forward-invariant language.",
            "Quotient learning should strip the tail and compare boundary DAGs across depths.",
        ],
        "limitations": [
            "Finite-depth avoidance does not establish an infinite surviving orbit.",
            "Acyclic boundary profiles neither prove nor disprove existence of a regular sanctuary.",
            "This experiment does not synthesize a candidate language.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-depth", type=int, default=32)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).resolve().parent / "results" / "summary.json",
    )
    args = parser.parse_args()
    if not 0 <= args.max_depth <= 64:
        parser.error("--max-depth must be between 0 and 64")

    summary = build_summary(args.max_depth)
    mathematical = {key: value for key, value in summary.items() if key != "environment"}
    digest = hashlib.sha256(
        json.dumps(mathematical, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()
    payload = {
        "sha256_of_mathematical_results": digest,
        "summary": summary,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    final = summary["rows"][-1]
    print(
        f"X-9201 depths=0..{args.max_depth} "
        f"final_forbidden={final['forbidden_count']} "
        f"final_states={final['minimal_states']} "
        f"final_boundary={final['boundary_states']} "
        f"sha256={digest}"
    )


if __name__ == "__main__":
    main()
