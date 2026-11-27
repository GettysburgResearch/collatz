"""Exact small-level controls for the primitive transfer and its cyclic Gram kernel."""

from fractions import Fraction
from functools import lru_cache
import json
from math import isqrt


def require(condition, label):
    if not condition:
        raise AssertionError(label)


def factors(value):
    return {p for p in range(2, value + 1) if value % p == 0 and prime(p)}


def prime(value):
    return value >= 2 and all(value % d for d in range(2, isqrt(value) + 1))


def root_of_order(order, prime_modulus):
    for seed in range(2, prime_modulus):
        candidate = pow(seed, (prime_modulus - 1) // order, prime_modulus)
        if all(pow(candidate, order // p, prime_modulus) != 1 for p in factors(order)):
            return candidate
    raise ValueError("missing root of unity")


def cyclic_weights(order, prime_modulus):
    denom = pow(pow(2, order, prime_modulus) - 1, -1, prime_modulus)
    return [pow(2, order - e, prime_modulus) * denom % prime_modulus
            for e in range(1, order + 1)]


def next_law(parent, modulus, prime_modulus):
    order = 2 * modulus // 3
    result = [0] * modulus
    for e, weight in enumerate(cyclic_weights(order, prime_modulus), start=1):
        multiplier = pow(2, -e, modulus)
        for x, probability in enumerate(parent):
            target = multiplier * (1 + 3 * x) % modulus
            result[target] += probability * weight
    return [value % prime_modulus for value in result]


def check_field(q):
    full_order = 6 * q
    p = 1 + full_order
    while not prime(p) or pow(2, 2 * q, p) == 1:
        p += full_order
    generator = root_of_order(full_order, p)
    n = 2 * q
    N = n // 3
    input_residues = [pow(2, j, q) for j in range(N)]
    output_residues = [pow(2, j, 3 * q) for j in range(n)]
    logs = {x: j for j, x in enumerate(output_residues)}
    require(len(set(input_residues)) == N and len(logs) == n, "cyclic generators")

    def phase(index, order):
        return pow(generator, (full_order // order) * (index % order), p)

    @lru_cache(maxsize=None)
    def gauss(index, modulus):
        residues = input_residues if modulus == q else output_residues
        return sum(phase(index * j, len(residues)) * phase(x, modulus)
                   for j, x in enumerate(residues)) % p

    @lru_cache(maxsize=None)
    def matrix(r, s):
        return sum(phase(r * logs[1 + 3 * x], n) * phase(-s * j, N)
                   for j, x in enumerate(input_residues)) * pow(N, -1, p) % p

    parent = [1]
    level = 1
    while level < q:
        level *= 3
        parent = next_law(parent, level, p)
    child = next_law(parent, 3 * q, p)
    require(sum(parent) % p == sum(child) % p == 1, "probability normalization")
    parents = [s for s in range(N) if s % 3]
    children = [r for r in range(n) if r % 3]
    moments = {s: sum(phase(s * j, N) * parent[x] for j, x in enumerate(input_residues)) % p
               for s in parents}
    for r in children:
        require(all(matrix(r, s) == 0 for s in range(0, N, 3)), "input conductor separation")
        for s in parents:
            numerator = gauss(-s, q) * gauss(-r + 3 * s, 3 * q)
            denominator = N * gauss(-r, 3 * q)
            require(matrix(r, s) * denominator % p == numerator % p, "Gauss ratio")
            require(matrix(r, s) * matrix(-r, -s) * N**2 % p == q % p, "Gauss modulus")
        current = sum(phase(r * j, n) * child[x] for j, x in enumerate(output_residues))
        require(current * (2 * phase(r, n) - 1) % p == sum(matrix(r, s) * moments[s] for s in parents) % p, "original-law primitive recurrence")
    for s in parents:
        for t in parents:
            require(sum(matrix(-r, -s) * matrix(r, t) for r in children) % p == 3 * (s == t), "tight frame columns")
    require(all(matrix(r, s) == 0 for r in range(0, n, 3) for s in parents), "output conductor separation")
    return {"q": q, "prime_for_Gauss_and_frame_replay": p,
            "primitive_input": len(parents), "primitive_output": len(children)}


def check_gram(q):
    n = 2 * q
    r = Fraction(1, 2)
    weights = [r ** (j if j else n) / (1 - r**n) for j in range(n)]
    allowed = [j for j in range(n) if j % 6 in (2, 4)]
    for s in allowed:
        for t in allowed:
            distance = (s - t) % n
            expected = (r**distance + r ** (n - distance)) / (1 - r**n)
            dot = sum(weights[(j - s) % n] * weights[(j - t) % n] for j in range(n))
            require(3 * dot == expected, "exact rational cyclic Gram kernel")
    return len(allowed) ** 2


if __name__ == "__main__":
    receipts = []
    for q in [9, 27, 81]:
        row = check_field(q)
        row["exact_rational_Gram_entries"] = check_gram(q)
        receipts.append(row)
    print(json.dumps(receipts, indent=2))
