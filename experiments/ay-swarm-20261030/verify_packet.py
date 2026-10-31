#!/usr/bin/env python3
"""Independent cross-track checks and optional exact artifact replay.

No implementation module from the research tracks is imported. This checks
finite instances and bytes; the universal arguments remain in the notes.
"""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
from itertools import product
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import time

ROOT = Path(__file__).resolve().parents[2]
FOLDER = Path(__file__).resolve().parent
RULES = {"ad": "d", "bd": "gd", "ae": "ea", "af": "eb", "ag": "fa",
         "be": "fb", "bf": "ga", "bg": "gb", "ce": "cb", "cf": "caa", "cg": "cab"}
BASE_DIGIT = {"a": (2, 0), "b": (2, 1), "e": (3, 0), "f": (3, 1), "g": (3, 2)}


def require(test, message):
    if not test:
        raise ValueError(message)


def v2(n):
    require(n > 0, "positive valuation argument required")
    return (n & -n).bit_length() - 1


def scan(word):
    n, h = 1, 0
    for symbol in word[1:-1]:
        base, digit = BASE_DIGIT[symbol]
        h += n.bit_length() if base == 3 else 0
        n = base * n + digit
    return n, h


def rank(word):
    n, h = scan(word)
    q = v2(n)
    m = n >> q
    s = m.bit_count()
    return (s * (s - 1) // 2 + v2(m + 1), q, h)


def source_guard(n):
    bits = bin(n)[2:][::-1]
    runs = []
    for bit in bits:
        if runs and runs[-1][0] == bit:
            runs[-1] = (bit, runs[-1][1] + 1)
        else:
            runs.append((bit, 1))
    carry, positive, negative = 1, 0, 0
    for bit, length in runs:
        if length == 1:
            positive += bit == "1" and carry == 0
            negative += bit == "0" and carry == 1
        else:
            carry = int(bit)
    return positive < negative or (positive == negative and v2(n + 1) >= 2)


def joint_order_checks():
    counts = Counter()
    words = 0
    for length in range(5):
        for digits in product(BASE_DIGIT, repeat=length):
            source = "c" + "".join(digits) + "d"
            n, _ = scan(source)
            words += 1
            for i in range(len(source) - 1):
                lhs = source[i:i + 2]
                if lhs not in RULES:
                    continue
                target = source[:i] + RULES[lhs] + source[i + 2:]
                before, after = rank(source), rank(target)
                if lhs == "bd":
                    admitted = source_guard(n)
                    require((after < before) if admitted else (after > before),
                            f"joint odd rank failed at {source}")
                    counts["guarded_odd" if admitted else "unguarded_odd_increase"] += 1
                else:
                    require(after < before, f"joint rank failed at {source}/{lhs}")
                    counts["even" if lhs == "ad" else "auxiliary"] += 1
                counts["rule:" + lhs] += 1
    return {"proper_words": words, "counts": dict(sorted(counts.items()))}


def independent_fibres(limit):
    """Literal forward word construction, no division-DAG implementation."""
    output = {n: [] for n in range(1, limit + 1)}
    todo = [(1, (0, 0, 0, 0, 0))]
    while todo:
        n, vector = todo.pop()
        output[n].append(vector)
        for i, (base, digit) in enumerate(BASE_DIGIT.values()):
            m = base * n + digit
            if m <= limit:
                v = list(vector)
                v[i] += 1
                todo.append((m, tuple(v)))
    return output


def additive_table_checks():
    fibres = independent_fibres(23)
    checks = 0
    for costs in product(range(5), repeat=5):
        a, b, e, f, g = costs
        x, z = min(b, e), min(2*b, b+e, a+f)
        table = {3:x, 5:min(a+b,g), 7:z,
                 9:min(2*e,b+f,b+e,2*a+b), 11:min(g+x,a+2*b),
                 13:min(2*f,a+b+x,2*a+f),
                 15:min(e+g,3*b,2*b+e,a+b+f,a+b+e),
                 17:min(2*g,a+b+g,a+b+f,3*a+b), 23:min(g+z,a+3*b)}
        for n, expected in table.items():
            literal = min(sum(w*c for w,c in zip(vector,costs)) for vector in fibres[n])
            require(literal == expected, "complete cost formula mismatch")
            checks += 1
        necessary = (table[3] >= table[5] and table[7] >= table[11]
                     and table[9] > table[7] and table[15] >= table[23]
                     and table[17] > table[13])
        require(not necessary, "finite tuple contradicts all-weight proof")
    return {"cost_tuples": 5**5, "exact_formula_checks": checks,
            "scope": "finite formula checks; the all-real theorem is proved in the note"}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def source_identities():
    paths = sorted((ROOT / "research/ay-swarm-20261030").glob("*.md"))
    paths += sorted(FOLDER.glob("*.py"))
    return {str(p.relative_to(ROOT)): {"sha256": sha(p.read_bytes()),
            "git_blob": hashlib.sha1(b"blob " + str(p.stat().st_size).encode()
                                     + b"\0" + p.read_bytes()).hexdigest()} for p in paths}


def replay_artifacts():
    cases = [("orders.py", "orders-results.json"),
             ("carry_geometry.py", "carry-results.json"),
             ("srs_semantics.py", "semantics-results.json"),
             ("representation_dag.py", "representation-results.json")]
    receipts = []
    with tempfile.TemporaryDirectory(prefix="ay-swarm-replay-") as tmp:
        for script, artifact in cases:
            expected = (FOLDER / artifact).read_bytes()
            for optimized in (False, True):
                target = Path(tmp) / (script + (".optimized" if optimized else ".normal") + ".json")
                argv = [sys.executable, "-X", "utf8", "-B"]
                if optimized:
                    argv.append("-O")
                argv += [str(FOLDER / script), "--output", str(target)]
                start = time.monotonic()
                result = subprocess.run(argv, cwd=ROOT, capture_output=True, timeout=240)
                require(result.returncode == 0, f"replay failed: {script}: {result.stderr.decode()}")
                actual = target.read_bytes()
                require(actual == expected, f"replay bytes differ: {script}, optimized={optimized}")
                receipts.append({"script": script, "optimized": optimized,
                                 "exit_code": result.returncode,
                                 "seconds": round(time.monotonic() - start, 3),
                                 "artifact": artifact, "artifact_sha256": sha(actual),
                                 "matches_recorded_artifact": True})
                print(f"PASS {script} optimized={optimized}", file=sys.stderr, flush=True)
    return receipts


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--replay", action="store_true", help="run all four author programs normally and under -O")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = {"schema": "ay-swarm-verification/v1", "status": "PASS",
              "scope": "finite independent checks and optional exact-byte replay; not a Collatz proof",
              "joint_microscopic_order": joint_order_checks(),
              "additive_cost_table": additive_table_checks()}
    if args.replay:
        result["execution_started_utc"] = datetime.now(timezone.utc).isoformat()
        result["replays"] = replay_artifacts()
        result["execution_finished_utc"] = datetime.now(timezone.utc).isoformat()
    result["source_identities"] = source_identities()
    body = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(body, encoding="utf-8")
    else:
        print(body, end="")


if __name__ == "__main__":
    main()
