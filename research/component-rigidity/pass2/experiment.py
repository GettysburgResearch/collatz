#!/usr/bin/env python3
"""Exact residue-locked inverse geometry. Standard library; no convergence claims.

Produces compact recipe certificates: clocks, original-source links, finite
rational net inputs and replayable windows. Huge integers are regenerated,
not replaced by floating-point logarithms or printed as enormous decimals.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def nat(x: int, minimum: int = 0) -> None:
    require(type(x) is int and x >= minimum, 'integer/type constraint')


def modulus(p: int, q: int) -> tuple[int, int]:
    require(type(p) is int and p in (3, 5), 'only proved multipliers 3 and 5')
    nat(q, 1)
    return p**q, (p-1)*p**(q-1)


def discrete_log(a: int, p: int, q: int) -> int:
    """Exact digit lift; 2 is primitive modulo 3^q and 5^q."""
    m, period = modulus(p, q)
    nat(a)
    require(a % p != 0, 'unit required')
    e = next(j for j in range(p-1) if pow(2, j, p) == a % p)
    small_m, small_period = p, p-1
    for _ in range(1, q):
        small_m *= p
        candidates = [e+j*small_period for j in range(p)
                      if pow(2, e+j*small_period, small_m) == a % small_m]
        require(len(candidates) == 1, 'unique digit lift')
        e = candidates[0]
        small_period *= p
    require(0 <= e < period and pow(2, e, m) == a % m, 'discrete log identity')
    return e


def step(n: int, p: int = 3) -> int:
    nat(n, 1)
    require(type(p) is int and p in (3, 5), 'multiplier')
    return (p*n+1)//2 if n & 1 else n//2


def advance(n: int, clock: int, p: int = 3) -> int:
    nat(clock)
    for _ in range(clock):
        n = step(n, p)
    return n


def anchor(n: int, p: int, q: int, r: int) -> dict:
    nat(n, 1)
    m, period = modulus(p, q)
    nat(r, 1)
    require(r < m and r % p, 'residue must be a canonical unit')
    target, original_clock = n, 0
    if n % p == 0:
        while target % 2 == 0:
            target //= 2
            original_clock += 1
        target = step(target, p)
        original_clock += 1
    s = discrete_log(r*pow(target, -1, m) % m, p, q)
    if (target << s) < 2:
        s += period
    seed = target << s
    require(seed % m == r and seed >= 2, 'seed')
    require(seed <= ((p+1)//2)*(1 << period)*n, 'uniform seed bound')
    return {'source': n, 'target': target, 'original_clock': original_clock,
            'seed_doublings': s, 'seed': seed}


def locked_step(y: int, p: int, q: int, r: int) -> tuple[int, int]:
    m, period = modulus(p, q)
    nat(y, 2)
    require(type(r) is int and 1 <= r < m and r % p and y % m == r, 'locked residue')
    big_m, big_period = p*m, p*period
    k = discrete_log((p*r+1)*pow(y, -1, big_m) % big_m, p, q+1)
    minimum = p.bit_length()
    while k < minimum:
        k += big_period
    z = ((1 << k)*y-1)//p
    require(p*z+1 == (1 << k)*y and z % m == r and z & 1, 'inverse identity')
    require(4*z >= 5*y and z < (1 << k)*y, 'growth')
    return z, k


def rotation_residue(p: int, q: int, r: int) -> int:
    m, _ = modulus(p, q)
    return discrete_log((p*r+1)*pow(r, -1, m) % m, p, q)


def normalize(x: F, period: int) -> F:
    """Representative modulo powers of 2^period, using only exact integers."""
    nat(period, 1)
    require(x > 0, 'positive phase')
    a, b = x.numerator, x.denominator
    exponent = a.bit_length()-b.bit_length()
    if exponent >= 0:
        if a < b << exponent:
            exponent -= 1
    elif a << (-exponent) < b:
        exponent -= 1
    exponent = period*(exponent//period)
    answer = x/F(1 << exponent) if exponent >= 0 else x*(1 << (-exponent))
    require(1 <= answer < 1 << period, 'normalized representative')
    return answer


def ideal_gap(p: int, q: int, r: int, depth: int) -> F:
    _, period = modulus(p, q)
    kappa = rotation_residue(p, q, r)
    x, ratio = F(1), F(1 << kappa, p)
    points = []
    for _ in range(depth+1):
        points.append(x)
        x = normalize(x*ratio, period)
    points = sorted(set(points))
    return max([v/u for u, v in zip(points, points[1:])]
               + [(1 << period)*points[0]/points[-1]])


def integer_hash(n: int) -> str:
    nat(n)
    return hashlib.sha256(n.to_bytes(max(1, (n.bit_length()+7)//8), 'big')).hexdigest()


def net_input(p: int, q: int, r: int, depth: int) -> dict:
    _, period = modulus(p, q)
    burn = 32
    gap = ideal_gap(p, q, r, depth)
    loss = F(5, 8)*F(4, 5)**burn
    target = F(21, 20)
    require(gap/(1-loss) < target, 'universal perturbed net target')
    kmax = p*period+p.bit_length()-1
    return {'p': p, 'q': q, 'r': r, 'period': period,
            'kappa': rotation_residue(p, q, r), 'burn': burn, 'depth': depth,
            'ratio': [21, 20], 'ideal_gap': [gap.numerator, gap.denominator],
            'threshold_prefactor': (p+1)//2,
            'threshold_binary_exponent': period+kmax*(burn+depth)}


def find_windows(seed: int, clocks: list[int], p: int, period: int,
                 burn: int, last: int, count: int = 8) -> list[dict]:
    pending = set(range(count))
    out = []
    y = seed
    for j in range(len(clocks)+1):
        if j >= burn:
            for w in sorted(pending):
                x = last*(17+w)//16+w*w
                t = period*max(0, (x.bit_length()-y.bit_length())//period)
                z = y << t
                if z < x:
                    t += period
                    z <<= period
                if 20*z <= 21*x:
                    out.append({'window_id': w, 'index': j, 'doublings': t,
                                'root_sha256': integer_hash(z)})
                    pending.remove(w)
        if j < len(clocks):
            y = ((1 << clocks[j])*y-1)//p
    require(not pending, 'net missed a relative window')
    return sorted(out, key=lambda item: item['window_id'])


def make_source_net(n: int, spec: dict) -> dict:
    p, q, r = (spec[k] for k in ('p', 'q', 'r'))
    row = anchor(n, p, q, r)
    y = row['seed']
    clocks = []
    for _ in range(spec['burn']+spec['depth']):
        y, k = locked_step(y, p, q, r)
        clocks.append(k)
    row.update({'p': p, 'q': q, 'r': r, 'clocks': clocks,
                'last_node_bits': y.bit_length(), 'last_node_sha256': integer_hash(y),
                'windows': find_windows(row['seed'], clocks, p, spec['period'], spec['burn'], y)})
    return row


def verify_gate(a: int, length: int, offsets: list[int], words: list[str],
                odd_count: int, intercept: int) -> None:
    """All-parameter physical gate verification with integer affine forms."""
    require(len(offsets) == len(words), 'gate inventory')
    for d, word in zip(offsets, words):
        slope, value = 1 << length, a+d
        require(len(word) == length, 'word length')
        for bit in word:
            require(bit in '01' and slope % 2 == 0 and value % 2 == int(bit), 'uniform parity')
            if bit == '1':
                slope, value = 3*slope//2, (3*value+1)//2
            else:
                slope, value = slope//2, value//2
        require((slope, value) == (3**odd_count, intercept), 'whole-cylinder endpoint')


def block_windows(row: dict) -> list[dict]:
    """The credited four-way gate B=388,M=2048,A=243,e=47."""
    require((row['p'], row['q'], row['r']) == (3, 5, 47), 'block net residue')
    targets = {hit['index']: [] for hit in row['windows']}
    for hit in row['windows']:
        targets[hit['index']].append(hit)
    y, chosen = row['seed'], {}
    for j in range(len(row['clocks'])+1):
        if j in targets:
            chosen[j] = y
        if j < len(row['clocks']):
            y = ((1 << row['clocks'][j])*y-1)//3
    last = y
    out = []
    for hit in row['windows']:
        w = hit['window_id']
        left_y = last*(17+w)//16+w*w
        endpoint = chosen[hit['index']] << hit['doublings']
        require((endpoint-47) % 243 == 0, 'transplant integrality')
        t = (endpoint-47)//243
        start = 388+2048*t
        # X=ceil(phi(left_y)), with phi(y)=388+2048*(y-47)/243.
        left = (243*388+2048*(left_y-47)+242)//243
        require(left <= start and 10*(start+3) <= 11*left, 'four-block relative placement')
        out.append({'window_id': w, 'start_sha256': integer_hash(start),
                    'start_bits': start.bit_length()})
    return out


def bounded_checks() -> dict:
    digest = hashlib.sha256()
    edges = literal_steps = residues = 0
    # Exhaust every input residue type at these finite precisions.
    for p, maxq in ((3, 7), (5, 4)):
        for q in range(1, maxq+1):
            m, period = modulus(p, q)
            for r in range(1, m):
                if r % p == 0:
                    continue
                kap = rotation_residue(p, q, r)
                for lift in range(p):
                    y = r+lift*m
                    if y < 2:
                        y += p*m
                    z, k = locked_step(y, p, q, r)
                    require(k % period == kap, 'constant clock residue')
                    require(z % m == r and p*z+1 == y << k, 'residue input class')
                    residues += 1
    # Fixed original-source grids; every displayed edge literally replayed.
    for p, precisions, sources in ((3, (1, 2, 3), range(1, 65)),
                                  (5, (1, 2), (1, 5, 13, 17))):
        for q in precisions:
            m, period = modulus(p, q)
            for r in range(1, m):
                if r % p == 0:
                    continue
                for n in sources:
                    row = anchor(n, p, q, r)
                    require(advance(n, row['original_clock'], p) == row['target'], 'original link')
                    require(advance(row['seed'], row['seed_doublings'], p) == row['target'], 'seed link')
                    y = row['seed']
                    for j in range(24):
                        z, k = locked_step(y, p, q, r)
                        x = z
                        for t in range(k):
                            require(x % 2 == (1 if t == 0 else 0), 'literal physical word')
                            x = (p*x+1)//2 if x % 2 else x//2
                        require(x == y, 'literal endpoint')
                        digest.update(f'{p},{q},{r},{n},{j},{k},{z:x}\n'.encode())
                        edges += 1
                        literal_steps += k
                        y = z
    verify_gate(4, 3, [0, 1], ['001', '100'], 1, 2)
    verify_gate(388, 11, list(range(4)),
                ['00101011100', '10001011100', '01100011100', '11101000001'], 5, 47)
    cycles = [[1, 3, 8, 4, 2], [13, 33, 83, 208, 104, 52, 26]]
    for cycle in cycles:
        require(all(step(a, 5) == b for a, b in zip(cycle, cycle[1:]+cycle[:1])), '5x+1 cycle')
    require(not set(cycles[0]) & set(cycles[1]), 'distinct control cycles')
    # Isolated exterior vertices: explicit legal finite colorings, not global ones.
    local = []
    for h in (64, 256, 1024, 4096, 16384):
        ones = {n for n in range(1, h) if n % 6 in (1, 3) and 3*n > 2*h}
        require(all(((n in ones) == (step(n) in ones))
                    for n in range(1, h+1) if step(n) <= h), 'open-boundary coloring')
        v = sum((n in ones) != (n+1 in ones) for n in range(h//2, h))
        require(v == 2*len(ones), 'isolated exterior variation')
        local.append({'height': h, 'isolated_ones': len(ones), 'last_shell_variation': v})
    rejected = 0
    bad_calls = [lambda: anchor(True,3,1,1), lambda: anchor(0,3,1,1),
                 lambda: anchor(1,3,2,3), lambda: locked_step(4,3,1,2),
                 lambda: discrete_log(0,3,2), lambda: modulus(7,1),
                 lambda: modulus(3,True), lambda: verify_gate(4,3,[0,1],['001','101'],1,2)]
    for call in bad_calls:
        try:
            call()
        except ValueError:
            rejected += 1
    require(rejected == len(bad_calls), 'direct negative controls')
    return {'residue_types': residues, 'literal_inverse_edges': edges,
            'literal_shortcut_steps': literal_steps, 'gate_families': 2,
            'open_boundary_examples': local, 'negative_controls': rejected,
            'semantic_sha256': digest.hexdigest()}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('certificates.json'))
    args = parser.parse_args()
    specs = [net_input(*x) for x in [(3,1,1,64),(3,1,2,64),(3,2,1,256),
             (3,2,8,256),(3,3,1,512),(3,3,26,512),(3,5,47,4096),
             (5,1,1,256)]]
    sources = [1,27,121,303,1311,2**127-1,27,13]
    rows = [make_source_net(n,spec) for n,spec in zip(sources,specs)]
    payload = {'schema': 'component-rigidity-locked-1',
               'status': 'PROPOSED proofs; finite exact recipe certificates only',
               'net_inputs': specs, 'source_nets': rows,
               'four_block_windows': block_windows(rows[6]), 'bounded_checks': bounded_checks()}
    args.output.write_text(json.dumps(payload, sort_keys=True, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'bounded_checks': payload['bounded_checks'], 'source_nets': len(rows),
                      'net_inverse_edges': sum(len(r['clocks']) for r in rows),
                      'window_witnesses': sum(len(r['windows']) for r in rows),
                      'four_blocks': len(payload['four_block_windows']),
                      'largest_node_bits': max(r['last_node_bits'] for r in rows)}, indent=2))


if __name__ == '__main__':
    main()
