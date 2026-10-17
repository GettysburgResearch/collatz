#!/usr/bin/env python3
"""Independent reconstruction of the X-8251 frozen artifact.

This verifier intentionally imports no project or generator module.  It
rebuilds the constants, branch residues, physical chart blocks, centered
quotient identities, finite counters, samples, and transcript digest.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from pathlib import Path

DELTA = 16**9 - 9**9
ROOT = 37_933_813_917
QA = (9**9 * ROOT + 1) // DELTA
QB = (16**9 * ROOT + 1) // DELTA


def ord_two(value: int) -> int:
    assert value
    value = abs(value)
    count = 0
    while value % 2 == 0:
        value //= 2
        count += 1
    return count


def egcd(a: int, b: int) -> tuple[int, int, int]:
    if b == 0:
        return a, 1, 0
    g, x1, y1 = egcd(b, a % b)
    return g, y1, x1 - (a // b) * y1


def inverse(a: int, modulus: int) -> int:
    g, x, _ = egcd(a % modulus, modulus)
    assert g == 1
    return x % modulus


def merge_crt(a: int, m: int, b: int, n: int) -> int:
    assert egcd(m, n)[0] == 1
    return (a + ((b - a) * inverse(m, n) % n) * m) % (m * n)


def factor_naive(value: int) -> list[int]:
    result: list[int] = []
    divisor = 2
    while divisor * divisor <= value:
        while value % divisor == 0:
            result.append(divisor)
            value //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if value > 1:
        result.append(value)
    return result


def data_for_run(run: int) -> dict[str, int]:
    shift = 3 * run + 36
    radix = 2**shift
    odd = 9 ** (run + 9)
    correction = 9**run * QA - 8**run * QB
    residue = (-correction * inverse(odd, radix)) % radix
    output = (odd * residue + correction) // radix
    assert odd * residue + correction == radix * output
    return {
        "shift": shift,
        "radix": radix,
        "odd": odd,
        "correction": correction,
        "residue": residue,
        "output": output,
    }


def apply_original(boundary: int, run: int) -> int | None:
    top = 9**run * (1 + 9**9 * boundary) - 2 ** (3 * run)
    bottom = 2 ** (3 * run + 36)
    if top % bottom:
        return None
    if ord_two(1 + 9**9 * boundary) != 3 * run:
        return None
    return top // bottom


def apply_centered(x: int, run: int) -> int | None:
    row = data_for_run(run)
    if (x - row["residue"]) % row["radix"]:
        return None
    lift = (x - row["residue"]) // row["radix"]
    return row["output"] + row["odd"] * lift


def joint_residue(old_run: int, new_run: int) -> tuple[int, int]:
    row = data_for_run(new_run)
    r_two_delta = ROOT + DELTA * row["residue"]
    m_two_delta = DELTA * row["radix"]
    three_power = 9**old_run
    if old_run:
        r_three = (-inverse(16**9, three_power)) % three_power
        combined = merge_crt(
            r_two_delta % m_two_delta,
            m_two_delta,
            r_three,
            three_power,
        )
    else:
        combined = r_two_delta % m_two_delta
    return combined, m_two_delta * three_power


def chart_once(z: int) -> tuple[int, int] | None:
    if z > 0 and z % 8 == 0:
        return 9 * z // 8, 0
    if z > 0 and z % 16 == 1:
        return (9 * z + 7) // 16, 1
    return None


def replay_boundary(boundary: int, old_run: int, new_run: int) -> tuple[int, int]:
    pre_b = 1 + 16**9 * boundary
    divisor = 7 * 9**old_run
    assert pre_b % divisor == 0
    core = pre_b // divisor
    assert core > 0 and core % 2 == 1
    z = 7 * 2 ** (3 * old_run) * core

    for _ in range(old_run):
        got = chart_once(z)
        assert got is not None and got[1] == 0
        z = got[0]
    assert z == pre_b

    for _ in range(9):
        got = chart_once(z)
        assert got is not None and got[1] == 1
        z = got[0]
    assert z == 1 + 9**9 * boundary
    assert ord_two(z) == 3 * new_run

    for _ in range(new_run):
        got = chart_once(z)
        assert got is not None and got[1] == 0
        z = got[0]

    next_boundary = apply_original(boundary, new_run)
    assert next_boundary is not None
    assert z == 1 + 16**9 * next_boundary
    return next_boundary, z


def pair_parameters(first: int, second: int) -> tuple[int, int]:
    left = data_for_run(first)
    right = data_for_run(second)
    rho = (
        (right["residue"] - left["output"])
        * inverse(left["odd"], right["radix"])
    ) % right["radix"]
    sigma = (
        left["output"] + left["odd"] * rho - right["residue"]
    ) // right["radix"]
    assert (
        left["output"] + left["odd"] * rho
        == right["residue"] + right["radix"] * sigma
    )
    return rho, sigma


def reconstruct() -> dict[str, object]:
    assert DELTA == 68_332_056_247
    assert ROOT == (-inverse(9**9, DELTA)) % DELTA
    assert (9**9 * ROOT + 1) % DELTA == 0
    assert (16**9 * ROOT + 1) % DELTA == 0
    assert QB - QA == ROOT
    factors = factor_naive(DELTA)
    assert factors == [7, 13, 19, 37, 163, 6553]

    cutoff = {
        "multiplier_43_positive": 9**52 > 2**165,
        "multiplier_44_positive": 9**53 > 2**168,
        "toll_43": str(9**43 * QA - 8**43 * QB),
        "toll_44": str(9**44 * QA - 8**44 * QB),
    }
    assert cutoff["multiplier_43_positive"] is False
    assert cutoff["multiplier_44_positive"] is True
    assert int(cutoff["toll_43"]) < 0 < int(cutoff["toll_44"])

    counts = {
        "centered_branch_instances": 0,
        "raw_centered_agreements": 0,
        "invariant_residue_checks": 0,
        "physical_high_block_replays": 0,
        "quotient_pair_identities": 0,
        "high_growth_checks": 0,
        "bounded_zero_carry_pairs": 0,
    }
    sha = hashlib.sha256()
    samples: list[dict[str, object]] = []

    for run in range(97):
        row = data_for_run(run)
        for lift in range(17):
            x = row["residue"] + row["radix"] * lift
            xp = row["output"] + row["odd"] * lift
            boundary = ROOT + DELTA * x
            direct = apply_original(boundary, run)
            assert direct == ROOT + DELTA * xp
            assert boundary % DELTA == ROOT
            assert direct % DELTA == ROOT
            assert boundary % 7 == 6 and direct % 7 == 6
            if run >= 44:
                assert xp > x
                counts["high_growth_checks"] += 1
            counts["centered_branch_instances"] += 1
            counts["raw_centered_agreements"] += 1
            counts["invariant_residue_checks"] += 1
            sha.update(f"B|{run}|{lift}|{x}|{xp}\n".encode("ascii"))

        if run in {0, 1, 43, 44, 64, 65, 96}:
            samples.append(
                {
                    "run": run,
                    "radix_bits": row["shift"],
                    "xi": str(row["residue"]),
                    "canonical_output": str(row["output"]),
                    "toll": str(row["correction"]),
                    "multiplier_bits": row["odd"].bit_length(),
                }
            )

    pairs = list(itertools.product(range(9), repeat=2))
    pairs += list(itertools.product(range(44, 51), repeat=2))
    for old_run, new_run in pairs:
        residue, modulus = joint_residue(old_run, new_run)
        for lift in range(5):
            boundary = residue + modulus * lift
            next_boundary, final_z = replay_boundary(boundary, old_run, new_run)
            x = (boundary - ROOT) // DELTA
            xp = apply_centered(x, new_run)
            assert xp is not None
            assert next_boundary == ROOT + DELTA * xp
            counts["physical_high_block_replays"] += 1
            sha.update(
                f"P|{old_run}|{new_run}|{lift}|{final_z}\n".encode("ascii")
            )

    pair_ranges = list(itertools.product(range(17), repeat=2))
    pair_ranges += list(itertools.product(range(44, 65), repeat=2))
    done: set[tuple[int, int]] = set()
    for first, second in pair_ranges:
        if (first, second) in done:
            continue
        done.add((first, second))
        rho, sigma = pair_parameters(first, second)
        left = data_for_run(first)
        right = data_for_run(second)
        for ell in range(7):
            k = rho + right["radix"] * ell
            x = left["residue"] + left["radix"] * k
            xp = apply_centered(x, first)
            assert xp is not None
            kp = (xp - right["residue"]) // right["radix"]
            assert xp == right["residue"] + right["radix"] * kp
            assert kp == sigma + left["odd"] * ell
            counts["quotient_pair_identities"] += 1
            sha.update(f"Q|{first}|{second}|{ell}|{k}|{kp}\n".encode("ascii"))

    zero: list[list[int]] = []
    for first in range(44, 81):
        for second in range(44, 81):
            rho, sigma = pair_parameters(first, second)
            if rho == 0 and sigma == 0:
                zero.append([first, second])
    assert not zero
    counts["bounded_zero_carry_pairs"] = len(zero)

    return {
        "experiment_id": "X-8251",
        "status": "exact finite verification of the declared corpus; L-8251/L-8252 remain PROPOSED",
        "constants": {
            "D9": DELTA,
            "D9_factorization": factors,
            "omega": ROOT,
            "a": QA,
            "b": QB,
            "b_minus_a": QB - QA,
        },
        "threshold": cutoff,
        "scope": {
            "centered_runs": [0, 96],
            "lifts_per_centered_run": 17,
            "physical_small_runs": [0, 8],
            "physical_high_runs": [44, 50],
            "physical_lifts_per_pair": 5,
            "quotient_small_runs": [0, 16],
            "quotient_high_runs": [44, 64],
            "quotient_lifts_per_pair": 7,
            "zero_carry_search": [44, 80],
        },
        "counters": counts,
        "zero_carry_pairs": zero,
        "samples": samples,
        "transcript_sha256": sha.hexdigest(),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("artifact", type=Path)
    args = parser.parse_args()
    frozen = json.loads(args.artifact.read_text(encoding="utf-8"))
    rebuilt = reconstruct()
    if rebuilt != frozen:
        raise SystemExit("independent reconstruction does not match frozen JSON")
    print("independent reconstruction matches")
    print(json.dumps(rebuilt["counters"], sort_keys=True))
    print(f"transcript_sha256={rebuilt['transcript_sha256']}")


if __name__ == "__main__":
    main()
