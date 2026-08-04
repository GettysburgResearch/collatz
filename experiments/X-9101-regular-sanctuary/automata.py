"""Small, exact finite-automata primitives for experiment X-9101.

Words are tuples of integer bits in least-significant-digit-first order.  A
candidate DFA is interpreted semantically by ``verify.py`` as its raw language
intersected with the canonical positive encodings ``{0,1}*1``.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Iterable, Iterator, Sequence


Bit = int
Word = tuple[Bit, ...]


def normalize_word(word: Sequence[int] | str) -> Word:
    if isinstance(word, str):
        if any(char not in "01" for char in word):
            raise ValueError(f"not a binary word: {word!r}")
        return tuple(int(char) for char in word)
    bits = tuple(word)
    if any(type(bit) is not int or bit not in (0, 1) for bit in bits):
        raise ValueError(f"not a binary word: {word!r}")
    return bits


def is_canonical_positive(word: Sequence[int] | str) -> bool:
    bits = normalize_word(word)
    return bool(bits) and bits[-1] == 1


def encode_lsd(value: int) -> Word:
    if value <= 0:
        raise ValueError("canonical positive encoding requires value > 0")
    return tuple(int(char) for char in reversed(bin(value)[2:]))


def decode_lsd(
    word: Sequence[int] | str, *, require_canonical: bool = True
) -> int:
    bits = normalize_word(word)
    if require_canonical and not is_canonical_positive(bits):
        raise ValueError(f"not a canonical positive LSD-first word: {bits!r}")
    return sum(bit << index for index, bit in enumerate(bits))


def word_text(word: Sequence[int] | str) -> str:
    return "".join(str(bit) for bit in normalize_word(word))


@dataclass(frozen=True)
class DFA:
    """A complete deterministic automaton over the alphabet ``{0,1}``."""

    transitions: tuple[tuple[int, int], ...]
    accepting: frozenset[int]
    start: int = 0

    def __post_init__(self) -> None:
        count = len(self.transitions)
        if count == 0:
            raise ValueError("a DFA must have at least one state")
        if type(self.start) is not int or not 0 <= self.start < count:
            raise ValueError("start state is outside the DFA")
        for row in self.transitions:
            if len(row) != 2:
                raise ValueError("each DFA state needs transitions on 0 and 1")
            if any(
                type(target) is not int or not 0 <= target < count for target in row
            ):
                raise ValueError("DFA transition target is outside the DFA")
        if any(
            type(state) is not int or not 0 <= state < count
            for state in self.accepting
        ):
            raise ValueError("accepting state is outside the DFA")

    @property
    def state_count(self) -> int:
        return len(self.transitions)

    def step(self, state: int, bit: int) -> int:
        if bit not in (0, 1):
            raise ValueError(f"invalid input bit: {bit!r}")
        return self.transitions[state][bit]

    def run(self, word: Sequence[int] | str, state: int | None = None) -> int:
        current = self.start if state is None else state
        for bit in normalize_word(word):
            current = self.step(current, bit)
        return current

    def accepts_raw(self, word: Sequence[int] | str) -> bool:
        return self.run(word) in self.accepting

    def accepts_canonical(self, word: Sequence[int] | str) -> bool:
        bits = normalize_word(word)
        return is_canonical_positive(bits) and self.accepts_raw(bits)

    def with_accepting(self, accepting: Iterable[int]) -> "DFA":
        return DFA(self.transitions, frozenset(accepting), self.start)

    def complement(self) -> "DFA":
        return self.with_accepting(set(range(self.state_count)) - self.accepting)

    def canonicalized(self) -> "DFA":
        """Drop unreachable states and number the rest in BFS order."""

        order: list[int] = []
        seen = {self.start}
        queue = deque([self.start])
        while queue:
            state = queue.popleft()
            order.append(state)
            for bit in (0, 1):
                target = self.step(state, bit)
                if target not in seen:
                    seen.add(target)
                    queue.append(target)

        rename = {old: new for new, old in enumerate(order)}
        transitions = tuple(
            tuple(rename[self.step(old, bit)] for bit in (0, 1)) for old in order
        )
        accepting = frozenset(rename[state] for state in self.accepting if state in seen)
        return DFA(transitions, accepting, 0)

    def minimized(self) -> "DFA":
        """Return the reachable Moore-minimized DFA."""

        dfa = self.canonicalized()
        block = [int(state in dfa.accepting) for state in range(dfa.state_count)]

        while True:
            signatures: dict[tuple[int, int, int], int] = {}
            refined: list[int] = []
            for state in range(dfa.state_count):
                signature = (
                    int(state in dfa.accepting),
                    block[dfa.step(state, 0)],
                    block[dfa.step(state, 1)],
                )
                if signature not in signatures:
                    signatures[signature] = len(signatures)
                refined.append(signatures[signature])
            if refined == block:
                break
            block = refined

        representatives: dict[int, int] = {}
        for state, group in enumerate(block):
            representatives.setdefault(group, state)
        groups = sorted(representatives)
        renumber = {group: index for index, group in enumerate(groups)}
        transitions = tuple(
            tuple(
                renumber[block[dfa.step(representatives[group], bit)]]
                for bit in (0, 1)
            )
            for group in groups
        )
        accepting = frozenset(
            renumber[group]
            for group, representative in representatives.items()
            if representative in dfa.accepting
        )
        start = renumber[block[dfa.start]]
        return DFA(transitions, accepting, start).canonicalized()

    def to_dict(self) -> dict[str, object]:
        return {
            "alphabet": [0, 1],
            "bit_order": "lsd_first",
            "start": self.start,
            "transitions": [list(row) for row in self.transitions],
            "accepting": sorted(self.accepting),
        }

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "DFA":
        alphabet = data.get("alphabet")
        if (
            not isinstance(alphabet, list)
            or any(type(symbol) is not int for symbol in alphabet)
            or alphabet != [0, 1]
        ):
            raise ValueError("certificate alphabet must be [0, 1]")
        if data.get("bit_order") != "lsd_first":
            raise ValueError("certificate must declare lsd_first bit order")
        raw_transitions = data.get("transitions")
        raw_accepting = data.get("accepting")
        start = data.get("start", 0)
        if type(start) is not int:
            raise ValueError("certificate start state must be an integer")
        if not isinstance(raw_transitions, list) or not isinstance(raw_accepting, list):
            raise ValueError("malformed DFA certificate")
        if any(
            not isinstance(row, list)
            or len(row) != 2
            or any(type(target) is not int for target in row)
            for row in raw_transitions
        ):
            raise ValueError("certificate transitions must be integer pairs")
        if any(type(state) is not int for state in raw_accepting):
            raise ValueError("certificate accepting states must be integers")
        transitions = tuple(tuple(row) for row in raw_transitions)
        accepting = frozenset(raw_accepting)
        return cls(transitions, accepting, start)


def universal_dfa() -> DFA:
    return DFA(((0, 0),), frozenset({0}))


def empty_dfa() -> DFA:
    return DFA(((0, 0),), frozenset())


def canonical_positive_dfa() -> DFA:
    # 0 = empty, 1 = nonempty ending in 0, 2 = ending in 1.
    return DFA(((1, 2), (1, 2), (1, 2)), frozenset({2}))


def product_dfa(left: DFA, right: DFA) -> DFA:
    """Intersection product, with pair index ``l * right.states + r``."""

    right_count = right.state_count

    def index(left_state: int, right_state: int) -> int:
        return left_state * right_count + right_state

    transitions: list[tuple[int, int]] = []
    for left_state in range(left.state_count):
        for right_state in range(right.state_count):
            transitions.append(
                tuple(
                    index(
                        left.step(left_state, bit), right.step(right_state, bit)
                    )
                    for bit in (0, 1)
                )
            )
    accepting = frozenset(
        index(left_state, right_state)
        for left_state in left.accepting
        for right_state in right.accepting
    )
    return DFA(
        tuple(transitions), accepting, index(left.start, right.start)
    ).canonicalized()


def finite_language_dfa(words: Iterable[Sequence[int] | str]) -> DFA:
    """Build a complete trie DFA for exactly the supplied finite words."""

    trie: list[dict[int, int]] = [{}]
    accepting: set[int] = set()
    for raw_word in words:
        state = 0
        for bit in normalize_word(raw_word):
            target = trie[state].get(bit)
            if target is None:
                target = len(trie)
                trie[state][bit] = target
                trie.append({})
            state = target
        accepting.add(state)

    dead = len(trie)
    transitions: list[tuple[int, int]] = []
    for edges in trie:
        transitions.append(tuple(edges.get(bit, dead) for bit in (0, 1)))
    transitions.append((dead, dead))
    return DFA(tuple(transitions), frozenset(accepting)).minimized()


def without_finite_words(words: Iterable[Sequence[int] | str]) -> DFA:
    return finite_language_dfa(words).complement().minimized()


def shortest_canonical_word(
    dfa: DFA, *, allowed_states: frozenset[int] | None = None
) -> Word | None:
    """Shortest-length canonical witness; LSD-lexicographic among ties.

    This is not necessarily the numerically least accepted integer because the
    input is least-significant-digit first.
    """

    targets = dfa.accepting if allowed_states is None else allowed_states
    # Monitor: 0 = empty, 1 = last bit 0, 2 = last bit 1.
    start = (dfa.start, 0)
    queue = deque([start])
    parent: dict[tuple[int, int], tuple[tuple[int, int], int] | None] = {start: None}

    while queue:
        state, monitor = queue.popleft()
        if monitor == 2 and state in targets:
            bits: list[int] = []
            current = (state, monitor)
            while parent[current] is not None:
                previous, bit = parent[current]  # type: ignore[misc]
                bits.append(bit)
                current = previous
            return tuple(reversed(bits))
        for bit in (0, 1):
            target = (dfa.step(state, bit), 1 if bit == 0 else 2)
            if target not in parent:
                parent[target] = ((state, monitor), bit)
                queue.append(target)
    return None


def threshold_core_dfa(core: DFA, minimum_length: int) -> tuple[DFA, frozenset[int]]:
    """Product a core with a saturating length guard.

    The returned forbidden set contains every expanded state reached before
    ``minimum_length`` bits.  Supplying it to the maximal-safe-kernel routine
    forces the synthesized language to respect that threshold.
    """

    if minimum_length < 1:
        raise ValueError("minimum_length must be positive")
    core_count = core.state_count

    def index(length_state: int, core_state: int) -> int:
        return length_state * core_count + core_state

    transitions: list[tuple[int, int]] = []
    for length_state in range(minimum_length + 1):
        next_length = min(minimum_length, length_state + 1)
        for core_state in range(core_count):
            transitions.append(
                tuple(
                    index(next_length, core.step(core_state, bit))
                    for bit in (0, 1)
                )
            )
    forbidden = frozenset(
        index(length_state, core_state)
        for length_state in range(minimum_length)
        for core_state in range(core_count)
    )
    expanded = DFA(tuple(transitions), frozenset(), index(0, core.start))
    return expanded, forbidden


def transition_skeletons(state_count: int) -> Iterator[DFA]:
    """Enumerate all labeled complete transition skeletons of a given size."""

    if state_count < 1:
        raise ValueError("state_count must be positive")
    from itertools import product

    for flat in product(range(state_count), repeat=2 * state_count):
        transitions = tuple(
            (flat[2 * state], flat[2 * state + 1])
            for state in range(state_count)
        )
        yield DFA(transitions, frozenset())
