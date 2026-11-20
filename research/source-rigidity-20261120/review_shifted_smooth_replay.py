#!/usr/bin/env python3
"""Independent finite controls for the frozen shifted-smooth review.

No import of the author's checker, no unrestricted orbit census, and no
claim to execute the astronomical SC4 horizon.
"""
from hashlib import sha256
import argparse
import json
from pathlib import Path
import re
import subprocess
import sys


def need(ok, reason):
    if not ok:
        raise ValueError(reason)


def factor_out(n, p):
    need(type(n) is int and n > 0, "positive integer required")
    power = 0
    while n % p == 0:
        n //= p
        power += 1
    return power, n


def actual_odd_step(n):
    need(type(n) is int and n > 0 and n % 2, "positive odd input required")
    m = 3*n + 1
    a = 0
    while m % 2 == 0:
        m //= 2
        a += 1
    return m, a


def shifted_coordinates(n):
    s, m = factor_out(n+1, 2)
    t, q = factor_out(m, 3)
    return s, t, q


def run(packet):
    proof = packet / "SHIFTED_SMOOTH_CYCLES.md"
    checker = packet / "check_shifted_smooth_cycles.py"
    frozen = packet / "shifted-smooth-cycles-report.json"
    normal = subprocess.run([sys.executable, "-X", "utf8", "-B", str(checker)], check=True,
                            stdout=subprocess.PIPE).stdout
    optimized = subprocess.run([sys.executable, "-X", "utf8", "-B", "-OO", str(checker)],
                               check=True, stdout=subprocess.PIPE).stdout
    need(normal == optimized == frozen.read_bytes(), "author reports differ")

    text = proof.read_text(encoding="utf-8")
    tabulated = []
    for line in text.splitlines():
        if re.match(r"^\|\s*\d+\s*\|", line):
            cells = [cell.strip() for cell in line.strip("|").split("|")]
            tabulated.append([int(cell) for cell in cells[:5]])
    need(len(tabulated) == 15, "missing or extra table row")

    computed = []
    for k in range(1, 16):
        start = 2*3**(k-1)-1
        target, a = actual_odd_step(start)
        s, t, q = shifted_coordinates(target)
        b, rest = factor_out(3**k-1, 2)
        need(target == rest and a == b+1, "boundary value or exponent")
        computed.append([k, b, s, t, q])
    need(tabulated == computed, "written table differs from literal map")

    states = {2**s*3**(k-s)-1
              for k in range(1, 16) for s in range(1, k+1)}
    need(len(states) == 120, "nonunique shifted coordinates")
    reaching_one = []
    exit_paths = 0
    cycles = set()
    for start in sorted(states):
        path, seen, n = [], {}, start
        while n not in seen:
            if shifted_coordinates(n)[2] != 1:
                exit_paths += 1
                break
            need(n in states, "small table permits an unexpected high index")
            seen[n] = len(path)
            path.append(n)
            if n == 1:
                reaching_one.append(start)
                cycles.add((1,))
                break
            n, _ = actual_odd_step(n)
        else:
            cycle = path[seen[n]:]
            rotations = [tuple(cycle[i:] + cycle[:i]) for i in range(len(cycle))]
            cycles.add(min(rotations))
    need(reaching_one == [1, 3, 5, 15, 23, 35, 53], "wrong finite basin")
    need(cycles == {(1,)}, "extra cycle in small complement")
    need(exit_paths == 113, "small-complement accounting failed")

    run_cases = run_edges = 0
    for k in (1, 2, 4, 8, 15, 16, 31, 32):
        for s in range(1, k+1):
            t = k-s
            n = 2**s*3**t-1
            for j in range(s-1):
                n, a = actual_odd_step(n)
                need(a == 1, "wrong valuation in compressed run")
                need(shifted_coordinates(n) == (s-j-1, t+j+1, 1),
                     "index not preserved through run")
                run_edges += 1
            need(n == 2*3**(k-1)-1, "run failed to reach its boundary")
            _, a = actual_odd_step(n)
            need(a >= 2, "boundary is not the first non-one exponent")
            run_cases += 1

    valuation_controls = []
    for k in (1, 2, 3, 4, 6, 8, 12, 15, 16, 17, 24, 31, 32,
              33, 48, 63, 64, 96, 127, 128, 256, 512, 1024):
        b, _ = factor_out(3**k-1, 2)
        v, _ = factor_out(k, 2)
        need(b == (1 if k % 2 else 2+v), "valuation formula")
        if k >= 16:
            floor_log = k.bit_length()-1
            c, _ = factor_out(2**b-1, 3)
            need(c < b <= floor_log+2 < k, "strict valuation separation")
            need(3**k > 2**(k+1)*3**(b-1), "unbounded proof inequality control")
        valuation_controls.append(k)

    need(3**11 == 177147 and 2**17 == 131072, "base arithmetic")
    dyadic_controls = []
    for v in range(4, 13):
        need(3**(2**v) > 2**(2**v+1)*3**(v+1), "dyadic endpoint inequality")
        need(4*3**(2*v+2) > 2*3**(v+2), "induction squaring factor")
        dyadic_controls.append(v)

    target, _ = actual_odd_step(2*3**15-1)
    need(shifted_coordinates(target) == (1, 2, 37367),
         "omitted successor-core negative control")
    need(shifted_coordinates(17) == (1, 2, 1), "17 is initially in class")
    need(actual_odd_step(17)[0] == 13 and shifted_coordinates(13)[2] == 7,
         "initial smoothness does not imply continued smoothness")
    need((9*2**35)**81 == 2**2835*3**162 < 2**3092,
         "SC4 constant normalization")

    return {
        "status": "PASS",
        "proof_sha256": sha256(proof.read_bytes()).hexdigest(),
        "author_checker_sha256": sha256(checker.read_bytes()).hexdigest(),
        "author_report_sha256": sha256(normal).hexdigest(),
        "author_normal_optimized_frozen_reports_equal": True,
        "table_rows_reconstructed_from_actual_map": len(computed),
        "small_complement_states": len(states),
        "small_complement_sources_exiting": exit_paths,
        "small_complement_cycles": [list(c) for c in sorted(cycles)],
        "within_class_finite_basin": reaching_one,
        "independent_compressed_run_cases": run_cases,
        "independent_compressed_run_edges": run_edges,
        "valuation_control_indices": valuation_controls,
        "dyadic_control_exponents": dyadic_controls,
        "negative_controls": ["omitting successor core=1", "assuming class invariance from the initial state"],
        "scope": "Finite arithmetic controls and literal maps only. Universal SS1, cycle/basin deductions, and SC4 same-horizon reasoning are reconstructed in the written review; no external finiteness theorem or astronomical horizon is executed."
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path,
                        default=Path(__file__).resolve().parent,
                        help="directory containing the frozen author's proof, checker, and report")
    args = parser.parse_args()
    print(json.dumps(run(args.source_root), indent=2, sort_keys=True))
