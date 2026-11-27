"""Exact finite controls for the written ordinary mass-operator calculation.

All arithmetic is integral or rational. These are finite checks, not a proof
of the infinite spectral statement. No assertions are erased by python -O.
"""

from fractions import Fraction
from itertools import product
import json


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def step(n):
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def run(n, k):
    for _ in range(k):
        n = step(n)
    return n


def cylinder(word):
    """Return the unique residue for a prescribed finite parity word."""
    residue, endpoint, odd_count, modulus = 0, 0, 0, 1
    for bit in word:
        require(bit in (0, 1), "nonbinary word")
        if endpoint % 2 != bit:
            residue += modulus
            endpoint += 3**odd_count
        require(endpoint % 2 == bit, "parity steering")
        endpoint = step(endpoint)
        odd_count += bit
        modulus *= 2
    require(0 <= residue < modulus, "least residue")
    return residue, endpoint, odd_count


def push(vector, clock=1, floor=0):
    result = {}
    for n, coefficient in vector.items():
        x = n
        alive = x > floor
        for _ in range(clock):
            x = step(x)
            alive = alive and x > floor
        if alive:
            result[x] = result.get(x, Fraction(0)) + coefficient
    return {n: c for n, c in result.items() if c}


def minus_multiple(left, right, scalar):
    result = dict(left)
    for n, c in right.items():
        result[n] = result.get(n, Fraction(0)) - scalar * c
    return {n: c for n, c in result.items() if c}


def norm(vector, alpha):
    return sum((abs(c) * Fraction(n)**alpha for n, c in vector.items()), Fraction(0))


def main():
    cylinder_count = 0
    physical_steps = 0
    for length in range(1, 10):
        for word in product((0, 1), repeat=length):
            residue, endpoint, odd_count = cylinder(word)
            for lift in (0, 1, 7, 37):
                x = residue + 2**length * lift
                for bit in word:
                    require(x % 2 == bit, "physical parity realization")
                    x = step(x)
                    physical_steps += 1
                require(x == endpoint + 3**odd_count * lift, "affine cylinder endpoint")
                cylinder_count += 1

    floor_checks = 0
    for h in range(65):
        for floor in (0, 1, 2, 10**6, 2**80):
            u = floor + 2
            even, odd = 2**h * u, 2**h * u - 1
            for i in range(h + 1):
                require(even == 2**(h-i) * u, "even prefix")
                require(odd == 3**i * 2**(h-i) * u - 1, "odd prefix")
                require(min(even, odd) > floor, "finite floor guard")
                even, odd = step(even), step(odd)
                floor_checks += 1

    eigen_checks = 0
    for alpha in (-2, -1, 0, 1, 2):
        lam = Fraction(2)**(-alpha) / 4
        for ell in (0, 1, 7, 10**6):
            a, b, target = 72*ell+10, 24*ell+3, 36*ell+5
            require(step(a) == step(b) == target, "collision pair")
            for length in (1, 2, 8, 32, 80):
                f = {}
                for j in range(length):
                    f[2**j*a] = lam**j
                    f[2**j*b] = -lam**j
                residual = minus_multiple(push(f), f, lam)
                expected = {
                    2**(length-1)*a: -lam**length,
                    2**(length-1)*b: lam**length,
                }
                require(residual == expected, "truncated eigenvector boundary")
                tail = lam**length * (Fraction(2**(length-1)*a)**alpha +
                                      Fraction(2**(length-1)*b)**alpha)
                require(norm(residual, alpha) == tail, "weighted eigenvector residual")
                eigen_checks += 1

    # General words are checked at block boundaries, so their eigenvalue
    # (3^q/2^k)^alpha is rational. The written one-step circle argument also
    # allows complex roots and is not claimed as an arithmetic enumeration.
    singular_checks = 0
    largest_bits = 0
    max_normalized_boundary = Fraction(0)
    words = [(0,), (1,), (0, 1), (1, 0, 1), (0, 0, 1, 1, 1),
             (1, 1, 0, 1, 0, 0, 1, 1)]
    for word in words:
        k, q = len(word), sum(word)
        for blocks in (1, 2, 8, 32, 64):
            full_word = word * blocks
            residue, _, _ = cylinder(full_word)
            horizon = len(full_word)
            source = residue + 2**horizon * 2**(horizon+100)
            largest_bits = max(largest_bits, source.bit_length())
            states = [source]
            x = source
            for bit in full_word:
                require(x % 2 == bit, "repeated physical word")
                require(x > 2**64, "singular-sequence floor")
                x = step(x)
                physical_steps += 1
            require(x > 2**64, "last floor")
            states = [run(source, k*j) for j in range(blocks+1)]
            require(len(set(states)) == len(states), "distinct block states")
            for alpha in (0, 1, 2):
                lam = Fraction(3**q, 2**k)**alpha
                g = {states[j]: lam**(-j) for j in range(blocks)}
                residual = minus_multiple(push(g, k, 2**64), g, lam)
                expected = {states[-1]: lam**(1-blocks), states[0]: -lam}
                require(residual == expected, "block boundary identity")
                normalized = blocks * norm(residual, alpha) / (lam * norm(g, alpha))
                require(normalized <= 3, "finite O(1/N) residual")
                max_normalized_boundary = max(max_normalized_boundary, normalized)
                singular_checks += 1

    print(json.dumps({
        "status": "PASS",
        "scope": "Exact finite parity cylinders, floor guards, truncated eigenvectors and rational block singular-sequence residuals; no infinite spectral theorem is certified by enumeration.",
        "cylinder_instances": cylinder_count,
        "floor_prefix_instances": floor_checks,
        "truncated_eigenvector_instances": eigen_checks,
        "block_singular_vector_instances": singular_checks,
        "physical_steps_checked": physical_steps,
        "largest_source_bits": largest_bits,
        "maximum_scaled_boundary_ratio": str(max_normalized_boundary),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
