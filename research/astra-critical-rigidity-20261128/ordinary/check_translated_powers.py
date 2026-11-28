"""Complete finite signed certificates and bounded ordinary translated-power controls."""

import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def step(x, den=1):
    return (3 * x + den) // 2 if x % 2 else x // 2


def center(c):
    return -6 if c == -1 else (-15, -4, -3, -2, -1, -2, -1, -8)[c % 8]


def even_budget(v):
    n, e = v, 0
    for _ in range(9):
        if n == -1:
            return e
        e += 1 - n % 2
        n = step(n)
    raise ValueError("representative failed to reach -1")


def signed_certificates():
    records = []
    for c in range(-24, 25):
        x0 = center(c)
        require((x0 - c) % 8 in (1, 3), "center outside the power subgroup")
        e = even_budget(x0)
        require(e <= 5, "more than five even steps")
        for d in range(1, e + 1):
            den = 3**d
            if (den - 1) * abs(c) >= den * 2**(e - d):
                continue
            x, y, delta = x0, c * (den - 1) + x0, 0
            for t in range(16):
                if x * den == y:
                    require(delta != d, "a meeting has the prohibited grade difference")
                    stop = "equal"
                    break
                if x == -1 and delta < d:
                    stop = "minus_one"
                    break
                delta += y % 2 - x % 2
                x, y = step(x), step(y, den)
            else:
                raise ValueError("no terminating certificate within 15 steps")
            records.append([c, d, t, delta, stop])
    require(len(records) == 17, "the exact 17-case partition changed")
    return records


def physical_controls():
    h, modulus = 8, 2**8
    shifts = (-1000, -24, -16, -8, -1, 0, 1, 2, 4, 7, 8, 16, 24, 1000)
    pairs, checked = 0, 0
    for c in shifts:
        period = modulus // 4
        residues = [n for n in range(period) if pow(3, n, modulus) == (center(c) - c) % modulus]
        require(len(residues) == 1, "power congruence did not select one class")
        n = residues[0] + period
        upper = 3**n + c
        require(upper > 0 and n > 3*h + 20, "inadmissible positive control")
        upper_states = set()
        for _ in range(h + 1):
            upper_states.add(upper)
            upper = step(upper)
        for m in range(n):
            lower = 3**m + c
            if lower <= 0:
                continue
            pairs += 1
            odds = 0
            while odds <= h:
                require(lower not in upper_states, "positive bounded-grade earlier-exponent meeting")
                checked += 1
                odds += lower % 2
                lower = step(lower)
    return {"height_H": h, "shifts": list(shifts), "earlier_positive_pairs": pairs,
            "physical_lower_dates_through_odd_budget": checked}


def offset_controls():
    count = 0
    for length in range(13):
        maxima = {}
        for tape in range(1 << length):
            c, p = 0, 0
            for t in range(length):
                if (tape >> t) & 1:
                    c = 3 * c + 2**t
                    p += 1
            # Sharp upper bound in integer form.
            require(c <= 2**(length-p) * (3**p - 2**p), "sharp offset bound failed")
            require(c < 3**p * 2**(length-p), "normalized offset bound failed")
            maxima[p] = max(c, maxima.get(p, 0))
            count += 1
        for p, peak in maxima.items():
            require(peak == 2**(length-p) * (3**p - 2**p), "offset optimum missed")
    return count


if __name__ == "__main__":
    print(json.dumps({"signed_cases": signed_certificates(), "offset_tapes": offset_controls(),
                      "physical": physical_controls()}, indent=2))
