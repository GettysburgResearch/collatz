#!/usr/bin/env python3
"""Exact structured-counterexample audit for the H renewal system.

This is a finite search only. It:
1. checks the zero-carry descent identities for compiler suffixes 10 and 30;
2. enumerates canonical centered stars in a finite (a,R,t) box;
3. iterates the exact renewal map, recording cycles and the longest renewal life.

Standard library only.
"""
from __future__ import annotations
import argparse, hashlib, json
from dataclasses import asdict, dataclass
from pathlib import Path


def v2(n: int) -> int:
    if n <= 0:
        raise ValueError("v2 expects positive integer")
    return (n & -n).bit_length() - 1


def canonical_x(a: int, R: int, t: int) -> int:
    modulus = 1 << (3 * R + 2)
    residue = (pow(3, -a, modulus) * ((1 << (3 * R)) - 1)) % modulus
    # X is odd already; impose X = 5 mod 6, equivalently X = 2 mod 3.
    lift = ((2 - residue) * pow(modulus, -1, 3)) % 3
    x = residue + modulus * lift
    if x <= 0:
        x += 3 * modulus
    return x + 3 * modulus * t


def renewal_step(a: int, X: int):
    if a < 1 or X <= 0 or X % 6 != 5:
        return None
    first = pow(3, a) * X + 1
    e2 = v2(first)
    if e2 < 3 or e2 % 3:
        return None
    R = e2 // 3
    U = first >> e2
    if U % 4 != 1:
        return None
    p = (1 << (3 * R + 2)) * U
    if p % 3 != 1:
        return None

    second = pow(9, R) * U - 1
    e2b = v2(second)
    if e2b < 2 or e2b % 2:
        return None
    b = e2b // 2
    Y = second >> e2b
    if Y % 6 != 5:
        return None
    return b, Y, R, U


def compiler_checks() -> list[dict]:
    packets = [
        # word, U, V, B, A, Y
        ("10", 128, 81, 56, 72, 46),
        ("30", 8192, 6561, 3584, 4608, 3691),
    ]
    out = []
    for word, U, V, B, A, Y in packets:
        if V * A + B != U * Y:
            raise AssertionError(("bad compiler affine data", word))
        fixed_num = B
        fixed_den = U - V
        displacement_at_A = A - Y
        if displacement_at_A <= 0:
            raise AssertionError(("compiler does not descend", word))
        out.append(
            {
                "word": word,
                "U": U,
                "V": V,
                "B": B,
                "A": A,
                "Y": Y,
                "fixed_point_num": fixed_num,
                "fixed_point_den": fixed_den,
                "displacement_at_A": displacement_at_A,
            }
        )
    return out


@dataclass(frozen=True)
class Summary:
    a_max: int
    R_max: int
    t_max: int
    stars_tested: int
    valid_first_renewals: int
    cycles_found: int
    maximum_renewal_steps: int
    maximizing_initial: dict
    maximizing_trajectory: list
    compiler_packets: list
    digest_sha256: str


def audit(a_max: int, R_max: int, t_max: int, max_steps: int) -> Summary:
    compiler = compiler_checks()
    stars = 0
    valid = 0
    cycles = 0
    best_len = -1
    best_initial = {}
    best_trajectory = []
    digest = hashlib.sha256()

    for a in range(1, a_max + 1):
        for R0 in range(1, R_max + 1):
            for t in range(t_max + 1):
                stars += 1
                X = canonical_x(a, R0, t)
                first = renewal_step(a, X)
                if first is None or first[2] != R0:
                    continue
                valid += 1

                current = (a, X)
                seen = {}
                trajectory = []
                for step_index in range(max_steps):
                    if current in seen:
                        cycles += 1
                        break
                    seen[current] = step_index
                    nxt = renewal_step(*current)
                    if nxt is None:
                        break
                    b, Y, R, U = nxt
                    trajectory.append(
                        {
                            "a": current[0],
                            "X": current[1],
                            "R": R,
                            "U": U,
                            "b": b,
                            "Y": Y,
                        }
                    )
                    current = (b, Y)

                if len(trajectory) > best_len:
                    best_len = len(trajectory)
                    best_initial = {"a": a, "R": R0, "t": t, "X": X}
                    best_trajectory = trajectory

                digest.update(
                    json.dumps(
                        {
                            "a": a,
                            "R": R0,
                            "t": t,
                            "X": X,
                            "length": len(trajectory),
                            "terminal": current,
                        },
                        sort_keys=True,
                        separators=(",", ":"),
                    ).encode()
                )

    payload = {
        "compiler": compiler,
        "best_initial": best_initial,
        "best_trajectory": best_trajectory,
        "stars": stars,
        "valid": valid,
        "cycles": cycles,
        "best_len": best_len,
    }
    digest.update(json.dumps(payload, sort_keys=True, separators=(",", ":")).encode())
    return Summary(
        a_max=a_max,
        R_max=R_max,
        t_max=t_max,
        stars_tested=stars,
        valid_first_renewals=valid,
        cycles_found=cycles,
        maximum_renewal_steps=best_len,
        maximizing_initial=best_initial,
        maximizing_trajectory=best_trajectory,
        compiler_packets=compiler,
        digest_sha256=digest.hexdigest(),
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--a-max", type=int, default=30)
    parser.add_argument("--R-max", type=int, default=20)
    parser.add_argument("--t-max", type=int, default=2000)
    parser.add_argument("--max-steps", type=int, default=100)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    summary = audit(args.a_max, args.R_max, args.t_max, args.max_steps)
    rendered = json.dumps(asdict(summary), indent=2, sort_keys=True)
    print(rendered)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
