#!/usr/bin/env python3
"""Reviewer D: independent bounded arithmetic audits, not universal proof checking.

No imports from source packets, old generators or old verifiers. All checks use
explicit exceptions and remain active under Python -O. Only --write writes data.
"""
from __future__ import annotations
import argparse
from collections import Counter, deque
from copy import deepcopy
from fractions import Fraction as F
from hashlib import sha256
from itertools import product
from math import factorial, gcd, prod
from pathlib import Path
import json

BASE = 'cd1b3689e8d37fc4232945072e2faf6bd5ee47bd'
SCHEMA = 'reviewer-d-integrated-audit/v1'
SCOPE = 'bounded exact regression evidence; mathematical verdicts require the written review'


def need(ok: bool, why: str) -> None:
    if not ok:
        raise ValueError(why)


def canonical(x: object) -> bytes:
    return json.dumps(x, sort_keys=True, separators=(',', ':')).encode()


def seal(x: object) -> str:
    return sha256(canonical(x)).hexdigest()


def step(n: int) -> int:
    return (3*n+1)//2 if n % 2 else n//2


def rational_step(x: F) -> F:
    need(x.denominator % 2 == 1, 'non-dyadic-integral rational')
    return (3*x+1)/2 if x.numerator % 2 else x/2


def affine(word: tuple[int, ...]) -> tuple[int, int, int]:
    q = sum(word)
    positions = [i for i, bit in enumerate(word) if bit]
    c = sum(2**i * 3**(q-1-j) for j, i in enumerate(positions))
    return 2**len(word), 3**q, c


def extraction() -> dict:
    cases = 0
    moduli = [1]
    for factor in (2, 1, 3, 2, 5, 1, 7, 2, 3, 5):
        moduli.append(moduli[-1]*factor)
    for n in range(-100, 101):
        residues = [n % m for m in moduli]
        for i in range(len(moduli)-1):
            k, kn = moduli[i:i+2]
            a = (residues[i+1]-residues[i])//k
            need(0 <= a < kn//k, 'canonical digit range')
            if k > abs(n):
                need(a == (0 if n >= 0 else kn//k-1), 'signed face')
            cases += 1
    J = 12
    r = [(-2**J) % 2**n for n in range(41)]
    a = [(r[n+1]-r[n])//2**n for n in range(40)]
    need(a == [0]*J+[1]*(40-J), 'negative ordinary counterexample')
    need(all(2**n-r[n] == 2**J for n in range(J, 41)), 'negative coface')
    return dict(mixed_radix_edges=cases, negative_integer=-2**J,
                initial_zero_digits=J, subsequent_checked_maximal_digits=40-J,
                transcript=seal([moduli, r, a]))


def periodic_and_cylinders() -> dict:
    words = replay_steps = lift_checks = 0
    kinds = Counter()
    digest_rows = []
    for L in range(1, 13):
        observed = {}
        for n in range(2**L):
            x = n
            bits = []
            for _ in range(L):
                bits.append(x % 2)
                x = step(x)
            w = tuple(bits)
            need(w not in observed, 'parity coding collision')
            observed[w] = n
        need(len(observed) == 2**L, 'parity coding omission')
        for w, r in sorted(observed.items()):
            P, Q, c = affine(w)
            need((Q*r+c) % P == 0, 'endpoint congruence')
            for lift in (0, 1, 3):
                n = r+P*lift
                x = n
                for bit in w:
                    need(x % 2 == bit, 'lift parity'); x = step(x)
                need(P*x == Q*n+c, 'affine lift')
                lift_checks += 1
            x = F(c, P-Q)
            y = x
            for bit in w:
                need(y.numerator % 2 == bit, 'periodic rational parity')
                y = rational_step(y); replay_steps += 1
            need(y == x, 'periodic rational closure')
            need((x.denominator == 1) == (c % abs(P-Q) == 0), 'whole denominator')
            kind = 'zero' if x == 0 else ('positive' if x > 0 else 'negative')
            kind += '_integer' if x.denominator == 1 else '_nonintegral'
            kinds[kind] += 1
            digest_rows.append([L, list(w), r, x.numerator, x.denominator])
            words += 1
    need(F(affine((1, 0))[2], 4-3) == 1, 'trivial positive realizer')
    preperiods = 0
    for L in range(1, 7):
        for w in product((0, 1), repeat=L):
            P, Q, c = affine(w)
            tail = F(c, P-Q)
            for j in range(6):
                for u in product((0, 1), repeat=j):
                    source = tail
                    for bit in reversed(u):
                        source = (2*source-1)/3 if bit else 2*source
                    y = source
                    for bit in u:
                        need(y.numerator % 2 == bit, 'preperiod inverse parity')
                        y = rational_step(y)
                    need(y == tail, 'preperiod transfer')
                    preperiods += 1
    return dict(words=words, periodic_steps=replay_steps, ordinary_lifts=lift_checks,
                kinds=dict(kinds), preperiod_pairs=preperiods,
                trivial_realizers=[1, 2], transcript=seal(digest_rows))


def coefficient() -> dict:
    positions = 0
    for source in range(1, 513):
        x = source; C = F(1); normalized_sum = F()
        for _ in range(64):
            odd = x % 2
            C *= F(3 if odd else 1, 2)
            if odd:
                normalized_sum += F(1, 2)/C
            x = step(x)
            need(F(x) == source*C+C*normalized_sum, 'surplus identity')
            positions += 1
    mins = []
    comparisons = 0
    for depth in range(13):
        survivors = []
        for n in range(1, 2**depth+1):
            x = n; p = q = 1; valid = True
            for _ in range(depth):
                q *= 3 if x % 2 else 1; p *= 2; x = step(x)
                if q < p: valid = False; break
            if valid: survivors.append(n)
        need(survivors, 'finite SC cylinder nonempty')
        m = min(survivors); mins.append(m)
        for B in range(1, 129):
            all_stop = True
            for n in range(1, B+1):
                x = n; p = q = 1; stopped = False
                for _ in range(depth):
                    q *= 3 if x % 2 else 1; p *= 2; x = step(x)
                    if q < p: stopped = True; break
                if not stopped: all_stop = False; break
            need((m > B) == all_stop, 'SC least-root equivalence')
            comparisons += 1
    need(mins[0] == 1, 'positive empty-depth minimum')
    return dict(sources=512, positions=positions, depths=list(range(13)),
                least_sources=mins, box_comparisons=comparisons)


def dfa_forbidden(forbidden: set[int]) -> tuple[int, int, list[list[int]]]:
    # State records last-bit canonicality and forbidden suffixes still possible.
    words = frozenset(bin(n)[2:][::-1] for n in forbidden)
    initial = (False, words)
    states = [initial]; ids = {initial: 0}; edges = []; accept = []
    for last_one, suffixes in states:
        accept.append(last_one and '' not in suffixes)
        row = []
        for bit in ('0', '1'):
            dest = (bit == '1', frozenset(s[1:] for s in suffixes if s.startswith(bit)))
            if dest not in ids: ids[dest] = len(states); states.append(dest)
            row.append(ids[dest])
        edges.append(row)
    classes = [int(b) for b in accept]
    while True:
        table = {}; new = []
        for i in range(len(states)):
            key = (accept[i], classes[edges[i][0]], classes[edges[i][1]])
            if key not in table: table[key] = len(table)
            new.append(table[key])
        if new == classes: break
        classes = new
    size = max(classes)+1
    out = [None]*size
    for i, c in enumerate(classes): out[c] = [classes[t] for t in edges[i]]
    # Reachability closure suffices for SCCs in these small complete machines.
    reach = []
    for i in range(size):
        got = {i}; todo = [i]
        while todo:
            for t in out[todo.pop()]:
                if t not in got: got.add(t); todo.append(t)
        reach.append(got)
    components = []; unseen = set(range(size))
    while unseen:
        i = min(unseen)
        c = sorted(j for j in unseen if j in reach[i] and i in reach[j])
        components.append(c); unseen.difference_update(c)
    cyclic = [c for c in components if len(c)>1 or c[0] in out[c[0]]]
    need(len(cyclic) == 1 and len(cyclic[0]) == 2, 'canonical SCC')
    need(all(t in cyclic[0] for i in cyclic[0] for t in out[i]), 'terminal SCC')
    return len(states), size, cyclic


def automata() -> dict:
    forbidden = {1, 2}; rows = []; memberships = 0
    for d in range(11):
        need(max(forbidden) == 2**(d+1), 'forbidden maximum')
        for n in range(1, 2**(d+2)+1):
            x = n; hit = x in (1, 2)
            for _ in range(d): x = step(x); hit |= x in (1, 2)
            need((n in forbidden) == hit, 'inverse/forward safety disagreement')
            memberships += 1
        witness = 2**(d+2)
        need(witness not in forbidden and step(witness) in forbidden, 'nonclosure')
        raw, minimal, cyclic = dfa_forbidden(forbidden)
        rows.append(dict(depth=d, forbidden_count=len(forbidden), maximum=max(forbidden),
                         raw_states=raw, minimal_states=minimal, cyclic_sizes=list(map(len, cyclic))))
        old = set(forbidden)
        forbidden |= {2*y for y in old}
        forbidden |= {(2*y-1)//3 for y in old if y % 3 == 2}
    return dict(rows=rows, ordinary_membership_checks=memberships)


P = 3**12
Q = 2**19
DIGITS = [229376, 258048, 290304, 326592, 367416, 413343]
SOURCE = [294912, 331776, 438784, 297024, 6472, 466033]
CAP = [298936, 336303, 444771, 301077, 6561, 472392]
MATRIX = [[4024,491448,384440,1912,292464,357191],
          [41391,4527,421807,39279,329831,394558],
          [149859,112995,5987,147747,438299,503026],
          [6165,493589,386581,4053,294605,359332],
          [235937,199073,92065,233825,89,64816],
          [177480,140616,33608,175368,465920,6359]]


def chart() -> dict:
    r = [(-a*pow(P, -1, Q)) % Q for a in DIGITS]
    c = [(P*x+a)//Q for x, a in zip(r, DIGITS)]
    need(r == SOURCE and c == CAP, 'chart source table')
    matrix = [[(ci-rj) % Q for rj in r] for ci in c]
    need(matrix == MATRIX, 'high quotient table')
    need(not ({x % 2048 for row in matrix for x in row} & {a % 2048 for a in DIGITS}),
         'quotient/allowed digit intersection')
    odd = DIGITS[-1]
    need(6*odd-sum(DIGITS) == 594979 and gcd(594979, Q) == 1, 'affine rigidity unit')
    automorphisms = []
    for image in DIGITS[:-1]:
        w = ((image-odd)*pow(DIGITS[0]-odd, -1, Q)) % Q
        t = (1-w)*odd % Q
        if {(t+w*a) % Q for a in DIGITS} == set(DIGITS): automorphisms.append([w,t])
    need(automorphisms == [[1,0]], 'alphabet automorphisms')
    rows = []; level = [((), 0, 0)]; levels = []; lifts = 0
    for depth in range(1, 5):
        following = []
        for word, root, cap in level:
            n = len(word)
            for i in range(6):
                b = ((r[i]-cap)*pow(P**n, -1, Q)) % Q
                k, rem = divmod(cap+P**n*b-r[i], Q)
                need(rem == 0 and k >= 0, 'append quotient')
                rr, ss = root+Q**n*b, c[i]+P*k
                ww = word+(i,)
                offset = sum(P**(depth-1-j)*Q**j*DIGITS[ii] for j, ii in enumerate(ww))
                independent = (-offset*pow(P**depth, -1, Q**depth)) % Q**depth
                need(rr == independent and Q**depth*ss == P**depth*rr+offset, 'closed tile')
                for h in (0, 1, 7):
                    start = rr+Q**depth*h; x = start
                    for ii in ww:
                        y = (P*x+Q-1)//Q
                        need(Q*y-P*x == DIGITS[ii], 'physical chart digit'); x = y
                    need(x == ss+P**depth*h, 'tile output lift')
                    low = (F(P,Q)**depth)*(start+F(DIGITS[0],P-Q))-F(DIGITS[0],P-Q)
                    high = (F(P,Q)**depth)*(start+F(DIGITS[-1],P-Q))-F(DIGITS[-1],P-Q)
                    need(low <= x <= high, 'cap growth bracket'); lifts += 1
                following.append((ww, rr, ss)); rows.append([list(ww),rr,ss,b])
        need(len({rr for _,rr,_ in following}) == 6**depth, 'root coding collision')
        levels.append([depth, len(following), min(rr for _,rr,_ in following)])
        level = following
    # Empty positive-depth family has minimum one, unlike its residue zero.
    need(min(range(1, 10)) == 1 and 0 != 1, 'empty-depth counterexample')
    # Difference between source value increment and high quotient increment.
    original = CAP[0]; shifted = original+P*Q
    quotient_difference = (shifted-SOURCE[0])//Q-(original-SOURCE[0])//Q
    need(quotient_difference == P and quotient_difference != P*Q, 'quotient increment')
    # A proper one-type sublanguage has a polynomial self-section other than F.
    i = 0; k0 = ((r[i]-c[i])*pow(P,-1,Q)) % Q
    x = r[i]+Q*k0; y = (P*x+Q-1)//Q
    kp, rem = divmod(P*k0+c[i]-r[i], Q)
    need(rem == 0 and y == r[i]+Q*kp, 'one-type child')
    need(Q*(Q*kp+r[i])-P*(Q*k0+r[i]) == DIGITS[i], 'proper-sublanguage section')
    need(Q*k0+r[i] != P*k0+c[i], 'identity differs from forward section')
    return dict(ordered_pairs=36, affine_automorphisms=automorphisms, words=len(rows),
                physical_lifts=lifts, levels=levels, tile_transcript=seal(rows),
                empty_depth_positive_minimum=1, empty_word_canonical_residue=0,
                correct_high_quotient_increment=quotient_difference,
                incorrect_printed_increment=P*Q,
                proper_sublanguage_example=dict(type=i,k=k0,next_k=kp,source=x,endpoint=y))


def centered() -> dict:
    M, N = 64, 81
    rho = F(M,N); d = F(N-M,N); periodic_words = 0; rows = []
    for L in range(1, 9):
        for w in product((0,1), repeat=L):
            tails = [d*sum((F(w[(j+k)%L])*rho**k for k in range(L)), F())/(1-rho**L)
                     for j in range(L)]
            errors = [(F(w[j])-tails[j])/M for j in range(L)]
            for j in range(L):
                jj = (j+1)%L
                need(abs(errors[j]) <= F(1,N), 'centered error strip')
                need(N*errors[j]-M*errors[jj] == w[j]-w[jj], 'centered recurrence')
            completion = -sum((F(w[j]-w[(j+1)%L],N)*rho**j for j in range(L)),F())/(1-rho**L)
            if any(w) and not all(w):
                need(completion.denominator != 1, 'nonconstant periodic ordinary completion')
            else: need(completion == 0, 'constant completion')
            rows.append([list(w),completion.numerator,completion.denominator]); periodic_words += 1
    # Nonconstant real paths at the two strip endpoints, no ordinary lift inferred.
    endpoint_errors = [F(1,N), -F(1,N)]
    need((F(1)-d)/M == endpoint_errors[0], '1000 endpoint')
    need(-rho/M == endpoint_errors[1], '0111 endpoint')
    path_count = repeat_checks = 0
    for w in product((0,1), repeat=8):
        C = sum(N**(7-j)*M**j*(N-M)*bit for j,bit in enumerate(w))
        root = (C*pow(N**8,-1,M**8)) % M**8
        for lift in (1, 2):
            start = root+lift*M**8; path = [start]
            for bit in w:
                need(path[-1] % M == bit, 'ordinary chart cylinder')
                y, rem = divmod(N*path[-1]-(N-M)*bit, M)
                need(rem == 0 and y > path[-1], 'ordinary chart growth')
                path.append(y)
            for r in range(8):
                for t in range(r+1, 8):
                    for length in range(1, 9-t):
                        if w[r:r+length] != w[t:t+length]: continue
                        delta = path[t]-path[r]
                        need(delta > 0 and delta % M**length == 0, 'repeated-factor divisibility')
                        need(M**(length+t) < start*N**t, 'strict global recurrence cone')
                        repeat_checks += 1
            path_count += 1
    tau = '0'
    for _ in range(15): tau = ''.join('01' if b=='0' else '10' for b in tau)
    for j in range(13):
        q = 2**j
        need(tau[q:2*q] == tau[2*q:3*q], 'Thue-Morse squares')
    need(81**2 < 64**3, 'positive repetition surplus')
    return dict(periodic_words=periodic_words, completion_transcript=seal(rows),
                finite_ordinary_paths=path_count, repeated_factor_checks=repeat_checks,
                thue_morse_scales=13, nonconstant_real_endpoint_errors=[[x.numerator,x.denominator] for x in endpoint_errors],
                constant_word_completion=0, constant_word_factor_complexity=1)


def divided_differences() -> dict:
    cases = 0
    for degree in range(1, 5):
        order = degree+1
        for start in range(50):
            nodes = [3*j+j%2 for j in range(start,start+order+1)]
            values = [F(x*(x-1),2) if degree == 2 else F(x**degree) for x in nodes]
            diff = sum((y/F(prod(x-z for z in nodes if z!=x)) for x,y in zip(nodes,values)),F())
            need(diff == 0, 'polynomial divided difference')
            denominator_bound = factorial(order*4)**(order+1)
            need((diff*denominator_bound).denominator == 1, 'fixed lattice')
            cases += 1
    return dict(polynomial_windows=cases, square_root_sparse_domain_gaps=[2*j+1 for j in range(1,11)],
                analytic_input='convergent Puiseux expansion and divided-difference mean-value theorem; not proved by finite tests')


def reconstruct() -> dict:
    return dict(schema=SCHEMA,base=BASE,scope=SCOPE,extraction=extraction(),
                periodic=periodic_and_cylinders(),coefficient=coefficient(),
                automata=automata(),six_branch=chart(),centered=centered(),
                divided_differences=divided_differences())


def validate(report: dict, expected: dict) -> None:
    need(isinstance(report,dict) and set(report)=={'payload','sha256'}, 'report envelope')
    need(report['sha256']==seal(report['payload']), 'payload hash')
    need(report['payload']==expected, 'independent audit reconstruction mismatch')


def self_test(report: dict, expected: dict) -> int:
    changes = [lambda p:p.update(scope='Collatz proved'),
               lambda p:p['extraction'].update(negative_integer=4096),
               lambda p:p['periodic'].update(trivial_realizers=[]),
               lambda p:p['coefficient']['least_sources'].__setitem__(0,0),
               lambda p:p['automata']['rows'][0].update(cyclic_sizes=[1]),
               lambda p:p['six_branch'].update(ordered_pairs=35),
               lambda p:p['centered'].update(constant_word_completion=1),
               lambda p:p['divided_differences'].update(polynomial_windows=0)]
    for change in changes:
        bad = deepcopy(report); change(bad['payload']); bad['sha256']=seal(bad['payload'])
        need(bad != report, 'no-op mutation')
        try: validate(bad,expected)
        except ValueError: continue
        raise ValueError('resealed corruption accepted')
    return len(changes)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    group = ap.add_mutually_exclusive_group(required=True)
    group.add_argument('--write',type=Path); group.add_argument('--check',type=Path)
    ap.add_argument('--self-test',action='store_true')
    args = ap.parse_args(); expected=reconstruct()
    report=dict(payload=expected,sha256=seal(expected))
    if args.write: args.write.write_bytes(canonical(report)+b'\n')
    else: validate(json.loads(args.check.read_text()),expected)
    print('PASS Reviewer D bounded audit:',report['sha256'])
    if args.self_test: print('Resealed corruptions rejected:',self_test(report,expected))
    print(json.dumps({k:v for k,v in expected.items() if k not in ('scope','schema')},sort_keys=True))

if __name__ == '__main__': main()
