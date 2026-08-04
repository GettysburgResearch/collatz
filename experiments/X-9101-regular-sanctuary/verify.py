"""Exact closure verification and fixed-skeleton synthesis for X-9101."""

from __future__ import annotations

from collections import defaultdict, deque
from dataclasses import dataclass
from typing import Iterable, Sequence

from automata import (
    DFA,
    Word,
    canonical_positive_dfa,
    finite_language_dfa,
    is_canonical_positive,
    normalize_word,
    product_dfa,
    shortest_canonical_word,
    without_finite_words,
)
from transducer import SubsequentialTransducer


def advance_word(dfa: DFA, state: int, word: Sequence[int]) -> int:
    for bit in word:
        state = dfa.step(state, bit)
    return state


def advance_monitor(monitor: int, word: Sequence[int]) -> int:
    # 0 = empty, 1 = nonempty ending 0, 2 = nonempty ending 1.
    for bit in word:
        monitor = 1 if bit == 0 else 2
    return monitor


ProductState = tuple[int, int, int, int, int]


def _reconstruct_word(
    state: ProductState,
    parent: dict[ProductState, tuple[ProductState, int] | None],
) -> Word:
    bits: list[int] = []
    current = state
    while parent[current] is not None:
        previous, bit = parent[current]  # type: ignore[misc]
        bits.append(bit)
        current = previous
    return tuple(reversed(bits))


@dataclass(frozen=True)
class RelationResult:
    edges: frozenset[tuple[int, int]]
    witnesses: dict[tuple[int, int], Word]
    product_states: int


def terminal_relation(
    dfa: DFA,
    transducer: SubsequentialTransducer,
    *,
    with_witnesses: bool = False,
) -> RelationResult:
    """Compute the exact endpoint relation induced by all canonical inputs.

    An edge ``p -> q`` exists exactly when some canonical input word leaves the
    raw DFA in ``p`` while its transducer image leaves the same DFA in ``q``.
    The finite search explores input DFA state, transducer state, output DFA
    state, and canonicality monitors for both streams.
    """

    start: ProductState = (dfa.start, transducer.start, dfa.start, 0, 0)
    queue = deque([start])
    seen = {start}
    parent: dict[ProductState, tuple[ProductState, int] | None] = (
        {start: None} if with_witnesses else {}
    )
    edges: set[tuple[int, int]] = set()
    witnesses: dict[tuple[int, int], Word] = {}

    while queue:
        state = queue.popleft()
        input_state, machine_state, output_state, input_monitor, output_monitor = state

        terminal = transducer.terminal_output(machine_state)
        if input_monitor == 2:
            if terminal is None:
                word = _reconstruct_word(state, parent) if with_witnesses else ()
                raise AssertionError(
                    "transducer has no terminal output on a canonical input: "
                    f"{word!r}"
                )
            final_output_state = advance_word(dfa, output_state, terminal)
            final_output_monitor = advance_monitor(output_monitor, terminal)
            if final_output_monitor != 2:
                word = _reconstruct_word(state, parent) if with_witnesses else ()
                raise AssertionError(
                    "transducer maps a canonical input to a noncanonical output: "
                    f"{word!r}"
                )
            edge = (input_state, final_output_state)
            if edge not in edges:
                edges.add(edge)
                if with_witnesses:
                    witnesses[edge] = _reconstruct_word(state, parent)

        for bit in (0, 1):
            next_machine, emitted = transducer.step(machine_state, bit)
            target: ProductState = (
                dfa.step(input_state, bit),
                next_machine,
                advance_word(dfa, output_state, emitted),
                1 if bit == 0 else 2,
                advance_monitor(output_monitor, emitted),
            )
            if target not in seen:
                seen.add(target)
                if with_witnesses:
                    parent[target] = (state, bit)
                queue.append(target)

    return RelationResult(frozenset(edges), witnesses, len(seen))


def closure_counterexample(
    dfa: DFA, transducer: SubsequentialTransducer
) -> tuple[Word, Word] | None:
    relation = terminal_relation(dfa, transducer, with_witnesses=True)
    violations = [
        edge
        for edge in relation.edges
        if edge[0] in dfa.accepting and edge[1] not in dfa.accepting
    ]
    if violations:
        edge = min(
            violations,
            key=lambda candidate: (
                len(relation.witnesses[candidate]),
                relation.witnesses[candidate],
            ),
        )
        word = relation.witnesses[edge]
        return word, transducer.transduce(word)
    return None


@dataclass(frozen=True)
class VerificationResult:
    valid: bool
    reason: str
    accepted_witness: Word | None
    closure_input: Word | None
    closure_output: Word | None
    relation_edges: int
    product_states: int

    def to_dict(self) -> dict[str, object]:
        def text(word: Word | None) -> str | None:
            return None if word is None else "".join(map(str, word))

        return {
            "valid": self.valid,
            "reason": self.reason,
            "accepted_witness_lsd": text(self.accepted_witness),
            "closure_input_lsd": text(self.closure_input),
            "closure_output_lsd": text(self.closure_output),
            "relation_edges": self.relation_edges,
            "product_states": self.product_states,
        }


def verify_candidate(
    dfa: DFA,
    transducer: SubsequentialTransducer,
    *,
    forbidden_words: Iterable[Sequence[int] | str] = ("1", "01"),
) -> VerificationResult:
    accepted = shortest_canonical_word(dfa)
    if accepted is None:
        return VerificationResult(
            False, "semantic language is empty", None, None, None, 0, 0
        )

    for raw_forbidden in forbidden_words:
        forbidden = normalize_word(raw_forbidden)
        if not is_canonical_positive(forbidden):
            raise ValueError(f"forbidden word is not canonical: {forbidden!r}")
        if dfa.accepts_raw(forbidden):
            return VerificationResult(
                False,
                "semantic language contains a forbidden trivial-cycle word",
                accepted,
                forbidden,
                transducer.transduce(forbidden),
                0,
                0,
            )

    relation = terminal_relation(dfa, transducer, with_witnesses=True)
    violations = [
        edge
        for edge in relation.edges
        if edge[0] in dfa.accepting and edge[1] not in dfa.accepting
    ]
    if violations:
        edge = min(
            violations,
            key=lambda candidate: (
                len(relation.witnesses[candidate]),
                relation.witnesses[candidate],
            ),
        )
        word = relation.witnesses[edge]
        return VerificationResult(
            False,
            "language is not forward invariant",
            accepted,
            word,
            transducer.transduce(word),
            len(relation.edges),
            relation.product_states,
        )

    return VerificationResult(
        True,
        "nonempty, safe, and exactly forward invariant",
        accepted,
        None,
        None,
        len(relation.edges),
        relation.product_states,
    )


@dataclass(frozen=True)
class KernelResult:
    candidate: DFA
    safe_states: frozenset[int]
    rejected_states: frozenset[int]
    witness: Word | None
    relation_edges: int
    product_states: int

    @property
    def nonempty(self) -> bool:
        return self.witness is not None


def maximal_safe_kernel(
    skeleton: DFA,
    transducer: SubsequentialTransducer,
    *,
    extra_forbidden_states: Iterable[int] = (),
    forbidden_words: Iterable[Sequence[int] | str] = ("1", "01"),
) -> KernelResult:
    """Synthesize the unique largest safe accepting set for a skeleton."""

    relation = terminal_relation(skeleton, transducer, with_witnesses=False)
    reverse: dict[int, set[int]] = defaultdict(set)
    for source, target in relation.edges:
        reverse[target].add(source)

    rejected = set(extra_forbidden_states)
    for word in forbidden_words:
        bits = normalize_word(word)
        if not is_canonical_positive(bits):
            raise ValueError(f"forbidden word is not canonical: {bits!r}")
        rejected.add(skeleton.run(bits))
    if any(not 0 <= state < skeleton.state_count for state in rejected):
        raise ValueError("extra forbidden state is outside the skeleton")

    queue = deque(rejected)
    while queue:
        target = queue.popleft()
        for predecessor in reverse.get(target, ()):
            if predecessor not in rejected:
                rejected.add(predecessor)
                queue.append(predecessor)

    safe = frozenset(set(range(skeleton.state_count)) - rejected)
    candidate = skeleton.with_accepting(safe)
    witness = shortest_canonical_word(candidate)
    return KernelResult(
        candidate=candidate,
        safe_states=safe,
        rejected_states=frozenset(rejected),
        witness=witness,
        relation_edges=len(relation.edges),
        product_states=relation.product_states,
    )


def preimage_dfa(transducer: SubsequentialTransducer, target: DFA) -> DFA:
    """DFA for words whose transducer output belongs to ``target``.

    Canonical input restrictions are intentionally not built in here.  Callers
    intersect with ``canonical_positive_dfa`` (or a stricter semantic domain).
    """

    target_count = target.state_count

    def index(machine_state: int, output_state: int) -> int:
        return machine_state * target_count + output_state

    transitions: list[tuple[int, int]] = []
    accepting: set[int] = set()
    for machine_state in range(transducer.state_count):
        for output_state in range(target_count):
            row: list[int] = []
            for bit in (0, 1):
                next_machine, emitted = transducer.step(machine_state, bit)
                next_output = advance_word(target, output_state, emitted)
                row.append(index(next_machine, next_output))
            transitions.append(tuple(row))

            terminal = transducer.terminal_output(machine_state)
            if terminal is not None:
                final_output = advance_word(target, output_state, terminal)
                if final_output in target.accepting:
                    accepting.add(index(machine_state, output_state))

    return DFA(
        tuple(transitions),
        frozenset(accepting),
        index(transducer.start, target.start),
    ).minimized()


def safety_base_dfa() -> DFA:
    """All canonical positives except the shortcut cycle words 1 and 01."""

    return product_dfa(
        canonical_positive_dfa(), without_finite_words(("1", "01"))
    ).minimized()


def safety_approximant(
    transducer: SubsequentialTransducer, depth: int
) -> DFA:
    """Return numbers avoiding {1,2} for the first ``depth + 1`` states."""

    if depth < 0:
        raise ValueError("depth must be nonnegative")
    base = safety_base_dfa()
    current = base
    for _ in range(depth):
        current = product_dfa(base, preimage_dfa(transducer, current)).minimized()
    return current


def direct_avoids(
    value: int,
    depth: int,
    direct_map,
) -> bool:
    for _ in range(depth + 1):
        if value in (1, 2):
            return False
        value = direct_map(value)
    return True
