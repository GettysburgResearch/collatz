#!/usr/bin/env python3
"""Exact scoped controls for the one-rise rational-cycle Sidon theorem.

Finite checks do not establish the unbounded theorem or integer-cycle exclusion.
Failure checks are explicit, so normal and optimized Python agree.
"""
from __future__ import annotations

from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import combinations_with_replacement
import json
from math import gcd
from pathlib import Path


def need(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def v2(n: int) -> int:
    need(n > 0, 'valuation requires a positive integer')
    return (n & -n).bit_length() - 1


def integer_hash(n: int) -> str:
    need(n >= 0, 'hash requires a nonnegative integer')
    return sha256(n.to_bytes(max(1, (n.bit_length()+7)//8), 'big')).hexdigest()


def check_cycle(p: int, A: int, D: int, C: int, count_products: bool) -> dict:
    need(p >= 2 and A > p, 'word length domain')
    need(D == (1 << A) - 3**p and D > 0, 'full denominator')
    need(C == 3**p - (1 << p), 'complete carry')
    need(D % 2 == C % 2 == 1, 'odd numerator and denominator')
    h = (1 << (A-p)) - 1
    numerators = []
    n = C
    for i in range(p):
        need(n > 0 and n % 2 == 1, 'positive odd state')
        need(v2(n + D) == p-i, 'shifted valuation ladder')
        if numerators:
            need(n > numerators[-1], 'strict upward order')
        numerators.append(n)
        if i < p-1:
            need(v2(3*n+D) == 1, 'interior gap')
            n = (3*n+D)//2
        else:
            need(v2(3*n+D) == A-p+1, 'final exact gap')
            need((3*n+D) >> (A-p+1) == C, 'literal closing state')
    need(numerators[0] + D == (1 << p)*h, 'initial numerator formula')
    need(numerators[-1] + D == 2*3**(p-1)*h, 'last numerator formula')

    # The full shortcut trajectory is checked separately, retaining the same D.
    n = C
    shortcut_states = []
    for k in range(A):
        need((n % 2) == (1 if k < p else 0), 'literal shortcut word')
        need(n >= C, 'shortcut minimum')
        shortcut_states.append(n)
        n = (3*n+D)//2 if n % 2 else n//2
    need(n == C, 'shortcut closure')
    need(len(set(shortcut_states)) == A, 'primitive shortcut cycle')

    common = gcd(C, D)
    for n in numerators:
        need(gcd(n, D) == common, 'same complete reduced denominator')
    result = {
        'odd_period': p, 'shortcut_period': A,
        'denominator_bits': D.bit_length(),
        'carry_bits': C.bit_length(),
        'full_denominator_sha256': integer_hash(D),
        'complete_carry_sha256': integer_hash(C),
        'reduced_denominator_bits': (D//common).bit_length(),
        'integral': common == D,
        'all_literal_steps_checked': A,
        'valuation_ladder_states_checked': p,
        'minimum': str(Fraction(C,D)) if D.bit_length() <= 120 else 'retained exactly; large rational',
    }
    if count_products:
        values = Counter()
        for i,j in combinations_with_replacement(range(p),2):
            product = numerators[i]*numerators[j]
            need(product not in values, 'nontrivial unordered product collision')
            values[product] = 1 if i == j else 2
        energy = sum(m*m for m in values.values())
        need(len(values) == p*(p+1)//2, 'maximal product count')
        need(energy == 2*p*p-p, 'exact energy')
        result['unordered_products_enumerated'] = len(values)
        result['ordered_product_energy'] = energy
    else:
        result['product_scope'] = 'valuation criterion checked at every state; no pair census'
    return result


def high_candidate(H: int, minimum_p: int = 2, cap: int = 200000) -> tuple[int,int,int,int]:
    need(H >= 1, 'positive floor')
    three = 1
    two = 1
    for p in range(1,cap+1):
        three *= 3
        two *= 2
        if p < minimum_p or 2*two >= three or two <= 4*H+1:
            continue
        A = three.bit_length()  # 3^p is never an integral power of two.
        binary = 1 << A
        if (4*H+1)*three < 4*H*binary and 2*H*binary < (2*H+1)*three:
            D = binary-three
            C = three-two
            need(H*D < C < 4*H*D, 'high minimum interval')
            need(C+D < two*D, 'below first possible integer in the 2-adic class')
            need(C % D != 0, 'full denominator must fail')
            return p,A,D,C
    raise ValueError('finite candidate search cap exhausted; no existence inference is drawn')


def main() -> None:
    small = []
    for p in range(2,33):
        for A in sorted({(3**p).bit_length(), 5*p}):
            small.append(check_cycle(p,A,(1<<A)-3**p,3**p-(1<<p),True))
    high = []
    for H in (1,10,100,1000):
        p,A,D,C = high_candidate(H, minimum_p=10)
        record = check_cycle(p,A,D,C,count_products=(p<=100))
        record['prescribed_floor'] = H
        record['minimum_interval'] = [H,4*H]
        record['exact_interval_tests_passed'] = True
        need(not record['integral'], 'nonintegral high control')
        high.append(record)
    rejected=[]
    p,A=4,20
    D,C=(1<<A)-3**p,3**p-(1<<p)
    for name,args in [
        ('wrong full denominator',(p,A,D+2,C,False)),
        ('wrong complete carry',(p,A,D,C+2,False)),
        ('wrong word clock',(p,A+1,D,C,False)),
    ]:
        try:
            check_cycle(*args)
        except ValueError:
            rejected.append(name)
        else:
            raise ValueError('damaged control accepted: '+name)
    note=Path(__file__).with_name('CYCLE_PRODUCT_TRANSFER_ATTEMPT.md')
    print(json.dumps({
        'scope':'Finite exact controls for a written all-period rational Sidon theorem; not an integer-cycle exclusion or a large cycle census.',
        'proof_sha256':sha256(note.read_bytes()).hexdigest(),
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
        'small_controls':small,'high_controls':high,'damaged_inputs_rejected':rejected,
    },indent=2,sort_keys=True))


if __name__ == '__main__':
    main()
