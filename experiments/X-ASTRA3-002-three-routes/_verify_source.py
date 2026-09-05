#!/usr/bin/env python3
"""Independent finite reconstruction. No generator or repository imports."""
from __future__ import annotations
import argparse
import copy
import hashlib
import json
from collections import Counter
from fractions import Fraction as Rat
from pathlib import Path


def seal(x):
    return hashlib.sha256(json.dumps(x, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def valuation(x, prime):
    x = abs(x)
    if not x:
        raise ValueError('zero valuation argument')
    k, power = 0, prime
    while x % power == 0:
        k += 1
        power *= prime
    return k


def step(x):
    if isinstance(x, Rat):
        return (3*x+1)/2 if x.numerator % 2 else x/2
    return (3*x+1)//2 if x % 2 else x//2


def odd_step(x):
    assert x % 2
    x = step(x)
    length = 1
    while x % 2 == 0:
        x //= 2
        length += 1
    return x, length


def whole_run(x):
    assert x % 2
    while x % 2:
        x = step(x)
    while x % 2 == 0:
        x //= 2
    return x


def cylinders():
    rows = []
    for A in range(1, 12):
        for q in range(1, min(A, 5)+1):
            found = {}
            for n in range(1, 2**(A+1), 2):
                x, word = n, []
                for _ in range(q):
                    x, a = odd_step(x)
                    word.append(a)
                if sum(word) == A:
                    key = tuple(word)
                    assert key not in found
                    found[key] = (n, x)
            for word in sorted(found):
                root, endpoint = found[word]
                B = 2**A*endpoint-3**q*root
                assert 0 < B*2**q <= (3**q-2**q)*2**A
                ends = []
                for lift in (0, 1, 3):
                    x = root+2**(A+1)*lift
                    observed = []
                    for _ in range(q):
                        x, a = odd_step(x)
                        observed.append(a)
                    assert tuple(observed) == word
                    ends.append(x)
                rows.append([list(word), B, root, ends])
    # Composition counts via Pascal recurrence, not the generator's binomial call.
    ways = [[0]*108 for _ in range(65)]
    ways[0][0] = 1
    for q in range(1, 65):
        for a in range(1, 108):
            ways[q][a] = ways[q][a-1]+ways[q-1][a-1]
    tails = []
    for q in range(1, 65):
        m = 5*q//3
        mass = sum((Rat(ways[q][a], 1 << a) for a in range(q, m+1)), Rat())
        assert mass.numerator**3*3456**q <= mass.denominator**3*3125**q
        tails.append([q, m, mass.numerator, mass.denominator])
    assert 8*3125**24 < 3456**24
    assert 3**200 < 2**317
    assert 317**6340 < 2**6023*117**2340*200**4000
    assert 8*177**2 > 500**2
    assert 463**2*65**3 > 250**2*98**3
    assert Rat(177, 500)+Rat(69, 200)*Rat(463, 250) < Rat(993, 1000)
    return dict(words=len(rows), ordinary_replays=3*len(rows), max_total=11, max_odd_depth=5,
                cylinder_digest=seal(rows), tail_cases=64, tail_digest=seal(tails), integer_certificates=6)


def corrections():
    records = []
    positions = 0
    for n in range(3, 516, 2):
        path = [n]
        while len(path)-1 < 128 and path[-1] not in path[:-1]:
            path.append(step(path[-1]))
        count = 0
        product = Rat(1)
        for k, (x, y) in enumerate(zip(path, path[1:]), 1):
            if x % 2:
                count += 1
                product *= 1+Rat(1, 3*x)
            assert product == Rat(y*2**k, n*3**count)
        k = len(path)-1
        coefficient = Rat(3**count, 2**k)
        records.append([n, k, min(path[:-1]), count, coefficient.numerator,
                        coefficient.denominator, product.numerator, product.denominator])
        positions += k
    core = []
    for n in range(1, 65):
        path = [n]
        while path[-1] != 1:
            path.append(step(path[-1]))
            assert len(path) <= 1001
        core.append(len(path)-1)
    return dict(sources=257, positions=positions, max_horizon=128, digest=seal(records),
                core_hitting_times=core)


def affine(word):
    one_positions = [i for i, ch in enumerate(word) if ch == '1']
    q = len(one_positions)
    A = sum(2**pos*3**(q-1-i) for i, pos in enumerate(one_positions))
    return 2**len(word), 3**q, A


def echo_reference():
    live = ['']
    words = []
    for length in range(1, 22):
        new = []
        for prefix in live:
            for ch in '01':
                word = prefix+ch
                if 3**word.count('1') < 2**length:
                    words.append(word)
                else:
                    new.append(word)
        live = new
    rows = []
    hist = Counter()
    signs = Counter()
    integer = old = cycles = integer_cycles = steps = 0
    for word in sorted(words):
        P, Q, A = affine(word)
        D = P-Q
        if A:
            r = Rat(A, D)
            x = r
            cycles += 1
            integer_cycles += int(r.denominator == 1)
            for bit in word:
                assert x.numerator % 2 == int(bit)
                x = step(x)
                assert x >= r
            assert x == r
        for d in range(1, (A+P-1)//P):
            r = Rat(A-P*d, D)
            y = r+d
            assert r > 0
            integer += int(r.denominator == 1)
            # Literal paired replay checks the old first-disagreement predicate.
            t = valuation(d, 2)
            z = y
            for _ in range(t+1):
                z = step(z)
            first_echo = t < len(word) and word[t] == '1' and z < r
            old += int(first_echo)
            u = ''
            b = 0
            pu = qu = 1
            au = 0
            end = 0
            for k in range(1, 2*len(word)+1):
                v = y.numerator % 2
                # Lift the source bit by testing the previous physical prefix.
                if ((qu*b+au)//pu) % 2 != v:
                    b += pu
                u += str(v)
                y = step(y)
                pu, qu, au = affine(u)
                assert (A-Q*d-D*b) % pu == 0
                coefficient = P*pu-Q*qu
                signs['positive' if coefficient > 0 else 'negative' if coefficient < 0 else 'zero'] += 1
                left = coefficient*d
                right = (pu-qu)*A-D*au
                assert (left >= right) == (y >= r)
                steps += 1
                if y < r:
                    end = k
                    break
            if first_echo:
                assert 0 < end <= t+1
            rows.append([word, d, int(first_echo), end])
            hist[end] += 1
    # Discover the rational countermodel's cycle independently.
    values = []
    x = Rat(61, 295)
    while x not in values:
        assert x >= Rat(61, 295) and len(values) < 1000
        values.append(x)
        x = step(x)
    index = values.index(x)
    assert index == 13 and len(values)-index == 30
    assert values[10]-values[0] == 1
    pre = [int(v*295) for v in values[:index]]
    cyc = [int(v*295) for v in values[index:]]
    return dict(limit=21, words=len(words), positive_pairs=len(rows), integer_sources=integer,
                old_rejections=old, continuation_rejections=len(rows)-hist[0], remaining=hist[0],
                steps=steps, coefficient_signs=dict(sorted(signs.items())), histogram={str(k): v for k, v in sorted(hist.items())}, digest=seal(rows),
                rational_cycles=cycles, integer_cycles=integer_cycles,
                rational_countermodel=dict(denominator=295, preperiod=pre, period=cyc))


def verify_ranks(data):
    profiles = [[[2,-1,2,1]], [[2,-1,2,-1]], [[3,-1,2,1]], [[3,-1,2,-1]],
                [[2,-1,3,1]], [[2,-1,3,-1]], [[2,-1,2,0]], [[3,-1,2,0]],
                [[2,-1,2,-1], [3,-1,3,1]]]
    assert set(data) == {'profiles', 'floor', 'witnesses', 'count'}
    assert data['profiles'] == profiles and data['floor'] == 10**6 and data['count'] == 36
    assert len(data['witnesses']) == 36
    seen = set()
    for row in data['witnesses']:
        assert set(row) == {'profile', 'mode', 'source', 'endpoint'}
        i, mode = row['profile'], row['mode']
        assert type(i) is int and 0 <= i < 9
        assert type(mode) in (int, str) and mode in (1, 2, 4, 'macro') and (i, mode) not in seen
        seen.add((i, mode))
        n, y = row['source'], row['endpoint']
        assert type(n) is int and type(y) is int and min(n, y) > 10**6
        if mode == 'macro':
            assert n % 2 and whole_run(n) == y
        else:
            x = n
            for _ in range(mode):
                x = step(x)
            assert x == y
        weights = []
        for x in (n, y):
            w = Rat(x)
            for prime, root, exponent, sign in profiles[i]:
                k = valuation(x-root, prime)
                power = (sign if sign else (-1)**k)*k**exponent
                w *= Rat(prime)**power
            weights.append(w)
        assert weights[1] > weights[0]
    assert seen == {(i, mode) for i in range(9) for mode in (1, 2, 4, 'macro')}


def validate(report, expected):
    assert set(report) == {'payload', 'sha256'}
    p = report['payload']
    assert set(p) == {'schema', 'scope', 'cylinders', 'corrections', 'echoes', 'ranks'}
    assert p['schema'] == 'X-ASTRA3-002/v1'
    assert p['scope'] == 'finite exact checks only; no Collatz proof or independent mathematical review'
    assert seal(p) == report['sha256']
    verify_ranks(p['ranks'])
    for name in ('cylinders', 'corrections', 'echoes'):
        assert p[name] == expected[name], name


def self_test(report, expected):
    mutations = [
        lambda p: p.__setitem__('scope', 'Collatz proved'),
        lambda p: p['cylinders'].__setitem__('words', 1022),
        lambda p: p['echoes'].__setitem__('continuation_rejections', 9779),
        lambda p: p['echoes']['rational_countermodel']['period'].__setitem__(0, 282),
        lambda p: p['ranks']['witnesses'].pop(),
        lambda p: p['ranks']['witnesses'][0].__setitem__('endpoint', 1000001),
    ]
    for alter in mutations:
        bad = copy.deepcopy(report)
        alter(bad['payload'])
        bad['sha256'] = seal(bad['payload'])
        try:
            validate(bad, expected)
        except (AssertionError, KeyError, TypeError, ValueError):
            continue
        raise AssertionError('resealed corruption accepted')
    return len(mutations)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('certificate', type=Path)
    parser.add_argument('--self-test', action='store_true')
    args = parser.parse_args()
    report = json.loads(args.certificate.read_text())
    expected = dict(cylinders=cylinders(), corrections=corrections(), echoes=echo_reference())
    validate(report, expected)
    print('PASS independent reconstruction', report['sha256'])
    if args.self_test:
        print('PASS resealed corruptions rejected:', self_test(report, expected))


if __name__ == '__main__':
    main()
