#!/usr/bin/env python3
"""Mechanical integrity checks for literature wave 11."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    ROOT / "literature/LIVE_REPO_REVIEW_WAVE11.md",
    ROOT / "literature/SOURCE_LEDGER_WAVE11.md",
    ROOT / "literature/claim-maps/WAVE11.md",
    ROOT / "literature/UNVERIFIED-WAVE11.md",
    ROOT / "literature/imported-theorems/LIT-KTHM-0065-verified-floor-fixed-support-pulse-closure.md",
    ROOT / "literature/experiments/LIT-X-0065-verified-floor-fixed-support/run.py",
    ROOT / "literature/experiments/LIT-X-0065-verified-floor-fixed-support/verify.py",
    ROOT / "literature/experiments/LIT-X-0065-verified-floor-fixed-support/results/canonical.json",
    ROOT / "literature/experiments/LIT-X-0065-verified-floor-fixed-support/README.md",
]

EXPECTED_DIGEST = "c730cce495223542e2d15e424ca0ba94996c2d0382289baab3604344abe8b179"


def main() -> None:
    missing = [str(path.relative_to(ROOT)) for path in REQUIRED if not path.is_file()]
    if missing:
        raise SystemExit("missing wave-11 files: " + ", ".join(missing))

    claim = REQUIRED[4].read_text()
    assert "P_3:\\quad 1\\le s\\le18" in claim
    assert "P_{11}:\\quad 1\\le s\\le117" in claim
    assert EXPECTED_DIGEST in claim
    assert "support 19" in claim and "support 118" in claim

    matveev = (
        ROOT
        / "literature/imported-theorems/LIT-KTHM-0060-matveev-log2-log3-specialization.md"
    ).read_text()
    assert "weighted parameter `B`" in matveev
    assert "incorrectly labeled" in matveev

    result_path = REQUIRED[7]
    result = json.loads(result_path.read_text())
    assert result["experiment_id"] == "LIT-X-0065"
    assert result["claim_id"] == "LIT-KTHM-0065"
    assert result["semantic_sha256"] == EXPECTED_DIGEST
    assert result["conclusion"]["first_uncovered_supports"] == {
        "P3": 19,
        "P11": 118,
    }

    copy = dict(result)
    digest = copy.pop("semantic_sha256")
    actual = hashlib.sha256(
        json.dumps(copy, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    assert actual == digest

    counts = {
        family["name"]: family["convergents"]["coverage_counts"]
        for family in result["families"]
    }
    assert counts["P3"] == {
        "verified_floor_only": 3,
        "pulse_comparison_only": 2,
        "both": 7,
        "total": 12,
    }
    assert counts["P11"] == {
        "verified_floor_only": 4,
        "pulse_comparison_only": 5,
        "both": 2,
        "total": 11,
    }

    print("literature wave 11 integrity checks passed")


if __name__ == "__main__":
    main()
