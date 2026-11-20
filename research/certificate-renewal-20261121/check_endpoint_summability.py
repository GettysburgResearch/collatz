#!/usr/bin/env python3
"""Bounded exact replay for ES1; all-time proof is in the adjacent note."""
from fractions import Fraction
import hashlib
import json
from pathlib import Path


def require(ok, message):
    if not ok:
        raise ValueError(message)


def v2(n):
    require(n > 0, 'positive input')
    return (n & -n).bit_length()-1


def main():
    targets = (1, 3, 5, 7, 9, 13, 27)
    totals = {t: Fraction(0) for t in targets}
    checks = 0
    first_hit_checks = 0
    exact_trivial_cycle_checks = 0
    telescoping_checks = 0
    sharp_factor_checks = 0
    total_fifth_mass = Fraction(0)
    cubic = [175, 2019, 8397, 13473]
    product_coefficients = [0]*5
    for i, a in enumerate([-1, 1]):
        for j, b in enumerate(cubic):
            product_coefficients[i+j] += a*b
    require(product_coefficients == [-175, -1844, -6378, -5076, 13473],
            'universal sharp-factor polynomial identity')
    require(all(a > 0 for a in cubic), 'positive quotient polynomial coefficients')
    for source in range(1, 512, 2):
        n = source
        J = Fraction(1)
        contributions = {t: Fraction(0) for t in targets}
        first = {}
        fifth_mass = Fraction(0)
        for q in range(65):
            if n in contributions:
                term = J**4 / n**2
                contributions[n] += term
                if n not in first:
                    first[n] = (q, J)
                    require(term <= Fraction(n**2, source**4), 'first-hit bound')
                    first_hit_checks += 1
            V = J**4 / n**4
            delta = 1-Fraction(3*n, 3*n+1)**4
            require(delta >= Fraction(175, 256*n), 'sharp elementary lower factor')
            fifth_mass += J**4 / n**5
            sharp_factor_checks += 1
            a = v2(3*n+1)
            J *= Fraction(3, 2**a)
            next_n = (3*n+1) >> a
            next_V = J**4 / next_n**4
            require(V-next_V == V*delta, 'exact weighted telescoping')
            telescoping_checks += 1
            n = next_n
        require(fifth_mass <= Fraction(256,175)*(Fraction(1,source**4)-J**4/n**4),
                'finite fifth-power Green bound with exact remainder')
        total_fifth_mass += fifth_mass
        for t in targets:
            ratio = Fraction(3*t, 3*t+1)**4
            bound = Fraction(t**2, source**4) / (1-ratio)
            require(contributions[t] <= bound, 'finite per-source all-time envelope')
            totals[t] += contributions[t]
            checks += 1
        if 1 in first:
            q0, J0 = first[1]
            exact_all_time = J0**4 / (1-Fraction(3,4)**4)
            remaining = J0**4 * Fraction(3,4)**(4*(65-q0)) / (1-Fraction(3,4)**4)
            require(contributions[1]+remaining == exact_all_time, 'exact trivial-cycle tail')
            exact_trivial_cycle_checks += 1
    for t, total in totals.items():
        require(total < 2*t*t*(3*t+1), 'all-source rational envelope diagnostic')
    require(Fraction(1, 1)/(1-Fraction(3,4)**4) == Fraction(256,175), 'source-one infinite sum')
    report = {
        'status': 'PASS',
        'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'scope': '65-step exact diagnostics on 256 odd sources; exact terminal geometric tails, weighted telescoping, and a universal polynomial factor identity; no asymptotic original-moment bound.',
        'targets': list(targets),
        'per_source_target_envelope_checks': checks,
        'first_hit_checks': first_hit_checks,
        'exact_trivial_cycle_tail_checks': exact_trivial_cycle_checks,
        'source_one_exact_all_time_mass': '256/175',
        'weighted_telescoping_checks': telescoping_checks,
        'sharp_factor_checks': sharp_factor_checks,
        'universal_sharp_factor_polynomial_coefficients': product_coefficients,
        'finite_all_source_fifth_power_mass': str(total_fifth_mass),
        'finite_endpoint_masses': {str(t): str(v) for t,v in totals.items()},
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
