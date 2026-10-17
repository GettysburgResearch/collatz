"""Run the deterministic baseline for experiment X-9101."""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
import sys

from automata import decode_lsd, encode_lsd, shortest_canonical_word, word_text
from search import known_3n_minus_1_cycle, search_guarded_cores, search_labeled_skeletons
from transducer import direct_shortcut, shortcut_transducer
from verify import safety_approximant, verify_candidate


def build_summary(*, exhaustive_states: int, approximation_depth: int) -> dict[str, object]:
    standard = shortcut_transducer(+1)
    control = shortcut_transducer(-1)

    for value in range(1, 100_000):
        encoded = encode_lsd(value)
        observed = decode_lsd(standard.transduce(encoded))
        expected = direct_shortcut(value, +1)
        if observed != expected:
            raise AssertionError((value, observed, expected))

    control_dfa = known_3n_minus_1_cycle()
    control_verification = verify_candidate(control_dfa, control)
    if not control_verification.valid:
        raise AssertionError("the 3n-1 positive control failed")

    approximants: list[dict[str, object]] = []
    for depth in range(approximation_depth + 1):
        dfa = safety_approximant(standard, depth)
        witness = shortest_canonical_word(dfa)
        approximants.append(
            {
                "depth": depth,
                "states": dfa.state_count,
                "shortest_word_lsd": None if witness is None else word_text(witness),
                "shortest_word_value": None if witness is None else decode_lsd(witness),
            }
        )

    small_search = [
        result.to_dict()
        for result in search_labeled_skeletons(
            standard, range(1, exhaustive_states + 1)
        )
    ]
    guarded_search = search_guarded_cores(
        standard, minimum_length=72, core_state_counts=(1, 2)
    )

    return {
        "experiment": "X-9101",
        "classification": "finite exact computation; no counterexample claim",
        "bit_order": "lsd_first",
        "environment": {
            "python": platform.python_version(),
            "platform": platform.platform(),
        },
        "transducer_direct_checks": {
            "map": "shortcut 3n+1",
            "range": "1 <= n < 100000",
            "all_equal": True,
        },
        "positive_control_3n_minus_1": control_verification.to_dict(),
        "safety_approximants": approximants,
        "standard_small_skeleton_search": small_search,
        "standard_guarded_core_search": guarded_search,
        "limitations": [
            "bounded skeleton failures do not imply Collatz convergence",
            "the 72-bit guard is search pruning, not part of candidate soundness",
            "BFS witnesses are shortest by bit length and LSD-lexicographic tie-break, not numeric order",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--exhaustive-states", type=int, default=3)
    parser.add_argument("--approximation-depth", type=int, default=20)
    args = parser.parse_args()
    if not 1 <= args.exhaustive_states <= 4:
        parser.error("--exhaustive-states must be between 1 and 4")
    if not 0 <= args.approximation_depth <= 20:
        parser.error("--approximation-depth must be between 0 and 20")

    summary = build_summary(
        exhaustive_states=args.exhaustive_states,
        approximation_depth=args.approximation_depth,
    )
    canonical = json.dumps(summary, indent=2, sort_keys=True)
    environment_independent = {
        key: value for key, value in summary.items() if key != "environment"
    }
    result_canonical = json.dumps(environment_independent, indent=2, sort_keys=True)
    payload = {
        "sha256_of_environment_bound_summary": hashlib.sha256(
            canonical.encode("utf-8")
        ).hexdigest(),
        "sha256_of_mathematical_results": hashlib.sha256(
            result_canonical.encode("utf-8")
        ).hexdigest(),
        "summary": summary,
    }
    json.dump(payload, sys.stdout, indent=2, sort_keys=True)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
