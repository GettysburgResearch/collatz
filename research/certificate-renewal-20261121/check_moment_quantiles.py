#!/usr/bin/env python3
"""Exact finite checks for MOMENT_QUANTILES.md; no asymptotic claim."""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from math import isqrt
from fractions import Fraction
from pathlib import Path


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def valuation2(n: int) -> int:
    require(n > 0, 'valuation input must be positive')
    return (n & -n).bit_length() - 1


def word_data(word: tuple[int, ...]) -> tuple[int, int, int, int]:
    require(bool(word) and all(isinstance(a, int) and a > 0 for a in word), 'positive word required')
    q = len(word)
    power3 = 3**q
    total = 0
    constant = 0
    for a in word:
        constant = 3 * constant + 2**total
        total += a
    residue = (constant * pow(2, -total, power3)) % power3
    if residue % 2 == 0:
        residue += power3
    source = (2**total * residue - constant) // power3
    return total, constant, residue, source


def check_word(word: tuple[int, ...], residue: int, source: int) -> None:
    total, constant, _, _ = word_data(word)
    q = len(word)
    require(0 < residue < 2 * 3**q and residue % 2 == 1, 'representative range/parity')
    require(0 < source < 2**(total + 1) and source % 2 == 1, 'source range/parity')
    require(3**q * source + constant == 2**total * residue, 'full word identity')
    n = source
    for a in word:
        require(valuation2(3*n + 1) == a, 'exact valuation')
        n = (3*n + 1) >> a
        require(n > 0 and n % 2 == 1, 'positive intermediate odd state')
    require(n == residue, 'endpoint')


def truncated_vector(qmax: int, cutoff: int):
    """All a_i<=cutoff, using the denominator 16^(cutoff*q)."""
    previous = [1]
    previous_modulus = 1
    denominator = 1
    base = 16**cutoff
    for q in range(1, qmax + 1):
        modulus = 3 * previous_modulus
        current = []
        coefficients = [(a, 81 * 16**(cutoff-a), 2**a) for a in range(1, cutoff+1)]
        for t in range(1, 2*modulus, 2):
            value = 0
            if t % 3:
                for a, coefficient, power2 in coefficients:
                    if (power2*t-1) % 3:
                        continue
                    u = ((power2*t-1)//3) % previous_modulus
                    if u % 2 == 0:
                        u += previous_modulus
                    value += coefficient * previous[(u-1)//2]
            current.append(value)
        denominator *= base
        yield q, current, denominator
        previous = current
        previous_modulus = modulus


def interval_decimal(n: Fraction, places: int = 12, upper: bool = False) -> str:
    scale = 10**places
    k = (n.numerator * scale) // n.denominator
    if upper and n.numerator * scale != k * n.denominator:
        k += 1
    return f'{k//scale}.{k%scale:0{places}d}'


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--max-q', type=int, default=12)
    parser.add_argument('--cutoff', type=int, default=12)
    args = parser.parse_args()
    require(1 <= args.max_q <= 12, 'bounded replay range')
    require(4 <= args.cutoff <= 16, 'bounded exponent cutoff')

    word_checks = 0
    cylinder_checks = 0
    finite_word_identity = Fraction(0)
    finite_source_identity = Fraction(0)
    for q in range(1, 5):
        seen_sources = set()
        for word in itertools.product(range(1, 6), repeat=q):
            total, constant, residue, source = word_data(word)
            check_word(word, residue, source)
            word_checks += 1
            weight = Fraction(3**(4*q), 2**(4*total))
            for k in range(4):
                n = source + 2**(total+1)*k
                require(n not in seen_sources, 'two distinct words share a source')
                seen_sources.add(n)
                endpoint = n
                for a in word:
                    require(valuation2(3*endpoint+1) == a, 'cylinder valuation')
                    endpoint = (3*endpoint+1) >> a
                expected = residue + 2*3**q*k
                require(endpoint == expected, 'whole affine cylinder endpoint')
                finite_word_identity += weight / expected**2
                finite_source_identity += weight / endpoint**2
                cylinder_checks += 1
    require(finite_word_identity == finite_source_identity, 'finite grouped moment identity')

    damaged = 0
    w = (2, 2, 2)
    a, c, r, b = word_data(w)
    for word, residue, source in [(w, r+2, b), (w, r, b+2**(a+1)), ((3, 2, 2), r, b), ((0,), 1, 1)]:
        try:
            check_word(word, residue, source)
        except ValueError:
            damaged += 1
        else:
            raise ValueError('damaged word accepted')
    require(damaged == 4, 'mutation count')

    direct_vector_checks = 0
    for q, vector, denominator in truncated_vector(3, 4):
        direct = [0] * (3**q)
        for word in itertools.product(range(1, 5), repeat=q):
            total, constant, residue, source = word_data(word)
            direct[(residue-1)//2] += 3**(4*q) * 16**(4*q-total)
        require(vector == direct, 'recurrence differs from direct finite word grouping')
        require(sum(vector) == (81 * sum(16**(4-a) for a in range(1, 5)))**q,
                'complete truncated word mass')
        direct_vector_checks += len(vector)

    # The complete recurrence differs pointwise from the truncated recurrence
    # by at most delta_q=q*(27/5)^q*16^(-cutoff). This follows inductively
    # from positive row mass <=27/5, complete max H_(q-1)<=(27/5)^(q-1),
    # and omitted row mass <=(27/5)*16^(-cutoff).
    # Since sum_{t odd}t^(-2)<2, the complete P_q error is <2*delta_q.
    scale = 10**18
    intervals = []
    upper_by_q = {}
    for q, vector, denominator in truncated_vector(args.max_q, args.cutoff):
        floor_sum = sum((scale * numerator)//(denominator*(2*i+1)**2)
                        for i, numerator in enumerate(vector))
        lower = Fraction(floor_sum, scale)
        omitted_exponents = 2 * q * Fraction(27, 5)**q / 16**args.cutoff
        rounding = Fraction(len(vector), scale)
        upper = lower + rounding + omitted_exponents
        require(lower >= 0 and upper > lower, 'moment enclosure order')
        if q == 1:
            require(lower <= Fraction(1107, 2125) <= upper, 'exact q=1 full sum')
        upper_by_q[q] = upper + Fraction(1, 2)*Fraction(3, 5)**q
        intervals.append({
            'q': q,
            'P_lower_decimal': interval_decimal(lower),
            'P_upper_decimal': interval_decimal(upper, upper=True),
            'lower_scaled_floor_numerator': floor_sum,
            'lower_scale': scale,
            'rounding_allowance_numerator': len(vector),
            'rounding_allowance_denominator': scale,
            'omitted_exponents_allowance': str(omitted_exponents),
            'all_odd_endpoint_representatives': len(vector),
        })

    source_checks = 0
    simple_paths = 0
    rank_occupancy_checks = 0
    for source in range(1, 512, 2):
        n = source
        states = []
        seen = set()
        cumulative = 0
        product = Fraction(1)
        for q in range(1, args.max_q+1):
            if n in seen:
                break
            seen.add(n)
            states.append(n)
            product *= 1 + Fraction(1, 3*n)
            a = valuation2(3*n+1)
            cumulative += a
            n = (3*n+1) >> a
            jacobian = Fraction(3**q, 2**cumulative)
            require(Fraction(n) == source*jacobian*product, 'exact multiplicative correction')
            contribution = jacobian**4 / n**2
            require(contribution <= upper_by_q[q], 'fixed source exceeds certified Q enclosure')
            source_checks += 1
        simple_paths += 1
        for j, state in enumerate(sorted(states), 1):
            # Explicit source theorem: j<=10*state^(29/30).
            require(j**30 <= 10**30 * state**29, 'ranked finite occupancy check')
            rank_occupancy_checks += 1

    # Symbolic toy check: (j^2)^(10/19) raised to -19/40 is j^(-1/2).
    require(Fraction(2)*Fraction(10,19)*Fraction(-19,40) == Fraction(-1,2), 'toy square exponent')
    toy_rows = []
    for m in [4, 16, 64, 256, 1024]:
        lower = sum((Fraction(1, isqrt(j) + (isqrt(j)**2 != j))
                     for j in range(1, m+1)), Fraction(0))
        require(lower**2 >= m, 'sparse toy inverse-moment lower bound')
        nonsquare = m*m-1
        require(isqrt(nonsquare)**2 != nonsquare and 2**nonsquare > nonsquare**3,
                'sparse toy polynomial upper premise failure')
        toy_rows.append({'square_indices_count': m, 'time_horizon': m*m,
                         'inverse_moment_sum_rational_lower': str(lower),
                         'lower_squared_at_least_square_indices_count': True,
                         'nonsquare_index_with_exponential_value_above_q_cubed': nonsquare})

    report = {
        'status': 'PASS',
        'scope': 'Exact finite arithmetic identities and rigorous finite moment enclosures; no asymptotic or cycle-exclusion verification.',
        'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'word_representatives_replayed': word_checks,
        'source_cylinder_lifts_replayed': cylinder_checks,
        'damaged_inputs_rejected': damaged,
        'direct_grouping_vector_coordinates': direct_vector_checks,
        'fixed_source_moment_checks': source_checks,
        'finite_simple_odd_paths': simple_paths,
        'ranked_occupancy_checks': rank_occupancy_checks,
        'toy_sequence_finite_examples': toy_rows,
        'max_q': args.max_q,
        'exponent_cutoff': args.cutoff,
        'moment_enclosures': intervals,
        'closing_statements': {'BC': 'OPEN', 'NC': 'OPEN', 'QC': 'OPEN', 'PC': 'OPEN'},
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
