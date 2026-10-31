#!/usr/bin/env python3
"""Exact, standalone checks for the occupation/concentration packet.

Run from any working directory. Uses only the Python standard library.
Four process workers are computational checks, NOT independent AI reviewers.
No check is a proof of a universal fixed-source regularity statement.
"""
from __future__ import annotations
import argparse
from concurrent.futures import ProcessPoolExecutor
from fractions import Fraction as F
from hashlib import sha256
from itertools import product
import json
from math import comb
from pathlib import Path


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def valuation(n: int) -> int:
    require(n > 0, "valuation requires a positive integer")
    return (n & -n).bit_length() - 1


def step(n: int) -> tuple[int, int]:
    require(n > 0 and n % 2 == 1, "positive odd state required")
    z = 3*n + 1
    a = valuation(z)
    return z >> a, a


def digest(obj: object) -> str:
    return sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def cylinder(word: tuple[int, ...]) -> tuple[int, int]:
    require(bool(word) and all(a >= 1 for a in word), "invalid valuation word")
    A, C = 0, 0
    for a in word:
        C = 3*C + (1 << A)
        A += a
    mod = 1 << (A+1)
    return (((1 << A)-C)*pow(3**len(word), -1, mod)) % mod, mod


def replay(n: int, word: tuple[int, ...]) -> list[int]:
    states = [n]
    for expected in word:
        n, actual = step(n)
        require(actual == expected, "valuation mismatch")
        states.append(n)
    return states


def log_bounds(x: F, terms: int = 42) -> tuple[F, F]:
    """Certified natural-log enclosure, using an exact atanh series."""
    require(x > 0, "log domain")
    u, k = x, 0
    while u >= 2:
        u /= 2
        k += 1
    while u < 1:
        u *= 2
        k -= 1
    def series(v: F) -> tuple[F, F]:
        z = (v-1)/(v+1)
        power, total = z, F(0)
        for j in range(terms):
            total += 2*power/(2*j+1)
            power *= z*z
        error = 2*power/((2*terms+1)*(1-z*z))
        return total, total+error
    lo, hi = series(u)
    l2, h2 = series(F(2))
    return (lo+k*l2, hi+k*h2) if k >= 0 else (lo+k*h2, hi+k*l2)


def outward(pair: tuple[F, F], digits: int = 18) -> list[str]:
    scale = 10**digits
    lo, hi = pair
    a = (lo.numerator*scale)//lo.denominator
    b = -((-hi.numerator*scale)//hi.denominator)
    def fixed(n: int) -> str:
        return ("-" if n < 0 else "") + str(abs(n)//scale) + "." + str(abs(n)%scale).zfill(digits)
    return [fixed(a), fixed(b)]


def coarse(pair: tuple[F, F]) -> tuple[F, F]:
    scale = 10**24
    lo, hi = pair
    return F((lo.numerator*scale)//lo.denominator, scale), F(-((-hi.numerator*scale)//hi.denominator), scale)


def kappa_at(d: F) -> tuple[F, F]:
    # kappa(d)=1-H_2(1/d), decreasing on 1<d<2.
    require(1 < d < 2, "cost outside entropy range")
    ld, hd = log_bounds(d)
    lm, hm = log_bounds(d-1)
    l2, h2 = log_bounds(F(2))
    t = (d-1)/d
    low_h, high_h = ld-t*hm, hd-t*lm
    return 1-high_h/l2, 1-low_h/h2


def rate_at(d: F) -> tuple[F, F]:
    l2, h2 = log_bounds(F(2))
    ld, hd = log_bounds(d)
    lm, hm = log_bounds(d-1)
    return d*l2-d*hd+(d-1)*lm, d*h2-d*ld+(d-1)*hm


def cylinders_track() -> dict:
    words, cases, rows = 0, 0, []
    for k in range(1, 6):
        for word in product(range(1, 5), repeat=k):
            r, mod = cylinder(word)
            require(r % 2 == 1, "cylinder root not odd")
            # Independently reconstruct by inverse branches at varying moduli.
            y, current = 1, 2
            for a in reversed(word):
                current <<= a
                y = ((1 << a)*y-1)*pow(3, -1, current) % current
            require((r, mod) == (y, current), "inverse-branch disagreement")
            for lift in range(3):
                states = replay(r+lift*mod, word)
                rows.append([list(word), states[0], states[-1]])
                cases += 1
            words += 1
    repetition_cases, cycle_exceptions, repetition_rows = 0, 0, []
    for k in range(1,6):
        for word in product(range(1,5), repeat=k):
            A,C=0,0
            for a in word:
                C=3*C+(1 << A)
                A+=a
            D=(1 << A)-3**k
            for repeats in range(1,5):
                repeated=word*repeats
                r,mod=cylinder(repeated)
                for lift in range(2):
                    n=r+lift*mod
                    states=replay(n,repeated)
                    defect=D*n-C
                    require(defect % mod == 0,"periodic defect divisibility")
                    if defect==0:
                        require(states[-1]==n,"cycle exception does not close")
                        cycle_exceptions+=1
                    else:
                        require(mod<=abs(defect)<=abs(D)*n+C,"source-size bound")
                    repetition_cases+=1
                    repetition_rows.append([list(word),repeats,n,defect])
    rejected = 0
    for n, word in [(0, (1,)), (2, (1,)), (3, (2,)), (1, (1,))]:
        try:
            replay(n, word)
        except ValueError:
            rejected += 1
    require(rejected == 4, "negative controls not rejected")
    return dict(track="cylinders", words=words, ordinary_lifts=cases,
                negative_controls_rejected=rejected, transcript_sha256=digest(rows),
                repetition_cases=repetition_cases, cycle_exceptions=cycle_exceptions,
                repetition_sha256=digest(repetition_rows))


def entropy_track() -> dict:
    l2, h2 = log_bounds(F(2))
    constants = {}
    for name, base in [("escape", F(3)), ("floor_4097", F(3)+F(1,4097))]:
        lb, hb = log_bounds(base)
        dl, dh = coarse((lb/h2, hb/l2))
        kap = (kappa_at(dh)[0], kappa_at(dl)[1])
        rate = (rate_at(dh)[0], rate_at(dl)[1])
        require(kap[0] > F(1,20), "1/20 threshold not certified")
        constants[name] = dict(cost=outward((dl,dh)), singular_mass_lower=outward((2-dh,2-dl)),
                               dyadic_kappa=outward(kap), valuation_KL_rate=outward(rate))
    distributions = 0
    z = F(4,5)
    for counts in product(range(9), repeat=4):
        total = sum(counts)
        if total == 0 or total > 8:
            continue
        ps = [F(x,total) for x in counts]
        mean = sum((i+1)*p for i,p in enumerate(ps))
        if mean > F(3,2):
            continue
        collision = sum(p*p*2**(i+1) for i,p in enumerate(ps))
        moment = sum(p*z**(i+1) for i,p in enumerate(ps))
        require(collision*z*z/(2-z*z) >= moment*moment, "Holder failed")
        require(collision >= z*(2-z*z) > 1, "cost/collision bound failed")
        distributions += 1
    types = []
    for B in [6, 12, 24, 48, 96, 192]:
        K = 2*B//3
        lC,hC = log_bounds(F(comb(B,K)))
        types.append(dict(length=B, ones=K, words=str(comb(B,K)),
                          collision_exponent=outward((1-hC/(B*l2), 1-lC/(B*h2)))))
    return dict(track="entropy", certified_constants=constants,
                rational_distributions_checked=distributions, balanced_block_models=types)


def adelic_track() -> dict:
    cases, rows = 0, []
    H = 10**20
    for k in range(1,6):
        for word in product(range(1,4), repeat=k):
            root, mod = cylinder(word)
            for ell in range(1,4):
                ternary = 3**ell
                for t in range(ternary):
                    if t % 3 == 0:
                        continue
                    n = root+mod*((t-root)*pow(mod,-1,ternary) % ternary)
                    period = mod*ternary
                    floor = H*(1 << sum(word))
                    n += max(0, (floor-n+period-1)//period)*period
                    states = replay(n,word)
                    require(min(states) >= H and n % ternary == t, "CRT/floor failure")
                    residue = t
                    for a,actual in zip(word,states[1:]):
                        residue = (3*residue+1)*pow(2**a,-1,ternary) % ternary
                        require(actual % ternary == residue, "ternary trajectory mismatch")
                    cases += 1
                    rows.append([list(word),ell,t,str(n)])
    models = []
    for q in [F(1,2),F(2,3)]:
        prev = {0:F(1)}
        levels = []
        for ell in range(1,5):
            mod, period = 3**ell, 2*3**(ell-1)
            weights = [q*(1-q)**(a-1)/(1-(1-q)**period) for a in range(1,period+1)]
            require(sum(weights)==1, "infinite-tail aggregation not normalized")
            def push(law: dict[int,F]) -> dict[int,F]:
                out = {}
                for x,p in law.items():
                    for a,w in enumerate(weights,1):
                        y = (3*x+1)*pow(2**a,-1,mod) % mod
                        out[y] = out.get(y,F(0))+p*w
                return out
            law = push(prev)
            require(sum(law.values())==1 and push(law)==law, "stationarity failure")
            project = {}
            for x,p in law.items():
                project[x % (mod//3)] = project.get(x % (mod//3),F(0))+p
            require(project==prev, "projective consistency failure")
            if q==F(1,2) and ell==2:
                expected = [F(x,63) for x in [0,8,16,0,11,4,0,2,22]]
                require([law.get(i,F(0)) for i in range(9)]==expected, "known control differs")
            levels.append(dict(level=ell, support=len(law),
                law_sha256=digest([[x,str(p)] for x,p in sorted(law.items())])))
            prev = law
        models.append(dict(odd_probability=str(q),levels=levels))
    return dict(track="adelic", joint_positive_witnesses=cases, minimum_state=str(H),
                witness_sha256=digest(rows), ternary_stationary_models=models)


def floor_and_binary_track() -> dict:
    receipt, max_steps, max_peak = [], [0,0], [0,0]
    for n in range(3,4097,2):
        x, steps, peak = n,0,n
        while x >= n:
            x,_ = step(x)
            peak = max(peak,x)
            steps += 1
            require(steps < 100000, "finite floor check failed to stop")
        receipt.append([n,steps,x,peak])
        max_steps = max(max_steps,[steps,n])
        max_peak = max(max_peak,[peak,n])
    # Induction certifies odd starts <=4095; even starts <=4096 halve first.
    binary_rows, cylinders = [], 0
    for q in [F(1,2),F(2,3),F(5,8)]:
        for L in range(1,13):
            ps=[]
            for r in range(1,1<<L,2):
                x,ones=r,0
                for _ in range(L):
                    odd=x%2
                    ones+=odd
                    x=(3*x+1)//2 if odd else x//2
                ps.append(q**(ones-1)*(1-q)**(L-ones))
            require(sum(ps)==1,"binary law not normalized")
            collision=(1 << (L-1))*sum(p*p for p in ps)
            require(collision==(2*(q*q+(1-q)**2))**(L-1),"binary collision formula failure")
            binary_rows.append([str(q),L,str(collision)])
            cylinders+=len(ps)
    return dict(track="floor_and_binary", all_positive_starts_through=4096,
                odd_induction_starts=len(receipt), max_odd_steps_and_source=max_steps,
                max_odd_peak_and_source=max_peak, floor_receipt_sha256=digest(receipt),
                binary_cylinders_checked=cylinders, binary_collision_sha256=digest(binary_rows))


TRACKS = [cylinders_track, entropy_track, adelic_track, floor_and_binary_track]


def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workers",type=int,default=4,choices=range(1,5))
    parser.add_argument("--output",type=Path)
    args=parser.parse_args()
    if args.workers==1:
        results=[f() for f in TRACKS]
    else:
        with ProcessPoolExecutor(max_workers=args.workers) as pool:
            results=[future.result() for future in [pool.submit(f) for f in TRACKS]]
    report=dict(schema=1,status="PASS",scope="standalone exact finite checks; not independent review or a Collatz proof",
                results=results)
    text=json.dumps(report,sort_keys=True,indent=2)+"\n"
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(text,encoding="utf-8")
    print(text,end="")


if __name__=="__main__":
    main()
