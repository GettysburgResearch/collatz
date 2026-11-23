#!/usr/bin/env python3
"""Exact controls for complete-witness transport, not target convergence tests."""

from __future__ import annotations

import json


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def shortcut(n: int) -> int:
    require(n > 0, "ordinary state must be positive")
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def correction(word: list[int]) -> int:
    result = 0
    total = 0
    for j, a in enumerate(word):
        require(a > 0, "nonpositive gap")
        result += 3 ** (len(word) - 1 - j) * (1 << total)
        total += a
    return result


def replay_odd(n: int, word: list[int], require_large: bool = False) -> int:
    require(n > 0 and n % 2 == 1, "odd source required")
    for a in word:
        if require_large:
            require(n > 1, "forced prefix reached one prematurely")
        q, remainder = divmod(3 * n + 1, 1 << a)
        require(a > 0 and remainder == 0 and q > 0 and q % 2 == 1,
                "gap is not the actual odd valuation")
        n = q
    return n


def check_certificate(n: int, word: list[int]) -> None:
    require(3 ** len(word) * n + correction(word) == 1 << sum(word),
            "complete certificate identity failed")
    require(replay_odd(n, word) == 1, "complete certificate did not reach one")


def normalize(r: int, z: int) -> tuple[int, int, list[dict[str, int]]]:
    require(r > 0 and z % 3 != 0, "normalizer requires a reduced ternary denominator")
    trace: list[dict[str, int]] = []
    odd_steps = 0
    j = r
    while j > 0:
        require(z != 0 and z % 3 != 0, "lost reduced denominator")
        trace.append({"denominator_exponent": j, "numerator": z})
        old_rank = (j, abs(z))
        if z % 2 == 0:
            z //= 2
        else:
            z = (z + 3 ** (j - 1)) // 2
            j -= 1
            odd_steps += 1
        require((j, abs(z)) < old_rank, "normalizer rank did not decrease")
    require(odd_steps == r, "normalizer did not clear exactly r odd factors")
    return len(trace), z, trace


def four_step_family(h: int) -> dict:
    require(h >= 1, "family starts at h=1")
    m = 27 * h
    K, rem = divmod(4 ** m - 1, 81)
    require(rem == 0 and K > 0 and K % 2 == 1, "family parameter failed")
    x, y = 256 * K + 1, 128 * K + 1
    word = [2, 2, 2, 2 * m + 2]
    require(x % 512 == 257 and (x + 1) // 2 == y, "wrong original residue or half")
    check_certificate(x, word)
    require(correction(word) == 175, "wrong input correction")
    front = [2, 2, 2, 1] + [2] * (m - 1)
    endpoint = replay_odd(y, front, require_large=True)
    require(endpoint == 4 * 3 ** (m - 1) + 1 and endpoint > 1,
            "wrong forced endpoint")
    returned = shortcut(shortcut(endpoint))
    require(returned == 3 ** m + 1 and returned < y, "target clock or descent failed")
    require(sum(front) + 2 == 2 * m + 7 and sum(word) == 2 * m + 8,
            "ordinary clock mismatch")
    return {"h": h, "m": m, "input_odd_length": 4,
            "input_bit_length": x.bit_length(), "input_residue": x % 512,
            "forced_output_prefix_odd_length": len(front),
            "every_possible_output_length_at_least": m + 4,
            "source_hitting_clock": 2 * m + 8, "target_return_clock": 2 * m + 7,
            "strict_original_output_descent": True,
            "output_certificate_existence_asserted": False}


def normalizer_control(prefix: list[int], final_gap: int) -> dict:
    word = prefix + [final_gap]
    r, A, C = len(word), sum(word), correction(word)
    x, rem = divmod((1 << A) - C, 3 ** r)
    require(rem == 0 and x > 0 and x % 512 in (129, 257, 385),
            "normalizer control is not an original-domain complete source")
    check_certificate(x, word)
    y = (x + 1) // 2
    z0, rem = divmod(3 ** r - C, 2)
    require(rem == 0, "nonintegral signed numerator")
    k, K, trace = normalize(r, z0)
    require(k <= A - 1, "control lacks the stated precision")
    n = y
    for i, state in enumerate(trace):
        j, z = state["denominator_exponent"], state["numerator"]
        require(3 ** j * n == (1 << (A - 1 - i)) + z,
                "compiled invariant failed")
        require(n % 2 == z % 2, "compiled parity mismatch")
        n = shortcut(n)
    require(n == (1 << (A - 1 - k)) + K, "normalizer endpoint is not physical")
    return {"source_prefix": prefix, "final_gap": final_gap, "r": r,
            "A": A, "C": C, "input_residue": x % 512,
            "normalizer_clock": k, "signed_K": K,
            "remaining_binary_exponent": A - 1 - k, "trace": trace}


def mersenne_family(h: int) -> dict:
    require(pow(2, 352, 729) == 7207 % 729 and pow(2, 486, 729) == 1,
            "all-parameter source congruence failed")
    a = 340 + 486 * h
    b = a + 1
    word = [2, 2, 2, 3, 3, a]
    x, rem = divmod((1 << (a + 12)) - 7207, 729)
    require(rem == 0 and x % 512 == 257, "Mersenne-family source failed")
    check_certificate(x, word)
    y = (x + 1) // 2
    front = [2, 2, 2, 1, 1, 2]
    n = replay_odd(y, front, require_large=True)
    require(correction(front) == 2215 and n == (1 << b) - 1,
            "wrong Mersenne prefix")
    for i in range(b):
        require(n == 3 ** i * (1 << (b - i)) - 1 and n > 1 and n % 2 == 1,
                "forced all-odd ascent failed")
        n = shortcut(n)
    require(n == 3 ** b - 1, "wrong forced high endpoint")
    return {"h": h, "a": a, "b": b, "input_odd_length": 6,
            "input_bit_length": x.bit_length(), "input_residue": x % 512,
            "source_hitting_clock": a + 12,
            "mersenne_entry_clock": 10, "forced_high_clock": 10 + b,
            "forced_high_bit_length": n.bit_length(),
            "every_possible_output_length_at_least": b + 6,
            "output_certificate_existence_asserted": False}


def precision_exhaustion() -> dict:
    x = 129
    n = x
    word: list[int] = []
    while n != 1:
        numerator = 3 * n + 1
        a = (numerator & -numerator).bit_length() - 1
        n = numerator >> a
        word.append(a)
    check_certificate(x, word)
    r, A, C = len(word), sum(word), correction(word)
    k, K, trace = normalize(r, (3 ** r - C) // 2)
    require((r, A, k, K) == (44, 77, 86, 7), "precision control changed")
    n = (x + 1) // 2
    first_hit = None
    first_mismatch = None
    for i, state in enumerate(trace):
        if n == 1 and first_hit is None:
            first_hit = i
        if n % 2 != state["numerator"] % 2 and first_mismatch is None:
            first_mismatch = i
        if i < A - 1:
            require(n % 2 == state["numerator"] % 2, "premature precision failure")
        n = shortcut(n)
    require(first_hit is not None and first_mismatch == A - 1,
            "precision boundary was not realized")
    return {"input": x, "output": 65, "input_odd_length": r,
            "input_complete_clock": A, "normalizer_clock": k, "signed_K": K,
            "available_binary_precision": A - 1,
            "first_actual_formal_parity_disagreement": first_mismatch,
            "actual_output_first_hitting_clock": first_hit,
            "scope": "first-hit source certificate; output converges; not a bad query"}


def main() -> None:
    results = {"schema": "collatz-target-entry-controls/v1",
               "normalization": "ordinary shortcut T; exact positive odd gaps",
               "scope": "finite forced prefixes and algebra; no universal output convergence claim",
               "four_step_family": [four_step_family(h) for h in (1, 2, 4, 16, 64)],
               "normalizer": [normalizer_control(p, a) for p, a in
                   [([2, 2, 2], 56), ([2, 2, 2, 1], 70),
                    ([2, 2, 2, 4], 68), ([2, 2, 2, 3, 3], 340),
                    ([2, 2, 2, 1, 1, 3], 1024)]],
               "mersenne_family": [mersenne_family(h) for h in (0, 1, 3, 7)],
               "precision_exhaustion": precision_exhaustion()}
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
