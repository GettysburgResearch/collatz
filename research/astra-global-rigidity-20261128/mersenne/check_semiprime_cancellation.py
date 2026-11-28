"""Verify finite four-prime deadline examples on the exact two octave scales."""
import json
from math import gcd, isqrt


def trial_prime(p):
    return p >= 2 and all(p % r for r in range(2, isqrt(p) + 1))


def certify_band(p, bits):
    # 69/100 < ln(2) < 70/100. Compare rational powers with integers.
    return ((100 ** 21) * p ** 20 > (70 * bits) ** 21 and
            (100 ** 23) * p ** 20 < (69 * bits) ** 23)


def pocklington(power, coefficient, witness):
    modulus = coefficient * (2 ** power) + 1
    known = 2 ** power
    if (known * known <= modulus or pow(witness, modulus - 1, modulus) != 1
            or gcd(pow(witness, (modulus - 1) // 2, modulus) - 1, modulus) != 1):
        raise ValueError("invalid 2-power Pocklington certificate")
    return modulus


def trajectory(n):
    states = [n]
    for _ in range(2_000):
        if states[-1] == 1:
            return states
        x = states[-1]
        states.append((3 * x + 1) // 2 if x % 2 else x // 2)
    raise ValueError(f"unverified trajectory from {n}")


def check(k, small, large, cofactor_rows):
    d = small * large
    if not (small < large and trial_prime(small) and trial_prime(large)
            and 2 ** k < d <= 2 ** (k + 1) and certify_band(small, k)):
        raise ValueError("invalid first semiprime")
    d_path = trajectory(d)
    if len(d_path) - 1 <= 5 * d.bit_length():
        raise ValueError("prefix did not miss its deadline")
    rows = []
    for target, p, power, coefficient, witness, expected_one in cofactor_rows:
        q = pocklington(power, coefficient, witness)
        m = p * q
        if not (p < q and trial_prime(p) and gcd(d, m) == 1
                and 2 ** (k*k) < m <= 2 ** (k*k + 1) and certify_band(p, k*k)):
            raise ValueError("invalid coprime second semiprime")
        n = d * m
        path = trajectory(n)
        opposite = 85 if target == 5 else 5
        if (target not in path or opposite in path or len(path) - 1 != expected_one
                or expected_one > 5 * n.bit_length()):
            raise ValueError("invalid product trajectory certificate")
        rows.append(dict(target=target, small_prime=p, power_of_two=power,
                         coefficient=coefficient, pocklington_witness=witness,
                         large_prime=q, cofactor=m, product=n,
                         first_target=path.index(target), first_one=expected_one,
                         deadline=5 * n.bit_length()))
    return dict(k=k, prefix=d, prefix_primes=[small, large],
                prefix_first_one=len(d_path)-1, prefix_deadline=5*d.bit_length(),
                cofactor_rows=rows)


if __name__ == '__main__':
    controls = [
        check(9, 7, 79, [
            (5, 71, 39, 61_944_317_087, 3, 309),
            (85, 71, 39, 61_944_320_231, 3, 293),
        ]),
        check(14, 11, 1_493, [
            (5, 179, 96, 7_081_846_928_649_326_265_344_710_785, 41, 1_017),
            (85, 179, 96, 7_081_846_928_649_326_265_344_711_437, 3, 844),
        ]),
    ]
    print(json.dumps(controls, indent=2))
