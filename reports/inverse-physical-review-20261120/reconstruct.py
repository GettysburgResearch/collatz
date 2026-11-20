#!/usr/bin/env python3
"""Independently reconstruct a full int32 potential from class-two bytes.

Optionally compare every output byte with the synthesis table and/or write
the reconstructed table for the independent scalar C++ verifier. No author
decoder or synthesis module is imported.
"""
from __future__ import annotations

import argparse
from array import array
import gzip
import hashlib
import json
import lzma
from pathlib import Path
import sys


def need(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("metadata", type=Path)
    parser.add_argument("--reference", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--values", type=Path,
                        help="regenerated class-two bytes for fixed-policy-bits-v1")
    args = parser.parse_args()
    meta = json.loads(args.metadata.read_text())
    need(meta["format"] in ("class-two-u8-v1", "fixed-policy-bits-v1"),
         "unknown potential encoding")
    depth, q = meta["digits"], meta["q"]
    count = 3 ** (depth - 1)
    policy_format = meta["format"] == "fixed-policy-bits-v1"
    encoded = (args.metadata.parent / meta["policy_file" if policy_format else "values_file"]).read_bytes()
    if encoded.startswith(b"\x1f\x8b"):
        decoded = gzip.decompress(encoded)
    elif encoded.startswith(b"\xfd7zXZ\x00"):
        decoded = lzma.decompress(encoded)
    else:
        raise ValueError("unsupported byte-stream compression")
    if policy_format:
        need(args.values is not None, "fixed-policy metadata requires --values")
        need(meta["policy_bits"] == 2 * (count // 3), "wrong policy bit count")
        need(len(decoded) == (meta["policy_bits"] + 7) // 8, "wrong decoded policy length")
        padding = meta["policy_bits"] % 8
        need(not padding or decoded[-1] >> padding == 0, "nonzero policy padding")
        need(hashlib.sha256(decoded).hexdigest() == meta["policy_sha256"],
             "decoded policy digest mismatch")
        values = args.values.read_bytes()
    else:
        values = decoded
    need(len(values) == count, "wrong class-two length")
    need(hashlib.sha256(values).hexdigest() == meta["values_sha256"],
         "decoded class-two digest mismatch")
    need(q + max(values) == meta["max_credit"], "credit metadata mismatch")
    reference = args.reference.open("rb") if args.reference else None
    output = args.output.open("wb") if args.output else None
    digest = hashlib.sha256()
    try:
        for first in range(0, count, 65536):
            block = array("i")
            need(block.itemsize == 4, "int32 array required")
            for j in range(first, min(first + 65536, count)):
                # Residue 3j+1 must take E; its double is 3(2j)+2.
                block.append(q + values[(2 * j) % count])
                block.append(values[j])
            if sys.byteorder != "little":
                block.byteswap()
            raw = block.tobytes()
            if reference:
                need(reference.read(len(raw)) == raw,
                     "full synthesis table differs from independent reconstruction")
            if output:
                output.write(raw)
            digest.update(raw)
        if reference:
            need(reference.read(1) == b"", "reference has trailing bytes")
    finally:
        if reference:
            reference.close()
        if output:
            output.close()
    full_hash = digest.hexdigest()
    expected_full = meta["full_int32_sha256"] if policy_format else meta["provenance"]["full_int32_sha256"]
    need(full_hash == expected_full,
         "reconstructed full-table digest mismatch")
    print(json.dumps({
        "status": "PASS",
        "digits": depth,
        "p": meta["p"],
        "q": q,
        "encoded_sha256": hashlib.sha256(encoded).hexdigest(),
        "encoded_bytes": len(encoded),
        "decoded_policy_sha256": hashlib.sha256(decoded).hexdigest() if policy_format else None,
        "decoded_policy_bits": meta["policy_bits"] if policy_format else None,
        "class_two_sha256": hashlib.sha256(values).hexdigest(),
        "full_int32_sha256": full_hash,
        "full_int32_bytes": 8 * count,
        "unit_rows": 2 * count,
        "reference_compared_byte_for_byte": bool(reference),
    }, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
