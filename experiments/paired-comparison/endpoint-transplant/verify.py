#!/usr/bin/env python3
"""Independent EPT verifier. Imports no generator or repository modules.
Negative inverse outcomes and earliest selector decisions are checked by
exhaustive FORWARD enumeration of all roots below the ORIGINAL source cap.
"""
import argparse
from collections import Counter
from copy import deepcopy
import hashlib
import json
from pathlib import Path


def check(ok, text):
    if not ok:
        raise ValueError(text)


def types(value):
    if type(value) is dict:
        for k, v in value.items():
            check(type(k) is str, 'key type')
            types(v)
    elif type(value) is list:
        for v in value:
            types(v)
    else:
        check(value is None or type(value) in (int, str), 'value type')


def object_pairs(pairs):
    obj = {}
    for k, v in pairs:
        check(k not in obj, 'duplicate JSON key')
        obj[k] = v
    return obj


def load(text):
    obj = json.loads(text, object_pairs_hook=object_pairs)
    types(obj)
    return obj


def walk(source, word):
    check(type(source) is int and source > 0, 'positive root')
    check(type(word) is str and set(word) <= {'0', '1'}, 'binary word')
    minimum = source
    for ch in word:
        p = source % 2
        check(p == int(ch), 'actual parity')
        source = source//2 if p == 0 else (source*3+1)//2
        minimum = min(minimum, source)
    return source, minimum


def blocks(word):
    return sum(ch == '1' and (i == 0 or word[i-1] == '0')
               for i, ch in enumerate(word))


class Verifier:
    def __init__(self):
        self.gates = {}
        self.current_cap = None
        self.reachable = {}

    def forward(self, cap):
        if cap != self.current_cap:
            check(2 <= cap <= 4096, 'finite experiment cap')
            reachable = {}
            for root in range(1, cap):
                x, used, last_odd = root, 0, False
                while True:
                    if x not in reachable or used < reachable[x]:
                        reachable[x] = used
                    odd = x % 2 == 1
                    new_used = used+int(odd and not last_odd)
                    if new_used > 3:
                        break
                    x = (x*3+1)//2 if odd else x//2
                    used, last_odd = new_used, odd
            self.current_cap, self.reachable = cap, reachable
        return self.reachable

    def witness(self, row, cap, x, budget):
        m, word = row['source'], row['word']
        check(type(m) is int and 0 < m < cap, 'immutable original cap')
        check(blocks(word) <= budget, 'odd-block budget')
        check(walk(m, word)[0] == x, 'witness endpoint')

    def row(self, r):
        types(r)
        kind = r['kind']
        if kind == 'gate':
            offsets, b, length, q, e = (r[k] for k in ('offsets', 'B', 'L', 'Q', 'e'))
            check(len(offsets) >= 2 and len(offsets) == len(set(offsets)) and
                  all(type(x) is int and x >= 0 for x in offsets), 'offset pattern')
            check(length > 0 and q > 0 and e > 0 and e % 3 != 0, 'gate dimensions')
            modulus = 2**length
            check(0 <= b < modulus and len(r['words']) == len(offsets), 'gate residue')
            check(r['t_min'] == max(0, (1-b-min(offsets)+modulus-1)//modulus), 'positive tail')
            for offset, word in zip(offsets, r['words']):
                check(len(word) == length, 'uniform clock')
                a, c = modulus, b+offset
                for ch in word:
                    check(ch in '01' and a % 2 == 0 and c % 2 == int(ch), 'whole-cell parity')
                    if ch == '1':
                        a, c = 3*a, 3*c+1
                    a, c = a//2, c//2
                check((a, c) == (3**q, e), 'whole affine identity')
            self.gates[tuple(offsets)] = r
        elif kind == 'log':
            q, k, period, u = (r[k] for k in ('Q', 'k', 'period', 'unit'))
            check(1 <= q <= 64 and period == 2*3**(q-1), 'multiplicative order')
            check(0 <= k < period and 0 < u < 3**q and u % 3, 'log domain')
            check(pow(2, k, 3**q) == u, 'discrete logarithm')
        elif kind == 'transplant':
            g = self.gates[tuple(r['gate_offsets'])]
            n, y, k, k0 = (r[k] for k in ('n', 'y', 'k', 'k0'))
            check(n > 0 and r['minimum'] > 0 and y % 3 != 0, 'transplant target')
            z, expected_prefix = n, ''
            while z % 3 == 0:
                expected_prefix += str(z % 2)
                z = z//2 if z % 2 == 0 else (3*z+1)//2
            check(z == y and r['prefix'] == expected_prefix, 'first ternary-unit target')
            order = 2*3**(g['Q']-1)
            check(r['period'] == order and 0 <= k0 < order, 'transplant order')
            check(k >= 0 and k % order == k0 and
                  pow(2, k0, 3**g['Q'])*y % (3**g['Q']) == g['e'] % (3**g['Q']), 'target residue')
            mod = 2**g['L']
            tmin = max(g['t_min'], (r['minimum']-g['B']-min(g['offsets'])+mod-1)//mod)
            threshold = 3**g['Q']*tmin+g['e']
            km = r['k_min']
            check(km >= 0 and y*2**km >= threshold and
                  (km == 0 or y*2**(km-1) < threshold), 'height threshold')
            check(r['t_min'] == tmin and km <= k < km+order, 'least admissible lift')
            check(r['t'] >= tmin and 3**g['Q']*r['t']+g['e'] == y*2**k, 'transplanted endpoint')
            check(r['start'] == g['B']+mod*r['t'], 'original sources')
            for d, word in zip(g['offsets'], g['words']):
                source = r['start']+d
                check(source >= r['minimum'], 'requested lower threshold')
                check(walk(source, word+'0'*k)[0] == y, 'pure ancestor path')
        elif kind == 'query':
            cap, x, b = r['cap'], r['X'], r['blocks']
            check(2 <= cap <= 128 and 1 <= x <= 256 and 0 <= b <= 3, 'query inventory range')
            exists = self.forward(cap).get(x, 4) <= b
            check(exists == (r['source'] is not None), 'complete forward inverse cross-check')
            if exists:
                self.witness(r, cap, x, b)
            else:
                check(r['word'] is None, 'negative outcome word')
        elif kind == 'selected':
            n, b, horizon = r['n'], r['blocks'], r['horizon']
            check(2 <= n <= 4096 and 0 <= b <= 3 and horizon == 8, 'selector inventory range')
            reachable = self.forward(n)
            x, prefix, low, first = n, '', n+1, None
            for a in range(1, horizon+1):
                prefix += str(x % 2)
                x = x//2 if x % 2 == 0 else (3*x+1)//2
                low = min(low, x)
                if reachable.get(x, 4) <= b:
                    first = a
                    break
            check((r['X'], r['prefix'], r['minimum'], r['a']) == (x, prefix, low, first), 'earliest actual endpoint')
            check(r['status'] == ('OUTSIDE' if first is None else 'MERGER'), 'selector outcome')
            if first is not None:
                self.witness(r, n, x, b)
            else:
                check(r['source'] is None and r['word'] is None, 'retained failure')
        elif kind == 'ternary':
            s, b, n, m = r['s'], r['b'], r['n'], r['source']
            check(s >= 6 and b > 0 and b % 2 == 1, 'ternary family domain')
            check(8*n+3 == 3**s*b and m+1 == 2**s*b, 'ternary family equations')
            check(n % 4 == 3 and n % 3 == 0 and 0 < m < n, 'original root constraints')
            check(r['word'] == '1'*s+'0100', 'ternary physical word')
            check(walk(n, '1')[0] == r['X'] == walk(m, r['word'])[0], 'one-step merger')
            check(3**s*m < 8*2**s*n, 'compression factor')
        elif kind == 'cap':
            cap, q = r['cap'], r['R']
            check(2**q <= cap < 2**(q+1) and q >= 1, 'dyadic cap')
            maximum = max(3**r*(cap//2**r) for r in range(1, q+1))-1
            check(r['endpoint_max'] == maximum == 3**q-1, 'sharp endpoint maximum')
        else:
            raise ValueError('unknown kind')


def inventory(r):
    k = r['kind']
    if k == 'gate': return k, tuple(r['offsets'])
    if k == 'log': return k, r['Q'], r['unit']
    if k == 'transplant': return k, r['n'], tuple(r['gate_offsets']), r['minimum']
    if k == 'query': return k, r['cap'], r['X'], r['blocks']
    if k == 'selected': return k, r['n'], r['blocks']
    if k == 'ternary': return k, r['s'], r['b']
    return k, r['cap']


def expected_inventory():
    expect = Counter()
    patterns = [tuple(range(k)) for k in range(2, 13)]
    patterns += [(0, a, b) for a in range(1, 9) for b in range(a+1, 13)]
    patterns += [(9, 0, 5, 2), (0, 3, 9, 27, 81), (0, 2**64+3)]
    expect.update(('gate', p) for p in patterns)
    for q in range(1, 65):
        order = 2*3**(q-1)
        expect.update(('log', q, pow(2, k, 3**q)) for k in {0, 1, order//2, order-1})
    expect.update(('transplant', n, tuple(range(k)), n+1) for n in range(1, 513) for k in (2, 3, 4))
    expect.update(('transplant', n, (0, 1, 2, 3), 10**30) for n in (3, 27, 71, 155, 641))
    expect.update(('query', n, x, b) for n in range(2, 129) for b in range(4) for x in range(1, 257))
    expect.update(('selected', n, b) for n in range(2, 4097) for b in range(4))
    for s in list(range(6, 65))+[96, 128]:
        residue = next(b for b in range(1, 32, 2) if (3**s*b) % 32 == 27)
        expect.update(('ternary', s, residue+32*t) for t in (0, 1, 17))
    expect.update(('cap', max(n, 2)) for n in (1, 2, 3, 4, 5, 17, 71, 273, 4647))
    return expect


def self_test(v, samples):
    mutations = [('gate','e',lambda x:x+1), ('gate','B',lambda x:x+1),
                 ('gate','Q',lambda x:x+1), ('gate','L',lambda x:x+1),
                 ('log','k',lambda x:x+1), ('log','period',lambda x:x+2),
                 ('log','unit',lambda x:3), ('transplant','y',lambda x:x+3),
                 ('transplant','start',lambda x:x+1), ('transplant','k',lambda x:x+1),
                 ('transplant','period',lambda x:x+1), ('transplant','minimum',lambda x:10**200),
                 ('positive_query','source',lambda x:10**9),
                 ('negative_query','source',lambda x:1),
                 ('selected','a',lambda x:None), ('selected','source',lambda x:10**9),
                 ('ternary','n',lambda x:x+2), ('ternary','source',lambda x:x+2),
                 ('ternary','s',lambda x:5), ('cap','endpoint_max',lambda x:x+1)]
    rejected = 0
    for kind, field, change in mutations:
        bad = deepcopy(samples[kind])
        bad[field] = change(bad[field])
        try:
            v.row(bad)
        except (ValueError, TypeError, KeyError):
            rejected += 1
        else:
            raise ValueError('accepted semantic mutation '+kind+'/'+field)
    for text in ('{"a":1,"a":2}', '{"a":true}', '{"a":1.0}'):
        try:
            load(text)
        except ValueError:
            rejected += 1
        else:
            raise ValueError('accepted malformed/type JSON')
    return rejected


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('full', type=Path)
    p.add_argument('--summary', type=Path, required=True)
    p.add_argument('--self-test', action='store_true')
    args = p.parse_args()
    v = Verifier()
    digest, counts, inventory_left, samples = hashlib.sha256(), Counter(), expected_inventory(), {}
    outcomes = {str(b): Counter() for b in range(4)}
    with args.full.open('rb') as source:
        for raw in source:
            r = load(raw)
            key = inventory(r)
            check(inventory_left[key] > 0, 'duplicate or unexpected corpus row')
            inventory_left[key] -= 1
            v.row(r)
            digest.update(raw)
            counts[r['kind']] += 1
            sk = r['kind']
            if sk == 'query': sk = 'positive_query' if r['source'] is not None else 'negative_query'
            if sk != 'selected' or r['status'] == 'MERGER': samples.setdefault(sk, deepcopy(r))
            if r['kind'] == 'selected':
                c = outcomes[str(r['blocks'])]
                c[r['status']] += 1
                if r['status'] == 'MERGER' and r['minimum'] > r['n']:
                    c['no_forward_descent'] += 1
                    if r['n'] % 3 == 0: c['no_forward_descent_divisible_by_3'] += 1
    check(not any(inventory_left.values()), 'missing corpus coverage')
    calculated = dict(schema='EPT-1', sha256=digest.hexdigest(), rows=sum(counts.values()),
                      counts=dict(counts), selected={k:dict(c) for k,c in outcomes.items()})
    check(load(args.summary.read_text()) == calculated, 'published summary')
    rejected = self_test(v, samples) if args.self_test else 0
    print(json.dumps(dict(status='PASS', rows=sum(counts.values()), sha256=digest.hexdigest(),
                          rejected_controls=rejected), sort_keys=True))


if __name__ == '__main__':
    main()
