#!/usr/bin/env python3
"""Exact controls for SS1--SS3; no S-unit theorem or unrestricted census."""
from hashlib import sha256
import json
from pathlib import Path


def require(condition, message):
    if not condition:
        raise ValueError(message)


def v_p(n, p):
    require(type(n) is int and n > 0, "positive integer domain")
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def odd_step(n):
    require(n > 0 and n % 2 == 1, "positive odd source")
    y = 3*n + 1
    return y >> v_p(y, 2)


def coordinates(n):
    m = n + 1
    s = v_p(m, 2)
    m >>= s
    t = v_p(m, 3)
    return s, t, m // (3 ** t)


def boundary_row(k):
    source = 2 * 3 ** (k - 1) - 1
    b = v_p(3 ** k - 1, 2)
    target = odd_step(source)
    require(target == (3 ** k - 1) >> b, "boundary formula")
    require(v_p(3 * source + 1, 2) == b + 1, "boundary clock shift")
    s, t, q = coordinates(target)
    require(3 ** k + 2 ** b - 1 == 2 ** (b + s) * 3 ** t * q,
            "complete shifted factorization")
    expected_b = 1 if k % 2 else 2 + v_p(k, 2)
    require(b == expected_b, "LTE formula")
    return [k, b, s, t, q]


def main():
    rows = [boundary_row(k) for k in range(1, 16)]
    smooth = [[k, s + t] for k, b, s, t, q in rows if q == 1]
    require(smooth == [[1, 1], [2, 1], [4, 2]], "small transition graph")
    require(3 ** 11 > 2 ** 17, "dyadic induction base")

    # These are additional arithmetic controls, not a claimed exhaustive search.
    large_indices = [16, 17, 18, 31, 32, 48, 64, 96, 128, 256, 512, 1024]
    for k in large_indices:
        k, b, s, t, q = boundary_row(k)
        v = k.bit_length() - 1
        require(b <= v + 2 < k, "large valuation upper bound")
        require(t == v_p(2 ** b - 1, 3) < b, "ternary valuation comparison")
        require(3 ** k > 2 ** (k + 1) * 3 ** (b - 1), "large growth inequality")
        require(q != 1 or s + t > k, "class-preserving growth implication")

    for v in range(4, 11):
        require(3 ** (2 ** v) > 2 ** (2 ** v + 1) * 3 ** (v + 1),
                "dyadic induction certificate")
        require(2 * 3 ** v > 1, "squaring implication factor")

    run_edges = 0
    for k in range(1, 16):
        for s in range(1, k + 1):
            t = k - s
            n = 2 ** s * 3 ** t - 1
            for j in range(s - 1):
                require(v_p(3*n + 1, 2) == 1, "run uses valuation one")
                n = odd_step(n)
                require(n + 1 == 2 ** (s-j-1) * 3 ** (t+j+1), "exact run")
                run_edges += 1
            require(n == 2 * 3 ** (k-1) - 1, "run boundary index")
            require(v_p(3*n + 1, 2) >= 2, "run actually ends")

    basin = sorted(2 ** s * 3 ** (k-s) - 1
                   for k in [1, 2, 4] for s in range(1, k+1))
    require(basin == [1, 3, 5, 15, 23, 35, 53], "seven-state set")
    paths = []
    for source in basin:
        path = [source]
        while path[-1] != 1:
            require(len(path) < 8, "small certificate did not terminate")
            require(coordinates(path[-1])[2] == 1, "within-class certificate")
            path.append(odd_step(path[-1]))
        require(all(coordinates(n)[2] == 1 for n in path), "complete smooth path")
        paths.append(path)

    # k=16 gives s'+t'=3<16 because its successor core is 37367.
    _, _, s, t, q = boundary_row(16)
    require(q == 37367 and s+t == 3, "negative omitted-core control")
    require(coordinates(odd_step(17))[2] == 7, "smooth starts need not stay smooth")

    print(json.dumps({
        "status": "PASS: finite exact controls for the written elementary proof",
        "proof_sha256": sha256(Path(__file__).with_name("SHIFTED_SMOOTH_CYCLES.md").read_bytes()).hexdigest(),
        "complete_small_boundary_table": rows,
        "small_class_preserving_transitions": smooth,
        "induction_base": {"3^11": 3 ** 11, "2^17": 2 ** 17},
        "additional_large_indices": large_indices,
        "exact_valuation_one_run_edges": run_edges,
        "within_class_paths_to_one": paths,
        "negative_controls": [
            "dropping successor core=1 makes the large-index claim false",
            "a shifted-smooth initial state can immediately leave the class",
        ],
        "scope": [
            "The table is complete only for 1<=k<=15; larger indices use the written inequality.",
            "No search for all high class-preserving transitions is performed.",
            "No external S-unit theorem or enormous deadline is verified computationally.",
            "No unrestricted Collatz conclusion is claimed.",
        ],
    }, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
