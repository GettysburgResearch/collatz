"""Check three squarefree products and all their prime and trajectory certificates."""
import json
from math import isqrt, prod


def trace(value):
    path = [value]
    for _ in range(200):
        if path[-1] == 1:
            return path
        n = path[-1]
        path.append((3 * n + 1) // 2 if n % 2 else n // 2)
    raise ValueError(f"certificate exhausted at {value}")


def check_row(primes, target, expected_opposite_step, expected_one):
    if len(set(primes)) != len(primes):
        raise ValueError("repeated prime factor")
    factors = []
    for p in primes:
        if p < 2 or any(p % d == 0 for d in range(2, isqrt(p) + 1)):
            raise ValueError(f"composite factor {p}")
        path = trace(p)
        deadline = 5 * p.bit_length()
        if target not in path or len(path) - 1 > deadline:
            raise ValueError(f"factor {p} lacks the required certificate")
        factors.append(dict(prime=p, first_target=path.index(target),
                            first_one=len(path) - 1, deadline=deadline))
    n = prod(primes)
    path = trace(n)
    opposite = 85 if target == 5 else 5
    if target in path or path.index(opposite) != expected_opposite_step:
        raise ValueError(f"incorrect product entrance for {n}")
    if len(path) - 1 != expected_one:
        raise ValueError(f"incorrect first arrival for {n}")
    return dict(product=n, factors=factors, factor_target=target,
                product_target=opposite, first_product_target=expected_opposite_step,
                product_first_one=expected_one, product_deadline=5 * n.bit_length())


if __name__ == "__main__":
    rows = [
        check_row([5, 17], 5, 0, 8),
        check_row([3, 12_163], 5, 88, 96),
        check_row([113, 401], 85, 56, 60),
    ]
    print(json.dumps(rows, indent=2))
