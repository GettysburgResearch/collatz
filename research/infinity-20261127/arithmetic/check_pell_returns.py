"""Exact controls for Pell return packing and the rank-31 exclusion."""

import json
from collections import Counter
from math import comb, isqrt


def require(test, message):
    if not test:
        raise ValueError(message)


def primes_from_five(count):
    result = []
    value = 5
    while len(result) < count:
        if all(value % d for d in range(2, isqrt(value) + 1)):
            result.append(value)
        value += 2
    return result


def log_weight(value, scale):
    return (value**scale).bit_length() - 1


def subset_weights(primes, scale):
    weights = Counter({0: 1})
    for prime in primes:
        shift = log_weight(prime, scale)
        shifted = {old + shift: count for old, count in weights.items()}
        weights.update(shifted)
    return weights


def numeric_rank_certificate():
    rank, steps, radius, scale = 31, 44, 12, 64
    floor = 2**71
    sphere = sum(comb(steps + 1, j) for j in range(radius + 1))
    require(sphere > 2**(rank + 4), "short even relation")
    clock = 69
    require((3 * floor + 1)**steps < 2**(clock + 1) * floor**steps,
            "record clock upper bound")
    require((3 * floor + 1)**steps < 2 * (3 * floor)**steps,
            "normalized record height")
    offset = 3**(steps - 1) + 2**(clock - steps + 1) * (
        3**(steps - 1) - 2**(steps - 1))
    threshold = (64 * (offset + 1))**(2 * radius + 2)
    height_bits = threshold.bit_length() - steps + 1
    require(height_bits == 2561, "odd maximum bound")
    primes = primes_from_five(rank)
    weights = subset_weights(primes, scale)
    require(sum(weights.values()) == 2**rank, "all pivot subsets")
    count = sum(
        frequency * (1 + scale * height_bits //
                     max(7 * scale, log_weight(12, scale) + parity * scale + weight))
        for weight, frequency in weights.items() for parity in (0, 1)
    )
    require(count == 127901154889 < 137500000000, "all-period rank exclusion")
    require(2**3321 < 10**1000 < 2**3322, "physical band rank")
    require(3 * 5**15 < 137500000000 <= 3 * 5**16, "cubeclass rank")
    return {
        "rank_hypothesis": rank,
        "record_odd_edges": steps,
        "hamming_ball_radius": radius,
        "hamming_ball_size": sphere,
        "available_vector_labels": 2**(rank + 4),
        "shortcut_clock_upper": clock,
        "offset_upper": str(offset),
        "strict_upper_log2_odd_maximum": height_bits,
        "pivot_primes": primes,
        "weight_log2_scale": scale,
        "distinct_weight_sums": len(weights),
        "rank_31_odd_period_upper": count,
        "published_odd_period_lower_comparison": 137500000000,
    }


def kfree(value, power):
    kernel = 1
    prime = 2
    while prime * prime <= value:
        exponent = 0
        while value % prime == 0:
            exponent += 1
            value //= prime
        kernel *= prime**(exponent % power)
        prime += 1 if prime == 2 else 2
    return kernel * value


def odd_step(x):
    numerator = 3*x + 1
    clock = (numerator & -numerator).bit_length() - 1
    return numerator >> clock, clock


def discriminant(x):
    # The consecutive factors are coprime.
    return kfree(3*x, 2) * kfree(3*x + 1, 2)


def literal_edge_controls():
    limit = 200001
    previous = {}
    repeated = 0
    cubes = set()
    first_pairs = []
    for x in range(1, limit, 2):
        y, a = odd_step(x)
        d = discriminant(x)
        require(kfree(3 * 2**(a % 2) * kfree(x, 2) * kfree(y, 2), 2) == d,
                "product squareclass")
        X = 6*x + 1
        V = isqrt((X*X - 1)//d)
        require(X*X - d*V*V == 1 and V % 2 == 0, "ordinary Pell identity")
        if d in previous:
            prior, old_X, old_V = previous[d]
            trace = X*old_X - d*V*old_V
            require(trace >= 97 and trace % 12 == 1, "Pell quotient trace")
            # x/prior > rho iff x/prior > 97 and (x/prior-97)^2 > 3*56^2.
            require(x > 97*prior and (x-97*prior)**2 > 3*(56*prior)**2,
                    "sharp absolute height ratio")
            require(x > 4*d*prior, "discriminant-specific height ratio")
            repeated += 1
            if len(first_pairs) < 8:
                first_pairs.append([d, prior, x, trace])
        previous[d] = (x, X, V)
        cube_code = (kfree(x, 3), kfree(y, 3), a % 3)
        require(cube_code not in cubes, "cubeclass edge collision")
        cubes.add(cube_code)
    require(repeated >= 3, "nonempty repeated-D controls")
    return {"odd_sources": len(cubes), "distinct_pell_discriminants": len(previous),
            "repeated_discriminants": repeated, "first_pairs": first_pairs}


def return_control(start, end):
    require(start != end and start > 0 and end > 0, "nontrivial return control")
    d = discriminant(start)
    require(d == discriminant(end), "same physical discriminant")
    source = start
    odd_count = clock = carry = 0
    seen = set()
    while source != end:
        require(source not in seen, "chosen end not on orbit")
        seen.add(source)
        if source % 2:
            carry = 3*carry + 2**clock
            odd_count += 1
            source = (3*source+1)//2
        else:
            source //= 2
        clock += 1
    A, B = 3**odd_count, 2**clock
    X, Y = 6*start+1, 6*end+1
    V, W = (isqrt((z*z-1)//d) for z in (X, Y))
    K, L = B*Y-A*X, B*W-A*V
    norm = K*K-d*L*L
    require(K == 6*carry+B-A and norm != 0, "nonzero norm at actual return")
    require(6*start*A < (2*abs(K)+1)*max(A*A, B*B), "exact norm time bound")
    return {"start": start, "end": end, "D": d, "shortcut_clock": clock,
            "odd_count": odd_count, "norm": str(norm)}


if __name__ == "__main__":
    report = {"certificate": numeric_rank_certificate(), "edges": literal_edge_controls(),
              "actual_returns": [return_control(225, 1), return_control(43681, 1)]}
    print(json.dumps(report, indent=2, sort_keys=True))
