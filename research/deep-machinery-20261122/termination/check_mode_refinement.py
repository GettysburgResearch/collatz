#!/usr/bin/env python3
"""Exact fixture for MODE_REFINEMENT_ATTEMPT.md; no conjectural orbit oracle."""

import json
from pathlib import Path


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def valuation(value, prime):
    value = abs(value)
    require(value != 0, "valuation called at zero")
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def shortcut(n):
    return (3 * n + 1) // 2 if n % 2 else n // 2


def active_mode(n):
    return valuation(n + 1, 2) if n % 2 else 0


def z(a, n):
    return (3**a - 2 ** (a + 1)) * n + 3**a - 2**a


def existing_rank(n):
    """Uses the cited parent finite-envelope formula as a dependency."""
    h = valuation(2 * n + 1, 3)
    indices = sorted({0, 1, 2} | ({h} if h >= 3 else set()))
    candidates = {}
    for a in indices:
        numerator = z(a, n)
        candidates[a] = (
            0 if numerator == 0 else numerator**2 // 3 ** valuation(numerator, 3)
        )
    least = min(candidates.values())
    winners = [a for a, value in candidates.items() if value == least]
    return least, winners


def literal_one_copy(n, expected_mode, expected_next_mode):
    require(active_mode(n) == expected_mode, "wrong initial physical mode")
    states = [n]
    current = n
    for _ in range(expected_mode):
        require(current % 2 == 1, "physical odd branch mismatch")
        current = shortcut(current)
        states.append(current)
    require(current % 2 == 0, "physical even branch mismatch")
    current = shortcut(current)
    states.append(current)
    require(active_mode(current) == expected_next_mode, "wrong next physical mode")
    require(expected_next_mode != expected_mode, "one-copy maximality not established")
    require(all(value > n for value in states[1:]), "unexpected ordinary descent")
    # A different next active mode proves that the one repeated block is maximal.
    require(
        valuation(z(expected_mode, n), 2) // (expected_mode + 1) == 1,
        "independent arithmetic maximal count differs from physical count",
    )
    return current, states


def fixture(b, pairs):
    X, Y = 3**b, 2**b
    D, B = 9 * X - 16 * Y, 13 * X - 8 * Y
    modulus = 2 ** ((b + 4) * pairs + 4) * 3 ** (b + 3)
    n = (-B * pow(D, -1, modulus)) % modulus
    if n < 10:
        n += modulus
    require((D * n + B) % modulus == 0, "CRT congruence failed")
    original = n
    pair_rows = []
    module_values = [n]
    module_ranks = [existing_rank(n)[0]]
    clock_count = 0
    for j in range(pairs):
        rank_n, winners_n = existing_rank(n)
        require(winners_n == [2], "wrong boundary envelope minimizer")
        require(rank_n * 9 == (n + 5) ** 2, "wrong boundary envelope value")
        old_v2 = valuation(D * n + B, 2)
        old_v3 = valuation(D * n + B, 3)
        y, first_word = literal_one_copy(n, 2, b)
        require(8 * y == 9 * n + 5, "first affine formula mismatch")
        rank_y, winners_y = existing_rank(y)
        require(winners_y == [2], "wrong intermediate envelope minimizer")
        require(rank_y * 81 == (y + 5) ** 2, "wrong intermediate envelope value")
        require(rank_y * 64 == rank_n * 9, "first-module rank factor mismatch")
        m, second_word = literal_one_copy(y, b, 2)
        require(16 * Y * m == 9 * X * n + B, "pair affine formula mismatch")
        rank_m, winners_m = existing_rank(m)
        require(winners_m == [2], "wrong return envelope minimizer")
        require(rank_m * 9 == (m + 5) ** 2, "wrong return envelope value")
        require(m > n and rank_m > rank_n, "pair did not increase ordinary value and rank")
        require(valuation(D * m + B, 2) == old_v2 - b - 4, "pair counter decrement mismatch")
        require(valuation(D * m + B, 3) == old_v3 + b + 2, "pair ternary increment mismatch")
        old_pair_rank = (D * n + B) ** 2 // 3**old_v3
        new_pair_rank = (D * m + B) ** 2 // 3 ** (old_v3 + b + 2)
        require(
            new_pair_rank * 2 ** (2 * b + 8) == old_pair_rank * 3 ** (b + 2),
            "repaired pair-rank transport mismatch",
        )
        require(new_pair_rank < old_pair_rank, "repaired pair rank did not contract")
        pair_rows.append({
            "pair_index": j,
            "source": str(n),
            "intermediate": str(y),
            "target": str(m),
            "ranks": [str(rank_n), str(rank_y), str(rank_m)],
            "literal_words": ["110", "1" * b + "0"],
            "literal_states": [[str(v) for v in first_word], [str(v) for v in second_word]],
            "maximal_counts": [1, 1],
            "pair_counter_before_after": [old_v2, old_v2 - b - 4],
        })
        module_values.extend((y, m))
        module_ranks.extend((rank_y, rank_m))
        clock_count += b + 4
        n = m
    unsafe_rank = module_ranks[1]
    unsafe_future = module_ranks[2:]
    require(len(unsafe_future) == 2 * pairs - 1, "wrong unsafe module count")
    require(all(value > unsafe_rank for value in unsafe_future), "unexpected unsafe repayment")
    return {
        "b": b,
        "pairs": pairs,
        "crt_modulus": str(modulus),
        "source": str(original),
        "target": str(n),
        "literal_shortcut_clocks": clock_count,
        "unsafe_start": str(module_values[1]),
        "unsafe_start_rank": str(unsafe_rank),
        "successive_modules_without_repayment": len(unsafe_future),
        "pair_rows": pair_rows,
    }


def main():
    cases = [fixture(b, pairs) for b in (3, 4, 7, 12) for pairs in (1, 2, 4, 8)]
    require(cases[0]["source"] == "662107", "frozen first fixture changed")
    require(cases[1]["source"] == "94720603", "frozen second fixture changed")
    require(cases[1]["target"] == "341379211", "frozen second endpoint changed")
    result = {
        "status": "all explicit checks passed; not a global Collatz proof",
        "parent_dependency": "pass4/MOVING_GHOST_RANK.md finite-envelope formula",
        "cases": cases,
        "case_count": len(cases),
        "pair_count": sum(case["pairs"] for case in cases),
        "shortcut_clocks": sum(case["literal_shortcut_clocks"] for case in cases),
        "checks": [
            "CRT realization in ordinary positive integers",
            "every literal parity branch independently replayed",
            "exact active-mode changes and maximal counts one",
            "existing envelope has unique index two and stated exact value",
            "rank grows at every pair return",
            "unsafe start has no repayment over the stated module window",
            "fresh pair counter and pair rank satisfy exact transport",
        ],
    }
    target = Path(__file__).with_name("mode-refinement-fixture.json")
    target.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({key: result[key] for key in ("status", "case_count", "pair_count", "shortcut_clocks")}))


if __name__ == "__main__":
    main()
