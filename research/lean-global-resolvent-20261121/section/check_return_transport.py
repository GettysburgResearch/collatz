#!/usr/bin/env python3
"""Exact integer witness for source/endpoint fourth-power weight distortion.

The finite check below does not assume Collatz.  It checks one initial segment
ending at the first positive marked return.  Large endpoints are reported by
exact formulas rather than by thousands of decimal digits.
"""
import json


def marked(n: int) -> bool:
    if n <= 0 or n % 2 == 0:
        return False
    d = n.bit_length() - 1
    return (d + 1) * (n - (1 << d)) <= 70 * (1 << d)


def shortcut(n: int) -> int:
    return (3*n + 1)//2 if n % 2 else n//2


def main() -> None:
    d, m = 8192, 13
    n = (1 << (d - m)) * (d + 8) - 1
    assert marked(n)
    x = n
    for j in range(1, 54):
        assert x % 2 == 1
        x = shortcut(x)
        assert x == 3**j * (1 << (d - m - j)) * (d + 8) - 1
        assert marked(x) == (j == 53)
    assert x > (1 << 31) * n
    # Cross multiplication checks n^-4 > 2^124 x^-4 exactly.
    assert x**4 > (1 << 124) * n**4
    print(json.dumps({
        "source": "2^8179 * 8200 - 1",
        "first_positive_return_clock": 53,
        "endpoint": "3^53 * 2^8126 * 8200 - 1",
        "source_and_endpoint_marked": True,
        "earlier_positive_clocks_marked": False,
        "endpoint_over_source_exceeds": "2^31",
        "transported_atom_over_endpoint_fourth_power_weight_exceeds": "2^124",
        "ordinary_source_convergence_assumed": False,
        "verification": "exact Python integers; independent finite computation"
    }, indent=2))


if __name__ == '__main__':
    main()
