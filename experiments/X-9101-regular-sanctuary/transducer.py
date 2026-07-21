"""Exact subsequential transducers for shortcut ``3n +/- 1`` maps.

The machines consume and emit canonical binary words least-significant digit
first.  A transition consumes exactly one input bit and may emit zero or one
output bit.  A terminal output flushes the bounded multiplication carry.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, Sequence

from automata import Word, is_canonical_positive, normalize_word


@dataclass(frozen=True)
class SubsequentialTransducer:
    name: str
    state_count: int
    start: int
    transitions: Mapping[tuple[int, int], tuple[int, Word]]
    terminal_outputs: Mapping[int, Word]

    def __post_init__(self) -> None:
        if self.state_count < 1:
            raise ValueError("a transducer must have at least one state")
        if not 0 <= self.start < self.state_count:
            raise ValueError("transducer start state is invalid")
        for state in range(self.state_count):
            for bit in (0, 1):
                transition = self.transitions.get((state, bit))
                if transition is None:
                    raise ValueError(
                        f"transducer is incomplete at state {state}, bit {bit}"
                    )
                target, output = transition
                if not 0 <= target < self.state_count:
                    raise ValueError("transducer target state is invalid")
                normalize_word(output)
        for state, output in self.terminal_outputs.items():
            if not 0 <= state < self.state_count:
                raise ValueError("terminal state is invalid")
            normalize_word(output)

    def step(self, state: int, bit: int) -> tuple[int, Word]:
        if bit not in (0, 1):
            raise ValueError(f"invalid input bit: {bit!r}")
        return self.transitions[(state, bit)]

    def terminal_output(self, state: int) -> Word | None:
        return self.terminal_outputs.get(state)

    def transduce(
        self, word: Sequence[int] | str, *, require_canonical: bool = True
    ) -> Word:
        bits = normalize_word(word)
        if require_canonical and not is_canonical_positive(bits):
            raise ValueError(f"noncanonical input to {self.name}: {bits!r}")
        state = self.start
        output: list[int] = []
        for bit in bits:
            state, emitted = self.step(state, bit)
            output.extend(emitted)
        terminal = self.terminal_output(state)
        if terminal is None:
            raise ValueError(f"input has no terminal output in {self.name}")
        output.extend(terminal)
        result = tuple(output)
        if require_canonical and not is_canonical_positive(result):
            raise AssertionError(
                f"{self.name} emitted noncanonical output {result!r}"
            )
        return result


# State names, kept numeric so product searches remain compact.
START = 0
EVEN_COPY = 1
CARRY_0 = 2
CARRY_1 = 3
CARRY_2 = 4


def shortcut_transducer(odd_offset: int = 1) -> SubsequentialTransducer:
    """Return the exact shortcut map for odd branch ``(3n+offset)/2``.

    Supported offsets are ``+1`` (the standard shortcut Collatz map) and ``-1``
    (a positive-control map containing the cycle 5 -> 7 -> 10 -> 5).
    """

    if odd_offset not in (-1, 1):
        raise ValueError("only odd offsets -1 and +1 are supported")

    initial_carry = CARRY_2 if odd_offset == 1 else CARRY_1
    transitions: dict[tuple[int, int], tuple[int, Word]] = {
        (START, 0): (EVEN_COPY, ()),
        (START, 1): (initial_carry, ()),
        (EVEN_COPY, 0): (EVEN_COPY, (0,)),
        (EVEN_COPY, 1): (EVEN_COPY, (1,)),
        (CARRY_0, 0): (CARRY_0, (0,)),
        (CARRY_0, 1): (CARRY_1, (1,)),
        (CARRY_1, 0): (CARRY_0, (1,)),
        (CARRY_1, 1): (CARRY_2, (0,)),
        (CARRY_2, 0): (CARRY_1, (0,)),
        (CARRY_2, 1): (CARRY_2, (1,)),
    }
    terminal_outputs: dict[int, Word] = {
        EVEN_COPY: (),
        CARRY_0: (),
        CARRY_1: (1,),
        CARRY_2: (0, 1),
    }
    sign = "+" if odd_offset == 1 else "-"
    return SubsequentialTransducer(
        name=f"shortcut_3n{sign}1",
        state_count=5,
        start=START,
        transitions=transitions,
        terminal_outputs=terminal_outputs,
    )


def direct_shortcut(value: int, odd_offset: int = 1) -> int:
    if value <= 0:
        raise ValueError("shortcut map requires a positive integer")
    if odd_offset not in (-1, 1):
        raise ValueError("only odd offsets -1 and +1 are supported")
    if value % 2 == 0:
        return value // 2
    return (3 * value + odd_offset) // 2
