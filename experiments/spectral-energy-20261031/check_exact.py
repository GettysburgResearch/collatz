#!/usr/bin/env python3
"""Exact small-law, operator and convergent-corridor checks. Not a proof assistant."""
from __future__ import annotations
import argparse
from array import array
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import random
import certify_energy as ce


def require(ok: bool, message: str) -> None:
    if not ok:
        raise AssertionError(message)

def v2(n: int) -> int:
    require(n > 0, 'positive valuation argument')
    return (n & -n).bit_length() - 1

def odd_step(n: int) -> tuple[int, int]:
    value = 3 * n + 1
    a = v2(value)
    return value >> a, a

def corridor(q: int) -> list[int]:
    A = 3 ** q + 1
    t = ((1 << A) - 1) // 3
    require((t + 1) % (3 ** q) == 0, 'corridor divisibility')
    h = (t + 1) // (3 ** q)
    return [3 ** j * 2 ** (q - j) * h - 1 for j in range(q + 1)]

def literal_law(previous: list[F]) -> list[F]:
    """Entire geometric exponent law, summed independently by its exact period."""
    m, modulus = len(previous), 3 * len(previous)
    period = 2 * m
    output = [F(0)] * modulus
    inverse_two = pow(2, -1, modulus)
    power = 1
    for a in range(1, period + 1):
        power = power * inverse_two % modulus
        weight = F(3 * (1 << (period - a)), (1 << period) - 1)
        for r, value in enumerate(previous):
            output[((3 * r + 1) * power) % modulus] += weight * value
    return output

def cyclic_L(previous: list[F]) -> list[F]:
    m, modulus = len(previous), 3 * len(previous)
    period = 2 * m
    cycle = []
    r = 1
    for _ in range(period):
        cycle.append(r)
        r = 2 * r % modulus
    forcing = [previous[((2 * r - 1) // 3) % m] if r % 3 == 2 else F(0) for r in cycle]
    current = F(0)
    for value in reversed(forcing):
        current = (current + 3 * value) / 2
    current /= 1 - F(1, 1 << period)
    output = [F(0)] * modulus
    for r, value in zip(reversed(cycle), reversed(forcing)):
        current = (current + 3 * value) / 2
        output[r] = current
    return output

def energy(values: list[F]) -> F:
    return sum((x*x for x in values), F(0)) / len(values)

def gram_rhs(f: list[F]) -> F:
    """Sum ALL shifts using the exact finite odometer period, not a cutoff."""
    m = len(f)
    cycle = []
    x = 0
    for _ in range(m):
        cycle.append(x)
        x = (4*x+1) % m
    require(x == 0 and len(set(cycle)) == m, 'full odometer cycle')
    vals = [f[x] for x in cycle]
    # h_j=sum_{k>=1}4^-k f_(j+k); solve h_j=(f_(j+1)+h_(j+1))/4.
    cur = F(0)
    for j in range(m-1, -1, -1):
        cur = (vals[(j+1) % m] + cur) / 4
    cur /= 1 - F(1, 4 ** m)
    h = [F(0)] * m
    for j in range(m-1, -1, -1):
        cur = (vals[(j+1) % m] + cur) / 4
        h[j] = cur
    return energy(f) + 2 * sum((a*b for a, b in zip(vals, h)), F(0)) / m

def apply_raw(f: dict[int, F], killed: set[int]) -> dict[int, F]:
    out = {}
    for n, value in f.items():
        if n in killed:
            continue
        t, a = odd_step(n)
        if t not in killed:
            out[t] = out.get(t, F(0)) + F(3, 2 ** a) * value
    return {n: value for n, value in out.items() if value}

def subtract(a: dict[int, F], b: dict[int, F]) -> dict[int, F]:
    out = dict(a)
    for n, value in b.items():
        out[n] = out.get(n, F(0)) - value
    return {n: value for n, value in out.items() if value}

def run() -> dict:
    old = [F(1)]
    low = high = array('q', [1 << 50])
    law_rows = []
    residue_checks = 0
    for q in range(1, 6):
        law = literal_law(old)
        require(law == cyclic_L(old), 'two exact whole-law constructions')
        low, high = ce.step(low, high)
        require(all(F(a, 1 << 50) <= x <= F(b, 1 << 50) for a, x, b in zip(low, law, high)),
                'every fixed-point interval contains exact rational density')
        require(energy(law) == gram_rhs(old), 'exact full Gram identity on density')
        for r in range(len(old)):
            require(sum(law[r+j*len(old)] for j in range(3))/3 == old[r], 'projectivity')
        M = (energy(old).numerator + energy(old).denominator - 1)//energy(old).denominator + 1
        require(energy(law)-energy(old) >= F(1, 4 ** (M-1)), 'elementary quantitative increment')
        require(sum(law) == len(law), 'exact Haar mean one')
        law_rows.append({'q':q,'residues':len(law),'energy':str(energy(law))})
        residue_checks += len(law)
        old = law
    rng = random.Random(3102026)
    signed_checks = 0
    for r in range(5):
        for case in range(8):
            f = [F(rng.randrange(-4,5), rng.randrange(1,5)) for _ in range(3 ** r)]
            lf = cyclic_L(f)
            e = energy(lf)
            require(e == gram_rhs(f), 'Gram identity on signed input')
            require(F(3,5)*energy(f) <= e <= F(5,3)*energy(f), 'sharp norm interval')
            signed_checks += 1
    seen = set()
    corridor_rows = []
    literal_steps = 0
    for q in range(1, 13):
        nodes = corridor(q)
        require(not (seen & set(nodes)), 'disjoint positive corridors')
        seen.update(nodes)
        current = nodes[0]
        for j, expected in enumerate(nodes):
            require(current == expected and current > 1 and current % 2, 'literal positive source')
            current, a = odd_step(current)
            require(a == (1 if j < q else 3 ** q + 1), 'entire exact valuation word')
            literal_steps += 1
        require(current == 1, 'actual convergence, not modular compatibility')
        corridor_rows.append({'q':q,'source_bits':nodes[0].bit_length(),
                              'terminal_valuation':3 ** q + 1,'odd_steps_to_one':q+1})
    residual_checks = 0
    for q in range(1, 8):
        nodes = corridor(q)
        for lam in (F(1,2),F(-1,2),F(1),F(-1),F(3,2),F(-3,2),F(9,4)):
            f = {n: (F(3,2)/lam)**j for j,n in enumerate(nodes)}
            for killed in (set(),{1,3,5,7}):
                # For tiny q the finite core may intersect a corridor; only use actual avoidance cases.
                if set(nodes) & killed:
                    continue
                residual = subtract(apply_raw(f,killed), {n:lam*x for n,x in f.items()})
                expected = {nodes[0]: -lam}
                if 1 not in killed:
                    expected[1] = F(3,2 ** (3 ** q+1)) * f[nodes[-1]]
                require(residual == expected, 'whole-vector endpoint-only residual')
                residual_checks += 1
    pair_checks = 0
    for q in range(1, 5):
        for lam in (F(1,2),F(-1,2),F(2,3)):
            arms=[]
            for r in (2*q,2*q+1):
                nodes=corridor(r)
                f={n:(F(3,2)/lam)**j for j,n in enumerate(nodes)}
                outgoing=F(3,2 ** (3 ** r+1))*f[nodes[-1]]
                arms.append({n:x/outgoing for n,x in f.items()})
            f=subtract(arms[0],arms[1])
            residual=subtract(apply_raw(f,set()),{n:lam*x for n,x in f.items()})
            require(set(residual)=={min(arms[0]),min(arms[1])}, 'critical pairing cancels terminal coordinate')
            pair_checks+=1
    payload={'status':'PASS','exact_law_residues':residue_checks,'law_rows':law_rows,
             'signed_Gram_tests':signed_checks,'literal_corridor_steps':literal_steps,
             'corridors':corridor_rows,'whole_vector_residual_tests':residual_checks,
             'critical_pair_tests':pair_checks,'theorem_prover_run':False,'Collatz_proved':False}
    data=json.dumps(payload,sort_keys=True,separators=(',',':')).encode()
    return {'payload':payload,'semantic_sha256':hashlib.sha256(data).hexdigest()}

def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    report=run()
    args.output.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps({'status':'PASS','semantic_sha256':report['semantic_sha256']}))

if __name__=='__main__':
    main()
