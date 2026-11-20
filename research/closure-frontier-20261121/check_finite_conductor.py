#!/usr/bin/env python3
"""Exact finite checks for FINITE_CONDUCTOR_RIGIDITY.md.

No floating point, package dependencies, or disabled-by-optimization asserts.
The finite census supports, and does not replace, the universal proofs.
"""

from collections import Counter
from fractions import Fraction
from math import gcd, isqrt
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def shortcut(n, sign=1):
    return n // 2 if n % 2 == 0 else (3 * n + sign) // 2


def parity_word(n, length, sign=1):
    word = []
    for _ in range(length):
        word.append(n % 2)
        n = shortcut(n, sign)
    return tuple(word), n


def exact_independence(r, endpoint=None):
    require(r >= 1, "positive dyadic depth required")
    q = 1 << r
    parity_counts = Counter(parity_word(n, r)[0] for n in range(q))
    require(len(parity_counts) == q, "parity coding not onto")
    require(set(parity_counts.values()) == {1}, "parity coding not injective")
    pairs = Counter()
    for n in range(q * q):
        end = parity_word(n, r)[1] if endpoint is None else endpoint(n, r)
        pairs[n % q, end % q] += 1
    require(len(pairs) == q * q, "endpoint product distribution has missing pairs")
    require(set(pairs.values()) == {1}, "endpoint product distribution not uniform")
    # One-step uniform pushforward, independently of the r-step test.
    counts = Counter(shortcut(n) % q for n in range(2 * q))
    require(counts == Counter({i: 2 for i in range(q)}), "one-step Haar pushforward failed")
    return {"r": r, "parity_words": q, "endpoint_pairs": q * q}


def dyadic_boolean_census(r):
    q = 1 << r
    total = 1 << q
    for mask in range(total):
        ones = mask.bit_count()
        defect = sum(((mask >> (n % q)) ^ (mask >> (shortcut(n) % q))) & 1
                     for n in range(2 * q))
        # 2*ones*(q-ones)/q^2 <= r*defect/(2q).
        require(4 * ones * (q - ones) <= r * q * defect,
                "dyadic Boolean coercivity violated")
    return {"r": r, "q": q, "all_boolean_labels": total}


def quotient_data(q):
    require(q > 1 and gcd(q, 6) == 1, "conductor must exceed one and be coprime to six")
    k = (q - 1).bit_length()
    length = 1 << k
    inv2 = pow(2, -1, q)
    for x in range(q):
        # Endpoints of the four-edge affine commutator.
        half = x * inv2 % q
        require((2 * (3 * half + 1)) % q == (3 * x + 2) % q,
                "commutator endpoint mismatch")
        counts = Counter((length * x + u) % q for u in range(length))
        require(len(counts) == q and min(counts.values()) >= 1,
                "binary averaging missed a target")
        require(length < 2 * q, "binary averaging constant exceeded")
    return k, length


def coprime_boolean_census(q):
    k, length = quotient_data(q)
    total = 1 << q
    for mask in range(total):
        def value(x):
            return (mask >> (x % q)) & 1
        a = sum(value(2 * x) != value(x) for x in range(q))
        b = sum(value(3 * x + 1) != value(x) for x in range(q))
        d = sum(value(x + 1) != value(x) for x in range(q))
        ones = mask.bit_count()
        require(d <= 2 * a + 2 * b, "translation comparison violated")
        require(2 * ones * (q - ones) <= length * k * (2 * a + b),
                "binary averaging coercivity violated")
    return {"q": q, "k": k, "all_boolean_labels": total}


def mean_pair_distance(histogram):
    # Integer-valued labels; compute sum_{a,b}|a-b| without a quadratic loop.
    count = sum(histogram.values())
    below_count = 0
    below_sum = 0
    numerator = 0
    for value, multiplicity in sorted(histogram.items()):
        numerator += 2 * multiplicity * (value * below_count - below_sum)
        below_count += multiplicity
        below_sum += value * multiplicity
    return Fraction(numerator, count * count)


def tent_check(r):
    require(r >= 2 and r % 2 == 0, "positive even tent length required")
    m = r // 2
    weights = list(range(1, m + 1)) + list(range(m, 0, -1))
    variance = sum(w * w for w in weights)
    require(variance * 3 == m * (m + 1) * (2 * m + 1), "tent variance formula")
    height = isqrt(variance)
    if height * height < variance:
        height += 1
    differences = [-weights[0]] + [weights[i - 1] - weights[i] for i in range(1, r)] + [weights[-1]]
    require(sum(w * w for w in differences) == r, "tent difference variance")
    require(12 * variance >= r ** 3, "tent cubic variance bound")
    # Exact independent-sign sum distribution.
    distribution = Counter({0: 1})
    for weight in weights:
        next_distribution = Counter()
        for value, count in distribution.items():
            next_distribution[value + weight] += count
            next_distribution[value - weight] += count
        distribution = next_distribution
    total = 1 << r
    second = sum(value ** 2 * count for value, count in distribution.items())
    fourth = sum(value ** 4 * count for value, count in distribution.items())
    require(second == total * variance, "second-moment identity")
    require(fourth == total * (3 * variance ** 2 - 2 * sum(w ** 4 for w in weights)),
            "fourth-moment identity")
    positive_tail = sum(count for value, count in distribution.items()
                        if value > 0 and 4 * value * value >= variance)
    require(32 * positive_tail >= 3 * total, "Paley-Zygmund sign bound")
    clipped = Counter()
    for value, count in distribution.items():
        clipped[max(-height, min(height, value))] += count
    oscillation = mean_pair_distance(clipped) / height
    require(oscillation >= Fraction(9, 1024), "tent oscillation lower bound")
    # Literal shortcut parity streams, not direct bit shifts, independently
    # audit that the construction really is a label of ordinary residue n.
    labels = []
    for n in range(total):
        bits, _ = parity_word(n, r)
        raw = sum(w * (2 * bit - 1) for w, bit in zip(weights, bits))
        labels.append(max(-height, min(height, raw)))
    require(Counter(labels) == clipped, "ordinary parity label distribution")
    defect_numerator = sum(abs(labels[n % total] - labels[shortcut(n) % total])
                           for n in range(2 * total))
    defect = Fraction(defect_numerator, 2 * total * height)
    require(defect * defect <= Fraction(r, height * height), "clipped difference bound")
    require(r * r * defect * defect <= 12, "O(1/r) defect bound")
    return {"r": r, "variance": variance, "rational_denominator": height,
            "oscillation": str(oscillation), "defect": str(defect)}


def negative_control_label(n, cache):
    # Exact finite orbit classification for the positive 3n-1 map.
    # A repeat certifies a cycle without assuming all starting values terminate.
    path = []
    positions = {}
    value = n
    while value not in cache and value not in positions:
        require(len(path) < 100000, "negative-control orbit exceeds scope")
        positions[value] = len(path)
        path.append(value)
        value = shortcut(value, sign=-1)
    if value in cache:
        label = cache[value]
    else:
        cycle = path[positions[value]:]
        label = int(1 in cycle)
    for value in path:
        cache[value] = label
    return label


def finite_source_controls():
    cache = {1: 1}
    rows = []
    for r in range(1, 9):
        q = 1 << r
        nmax = 16 * q
        cutoff = 3 * nmax // 2
        values = {n: negative_control_label(n, cache) for n in range(1, cutoff + 1)}
        require(values[1] == 1 and values[5] == 0, "control must be nonconstant")
        counts = [[0, 0] for _ in range(q)]
        for n, label in values.items():
            counts[n % q][label] += 1
        approximation = [int(one > zero) for zero, one in counts]
        errors = sum(values[n] != approximation[n % q] for n in range(1, cutoff + 1))
        minority = min(sum(values[n] == 0 for n in range(1, nmax + 1)),
                       sum(values[n] == 1 for n in range(1, nmax + 1)))
        require(errors > 0 and minority > 0, "nontrivial error/minority control")
        for n in range(1, nmax + 1):
            require(values[n] == negative_control_label(shortcut(n, sign=-1), cache),
                    "finite control label not invariant")
        edge = sum(approximation[n % q] != approximation[shortcut(n, sign=-1) % q]
                   for n in range(1, 2 * q + 1))
        require(nmax * edge <= 6 * q * errors, "finite edge-to-error bound")
        require(minority <= (1 + 3 * r) * errors, "finite-source inequality")
        rows.append({"r": r, "N": nmax, "cutoff": cutoff,
                     "minority": minority, "approximation_errors": errors})
    return rows


def reject_controls():
    cases = [lambda: quotient_data(6), lambda: quotient_data(9),
             lambda: exact_independence(0), lambda: tent_check(3),
             lambda: exact_independence(3, lambda n, r: n)]
    for index, case in enumerate(cases):
        try:
            case()
        except ValueError:
            continue
        raise ValueError("damaged input accepted: " + str(index))
    return len(cases)


def main():
    report = {
        "status": "PASS",
        "scope": "Finite exact audits only; universal claims use written proofs; no Collatz proof.",
        "dyadic_independence": [exact_independence(r) for r in range(1, 9)],
        "dyadic_boolean_censuses": [dyadic_boolean_census(r) for r in range(1, 5)],
        "coprime_boolean_censuses": [coprime_boolean_census(q) for q in (5, 7, 11, 13)],
        "coprime_affine_moduli": sum(1 for q in range(5, 256) if gcd(q, 6) == 1 and quotient_data(q)),
        "tent_labels": [tent_check(r) for r in range(2, 17, 2)],
        "finite_source_negative_controls": finite_source_controls(),
        "rejected_damaged_inputs": reject_controls(),
        "external_predecessor_theorem_replayed": False,
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
