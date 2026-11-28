"""Replay the signed integer recurrence and each strict chronological cut."""

import json
from math import gcd


def require(condition, message):
    if not condition:
        raise ValueError(message)


def step(x):
    return (3 * x + 1) // 2 if x % 2 else x // 2


def trail(s, r, limit):
    a, b = s, 3**r * s
    g = h = 0
    rows = []
    for t in range(limit + 1):
        d = 3**g * b - 3**(h + r) * a
        rows.append((a, b, g, h, d))
        require(abs(d) <= 3**(g + h + r), "determinant exceeds envelope")
        if t and a != b:
            require(d != 0 and gcd(a * b, 3) == 1, "broken post-odd rigidity")
        if t == limit:
            break
        aa, bb = a % 2, b % 2
        a, b, g, h = step(a), step(b), g + aa, h + bb
        next_d = 3**g * b - 3**(h + r) * a
        rhs = 3**(aa + bb) * d + 3**g * bb - 3**(h + r) * aa
        require(2 * next_d == rhs, "signed one-step recurrence failed")
    return rows


def audit_block(rows, r, start, length):
    qa = rows[start][2] + rows[start][3]
    qb = rows[start + length][2] + rows[start + length][3]
    terms = [(0, 3**(qb - qa) * rows[start][4])]
    tied_dates = 0
    for j in range(length):
        a, b, g, h, _ = rows[start + j]
        aa, bb = a % 2, b % 2
        tail = 3**(qb - (g + h + aa + bb))
        if bb:
            terms.append((j, 2**j * tail * 3**(g + aa)))
        if aa:
            terms.append((j, -2**j * tail * 3**(h + r + bb)))
        tied_dates += aa * bb
    terms.append((length, -(2**length) * rows[start + length][4]))
    require(len(terms) == qb - qa + 2, "lost a tied-exponent pure term")
    require(sum(value for _, value in terms) == 0, "expanded block is not zero")
    zero_cuts = 0
    for t in range(1, length + 1):
        _, _, g, h, det = rows[start + t]
        expected = (2**t) * 3**(qb - g - h) * det
        actual = sum(value for exponent, value in terms if exponent < t)
        require(actual == expected, "chronological cut ledger failed")
        zero_cuts += (actual == 0)
    return length, tied_dates, zero_cuts


def main():
    horizon = 40
    pairs = recurrence_steps = blocks = strict_cuts = tied = 0
    for s in range(1, 514, 2):
        for r in (1, 2, 3, 5, 8):
            rows = trail(s, r, horizon)
            pairs += 1
            recurrence_steps += horizon
            first_equal = next((t for t, row in enumerate(rows) if row[0] == row[1]),
                               horizon + 1)
            for start in (1, 4, 11):
                for length in (1, 3, 7, 13):
                    if start + length >= first_equal:
                        continue
                    qty, tied_here, zeros = audit_block(rows, r, start, length)
                    require(zeros == 0, "nonzero hypothesis failed before the first meeting")
                    blocks += 1
                    strict_cuts += qty
                    tied += tied_here

    # The same identity admits zero cuts after a true physical merger.
    # Choose a grade-five cylinder whose new common tail is a power of two.
    exponent = next(e for e in range(60, 90) if pow(2, e, 27) == 20)
    t = (2**exponent - 20) // 27
    s = 23 + 32 * t
    rows = trail(s, 1, 5 + exponent)
    require(rows[5][:2] == (2**exponent, 2**exponent), "wrong merged control")
    _, _, zero_cuts = audit_block(rows, 1, 5, exponent)
    require(zero_cuts == exponent and sum(rows[-1][2:4]) == 5,
            "merger did not supply the zero-cut control")
    result = {"odd_source_range": [1, 513], "three_power_exponents": [1, 2, 3, 5, 8],
              "pairs": pairs, "native_horizon": horizon, "signed_recurrence_steps": recurrence_steps,
              "unmatched_blocks": blocks, "strict_nonzero_cuts": strict_cuts,
              "two_odd_dates_over_tested_blocks": tied,
              "merged_control": {"odd_source": s, "first_common_clock": 5,
                                 "fixed_total_grade": 5, "zero_cuts_after_first_merge": zero_cuts}}
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
