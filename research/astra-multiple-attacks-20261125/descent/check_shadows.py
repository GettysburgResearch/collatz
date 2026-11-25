"""Exact finite seed check for the endpoint-uniform D=8 refinement."""
import json


def step(n):
    return (3 * n + 1) // 2 if n % 2 else n // 2


def orbit(start, length):
    state, grade = start, 0
    for _ in range(length):
        grade += state % 2
        state = step(state)
    return state, grade


def finite_seeds(extra):
    bound = 3**extra
    ceiling = 2 * bound
    maximum, witness, checked = 0, None, 0
    # Seed zero has grade zero at all clocks.
    for seed in range(1, bound):
        state, odd, clock, binary, ternary = seed, 0, 0, 1, 1
        while True:
            checked += 1
            if binary <= ceiling * ternary and odd > maximum:
                maximum, witness = odd, (seed, clock, state)
            # The two-clock cycle at one multiplies the ratio by 4/3.
            # Its intervening odd departure multiplies it by 2/3.
            if state == 1 and 2 * binary > 3 * ceiling * ternary:
                break
            if clock >= 10000:
                raise RuntimeError(f"uncertified seed {seed}")
            if state % 2:
                odd += 1
                ternary *= 3
            state = step(state)
            binary *= 2
            clock += 1
    return {"D": extra, "seed_count_including_zero": bound,
            "ratio_ceiling": ceiling, "maximum_odd_grade": maximum,
            "maximizing_seed_clock_endpoint": witness,
            "positive_seed_clock_pairs_checked": checked}


def family(h):
    m = 2 * 3 ** (h - 1)
    x = 2**m - 1
    a, remainder = divmod(x, 3**h)
    w = 2**h * a - 1
    if remainder or a % 3 != 1 or w % 3 or not 0 < w < x:
        raise RuntimeError("ternary source test failed")
    if orbit(x // 3, m) != (1, 1):
        raise RuntimeError("one-odd lower certificate failed")
    right, upper_grade = orbit(x, m + 2)
    left, smaller_grade = orbit(w, h + m + 2)
    if (left, upper_grade, smaller_grade) != (right, m, m + h):
        raise RuntimeError("later exact certificate failed")
    short = None
    if x % 243 == 0:
        partner = 192 * (x // 243) - 3
        if not (0 < partner < x and partner % 3 == 0):
            raise RuntimeError("bounded-work source failed")
        if orbit(partner, 7) != ((x - 1) // 2, 4):
            raise RuntimeError("seven-step partner failed")
        if orbit(partner, m + 8) != (right, m + 4):
            raise RuntimeError("fixed-work exit failed")
        short = m + 4
    return {"h": h, "m": m, "upper_source_bits": x.bit_length(),
            "four_odd_partner_grade_when_applicable": short,
            "smaller_triple_bits": w.bit_length(), "upper_grade": upper_grade,
            "smaller_grade": smaller_grade}


if __name__ == "__main__":
    print(json.dumps({"finite_unrestricted_endpoint_check": finite_seeds(8),
                      "later_certificates": [family(h) for h in (2, 4, 6)]},
                     indent=2))
