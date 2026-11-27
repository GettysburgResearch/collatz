"""Fresh normal/optimized replay of the two new exact finite certificates."""

from __future__ import annotations

import ast
import hashlib
import json
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[2]
PACKET = ROOT / "research/killed-green-head-closure-20261124"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    rows = []
    for folder, script_name in [("escape-analysis", "controls.py"), ("global-bridge", "check.py")]:
        script = PACKET / folder / script_name
        original_digest = digest(script)
        assertion_count = sum(isinstance(node, ast.Assert) for node in ast.walk(ast.parse(script.read_text())))
        if assertion_count:
            raise RuntimeError((folder, "checks disappear under -O", assertion_count))
        expected = json.loads((script.parent / "CONTROLS.json").read_text())
        outputs = []
        for flags in [[], ["-O"]]:
            command = [sys.executable, *flags, "-X", "utf8", "-B", str(script)]
            result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, timeout=180)
            if result.returncode != 0 or result.stderr:
                raise RuntimeError((folder, flags, result.returncode, result.stdout, result.stderr))
            parsed = json.loads(result.stdout)
            if parsed != expected:
                raise RuntimeError((folder, flags, "published expectation mismatch", parsed))
            outputs.append(result.stdout)
        if outputs[0] != outputs[1] or original_digest != digest(script):
            raise RuntimeError((folder, "unstable source or output"))
        sources = {str(script.relative_to(ROOT)): digest(script)}
        for certificate in sorted(script.parent.glob("cover*.txt")):
            sources[str(certificate.relative_to(ROOT))] = digest(certificate)
        rows.append({
            "sources_sha256": sources,
            "normal_exit": 0,
            "optimized_exit": 0,
            "identical_outputs": True,
            "ast_assert_nodes": assertion_count,
            "output_sha256": hashlib.sha256(outputs[0].encode()).hexdigest(),
            "checks": expected,
        })
    print(json.dumps({"python_version": sys.version.split()[0], "replays": rows,
                      "scope": "Exact finite arithmetic, not a proof of the missing universal upper bound."},
                     indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
