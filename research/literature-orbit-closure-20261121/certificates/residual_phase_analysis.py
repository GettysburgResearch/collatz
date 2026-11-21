"""Finite checks and examples for the variable-clock prefix family.

The unbounded family is proved by the Lean modules, not by these examples.
The eight-clock phase census below is a bounded exact computation.
"""
import json
from pathlib import Path

def orbit_count(n, clock):
    odd = 0
    for _ in range(clock):
        odd += n % 2
        n = (3 * n + 1) // 2 if n % 2 else n // 2
    return (n, odd)

def selector(k):
    return (6400 * pow(2, 53 * k + 1, 20736) + 14337 * 147 * pow(3, 63 * (k + 1), 20736)) % 20736

def family(k, t):
    w = selector(k) + 20736 * t
    u = 81 * w
    z = 9 * (2 ** k * w // 81)
    return (128 * z + 27, 2 ** (k - 3) * u - 1)

def main():
    phases = {}
    for r in range(1, 9):
        phases[r] = []
        for v in range(1, 256, 2):
            left, p = orbit_count(v - 1, 8)
            right, q = orbit_count(3 ** r * v - 1, 8)
            if left == right and p == q + r:
                phases[r].append(v)
    if not phases[1] == sorted(list(range(3, 256, 4)) + [185]):
        raise RuntimeError('Failed invariant: phases[1] == sorted(list(range(3, 256, 4)) + [185])')
    if not phases[2] == [147, 185]:
        raise RuntimeError('Failed invariant: phases[2] == [147, 185]')
    if not phases[3] == [147]:
        raise RuntimeError('Failed invariant: phases[3] == [147]')
    if not all((not phases[r] for r in range(4, 9))):
        raise RuntimeError('Failed invariant: all((not phases[r] for r in range(4, 9)))')
    half_examples = []
    for k in range(13):
        a = (28 * pow(2, 5 * k + 1, 36) + 9 * pow(3, k, 36)) % 36
        base = 128 * (2 ** k * a // 9) + 27
        for t in (0, 1, 2):
            w = a + 36 * t
            n = 128 * (2 ** k * w // 9) + 27
            x = 2 ** (k + 3) * w - 1
            if not n == base + 2 ** (k + 9) * t:
                raise RuntimeError('Failed invariant: n == base + 2 ** (k + 9) * t')
            if not (n % 128 == 27 and 0 < x < n):
                raise RuntimeError('Failed invariant: n % 128 == 27 and 0 < x < n')
            if not 16 * x + 3 == 9 * n:
                raise RuntimeError('Failed invariant: 16 * x + 3 == 9 * n')
            if not orbit_count(x, k + 5)[0] == orbit_count(n, k + 9)[0]:
                raise RuntimeError('Failed invariant: orbit_count(x, k + 5)[0] == orbit_count(n, k + 9)[0]')
            if not all((orbit_count(n, i)[0] >= n for i in range(k + 10))):
                raise RuntimeError('Failed invariant: all((orbit_count(n, i)[0] >= n for i in range(k + 10)))')
        half_examples.append(dict(k=k, source=base, partner=2 ** (k + 3) * a - 1, source_clock=k + 9, partner_clock=k + 5))
    examples = []
    for k in range(6, 15):
        n0, x0 = family(k, 0)
        modulus = 73728 * 2 ** (k + 2)
        if not 0 < n0 < modulus:
            raise RuntimeError('Failed invariant: 0 < n0 < modulus')
        for t in (0, 1, 2):
            n, x = family(k, t)
            if not 0 < x < n:
                raise RuntimeError('Failed invariant: 0 < x < n')
            if not n == n0 + modulus * t:
                raise RuntimeError('Failed invariant: n == n0 + modulus * t')
            if not n % 73728 == 34587:
                raise RuntimeError('Failed invariant: n % 73728 == 34587')
            if not 1024 * x == 729 * n + 29:
                raise RuntimeError('Failed invariant: 1024 * x == 729 * n + 29')
            if not orbit_count(x, k + 5)[0] == orbit_count(n, k + 15)[0]:
                raise RuntimeError('Failed invariant: orbit_count(x, k + 5)[0] == orbit_count(n, k + 15)[0]')
            if not all((orbit_count(n, i)[0] >= n for i in range(k + 8))):
                raise RuntimeError('Failed invariant: all((orbit_count(n, i)[0] >= n for i in range(k + 8)))')
            value = orbit_count(n, 7)[0] + 1
            if not value & -value == 2 ** k:
                raise RuntimeError('Failed invariant: value & -value == 2 ** k')
            w = selector(k) + 20736 * t
            smaller = 2 ** (k + 1) * w - 1
            if not 64 * smaller + 51 == 9 * n:
                raise RuntimeError('Failed invariant: 64 * smaller + 51 == 9 * n')
            if not orbit_count(smaller, k + 9)[0] == orbit_count(n, k + 15)[0]:
                raise RuntimeError('Failed invariant: orbit_count(smaller, k + 9)[0] == orbit_count(n, k + 15)[0]')
            if k >= 8:
                if not all((orbit_count(n, i)[0] >= n for i in range(k + 16))):
                    raise RuntimeError('Failed invariant: all((orbit_count(n, i)[0] >= n for i in range(k + 16)))')
        examples.append(dict(k=k, w=selector(k), source=n0, partner=x0, source_clock=k + 15, partner_clock=k + 5, source_increment=modulus))
    certificate = Path(__file__).with_name('al27_certificate.json')
    if certificate.exists():
        if not 34587 in json.loads(certificate.read_text())['unresolved']:
            raise RuntimeError("Failed invariant: 34587 in json.loads(certificate.read_text())['unresolved']")
    print(json.dumps(dict(status='PASS', bounded_phase_census=phases, examples=examples, half_examples=half_examples, scope='Finite examples; unbounded family is proved in Lean.'), indent=2))
if __name__ == '__main__':
    main()
