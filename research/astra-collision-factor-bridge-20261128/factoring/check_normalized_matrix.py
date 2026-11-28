#!/usr/bin/env python3
"""Independent exact checks of the general normalized residue/moment matrix.

This consumer reconstructs word carries from native shortcut iteration on
complete binary cylinders. It does not import primary_cartier_profile.py.
The finite checks are not a proof of the asymptotic or complexity claims.
"""
from __future__ import annotations
import argparse
from collections import defaultdict
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
import json
from math import comb
from pathlib import Path


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def native_cylinder(h: int):
    records = []
    for n in range(2 ** h):
        v, a, tape = n, 0, []
        for _ in range(h):
            odd = v % 2
            tape.append(odd)
            a += odd
            v = (3 * v + 1) // 2 if odd else v // 2
        carry = 2 ** h * v - 3 ** a * n
        require(carry >= 0, 'Negative word carry')
        records.append((a, carry, tuple(tape)))
    require(len({t for _, _, t in records}) == 2 ** h,
            'Native binary cylinder words are not distinct')
    require(len({(a, carry) for a, carry, _ in records}) == 2 ** h,
            'Equal-grade carries are not distinct')
    return records


def advance(state, modulus: int, degree: int):
    out = defaultdict(int)
    inv2 = pow(2, -1, modulus)
    for (a, s, j), value in state.items():
        even_r = s * inv2 % modulus
        out[a, even_r, j] += 2 ** (degree - j) * value
        odd_r = (3 * s + 1) * inv2 % modulus
        for p in range(j, degree + 1):
            out[a + 1, odd_r, p] += 2 ** (degree - p) * comb(p, j) * 3 ** j * value
    return {key: value for key, value in out.items() if value}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    census = {h: native_cylinder(h) for h in range(9)}
    matrix_cases = native_checks = 0
    rows = []
    for k in [1, 2, 3]:
        modulus = 3 ** k
        for degree in range(4):
            state = {(0, 0, 0): 1}
            for h in range(9):
                direct = defaultdict(int)
                for a, carry, _ in census[h]:
                    r = carry * pow(pow(2, h, modulus), -1, modulus) % modulus
                    for p in range(degree + 1):
                        direct[a, r, p] += 2 ** ((degree - p) * h) * carry ** p
                    native_checks += 1
                direct = {key: value for key, value in direct.items() if value}
                require(state == direct, f'Matrix differs: k={k}, d={degree}, h={h}')
                matrix_cases += 1
                if h == 8:
                    encoded = json.dumps(sorted((list(key), value) for key, value in direct.items()))
                    rows.append({'k': k, 'd': degree, 'h': h,
                                 'nonzero_entries': len(direct),
                                 'entries_sha256': hashlib.sha256(encoded.encode()).hexdigest()})
                state = advance(state, modulus, degree)
    fibre_terms = lattice_checks = cutoff_checks = 0
    for h, records in census.items():
        for y in range(1, 31):
            for a in range(h + 1):
                modulus = 3 ** a
                delta = Fraction(modulus, 2 ** h)
                points = []
                for grade, carry, tape in records:
                    if grade != a or (2 ** h * y - carry) % modulus:
                        continue
                    n = (2 ** h * y - carry) // modulus
                    require(n > 0, 'Full positive endpoint fibre contains nonpositive input')
                    v, actual_tape = n, []
                    for _ in range(h):
                        odd = v % 2
                        actual_tape.append(odd)
                        v = (3 * v + 1) // 2 if odd else v // 2
                    require(v == y and tuple(actual_tape) == tape,
                            'Full-conductor congruence does not realize the native word')
                    point = Fraction(carry, 2 ** h)
                    require(0 <= point < y and (y - point) / delta == n,
                            'Compact support/lattice identity fails')
                    points.append(point)
                    fibre_terms += 1
                require(len(points) == len(set(points)), 'Fibre multiplicity exceeds one')
                points.sort()
                for left, right in zip(points, points[1:]):
                    require(right - left >= delta, 'Fibre spacing below the exact mesh')
                    lattice_checks += 1
                for maximum in [1, 7, 64]:
                    length = delta * maximum
                    count = sum(y - length <= point < y for point in points)
                    direct = 0
                    for n in range(1, maximum + 1):
                        v, grade = n, 0
                        for _ in range(h):
                            odd = v % 2
                            grade += odd
                            v = (3 * v + 1) // 2 if odd else v // 2
                        direct += v == y and grade == a
                    require(count == direct, 'Full real-window count differs from native input census')
                    if length >= y:
                        require(count == len(points), 'Automatic full-window case fails')
                    cutoff_checks += 1
    report = {
        'schema': 'collatz-normalized-matrix-independent-check/v1',
        'success': True,
        'recorded_utc': datetime.now(timezone.utc).isoformat(),
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'matrix_cases': matrix_cases,
        'native_cylinder_checks': native_checks,
        'full_fibre_terms_checked': fibre_terms,
        'successive_lattice_spacings_checked': lattice_checks,
        'ordinary_window_comparisons': cutoff_checks,
        'rows': rows,
        'scope': 'Exact finite checks for k=1..3, moments0..3, clocks0..8; full-conductor positive endpoint/lattice/window checks for y=1..30 and X=1,7,64. No approximation, convergence or asymptotic complexity claim.'
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({key: report[key] for key in ['success', 'matrix_cases', 'native_cylinder_checks', 'full_fibre_terms_checked', 'ordinary_window_comparisons']}))


if __name__ == '__main__':
    main()
