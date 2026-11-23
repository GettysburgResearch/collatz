#!/usr/bin/env python3
"""Exact coefficient/offset guards; does not reverify old ordinary templates."""
from fractions import Fraction
import json

ROWS = [
    ('-197/243', 7, 5, -69, 48, 292863),
    ('-29/27', 9, 6, -271, 674, 774143),
    ('-755/729', 9, 6, -243, 486, 980991),
    ('-1039/729', 11, 7, -1069, 779, 761855),
    ('-3125/2187', 11, 7, -1077, 480, 4052991),
    ('-3101/2187', 11, 7, -1053, 1377, 3137535),
    ('-3011/2187', 11, 7, -963, 2007, 3063807),
    ('-1603/2187', 10, 7, -579, 2100, 3223551),
]

OLD_SOURCE = [2, 2, 2, 1, 2, 4]
OLD_TARGET = [2, 2, 3, 1]
NEW_WORDS = {
    '-197/243': ([2,2,2,1,1,2,2,1,2,4,5], [2,2,4,2,1,1,2,1,2]),
    '-29/27': ([2,2,2,1,1,2,2,2,1,2,4,5], [2,2,4,2,1,2,1,2,1,2]),
    '-755/729': ([2,2,2,1,1,1,2,1,1,3,3,7], [2,2,5,1,1,1,1,1,3,2]),
    '-1039/729': ([2,2,2,1,1,2,2,2,2,1,2,4,5], [2,2,4,2,1,2,2,1,2,1,2]),
    '-3125/2187': ([2,2,2,1,1,3,1,2,2,1,2,4,5], [2,2,4,1,1,4,1,1,2,1,2]),
    '-3101/2187': ([2,2,2,1,1,2,1,1,4,1,2,4,5], [2,2,4,3,1,1,1,1,1,3,2]),
    '-3011/2187': ([2,2,2,1,2,1,1,2,1,1,3,3,7], [2,2,3,1,1,5,1,1,2,1,2]),
    '-1603/2187': ([2,2,2,1,2,1,1,2,2,1,2,4,5], [2,2,3,1,1,4,1,1,2,1,2]),
}


def require(value, message):
    if not value:
        raise ValueError(message)


def rational(value):
    return {'numerator': value.numerator, 'denominator': value.denominator}


def prefix_bounds(slope, offset, word):
    """Affine identities in h>=1; ordinary legality stays a source dependency."""
    slope, offset = Fraction(slope), Fraction(offset)
    lower = []
    for a in word:
        require(slope > 0 and slope+offset > 1, 'a prefix can reach the one-cycle')
        lower.append(slope+offset)
        slope, offset = 3*slope/2**a, (3*offset+1)/2**a
    require(slope > 0 and slope+offset > 1, 'retained endpoint permits an empty tail')
    lower.append(slope+offset)
    return slope, offset, min(lower)


def main():
    out = []
    for reference, a, b, c, rho, initial in ROWS:
        factor = Fraction(402**a, 200**a * 3**b)
        binary_margin = 2**a - 3**b - 64*c
        psi_margin = 2**a - 3**b - 27*c
        require(factor < 1, 'coefficient guard fails')
        require(binary_margin > 0, 'binary offset guard fails')
        require(psi_margin > 0, 'psi offset guard fails')
        require(initial % 2048 == 2047, 'initial binary class mismatch')
        require(initial % 3**b == rho, 'initial ternary class mismatch')
        numerator = 2**a*initial+c
        require(numerator % 3**b == 0, 'initial child not integral')
        child = numerator // 3**b
        require(0 < child < initial, 'initial child outside strict parameter descent')
        old_binary, new_binary = 128*initial+1, 128*child+1
        old_psi, new_psi = 81*initial+2, 81*child+2
        require(3**b*(new_binary+1) == 2**a*(old_binary+1)-2*binary_margin,
                'binary source affine identity mismatch')
        require(3**b*(new_psi+1) == 2**a*(old_psi+1)-3*psi_margin,
                'psi source affine identity mismatch')
        binary_ratio = Fraction((new_binary+1)*201**a, (old_binary+1)*200**a)
        psi_ratio = Fraction((new_psi+1)*201**a, (old_psi+1)*200**a)
        require(binary_ratio < factor and psi_ratio < factor,
                'exact initial-source ratio does not improve the universal coefficient')
        source_new, target_new = NEW_WORDS[reference]
        # M=2048h-1 and M'=(2^aM+c)/3^b, for every h>=1 satisfying old guards.
        source_old_affine = prefix_bounds(128*2048, -127, OLD_SOURCE)
        target_old_affine = prefix_bounds(64*2048, -63, OLD_TARGET)
        source_new_affine = prefix_bounds(Fraction(128*2**a*2048, 3**b),
            Fraction(128*(c-2**a), 3**b)+1, source_new)
        target_new_affine = prefix_bounds(Fraction(64*2**a*2048, 3**b),
            Fraction(64*(c-2**a), 3**b)+1, target_new)
        require(source_old_affine[:2] == (23328,-11), 'old source endpoint identity')
        require(source_new_affine[:2] == (1458,-1), 'new source endpoint identity')
        require(target_old_affine[:2] == (41472,-19), 'old target endpoint identity')
        require(target_new_affine[:2] == (10368,-5), 'new target endpoint identity')
        require(sum(source_new)-sum(OLD_SOURCE)-4 == a, 'source net clock increment')
        require(sum(target_new)-sum(OLD_TARGET)-2 == a, 'target net clock increment')
        require(len(source_new)-len(OLD_SOURCE) == b, 'source odd-count increment')
        require(len(target_new)-len(OLD_TARGET) == b, 'target odd-count increment')
        out.append({
            'reference': reference, 'a': a, 'b': b, 'c': c, 'rho': rho,
            'coefficient_ratio': rational(factor),
            'coefficient_guard_margin': 200**a*3**b-402**a,
            'binary_offset_margin': binary_margin,
            'psi_offset_margin': psi_margin,
            'first_parameter': initial, 'first_child_parameter': child,
            'first_binary_source_rank_ratio': rational(binary_ratio),
            'first_psi_source_rank_ratio': rational(psi_ratio),
            'retained_words': {'source_old': OLD_SOURCE, 'source_new': source_new,
                               'target_old': OLD_TARGET, 'target_new': target_new},
            'prefix_lower_bounds_for_all_h_ge_one': {
                'source_old': rational(source_old_affine[2]),
                'source_new': rational(source_new_affine[2]),
                'target_old': rational(target_old_affine[2]),
                'target_new': rational(target_new_affine[2]),
            },
            'source_clock_increment_without_padding': a,
        })
    expanding = Fraction(21092*200**30, 19484*201**30)
    require(expanding < 1, 'expanding balanced return does not pass rank guard')
    print(json.dumps({
        'status': 'PASS',
        'scope': 'Exact common-rank coefficient, affine-offset, all-h prefix lower-bound, '
                 'and no-padding clock checks; old ordinary template legality remains a pinned dependency.',
        'source': {
            'pr': 168, 'head': 'e4599b32e4b1a955ac9315d46782d4ad6a5db96c',
            'path': 'research/closure-frontier-20261121/NEGATIVE_TEMPLATE_GRAMMAR.md',
            'claims': ['NT2', 'NT3', 'Eight exact instances'],
        },
        'lambda': {'numerator': 201, 'denominator': 200},
        'symbolic_retained_endpoints_in_h': {
            'source_old': [23328, -11], 'source_new': [1458, -1],
            'target_old': [41472, -19], 'target_new': [10368, -5],
        },
        'rows': out,
        'expanding_return': {'source': 19483, 'endpoint': 21091, 'clock': 30,
                             'rank_ratio': rational(expanding),
                             'guard_margin': 19484*201**30-21092*200**30},
        'coverage': 'OPEN',
    }, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
