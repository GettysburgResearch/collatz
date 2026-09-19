#!/usr/bin/env python3
"""Exact, bounded source-merging experiments. Standard library only.

This is a terminating PARTIAL selector, not a proof of complete coverage.
All physical certificates use the unabsorbed shortcut map, including 1->2->1.
The independent verifier does not import this module.
"""
from __future__ import annotations
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
from typing import Any

BASE = "ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a"
SCHEMA = "AEM-001/v1"


def need(ok: bool, why: str) -> None:
    if not ok:
        raise ValueError(why)


def positive(n: int) -> None:
    need(type(n) is int and n > 0, "expected positive integer (not bool/float)")


def T(n: int) -> int:
    return (3*n+1)//2 if n & 1 else n//2


def v2(n: int) -> int:
    positive(n)
    return (n & -n).bit_length()-1


def serial(data: Any) -> bytes:
    return json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode()


def digest(data: Any) -> str:
    return hashlib.sha256(serial(data)).hexdigest()


def walk(n: int, segments: list[list[Any]]) -> dict[str, int]:
    positive(n)
    x, clock, peak, low = n, 0, n, None
    for word, repeats in segments:
        need(type(word) is str and word and set(word) <= {"0", "1"}, "invalid word")
        need(type(repeats) is int and repeats >= 0, "invalid repeat count")
        need(clock + len(word)*repeats <= 100_000, "finite replay budget exceeded")
        for _ in range(repeats):
            for bit in word:
                need(x % 2 == int(bit), "illegal physical parity")
                x = T(x)
                clock += 1
                peak = max(peak, x)
                low = x if low is None else min(low, x)
    return {"endpoint": x, "clock": clock, "peak": peak,
            "minimum_after_source": n if low is None else low}


def certificate(n: int, m: int, left: list[list[Any]], right: list[list[Any]], rule: str) -> dict[str, Any]:
    positive(n); positive(m)
    need(m < n, "not lower than the ORIGINAL source")
    l, r = walk(n, left), walk(m, right)
    need(l["endpoint"] == r["endpoint"], "no shared state")
    return {"source": n, "partner": m, "rule": rule,
            "left": left, "right": right, "left_stats": l, "right_stats": r}


def good_odd_exit(n: int) -> dict[str, Any] | None:
    positive(n)
    if n <= 1 or n % 2 == 0:
        return None
    r = v2(n+1)
    u = (n+1) >> r
    if pow(3, r, 4)*u % 4 != 1:
        return None
    return certificate(n, (n-1)//2,
                       [["1", r], ["00", 1]],
                       [["1", r-1], ["01", 1]], "odd-exit-half")


def block_exit(n: int) -> dict[str, Any] | None:
    """AEM-003: k and h are read from the given input, not guessed futures."""
    positive(n)
    depth = v2(n+5)
    if n <= 5 or depth < 3 or depth % 3:
        return None
    k, u = depth//3, (n+5) >> depth
    z = 9**k*u+1
    s = v2(z)
    if s < 5:
        return None
    h, a = s-4, z >> s
    if pow(3, h+1, 4)*a % 4 != 1:
        return None
    cert = certificate(n, (n-5)//2,
                       [["110", k], ["0100", 1], ["1", h], ["00", 1]],
                       [["110", k-1], ["1110000", 1], ["1", h-1], ["01", 1]],
                       "two-exit-half")
    need(cert["left_stats"]["endpoint"] == (3**(h+1)*a-1)//4, "closed endpoint")
    return cert


def family(k: int, h: int, t: int) -> tuple[int, int, int]:
    """Construct test inputs, with 3|n. This construction is not a selector."""
    positive(k); positive(h)
    need(type(t) is int and t >= 0, "invalid translate")
    p = 9**k
    modulus = 3*p
    epsilon = 1 if k % 2 else -1
    a0 = ((1+epsilon*p)*pow(2**(h+4), -1, modulus)) % modulus
    lift = ((pow(3, h+1, 4)-a0)*pow(modulus, -1, 4)) % 4
    a = a0 + modulus*lift + 4*modulus*t
    u, rem = divmod(2**(h+4)*a-1, p)
    need(rem == 0 and u > 0 and u % 2 == 1, "CRT construction")
    n = 8**k*u-5
    need(n % 12 == 3, "residual family")
    return n, u, a


def choose(n: int) -> dict[str, Any] | None:
    """Every accepted rule uses ordinary source order, never mixed ranks."""
    positive(n)
    if n == 1:
        return None
    if not n & 1:
        return certificate(n, n//2, [["0", 1]], [], "even")
    if n % 4 == 1:
        return certificate(n, (3*n+1)//4, [["10", 1]], [], "one-mod-four")
    if n % 3 == 2:
        return certificate(n, (2*n-1)//3, [], [["1", 1]], "odd-ancestor")
    if n % 9 == 4:
        return certificate(n, (8*n-5)//9, [], [["110", 1]], "110-ancestor")
    return good_odd_exit(n) or block_exit(n)


def normalize(n: int) -> dict[str, Any]:
    positive(n)
    root, current, chain = n, n, []
    A = B = 0  # T^A(root) = T^B(current)
    while current != 1:
        c = choose(current)
        if c is None:
            break
        chain.append(c)
        a, b = c["left_stats"]["clock"], c["right_stats"]["clock"]
        align = max(B, a)
        A, B = A + align-B, b + align-a
        current = c["partner"]
    left, right = root, current
    for _ in range(A): left = T(left)
    for _ in range(B): right = T(right)
    need(left == right, "composed physical clocks")
    return {"source": root, "terminal": current,
            "status": "CORE" if current == 1 else "UNRESOLVED",
            "clocks": [A, B], "meeting": left, "chain": chain}


def family_keys() -> list[tuple[int, int, int]]:
    small = [(k,h,t) for k in range(1,33) for h in range(1,17) for t in range(2)]
    large = [(k,h,t) for k in (48,64,128,256,1024) for h in (1,2,8,32,128,1024) for t in range(2)]
    return small+large


def build() -> dict[str, Any]:
    odd_certificates = []
    odd_misses = []
    for n in range(3,8193,2):
        c = good_odd_exit(n)
        if c is None: odd_misses.append(n)
        else: odd_certificates.append(c)
    mersennes = [good_odd_exit(2**r-1) for r in range(2,257,2)]
    need(all(c is not None for c in mersennes), "even Mersenne guard")

    rows = []
    for k,h,t in family_keys():
        n,u,a = family(k,h,t)
        c = block_exit(n)
        need(c is not None, "family missing")
        need(c["left_stats"]["clock"] == 3*k+h+6, "left clock")
        need(c["right_stats"]["clock"] == 3*k+h+5, "right clock")
        if k >= 23:
            need(c["left_stats"]["minimum_after_source"] > n, "no-forward-descent assertion")
        third = certificate(n, n//3-2, c["left"], [["1",1]]+c["right"], "two-exit-third")
        need(third["left_stats"]["clock"] == third["right_stats"]["clock"], "equal-clock composition")
        rows.append({"k":k, "h":h, "t":t, "u":u, "a":a, "certificate":c,
                     "third_certificate":third})

    grid_yes, grid_no = [], []
    for k in range(1,25):
        for u in range(1,256,2):
            n=8**k*u-5
            c=block_exit(n)
            if c is None: grid_no.append([k,u])
            else: grid_yes.append({"k":k,"u":u,"certificate":c})

    norms=[normalize(n) for n in range(2,4097)]
    counts=Counter(r["status"] for r in norms)
    rules=Counter(c["rule"] for r in norms for c in r["chain"])
    payload={"schema":SCHEMA,"base":BASE,
             "odd_exit":{"sources":[3,8192],"certificates":odd_certificates,"unresolved":odd_misses},
             "even_mersenne":{"exponents":[2,256,2],"certificates":mersennes},
             "two_exit":{"crt_cases":rows,"grid":{"k":[1,24],"u":[1,255,2],
                                                       "certificates":grid_yes,"unresolved":grid_no}},
             "normalizer":{"sources":[2,4096],"rows":norms,"counts":dict(counts),"rule_uses":dict(rules)},
             "fixed_controls":{"invalid_echo":{"source":7,"partner":11,"left":[["11",1]],"right":[["1",1]]},
                               "bad_final_guard":{"k":2,"u":47,"n":3003},
                               "missing_bridge_guard":{"k":2,"u":5,"n":315},
                               "minimum_k_no_forward_descent_bound":23}}
    return {"payload":payload,"sha256":digest(payload)}


def summary(envelope: dict[str, Any]) -> dict[str, Any]:
    p=envelope["payload"]
    return {"status":"PASS","semantic_sha256":envelope["sha256"],
            "odd_exit_certificates":len(p["odd_exit"]["certificates"]),
            "odd_exit_unresolved":len(p["odd_exit"]["unresolved"]),
            "even_mersenne_certificates":len(p["even_mersenne"]["certificates"]),
            "two_exit_crt_cases":len(p["two_exit"]["crt_cases"]),
            "equal_clock_third_certificates":len(p["two_exit"]["crt_cases"]),
            "two_exit_grid_certificates":len(p["two_exit"]["grid"]["certificates"]),
            "two_exit_grid_unresolved":len(p["two_exit"]["grid"]["unresolved"]),
            "normalizer":p["normalizer"]["counts"],
            "normalizer_rules":p["normalizer"]["rule_uses"]}


def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path)
    parser.add_argument("--check",type=Path)
    parser.add_argument("--source",type=int)
    parser.add_argument("--example",type=int,nargs=3,metavar=("K","H","T"))
    args=parser.parse_args()
    if args.source is not None:
        print(json.dumps(normalize(args.source),sort_keys=True,indent=2));return
    if args.example is not None:
        n,u,a=family(*args.example)
        c=block_exit(n)
        need(c is not None,"constructed example unexpectedly unresolved")
        third=certificate(n,n//3-2,c["left"],[["1",1]]+c["right"],"two-exit-third")
        print(json.dumps({"parameters":args.example,"u":u,"a":a,"certificate":c,
                          "third_certificate":third},sort_keys=True,indent=2));return
    envelope=build()
    if args.check:
        observed=json.loads(args.check.read_text())
        need(serial(observed)==serial(envelope),"artifact mismatch, including exact JSON types")
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_bytes(serial(envelope)+b"\n")
    print(json.dumps(summary(envelope),sort_keys=True,indent=2))

if __name__=="__main__":
    main()
