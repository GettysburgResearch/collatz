#!/usr/bin/env python3
"""Derive exact residue cylinders for the D-9701 dyadic-boundary class.

This is the proof-oriented implementation.  The independent verifier in
verify.py does not import this module and uses a different lifting algorithm.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Sequence

PR3_INTERFACE_HEAD = "bdbf5620743f48914331f015d5cba1ba9268b616"
SCHEMA = "X-9701/v1"
TYPES: tuple[int, ...] = (5, 6, 7, 8)


@dataclass(frozen=True)
class TowerType:
    kind: int
    k0: int
    r: int
    g0: int
    b: int


TOWER_TYPES: dict[int, TowerType] = {
    5: TowerType(5, 5, 5, 5, 2),
    6: TowerType(6, 6, 4, 4, 3),
    7: TowerType(7, 7, 3, 5, 2),
    8: TowerType(8, 8, 2, 6, 1),
}


@dataclass(frozen=True)
class TowerData:
    kind: int
    t: int
    mu: int
    A: int
    K: int
    B: int
    G: int


@dataclass(frozen=True)
class ConnectorData:
    source: int
    target: int
    t: int
    N: int
    q: int
    C: int
    source_tower: TowerData
    target_tower: TowerData


def least_residue(value: int, modulus: int) -> int:
    return value % modulus


def inverse_mod_odd(value: int, modulus: int) -> int:
    if value % 2 == 0 or modulus <= 0 or modulus & (modulus - 1):
        raise ValueError("expected an odd value and a positive power-of-two modulus")
    return pow(value, -1, modulus)


def tower_data(kind: int, t: int) -> TowerData:
    spec = TOWER_TYPES[kind]
    if t < 0:
        raise ValueError("tower height must be nonnegative")
    if spec.k0 + spec.r + 1 != 11 or spec.g0 + spec.b != 7:
        raise AssertionError("universal exponent identities failed")

    k = spec.k0 + 11 * t
    g = spec.g0 + 7 * t
    modulus = 1 << (spec.r + 1)
    three_g_mod = pow(3, g, modulus)
    mu = least_residue(-inverse_mod_odd(three_g_mod, modulus), modulus)
    if mu % 2 != 1 or not (0 < mu < modulus):
        raise AssertionError("mu is not the required odd canonical residue")
    if (pow(3, g, modulus) * mu + 1) % modulus != 0:
        raise AssertionError("tower recovery congruence failed")

    K = k + spec.r + 1
    G = g + spec.b
    A = (1 << k) * mu
    quotient = (pow(3, g) * mu + 1) // modulus
    B = pow(3, spec.b) * quotient

    if K != 11 * (t + 1) or G != 7 * (t + 1):
        raise AssertionError("universal K/G schedule failed")
    if not (0 < A < (1 << K)):
        raise AssertionError("A is outside its canonical binary block")
    if not (0 < B < pow(3, G)):
        raise AssertionError("B is outside its canonical ternary block")
    return TowerData(kind=kind, t=t, mu=mu, A=A, K=K, B=B, G=G)


def connector_data(source: int, target: int, t: int) -> ConnectorData:
    if t < 1:
        raise ValueError("D-9701 starts at a dyadic height t >= 1")
    left = tower_data(source, t)
    right = tower_data(target, 2 * t)
    N = pow(3, left.G)
    q = 1 << right.K
    C = left.B - right.A
    return ConnectorData(
        source=source,
        target=target,
        t=t,
        N=N,
        q=q,
        C=C,
        source_tower=left,
        target_tower=right,
    )


def exact_div(numerator: int, denominator: int, label: str) -> int:
    quotient, remainder = divmod(numerator, denominator)
    if remainder != 0:
        raise AssertionError(f"nonintegral {label}: remainder {remainder}")
    return quotient


def build_cylinder(types: Sequence[int], m0: int = 0) -> dict[str, Any]:
    if len(types) < 1:
        raise ValueError("a directive needs at least one type")
    if any(kind not in TOWER_TYPES for kind in types):
        raise ValueError("unknown tower type")
    if m0 < 0:
        raise ValueError("m0 must be nonnegative")

    P = 1
    F = 0
    Q = 1
    R = 0
    H = 0
    blocks: list[int] = []
    maps: list[ConnectorData] = []
    prefix_records: list[dict[str, str | int]] = []

    for index, (source, target) in enumerate(zip(types, types[1:])):
        t = 1 << (m0 + index)
        edge = connector_data(source, target, t)
        maps.append(edge)

        rho = least_residue(-edge.C * inverse_mod_odd(edge.N, edge.q), edge.q)
        a = least_residue((rho - H) * inverse_mod_odd(P, edge.q), edge.q)
        if not (0 <= a < edge.q):
            raise AssertionError("new residue block is outside its radix")

        old_P, old_F, old_Q, old_R, old_H = P, F, Q, R, H
        R = old_R + old_Q * a
        Q = old_Q * edge.q
        P = edge.N * old_P
        F = edge.N * old_F + old_Q * edge.C
        H = exact_div(edge.N * (old_H + old_P * a) + edge.C, edge.q, "block endpoint")

        direct_R = least_residue(-F * inverse_mod_odd(P, Q), Q)
        direct_H = exact_div(P * R + F, Q, "composite endpoint")
        if R != direct_R or H != direct_H:
            raise AssertionError("block recurrence disagrees with composite cylinder")
        if R % old_Q != old_R:
            raise AssertionError("cylinders are not nested")

        blocks.append(a)
        prefix_records.append(
            {
                "index": index,
                "t": t,
                "source": source,
                "target": target,
                "block": str(a),
                "R": str(R),
                "Q": str(Q),
                "H": str(H),
            }
        )

    return {
        "types": list(types),
        "m0": m0,
        "maps": maps,
        "P": P,
        "F": F,
        "Q": Q,
        "R": R,
        "H": H,
        "blocks": blocks,
        "prefix_records": prefix_records,
    }


def replay_affine(h0: int, maps: Sequence[ConnectorData]) -> list[int]:
    path = [h0]
    value = h0
    for index, edge in enumerate(maps):
        value = exact_div(edge.N * value + edge.C, edge.q, f"affine connector {index}")
        path.append(value)
    return path


def choose_nonnegative_member(cylinder: dict[str, Any]) -> tuple[int, int, list[int]]:
    """Choose R + Q*y so that all finite high-tail states are nonnegative."""

    R = int(cylinder["R"])
    Q = int(cylinder["Q"])
    maps: Sequence[ConnectorData] = cylinder["maps"]

    base = R
    stride = Q
    bases = [base]
    strides = [stride]
    for index, edge in enumerate(maps):
        base = exact_div(edge.N * base + edge.C, edge.q, f"member base {index}")
        stride = exact_div(edge.N * stride, edge.q, f"member stride {index}")
        if stride <= 0:
            raise AssertionError("member stride must stay positive")
        bases.append(base)
        strides.append(stride)

    lift = 0
    for base_value, stride_value in zip(bases, strides):
        if base_value < 0:
            lift = max(lift, (-base_value + stride_value - 1) // stride_value)
    # Use the next member so all tails are strictly positive, not merely nonnegative.
    lift += 1
    h0 = R + Q * lift
    path = replay_affine(h0, maps)
    if any(value <= 0 for value in path):
        raise AssertionError("selected finite member is not strictly positive")
    return lift, h0, path


def shortcut_step(value: int) -> int:
    if value <= 0:
        raise ValueError("physical replay is restricted to positive integers")
    if value & 1:
        return (3 * value + 1) // 2
    return value // 2


def replay_physical(types: Sequence[int], m0: int, h_path: Sequence[int]) -> tuple[list[int], list[int]]:
    if len(h_path) != len(types):
        raise ValueError("one high-tail value is required at every tower boundary")

    physical: list[int] = []
    odd_counts: list[int] = []
    for index, (kind, h_value) in enumerate(zip(types, h_path)):
        t = 1 << (m0 + index)
        tower = tower_data(kind, t)
        x = tower.A + (1 << tower.K) * h_value - 34
        if x <= 0:
            raise AssertionError("selected physical state is not positive")
        physical.append(x)

    for index, (source, target) in enumerate(zip(types, types[1:])):
        del target
        t = 1 << (m0 + index)
        tower = tower_data(source, t)
        value = physical[index]
        odd = 0
        for _ in range(tower.K):
            odd += value & 1
            value = shortcut_step(value)
        if value != physical[index + 1]:
            raise AssertionError("direct shortcut replay missed the next tower boundary")
        if odd != tower.G:
            raise AssertionError("physical replay has the wrong odd-step count")
        odd_counts.append(odd)

    return physical, odd_counts


def assert_proof_interfaces() -> dict[str, Any]:
    if pow(3, 7) >= (1 << 12):
        raise AssertionError("3^7 < 2^12 gate failed")

    checked_heights = (1, 2, 4, 8, 16, 32)
    trap_checks = 0
    pair_checks = 0
    for t in checked_heights:
        for source in TYPES:
            for target in TYPES:
                edge = connector_data(source, target, t)
                N, q = edge.N, edge.q
                A, B = edge.target_tower.A, edge.source_tower.B
                if not (512 * N < q):
                    raise AssertionError("N/q < 1/512 failed")
                if not (0 < B < N):
                    raise AssertionError("source block bound failed")
                if not (q <= 64 * A <= 63 * q):
                    raise AssertionError("target-anchor interval failed")
                for h in (-1, 0, 1):
                    numerator = N * h + B - A
                    if not (-q < numerator < 0):
                        raise AssertionError("finite trap exclusion failed")
                    if numerator % q == 0:
                        raise AssertionError("a trap numerator unexpectedly divided by q")
                    trap_checks += 1
                pair_checks += 1

    return {
        "three7": pow(3, 7),
        "two12": 1 << 12,
        "contraction_numerator": 1,
        "contraction_denominator": 512,
        "affine_error_numerator": 513,
        "affine_error_denominator": 512,
        "fixed_point_numerator": 513,
        "fixed_point_denominator": 511,
        "trap_radius": 2,
        "checked_heights": list(checked_heights),
        "pair_checks": pair_checks,
        "trap_checks": trap_checks,
    }


def record_line(types: Sequence[int], cylinder: dict[str, Any]) -> bytes:
    record = {
        "types": list(types),
        "m0": int(cylinder["m0"]),
        "R": str(cylinder["R"]),
        "Q": str(cylinder["Q"]),
        "blocks": [str(value) for value in cylinder["blocks"]],
    }
    return (json.dumps(record, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def exhaustive_audit(type_length: int = 5, m0: int = 0) -> dict[str, Any]:
    if type_length < 2:
        raise ValueError("exhaustive directives need at least one transition")
    digest = hashlib.sha256()
    directive_count = 0
    transition_count = 0
    zero_block_count = 0
    nonzero_block_count = 0
    maximum_modulus_bits = 0

    for types in itertools.product(TYPES, repeat=type_length):
        cylinder = build_cylinder(types, m0=m0)
        digest.update(record_line(types, cylinder))
        directive_count += 1
        transition_count += len(types) - 1
        zero_block_count += sum(value == 0 for value in cylinder["blocks"])
        nonzero_block_count += sum(value != 0 for value in cylinder["blocks"])
        Q = int(cylinder["Q"])
        if Q & (Q - 1):
            raise AssertionError("cylinder modulus is not a power of two")
        maximum_modulus_bits = max(maximum_modulus_bits, Q.bit_length() - 1)

    return {
        "type_length": type_length,
        "m0": m0,
        "directive_count": directive_count,
        "transition_count": transition_count,
        "zero_block_count": zero_block_count,
        "nonzero_block_count": nonzero_block_count,
        "maximum_modulus_bits": maximum_modulus_bits,
        "records_sha256": digest.hexdigest(),
    }


def certificate(name: str, types: Sequence[int], m0: int = 0) -> dict[str, Any]:
    cylinder = build_cylinder(types, m0=m0)
    lift, h0, h_path = choose_nonnegative_member(cylinder)
    physical_path, odd_counts = replay_physical(types, m0, h_path)

    return {
        "name": name,
        "types": list(types),
        "m0": m0,
        "transitions": len(types) - 1,
        "blocks": [str(value) for value in cylinder["blocks"]],
        "R": str(cylinder["R"]),
        "Q": str(cylinder["Q"]),
        "Q_bits": int(cylinder["Q"]).bit_length() - 1,
        "lift_index": str(lift),
        "h0": str(h0),
        "h_path": [str(value) for value in h_path],
        "physical_path": [str(value) for value in physical_path],
        "odd_counts": odd_counts,
        "nonzero_blocks": sum(value != 0 for value in cylinder["blocks"]),
    }


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("utf-8")


def build_payload() -> dict[str, Any]:
    proof_interfaces = assert_proof_interfaces()
    exhaustive = exhaustive_audit(type_length=5, m0=0)
    selected = [
        certificate("constant-5", [5, 5, 5, 5, 5, 5, 5]),
        certificate("four-cycle", [5, 6, 7, 8, 5, 6, 7]),
        certificate("reverse-cycle", [8, 7, 6, 5, 8, 7, 6]),
        certificate("outer-alternation", [5, 8, 5, 8, 5, 8, 5]),
        certificate("mixed", [6, 8, 7, 5, 6, 8, 7]),
    ]
    total_replayed = sum(item["transitions"] for item in selected)

    payload: dict[str, Any] = {
        "schema": SCHEMA,
        "agent": "gpt56-cylinder-01",
        "issue": 31,
        "claims": ["D-9701", "L-9701", "T-9701", "T-9702", "Q-9701", "X-9701"],
        "pr3_interface_head": PR3_INTERFACE_HEAD,
        "tower_types": {
            str(kind): {
                "k0": spec.k0,
                "r": spec.r,
                "g0": spec.g0,
                "b": spec.b,
            }
            for kind, spec in sorted(TOWER_TYPES.items())
        },
        "proof_interfaces": proof_interfaces,
        "exhaustive": exhaustive,
        "selected_certificates": selected,
        "physical_tower_blocks_replayed": total_replayed,
    }
    payload["payload_sha256"] = hashlib.sha256(canonical_bytes(payload)).hexdigest()
    return payload


def write_summary(path: Path, payload: dict[str, Any]) -> None:
    exhaustive = payload["exhaustive"]
    lines = [
        "X-9701 exact dyadic-boundary cylinder derivation",
        f"PR3 interface head: {payload['pr3_interface_head']}",
        f"tower types: {len(payload['tower_types'])}",
        f"exhaustive type words: {exhaustive['directive_count']}",
        f"exhaustive transitions: {exhaustive['transition_count']}",
        f"finite zero blocks observed: {exhaustive['zero_block_count']}",
        f"finite nonzero blocks observed: {exhaustive['nonzero_block_count']}",
        f"maximum cumulative modulus bits: {exhaustive['maximum_modulus_bits']}",
        f"exhaustive record digest: {exhaustive['records_sha256']}",
        f"selected certificates: {len(payload['selected_certificates'])}",
        f"physical tower blocks replayed: {payload['physical_tower_blocks_replayed']}",
        f"payload digest: {payload['payload_sha256']}",
        "all derivation checks passed",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--summary", type=Path, required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    payload = build_payload()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    write_summary(args.summary, payload)
    print(f"wrote {args.output}")
    print(f"wrote {args.summary}")
    print(f"payload sha256: {payload['payload_sha256']}")
    print("all derivation checks passed")


if __name__ == "__main__":
    main()
