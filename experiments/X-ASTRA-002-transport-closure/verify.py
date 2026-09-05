#!/usr/bin/env python3
"""Independent implementation replay of X-ASTRA-002; never imports run.py.

Uses recursive affine composition, a uniqueness check for each CRT witness,
direct forward enumeration for the compiler corpus, and backward substitution
for the finite potential identities. Both implementations have the same author;
this is not an independent mathematical review of the all-parameter theorem.
"""
from __future__ import annotations

import argparse
import copy
import tempfile
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path
from typing import Any

BITS = 512
UNIT = 2**BITS


def check(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def stable(obj: Any) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()


def ord3(value: int) -> int:
    check(value != 0, "zero valuation")
    value = abs(value)
    power = 3
    count = 0
    while value % power == 0:
        count += 1
        power *= 3
    return count


def T(value: int) -> int:
    check(value > 0, "nonpositive physical state")
    return (value + (2*value+1)*(value % 2)) // 2


def seed(value: int) -> Q:
    check(value >= 2, "source outside killed domain")
    return Q(3**ord3(value+1), (value+1)**2)


def branches(depth: int) -> list[list[tuple[int, int, int]]]:
    # An affine branch is (multiplicative numerator, denominator, offset).
    levels = [[(1, 1, 0)]]
    for _ in range(depth):
        nxt = []
        for m, d, c in levels[-1]:
            nxt.append((m, 2*d, c))
            nxt.append((3*m, 2*d, 3*c+d))
        levels.append(nxt)
    return levels


def dictionaries() -> dict[str, tuple[list[tuple[int, int, Q]], int]]:
    result = {
        "base": ([(1, 1, Q(1))], 0),
        "displaced_repair": ([(1, 1, Q(1)), (8, -1, Q(1)), (16, -5, Q(1))], 0),
        "mixed_centres": ([(1, 1, Q(1)), (1, -1, Q(2)), (2, 1, Q(3, 2)), (5, -7, Q(1, 3))], 0),
        "zero_centre": ([(1, 0, Q(1))], 0),
    }
    for N in (2, 4, 6):
        atoms = [(d, m-c, Q(65,64)**k*m)
                 for k, level in enumerate(branches(N)) for m, d, c in level]
        result[f"green_depth_{N}"] = (atoms, N)
    return result


def contains(centre: Q, atoms: list[tuple[int, int, Q]]) -> bool:
    for slope, shift, _ in atoms:
        p = Q(-shift, slope)
        if centre == 0:
            if p == 0:
                return True
            continue
        if p * centre <= 0:
            continue
        while abs(p) > abs(centre):
            p /= 2
        if p == centre:
            return True
    return False


def first_centre(atoms: list[tuple[int, int, Q]], cap: int, depth: int) -> tuple[int,Q,Q]:
    A, B, _ = atoms[0]
    index = max(cap-1, depth)
    while index < 10000:
        r = Q(-B, A*2**index)
        z = Q(3,2)*r+Q(1,2)
        if not contains(z, atoms):
            return index, r, z
        index += 1
    raise ValueError("failed finite centre selection")


def round_up(q: Q) -> int:
    quotient, remainder = divmod(q.numerator*UNIT, q.denominator)
    return quotient + int(remainder != 0)


def full_upper(y: int, atoms: list[tuple[int,int,Q]], J: int) -> int:
    check(all(2*abs(B) < y for _,B,_ in atoms), "invalid affine tail domain")
    total = 0
    for j in range(J):
        for A,B,c in atoms:
            value = A*2**j*y+B
            total += round_up(Q(3,2)**j*c*Q(3**ord3(value), value*value))
    mass_constant = sum((Q(2)*c/A for A,_,c in atoms), Q())
    tail = Q(4)*mass_constant*Q(3,4)**J/y
    return total + round_up(tail)


def check_witnesses(rows: Any) -> tuple[int,int,int]:
    check(isinstance(rows,list), "witness array required")
    ds = dictionaries()
    expected = {(name,b,h) for name in ds for b in (1,4,8) for h in (16,32,64)}
    check(len(rows) == len(expected), "missing or extra witness rows")
    seen = set()
    paths = 0
    min_ratio = None
    base_fields = {"case", "formal_atoms", "distinct_centres", "cap", "h", "ray_index",
                   "source_centre", "endpoint_centre", "u", "endpoint", "source_valuation",
                   "ray_terms", "upper_scaled", "common_lower", "certified_common_ratio_floor"}
    for row in rows:
        check(isinstance(row,dict), "invalid witness")
        name,b,h = row.get("case"),row.get("cap"),row.get("h")
        check(type(b) is int and type(h) is int, "integer parameters required")
        key = (name,b,h)
        check(key in expected and key not in seen, "invalid or duplicate witness parameters")
        seen.add(key)
        atoms,N = ds[name]
        fields = base_fields | ({"deeper_history","deeper_ratio_floor"} if N else set())
        check(set(row) == fields, "unexpected witness fields")
        check(row["formal_atoms"] == len(atoms), "dictionary coverage")
        check(row["distinct_centres"] == len({Q(-B,A) for A,B,_ in atoms}), "centre coverage")
        j,r,z = first_centre(atoms,b,N)
        check(row["ray_index"] == j, "noncanonical escaping ray")
        check(row["source_centre"] == [r.numerator,r.denominator], "source centre")
        check(row["endpoint_centre"] == [z.numerator,z.denominator], "endpoint centre")
        u,y = row["u"],row["endpoint"]
        check(type(u) is int and type(y) is int, "ordinary sources must be integers")
        A,B,c = atoms[0]
        # These conditions uniquely determine the two-lift CRT source.
        check(2*3**h <= u < 4*3**h and u%2 == 1, "ordinary lift range/parity")
        value = A*2**j*u+B
        check(value % 3**h == 0, "source congruence")
        check(y == T(u), "physical endpoint")
        v = ord3(value)
        check(row["source_valuation"] == v and v >= h, "valuation witness")
        J = 4*h+64
        check(row["ray_terms"] == J, "ray truncation coverage")
        upper = full_upper(y,atoms,J)
        check(row["upper_scaled"] == upper, "infinite-ray upper enclosure")
        lower = Q(3,2)**(j-b+1)*c*Q(3**v,value*value)
        check(row["common_lower"] == [lower.numerator,lower.denominator], "common lower weight")
        ratio = (UNIT*lower.numerator)//(lower.denominator*upper)
        check(row["certified_common_ratio_floor"] == ratio and ratio >= 1, "common ratio bound")
        min_ratio = ratio if min_ratio is None else min(min_ratio,ratio)
        for ell in range(1,b+1):
            physical = [2**(ell-1)*u]
            for _ in range(ell):
                physical.append(T(physical[-1]))
            check(physical[-1] == y and min(physical)>1, "killing or endpoint failure")
            check([x%2 for x in physical[:-1]] == [0]*(ell-1)+[1], "physical word")
            # The earlier ray term in W(source) is no smaller than common lower.
            own_lower = Q(3,2)**(j-ell+1)*c*Q(3**v,value*value)
            check(own_lower >= lower, "simultaneous lower bound")
            paths += 1
        if N:
            M = j+1
            check(row["deeper_history"] == M and M>N, "omitted-history depth")
            x=2**j*u
            for _ in range(M):
                check(x>1,"deeper path hit killed state")
                x=T(x)
            check(x==y,"deeper physical endpoint")
            deeper=Q(65,64)**M*seed(2**j*u)
            check(row["deeper_ratio_floor"] == (UNIT*deeper.numerator)//(deeper.denominator*upper),
                  "omitted-history lower ratio")
    check(seen==expected,"incomplete Cartesian coverage")
    return len(rows),paths,int(min_ratio)


def compiler_replay() -> dict[str,int]:
    levels=branches(6)
    terms=0
    comparisons=0
    for k in range(7):
        by_endpoint={y:set() for y in range(2,129)}
        # T^k(n)>=n/2^k makes this finite source cutoff exhaustive for y<=128.
        for n in range(2,128*2**k+1):
            x=n
            survived=True
            for _ in range(k):
                if x==1:
                    survived=False
                    break
                x=T(x)
            if survived and x in by_endpoint:
                by_endpoint[x].add(n)
        for y in range(2,129):
            compiled=set()
            for m,d,c in levels[k]:
                div,rem=divmod(d*y-c,m)
                if rem or div<2:
                    continue
                x=div
                for _ in range(k):
                    if x==1:
                        break
                    x=T(x)
                else:
                    if x==y:
                        check(div not in compiled,"duplicate physical inverse word")
                        compiled.add(div)
                        L=d*y+m-c
                        check(Q(3**(ord3(m)+ord3(L)),L*L)==seed(div),"affine weight normalization")
            check(compiled==by_endpoint[y],"forward/affine source mismatch")
            terms+=len(compiled)
            comparisons+=1
    return {"endpoint_depth_comparisons":comparisons,"guarded_source_terms":terms,
            "max_endpoint":128,"max_depth":6}


def qualitative_replay() -> dict[str,int]:
    for rule,rho in [(0,Q(1,2)),(1,Q(2,3)),(2,Q(3,4))]:
        parents={n:(n-1 if rule==0 else n//2 if rule==1 else 1+(n*n+1)%(n-1))
                 for n in range(2,25)}
        tau={1:0}
        for n in range(2,25):
            check(parents[n]<n,"toy system is not terminating")
            tau[n]=1+tau[parents[n]]
        c={n:Q(1,2**n)*rho**tau[n] for n in parents}
        W=c.copy()
        for n in range(24,1,-1):
            if parents[n]!=1:
                W[parents[n]]+=W[n]/rho
        for y in parents:
            incoming=sum((W[n] for n in parents if parents[n]==y),Q())
            check(incoming==rho*(W[y]-c[y]),"resolvent identity")
            check(incoming<rho*W[y] and W[y]>0,"strict positivity")
        check(sum(W.values(),Q())<=rho/(2*(1-rho)),"global finite-system norm")
    return {"finite_terminating_systems":3,"states_per_system":23}


def verify(path: Path) -> tuple[str,tuple[int,int,int]]:
    report=json.loads(path.read_text())
    check(set(report)=={"payload","sha256"},"report keys")
    p=report["payload"]
    check(set(p)=={"schema","precision_bits","scope","parameters","witnesses","compiler","qualitative_identity"},"payload keys")
    digest=hashlib.sha256(stable(p)).hexdigest()
    check(report["sha256"]==digest,"semantic digest mismatch")
    check(p["schema"]=="X-ASTRA-002/v1" and type(p["precision_bits"]) is int and p["precision_bits"]==BITS,"schema or precision")
    scope={"finite_witness_rows":True,"infinite_ray_tail_enclosed":True,
           "all_parameter_theorem_by_computation":False,"collatz_proved":False,
           "uniform_green_bound_proved":False}
    check(stable(p["scope"])==stable(scope),"inflated or altered mathematical scope")
    params={"caps":[1,4,8],"heights":[16,32,64],"history_depths":[2,4,6],
            "a":[3,2],"lambda":[65,64]}
    check(stable(p["parameters"])==stable(params),"parameter coverage")
    stats=check_witnesses(p["witnesses"])
    check(p["compiler"]==compiler_replay(),"compiler corpus metadata")
    check(p["qualitative_identity"]==qualitative_replay(),"finite potential corpus metadata")
    return digest,stats


def tamper_self_test(path: Path) -> list[str]:
    original = json.loads(path.read_text())
    tests = []
    p = copy.deepcopy(original)
    p["payload"]["witnesses"].pop()
    tests.append(("deleted-witness", p))
    p = copy.deepcopy(original)
    p["payload"]["scope"]["uniform_green_bound_proved"] = True
    tests.append(("inflated-scope", p))
    p = copy.deepcopy(original)
    p["payload"]["witnesses"][0]["upper_scaled"] //= 2
    tests.append(("understated-tail-enclosure", p))
    p = copy.deepcopy(original)
    p["payload"]["witnesses"][0]["u"] += 3**16
    tests.append(("wrong-parity-ordinary-lift", p))
    p = copy.deepcopy(original)
    p["payload"]["compiler"]["guarded_source_terms"] -= 1
    tests.append(("reduced-compiler-coverage", p))
    rejected = []
    for name, report in tests:
        report["sha256"] = hashlib.sha256(stable(report["payload"])).hexdigest()
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            json.dump(report, f)
            temporary = Path(f.name)
        try:
            try:
                verify(temporary)
            except ValueError:
                rejected.append(name)
            else:
                raise RuntimeError("resealed tamper case accepted: " + name)
        finally:
            temporary.unlink()
    return rejected



def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report",type=Path)
    parser.add_argument("--self-test",action="store_true",help="reject five deliberately resealed corrupt reports")
    args=parser.parse_args()
    digest,stats=verify(args.report)
    print("INDEPENDENT IMPLEMENTATION REPLAY PASS",digest)
    print("witness_rows",stats[0],"physical_block_paths",stats[1],"min_common_ratio_floor",stats[2])
    if args.self_test:
        print("RESEALED TAMPER CASES REJECTED:", ", ".join(tamper_self_test(args.report)))


if __name__=="__main__":
    main()
