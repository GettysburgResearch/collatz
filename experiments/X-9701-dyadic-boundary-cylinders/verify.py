#!/usr/bin/env python3
"""Independent exact replay verifier for X-9701.

This file intentionally does not import derive.py.  It reconstructs the finite
cores by brute-force modular search, lifts cylinders by direct endpoint replay,
and executes the shortcut map on every selected physical tower block.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from pathlib import Path
from typing import Any, Sequence

SCHEMA = "X-9701/v1"
TYPES: tuple[int, ...] = (5, 6, 7, 8)
SPECS: dict[int, tuple[int, int, int, int]] = {
    5: (5, 5, 5, 2),
    6: (6, 4, 4, 3),
    7: (7, 3, 5, 2),
    8: (8, 2, 6, 1),
}


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("utf-8")


def verify_payload_digest(payload: dict[str, Any]) -> None:
    expected = payload.get("payload_sha256")
    if not isinstance(expected, str):
        raise AssertionError("missing payload digest")
    stripped = dict(payload)
    del stripped["payload_sha256"]
    actual = hashlib.sha256(canonical_bytes(stripped)).hexdigest()
    if actual != expected:
        raise AssertionError(f"payload digest mismatch: {actual} != {expected}")


def brute_mu(kind: int, t: int) -> int:
    k0, r, g0, b = SPECS[kind]
    del k0, b
    modulus = 1 << (r + 1)
    power = pow(3, g0 + 7 * t, modulus)
    hits = [candidate for candidate in range(1, modulus, 2) if (power * candidate + 1) % modulus == 0]
    if len(hits) != 1:
        raise AssertionError(f"expected one odd recovery residue, found {hits}")
    return hits[0]


def tower(kind: int, t: int) -> dict[str, int]:
    k0, r, g0, b = SPECS[kind]
    if k0 + r + 1 != 11 or g0 + b != 7:
        raise AssertionError("type table violates the universal exponent identities")
    mu = brute_mu(kind, t)
    k = k0 + 11 * t
    g = g0 + 7 * t
    modulus = 1 << (r + 1)
    K = k + r + 1
    G = g + b
    numerator = pow(3, g) * mu + 1
    if numerator % modulus:
        raise AssertionError("brute recovery residue does not divide exactly")
    A = (1 << k) * mu
    B = pow(3, b) * (numerator // modulus)
    if K != 11 * (t + 1) or G != 7 * (t + 1):
        raise AssertionError("universal tower exponents failed")
    return {"mu": mu, "A": A, "K": K, "B": B, "G": G}


def edge(source: int, target: int, t: int) -> dict[str, int]:
    left = tower(source, t)
    right = tower(target, 2 * t)
    return {
        "source": source,
        "target": target,
        "t": t,
        "N": pow(3, left["G"]),
        "q": 1 << right["K"],
        "C": left["B"] - right["A"],
        "source_A": left["A"],
        "source_K": left["K"],
        "source_B": left["B"],
        "source_G": left["G"],
        "target_A": right["A"],
        "target_K": right["K"],
    }


def divide_exact(numerator: int, denominator: int, context: str) -> int:
    quotient, remainder = divmod(numerator, denominator)
    if remainder:
        raise AssertionError(f"{context} is not integral; remainder={remainder}")
    return quotient


def replay(value: int, maps: Sequence[dict[str, int]]) -> list[int]:
    path = [value]
    for index, item in enumerate(maps):
        value = divide_exact(item["N"] * value + item["C"], item["q"], f"affine step {index}")
        path.append(value)
    return path


def independently_lift(types: Sequence[int], m0: int) -> dict[str, Any]:
    """Lift one cylinder by comparing the endpoints of R and R+Q.

    No composite P/F recurrence is used.  At each extension we directly replay
    the existing representative and one full modulus translate through the
    already accepted prefix; their endpoint difference is the live stride.
    """

    maps: list[dict[str, int]] = []
    R = 0
    Q = 1
    blocks: list[int] = []

    for index, (source, target) in enumerate(zip(types, types[1:])):
        item = edge(source, target, 1 << (m0 + index))
        endpoint0 = replay(R, maps)[-1]
        endpoint1 = replay(R + Q, maps)[-1]
        stride = endpoint1 - endpoint0
        if stride <= 0 or stride % 2 == 0:
            raise AssertionError("accepted-cylinder endpoint stride is not positive odd")

        constant = item["N"] * endpoint0 + item["C"]
        coefficient = item["N"] * stride
        block = (-constant * pow(coefficient, -1, item["q"])) % item["q"]
        old_R, old_Q = R, Q
        R += Q * block
        Q *= item["q"]
        maps.append(item)

        if R % old_Q != old_R:
            raise AssertionError("independent lift broke cylinder nesting")
        accepted_path = replay(R, maps)
        if len(accepted_path) != len(maps) + 1:
            raise AssertionError("independent replay has wrong length")
        blocks.append(block)

    return {"R": R, "Q": Q, "blocks": blocks, "maps": maps}


def record_line(types: Sequence[int], m0: int, lifted: dict[str, Any]) -> bytes:
    record = {
        "types": list(types),
        "m0": m0,
        "R": str(lifted["R"]),
        "Q": str(lifted["Q"]),
        "blocks": [str(value) for value in lifted["blocks"]],
    }
    return (json.dumps(record, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def recompute_exhaustive(reference: dict[str, Any]) -> None:
    type_length = int(reference["type_length"])
    m0 = int(reference["m0"])
    digest = hashlib.sha256()
    directive_count = 0
    transition_count = 0
    zero_block_count = 0
    nonzero_block_count = 0
    maximum_modulus_bits = 0

    for types in itertools.product(TYPES, repeat=type_length):
        lifted = independently_lift(types, m0)
        digest.update(record_line(types, m0, lifted))
        directive_count += 1
        transition_count += len(types) - 1
        zero_block_count += sum(value == 0 for value in lifted["blocks"])
        nonzero_block_count += sum(value != 0 for value in lifted["blocks"])
        Q = int(lifted["Q"])
        if Q & (Q - 1):
            raise AssertionError("independently lifted modulus is not a power of two")
        maximum_modulus_bits = max(maximum_modulus_bits, Q.bit_length() - 1)

    actual = {
        "type_length": type_length,
        "m0": m0,
        "directive_count": directive_count,
        "transition_count": transition_count,
        "zero_block_count": zero_block_count,
        "nonzero_block_count": nonzero_block_count,
        "maximum_modulus_bits": maximum_modulus_bits,
        "records_sha256": digest.hexdigest(),
    }
    if actual != reference:
        raise AssertionError(f"exhaustive summary mismatch:\nactual={actual}\nreference={reference}")


def shortcut(value: int) -> int:
    if value <= 0:
        raise AssertionError("generated physical certificate is not positive")
    return (3 * value + 1) // 2 if value & 1 else value // 2


def verify_certificate(item: dict[str, Any]) -> int:
    types = [int(value) for value in item["types"]]
    m0 = int(item["m0"])
    lifted = independently_lift(types, m0)
    if str(lifted["R"]) != item["R"]:
        raise AssertionError(f"{item['name']}: R mismatch")
    if str(lifted["Q"]) != item["Q"]:
        raise AssertionError(f"{item['name']}: Q mismatch")
    if [str(value) for value in lifted["blocks"]] != item["blocks"]:
        raise AssertionError(f"{item['name']}: block mismatch")
    if int(item["Q_bits"]) != int(lifted["Q"]).bit_length() - 1:
        raise AssertionError(f"{item['name']}: modulus bit length mismatch")

    h0 = int(item["h0"])
    lift_index = int(item["lift_index"])
    if h0 != int(lifted["R"]) + int(lifted["Q"]) * lift_index:
        raise AssertionError(f"{item['name']}: member is outside its recorded cylinder")
    h_path = replay(h0, lifted["maps"])
    if [str(value) for value in h_path] != item["h_path"]:
        raise AssertionError(f"{item['name']}: affine path mismatch")
    if any(value <= 0 for value in h_path):
        raise AssertionError(f"{item['name']}: high-tail path is not strictly positive")

    physical: list[int] = []
    for index, (kind, h_value) in enumerate(zip(types, h_path)):
        t = 1 << (m0 + index)
        data = tower(kind, t)
        value = data["A"] + (1 << data["K"]) * h_value - 34
        if value <= 0:
            raise AssertionError(f"{item['name']}: physical boundary is not positive")
        physical.append(value)
    if [str(value) for value in physical] != item["physical_path"]:
        raise AssertionError(f"{item['name']}: physical boundary path mismatch")

    observed_odd_counts: list[int] = []
    for index, kind in enumerate(types[:-1]):
        t = 1 << (m0 + index)
        data = tower(kind, t)
        value = physical[index]
        odd_count = 0
        for _ in range(data["K"]):
            odd_count += value & 1
            value = shortcut(value)
        if value != physical[index + 1]:
            raise AssertionError(f"{item['name']}: shortcut replay misses boundary {index + 1}")
        if odd_count != data["G"]:
            raise AssertionError(f"{item['name']}: wrong odd count at boundary {index}")
        observed_odd_counts.append(odd_count)
    if observed_odd_counts != [int(value) for value in item["odd_counts"]]:
        raise AssertionError(f"{item['name']}: recorded odd counts mismatch")
    if int(item["nonzero_blocks"]) != sum(value != 0 for value in lifted["blocks"]):
        raise AssertionError(f"{item['name']}: nonzero-block count mismatch")
    return len(observed_odd_counts)


def verify_proof_interfaces(reference: dict[str, Any]) -> None:
    if pow(3, 7) != int(reference["three7"]):
        raise AssertionError("3^7 fingerprint mismatch")
    if 1 << 12 != int(reference["two12"]):
        raise AssertionError("2^12 fingerprint mismatch")
    if not (pow(3, 7) < (1 << 12)):
        raise AssertionError("elementary exponential gate failed")
    if (int(reference["fixed_point_numerator"]), int(reference["fixed_point_denominator"])) != (513, 511):
        raise AssertionError("fixed-point bound was altered")
    if int(reference["trap_radius"]) != 2:
        raise AssertionError("trap radius was altered")

    pair_checks = 0
    trap_checks = 0
    for t in [int(value) for value in reference["checked_heights"]]:
        for source in TYPES:
            for target in TYPES:
                item = edge(source, target, t)
                N, q = item["N"], item["q"]
                A, B = item["target_A"], item["source_B"]
                if not (512 * N < q):
                    raise AssertionError("independent contraction audit failed")
                if not (0 < B < N):
                    raise AssertionError("independent B bound failed")
                if not (q <= 64 * A <= 63 * q):
                    raise AssertionError("independent A interval failed")
                for h in (-1, 0, 1):
                    numerator = N * h + B - A
                    if not (-q < numerator < 0):
                        raise AssertionError("independent trap interval failed")
                    if numerator % q == 0:
                        raise AssertionError("independent trap divisibility failed")
                    trap_checks += 1
                pair_checks += 1
    if pair_checks != int(reference["pair_checks"]) or trap_checks != int(reference["trap_checks"]):
        raise AssertionError("proof-interface count mismatch")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check-results", type=Path, required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    payload = json.loads(args.check_results.read_text(encoding="utf-8"))
    if payload.get("schema") != SCHEMA:
        raise AssertionError("unexpected result schema")
    verify_payload_digest(payload)
    verify_proof_interfaces(payload["proof_interfaces"])
    recompute_exhaustive(payload["exhaustive"])
    replayed = sum(verify_certificate(item) for item in payload["selected_certificates"])
    if replayed != int(payload["physical_tower_blocks_replayed"]):
        raise AssertionError("physical replay count mismatch")
    print(f"verified payload sha256: {payload['payload_sha256']}")
    print(f"verified exhaustive records: {payload['exhaustive']['directive_count']}")
    print(f"verified physical tower blocks: {replayed}")
    print("all independent replay checks passed")


if __name__ == "__main__":
    main()
