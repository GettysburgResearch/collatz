#!/usr/bin/env python3
"""Find and independently check finite semiprime merger certificates.

The bounded command makes no promise that the selected limits suffice. The
written theorem proves that the unrestricted dovetail eventually succeeds,
using explicitly named external analytic inputs. No conjectural orbit
convergence, floating-point logarithm, or probable-prime test is used here.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from math import isqrt
from pathlib import Path


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def step(n: int) -> int:
    require(n > 0, "The source must be positive")
    return (3 * n + 1) // 2 if n % 2 else n // 2


def prime(n: int) -> bool:
    """Deterministic trial division, for a finite certificate consumer."""
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    return all(n % d for d in range(3, isqrt(n) + 1, 2))


def unit_prefix(n: int) -> list[int]:
    require(n > 0, "The source must be positive")
    result = [n]
    while result[-1] % 3 == 0:
        result.append(step(result[-1]))
    return result


def member(n: int, p: int, q: int) -> bool:
    b = n.bit_length()
    return (b >= 4 and n == p * q and p < q and prime(p) and prime(q)
            and b < p and 4 * p <= b * b)


def check_path(path: list[int]) -> None:
    require(bool(path), "Empty path")
    require(all(isinstance(n, int) and n > 0 for n in path), "Nonpositive state")
    require(all(step(x) == y for x, y in zip(path, path[1:])), "Invalid edge")


def check_certificate(record: dict) -> None:
    start, n, p, q = (record[k] for k in ("start", "representative", "p", "q"))
    first, second = record["start_path"], record["representative_path"]
    require(member(n, p, q), "Not in the exact integer semiprime family")
    check_path(first)
    check_path(second)
    require(first[0] == start and second[0] == n, "Wrong path origin")
    require(first[-1] == second[-1] == record["meeting_value"], "No actual merger")
    require(first[-1] % 3 != 0, "The normalized target is not a unit modulo three")


def candidates(maximum: int):
    """Yield each candidate exactly once, with its verified factor pair."""
    require(maximum >= 1, "Nonpositive maximum")
    bound = maximum.bit_length() ** 2 // 4
    rows = []
    for p in range(3, bound + 1, 2):
        if not prime(p):
            continue
        for q in range(p + 2, maximum // p + 1, 2):
            n = p * q
            if member(n, p, q):
                rows.append((n, p, q))
    return sorted(rows)


def bounded_search(starts: list[int], maximum: int, steps: int) -> dict:
    require(steps >= 0, "Negative step bound")
    prefixes = {n: unit_prefix(n) for n in starts}
    pending = set(starts)
    records = []
    examined = 0
    for n, p, q in candidates(maximum):
        if not pending:
            break
        examined += 1
        path, seen = [n], {n}
        for date in range(steps + 1):
            matched = [a for a in sorted(pending) if prefixes[a][-1] == path[-1]]
            for a in matched:
                record = dict(start=a, representative=n, p=p, q=q,
                              meeting_value=path[-1], start_path=prefixes[a],
                              representative_path=list(path))
                check_certificate(record)
                records.append(record)
                pending.remove(a)
            if date == steps or not pending:
                break
            following = step(path[-1])
            if following in seen:
                break
            seen.add(following)
            path.append(following)
    return dict(success=not pending, unresolved=sorted(pending),
                candidates_examined=examined, certificates=records,
                maximum_representative=maximum, maximum_steps=steps)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("starts", nargs="+", type=int)
    parser.add_argument("--maximum", type=int, default=65536)
    parser.add_argument("--steps", type=int, default=512)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = bounded_search(args.starts, args.maximum, args.steps)
    result.update(schema="collatz-exact-semiprime-representative/v1",
                  recorded_utc=datetime.now(timezone.utc).isoformat(),
                  script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  scope="Finite ordinary merger certificates only. The unrestricted search's source-qualified termination theorem is written; bounded success is not universal convergence or a complexity bound.")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"success": result["success"], "unresolved": result["unresolved"],
                      "candidates_examined": result["candidates_examined"],
                      "certificates": [{"start": x["start"], "representative": x["representative"],
                                        "meeting": x["meeting_value"],
                                        "clocks": [len(x["start_path"]) - 1,
                                                   len(x["representative_path"]) - 1]}
                                       for x in result["certificates"]]}))


if __name__ == "__main__":
    main()
