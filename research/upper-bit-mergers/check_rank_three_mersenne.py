"""Verify the finite words and exponent classes in the rank-three Mersenne transfer."""

from check import step


# Indexed by the residue of q + log_2(t mod 27) modulo 18.
TEMPLATES = (
    (39, 271, 132), (0, 1, 0), (63, 412, 197), (1, 2, 0),
    (38, 271, 133), (57, 355, 167), (62, 412, 198), (124, 1027, 524),
    (78, 569, 281), (56, 355, 168), (79, 569, 280), (169, 1298, 650),
    (60, 412, 200), (6, 19, 6), (61, 412, 199), (7, 19, 5),
    (81, 569, 278), (183, 1298, 636),
)


def verify_templates():
    units = {pow(2, j, 27) for j in range(18)}
    if len(units) != 18:
        raise AssertionError("2 must generate all units modulo 27")
    for residue, (d, clock, expected_odds) in enumerate(TEMPLATES):
        value = -(3**d + 1)
        odds = 0
        for _ in range(clock):
            if value == -1:
                raise AssertionError((residue, "early arrival at -1"))
            odds += value % 2
            value = step(value)
        if (value, odds) != (-1, expected_odds):
            raise AssertionError((residue, value, odds))
        # Write t = 2^j mod 27. All q in this row equal residue - j mod 18.
        c = d + 2
        for j in range(18):
            q = (residue - j) % 18
            exponent = (q + clock - d - odds + c + 2) % 18
            if (pow(2, exponent + j, 27) - pow(2, c + 2, 27) - 21) % 27:
                raise AssertionError((residue, j, "nonintegral inverse word"))
        if clock <= d + odds:
            raise AssertionError((residue, "the inverse exponent must exceed q"))
    threshold = max(d + odds for d, _, odds in TEMPLATES)
    if threshold != 819:
        raise AssertionError(("threshold", threshold))
    return threshold


def verify_small_mersennes(threshold):
    longest = (0, 0)
    for q in range(1, threshold):
        value = 3**q - 1
        for clock in range(6501):
            if value == 1:
                longest = max(longest, (clock, q))
                break
            value = step(value)
        else:
            raise AssertionError((q, "small case did not reach 1"))
    return longest


if __name__ == "__main__":
    threshold = verify_templates()
    clock, exponent = verify_small_mersennes(threshold)
    print(f"Verified 18 signed words and all 324 modulus-27 residue combinations; "
          f"symbolic transfer covers q >= {threshold}.")
    print(f"All {threshold - 1} smaller positive exponents reach 1; "
          f"longest tail from 3^q-1 was {clock} steps at q={exponent}.")
