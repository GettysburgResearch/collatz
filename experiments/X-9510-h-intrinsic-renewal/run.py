#!/usr/bin/env python3
"""Exact finite audit for the intrinsic H renewal-height decoder.

Finite computation only. It checks the one-integer renewal map against the
renewal type/counter parametrization, checks the exact predecessor formula, and
searches a bounded ordinary box for long renewal chains and cycles.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import asdict, dataclass
from functools import lru_cache
from pathlib import Path


def vp(n: int, p: int) -> int:
    if n <= 0:
        raise ValueError("valuation requires a positive integer")
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def v2(n: int) -> int:
    if n <= 0:
        raise ValueError("v2 requires a positive integer")
    return (n & -n).bit_length() - 1


@lru_cache(None)
def type_data(a: int, R: int, b: int) -> dict[str, int]:
    d = 3 * R + 2 * b
    two_modulus = 1 << (d + 1)
    coefficient = 9**R * 3**a
    rhs = (1 << d) + 8**R - 9**R
    residue_two = rhs * pow(coefficient, -1, two_modulus) % two_modulus
    x0 = next(
        residue_two + t * two_modulus
        for t in range(3)
        if (residue_two + t * two_modulus) % 3 == 2
    )
    modulus = 3 * two_modulus
    u0 = (3**a * x0 + 1) // 8**R
    y0 = (9**R * u0 - 1) // 4**b
    assert x0 % 6 == 5
    assert u0 % 4 == 1
    assert y0 % 6 == 5
    return {
        "a": a,
        "R": R,
        "b": b,
        "modulus": modulus,
        "x0": x0,
        "u0": u0,
        "y0": y0,
    }


def renewal_step(Z: int) -> tuple[int, tuple[int, int, int, int, int, int]] | None:
    if Z <= 0:
        return None
    a = vp(Z, 3)
    if a < 1:
        return None
    X = Z // 3**a
    if X % 6 != 5:
        return None
    e = v2(Z + 1)
    if e <= 0 or e % 3:
        return None
    R = e // 3
    if R < 1:
        return None
    U = (Z + 1) >> e
    if U % 4 != 1:
        return None
    T = 9**R * U - 1
    f = v2(T)
    if f <= 0 or f % 2:
        return None
    b = f // 2
    if b < 1:
        return None
    Y = T >> f
    if Y % 6 != 5:
        return None
    return 3**b * Y, (a, R, b, X, U, Y)


def renewal_predecessor(Z: int) -> tuple[int, tuple[int, int, int, int, int, int]] | None:
    if Z <= 0:
        return None
    a = vp(Z, 3)
    if a < 1:
        return None
    X = Z // 3**a
    if X % 6 != 5:
        return None
    T = 4**a * X + 1
    m = vp(T, 3)
    if m < 2 or m % 2:
        return None
    R = m // 2
    U = T // 9**R
    Z_minus = 8**R * U - 1
    a_minus = vp(Z_minus, 3)
    if a_minus < 1:
        return None
    X_minus = Z_minus // 3**a_minus
    if X_minus % 6 != 5:
        return None
    check = renewal_step(Z_minus)
    if check is None or check[0] != Z:
        return None
    return Z_minus, (a_minus, R, a, X_minus, U, X)


def direct_type_transition(
    source: tuple[int, int, int], k: int
) -> tuple[tuple[int, int, int], int] | None:
    data = type_data(*source)
    X = data["x0"] + data["modulus"] * k
    first = 3**source[0] * X + 1
    e = v2(first)
    if e <= 0 or e % 3:
        return None
    R = e // 3
    U = first >> e
    if R <= 0 or U % 4 != 1:
        return None
    second = 9**R * U - 1
    f = v2(second)
    if f <= 0 or f % 2:
        return None
    b = f // 2
    Y = second >> f
    if b <= 0 or Y % 6 != 5:
        return None
    next_first = 3**b * Y + 1
    e2 = v2(next_first)
    if e2 <= 0 or e2 % 3:
        return None
    S = e2 // 3
    U2 = next_first >> e2
    if S <= 0 or U2 % 4 != 1:
        return None
    next_second = 9**S * U2 - 1
    f2 = v2(next_second)
    if f2 <= 0 or f2 % 2:
        return None
    c = f2 // 2
    if c <= 0:
        return None
    target = (b, S, c)
    target_data = type_data(*target)
    difference = Y - target_data["x0"]
    if difference < 0 or difference % target_data["modulus"]:
        return None
    return target, difference // target_data["modulus"]


def Z_from_type_counter(tau: tuple[int, int, int], k: int) -> int:
    data = type_data(*tau)
    return 3**tau[0] * (data["x0"] + data["modulus"] * k)


def life(Z: int, maximum_steps: int) -> tuple[int, str, list[dict[str, object]]]:
    seen: set[int] = set()
    path: list[dict[str, object]] = []
    current = Z
    for _ in range(maximum_steps):
        if current in seen:
            return len(path), "cycle", path
        seen.add(current)
        result = renewal_step(current)
        if result is None:
            return len(path), "exit", path
        nxt, data = result
        path.append(
            {
                "Z": current,
                "Z_next": nxt,
                "type": list(data[:3]),
                "X": data[3],
                "U": data[4],
                "Y": data[5],
            }
        )
        current = nxt
    return len(path), "limit", path


@dataclass(frozen=True)
class Summary:
    max_type: int
    k_max: int
    states: int
    step_checks: int
    inverse_checks: int
    defined_next_renewals: int
    source_states: int
    states_with_expanding_predecessor: int
    maximum_renewal_life: int
    maximizing_type: tuple[int, int, int]
    maximizing_k: int
    maximizing_Z: int
    maximizing_status: str
    maximizing_path: list[dict[str, object]]
    digest_sha256: str


def audit(max_type: int, k_max: int, maximum_steps: int) -> Summary:
    total = step_checks = inverse_checks = defined_next = 0
    source_states = expanding_predecessors = 0
    best_life = -1
    best: tuple[tuple[int, int, int], int, int, str, list[dict[str, object]]] | None = None
    digest = hashlib.sha256()

    def predecessor_expands(R: int, a: int) -> bool:
        return 9**R * 3**a > 8**R * 4**a

    for a in range(1, max_type + 1):
        for R in range(1, max_type + 1):
            for b in range(1, max_type + 1):
                tau = (a, R, b)
                data = type_data(*tau)
                for k in range(k_max + 1):
                    total += 1
                    Z = 3**a * (data["x0"] + data["modulus"] * k)
                    result = renewal_step(Z)
                    if result is None or result[1][:3] != tau:
                        raise AssertionError(("intrinsic decode", tau, k, Z, result))
                    Z_next, _ = result
                    step_checks += 1

                    pred = renewal_predecessor(Z_next)
                    if pred is None or pred[0] != Z:
                        raise AssertionError(("inverse round trip", tau, k, Z, Z_next, pred))
                    inverse_checks += 1

                    direct = direct_type_transition(tau, k)
                    next_intrinsic = renewal_step(Z_next)
                    if direct is None:
                        if next_intrinsic is not None:
                            raise AssertionError(("type decoder missed next renewal", tau, k))
                    else:
                        target, k_next = direct
                        if next_intrinsic is None or Z_from_type_counter(target, k_next) != Z_next:
                            raise AssertionError(("type/intrinsic mismatch", tau, k, direct))
                        defined_next += 1

                    incoming = renewal_predecessor(Z)
                    if incoming is None:
                        source_states += 1
                        incoming_Z = None
                    else:
                        incoming_Z, incoming_data = incoming
                        if predecessor_expands(incoming_data[1], a):
                            expanding_predecessors += 1

                    trajectory_length, status, path = life(Z, maximum_steps)
                    if status == "cycle":
                        raise AssertionError(("positive renewal cycle", tau, k, path))
                    if trajectory_length > best_life:
                        best_life = trajectory_length
                        best = (tau, k, Z, status, path)

                    digest.update(
                        json.dumps(
                            {
                                "tau": tau,
                                "k": k,
                                "Z": Z,
                                "Z_next": Z_next,
                                "predecessor": incoming_Z,
                                "next": direct,
                            },
                            sort_keys=True,
                            separators=(",", ":"),
                        ).encode("utf-8")
                    )

    assert best is not None
    tau, k, Z, status, path = best
    return Summary(
        max_type=max_type,
        k_max=k_max,
        states=total,
        step_checks=step_checks,
        inverse_checks=inverse_checks,
        defined_next_renewals=defined_next,
        source_states=source_states,
        states_with_expanding_predecessor=expanding_predecessors,
        maximum_renewal_life=best_life,
        maximizing_type=tau,
        maximizing_k=k,
        maximizing_Z=Z,
        maximizing_status=status,
        maximizing_path=path,
        digest_sha256=digest.hexdigest(),
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-type", type=int, default=18)
    parser.add_argument("--k-max", type=int, default=127)
    parser.add_argument("--max-steps", type=int, default=100)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.max_type < 1 or args.k_max < 0 or args.max_steps < 1:
        raise SystemExit("invalid bounds")
    summary = audit(args.max_type, args.k_max, args.max_steps)
    rendered = json.dumps(asdict(summary), indent=2, sort_keys=True)
    print(rendered)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
