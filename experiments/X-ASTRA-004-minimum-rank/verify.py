#!/usr/bin/env python3
"""Separate physical-step replay. Imports neither run.py nor repository modules."""
from __future__ import annotations
import argparse
import copy
import hashlib
import json
from collections import Counter, deque
from fractions import Fraction
from pathlib import Path


def v(n: int, p: int) -> int:
    assert n != 0
    power, e = p, 0
    while n % power == 0:
        power *= p
        e += 1
    return e


def weight(n: int) -> int:
    assert n > 0 and (n-1) % 3 == 0
    z = 2*n+1
    unit = z//3**v(z, 3)
    return z*unit


def step(n: int) -> int:
    return n//2 if n % 2 == 0 else (3*n+1)//2


def section(n: int) -> tuple[int, str]:
    if n == 1:
        return 1, ""
    x, bits = n, []
    for _ in range((2*n+1).bit_length()+2):
        bits.append(str(x % 2))
        x = step(x)
        if x % 3 == 1:
            return x, ''.join(bits)
    raise AssertionError("return-length bound failed")


def back(y: int) -> list[int]:
    if y == 1:
        return [4]
    out, x = [], 2*y
    while x % 3 == 2:
        out.append(2*x)
        x = (2*x-1)//3
    if x % 3 == 1:
        out.append(x)
    return out


def follow(n: int, word: str) -> int:
    for b in word:
        assert b in '01' and n % 2 == int(b)
        n = step(n)
    return n


def sha(x: object) -> str:
    return hashlib.sha256(json.dumps(x, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def reduce(n: int) -> tuple[str, int, str, str]:
    h, y = v(2*n+1, 3), section(n)[0]
    if h == 1:
        return 'height_one', y, section(n)[1], ''
    if n % 2 == 0:
        return 'even_merge', (n-1)//3, '0', '1'
    if weight(y) < weight(n):
        return 'forward', y, section(n)[1], ''
    odd_parents = [x for x in back(n) if x % 2]
    if odd_parents and weight(odd_parents[0]) < weight(n):
        x = odd_parents[0]
        return 'inverse', x, '', section(x)[1]
    if h == 2 and n % 4 == 1:
        x, w2 = section(y)
        return 'depth_two_forward', x, section(n)[1]+w2, ''
    if h == 2 and n % 16 == 3:
        return 'depth_two_merge', (3*n-1)//8, '1100', '1'
    if v(128*n-71, 3) >= 9:
        return 'reverse_six', (64*n-49)//27, '', '100110'
    return 'residual', 0, '', ''


def local_path(n: int, limit: int) -> list[int] | None:
    queue, used = deque([[n]]), {n}
    while queue:
        path = queue.popleft()
        if len(path)-1 >= limit:
            continue
        for x in [section(path[-1])[0]]+back(path[-1]):
            if x in used:
                continue
            used.add(x)
            extended = path+[x]
            if weight(x) < weight(n):
                return extended
            queue.append(extended)
    return None


def join_words(n: int, x: int) -> tuple[str, str, int]:
    left = {n: ''}
    y, w = n, ''
    for _ in range(4):
        if y == 1:
            break
        y, add = section(y)
        w += add
        left.setdefault(y, w)
    y, w = x, ''
    for _ in range(5):
        if y in left:
            return left[y], w, y
        y, add = section(y)
        w += add
    raise AssertionError('no merging point')


def affine_check(word: str) -> tuple[Fraction, Fraction]:
    mul, add = Fraction(1), Fraction(0)
    for b in word:
        if b == '1':
            mul, add = 3*mul/2, (3*add+1)/2
        else:
            mul, add = mul/2, add/2
    return mul, add


def make_tile(n: int, x: int) -> dict:
    wn, wx, meet = join_words(n, x)
    j, k, qn, qx = len(wn), len(wx), wn.count('1'), wx.count('1')
    hn, hx = v(2*n+1, 3), v(2*x+1, 3)
    mn, mx = 2**j*3**qx, 2**k*3**qn
    while mn % 3**(hn+1) or mx % 3**(hx+1):
        mn *= 3
        mx *= 3
    cn, bn = affine_check(wn)
    cx, bx = affine_check(wx)
    assert cn*n+bn == cx*x+bx == meet and cn*mn == cx*mx
    s = Fraction(mx, mn)**2*Fraction(3**hn, 3**hx)
    assert s <= 1 and weight(x) < weight(n)
    for t in [0, 1, 7, 1000, 10**30]:
        nn, xx = n+mn*t, x+mx*t
        assert follow(nn, wn) == follow(xx, wx)
        assert (v(2*nn+1, 3), v(2*xx+1, 3)) == (hn, hx)
        assert weight(xx) < weight(nn)
    return dict(n=n, x=x, wn=wn, wx=wx, meeting=meet, hn=hn, hx=hx,
                period_n=mn, period_x=mx, slope=[s.numerator, s.denominator])


def inv_mod(a: int, m: int) -> int:
    # Extended Euclid, rather than the generator's modular pow.
    old_r, r, old_s, s = a, m, 1, 0
    while r:
        q = old_r//r
        old_r, r, old_s, s = r, old_r-q*r, s, old_s-q*s
    assert old_r == 1
    return old_s % m


def reconstruct() -> dict:
    rows, residual, cnt = [], [], Counter()
    h2_total = h2_left = 0
    residues = [139, 427, 571, 859, 1003]
    for n in range(4, 262145, 3):
        tag, x, wn, wx = reduce(n)
        cnt[tag] += 1
        if x:
            assert weight(x) < weight(n) and follow(n, wn) == follow(x, wx)
        else:
            residual.append(n)
        if v(2*n+1, 3) == 2:
            h2_total += 1
            assert (tag == 'residual') == (n % 1296 in residues)
            h2_left += tag == 'residual'
        rows.append([n, tag, x, wn, wx])
    core = dict(cutoff=262144, source_count=len(rows), counts=dict(sorted(cnt.items())),
                h2_count=h2_total, h2_residual=h2_left, row_sha256=sha(rows),
                first_residuals=residual[:20])
    fans = []
    for y in range(4, 388, 3):
        # All first-return sources are <=4y; no empirical cutoff is used.
        xs = [x for x in range(4, 4*y+1, 3) if section(x)[0] == y]
        assert xs == sorted(back(y))
        fans.append([y, xs])
    fan = dict(endpoints=len(fans), sources=sum(len(z[1]) for z in fans), rows_sha256=sha(fans))
    families, steps = [], 0
    heights, horizons = [6, 7, 12, 24, 64], [1, 2, 3, 8, 16, 32, 64]
    for H in heights:
        for L in horizons:
            m2, m3 = 2**(3*L+1), 3**(H+4)
            r2 = (2**(3*L)-5) % m2
            r3 = (71+3**(H+3))*inv_mod(128, m3) % m3
            residue = r2+m2*((r3-r2)*inv_mod(m2, m3) % m3)
            for t in [0, 1]:
                n = residue+(t+1)*m2*m3
                x = (64*n-49)//27
                assert n % m2 == r2 and n % m3 == r3
                assert v(n+5, 2) == 3*L and v(2*x+1, 3) == H
                assert x > n and 4*weight(x) < weight(n)
                assert follow(x, '100110') == n
                assert section(section(x)[0])[0] == n
                assert v(2*n+1, 3) == 3 and v(128*n-71, 3) == H+3
                assert all(weight(z) >= weight(n) for z in [section(n)[0]]+back(n)+back(section(n)[0]))
                y = n
                for i in range(1, L+1):
                    assert v(y+1, 2) == 2
                    y = section(y)[0]
                    assert 8**i*(y+5) == 9**i*(n+5)
                    assert y > n and weight(y) > 3*weight(n)
                    steps += 1
                families.append([H, L, t, n, x, y])
    family = dict(heights=heights, horizons=horizons, lifts=[0, 1], rows=len(families),
                  forward_returns=steps, rows_sha256=sha(families), example=families[0])
    sr, sc, tiles = [], Counter(), []
    for n in residual[:1024]:
        path = local_path(n, 4)
        y, forward = n, 0
        for d in range(1, 5):
            y = section(y)[0]
            if weight(y) < weight(n):
                forward = d
                break
        if path is None:
            verdict = 'unresolved_at_depth_4'
        elif forward:
            verdict = 'forward_also'
        else:
            verdict = 'two_sided_only'
            tiles.append(make_tile(n, path[-1]))
        sc[verdict] += 1
        sr.append([n, forward, path, verdict])
    assert local_path(121, 8) is None
    z = 121
    for d in range(1, 17):
        z = section(z)[0]
        assert (weight(z) < weight(121)) == (d == 16)
    assert z == 40
    bounds = dict(quarter=[4096, 19683], h2_high_a=[3888, 3969], h2_double_one=[361, 363],
                  h2_second_long=[Fraction(81*98**2, 256*63**2).numerator,
                                  Fraction(81*98**2, 256*63**2).denominator])
    assert all(Fraction(*z) < 1 for z in bounds.values()) and 4*4096 < 19683
    return dict(schema=1, scope='finite_exact_support_not_Collatz_closure',
                parent='345168de8732f6240e5c926420cee3db3b0fa137',
                residues_mod_1296=residues, core=core, fan=fan, family=family,
                rational_bounds=bounds,
                search=dict(sources=1024, radius=4, counts=dict(sorted(sc.items())),
                            row_sha256=sha(sr), unresolved_radius_8=121,
                            first_forward_drop_121=[16, 40]),
                lift_parameters=[0, 1, 7, 1000, 10**30], tiles=tiles)


def validate(report: dict, expected: dict) -> None:
    assert set(report) == {'payload', 'sha256'}
    assert report['sha256'] == sha(report['payload']), 'bad seal'
    assert report['payload'] == expected, 'physical replay or scope mismatch'


def self_test(report: dict, expected: dict) -> None:
    mutations = [lambda p: p['tiles'].pop(),
                 lambda p: p.update(scope='all_sources_all_depth_Collatz_proved'),
                 lambda p: p['core'].update(cutoff=1024),
                 lambda p: p['family']['horizons'].pop(),
                 lambda p: p['tiles'][0].update(x=p['tiles'][0]['x']+1),
                 lambda p: p['tiles'][0].update(period_x=p['tiles'][0]['period_x']+2)]
    for mutate in mutations:
        bad = copy.deepcopy(report)
        mutate(bad['payload'])
        bad['sha256'] = sha(bad['payload'])
        try:
            validate(bad, expected)
        except AssertionError:
            continue
        raise AssertionError('resealed false report accepted')
    print('REJECTED 6 RESEALED TAMPER CASES')


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('report', type=Path)
    p.add_argument('--self-test', action='store_true')
    args = p.parse_args()
    if not __debug__:
        raise RuntimeError('run without -O')
    report = json.loads(args.report.read_text())
    expected = reconstruct()
    validate(report, expected)
    if args.self_test:
        self_test(report, expected)
    print('INDEPENDENT IMPLEMENTATION REPLAY PASS', sha(expected))


if __name__ == '__main__':
    main()
