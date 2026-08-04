#!/usr/bin/env python3
"""Exact checks for L-0015 and T-0020.

This is a small independent bridge, not a replacement for PR #12's full
regular-sanctuary verifier.  It demonstrates the exact compilation from a
regular language of finite interval endpoints to a regular language of interval
lengths, and it replays the shortcut-map closure relation on the compiled DFA.

Binary words are least-significant digit first.  A pair symbol is encoded as
2*v_bit + q_bit, so the alphabet 0,1,2,3 represents 00,01,10,11.
"""

from __future__ import annotations

from collections import defaultdict, deque
from dataclasses import dataclass
import random
from typing import Iterable, Sequence


Word = tuple[int, ...]
PairWord = tuple[int, ...]


def encode_lsd(value: int) -> Word:
    if value <= 0:
        raise ValueError("positive canonical integer required")
    return tuple(int(ch) for ch in reversed(bin(value)[2:]))


def decode_lsd(word: Sequence[int]) -> int:
    if not word or word[-1] != 1:
        raise ValueError("noncanonical LSD-first word")
    return sum(bit << i for i, bit in enumerate(word))


def encode_pair(v: int, q: int) -> PairWord:
    if v < 0 or q < 0 or (v == 0 and q == 0):
        raise ValueError("nonzero nonnegative endpoint pair required")
    length = max(v.bit_length(), q.bit_length())
    return tuple(
        2 * ((v >> i) & 1) + ((q >> i) & 1)
        for i in range(length)
    )


@dataclass(frozen=True)
class DFA:
    """Complete DFA over bits 0,1 with canonical-positive semantics at use sites."""

    transitions: tuple[tuple[int, int], ...]
    accepting: frozenset[int]
    start: int = 0

    @property
    def state_count(self) -> int:
        return len(self.transitions)

    def step(self, state: int, symbol: int) -> int:
        return self.transitions[state][symbol]

    def run(self, word: Sequence[int]) -> int:
        state = self.start
        for symbol in word:
            state = self.step(state, symbol)
        return state

    def accepts_canonical(self, word: Sequence[int]) -> bool:
        return bool(word) and word[-1] == 1 and self.run(word) in self.accepting


@dataclass(frozen=True)
class PairDFA:
    """Complete DFA over the convolution alphabet 00,01,10,11."""

    transitions: tuple[tuple[int, int, int, int], ...]
    accepting: frozenset[int]
    start: int = 0

    @property
    def state_count(self) -> int:
        return len(self.transitions)

    def step(self, state: int, symbol: int) -> int:
        return self.transitions[state][symbol]


def finite_pair_dfa(words: Iterable[PairWord]) -> PairDFA:
    """Trie DFA for an exact finite language of endpoint convolutions."""

    trie: list[dict[int, int]] = [{}]
    accepting: set[int] = set()

    for word in words:
        state = 0
        for symbol in word:
            if symbol not in range(4):
                raise ValueError("invalid pair symbol")
            if symbol not in trie[state]:
                trie[state][symbol] = len(trie)
                trie.append({})
            state = trie[state][symbol]
        accepting.add(state)

    sink = len(trie)
    trie.append({})
    transitions: list[tuple[int, int, int, int]] = []
    for state, row in enumerate(trie):
        if state == sink:
            transitions.append((sink, sink, sink, sink))
        else:
            transitions.append(
                tuple(row.get(symbol, sink) for symbol in range(4))
            )
    return PairDFA(tuple(transitions), frozenset(accepting))


def fixed_gauge_all_positive_pair_dfa() -> PairDFA:
    """Accept exactly conv(1,q) with q>=2, i.e. intervals [1,q) of positive length."""

    sink = 4
    transitions = (
        (sink, sink, 1, 1),       # first pair bit has v_0=1
        (2, 3, sink, sink),       # at least one high q bit follows
        (2, 3, sink, sink),       # current high q bit is 0
        (2, 3, sink, sink),       # current high q bit is 1
        (sink, sink, sink, sink),
    )
    return PairDFA(transitions, frozenset({3}))


def project_interval_lengths(pair_dfa: PairDFA) -> DFA:
    """Compile a pair-language DFA to the canonical language of q-v.

    The product NFA existentially guesses endpoint bits and enforces v+n=q
    with one binary carry.  It first accepts padded n tracks of the same length
    as the endpoint convolution.  A right quotient by 0* removes high zero
    padding, after which a three-state monitor enforces canonical positivity.
    """

    product_states = [
        (pair_state, carry)
        for pair_state in range(pair_dfa.state_count)
        for carry in (0, 1)
    ]
    index = {state: i for i, state in enumerate(product_states)}
    nfa: list[list[set[int]]] = [
        [set(), set()] for _ in product_states
    ]

    for pair_state, carry in product_states:
        source = index[(pair_state, carry)]
        for n_bit in (0, 1):
            for v_bit in (0, 1):
                for q_bit in (0, 1):
                    total = v_bit + n_bit + carry
                    if total % 2 != q_bit:
                        continue
                    next_carry = total // 2
                    target_pair = pair_dfa.step(
                        pair_state, 2 * v_bit + q_bit
                    )
                    nfa[source][n_bit].add(
                        index[(target_pair, next_carry)]
                    )

    exact_accepting = {
        index[(state, 0)] for state in pair_dfa.accepting
    }

    # Right quotient by 0*: a prefix is accepted when some all-zero high
    # padding reaches an exact padded endpoint.
    reverse_zero: list[set[int]] = [set() for _ in product_states]
    for source, rows in enumerate(nfa):
        for target in rows[0]:
            reverse_zero[target].add(source)

    quotient_accepting = set(exact_accepting)
    queue = deque(exact_accepting)
    while queue:
        target = queue.popleft()
        for source in reverse_zero[target]:
            if source not in quotient_accepting:
                quotient_accepting.add(source)
                queue.append(source)

    initial_subset = frozenset(
        {index[(pair_dfa.start, 0)]}
    )

    # Status: 0 empty, 1 nonempty ending in 0, 2 ending in 1.
    start = (initial_subset, 0)
    state_ids = {start: 0}
    queue = deque([start])
    transitions: list[tuple[int, int]] = []
    accepting: set[int] = set()

    while queue:
        subset, status = queue.popleft()
        state_id = state_ids[(subset, status)]
        row: list[int] = []

        for bit in (0, 1):
            target_subset: set[int] = set()
            for source in subset:
                target_subset.update(nfa[source][bit])
            target = (frozenset(target_subset), 1 if bit == 0 else 2)
            if target not in state_ids:
                state_ids[target] = len(state_ids)
                queue.append(target)
            row.append(state_ids[target])

        transitions.append(tuple(row))
        if status == 2 and subset.intersection(quotient_accepting):
            accepting.add(state_id)

    return DFA(tuple(transitions), frozenset(accepting))


# Exact shortcut subsequential transducer, independently restated from PR #12.
TRANSDUCER_TRANSITIONS = {
    ("S", 0): ("E", ()),
    ("S", 1): ("C2", ()),
    ("E", 0): ("E", (0,)),
    ("E", 1): ("E", (1,)),
    ("C0", 0): ("C0", (0,)),
    ("C0", 1): ("C1", (1,)),
    ("C1", 0): ("C0", (1,)),
    ("C1", 1): ("C2", (0,)),
    ("C2", 0): ("C1", (0,)),
    ("C2", 1): ("C2", (1,)),
}
TRANSDUCER_FINAL = {
    "S": None,
    "E": (),
    "C0": (),
    "C1": (1,),
    "C2": (0, 1),
}


def closure_witness(dfa: DFA) -> Word | None:
    """Return a shortest canonical w with w accepted but T(w) rejected."""

    # (input DFA, transducer, output DFA, input monitor, output monitor)
    start = (dfa.start, "S", dfa.start, 0, 0)
    queue = deque([start])
    predecessor = {start: None}
    predecessor_bit: dict[tuple[object, ...], int] = {}

    while queue:
        state = queue.popleft()
        q_in, transducer, q_out, input_status, output_status = state

        if input_status == 2 and q_in in dfa.accepting:
            final = TRANSDUCER_FINAL[transducer]
            if final is None:
                raise AssertionError("undefined terminal output on canonical input")
            flushed_state = q_out
            flushed_status = output_status
            for bit in final:
                flushed_state = dfa.step(flushed_state, bit)
                flushed_status = 1 if bit == 0 else 2

            if flushed_status != 2 or flushed_state not in dfa.accepting:
                word: list[int] = []
                cursor = state
                while predecessor[cursor] is not None:
                    word.append(predecessor_bit[cursor])
                    cursor = predecessor[cursor]
                return tuple(reversed(word))

        for bit in (0, 1):
            next_transducer, emitted = TRANSDUCER_TRANSITIONS[
                (transducer, bit)
            ]
            next_input = dfa.step(q_in, bit)
            next_output = q_out
            next_output_status = output_status
            for out_bit in emitted:
                next_output = dfa.step(next_output, out_bit)
                next_output_status = 1 if out_bit == 0 else 2

            target = (
                next_input,
                next_transducer,
                next_output,
                1 if bit == 0 else 2,
                next_output_status,
            )
            if target not in predecessor:
                predecessor[target] = state
                predecessor_bit[target] = bit
                queue.append(target)

    return None


def endpoint_relation(dfa: DFA) -> set[tuple[int, int]]:
    """Exact raw-state relation induced by one shortcut step."""

    start = (dfa.start, "S", dfa.start, 0, 0)
    queue = deque([start])
    seen = {start}
    relation: set[tuple[int, int]] = set()

    while queue:
        q_in, transducer, q_out, input_status, output_status = queue.popleft()

        if input_status == 2:
            final = TRANSDUCER_FINAL[transducer]
            if final is None:
                raise AssertionError("undefined terminal output")
            flushed_state = q_out
            flushed_status = output_status
            for bit in final:
                flushed_state = dfa.step(flushed_state, bit)
                flushed_status = 1 if bit == 0 else 2
            if flushed_status != 2:
                raise AssertionError("noncanonical shortcut output")
            relation.add((q_in, flushed_state))

        for bit in (0, 1):
            next_transducer, emitted = TRANSDUCER_TRANSITIONS[
                (transducer, bit)
            ]
            next_input = dfa.step(q_in, bit)
            next_output = q_out
            next_output_status = output_status
            for out_bit in emitted:
                next_output = dfa.step(next_output, out_bit)
                next_output_status = 1 if out_bit == 0 else 2

            target = (
                next_input,
                next_transducer,
                next_output,
                1 if bit == 0 else 2,
                next_output_status,
            )
            if target not in seen:
                seen.add(target)
                queue.append(target)

    return relation


def maximal_safe_states(dfa: DFA) -> set[int]:
    """Greatest raw-state kernel avoiding canonical 1 and 2."""

    relation = endpoint_relation(dfa)
    forbidden = {
        dfa.run(encode_lsd(1)),
        dfa.run(encode_lsd(2)),
    }
    reverse: dict[int, set[int]] = defaultdict(set)
    for source, target in relation:
        reverse[target].add(source)

    unsafe = set(forbidden)
    queue = deque(forbidden)
    while queue:
        target = queue.popleft()
        for source in reverse[target]:
            if source not in unsafe:
                unsafe.add(source)
                queue.append(source)

    return set(range(dfa.state_count)) - unsafe


def shortest_canonical_word_to_states(
    dfa: DFA, target_states: set[int]
) -> Word | None:
    """Return a shortest canonical word ending in target_states, if one exists."""

    start = (dfa.start, 0)  # status: 0 empty, 1 last 0, 2 last 1
    queue = deque([start])
    predecessor = {start: None}
    predecessor_bit: dict[tuple[int, int], int] = {}

    while queue:
        state, status = queue.popleft()
        if status == 2 and state in target_states:
            word: list[int] = []
            cursor = (state, status)
            while predecessor[cursor] is not None:
                word.append(predecessor_bit[cursor])
                cursor = predecessor[cursor]
            return tuple(reversed(word))

        for bit in (0, 1):
            target = (dfa.step(state, bit), 1 if bit == 0 else 2)
            if target not in predecessor:
                predecessor[target] = (state, status)
                predecessor_bit[target] = bit
                queue.append(target)

    return None


def accepted_values(dfa: DFA, limit: int) -> set[int]:
    return {
        value
        for value in range(1, limit + 1)
        if dfa.accepts_canonical(encode_lsd(value))
    }


def finite_pair_projection_checks() -> None:
    rng = random.Random(20260721)

    for _ in range(64):
        pairs: set[tuple[int, int]] = set()
        for _ in range(40):
            v = rng.randint(1, 96)
            q = rng.randint(v + 1, 192)
            pairs.add((v, q))

        pair_dfa = finite_pair_dfa(
            encode_pair(v, q) for v, q in pairs
        )
        length_dfa = project_interval_lengths(pair_dfa)
        expected = {q - v for v, q in pairs}
        got = accepted_values(length_dfa, 192)
        assert got == expected

    # Multiple gauges of the same physical lengths are correctly deduplicated.
    pairs = {
        (1, 2),      # length 1
        (1, 3),      # length 2
        (1, 4),      # length 3
        (5, 8),      # another gauge for length 3
        (13, 21),    # length 8
        (100, 108),  # another gauge for length 8
    }
    compiled = project_interval_lengths(
        finite_pair_dfa(encode_pair(v, q) for v, q in pairs)
    )
    assert accepted_values(compiled, 32) == {1, 2, 3, 8}


def infinite_regular_control_checks() -> tuple[int, int]:
    pair_dfa = fixed_gauge_all_positive_pair_dfa()
    length_dfa = project_interval_lengths(pair_dfa)

    assert accepted_values(length_dfa, 4096) == set(range(1, 4097))
    assert closure_witness(length_dfa) is None
    safe = maximal_safe_states(length_dfa)
    assert shortest_canonical_word_to_states(length_dfa, safe) is None

    return pair_dfa.state_count, length_dfa.state_count


def finite_phase_normalization_check() -> int:
    """Replay the finite-block normalization on the terminal two-cycle."""

    def shortcut(n: int) -> int:
        return n // 2 if n % 2 == 0 else (3 * n + 1) // 2

    checkpoint = {1, 2}
    block_length = 2
    assert {shortcut(shortcut(n)) for n in checkpoint} == checkpoint

    normalized = {
        n
        for start in checkpoint
        for n in (start, shortcut(start))
    }
    assert normalized == {1, 2}
    assert {shortcut(n) for n in normalized} == normalized
    return len(normalized)


def main() -> None:
    finite_pair_projection_checks()
    print("verified exact regular interval-length projection")

    pair_states, length_states = infinite_regular_control_checks()
    print(
        "compiled fixed-gauge all-positive intervals:",
        f"pair_states={pair_states}",
        f"length_states={length_states}",
    )
    print("verified exact shortcut closure and empty safe kernel")

    size = finite_phase_normalization_check()
    print(f"verified finite-block normalization on {size}-value control")
    print("all regular-marked-collapse checks passed")


if __name__ == "__main__":
    main()
