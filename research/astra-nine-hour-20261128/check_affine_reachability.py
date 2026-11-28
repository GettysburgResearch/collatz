#!/usr/bin/env python3
"""Exact finite controls for affine legality and odd-modulus transitivity.

This does not search for, or claim, an unrestricted Collatz proof.
All checks remain active under Python optimization.
"""
from collections import deque
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def step(n):
    return n // 2 if n % 2 == 0 else (3*n + 1) // 2


def run():
    root = Path(__file__).resolve().parent
    endpoint_cases = 0
    integral_cases = 0
    bad_branch_cases = 0
    word_rows = 0
    max_length = 10
    for length in range(max_length + 1):
        seen = set()
        for code in range(1 << length):
            bits = [(code >> j) & 1 for j in range(length)]
            a, c, denominator = 1, 0, 1
            for bit in bits:
                a = (3 if bit else 1) * a
                c = (3 if bit else 1) * c + bit * denominator
                denominator *= 2
            residue = (-c * pow(a, -1, denominator)) % denominator
            require(residue not in seen, 'Parity-cylinder collision')
            seen.add(residue)
            word_rows += 1
            for source in range(65):
                value = Fraction(source)
                actual = source
                legal = True
                broken_at = None
                for j, bit in enumerate(bits):
                    if legal and bit != actual % 2:
                        legal = False
                        broken_at = j
                    value = ((3*value + 1) if bit else value) / 2
                    actual = step(actual)
                    if broken_at is not None:
                        require(value.denominator == 1 << (j-broken_at+1),
                                'A broken parity branch recovered integrality')
                require(value == Fraction(a*source+c, denominator),
                        'Literal rational word and cleared numerator disagree')
                integral = value.denominator == 1
                require(integral == legal, 'Integrality/legality mismatch')
                if integral:
                    require(value.numerator == actual, 'Wrong ordinary endpoint')
                    integral_cases += 1
                else:
                    bad_branch_cases += 1
                endpoint_cases += 1
        require(len(seen) == 1 << length, 'Incomplete cylinder partition')

    quotient_states = 0
    largest_distance = 0
    largest_distance_modulus = None
    modulus_count = 0
    for modulus in range(1, 502, 2):
        inverse_two = pow(2, -1, modulus)
        parents = [[] for _ in range(modulus)]
        for x in range(modulus):
            for bit in (0, 1):
                y = (((3*x+1) if bit else x)*inverse_two) % modulus
                parents[y].append(x)
        distance = {1 % modulus: 0}
        queue = deque(distance)
        while queue:
            y = queue.popleft()
            for x in parents[y]:
                if x not in distance:
                    distance[x] = distance[y]+1
                    queue.append(x)
        require(len(distance) == modulus, 'Odd quotient has an unreachable state')
        height = max(distance.values())
        if height > largest_distance:
            largest_distance = height
            largest_distance_modulus = modulus
        quotient_states += modulus
        modulus_count += 1

    # This real convexity obstruction uses only actual nonterminal inputs.
    triangle = [(Fraction(1, 9), (3, 5)),
                (Fraction(1, 9), (5, 8)),
                (Fraction(7, 9), (4, 2))]
    for _, (x, y) in triangle:
        require(step(x) == y, 'Invalid actual triangle edge')
    point = tuple(sum(w*p[i] for w, p in triangle) for i in (0, 1))
    require(point == (4, 3) and step(4) != 3, 'Convexity control failed')

    return {
        'scope': 'finite exact controls, not unrestricted Collatz verification',
        'maximum_word_length': max_length,
        'complete_word_rows': word_rows,
        'source_word_cases': endpoint_cases,
        'integer_endpoints': integral_cases,
        'irreversible_bad_branches': bad_branch_cases,
        'odd_moduli_through': 501,
        'odd_moduli_tested': modulus_count,
        'quotient_states': quotient_states,
        'maximum_shortest_quotient_word': largest_distance,
        'first_modulus_at_maximum': largest_distance_modulus,
        'convex_false_edge': [4, 3],
        'source_sha256': {
            name: sha256((root/name).read_bytes()).hexdigest()
            for name in ('AffineReachability.lean', 'check_affine_reachability.py')
        },
    }


if __name__ == '__main__':
    print(json.dumps(run(), sort_keys=True))
