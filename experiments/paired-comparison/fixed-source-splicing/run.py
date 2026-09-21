#!/usr/bin/env python3
"""Exact, bounded original-source splicing experiment. PROPOSED mathematics.
The old selector is hash-pinned; only its actual successful words are retained.
"""
import argparse
import hashlib
import importlib.util
import json
from collections import Counter
from pathlib import Path

PARENT_BLOB = '0fb8e0a5da81c4c9138e39152e4389587291a0c2'
LIMIT = 65536
HORIZON = 64


def require(test, message):
    if not test:
        raise ValueError(message)


def positive(n):
    require(type(n) is int and n > 0, 'positive integer required')


def valuation(n):
    positive(n)
    return (n & -n).bit_length() - 1


def step(n):
    return (3*n+1)//2 if n % 2 else n//2


def trace(n, word):
    positive(n)
    require(type(word) is str and set(word) <= {'0', '1'}, 'word')
    values = []
    for bit in word:
        require(n % 2 == int(bit), 'illegal physical word')
        n = step(n)
        values.append(n)
    return n, values


def certificate(n, m, upper, lower, method):
    positive(n); positive(m)
    require(m < n, 'companion is not below ORIGINAL source')
    y, values = trace(n, upper)
    z, _ = trace(m, lower)
    require(y == z, 'endpoint mismatch')
    return dict(status='MERGE', method=method, m=m, words=[upper, lower],
                endpoint=y, minimum=min(values), strict=int(min(values) > n))


def load_parent(path):
    raw = path.read_bytes()
    digest = hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
    require(digest == PARENT_BLOB, 'parent generator blob changed')
    spec = importlib.util.spec_from_file_location('pinned_ufs', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def baseline(n, old):
    if n % 2 == 0:
        return certificate(n, n//2, '0', '', 'EVEN')
    if n % 4 == 1:
        return certificate(n, (3*n+1)//4, '10', '', 'MOD4')
    r = valuation(n+1); u = (n+1)//2**r
    if 3**r*u % 4 == 1:
        return certificate(n, (n-1)//2, '1'*r+'00', '1'*(r-1)+'01', 'GOOD_EXIT')
    c = (3**(r-1)*u-1)//4
    previous = old.classify(c, set())
    if previous['status'] != 'MERGE':
        return dict(status=previous['status'], C=c)
    w, z = previous['words']
    return certificate(n, (n-1)//2, '1'*r+'01'+w, '1'*(r-1)+'00'+z, 'UFS')


def new_selector(n):
    """Called only on a hard first exit. Never selects future parameter digits."""
    r = valuation(n+1); u = (n+1)//2**r
    require(r >= 2 and 3**r*u % 4 == 3, 'hard first exit required')
    c = (3**(r-1)*u-1)//4
    e = valuation(c)
    if e % 2:
        k = (e-1)//2; v = c//2**e; m = 3**(k+1)*v
        if m < n:
            return certificate(n, m, '1'*r+'01'*(k+1)+'00', '1', 'VALUATION')
    if r in (2, 3):
        z = (3**r*u-1)//2; s = valuation(z+1); v = (z+1)//2**s
        if 3**s*v % 4 == 1:
            return certificate(n, 3*c, '1'*r+'0'+'1'*s+'00',
                               '1'*(s-1)+'01', 'RESTART')
    z = (3**r*u-1)//2; s = valuation(z+1); v = (z+1)//2**s
    if 3**s*v % 4 == 3:
        d = (3**(s-1)*v-1)//4
        e = valuation(d)
        if e % 2:
            h = (e-1)//2; m = 3**(h+1)*(d//2**e)
            if m < n:
                return certificate(n, m, '1'*r+'0'+'1'*s+'01'*(h+1)+'00',
                                   '1', 'SECOND_VALUATION')
    y = n; word = ''
    for clock in range(1, HORIZON+1):
        word += str(y % 2); y = step(y)
        if y <= n:
            return dict(status='OUTSIDE', stop='DESCENT_OR_RETURN', clock=clock, state=y)
        if y % 3 == 2 and 2*y-1 < 3*n:
            return certificate(n, (2*y-1)//3, word, '1', 'BAND')
    return dict(status='OUTSIDE', stop='HORIZON', clock=HORIZON, state=y)


def symbolic(A, B, word):
    """Affine output and all positive-time affine prefixes, for every t>=0."""
    require(A > 0 and B > 0, 'nonpositive affine tail')
    prefixes = []
    for bit in word:
        require(A % 2 == 0 and B % 2 == int(bit), 'whole-cylinder parity')
        if bit == '1':
            A, B = 3*A, 3*B+1
        A //= 2; B //= 2
        prefixes.append([A, B])
    return [A, B], prefixes


def family(kind, args, forms, words, strict=0, divisible=0):
    end, prefixes = symbolic(*forms[0], words[0])
    other, _ = symbolic(*forms[1], words[1])
    require(end == other, 'affine merger')
    if kind != 'TEMPLATE':
        require(forms[0][0] > forms[1][0] and forms[0][1] > forms[1][1], 'whole-root order')
    if strict:
        require(all(a >= forms[0][0] and b > forms[0][1] for a, b in prefixes), 'whole strict path')
    if divisible:
        require(all(x % 3 == 0 for x in forms[0]), 'whole 3-divisibility')
    return dict(kind=kind, args=args, forms=forms, words=words, endpoint=end,
                strict=strict, divisible3=divisible)


def valuation_family(r, k, kind):
    # Exact odd valuation: 3^(r-1)u-1 = 2^(2k+3) modulo 2^(2k+4).
    Q = 2**(2*k+4)
    u = ((1+Q//2)*pow(3**(r-1), -1, Q)) % Q
    u += Q*((pow(2**r, -1, 3)-u)*pow(Q, -1, 3) % 3)
    U = 3*Q
    nA, nB = 2**r*U, 2**r*u-1
    mA = 3**(r+k)*U//2**(2*k+3)
    mB = 3**(k+1)*(3**(r-1)*u-1)//2**(2*k+3)
    require(nA > mA, 'family slope must decrease')
    if nB <= mB:
        shift = (mB-nB)//(nA-mA)+1
        u += U*shift; nB += nA*shift; mB += mA*shift
    words = ['1'*r+'01'*(k+1)+'00', '1']
    return family(kind, [r, k, u, U], [[nA, nB], [mA, mB]], words,
                  strict=int(kind == 'UNBOUNDED'), divisible=1)


def family_rows():
    for k in range(81):
        yield family('TEMPLATE', [k],
                     [[9*2**(2*k+2), 9*2**(2*k+1)+2], [2*3**(k+1), 3**(k+1)]],
                     ['01'*k+'00', '1'])
    for r in range(2, 6):
        for k in range(65):
            yield valuation_family(r, k, 'SHORT_RUN')
    for r in range(5, 81):
        k = 0
        while 3**(r+k) >= 2**(r+2*k+3):
            k += 1
        yield valuation_family(r, k, 'UNBOUNDED')
    for r in (2, 3):
        for s in range(1, 81):
            U = 2**(s+3)
            u = ((2**(s+1)*pow(3**s, -1, 4)-1)*pow(3**r, -1, U)) % U
            forms = [[2**r*U, 2**r*u-1], [3**r*U//4, 3*(3**(r-1)*u-1)//4]]
            yield family('RESTART_FAMILY', [r, s, u, U], forms,
                         ['1'*r+'0'+'1'*s+'00', '1'*(s-1)+'01'])


def dumps(row):
    return json.dumps(row, sort_keys=True, separators=(',', ':'))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--full', type=Path, required=True)
    parser.add_argument('--summary', type=Path, required=True)
    parser.add_argument('--parent', type=Path, default=Path(__file__).resolve().parents[1]/'universal-finite-synchronization/run.py')
    args = parser.parse_args()
    old = load_parent(args.parent)
    counts = Counter(); digest = hashlib.sha256(); baseline_hash = hashlib.sha256()
    with args.full.open('wb') as stream:
        def emit(row):
            data = (dumps(row)+'\n').encode(); stream.write(data); digest.update(data)
            counts['rows'] += 1; counts['kind_'+row['kind']] += 1
        for row in family_rows():
            emit(row)
        for n in range(2, LIMIT+1):
            base = baseline(n, old)
            baseline_hash.update((dumps([n, base])+'\n').encode())
            result = base if base['status'] == 'MERGE' else new_selector(n)
            counts['baseline_'+base['status']] += 1
            counts['final_'+result['status']] += 1
            if base['status'] != 'MERGE' and result['status'] == 'MERGE':
                counts['added_'+result['method']] += 1
                counts['added_strict'] += result['strict']
            if result['status'] == 'OUTSIDE':
                counts['outside_'+result['stop']] += 1
            emit(dict(kind='SOURCE', n=n, baseline=base, result=result))
    summary = dict(schema=1, source_range=[2, LIMIT], scan_horizon=HORIZON,
                   counts=dict(sorted(counts.items())), sha256=digest.hexdigest(),
                   baseline_sha256=baseline_hash.hexdigest(), parent_blob=PARENT_BLOB)
    args.summary.write_text(json.dumps(summary, sort_keys=True, indent=2)+'\n')
    print(dumps(summary))


if __name__ == '__main__':
    main()
