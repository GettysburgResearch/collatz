#!/usr/bin/env python3
"""Exact sample legality and finite congruence branches; no uniform-J proof."""
from __future__ import annotations
import argparse
import copy
import hashlib
import json
from pathlib import Path

RAW_SEARCH_SHA256 = '83fa609bc05e22f54e01a7fe2bc2bf872986254d4f2cd842e80acee7612edcdd'


def need(ok, message):
    if not ok:
        raise ValueError(message)


def integer(x):
    return type(x) is int


def positive_form(row):
    need(isinstance(row, list) and len(row) == 2, 'two affine coefficients')
    need(all(integer(x) and x > 0 for x in row), 'positive integer affine coefficients')
    return row[0], row[1]


def verify_sample(data):
    need(data['assumed_high_level'] == 8, 'frozen high level')
    need(data['raw_search_report_sha256'] == RAW_SEARCH_SHA256,
         'recorded exploratory source identity')
    path = data['certificate']['path']
    need(isinstance(path, list) and len(path) == 44, '43-move frozen sample')
    need(path[0] == [[10368, 3823], None], 'frozen initial form')
    forward = reverse = high_forward = high_reverse = 0
    divisions = {2: 0, 3: 0}
    for index, (next_row, op) in enumerate(path[1:], 1):
        a, b = positive_form(path[index-1][0])
        need(isinstance(op, list) and len(op) == 2, 'operation shape')
        kind, exponent = op
        need(integer(exponent) and exponent >= 1, 'positive integer exponent')
        if kind == 'forward':
            need(a % 2 == 0 and b % 2 == 1, 'whole-class odd forward input')
            if exponent == 1:
                need(a % 3 == 0 and b % 3 != 0, 'whole-class ternary-unit low law')
            else:
                need(exponent >= 8, 'available high law')
                high_forward += 1
            a, b = 3**exponent*a, 3**exponent*b+1
            forward += 1
        elif kind == 'reverse':
            a, b = 2**exponent*a, 2**exponent*b-1
            exact_one = a % 9 == 0 and b % 3 == 0 and b % 9 != 0
            high = a % (3**8) == 0 and b % (3**8) == 0
            need(exact_one or high, 'whole-class reverse ternary valuation')
            high_reverse += int(high)
            reverse += 1
        else:
            raise ValueError('unknown operation')
        need(a > 0 and b > 0, 'positive raw affine form on all t>=0')
        for prime in (2, 3):
            while a % prime == 0 and b % prime == 0:
                a //= prime
                b //= prime
                divisions[prime] += 1
        need([a, b] == list(positive_form(next_row)), 'exact normalized affine endpoint')
    need(path[-1][0] == [648, 239], 'frozen final form')
    need(16*648 == 10368 and 16*239 == 3823+1, 'endpoint is (n+1)/16')
    need(10368-648 > 0 and 3823-239 > 0, 'strict descent for every t>=0')
    return dict(moves=43, forward_moves=forward, reverse_moves=reverse,
                high_forward_moves=high_forward, high_reverse_moves=high_reverse,
                removed_factors=divisions, source=[10368,3823], endpoint=[648,239],
                strict_descent_for_all_nonnegative_parameters=True)


def pure_three(value):
    exponent = 0
    while value > 0 and value % 3 == 0:
        exponent += 1
        value //= 3
    return exponent if value == 1 else None


def check_small_inverse_obstructions():
    need([v for v in range(1,5,2) if v%3] == [1], 'complete core list below5')
    need([v for v in range(1,7,2) if v%3] == [1,5], 'complete core list below7')
    # Multiplication by3 modulo8 has exact period2, so these are every power.
    powers8 = [pow(3,j,8) for j in range(2)]
    need(powers8 == [1,3] and pow(3,2,8) == 1, 'complete powers of3 mod8')
    need(7 not in powers8, 'v=1 excludes every a>=3 for either source')
    small = {}
    for n in (5,7):
        solutions=[]
        for a in (1,2):
            h=pure_three(n*2**a-1)
            if h is not None and h>=1:
                solutions.append([a,h,1])
        small[n]=solutions
    need(small[5] == [[1,2,1]], 'complete source5 solutions')
    need(small[7] == [[2,3,1]], 'source7 core1 solutions')
    # For core5 at source7, mod7 forces h=4 mod6, hence h even.
    residues=[pow(3,h,7) for h in range(6)]
    need(len(set(residues)) == 6 and pow(3,6,7) == 1, 'exact period6 mod7')
    eligible=[h for h in range(6) if (5*residues[h]+1)%7 == 0]
    need(eligible == [4], 'core5 forces even h')
    need((5*pow(3,0,8)+1)%8 == 6, 'even h contradicts a>=3 mod8')
    need(all((7*2**a-1)%5 != 0 for a in (1,2)), 'core5 excludes a=1,2')
    return {'source5_all_solutions_a_h_core':small[5],
            'source7_all_solutions_a_h_core':small[7],
            'unbounded_a_branches':'excluded by complete residue periods, not a finite exponent search'}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--sample',type=Path,default=Path(__file__).with_name('level8-sample-verification.json'))
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    data=json.loads(args.sample.read_text(encoding='utf-8'))
    sample=verify_sample(data)
    rejected=[]
    for kind in ('intermediate_form','endpoint','zero_exponent'):
        bad=copy.deepcopy(data)
        if kind=='intermediate_form':bad['certificate']['path'][1][0][1]+=2
        elif kind=='endpoint':bad['certificate']['path'][-1][0][1]+=1
        else:bad['certificate']['path'][1][1][1]=0
        try:
            verify_sample(bad)
        except (ValueError,TypeError):
            rejected.append(kind)
        else:
            raise ValueError('damaged sample unexpectedly accepted: '+kind)
    report={'status':'PASS',
      'scope':'exact whole-affine sample and exhaustive congruence branches for n=5,7; no universal-J, S-unit implementation, or exhaustive ancestor search',
      'sample':sample,'inverse_obstructions':check_small_inverse_obstructions(),
      'damaged_samples_rejected':rejected,
      'sample_sha256':hashlib.sha256(args.sample.read_bytes()).hexdigest(),
      'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'recorded_raw_search_sha256':RAW_SEARCH_SHA256,
      'raw_search_provenance_scope':'recorded hash from the exploratory run; the large raw report is not reread by this verifier'}
    raw=json.dumps(report,indent=2,sort_keys=True)+'\n'
    if args.output:args.output.write_text(raw,encoding='utf-8')
    print(raw,end='')


if __name__=='__main__':main()
