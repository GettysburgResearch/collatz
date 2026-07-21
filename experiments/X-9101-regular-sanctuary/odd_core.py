"""Odd-core tooling for exact regular-sanctuary experiments.

The primary map in this module is the fully accelerated odd Collatz map

    U(m) = (3*m + 1) / 2**v_2(3*m + 1),

defined for positive odd ``m``.  The same construction supports ``3*m - 1`` as
an explicit positive-control map.  ``odd_core_transducer`` is total on
canonical positive inputs: it first ignores the low zero bits of its input, so
on an arbitrary positive ``n`` it computes ``U(odd_part(n))``.  Its restriction
to odd inputs is therefore exactly ``U``.

Odd-core automata are conjecture generators only.  A proposed odd language
``O`` is lifted by ``lift_odd_dfa_to_shortcut`` to the ordinary LSD-first
language ``0* O``.  The lifted DFA can then be checked by the existing shortcut
transducer and certificate verifier, leaving the final trust boundary
unchanged.
"""

from __future__ import annotations

from typing import Sequence

from automata import DFA, Word
from transducer import SubsequentialTransducer


# The transducer skips input zeros until the first one.  Thereafter its state is
# (carry, emitting), where ``emitting`` records whether the first one in the
# shortcut output has been seen.  Suppressing output before that first one
# removes every factor of two from (3*m + 1)/2.
_SKIP_LOW_INPUT_ZEROS = 0


def _work_state(carry: int, emitting: bool) -> int:
    return 1 + 2 * carry + int(emitting)


def _suppress_low_zeros(emitting: bool, output: Word) -> tuple[bool, Word]:
    kept: list[int] = []
    for bit in output:
        if emitting or bit == 1:
            kept.append(bit)
            emitting = True
    return emitting, tuple(kept)


def odd_part(value: int) -> int:
    """Return the positive odd part of ``value``."""

    if type(value) is not int or value <= 0:
        raise ValueError("odd_part requires a positive integer")
    while value % 2 == 0:
        value //= 2
    return value


def direct_fully_accelerated_odd(value: int, odd_offset: int = 1) -> int:
    """Evaluate fully accelerated ``3*value + odd_offset`` on an odd input."""

    if type(value) is not int or value <= 0 or value % 2 == 0:
        raise ValueError(
            "fully accelerated odd map requires a positive odd integer"
        )
    if odd_offset not in (-1, 1):
        raise ValueError("only odd offsets -1 and +1 are supported")
    result = 3 * value + odd_offset
    while result % 2 == 0:
        result //= 2
    return result


def direct_odd_core_map(value: int, odd_offset: int = 1) -> int:
    """Evaluate the totalized map ``U(odd_part(value))``."""

    return direct_fully_accelerated_odd(odd_part(value), odd_offset)


def odd_core_transducer(odd_offset: int = 1) -> SubsequentialTransducer:
    """Return a seven-state transducer for ``U(odd_part(n))``.

    Bits are consumed and emitted least-significant first.  On the first input
    one, shortcut multiplication starts with carry two for ``3*m + 1`` or carry
    one for ``3*m - 1``.  The raw output is the canonical encoding of the
    corresponding shortcut image of the odd part ``m``.  Dropping its initial
    zero run produces the canonical encoding of the fully accelerated image.

    Although the intended search domain is odd canonical words, totalizing the
    map this way makes it safe to place in the existing finite product-graph
    machinery, which explores every canonical input word.
    """

    if odd_offset not in (-1, 1):
        raise ValueError("only odd offsets -1 and +1 are supported")

    # Raw shortcut carry transitions after the first (oddness) input bit.
    # Each entry is (next carry, one raw output bit).
    carry_transitions: dict[tuple[int, int], tuple[int, Word]] = {
        (0, 0): (0, (0,)),
        (0, 1): (1, (1,)),
        (1, 0): (0, (1,)),
        (1, 1): (2, (0,)),
        (2, 0): (1, (0,)),
        (2, 1): (2, (1,)),
    }
    raw_terminal_outputs: dict[int, Word] = {
        0: (),
        1: (1,),
        2: (0, 1),
    }

    initial_carry = 2 if odd_offset == 1 else 1
    transitions: dict[tuple[int, int], tuple[int, Word]] = {
        (_SKIP_LOW_INPUT_ZEROS, 0): (_SKIP_LOW_INPUT_ZEROS, ()),
        (_SKIP_LOW_INPUT_ZEROS, 1): (
            _work_state(initial_carry, False),
            (),
        ),
    }
    terminal_outputs: dict[int, Word] = {}

    for carry in range(3):
        for emitting in (False, True):
            state = _work_state(carry, emitting)
            for bit in (0, 1):
                next_carry, raw_output = carry_transitions[(carry, bit)]
                next_emitting, output = _suppress_low_zeros(
                    emitting, raw_output
                )
                transitions[(state, bit)] = (
                    _work_state(next_carry, next_emitting),
                    output,
                )

            _, terminal_output = _suppress_low_zeros(
                emitting, raw_terminal_outputs[carry]
            )
            terminal_outputs[state] = terminal_output

    sign = "+" if odd_offset == 1 else "-"
    return SubsequentialTransducer(
        name=f"fully_accelerated_odd_core_3n{sign}1",
        state_count=7,
        start=_SKIP_LOW_INPUT_ZEROS,
        transitions=transitions,
        terminal_outputs=terminal_outputs,
    )


def lift_odd_dfa_to_shortcut(odd_dfa: DFA) -> DFA:
    """Lift an odd-language DFA ``O`` to the ordinary language ``0* O``.

    Under canonical LSD-first semantics, the lifted DFA accepts ``n`` exactly
    when ``odd_dfa`` accepts the canonical encoding of ``odd_part(n)``.  A new
    start state skips all initial zero bits.  The first one, and every later
    bit, is processed by ``odd_dfa`` from its own start state.

    If ``O`` is nonempty, excludes one, and is forward invariant under ``U``,
    this lifted language is a shortcut-map sanctuary.  The returned DFA should
    nevertheless always be passed to the existing standard shortcut verifier;
    this function does not assert those premises itself.
    """

    offset = 1
    skip_state = 0
    transitions: list[tuple[int, int]] = [
        (
            skip_state,
            offset + odd_dfa.step(odd_dfa.start, 1),
        )
    ]
    transitions.extend(
        (
            offset + odd_dfa.step(state, 0),
            offset + odd_dfa.step(state, 1),
        )
        for state in range(odd_dfa.state_count)
    )
    accepting = frozenset(offset + state for state in odd_dfa.accepting)
    return DFA(tuple(transitions), accepting, skip_state).minimized()


def transduce_odd_word(
    word: Sequence[int] | str,
    *,
    odd_offset: int = 1,
) -> Word:
    """Transduce one canonical odd word, rejecting an even-domain mistake."""

    from automata import normalize_word

    bits = normalize_word(word)
    if not bits or bits[0] != 1:
        raise ValueError("fully accelerated odd map requires an odd word")
    return odd_core_transducer(odd_offset).transduce(bits)
