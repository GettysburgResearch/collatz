#!/usr/bin/env python3
"""Reviewer D final-pass regressions. Not a full-checkout or universal proof test.

Standard library only. No source, prior generator, or verifier is imported.
All predicates remain active under optimized Python; only --write writes data.
"""
from __future__ import annotations
import argparse
from copy import deepcopy
from fractions import Fraction as F
from hashlib import sha256
from itertools import product
from math import gcd
from pathlib import Path
import json

SCHEMA = 'reviewer-d-final-regressions/v1'
SCOPE = 'finite exact endpoint and hypothesis regressions; not a full repository validation'
BASE = 'cd1b3689e8d37fc4232945072e2faf6bd5ee47bd'
PRIOR = '0ce01f9cff107745abc3dabb8b1faa27ab6acfd4'


def need(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def canonical(obj: object) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()


def digest(obj: object) -> str:
    return sha256(canonical(obj)).hexdigest()


def rat(x: F) -> list[int]:
    return [x.numerator, x.denominator]


def centered_endpoints() -> dict:
    pairs = [(M, N) for N in range(3, 13) for M in range(2, N) if gcd(M, N) == 1]
    pairs.append((64, 81))
    transcript = []
    comparisons = endpoints = zeros = 0
    for M, N in pairs:
        rho = F(M, N)
        for length in range(1, 7):
            for prefix in product((0, 1), repeat=length):
                for tail in (0, 1):
                    digits = list(prefix) + [tail]
                    companions = [F(tail)]
                    for bit in reversed(prefix):
                        companions.insert(0, (1-rho)*bit + rho*companions[0])
                    errors = [(F(bit)-x)/M for bit, x in zip(digits, companions)]
                    for i, error in enumerate(errors):
                        need(abs(error) <= F(1, N), 'closed strip failed')
                        future = digits[i:]
                        is_constant = all(bit == future[0] for bit in future)
                        need((error == 0) == is_constant, 'zero-error classification')
                        if error:
                            need((error > 0) == bool(digits[i]), 'nonzero error sign')
                        if i < length:
                            need(N*error - M*errors[i+1] == digits[i]-digits[i+1], 'carry recurrence')
                            opposite_tail = all(bit == 1-digits[i] for bit in digits[i+1:])
                            need((abs(error) == F(1, N)) == opposite_tail, 'endpoint classification')
                        endpoints += int(abs(error) == F(1, N))
                        zeros += int(error == 0)
                        comparisons += 1
                    transcript.append([M, N, list(prefix), tail, [rat(x) for x in errors]])
    # Explicit counterexamples: a nonconstant current code can reach either endpoint.
    M, N = 64, 81
    plus = (F(1) - F(N-M, N))/M
    minus = -F(M, N)/M
    need(plus == F(1, N) and minus == -F(1, N), 'named endpoint witnesses')
    # The same-sign inverse branch g(r)=rho*r has open cylinders
    # (0, rho**k/N). Their infinite intersection is empty, by rho<1.
    # The finite rows test the formula, not that all-depth assertion numerically.
    radii = [F(M, N)**k/N for k in range(17)]
    need(all(0 < b < a for a, b in zip(radii, radii[1:])), 'nested open radii')
    return dict(parameter_pairs=len(pairs), codes=len(transcript), positions=comparisons,
                endpoint_positions=endpoints, zero_positions=zeros,
                witnesses=[rat(plus), rat(minus)],
                open_cylinder_radii=[rat(x) for x in radii],
                infinite_intersection_claim='proved in FINAL_HANDOFF.md, not by this finite test',
                transcript_sha256=digest(transcript))


def hypotheses() -> dict:
    P, Q = 3**12, 2**19
    digits = [229376, 258048, 290304, 326592, 367416, 413343]
    residues = [(-a*pow(P, -1, Q)) % Q for a in digits]
    need(len(set(residues)) == 6, 'distinct constant-parent congruences')
    counts = [sum((P*c+a) % Q == 0 for a in digits) for c in residues]
    need(counts == [1]*6, 'constant parent cannot have six integral children')
    even_values = [F(2*k, 2) for k in range(1, 129)]
    odd_values = [F(2*k-1, 2) for k in range(1, 129)]
    need(all(x.denominator == 1 for x in even_values), 'syndetic integer values')
    need(all(x.denominator == 2 for x in odd_values), 'missing full-tail integrality')
    signed = []
    for J in range(1, 25):
        values = [(-2**J) % 2**k for k in range(J+13)]
        bits = [(values[k+1]-values[k])//2**k for k in range(J+12)]
        need(bits == [0]*J + [1]*12, 'negative ordinary face')
        signed.append([J, values, bits])
    return dict(constant_parent_residues=residues, legal_child_counts=counts,
                syndetic_even_samples=len(even_values), nonintegral_odd_controls=len(odd_values),
                signed_face_cases=len(signed), signed_sha256=digest(signed))


def build() -> dict:
    payload = dict(schema=SCHEMA, scope=SCOPE, base=BASE, prior_review=PRIOR,
                   centered=centered_endpoints(), hypotheses=hypotheses())
    return dict(payload=payload, sha256=digest(payload))


def validate(actual: dict, expected: dict) -> None:
    need(isinstance(actual, dict) and set(actual) == {'payload', 'sha256'}, 'invalid envelope')
    need(actual['sha256'] == digest(actual['payload']), 'digest mismatch')
    # Canonical serialization, not Python numeric equality: 1, 1.0, and true differ.
    need(canonical(actual) == canonical(expected), 'independent regeneration mismatch')


def self_test(expected: dict) -> int:
    edits = [
        lambda p: p.update(scope='all-time Collatz proof'),
        lambda p: p['centered'].update(codes=p['centered']['codes']+1),
        lambda p: p['centered']['witnesses'][0].__setitem__(0, 0),
        lambda p: p['centered']['open_cylinder_radii'].pop(),
        lambda p: p['hypotheses']['legal_child_counts'].__setitem__(0, 6),
        lambda p: p['hypotheses'].update(syndetic_even_samples=0),
        lambda p: p['hypotheses'].update(signed_face_cases=0),
        lambda p: p['hypotheses']['legal_child_counts'].__setitem__(0, True),
    ]
    for change in edits:
        bad = deepcopy(expected)
        change(bad['payload'])
        need(canonical(bad['payload']) != canonical(expected['payload']), 'no-op mutation')
        bad['sha256'] = digest(bad['payload'])
        try:
            validate(bad, expected)
        except ValueError:
            continue
        raise ValueError('resealed corruption accepted')
    return len(edits)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--check', type=Path)
    group.add_argument('--write', type=Path)
    parser.add_argument('--self-test', action='store_true')
    args = parser.parse_args()
    expected = build()
    if args.check:
        validate(json.loads(args.check.read_text(encoding='utf-8')), expected)
    if args.write:
        args.write.parent.mkdir(parents=True, exist_ok=True)
        args.write.write_bytes(canonical(expected)+b'\n')
    print('PASS Reviewer D final regressions:', expected['sha256'])
    if args.self_test:
        print('Resealed corruptions rejected:', self_test(expected))
    print(json.dumps({k: expected['payload']['centered'][k] for k in
                      ('parameter_pairs', 'codes', 'positions', 'endpoint_positions', 'zero_positions')}, sort_keys=True))


if __name__ == '__main__':
    main()
