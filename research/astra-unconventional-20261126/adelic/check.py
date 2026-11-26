"""Exact finite controls for the adelic lane. Uses only the Python standard library."""

from functools import cache
from itertools import combinations, product
from math import factorial, gcd, prod
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def native_step(x):
    numerator = 3 * x + 1
    divisor = numerator & -numerator
    return numerator // divisor, divisor.bit_length() - 1


def forward(x, odd_count):
    total = 0
    for _ in range(odd_count):
        x, elapsed = native_step(x)
        total += elapsed
    return x, total


@cache
def fiber(y, k, total):
    """All positive odd sources at the two specified exact grades."""
    if k == 0:
        return (y,) if total == 0 else ()
    if y % 3 == 0 or total < k:
        return ()
    sources = []
    for elapsed in range(1, total - k + 2):
        numerator = (y << elapsed) - 1
        if numerator % 3 == 0:
            sources.extend(fiber(numerator // 3, k - 1, total - elapsed))
    return tuple(sorted(sources))


def binomial_minor(points):
    degree = len(points) - 1
    denominator = prod(factorial(j) for j in range(degree + 1))
    numerator = prod(b - a for a, b in combinations(points, 2))
    require(numerator % denominator == 0, "integral binomial determinant")
    return numerator // denominator


def lattice_control(y, k, total, degree, modulus=2, residue=1):
    sources = fiber(y, k, total)
    require(len(sources) == len(set(sources)), "unique inverse realization")
    require(all(forward(x, k) == (y, total) for x in sources), "native replay")
    points = [(x - residue) // modulus for x in sources if x % modulus == residue]
    divisor, certificate = 0, []
    for sample in combinations(points, degree + 1):
        minor = binomial_minor(sample)
        updated = gcd(divisor, minor)
        if divisor != updated:
            certificate.append([list(sample), minor])
            divisor = updated
        if divisor == 1:
            break
    require(divisor > 0, "full rational rank")
    return dict(terminal=y, odd_count=k, shortcut_count=total, chart=[residue, modulus],
                degree=degree, source_count=len(points), index=divisor,
                improving_minors=certificate)


def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    d, u, v = extended_gcd(b, a % b)
    return d, v, u - (a // b) * v


def chart_basis(y, k, total, chart):
    points = [(x, (x - chart) // 6) for x in fiber(y, k, total) if x % 6 == chart]
    if len(points) < 2:
        return None
    anchor, t0 = points[0]
    difference, weights = 0, {}
    for x, t in points[1:]:
        new, a, b = extended_gcd(difference, t - t0)
        if difference == new:
            continue
        weights = {z: a * v for z, v in weights.items()}
        weights[x] = weights.get(x, 0) + b
        weights[anchor] = weights.get(anchor, 0) - b
        difference = new
        if difference == 1:
            break
    if difference != 1:
        return None
    zero = {x: -t0 * v for x, v in weights.items()}
    zero[anchor] = zero.get(anchor, 0) + 1
    return {x: (zero.get(x, 0), weights[x]) for x in weights
            if zero.get(x, 0) != 0 or weights[x] != 0}


def tensor_control(terminal, charts, k, total):
    """Materialize actual path rows and an integer left inverse of their moment matrix."""
    paths = [((), (), terminal)]
    for chart in reversed(charts):
        new_paths = []
        for outer, coeffs, y in paths:
            basis = chart_basis(y, k, total, chart)
            require(basis is not None, f"chart basis at {y}")
            for x, weights in basis.items():
                require(forward(x, k) == (y, total), "marked segment replay")
                new_paths.append((((x - chart) // 6,) + outer, (weights,) + coeffs, x))
        paths = new_paths
    indices = list(product((0, 1), repeat=len(charts)))
    rows = [[prod(t ** a for t, a in zip(ts, powers)) for powers in indices]
            for ts, _, _ in paths]
    largest_weight = 0
    for desired in indices:
        reconstruction = [0] * len(indices)
        for row, (_, coeffs, _) in zip(rows, paths):
            weight = prod(pair[j] for pair, j in zip(coeffs, desired))
            largest_weight = max(largest_weight, abs(weight))
            for j, value in enumerate(row):
                reconstruction[j] += weight * value
        require(reconstruction == [int(desired == j) for j in indices], "tensor identity")
    return dict(terminal=terminal, chart_residues=charts, odd_count_per_segment=k,
                shortcut_count_per_segment=total, marked_paths=len(paths),
                integral_identity_rank=len(indices), maximum_source=max(row[2] for row in paths),
                maximum_signed_coefficient=largest_weight)


def correction_control():
    """Perform inherited-precision CRT resets in an explicitly fixed seven-block word."""
    words = []
    for j in range(7):
        initial_ones = 12 + 2 * j
        words.append([1] * initial_ones + [1, 2, 1, 2, 2] * (7 + j))
    gap_script = sum(words, [])
    moduli = [15, 21, 35, 105, 315, 385, 1155]
    q, states, errors = 4095, [4095], []
    starts, evidence = [], []
    for i, (word, odd_modulus) in enumerate(zip(words, moduli)):
        starts.append(len(errors))
        next_bits = 12 + 2 * (i + 1)
        residue = (1 << next_bits) - 1
        precision = next_bits
        for elapsed in reversed(word[1:]):
            precision += elapsed
            modulus = 1 << precision
            residue = (((1 << elapsed) * residue - 1) * pow(3, -1, modulus)) % modulus
        two_power = 1 << (precision + word[0])
        target = ((residue << word[0]) - 3 * q) % two_power
        defect = target + two_power * (((1 - target) * pow(two_power, -1, odd_modulus)) % odd_modulus)
        if defect <= 1:
            defect += two_power * odd_modulus
        require((defect - 1) % ((1 << (12 + 2 * i)) * odd_modulus) == 0, "inherited precision")
        require(1 < defect <= 2 * two_power * odd_modulus, "CRT bound")
        for j, elapsed in enumerate(word):
            use = defect if j == 0 else 1
            require(native_step(q)[1] == elapsed, "native exponent at each edge")
            numerator = 3 * q + use
            require(numerator % (2 << elapsed) == 1 << elapsed, "corrected odd quotient")
            q = numerator >> elapsed
            states.append(q)
            errors.append(use)
        require(q % (1 << next_bits) == (1 << next_bits) - 1, "next reset class")
        evidence.append(dict(reset=starts[-1], defect_bits=defect.bit_length(),
                             inherited_bits=12 + 2 * i, odd_modulus=odd_modulus))
    windows = 0
    for i, start in enumerate(starts):
        width = 5 + i
        for begin in range(max(0, start - width + 1), start + 1):
            native = states[begin]
            for j in range(width):
                native, gap = native_step(native)
                require(gap == gap_script[begin + j], "native window script")
                require((native - states[begin + j + 1]) % (4 * moduli[i]) == 0,
                        "actual window state modulo the requested modulus")
            windows += 1
    return dict(start=states[0], edges=len(errors), corrections=len(starts),
                reset_evidence=evidence, windows_crossing_a_reset=windows,
                final_height_bits=q.bit_length())


def main():
    lattices = [lattice_control(1, 6, 18, 4), lattice_control(11, 4, 18, 4),
                lattice_control(1, 8, 26, 3, 6, 1), lattice_control(1, 8, 26, 3, 6, 5)]
    require(all(row["index"] == 1 for row in lattices), "full integral examples")
    neg = lattice_control(1, 4, 14, 4)
    require(neg["index"] == 77000, "short-clock negative control")
    result = dict(ordinary_lattices=lattices, early_failure=neg,
                  mixed_cuts=tensor_control(1, [5, 1, 5], 6, 26),
                  sparse_corrections=correction_control())
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
