"""Exact finite controls for NUMEN_INVERSE_FIBER.md; no infinite proof claim."""
from fractions import Fraction
import json

TABLE = {1: (4, 8), 2: (3, 7), 4: (6, 8), 5: (3, 5), 7: (4, 6), 8: (5, 7)}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def valuation3(n):
    require(n != 0, "valuation requested at zero")
    n = abs(n)
    v = 0
    while n % 3 == 0:
        n //= 3
        v += 1
    return v


def finite_numen(code):
    require(code >= 0, "negative finite binary code")
    answer = Fraction(0)
    power3 = 1
    position = 0
    while code:
        if code & 1:
            answer += Fraction(power3, 2 ** (position + 1))
            power3 *= 3
        code >>= 1
        position += 1
    return answer


def verify_prefix(root, state, clock, count, code):
    require(root > 0 and state > 0, "nonpositive ordinary state")
    require(root % 2 == 1 and state % 2 == 1, "even odd-clock state")
    require(root % 3 != 0 and state % 3 != 0, "nonunit state")
    require(code.bit_length() == clock, "last one not at the stated clock")
    require(code.bit_count() == count, "wrong odd count")
    partial = finite_numen(code)
    tail = Fraction(3 ** count * state, 2 ** clock)
    require(Fraction(root) - partial == tail, "affine/series prefix mismatch")
    require(valuation3(tail.numerator) - valuation3(tail.denominator) == count,
            "wrong exact 3-adic valuation")
    require(partial <= Fraction(1, 5), "real series exceeded the proved bound")
    return partial


def main():
    for residue, expected in TABLE.items():
        actual = tuple(e for e in range(3, 9) if (2 ** e * residue) % 9 in (4, 7))
        require(actual == expected, "residue table mismatch")
    require(finite_numen(2) == Fraction(1, 4), "numen normalization mismatch")
    rays = []
    controls = []
    prefixes = 0
    for root in (1, 7):
        for selector in ("smaller", "alternating"):
            q, clock, code, states = root, 0, 0, [root]
            for i in range(128):
                e = TABLE[q % 9][0 if selector == "smaller" else i % 2]
                numerator = 2 ** e * q - 1
                require(numerator % 3 == 0, "nonintegral inverse edge")
                nxt = numerator // 3
                require(nxt > q and nxt % 2 == 1 and nxt % 3 != 0,
                        "invalid increasing unit predecessor")
                require(3 * nxt + 1 == 2 ** e * q, "wrong affine edge")
                # Since q is odd, e is the exact forward valuation.
                require(((3 * nxt + 1) >> e) == q and q % 2 == 1,
                        "wrong exact forward exponent")
                q = nxt
                clock += e
                code += 2 ** (clock - 1)
                verify_prefix(root, q, clock, i + 1, code)
                states.append(q)
                prefixes += 1
            if root == 1 and selector == "smaller":
                require(states[:7] == [1, 5, 13, 277, 1477, 7877, 21005],
                        "displayed root-one sequence mismatch")
            controls.append((root, q, clock, 128, code))
            rays.append({"root": root, "selector": selector, "odd_depth": 128,
                         "bit_clock": clock, "last_state_digits": len(str(q)),
                         "initial_states": states[:9]})
    damaged = []
    root, state, clock, count, code = controls[0]
    for name, args in (
        ("altered_state", (root, state + 2, clock, count, code)),
        ("altered_clock", (root, state, clock + 1, count, code)),
        ("altered_code", (root, state, clock, count, code ^ 1)),
    ):
        try:
            verify_prefix(*args)
        except ValueError:
            damaged.append(name)
        else:
            raise ValueError("damaged prefix accepted: " + name)
    x, orbit = 7, [7]
    while x != 1:
        require(len(orbit) < 64, "unexpected forward orbit length")
        x = x // 2 if x % 2 == 0 else (3 * x + 1) // 2
        orbit.append(x)
    require(len(set(orbit)) == len(orbit), "7 orbit repeats before 1")
    print(json.dumps({"scope": "finite arithmetic controls only; infinite claims are written",
                      "residue_classes": len(TABLE), "prefixes": prefixes,
                      "rays": rays, "damaged_prefixes_rejected": damaged,
                      "forward_orbit_of_7": orbit}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
