#!/usr/bin/env python3
"""Exact finite support for the proposed linear-frontier and section-depth packet.

No unbounded search, external dependency, or claim of universal termination.
The default corpus is fixed. Reports are compared, never silently overwritten.
"""
from __future__ import annotations

import argparse
import copy
from fractions import Fraction as F
import hashlib
import itertools
import json
from pathlib import Path

BASE = "69b1ed57ce90fe8c9d6d7c80c69760a86eb0fd2a"
SCOPE = {"all_parameter_claims": "PROPOSED_PENDING_INDEPENDENT_REVIEW",
         "collatz_proved": False, "complete_selector": False,
         "rank": "P(n)=(2n+1)^2/3^v3(2n+1)",
         "clock": "first positive-time returns to n=1 mod3; absorb at1",
         "box": "0<=r,s<=D; witness x in the positive section",
         "finite_tests_only": True}


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def canonical(obj: object) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":")).encode("utf-8")


def sha(obj: object) -> str:
    return hashlib.sha256(canonical(obj)).hexdigest()


def integer_sha(n: int) -> str:
    return hashlib.sha256(hex(n).encode("ascii")).hexdigest()


def vp(n: int, prime: int = 3) -> int:
    require(n != 0 and prime in (2, 3), "finite valuation domain")
    n = abs(n)
    if prime == 2:
        return (n & -n).bit_length()-1
    exponent = 0
    while n % prime == 0:
        n //= prime
        exponent += 1
    return exponent


def vq(x: F) -> int:
    require(x != 0, "finite rational valuation")
    return vp(x.numerator)-vp(x.denominator)


def residue3(x: F) -> int:
    require(x.denominator % 3 != 0, "3-integral dyadic comparison")
    return (x.numerator*pow(x.denominator, -1, 3)) % 3


def step(n: int) -> int:
    return (3*n+1)//2 if n % 2 else n//2


def rank(n: int) -> int:
    require(n >= 1, "positive rank")
    z = 2*n+1
    return z*z//3**vp(z)


def corridor_rank(n: int) -> int:
    require(n >= 1, "positive corridor input")
    return (n+5)**2//3**vp(n+5)


def section(n: int) -> tuple[int, int]:
    require(n >= 1 and n % 3 == 1, "section domain")
    if n == 1:
        return 1, 0
    if n % 4 == 0:
        return n//4, 2
    m = n if n % 2 else n//2
    a = vp(m+1, 2)
    y = (3**a*((m+1) >> a)-1)//2
    return y, a+1+(n % 2 == 0)


def fan(y: int, cap: int | None = None) -> list[tuple[int, int, int, int]]:
    """(source, odd steps, even steps, gap). No full fan formed before pruning."""
    require(y % 3 == 1 and y != 1, "signed nonabsorbing section")
    h = vp(2*y+1)
    u = (2*y+1)//3**h
    gaps = range(1, h+1) if cap is None else range(1, min(h, cap-1)+1)
    out = [(2**(h-d+1)*3**d*u-2, h-d, 2, d) for d in gaps]
    z = 2**h*u-1
    if z % 3 == 1:
        out.append((z, h, 1, 0))
    return out


def cone(root: int, radius: int, pruned: bool) -> dict[int, tuple[int, int, int]]:
    require(root >= 1 and root % 3 == 1 and radius >= 0, "positive cone domain")
    # Earliest BFS discovery gives the largest remaining radius. Its retained
    # threshold is at least as large as a later occurrence's threshold.
    nodes = {root: (0, 0, 0)}
    layer = [root]
    for depth in range(radius):
        following = []
        for y in layer:
            if y == 1:
                continue
            oldq, oldk, _ = nodes[y]
            cap = 4*(radius-depth)-2 if pruned else None
            for x, q, e, _ in fan(y, cap):
                if x not in nodes:
                    nodes[x] = (oldq+q, oldk+q+e, depth+1)
                    following.append(x)
        layer = following
    return nodes


def compare_cones() -> dict:
    cases = [(n, d) for n in range(4, 388, 3) for d in range(7)]
    cases += [(208363, 3), (29371, 2), (121, 8), (859, 6)]
    rows = []
    for n, d in cases:
        full, short = cone(n, d, False), cone(n, d, True)
        a, b = min(full, key=rank), min(short, key=rank)
        require(a == b, "linear pruning lost minimum")
        for x, (q, k, depth) in full.items():
            require(x <= 4**depth*n, "inverse spatial bound")
            require(3**q*x <= 2**k*n and k-q <= 2*depth, "inverse clock inequality")
        rows.append([n, d, a, len(full), len(short)])
    return {"cases": len(rows), "full_nodes_sum": sum(r[3] for r in rows),
            "pruned_nodes_sum": sum(r[4] for r in rows), "rows_sha256": sha(rows)}


def negative_checks() -> dict:
    nodes = {-2: (0, 0, 0)}
    layer = [-2]
    tables, product_rows = [], []
    for d in range(11):
        B = 1+max(q+vp(2*v+1) for v, (q, k, t) in nodes.items())
        require(d//3+2 <= B <= 4*d+2, "linear precision envelope")
        tables.append([d, len(nodes), B])
        if d == 10:
            break
        following = []
        for y in layer:
            q0, k0, _ = nodes[y]
            for x, q, e, _ in fan(y):
                require(x <= -2 and x not in nodes, "negative path repetition/sign")
                nodes[x] = (q0+q, k0+q+e, d+1)
                following.append(x)
        layer = following
    for v, (q, k, depth) in sorted(nodes.items()):
        x, odds, correction = v, [], F(1)
        for _ in range(k):
            if x % 2:
                odds.append(-x)
                correction *= F(3*(-x)-1, 3*(-x))
            x = step(x)
        require(x == -2 and len(set(odds)) == q, "negative literal path")
        require(all(a >= 2*i+1 for i, a in enumerate(sorted(odds), 1)), "distinct odd magnitudes")
        require(correction**5*(q+1) >= 1, "correction product")
        m = q+vp(2*v+1)
        require(3**(5*m) <= 32*m*4**(5*depth)*2**(5*m), "precision product inequality")
        product_rows.append([v, q, k, depth, m])
    greedy, y, q = [], -2, 0
    for d in range(65):
        require(q >= d//3, "odd exit every three returns")
        greedy.append([d, y, q])
        if y % 9 == 1:
            x = (4*y-1)//3
            require(step(step(x)) == y, "negative odd-edge construction")
            y, q = x, q+1
        else:
            y *= 4
    coefficients = [1296, 2160, 1800, 930, 269, 32]
    polynomial_rows = []
    for i in range(1, 129):
        lhs = (6*i+2)**5*(i+1)-(6*i+3)**5*i
        rhs = sum(c*i**(5-j) for j, c in enumerate(coefficients))
        require(lhs == rhs and lhs > 0, "exact fifth-power identity")
        polynomial_rows.append([i, lhs])
    require(3**50 > 320*4**10*2**50, "r=2 exponential base")
    require(10*81**5 > 14*64**5, "cofinal ratio")
    return {"precision_table": tables, "negative_vertices": len(nodes),
            "product_rows_sha256": sha(product_rows), "greedy_edges": 64,
            "greedy_sha256": sha(greedy), "polynomial_cases": 128,
            "polynomial_sha256": sha(polynomial_rows)}


def remainder_checks() -> dict:
    rows = []
    for length in range(1, 13):
        minima = {}
        for bits in itertools.product((0, 1), repeat=length):
            q, B = 0, 0
            for i, bit in enumerate(bits):
                q += bit
                B = 3**bit*B+2**i
            minima[q] = min(minima.get(q, B), B)
        for q, minimum in sorted(minima.items()):
            require(minimum == 3**q+2**length-2**(q+1), "minimum shifted remainder")
            rows.append([length, q, minimum])
    for r in range(1, 65):
        require(10*8**r-8*4**r > 0, "ghost stripping obstruction")
    return {"words": sum(2**j for j in range(1, 13)), "minima_sha256": sha(rows),
            "ghost_lengths_checked": 64}


def symbolic_bounds(D: int) -> dict:
    """Audit the finite A/B comparison argument, not a sampled ordinary orbit."""
    h0, K = 4*D+1, 36*D+20
    t0 = 5*2**h0
    Arows, Brows, highs = [], [], []
    for r in range(D+1):
        pending = [(F(9, 8)**r/2, F(9, 2)*F(9, 8)**r-5, 0, 0, 0)]
        while pending:
            a, b, q, k, depth = pending.pop()
            require((2**(3*r+1)*b).denominator == 1, "A dyadic denominator")
            require(abs(b)+2 <= 12*8**D, "A real comparison bound")
            if 2*b+1 == 0:
                p = q-2*r
                require(k == 3*r and a == F(1, 2)*F(3)**(-p), "homogeneous high node")
                require(-2*r <= p <= 0, "forbidden homogeneous reduction")
                highs.append([r, depth, p])
                if depth == D:
                    continue
                roots = [(F(2)**(1-p-d)*3**d, F(-2)) for d in range(1, 4*(D-depth)-2)]
                if p % 2:
                    roots.append((F(2)**(-p), F(-1)))
                for c, e in roots:
                    x0 = c*t0+e
                    require(x0.denominator == 1 and int(x0) > 1 and int(x0)%3 == 1, "B ordinary comparison root")
                    require(x0 < 2**(10*D+5), "B root size")
                    todo = [(c, e, 0, 0)]
                    while todo:
                        aa, bb, qq, dd = todo.pop()
                        xx = aa*t0+bb
                        require(xx.denominator == 1 and int(xx)>1, "B integral comparison")
                        xx = int(xx)
                        H = vp(2*xx+1)
                        require(xx < 2**(12*D+5) and H <= 12*D+6, "B spatial/depth bound")
                        require(qq <= 24*D+10 and vq(2*aa) >= -qq, "B coefficient denominator")
                        require(K+1+vq(2*aa) > H, "B frozen precision")
                        require(aa >= F(2,3)**qq and abs(bb)+2 <= 4**(D+1), "B coefficient/constant bounds")
                        Brows.append([r, depth, p, dd, qq, H, str(aa), str(bb)])
                        if dd == D-depth-1:
                            continue
                        for child, qedge, even, gap in fan(xx):
                            factor = F(2**(qedge+even), 3**qedge)
                            offset = F(child)-factor*xx
                            todo.append((factor*aa, factor*bb+offset, qq+qedge, dd+1))
                continue
            H = vq(2*b+1)
            require(1 <= H <= 4*D+4 and q <= min(4*D*(D+1),24*D+16), "A fixed valuation bound")
            require(a >= F(1,2)*F(2,3)**q and vq(2*a) == 2*r-q, "A coefficient")
            Arows.append([r, depth, q, k, H, str(a), str(b)])
            if depth == D:
                continue
            for j in range(H):
                factor = F(2**(j+2), 3**j)
                offset = F(2**(j+1), 3**j)-2
                pending.append((factor*a, factor*b+offset, q+j, k+j+2, depth+1))
            factor = F(2**(H+1), 3**H)
            offset = F(2**H, 3**H)-1
            nextb = factor*b+offset
            if residue3(nextb) == 1:
                pending.append((factor*a, nextb, q+H, k+H+1, depth+1))
    Arows.sort(); Brows.sort(); highs.sort()
    return {"D": D, "A_low_nodes": len(Arows), "A_high_nodes": len(highs),
            "B_nodes": len(Brows), "A_sha256": sha(Arows), "high_sha256": sha(highs),
            "B_sha256": sha(Brows)}


def family(D: int, extra_h: int, lift: int, full: bool) -> dict:
    h, h0, K = 256*(D+1)+extra_h, 4*D+1, 36*D+20
    L = 2*(h+D+2)
    N = 3*D+L+1
    modulus2, modulus3 = 2**(N+1), 3**(K+1)
    residue_n = (8**D*(5+2**L)*pow(9**D, -1, 2**N)-5) % (2**N)
    r2 = (2*residue_n+1)*pow(3**h, -1, modulus2) % modulus2
    r3 = 5*2**h0*pow(pow(2, h, modulus3), -1, modulus3) % modulus3
    u = r2+modulus2*((r3-r2)*pow(modulus2, -1, modulus3) % modulus3)
    u += lift*modulus2*modulus3
    require(u>0 and u%2 and u%3, "ordinary CRT unit")
    n = (3**h*u-1)//2
    require(vp(2*n+1) == h and n%2, "source depth/parity")
    require((2**h*u-5*2**h0) % modulus3 == 0, "frozen dyadic cofactor")
    p0, c0, y = rank(n), corridor_rank(n), n
    box_rows, total_nodes = [], 0
    for r in range(D+1):
        small = cone(y, D, True)
        winner = min(small, key=rank)
        require(winner == n, "bounded section merger unexpectedly succeeds")
        large = cone(y, D, False) if full else None
        if large is not None:
            require(min(large, key=rank) == n, "full inverse box contradicts theorem")
        box_rows.append([r, len(small), len(large) if large is not None else None])
        total_nodes += len(small)
        if r < D:
            yy, clock = section(y)
            require(y%8 == 3 and clock == 3 and yy > y, "growing corridor")
            require(64*corridor_rank(yy) == 9*corridor_rank(y), "alternate-rank drop")
            if r == 0:
                require(min(rank(yy),corridor_rank(yy))>min(p0,c0), "naive minimum obstruction")
                require(max(rank(yy),corridor_rank(yy))>max(p0,c0), "naive maximum obstruction")
            y = yy
    require(vp(y, 2) == L, "exact terminal even run")
    m = y >> L
    require(m%2 and m%3==1 and 4*rank(m)<p0, "common-P repayment")
    require(64**D*corridor_rank(y) == 9**D*c0, "corridor telescoping")
    # Literal shortcut replay checks all the guards, not just the affine endpoint.
    x = n
    for bit in "110"*D+"0"*L:
        require(x%2 == int(bit), "literal repayment parity")
        x = step(x)
    require(x == m, "literal repayment endpoint")
    return {"D": D, "h": h, "K": K, "lift": lift, "L": L,
            "source_bits": n.bit_length(), "endpoint_bits": m.bit_length(),
            "source_sha256": integer_sha(n), "unit_sha256": integer_sha(u),
            "endpoint_sha256": integer_sha(m), "box": box_rows,
            "full_box_replayed": full, "pruned_nodes": total_nodes,
            "repayment_shortcut_steps": 3*D+L, "repayment_section_returns": D+L//2,
            "P_quarter_drop": True, "corridor_rank_each_ratio": [9,64], "naive_min_max_increase": True}


def controls() -> dict:
    low = [x for x in range(1, 122) if rank(x)<rank(121)]
    union = set()
    for x in low:
        seen = set()
        while x not in seen:
            require(len(seen)<128, "finite control guard")
            seen.add(x); union.add(x); x = step(x)
        require(x in (1,2), "finite control did not reach trivial cycle")
    x, raw, returns = 121, 0, 0
    while x not in union:
        x, cost = section(x)
        raw += cost; returns += 1
    require((x, raw, returns) == (40,54,16), "121 all-witness first meeting")
    old = {208363}; layer = [208363]
    for _ in range(3):
        following = [x for y in layer for x,q,e,d in fan(y) if d<=1]
        old.update(following); layer=following
    exact = cone(208363, 3, False)
    require(min(old,key=rank)==208363 and min(exact,key=rank)==4445077, "unsafe old pruning control")
    return {"lower_rank_pool_121": low, "forward_union": sorted(union),
            "first_meeting_121": [16,54,40], "old_pruning_control": [208363,4445077]}



def compressed_convergence(D: int) -> dict:
    """A symbolic family reaching1. Its enormous source is NOT materialized."""
    h, K, h0 = 256*(D+1), 36*D+20, 4*D+1
    M = h+2*D+K+1
    modulus = 3**M
    target = (9**(D+1)-10*8**D+3**(h+2*D)*5*2**h0*pow(2**h,-1,modulus)) % modulus
    target = target*pow(2**(3*D+1),-1,modulus) % modulus
    require(target%3==1, "logarithm in the principal ternary units")
    exponent, accumulated, generator, weight, small = 0, 1, 4, 1, 9
    digits=[]
    for _ in range(M-1):
        candidates=[d for d in (0,1,2) if accumulated*pow(generator,d,small)%small==target%small]
        require(len(candidates)==1, "unique ternary exponent digit")
        d=candidates[0];digits.append(d)
        exponent+=d*weight
        accumulated=accumulated*pow(generator,d,modulus)%modulus
        generator=pow(generator,3,modulus);weight*=3;small*=3
    require(pow(4,exponent,modulus)==target and 0<=exponent<weight, "discrete logarithm certificate")
    threshold=h+D+2
    exponent += max(0,(threshold-exponent+weight-1)//weight)*weight
    L=2*exponent
    require(L>=2*(h+D+2) and L%2==0, "sufficient even ending")
    znum=(pow(2,3*D+L+1,modulus)+10*8**D-9**(D+1))%modulus
    require(vp(znum)==h+2*D, "compressed source exact depth")
    ures=znum//3**(h+2*D)
    require((pow(2,h,3**(K+1))*ures-5*2**h0)%3**(K+1)==0, "compressed frozen cofactor")
    return {"D":D,"h":h,"K":K,"modulus_exponent":M,
            "terminal_even_steps_hex":hex(L),"exponent_lifting_digits_sha256":sha(digits),
            "source_expression":"(2^(3D+L)+5*(8^D-9^D))/9^D",
            "exact_word":"(110)^D 0^L","endpoint":1,
            "ordinary_source_materialized":False,"all_steps_literally_replayed":False,
            "modular_guards_replayed":True}


def build() -> dict:
    rows = [family(D, extra, lift, D<=2 and extra==0 and lift==0)
            for D in (1,2,3,4) for extra,lift in ((0,0),(0,1),(1,0))]
    body = {"schema": "X-ALF-001/v1", "base": BASE, "scope": SCOPE,
            "negative": negative_checks(), "inverse": compare_cones(),
            "remainders": remainder_checks(), "symbolic": [symbolic_bounds(D) for D in range(1,6)],
            "families": rows, "compressed_convergence": [compressed_convergence(D) for D in (1,2,3,4)], "controls": controls()}
    return {"body": body, "sha256": sha(body)}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = build()
    if args.check:
        require(result == json.loads(args.check.read_text(encoding="utf-8")), "canonical report mismatch")
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_bytes(json.dumps(result, sort_keys=True, indent=2).encode()+b"\n")
    print("PASS", result["sha256"])
    print("family rows",len(result["body"]["families"]),"inverse comparisons",result["body"]["inverse"]["cases"])


if __name__ == "__main__":
    main()
