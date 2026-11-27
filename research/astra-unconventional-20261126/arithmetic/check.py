"""Exact cycle identities and certified upper counts for the model spacing problem."""

import json
from fractions import Fraction
from math import gcd


def require(condition, message):
    if not condition:
        raise ValueError(message)


def cycle(word):
    exponents = [int(a) for a in word]
    p, h = len(word), sum(exponents)
    determinant = 2**h - 3**p
    carry = 0
    elapsed = 0
    for a in exponents:
        carry = 3 * carry + 2**elapsed
        elapsed += a
    x0 = Fraction(carry, determinant)
    d = x0.denominator
    xs = [x0]
    for a in exponents:
        y = (3 * xs[-1] + 1) / 2**a
        require(y.numerator % 2 == 1 and y.denominator == d, "physical gap")
        xs.append(y)
    require(xs.pop() == x0 and len(set(xs)) == p, "primitive closure")
    minimum = min(xs)
    origin = xs.index(minimum)
    xs = xs[origin:] + xs[:origin]
    exponents = exponents[origin:] + exponents[:origin]
    bands = [max(k for k in range(3) if x >= 2**k * minimum) for x in xs]
    mantissas = [4 * x / 2**k for x, k in zip(xs, bands)]
    order = sorted(range(p), key=lambda i: mantissas[i])
    require([i * h % p for i in order] == list(range(p)), "rank permutation")
    require(all(minimum <= z / 4 < 2 * minimum for z in mantissas), "bands")
    numerators = [int(d * z) for z in mantissas]
    require(all(n == d * z for n, z in zip(numerators, mantissas)), "lattice")
    for i, z in enumerate(mantissas):
        rank = i * h % p
        b = (rank + h) // p
        c = 2 ** (2 - bands[i])
        require(2**b * mantissas[(i + 1) % p] == 3 * z + c, "folded edge")
        lower = max(0, (z - 6 * p) / (4 * minimum))
        upper = (z + 6 * p) / (4 * minimum)
        require(lower**p <= 2**rank <= upper**p, "exact geometric envelope")
    observations = []
    for k in (1, 2, 4, 7, 16, 2 * p + 1):
        q = 3**k
        dictionary = {}
        for j in range(p):
            word_key = tuple(exponents[i % p] for i in range(j - k, j))
            residue = int(d * xs[j]) % q
            require(dictionary.setdefault(word_key, residue) == residue, "incoming word")
            require(numerators[j] % q == (2 ** (2 - bands[j]) * residue) % q, "folded residue")
        observations.append([k, len(dictionary), len({n % q for n in numerators})])
    require(d == determinant // gcd(carry, determinant), "complete denominator")
    return {
        "odd_period": p,
        "shortcut_period": h,
        "minimum": str(minimum),
        "determinant": determinant,
        "reduced_denominator": d,
        "incoming_k_words_residues": observations,
    }


def scaled_roots(p, scale):
    """Return exact floors of scale * 2**(r/p), without real logarithms."""
    scale_power = scale**p
    roots = []
    for r in range(p):
        target = scale_power << r
        lo, hi = scale, 2 * scale
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            if mid**p <= target:
                lo = mid
            else:
                hi = mid
        require(lo**p <= target < (lo + 1) ** p, "integer root certificate")
        roots.append(lo)
    return roots


def spacing_control(p):
    scale = 2**52
    roots = scaled_roots(p, scale)
    trials = []
    for numerator, denominator in [(1, 1), (3, 1), (7, 1), (p, 3), (p, 1), (p**2, 1), (p**3, 1)]:
        modulus = scale * denominator
        count, undecided = p, 0
        for j, z in enumerate(roots):
            for y in roots[:j]:
                t = (numerator * (z - y)) % modulus
                distance = min(t, modulus - t)
                # Each root has error in [0,1), so the difference has error < 1.
                if p * (distance - numerator) <= modulus:
                    count += 2
                    if p * (distance + numerator) > modulus:
                        undecided += 2
        trials.append({"R": str(Fraction(numerator, denominator)),
                       "pairs_upper": count, "uncertain_pairs": undecided})
    return {"p": p, "K": 1, "trials": trials}


def main():
    controls = [cycle(word) for word in ("2", "11222", "12112121212211222212212121221122212211222")]
    results = {"scope": "Finite exact controls. Model pair counts do not establish an asymptotic bound.",
               "cycles": controls, "spacing": [spacing_control(p) for p in (41, 97, 211)]}
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
