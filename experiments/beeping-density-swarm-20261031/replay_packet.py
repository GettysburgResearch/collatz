#!/usr/bin/env python3
"""Replay the second swarm packet without changing its saved evidence."""
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
    ("contact_transport", "check_contact_transport.py", "contact_transport_checks.json"),
    ("independent_contact_review", "check_contact_review.py", "contact_review_checks.json"),
    ("inverse_green", "check_inverse_green.py", "inverse_green_checks.json"),
    ("harmonic_spectrum", "check_harmonic_spectrum.py", "harmonic_spectrum_checks.json"),
    ("critical_energy", "check_critical_energy.py", "critical_energy_checks.json"),
)


def digest(value: object) -> str:
    body = json.dumps(value, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(body).hexdigest()


def replay(job: tuple[str, str, str]) -> dict:
    name, program, evidence = job
    expected = json.loads((HERE / evidence).read_text(encoding="utf-8"))
    modes = []
    with TemporaryDirectory(prefix="collatz-second-swarm-") as temporary:
        for mode, flags in (("normal", ()), ("optimized", ("-O",))):
            target = Path(temporary) / f"{name}-{mode}.json"
            argv = [sys.executable, "-X", "utf8", "-B", *flags,
                    str(HERE / program), "--output", str(target)]
            result = subprocess.run(argv, cwd=HERE, capture_output=True,
                                    text=True, encoding="utf-8", timeout=240)
            if result.returncode:
                raise RuntimeError(f"{name}/{mode}: exit {result.returncode}\n"
                                   + result.stdout[-4000:] + result.stderr[-4000:])
            actual = json.loads(target.read_text(encoding="utf-8"))
            if actual != expected:
                raise RuntimeError(f"{name}/{mode}: complete JSON differs from {evidence}")
            modes.append({"mode": mode, "exit_code": result.returncode,
                          "complete_saved_json_match": True,
                          "semantic_sha256": digest(actual)})
    return {"name": name, "program": program, "arguments": [],
            "saved_evidence": evidence, "modes": modes}


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
        "schema": "collatz-second-swarm-replay/v1", "status": "PASS",
        "scope": "five bounded exact suites, normal and optimized; full saved-JSON equality; no Collatz proof, reachability decision, or external Lean replay",
        "python": sys.version, "platform": sys.platform,
        "program_sha256": sources, "suites": rows,
        "suite_count": len(rows), "process_count": sum(len(r["modes"]) for r in rows),
    }
    encoded = json.dumps(receipt, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded, encoding="utf-8")
    print(json.dumps({"status": "PASS", "suites": len(rows),
                      "processes": receipt["process_count"],
                      "all_saved_json_equal": True,
                      "output": str(args.output) if args.output else None}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
