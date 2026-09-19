#!/usr/bin/env python3
"""Independent exact certificate/inventory verifier; imports no project module.

Reconstructs CRT inputs through a different modulus, checks literal parity and
an independent affine endpoint, and rejects non-decreasing/echo certificates.
This is bounded computational evidence, not independent mathematical review.
"""
from __future__ import annotations
import argparse
from collections import Counter
from copy import deepcopy
from fractions import Fraction
import hashlib
import json
from pathlib import Path
from typing import Any

BASE = "ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def encoding(obj: Any) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("utf-8")


def equal(got: Any, expected: Any, message: str) -> None:
    require(encoding(got) == encoding(expected), message + " (including JSON types)")


def integer(x: Any, minimum: int = 0) -> None:
    require(type(x) is int and x >= minimum, "invalid integer/type")


def keys(obj: Any, names: str) -> None:
    require(type(obj) is dict and set(obj) == set(names.split()), "incorrect object keys")


def step(value: int) -> int:
    half, odd = divmod(value, 2)
    return 3*half+2 if odd else half


def run_steps(value: int, length: int) -> int:
    integer(value, 1); integer(length)
    require(length <= 100_000, "clock beyond declared verifier budget")
    for _ in range(length):
        value = step(value)
    return value


def physical(start: int, segments: Any) -> dict[str, int]:
    integer(start, 1)
    require(type(segments) is list, "segments must be a list")
    bits = []
    for segment in segments:
        require(type(segment) is list and len(segment) == 2, "invalid segment")
        word, repeat = segment
        require(type(word) is str and len(word) > 0 and all(b in "01" for b in word), "word")
        integer(repeat)
        require(len(bits)+len(word)*repeat <= 100_000, "replay budget")
        bits.extend(word*repeat)
    x, peak, low = start, start, None
    # Independently check the rational affine map represented by the whole word.
    multiplier, remainder, denominator = 1, 0, 1
    for b in bits:
        half, odd = divmod(x, 2)
        require(odd == (1 if b == "1" else 0), "physical parity mismatch")
        x = 3*half+2 if odd else half
        if odd:
            multiplier *= 3
            remainder = 3*remainder+denominator
        denominator *= 2
        peak = max(peak, x)
        low = x if low is None else min(low, x)
    quotient, rest = divmod(multiplier*start+remainder, denominator)
    require(rest == 0 and quotient == x, "affine/raw endpoint mismatch")
    return {"endpoint":x, "clock":len(bits), "peak":peak,
            "minimum_after_source":start if low is None else low}


def check_certificate(c: Any, specification: tuple[Any, ...] | None = None) -> None:
    keys(c, "source partner rule left right left_stats right_stats")
    n, m = c["source"], c["partner"]
    integer(n, 2); integer(m, 1)
    require(m < n, "partner is not below the ORIGINAL source")
    require(type(c["rule"]) is str and c["rule"], "rule label")
    if specification is not None:
        sn, sm, rule, left, right = specification
        equal([n,m,c["rule"],c["left"],c["right"]], [sn,sm,rule,left,right], "rule specification")
    left, right = physical(n,c["left"]), physical(m,c["right"])
    equal(c["left_stats"], left, "left statistics")
    equal(c["right_stats"], right, "right statistics")
    require(left["endpoint"] == right["endpoint"], "no exact meeting")


def odd_spec(n: int) -> tuple[Any, ...] | None:
    if n <= 1 or n % 2 == 0:
        return None
    u, r = n+1, 0
    while u % 2 == 0:
        u //= 2; r += 1
    if (3**r*u-1) % 4:
        return None
    return n,(n-1)//2,"odd-exit-half",[["1",r],["00",1]],[["1",r-1],["01",1]]


def block_parameters(n: int) -> tuple[int,int,int,int] | None:
    if n <= 5:
        return None
    u, k = n+5, 0
    while u % 8 == 0:
        u //= 8; k += 1
    if k == 0 or u % 2 == 0:
        return None
    a, depth = 9**k*u+1, 0
    while a % 2 == 0:
        a //= 2; depth += 1
    h = depth-4
    if h < 1 or (3**(h+1)*a-1) % 4:
        return None
    return k,u,h,a


def block_spec(n: int) -> tuple[Any, ...] | None:
    parameters = block_parameters(n)
    if parameters is None:
        return None
    k,u,h,a = parameters
    return n,(n-5)//2,"two-exit-half",[["110",k],["0100",1],["1",h],["00",1]],[["110",k-1],["1110000",1],["1",h-1],["01",1]]


def selected_spec(n: int) -> tuple[Any, ...] | None:
    if n == 1:
        return None
    if n % 2 == 0:
        return n,n//2,"even",[["0",1]],[]
    if n % 4 == 1:
        return n,(3*n+1)//4,"one-mod-four",[["10",1]],[]
    if n % 3 == 2:
        return n,(2*n-1)//3,"odd-ancestor",[],[["1",1]]
    if n % 9 == 4:
        return n,(8*n-5)//9,"110-ancestor",[],[["110",1]]
    return odd_spec(n) or block_spec(n)


def independent_crt(k: int, h: int, t: int) -> tuple[int,int,int]:
    # Solve for u modulo 3*2^(h+6), rather than a modulo 12*9^k.
    power, modulus = 9**k, 2**(h+6)
    odd_part_class = 1 if (h+1) % 2 == 0 else 3
    binary = ((2**(h+4)*odd_part_class-1)*pow(power,-1,modulus)) % modulus
    ternary = 1 if k % 2 else 2
    digit = ((ternary-binary)*pow(modulus,-1,3)) % 3
    u = binary+modulus*digit+3*modulus*t
    a, rem = divmod(power*u+1,2**(h+4))
    require(rem == 0 and a % 2 == 1, "independent CRT valuation")
    return 8**k*u-5,u,a


def symbolic_bridge() -> dict[str, Any]:
    # v=7+32t, t>=0; every state is an integer affine function of t.
    # Even coefficient + correct constant parity certifies the ENTIRE cylinder.
    def affine_walk(alpha: int, beta: int, word: str) -> tuple[Fraction,Fraction]:
        x,y=Fraction(alpha),Fraction(beta)
        for bit in word:
            require(x.denominator == y.denominator == 1 and x >= 0 and y > 0, "affine positive integrality")
            require(x.numerator % 2 == 0 and y.numerator % 2 == int(bit), "whole-cylinder parity")
            if bit == "1": x,y=3*x/2,(3*y+1)/2
            else: x,y=x/2,y/2
        require(x.denominator == y.denominator == 1, "final affine integrality")
        return x,y
    x=affine_walk(256,51,"1100100")
    y=affine_walk(128,23,"1110000")
    require(x == (Fraction(54),Fraction(11)) and y == (Fraction(27),Fraction(5)), "bridge endpoints")
    require(x[0] == 2*y[0] and x[1] == 2*y[1]+1, "whole affine half-source relation")
    require(81*9**22 > 128*8**23 and 81*9**21 <= 128*8**22, "threshold arithmetic")
    return {"cylinder":"v=7+32t, t>=0", "X":"54t+11", "Y":"27t+5", "threshold_bound":23}


def validate(envelope: Any) -> dict[str, Any]:
    keys(envelope,"payload sha256")
    p=envelope["payload"]
    require(type(envelope["sha256"]) is str and hashlib.sha256(encoding(p)).hexdigest() == envelope["sha256"], "digest")
    keys(p,"schema base odd_exit even_mersenne two_exit normalizer fixed_controls")
    equal([p["schema"],p["base"]],["AEM-001/v1",BASE],"schema/base")
    odd=p["odd_exit"]; keys(odd,"sources certificates unresolved")
    equal(odd["sources"],[3,8192],"odd range")
    yes=[n for n in range(3,8193,2) if odd_spec(n) is not None]
    no=[n for n in range(3,8193,2) if odd_spec(n) is None]
    equal([c["source"] for c in odd["certificates"]],yes,"odd complete success inventory")
    equal(odd["unresolved"],no,"odd complete miss inventory")
    for c in odd["certificates"]: check_certificate(c,odd_spec(c["source"]))

    mer=p["even_mersenne"]; keys(mer,"exponents certificates")
    equal(mer["exponents"],[2,256,2],"Mersenne range")
    equal([c["source"] for c in mer["certificates"]],[2**r-1 for r in range(2,257,2)],"Mersenne inventory")
    for c in mer["certificates"]: check_certificate(c,odd_spec(c["source"]))

    two=p["two_exit"]; keys(two,"crt_cases grid")
    expected_keys=[[k,h,t] for k in range(1,33) for h in range(1,17) for t in range(2)]
    expected_keys += [[k,h,t] for k in (48,64,128,256,1024) for h in (1,2,8,32,128,1024) for t in range(2)]
    equal([[r["k"],r["h"],r["t"]] for r in two["crt_cases"]],expected_keys,"CRT complete inventory")
    no_drop_cases=0
    for row in two["crt_cases"]:
        keys(row,"k h t u a certificate third_certificate")
        k,h,t=row["k"],row["h"],row["t"]
        n,u,a=independent_crt(k,h,t)
        equal([row["u"],row["a"],row["certificate"]["source"]],[u,a,n],"independent CRT")
        require(n % 12 == 3,"old residual class")
        equal(block_parameters(n),(k,u,h,a),"actual input parameters")
        c=row["certificate"]; check_certificate(c,block_spec(n))
        equal([c["left_stats"]["clock"],c["right_stats"]["clock"]],[3*k+h+6,3*k+h+5],"two clocks")
        equal(c["left_stats"]["endpoint"],(3**(h+1)*a-1)//4,"closed endpoint")
        third=row["third_certificate"]
        check_certificate(third,(n,n//3-2,"two-exit-third",c["left"],[["1",1]]+c["right"]))
        require(third["left_stats"]["clock"] == third["right_stats"]["clock"],"equal-clock composition")
        if k >= 2:
            require((n//3-2) % 32 == 7,"reduced source has a three-odd hard exit")
        if k >= 23:
            require(c["left_stats"]["minimum_after_source"] > n,"no forward descent on declared arm")
            no_drop_cases += 1
    grid=two["grid"];keys(grid,"k u certificates unresolved")
    equal([grid["k"],grid["u"]],[[1,24],[1,255,2]],"grid ranges")
    successes,misses=[],[]
    for k in range(1,25):
        for u in range(1,256,2):
            (successes if block_spec(8**k*u-5) else misses).append([k,u])
    equal([[r["k"],r["u"]] for r in grid["certificates"]],successes,"complete grid successes")
    equal(grid["unresolved"],misses,"complete grid misses")
    for row in grid["certificates"]:
        keys(row,"k u certificate")
        check_certificate(row["certificate"],block_spec(8**row["k"]*row["u"]-5))

    norm=p["normalizer"];keys(norm,"sources rows counts rule_uses")
    equal(norm["sources"],[2,4096],"normalizer range")
    equal([r["source"] for r in norm["rows"]],list(range(2,4097)),"normalizer complete inventory")
    counts,rules=Counter(),Counter()
    for row in norm["rows"]:
        keys(row,"source terminal status clocks meeting chain")
        current=row["source"]; A=B=0
        for cert in row["chain"]:
            spec=selected_spec(current)
            require(spec is not None,"selector should have stopped")
            check_certificate(cert,spec)
            a,b=cert["left_stats"]["clock"],cert["right_stats"]["clock"]
            A,B=A+max(0,a-B),b+max(0,B-a)
            rules[cert["rule"]]+=1
            current=cert["partner"]
        require(current == 1 or selected_spec(current) is None,"premature unresolved output")
        status="CORE" if current == 1 else "UNRESOLVED"
        equal([row["terminal"],row["status"],row["clocks"]],[current,status,[A,B]],"chain terminal/clocks")
        left=run_steps(row["source"],A);right=run_steps(current,B)
        require(left == right,"composed raw physical meeting")
        equal(row["meeting"],left,"chain endpoint")
        counts[status]+=1
    equal(norm["counts"],dict(counts),"normalizer counts")
    equal(norm["rule_uses"],dict(rules),"normalizer rule accounting")
    equal(p["fixed_controls"],{
        "invalid_echo":{"source":7,"partner":11,"left":[["11",1]],"right":[["1",1]]},
        "bad_final_guard":{"k":2,"u":47,"n":3003},
        "missing_bridge_guard":{"k":2,"u":5,"n":315},
        "minimum_k_no_forward_descent_bound":23},"fixed controls")
    require(block_spec(315) is None and block_spec(3003) is None,"failed guards")
    require(physical(7,[["11",1]])["endpoint"] == physical(11,[["1",1]])["endpoint"],"echo is a real meeting")
    return {"status":"PASS", "semantic_sha256":envelope["sha256"], "odd_exit_certificates":len(yes),
            "even_mersenne_certificates":len(mer["certificates"]),"two_exit_crt_cases":len(expected_keys),
            "no_forward_descent_crt_cases":no_drop_cases,"equal_clock_third_certificates":len(expected_keys),"two_exit_grid_certificates":len(successes),
            "normalizer_counts":dict(counts),"symbolic_bridge":symbolic_bridge()}


def self_test(envelope: dict[str,Any]) -> dict[str,Any]:
    # All altered envelopes are re-sealed: rejecting a stale hash is not the test.
    mutations=[]
    def add(name: str, mutate: Any) -> None:
        mutations.append((name,mutate))
    def first(p:dict[str,Any]) -> dict[str,Any]: return p["odd_exit"]["certificates"][0]
    add("schema",lambda p:p.__setitem__("schema","other"))
    add("source boolean alias",lambda p:first(p).__setitem__("partner",True))
    add("integral float alias",lambda p:first(p).__setitem__("partner",1.0))
    add("repeat boolean alias",lambda p:first(p)["left"][1].__setitem__(1,True))
    add("clock corruption",lambda p:first(p)["left_stats"].__setitem__("clock",5))
    add("endpoint corruption",lambda p:first(p)["right_stats"].__setitem__("endpoint",3))
    add("peak corruption",lambda p:first(p)["left_stats"].__setitem__("peak",999))
    add("parity corruption",lambda p:first(p)["left"].__setitem__(0,["0",2]))
    add("nondecreasing partner",lambda p:first(p).__setitem__("partner",3))
    add("nonpositive partner",lambda p:first(p).__setitem__("partner",0))
    add("omitted certificate",lambda p:p["odd_exit"]["certificates"].pop(0))
    add("duplicated certificate",lambda p:p["odd_exit"]["certificates"].insert(0,deepcopy(first(p))))
    add("lost unresolved source",lambda p:p["odd_exit"]["unresolved"].pop())
    add("false source pin",lambda p:p.__setitem__("base","0"*40))
    add("CRT source parameter",lambda p:p["two_exit"]["crt_cases"][0].__setitem__("u",105))
    add("CRT valuation length",lambda p:p["two_exit"]["crt_cases"][0].__setitem__("h",2))
    add("two-exit physical word",lambda p:p["two_exit"]["crt_cases"][0]["certificate"]["right"].__setitem__(1,["111000",1]))
    add("one-third source",lambda p:p["two_exit"]["crt_cases"][0]["third_certificate"].__setitem__("partner",272))
    add("no-forward minimum",lambda p:p["two_exit"]["crt_cases"][704]["certificate"]["left_stats"].__setitem__("minimum_after_source",1))
    add("grid coverage omission",lambda p:p["two_exit"]["grid"]["unresolved"].pop())
    rejected=[]
    for name,mutate in mutations:
        changed=deepcopy(envelope)
        mutate(changed["payload"])
        changed["sha256"]=hashlib.sha256(encoding(changed["payload"])).hexdigest()
        try: validate(changed)
        except (ValueError,KeyError,TypeError): rejected.append(name)
        else: raise ValueError("resealed corruption accepted: "+name)
        del changed
    # Real meetings that do not descend, and one positive but illegal path.
    def bare(n:int,m:int,left:list,right:list) -> dict[str,Any]:
        return {"source":n,"partner":m,"rule":"adversarial-control","left":left,"right":right,
                "left_stats":physical(n,left),"right_stats":physical(m,right)}
    bad=[("retracing 7->11->17",bare(7,11,[["11",1]],[["1",1]])),
         ("mixed-rank 11->17",bare(11,17,[["1",1]],[])),
         ("equal-source zero progress",bare(7,7,[],[]))]
    for name,c in bad:
        try: check_certificate(c)
        except ValueError: rejected.append(name)
        else: raise ValueError("non-progress accepted: "+name)
    try: physical(7,[["0",1]])
    except ValueError: rejected.append("positive but illegal parity")
    else: raise ValueError("illegal parity accepted")
    # Successful cross-direction composition: 3 -> 1 shares state 2.
    valid=envelope["payload"]["odd_exit"]["certificates"][0]
    check_certificate(valid)
    return {"resealed_mutations_rejected":len(mutations),"direct_bad_controls_rejected":4,"names":rejected}


def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("artifact",type=Path)
    parser.add_argument("--self-test",action="store_true")
    args=parser.parse_args()
    artifact=json.loads(args.artifact.read_text(encoding="utf-8"))
    result=validate(artifact)
    if args.self_test:result["self_test"]=self_test(artifact)
    print(json.dumps(result,sort_keys=True,indent=2))

if __name__ == "__main__":
    main()
