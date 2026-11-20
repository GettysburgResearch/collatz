#!/usr/bin/env python3
"""Independent literal-shortcut reconstruction of the shifted-core interface."""
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
from math import gcd
import json


def check(condition, label):
    if not condition:
        raise RuntimeError(label)


def v(n, p):
    result = 0
    while n % p == 0:
        n //= p
        result += 1
    return result


def core(n, primes):
    for p in primes:
        while n % p == 0:
            n //= p
    return n


def odd_step(n):
    check(n > 0 and n % 2 == 1, "ordinary odd domain")
    x = (3*n + 1)//2
    a = 1
    while x % 2 == 0:
        x //= 2
        a += 1
    return x, a


def main():
    sources = set(range(1, 1000, 2))
    # Force long division blocks and long valuation-one blocks separately.
    sources.update((4**k-1)//3 for k in (2, 5, 32, 128, 513))
    sources.update(2**k-1 for k in (3, 17, 65, 257, 1025))
    pools = ((2,3), (2,3,5,7,11))
    checks = 0
    defect_checks = 0
    degenerate_checks = 0
    max_a = 0
    gcd_checks = 0
    run_checks = 0
    for n in sorted(sources):
        n1,a = odd_step(n)
        max_a = max(max_a,a)
        m,m1=n+1,n1+1
        check(2**a*m1 == 3*m+2**a-2, "shifted identity")
        sigma=v(m,2)
        check((a==1)==(sigma>=2), "exact defect boundary")
        y=n
        for _ in range(sigma-1):
            y, exponent=odd_step(y)
            check(exponent==1, "full initial run")
            run_checks += 1
        check(odd_step(y)[1]>=2, "first non-one step")
        for P in pools:
            q,q1=core(m,P),core(m1,P)
            u,u1=m//q,m1//q1
            X=2**(a-1)
            Y=Fraction(3*q,2)*u
            Z=-q1*2**(a-1)*u1
            check(X+Y+Z==1, "unit equation")
            checks += 1
            if a>=2:
                check(all(z != 0 for z in (X,Y,Z,X+Y,X+Z,Y+Z,X+Y+Z)),
                      "all seven nonempty subsums")
                check(X+Z<0 and Y+Z<0 and X+Y>0, "sign proof")
                check((2**(a-1)-1)%gcd(q,q1)==0, "retained core gcd")
                defect_checks += 1
                gcd_checks += 1
            else:
                check(Y+Z==0 and q==q1, "excluded degenerate class")
                degenerate_checks += 1

    prefix_records=[]
    for start in (3,7,27,97,871,6171,77031,837799):
        seen=set()
        n=start
        D=0
        ell=(start+1-1).bit_length()
        K={core(n+1,(2,3))}
        transitions=set()
        edges=Counter()
        clock=0
        while n not in seen:
            seen.add(n)
            nxt,a=odd_step(n)
            if nxt in seen:
                break
            clock += 1
            q,q1=core(n+1,(2,3)),core(nxt+1,(2,3))
            K.add(q1)
            if a>=2:
                D += 1
                vector=(2**(a-1),(n+1)//q,2**(a-1)*(nxt+1)//q1)
                encoding=(q,q1,vector)
                check(encoding not in transitions, "injective simple-path encoding")
                transitions.add(encoding)
                edges[q,q1] += 1
            check(clock<ell*(2**(D+1)-1), "integer source-fixed clock")
            n=nxt
        prefix_records.append({"source":start,"simple_edges":clock,"defects":D,
                               "cores_including_endpoint":len(K),
                               "maximum_pair_multiplicity":max(edges.values(),default=0)})

    creation=[]
    for k in (1,2,4,12,60,120):
        n=2*3**(2*k)-1
        n1,a=odd_step(n)
        q1=(3**(2*k+1)+1)//4
        check(a==2 and core(n+1,(2,3))==1, "fixed-cost new core input")
        check(core(n1+1,(2,3))==q1, "fixed-cost new core output")
        if k%60==0:
            check(core(n1+1,(2,3,5,7,11,13))==q1, "prime pool avoidance")
        creation.append({"k":k,"new_core_bitlength":q1.bit_length()})

    # Every repeated occurrence of the trivial cycle is the same transition,
    # so no occurrence count is inferred from the distinct-solution theorem.
    n=1
    cycle=[]
    for _ in range(8):
        nxt,a=odd_step(n)
        cycle.append((n,nxt,a))
        n=nxt
    check(len(set(cycle))==1, "cycle occurrence/domain control")
    check(3**162<2**257, "published constant integer comparison")
    check(core(17+1,(2,3))==1 and core(odd_step(17)[0]+1,(2,3))==7,
          "terminal core must be counted")

    print(json.dumps({
        "schema":"collatz-shifted-core-independent/v1",
        "scope":"independent finite literal arithmetic; no numerical verification of the S-unit bound",
        "source_sha256":sha256(Path(__file__).read_bytes()).hexdigest(),
        "ordinary_sources":len(sources),"pool_transition_checks":checks,
        "nondegenerate_defect_checks":defect_checks,"degenerate_one_checks":degenerate_checks,
        "retained_core_gcd_checks":gcd_checks,"literal_one_run_edges":run_checks,
        "largest_odd_exponent":max_a,"prefixes":prefix_records,
        "new_core_family":creation,"domain_controls":3,"result":"PASS"
    },sort_keys=True,indent=2))


if __name__=="__main__":
    main()
