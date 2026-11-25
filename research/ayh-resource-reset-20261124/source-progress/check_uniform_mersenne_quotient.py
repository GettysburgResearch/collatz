"""Exhaust the finite quotient proved in UNIFORM_MERSENNE_QUOTIENT.md.

Every loop below is bounded before it runs. A failure to classify a center
within the replay clock is an error, never a reason to discard that center.
"""
from fractions import Fraction

CAP = Fraction(1024, 81)
OFFSET = Fraction(527, 81)
# (period, odd count, calibrated upper constant)
CYCLES = {-1: (1, 1, 1), -5: (3, 2, 5), -17: (11, 7, 18)}
STATES = [(-1, 0, 0), (-1, 1, 0), (-17, -1, 3), (-5, 2, 1)]


def require(test, context):
    if not test:
        raise ValueError(context)


def classify(center):
    """Return first chosen phase, number of shortcut steps, and odd count."""
    odds = 0
    for length in range(2001):
        if center in CYCLES or center in (0, 1):
            return int(center), length, odds
        odd = center.numerator % 2
        center = ((3 * center + 1) if odd else center) / 2
        odds += odd
    raise ValueError(("unclassified finite center", center))


def normalized(phase, length, odds, u, v):
    period, odd_period, _ = CYCLES[phase]
    require(v + odds >= 0, (phase, length, odds, u, v))
    turns, residue = divmod(v + odds, odd_period)
    return phase, u - length + period * turns, residue


def query_edges(state, base_exponent=97, cap=CAP, offset=OFFSET):
    phase, U, V = state
    period, odd_period, calibration = CYCLES[phase]
    # Replacing the rational exponent period*V/odd_period by its floor
    # only enlarges the search. The integer-center case already has v>=0.
    coarse_scale = Fraction(2) ** (U + period * V // odd_period)
    bound_integer = calibration * cap / coarse_scale
    for y in range(15, int(bound_integer) + 1, 16):
        require(classify(Fraction(-y))[0] != phase, ("integral candidate", state, y))
    edges = []
    for d in range(1, 5):
        den = 3 ** d
        bound_m = int(bound_integer * Fraction(9, 2) ** d)
        for m in range(den, bound_m + 1):
            if m % 3 == 0 or (m + 17 * den) % 16:
                continue
            c = Fraction(-m, den)
            seen_phase, length, odds = classify(c)
            if seen_phase != phase:
                continue
            _, shift, residue = normalized(phase, length, odds, 0, -d)
            if residue != V:
                continue
            u = U - shift
            alpha = Fraction(2) ** u / den
            if alpha > cap or (alpha == cap and c >= -offset):
                continue
            # Use a sufficiently large ordinary exponent on the actual row.
            # Comparing the mod-48 residues at j and j+162 certifies all lifts
            # because 3^(d+1) divides 2^162-1 and both binary terms vanish mod 16.
            j = base_exponent + 162 * max(0, (4 - u - base_exponent + 161) // 162)
            require(j + u >= 4 and (2**162-1) % (3*den) == 0, (state, d, u, j))
            val = alpha * 2**j + c
            if val.denominator != 1 or val % 48 != 17:
                continue
            other, H, O = classify(3*c)
            nxt = normalized(other, H, O, u, 1-d) if other in CYCLES else other
            edges.append((d, m, u, length, odds, H, O, nxt))
    return edges


if __name__ == "__main__":
    require((2**162-1) % 243 == 0 and (2**162-1) % 729 != 0, "ternary precision")
    got = [query_edges(s) for s in STATES]
    expected = [
        [(3, 341, 8, 8, 3, 9, 5, (-17, -1, 3))],
        [(1, 13, 5, 5, 2, 6, 3, (-5, 2, 1))],
        [], [],
    ]
    require(got == expected, got)
    for state, rows in zip(STATES, got):
        print(f"{state}: {rows}")
    for state in STATES[:2]:
        rows = query_edges(state, 11, Fraction(128, 81), Fraction(271, 81))
        require(not rows, ("e=6", state, rows))
        print(f"e=6 {state}: {rows}")
