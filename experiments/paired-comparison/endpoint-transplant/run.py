#!/usr/bin/env python3
"""EPT corpus: proposed endpoint transplantation and source-capped inverse blocks.
Standard library only. No assumption of Collatz convergence; no assert guards.
"""
import argparse
from collections import Counter
from functools import lru_cache
import hashlib
import json
from pathlib import Path


def require(ok, message):
    if not ok:
        raise ValueError(message)


def integer(x, lower=0):
    require(type(x) is int and x >= lower, 'invalid integer')
    return x


def T(n):
    return (3*n+1)//2 if n & 1 else n//2


def trace(n, length):
    word = ''
    for _ in range(length):
        word += str(n & 1)
        n = T(n)
    return n, word


def gate(offsets):
    require(type(offsets) is list and len(offsets) >= 2, 'offset list')
    for x in offsets:
        integer(x)
    require(len(set(offsets)) == len(offsets), 'duplicate offsets')
    slopes = [1]*len(offsets)
    intercepts = offsets[:]
    words = ['']*len(offsets)
    residue = length = 0

    def impose(i, value, bits):
        nonlocal residue, length
        modulus = 1 << bits
        digit = ((value-intercepts[i])*pow(slopes[i], -1, modulus)) % modulus
        residue += (1 << length)*digit
        length += bits
        for h in range(len(slopes)):
            a = slopes[h]*modulus
            b = slopes[h]*digit+intercepts[h]
            for _ in range(bits):
                parity = b & 1
                words[h] += str(parity)
                require(a % 2 == 0, 'nonuniform parity prefix')
                a = (3*a if parity else a)//2
                b = T(b)
            slopes[h], intercepts[h] = a, b

    # Credited ACS-002/003 controlled chart reductions, reconstructed here.
    for h in range(1, len(offsets)):
        while (slopes[0], intercepts[0]) != (slopes[h], intercepts[h]):
            lo, hi = (0, h) if slopes[0] <= slopes[h] else (h, 0)
            factor = slopes[hi]//slopes[lo]
            b = intercepts[hi]-factor*intercepts[lo]
            if factor > 1:
                impose(lo, 1 if b & 1 or b == 0 else 0, 1)
            elif b:
                lower = lo if b > 0 else hi
                gap = abs(b)
                if gap == 1:
                    impose(lower, 4, 3)
                elif gap % 2 == 0:
                    impose(lower, 0, 1)
                elif gap % 4 == 1:
                    impose(lower, 1, 2)
                else:
                    impose(lower, 2, 2)
    a = slopes[0]
    q = 0
    while a % 3 == 0:
        a //= 3
        q += 1
    require(a == 1 and q > 0 and intercepts[0] % 3 != 0, 'endpoint unit')
    t_min = max(0, (1-residue-min(offsets)+(1 << length)-1)//(1 << length))
    return dict(kind='gate', offsets=offsets, B=residue, L=length, Q=q,
                e=intercepts[0], t_min=t_min, words=words)


def log2_ternary(unit, q):
    integer(q, 1)
    integer(unit, 1)
    require(unit < 3**q and unit % 3 != 0, 'nonunit or noncanonical unit')
    k = 0 if unit % 3 == 1 else 1
    modulus, period = 3, 2
    for _ in range(1, q):
        modulus *= 3
        candidates = [k+d*period for d in range(3)
                      if pow(2, k+d*period, modulus) == unit % modulus]
        require(len(candidates) == 1, 'ternary lift')
        k = candidates[0]
        period *= 3
    return k, period


def transplant(n, g, minimum=1):
    integer(n, 1)
    integer(minimum, 1)
    y, prefix = n, ''
    while y % 3 == 0:
        prefix += str(y & 1)
        y = T(y)
    modulus = 3**g['Q']
    unit = g['e']*pow(y, -1, modulus) % modulus
    k0, period = log2_ternary(unit, g['Q'])
    t_min = max(g['t_min'], (minimum-g['B']-min(g['offsets'])+
                               (1 << g['L'])-1)//(1 << g['L']))
    threshold = modulus*t_min+g['e']
    k_min = 0
    while (y << k_min) < threshold:
        k_min += 1
    k = k0+max(0, (k_min-k0+period-1)//period)*period
    t = ((y << k)-g['e'])//modulus
    start = g['B']+(1 << g['L'])*t
    return dict(kind='transplant', n=n, gate_offsets=g['offsets'], minimum=minimum,
                y=y, prefix=prefix, k=k, k0=k0, period=period, k_min=k_min,
                t_min=t_min, t=t, start=start)


def envelope(cap, blocks):
    integer(cap, 2)
    integer(blocks)
    for _ in range(blocks):
        cap = 3**(cap.bit_length()-1)
    return cap


def block_parents(endpoint, cap):
    integer(endpoint, 1)
    integer(cap, 2)
    limit = 3**(cap.bit_length()-1)
    value, zeros = endpoint, 0
    found = []
    while value+1 <= limit:
        quotient, ones = value+1, 0
        while quotient % 3 == 0:
            quotient //= 3
            ones += 1
            source = (quotient << ones)-1
            if 1 <= source < cap:
                found.append((source, '1'*ones+'0'*zeros))
        zeros += 1
        value *= 2
    return sorted(found)


@lru_cache(maxsize=None)
def inverse(cap, endpoint, blocks):
    if endpoint < cap:
        return endpoint, ''
    if blocks == 0 or endpoint >= envelope(cap, blocks):
        return None
    for source, suffix in block_parents(endpoint, envelope(cap, blocks-1)):
        earlier = inverse(cap, source, blocks-1)
        if earlier is not None:
            return earlier[0], earlier[1]+suffix
    return None


def query(cap, endpoint, blocks):
    integer(cap, 2)
    integer(endpoint, 1)
    integer(blocks)
    result = inverse(cap, endpoint, blocks)
    return dict(kind='query', cap=cap, X=endpoint, blocks=blocks,
                source=None if result is None else result[0],
                word=None if result is None else result[1])


def selected(n, blocks, horizon=8):
    endpoint, prefix, low = n, '', n+1
    for a in range(1, horizon+1):
        prefix += str(endpoint & 1)
        endpoint = T(endpoint)
        low = min(low, endpoint)
        result = inverse(n, endpoint, blocks)
        if result:
            return dict(kind='selected', n=n, blocks=blocks, horizon=horizon,
                        status='MERGER', a=a, X=endpoint, prefix=prefix,
                        source=result[0], word=result[1], minimum=low)
    return dict(kind='selected', n=n, blocks=blocks, horizon=horizon,
                status='OUTSIDE', a=None, X=endpoint, prefix=prefix,
                source=None, word=None, minimum=low)


def corpus():
    patterns = [list(range(k)) for k in range(2, 13)]
    patterns += [[0, a, b] for a in range(1, 9) for b in range(a+1, 13)]
    patterns += [[9, 0, 5, 2], [0, 3, 9, 27, 81], [0, 2**64+3]]
    gates = [gate(p) for p in patterns]
    yield from gates
    for q in range(1, 65):
        period = 2*3**(q-1)
        for k in sorted({0, 1, period//2, period-1}):
            unit = pow(2, k, 3**q)
            got, order = log2_ternary(unit, q)
            yield dict(kind='log', Q=q, unit=unit, k=got, period=order)
    # Explicit full integers, not symbolic enormous powers, for bounded targets.
    for n in range(1, 513):
        for g in gates[:3]:
            yield transplant(n, g, n+1)
    for n in (3, 27, 71, 155, 641):
        yield transplant(n, gates[2], 10**30)
    # Complete rectangular small-query grid; its negatives are independently checked.
    for cap in range(2, 129):
        for blocks in range(4):
            for endpoint in range(1, 257):
                yield query(cap, endpoint, blocks)
        inverse.cache_clear()
    # Same original-source grid for each block budget, retaining every failure.
    for n in range(2, 4097):
        for blocks in range(4):
            yield selected(n, blocks)
        inverse.cache_clear()
    for s in list(range(6, 65))+[96, 128]:
        # n=3 mod4 and 3|n, both original roots positive.
        residue = 27*pow(3**s, -1, 32) % 32
        for t in (0, 1, 17):
            b = residue+32*t
            n = (3**s*b-3)//8
            m = 2**s*b-1
            yield dict(kind='ternary', s=s, b=b, n=n, source=m,
                        word='1'*s+'0100', X=T(n))
    for n in (1, 2, 3, 4, 5, 17, 71, 273, 4647):
        yield dict(kind='cap', cap=max(n, 2), R=max(n, 2).bit_length()-1,
                   endpoint_max=3**(max(n, 2).bit_length()-1)-1)


def encode(row):
    return json.dumps(row, sort_keys=True, separators=(',', ':'))+'\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--full', type=Path, required=True)
    parser.add_argument('--summary', type=Path, required=True)
    args = parser.parse_args()
    digest = hashlib.sha256()
    counts = Counter()
    outcomes = {str(b): Counter() for b in range(4)}
    with args.full.open('w', encoding='utf-8', newline='\n') as output:
        for row in corpus():
            data = encode(row)
            output.write(data)
            digest.update(data.encode())
            counts[row['kind']] += 1
            if row['kind'] == 'selected':
                c = outcomes[str(row['blocks'])]
                c[row['status']] += 1
                if row['status'] == 'MERGER' and row['minimum'] > row['n']:
                    c['no_forward_descent'] += 1
                    if row['n'] % 3 == 0:
                        c['no_forward_descent_divisible_by_3'] += 1
    summary = dict(schema='EPT-1', sha256=digest.hexdigest(), rows=sum(counts.values()),
                   counts=dict(counts), selected={k: dict(v) for k, v in outcomes.items()})
    args.summary.write_text(json.dumps(summary, indent=2, sort_keys=True)+'\n')
    print(json.dumps(summary, sort_keys=True))


if __name__ == '__main__':
    main()
