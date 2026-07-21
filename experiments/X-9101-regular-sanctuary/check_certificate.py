"""Dependency-free verifier for a regular-sanctuary JSON certificate."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from automata import DFA
from transducer import shortcut_transducer
from verify import verify_candidate


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    parser.add_argument(
        "--allow-nonstandard-control",
        action="store_true",
        help="permit the 3n-1 positive-control map; never use this for a Collatz claim",
    )
    args = parser.parse_args()

    with args.certificate.open("r", encoding="utf-8") as handle:
        payload = json.load(handle)
    if not isinstance(payload, dict) or not isinstance(payload.get("dfa"), dict):
        parser.error("certificate must contain a DFA object")
    if payload.get("schema") != "regular-sanctuary-certificate-v1":
        parser.error("unsupported or missing certificate schema")
    map_id = payload.get("map")
    offsets = {
        "shortcut_3n_plus_1": 1,
        "shortcut_3n_minus_1": -1,
    }
    if not isinstance(map_id, str) or map_id not in offsets:
        parser.error("certificate map must be an explicit supported map ID")
    odd_offset = offsets[map_id]
    if odd_offset != 1 and not args.allow_nonstandard_control:
        parser.error(
            "nonstandard map rejected; pass --allow-nonstandard-control only for tests"
        )
    dfa = DFA.from_dict(payload["dfa"])
    machine = shortcut_transducer(odd_offset)
    result = verify_candidate(dfa, machine)
    output = {
        "certificate_schema": payload["schema"],
        "map": map_id,
        "transducer": machine.name,
        "verification": result.to_dict(),
    }
    json.dump(output, sys.stdout, indent=2, sort_keys=True)
    sys.stdout.write("\n")
    if not result.valid:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
