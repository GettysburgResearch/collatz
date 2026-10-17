"""Second exact candidate check via regular preimage and DFA inclusion.

The primary verifier computes an endpoint relation in one product graph.  This
module takes the logically equivalent but algorithmically separate route

    L(D) subset T^{-1}(L(D)).

It constructs the complete regular preimage under the subsequential
transducer, complements it, and checks emptiness of the resulting DFA
intersection.  It intentionally reuses the frozen automata/transducer data
types, but it does not call ``terminal_relation`` or ``verify_candidate``.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Iterable, Sequence

from automata import (
    DFA,
    Word,
    canonical_positive_dfa,
    is_canonical_positive,
    normalize_word,
    product_dfa,
    shortest_canonical_word,
)
from transducer import SubsequentialTransducer
from verify import preimage_dfa


@dataclass(frozen=True)
class PreimageVerificationResult:
    valid: bool
    reason: str
    accepted_witness: Word | None
    closure_input: Word | None
    closure_output: Word | None
    candidate_states: int
    preimage_states: int
    violation_states: int


def _validate_canonical_transducer_contract(
    transducer: SubsequentialTransducer,
) -> None:
    """Check total canonical-to-canonical behavior without a candidate DFA.

    ``preimage_dfa`` quite properly treats an undefined terminal output as a
    rejecting path.  A Collatz certificate checker needs the stronger global
    contract that *every* canonical positive input has a terminal output and
    produces a canonical positive output.  Validate that contract in the
    small graph consisting only of transducer state and endpoint monitors.
    """

    # Monitor values: 0 = empty, 1 = nonempty ending zero, 2 = ending one.
    start = (transducer.start, 0, 0)
    queue = deque([start])
    parent: dict[
        tuple[int, int, int],
        tuple[tuple[int, int, int], int] | None,
    ] = {start: None}

    def witness(state: tuple[int, int, int]) -> Word:
        bits: list[int] = []
        current = state
        while parent[current] is not None:
            previous, bit = parent[current]  # type: ignore[misc]
            bits.append(bit)
            current = previous
        return tuple(reversed(bits))

    def advance(monitor: int, output: Sequence[int]) -> int:
        for bit in output:
            monitor = 1 if bit == 0 else 2
        return monitor

    while queue:
        state = queue.popleft()
        machine_state, input_monitor, output_monitor = state
        if input_monitor == 2:
            terminal = transducer.terminal_output(machine_state)
            if terminal is None:
                raise AssertionError(
                    "transducer has no terminal output on a canonical input: "
                    f"{witness(state)!r}"
                )
            if advance(output_monitor, terminal) != 2:
                raise AssertionError(
                    "transducer maps a canonical input to a noncanonical output: "
                    f"{witness(state)!r}"
                )

        for bit in (0, 1):
            next_machine, emitted = transducer.step(machine_state, bit)
            target = (
                next_machine,
                1 if bit == 0 else 2,
                advance(output_monitor, emitted),
            )
            if target not in parent:
                parent[target] = (state, bit)
                queue.append(target)


def verify_candidate_via_preimage(
    dfa: DFA,
    transducer: SubsequentialTransducer,
    *,
    forbidden_words: Iterable[Sequence[int] | str] = ("1", "01"),
) -> PreimageVerificationResult:
    """Verify nonemptiness, safety, and closure without endpoint relations."""

    semantic_candidate = product_dfa(dfa, canonical_positive_dfa()).minimized()
    accepted = shortest_canonical_word(semantic_candidate)
    if accepted is None:
        return PreimageVerificationResult(
            False,
            "semantic language is empty",
            None,
            None,
            None,
            semantic_candidate.state_count,
            0,
            0,
        )

    for raw_forbidden in forbidden_words:
        forbidden = normalize_word(raw_forbidden)
        if not is_canonical_positive(forbidden):
            raise ValueError(f"forbidden word is not canonical: {forbidden!r}")
        if semantic_candidate.accepts_raw(forbidden):
            return PreimageVerificationResult(
                False,
                "semantic language contains a forbidden trivial-cycle word",
                accepted,
                forbidden,
                transducer.transduce(forbidden),
                semantic_candidate.state_count,
                0,
                0,
            )

    _validate_canonical_transducer_contract(transducer)
    preimage = preimage_dfa(transducer, semantic_candidate)
    violation_language = product_dfa(
        semantic_candidate, preimage.complement()
    ).minimized()
    closure_input = shortest_canonical_word(violation_language)
    if closure_input is not None:
        closure_output = transducer.transduce(closure_input)
        if not semantic_candidate.accepts_raw(closure_input):
            raise AssertionError("preimage witness is not in the candidate language")
        if semantic_candidate.accepts_raw(closure_output):
            raise AssertionError("preimage witness output remains in the candidate")
        return PreimageVerificationResult(
            False,
            "language is not forward invariant",
            accepted,
            closure_input,
            closure_output,
            semantic_candidate.state_count,
            preimage.state_count,
            violation_language.state_count,
        )

    return PreimageVerificationResult(
        True,
        "nonempty, safe, and exactly forward invariant",
        accepted,
        None,
        None,
        semantic_candidate.state_count,
        preimage.state_count,
        violation_language.state_count,
    )
