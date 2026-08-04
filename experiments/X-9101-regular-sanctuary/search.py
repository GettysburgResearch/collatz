"""Bounded, proof-checked search routines for experiment X-9101."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from automata import (
    DFA,
    decode_lsd,
    finite_language_dfa,
    threshold_core_dfa,
    transition_skeletons,
    word_text,
)
from transducer import SubsequentialTransducer
from verify import maximal_safe_kernel, verify_candidate


@dataclass(frozen=True)
class SkeletonSearchResult:
    state_count: int
    skeletons_checked: int
    nonempty_kernels: int
    first_candidate: DFA | None
    first_witness_lsd: str | None
    first_witness_value: int | None

    def to_dict(self) -> dict[str, object]:
        return {
            "state_count": self.state_count,
            "skeletons_checked": self.skeletons_checked,
            "nonempty_kernels": self.nonempty_kernels,
            "first_candidate": (
                None if self.first_candidate is None else self.first_candidate.to_dict()
            ),
            "first_witness_lsd": self.first_witness_lsd,
            "first_witness_value": self.first_witness_value,
        }


def search_labeled_skeletons(
    transducer: SubsequentialTransducer,
    state_counts: Iterable[int],
) -> list[SkeletonSearchResult]:
    results: list[SkeletonSearchResult] = []
    for state_count in state_counts:
        checked = 0
        found = 0
        first_candidate: DFA | None = None
        first_witness = None
        for skeleton in transition_skeletons(state_count):
            checked += 1
            kernel = maximal_safe_kernel(skeleton, transducer)
            if not kernel.nonempty:
                continue
            found += 1
            verification = verify_candidate(kernel.candidate, transducer)
            if not verification.valid:
                raise AssertionError(
                    "maximal-safe kernel failed independent candidate verification"
                )
            if first_candidate is None:
                first_candidate = kernel.candidate
                first_witness = kernel.witness
        results.append(
            SkeletonSearchResult(
                state_count=state_count,
                skeletons_checked=checked,
                nonempty_kernels=found,
                first_candidate=first_candidate,
                first_witness_lsd=(
                    None if first_witness is None else word_text(first_witness)
                ),
                first_witness_value=(
                    None if first_witness is None else decode_lsd(first_witness)
                ),
            )
        )
    return results


def search_guarded_cores(
    transducer: SubsequentialTransducer,
    *,
    minimum_length: int,
    core_state_counts: Iterable[int],
) -> list[dict[str, object]]:
    """Exhaust small transition cores behind an explicit length threshold."""

    results: list[dict[str, object]] = []
    for core_states in core_state_counts:
        checked = 0
        found = 0
        first_witness = None
        first_candidate = None
        expanded_states = (minimum_length + 1) * core_states
        for core in transition_skeletons(core_states):
            checked += 1
            expanded, early_states = threshold_core_dfa(core, minimum_length)
            kernel = maximal_safe_kernel(
                expanded,
                transducer,
                extra_forbidden_states=early_states,
            )
            if kernel.nonempty:
                found += 1
                verification = verify_candidate(kernel.candidate, transducer)
                if not verification.valid:
                    raise AssertionError("guarded kernel failed exact verification")
                if first_witness is None:
                    first_witness = kernel.witness
                    first_candidate = kernel.candidate.to_dict()
        results.append(
            {
                "core_states": core_states,
                "expanded_states": expanded_states,
                "minimum_length": minimum_length,
                "skeletons_checked": checked,
                "nonempty_kernels": found,
                "first_candidate": first_candidate,
                "first_witness_lsd": (
                    None if first_witness is None else word_text(first_witness)
                ),
                "first_witness_value": (
                    None if first_witness is None else decode_lsd(first_witness)
                ),
            }
        )
    return results


def known_3n_minus_1_cycle() -> DFA:
    return finite_language_dfa(("101", "111", "0101"))
