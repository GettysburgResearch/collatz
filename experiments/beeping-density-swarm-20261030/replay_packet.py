#!/usr/bin/env python3
"""Replay this bounded packet without changing its saved evidence files."""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory

HERE = Path(__file__).resolve().parent
JOBS = (
    ("beeping", "verify_beeping.py", (), "--output", "beeping_evidence.json"),
    ("density", "check_density_bridge.py", ("--maximum", "100000"),
     "--output", "density_bridge_report.json"),
    ("spikes", "check_negative_spikes.py", (), "--output", "negative_spikes_report.json"),
    ("ranks", "check_rank_envelope.py", ("--bound", "10000"),
     "--out", "rank_envelope_results.json"),
    ("near_invariants", "verify_near_invariants.py", (),
     "--output", "near_invariants_evidence.json"),
    ("regularity_review", "check_regularity_review.py", (),
     None, "regularity_review_checks.json"),
)


def digest(value: object) -> str:
    body = json.dumps(value, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(body).hexdigest()


def replay(job: tuple) -> dict:
    name, program, arguments, output_flag, expected_file = job
    expected = json.loads((HERE / expected_file).read_text(encoding="utf-8"))
    modes = []
    with TemporaryDirectory(prefix="collatz-beeping-density-") as temporary:
        for mode, flags in (("normal", ()), ("optimized", ("-O",))):
            target = Path(temporary) / f"{name}-{mode}.json"
            argv = [sys.executable, "-X", "utf8", "-B", *flags,
                    str(HERE / program), *arguments]
            if output_flag:
                argv.extend((output_flag, str(target)))
            result = subprocess.run(argv, cwd=HERE, capture_output=True,
                                    text=True, encoding="utf-8", timeout=180)
            if result.returncode:
                raise RuntimeError(f"{name}/{mode}: exit {result.returncode}\n"
                                   + result.stdout[-4000:] + result.stderr[-4000:])
            actual = json.loads(target.read_text(encoding="utf-8")
                                if output_flag else result.stdout)
            if actual != expected:
                raise RuntimeError(f"{name}/{mode}: complete JSON differs from {expected_file}")
            modes.append({"mode": mode, "exit_code": result.returncode,
                          "complete_saved_json_match": True,
                          "semantic_sha256": digest(actual)})
    return {"name": name, "program": program, "arguments": list(arguments),
            "saved_evidence": expected_file, "modes": modes}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        help="Optional aggregate receipt; use a path outside the checkout.")
    parser.add_argument("--jobs", type=int, default=3)
    args = parser.parse_args()
    if args.jobs < 1:
        parser.error("--jobs must be positive")
    if args.output and args.output.resolve().is_relative_to(HERE):
        parser.error("keep the aggregate receipt outside the experiment directory")
    with ThreadPoolExecutor(max_workers=min(args.jobs, len(JOBS))) as pool:
        rows = list(pool.map(replay, JOBS))
    sources = {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
               for p in sorted(HERE.glob("*.py"))}
    receipt = {
        "schema": "beeping-density-packet-replay/v1", "status": "PASS",
        "scope": "six bounded suites, normal and optimized; full saved-JSON equality; not a Collatz proof or external Lean replay",
        "python": sys.version, "platform": sys.platform,
        "program_sha256": sources, "suites": rows,
        "suite_count": len(rows), "process_count": sum(len(r["modes"]) for r in rows),
    }
    encoded = json.dumps(receipt, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded, encoding="utf-8")
    print(json.dumps({"status": "PASS", "suites": len(rows), "processes": receipt["process_count"],
                      "all_saved_json_equal": True, "output": str(args.output) if args.output else None}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
