#!/usr/bin/env python3
"""Exact finite controls for the written complete-denominator tensor attempt.

This is not a proof of integer-cycle exclusion or of the all-period results.
The latter are proved in PAIRED_TENSOR_CLOSURE_ATTEMPT.md.
"""
from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import json
from math import gcd
from pathlib import Path


def need(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def ihash(n: int) -> str:
    need(n >= 0, 'nonnegative integer hash domain')
    return sha256(n.to_bytes(max(1, (n.bit_length()+7)//8), 'big')).hexdigest()


def carries(word: tuple[int, ...]) -> tuple[int, int]:
    C = Cs = 0
    for i, e in enumerate(word):
        need(e in (0, 1), 'binary chronological word')
        C = 3**e*C + e*(1 << i)
        Cs = 3**(1-e)*Cs + (1-e)*(1 << i)
    return C, Cs


def check_word(word: tuple[int, ...], label: str) -> dict:
    A, p = len(word), sum(word)
    b = A-p
    need(0 < p < A, 'nonconstant word')
    C, Cs = carries(word)
    D, E, T = (1 << A)-3**p, (1 << A)-3**b, (1 << (2*A))-3**A
    need(D > 0 and E > 0, 'positive paired denominators')
    original_gcd, companion_gcd = gcd(C,D), gcd(Cs,E)
    q = E//companion_gcd
    need(gcd(T,D) == gcd(D,E) == gcd(T,E), 'complete tensor gcd identity')
    U, V, centered_sum, tensor_sum = C, Cs, 0, 0
    original_states, companion_states = set(), set()
    for i, e in enumerate(word):
        need(U > 0 and V > 0, 'positive paired raw states')
        need(U % 2 == e and V % 2 == 1-e, 'literal complementary parity')
        need(gcd(U,D) == original_gcd, 'same original complete denominator')
        need(gcd(V,E) == companion_gcd, 'same companion complete denominator')
        original_states.add(U)
        companion_states.add(V)
        centered_sum += (2*U-D)*(2*V-E)
        forcing = e*D*V + (1-e)*E*U
        tensor_sum = 3*tensor_sum + (1 << (2*i))*forcing
        U1 = (3**e*U+e*D)//2
        V1 = (3**(1-e)*V+(1-e)*E)//2
        need(4*U1*V1 == 3*U*V+forcing, 'literal paired product step')
        U,V = U1,V1
    need((U,V) == (C,Cs), 'both complete cycles close')
    need(len(original_states) == len(companion_states) == A, 'both periods primitive')
    need(centered_sum == 3*A*D*E, 'centered product sum')
    need(tensor_sum == T*C*Cs, 'complete tensor closure')
    return {
        'label': label, 'shortcut_period': A, 'original_odd_steps': p,
        'complementary_odd_steps': b,
        'original_reduced_denominator_bits': (D//original_gcd).bit_length(),
        'complementary_reduced_denominator_bits': q.bit_length(),
        'original_is_integral': original_gcd == D,
        'original_full_denominator_sha256': ihash(D),
        'original_full_carry_sha256': ihash(C),
        'complementary_full_denominator_sha256': ihash(E),
        'complementary_full_carry_sha256': ihash(Cs),
        'complementary_reduced_denominator_sha256': ihash(q),
        'literal_paired_steps_checked': A,
        'full_gcd_and_tensor_checks_passed': True,
    }


def high_candidate(H: int, cap: int = 200000) -> tuple[int, int]:
    need(H >= 1, 'positive floor')
    power3 = 1
    for p in range(1, cap+1):
        power3 *= 3
        if p < 10 or 2*(1 << p) >= power3 or (1 << p) <= 4*H+1:
            continue
        A = power3.bit_length()
        power2 = 1 << A
        if (4*H+1)*power3 < 4*H*power2 and 2*H*power2 < (2*H+1)*power3:
            return p, A
    raise ValueError('finite candidate cap exhausted; no universal inference is drawn')


def check_high(H: int) -> dict:
    p, A = high_candidate(H)
    b, d = A-p, 2*p-A
    D, E = (1 << A)-3**p, (1 << A)-3**b
    C, Cs = 3**p-(1 << p), (1 << p)*(3**b-(1 << b))
    need(carries((1,)*p+(0,)*b) == (C,Cs), 'both one-rise complete carries')
    need(H*D < C < 4*H*D, 'high minimum interval')
    need(C+D < (1 << p)*D and C % D != 0, 'original full nonintegrality')
    original_gcd = gcd(C,D)
    companion_gcd = gcd(Cs,E)
    need(original_gcd == gcd(C,(1 << b)-1), 'original full gcd formula')
    need(companion_gcd == gcd(3**b-(1 << b),(1 << p)-1), 'companion full gcd formula')
    q = E//companion_gcd
    need(d >= 2 and A <= 4*d+4, 'excess-to-period estimate')
    need(q > 3**d-1, 'exponential complete companion bound')
    need(2*q > A and q > 3*d, 'both refreshed complementary lower bounds')
    result = check_word((1,)*p+(0,)*b, f'high floor {H}')
    result.update({
        'prescribed_floor': H, 'minimum_open_interval': [H,4*H],
        'minimum': str(Fraction(C,D)) if D.bit_length() <= 160 else 'exact interval certified',
        'excess_original_odd_over_even': d,
        'complementary_denominator_exceeds_3_power_excess_minus_1': True,
        'both_new_linear_companion_bounds_passed': True,
    })
    return result


def main() -> None:
    note = Path(__file__).with_name('PAIRED_TENSOR_CLOSURE_ATTEMPT.md')
    result = {
        'scope': 'Six exact finite paired-cycle controls, not integer-cycle exclusion or a cycle census.',
        'proof_sha256': sha256(note.read_bytes()).hexdigest(),
        'checker_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
        'generic_controls': [
            check_word((1,0), 'integer core'),
            check_word((1,1,0,1,1,0,1,0), 'positive non-one-rise rational control'),
        ],
        'high_controls': [check_high(H) for H in (1,10,100,1000)],
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
