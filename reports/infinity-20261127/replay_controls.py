"""Replay explicitly listed bounded controls, in ordinary and optimized Python.

These are finite arithmetic checks, not proof of the infinite statements. The
manifest lists every local source imported by each control and its full expected
JSON output. Receipts and subprocess outputs are written outside the checkout.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    repo, out = args.repo.resolve(), args.out.resolve()
    require(not out.is_relative_to(repo), "Output must be outside the checkout")
    out.mkdir(parents=True, exist_ok=False)
    manifest_bytes = args.manifest.read_bytes()
    manifest = json.loads(manifest_bytes)
    require(isinstance(manifest, list) and manifest, "Expected a nonempty control list")
    inputs = {p for row in manifest for p in [row["script"], row["expected"], *row["local_imports"]]}
    require(all((repo / p).resolve().is_relative_to(repo) for p in inputs), "Input outside checkout")
    before = {p: (repo / p).read_bytes() for p in inputs}
    receipt = {
        "scope": "Bounded exact arithmetic controls; no universal mathematical conclusion",
        "started_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "python": sys.version,
        "driver_sha256": sha(Path(__file__).read_bytes()),
        "manifest_sha256": sha(manifest_bytes),
        "inputs": {p: sha(b) for p, b in sorted(before.items())},
        "controls": [],
    }
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", PYTHONUTF8="1")
    for item in manifest:
        outputs = []
        for mode in ([], ["-O"]):
            command = [sys.executable, "-X", "utf8", "-B", *mode, str(repo / item["script"])]
            started = time.monotonic()
            result = subprocess.run(command, cwd=repo, env=env, capture_output=True)
            filename = Path(item["script"]).stem + (".optimized" if mode else ".normal")
            (out / (filename + ".json")).write_bytes(result.stdout)
            (out / (filename + ".stderr")).write_bytes(result.stderr)
            row = {
                "script": item["script"], "command": command,
                "exit_code": result.returncode,
                "seconds": round(time.monotonic() - started, 3),
                "stdout_sha256": sha(result.stdout), "stderr_sha256": sha(result.stderr),
            }
            receipt["controls"].append(row)
            (out / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
            require(result.returncode == 0 and not result.stderr, f"Control failed: {filename}")
            actual = json.loads(result.stdout)
            require(actual == json.loads(before[item["expected"]]), f"Full output differs: {filename}")
            row["full_json_matches"] = True
            outputs.append(result.stdout)
        require(outputs[0] == outputs[1], f"Optimized output differs: {item['script']}")
        print(f"PASS {item['script']}: complete JSON, ordinary and optimized", flush=True)
    require(all((repo / p).read_bytes() == b for p, b in before.items()), "Source changed during replay")
    require(args.manifest.read_bytes() == manifest_bytes, "Manifest changed during replay")
    receipt["finished_utc"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    receipt["complete"] = True
    (out / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")


if __name__ == "__main__":
    main()
