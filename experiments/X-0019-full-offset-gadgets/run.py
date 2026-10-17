#!/usr/bin/env python3
"""X-0019: exact full-offset collision gadgets and correlated selectors.

The program uses standard-library integers only. It exhaustively enumerates all
weight-b parity words of length 6b for b <= 6, locates every signature whose
normalized offsets fill Z/3^b Z, freezes one representative per offset, and
replays the correlated selector of T-0041.
"""
from __future__ import annotations

import hashlib
import json
from itertools import combinations
from math import comb


def affine_constant(positions: tuple[int, ...]) -> int:
    weight = len(positions)
    return sum((1 << position) * 3 ** (weight - 1 - index) for index, position in enumerate(positions))


def prefix_positions(mask: int, b: int) -> tuple[int, ...]:
    positions = [index for index in range(b) if mask & (1 << index)]
    positions.extend(range(b, b + (b - len(positions))))
    return tuple(positions)


def shortest_odd_tail(b: int, core_length: int) -> int:
    tail = 0
    while 3 ** (2 * b + tail) <= 2 ** (core_length + tail):
        tail += 1
    return tail


def gadget_record(b: int) -> dict[str, object]:
    length = 6 * b
    low_modulus = 3**b
    full_modulus = low_modulus**2
    powers_two = [pow(2, position, full_modulus) for position in range(length)]
    powers_three = [pow(3, b - 1 - index, full_modulus) for index in range(b)]

    fibers = [0] * low_modulus
    representatives: list[dict[int, tuple[int, ...]]] = [dict() for _ in range(low_modulus)]
    represented: set[int] = set()

    for positions in combinations(range(length), b):
        value = sum(
            powers_two[position] * powers_three[index]
            for index, position in enumerate(positions)
        ) % full_modulus
        signature = value % low_modulus
        offset = (value - signature) // low_modulus
        fibers[signature] |= 1 << offset
        representatives[signature].setdefault(offset, positions)
        represented.add(value)

    full_mask = (1 << low_modulus) - 1
    complete_signatures = [
        signature for signature, bits in enumerate(fibers) if bits == full_mask
    ]
    if not complete_signatures:
        raise AssertionError(f"no full-offset signature at b={b}")

    signature = complete_signatures[0]
    chosen = representatives[signature]
    if len(chosen) != low_modulus:
        raise AssertionError("incomplete representative table")

    actual_values = {
        offset: affine_constant(chosen[offset]) for offset in range(low_modulus)
    }
    reference = actual_values[0]
    for offset, value in actual_values.items():
        if value % low_modulus != signature:
            raise AssertionError("signature mismatch")
        if ((value - reference) // low_modulus) % low_modulus != offset:
            raise AssertionError("normalized offset mismatch")

    gadget_digest = hashlib.sha256()
    for offset in range(low_modulus):
        gadget_digest.update(bytes(chosen[offset]))

    prefixes = []
    for mask in range(1 << b):
        positions = prefix_positions(mask, b)
        if len(positions) != b or len(set(positions)) != b:
            raise AssertionError("bad dyadic prefix")
        prefixes.append((mask, positions, affine_constant(positions)))

    reference_prefix = prefixes[0][2]
    inverse_scale = pow(pow(2, 2 * b, low_modulus), -1, low_modulus)
    selector_digest = hashlib.sha256()
    common_signature: int | None = None
    inverse_roots = []

    for mask, prefix, prefix_value in prefixes:
        correction = (-(prefix_value - reference_prefix) * inverse_scale) % low_modulus
        suffix = chosen[correction]
        suffix_value = actual_values[correction]
        combined_value = 3**b * prefix_value + 2 ** (2 * b) * suffix_value

        residue = combined_value % full_modulus
        if common_signature is None:
            common_signature = residue
        elif residue != common_signature:
            raise AssertionError("correlated words do not collide")

        root_residue = (
            -combined_value * pow(3, -2 * b, 1 << b)
        ) % (1 << b)
        inverse_roots.append(root_residue)

        selector_digest.update(mask.to_bytes(max(1, (b + 7) // 8), "big"))
        selector_digest.update(bytes(prefix))
        selector_digest.update(bytes(suffix))
        selector_digest.update(
            correction.to_bytes(max(1, (low_modulus.bit_length() + 7) // 8), "big")
        )

    if len(set(inverse_roots)) != 1 << b:
        raise AssertionError("dyadic inverse-root projection is incomplete")

    core_length = 8 * b
    tail = shortest_odd_tail(b, core_length)
    if not 3 ** (2 * b + tail) > 2 ** (core_length + tail):
        raise AssertionError("tail is not supercritical")
    if tail and 3 ** (2 * b + tail - 1) > 2 ** (core_length + tail - 1):
        raise AssertionError("tail is not shortest")

    return {
        "b": b,
        "word_count": comb(length, b),
        "gadget_length": length,
        "gadget_weight": b,
        "first_complete_signature": signature,
        "complete_signature_count": len(complete_signatures),
        "distinct_residues_mod_3_2b": len(represented),
        "unit_residues_mod_3_2b": 2 * 3 ** (2 * b - 1),
        "gadget_representative_digest": gadget_digest.hexdigest(),
        "selector_branches": 1 << b,
        "selector_core_length": core_length,
        "selector_weight": 2 * b,
        "selector_precision": 2 * b,
        "selector_digest": selector_digest.hexdigest(),
        "shortest_odd_tail": tail,
        "supercritical_length": core_length + tail,
        "supercritical_weight": 2 * b + tail,
    }


def main() -> None:
    records = [gadget_record(b) for b in range(1, 7)]
    payload = {"experiment": "X-0019", "records": records}
    semantic = hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()

    print("full-offset gadget and correlated-selector checks passed")
    for record in records:
        print(
            "b={b} signature={first_complete_signature} "
            "complete={complete_signature_count} represented={distinct_residues_mod_3_2b} "
            "branches={selector_branches} core={selector_core_length} "
            "tail={shortest_odd_tail} final={supercritical_length}".format(**record)
        )
    print(f"semantic_sha256={semantic}")


if __name__ == "__main__":
    main()
