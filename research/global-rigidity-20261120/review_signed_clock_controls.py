#!/usr/bin/env python3
"""Small independent exact controls for SF1 and its signed cancellation."""
from fractions import Fraction as F
import json


def need(test, message):
    if not test:
        raise ValueError(message)


def step(x):
    x = F(x)
    need(x > 0 and x.denominator % 2 and x.numerator % 2,
         'positive odd rational state')
    y = 3 * x + 1
    numerator = y.numerator
    a = 0
    while numerator % 2 == 0:
        numerator //= 2
        a += 1
    need(a >= 1, 'odd step must divide by two')
    return y / 2**a, a


def main():
    cases = edges = 0
    horizon = 12
    for ell in range(1, 7):
        rho = F(1) + F(2, 3) ** ell
        rational_values, gaps, totals = [rho], [], [0]
        for _ in range(horizon):
            image, a = step(rational_values[-1])
            rational_values.append(image)
            gaps.append(a)
            totals.append(totals[-1] + a)
        base = 3 ** (ell - 1)
        v = 0
        while 1 + (2 * v + 1) * base + ell - 1 <= totals[-1]:
            v += 1
        for offset in (0, 2, 5):
            H = 1 + (2 * (v + offset) + 1) * base
            need(H % 2 == 0 and (H - 1) % base == 0, 'admissible H')
            numerator = 2 ** (H - 1) + 1
            need(numerator % 3**ell == 0, 'positive root divisibility')
            m = numerator // 3**ell
            n = 2**ell * m - 1
            root = (2**H - 1) // 3
            need(n > 0 and n % 2 and m % 2, 'ordinary odd witnesses')
            x = F(n)
            landing_product = F(1)
            for j in range(ell):
                need(x == 2 ** (ell - j) * 3**j * m - 1, 'landing path formula')
                landing_product *= 3 * x / (3 * x + 1)
                x, a = step(x)
                need(a == (1 if j < ell - 1 else H), 'exact landing gap')
                edges += 1
            need(x == 1 and root == 2 * 3 ** (ell - 1) * m - 1,
                 'landing root hits one')
            exact_landing_product = F(n * 3**ell, 2 ** (H + ell - 1))
            need(landing_product == exact_landing_product,
                 'product includes exactly ell pre-landing inputs')
            for later in range(1, 5):
                landing_product *= F(3, 4)
                # All subsequent ordinary states are the fixed odd state 1.
                need(x == 1 and landing_product == exact_landing_product * F(3, 4) ** later,
                     'cycle after landing')
            x = F(n + 2)
            delta = F(2 ** (H + ell - 1), 3**ell)
            need(x == rho + delta, 'adjacent decomposition')
            for j in range(horizon + 1):
                need(x == rational_values[j] + F(3**j, 2 ** totals[j]) * delta,
                     'finite ordinary/rational affine identity')
                need(x.denominator == 1 and x > 0 and x.numerator % 2,
                     'actual ordinary neighboring state')
                if j < horizon:
                    x, a = step(x)
                    need(a == gaps[j], 'stable finite valuation word')
                    edges += 1
            cases += 1
    c = F(3, 4)
    # This normalized signed filter cancels every ell=1 jump, so the
    # longer-landing construction is essential to the full classification.
    alpha = [F(4), F(0), F(-7), F(4)]
    def G(ell):
        return sum((a if q <= ell else a * c ** (q - ell)
                    for q, a in enumerate(alpha)), F(0))
    need(sum(alpha) == 1 and G(1) == 1 and G(2) == 0,
         'one-landing cancellation control')
    for ell in range(1, 6):
        tail = sum((a * c ** (q - ell - 1)
                    for q, a in enumerate(alpha) if q >= ell + 1), F(0))
        need(G(ell + 1) - G(ell) == (1 - c) * tail,
             'signed tail recurrence')
    print(json.dumps({
        'status': 'PASS independent finite controls',
        'landing_times': [1, 6],
        'rational_neighbor_horizon': horizon,
        'ordinary_pair_cases': cases,
        'exact_ordinary_edges': edges,
        'signed_filter': ['4', '0', '-7', '4'],
        'signed_G1': str(G(1)), 'signed_G2': str(G(2)),
        'scope': 'finite controls only; classification and all horizons use the written proof',
    }, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
