#!/usr/bin/env python3
"""Lightweight integrity and arithmetic checks for the Mazur 2026 import.

The repository intentionally does not redistribute the two source PDFs. By
passing ``--pdf-dir`` a reviewer can verify separately obtained copies against
the exact recorded hashes. Without that option the script checks the source
metadata, the non-redistribution boundary, and the small integer/rational
calculations exposed in the review packet.

This script does not replay either Lean development or the large predecessor
certificate payloads.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path
import sys
from typing import Any

ROOT = Path(__file__).resolve().parent
SOURCES = ROOT / "sources.json"
REPORT = ROOT / "local-check-report.json"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def record(checks: list[dict[str, object]], name: str, ok: bool, detail: object) -> None:
    checks.append({"name": name, "ok": bool(ok), "detail": detail})


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--pdf-dir",
        type=Path,
        help="directory containing the two separately obtained source PDFs",
    )
    parser.add_argument(
        "--no-write-report",
        action="store_true",
        help="run checks without replacing local-check-report.json",
    )
    return parser.parse_args()


def check_source_pdf(
    checks: list[dict[str, object]],
    source: dict[str, Any],
    pdf_dir: Path | None,
) -> None:
    pdf = source.get("supplied_pdf", {})
    sid = source["id"]
    filename = pdf.get("filename")
    record(checks, f"{sid}:pdf_filename", isinstance(filename, str) and filename.endswith(".pdf"), filename)
    record(checks, f"{sid}:pdf_pages", isinstance(pdf.get("pages"), int) and pdf["pages"] > 0, pdf.get("pages"))
    record(checks, f"{sid}:pdf_bytes", isinstance(pdf.get("bytes"), int) and pdf["bytes"] > 0, pdf.get("bytes"))
    digest_expected = pdf.get("sha256")
    record(
        checks,
        f"{sid}:pdf_hash_shape",
        isinstance(digest_expected, str) and len(digest_expected) == 64,
        digest_expected,
    )
    record(
        checks,
        f"{sid}:not_redistributed",
        pdf.get("repository_copy") is False,
        pdf.get("redistribution_note"),
    )

    if pdf_dir is None:
        return

    path = pdf_dir / filename
    exists = path.is_file()
    record(checks, f"{sid}:supplied_pdf_exists", exists, filename)
    if not exists:
        return
    raw = path.read_bytes()
    record(checks, f"{sid}:pdf_magic", raw.startswith(b"%PDF-"), raw[:8].decode("latin-1", "replace"))
    record(checks, f"{sid}:pdf_eof", b"%%EOF" in raw[-2048:], "EOF marker in final 2048 bytes")
    record(checks, f"{sid}:pdf_size", len(raw) == pdf["bytes"], len(raw))
    digest = sha256(path)
    record(checks, f"{sid}:pdf_sha256", digest == digest_expected, digest)


def main() -> int:
    args = parse_args()
    checks: list[dict[str, object]] = []
    data = json.loads(SOURCES.read_text(encoding="utf-8"))

    record(checks, "schema_version", data.get("schema_version") == "1.0", data.get("schema_version"))
    records = data.get("records", [])
    record(checks, "record_count", len(records) == 2, len(records))

    committed_pdfs = sorted(path.name for path in (ROOT / "papers").glob("*.pdf"))
    record(checks, "no_pdf_binaries_committed", not committed_pdfs, committed_pdfs)
    record(checks, "paper_index_exists", (ROOT / "papers/README.md").is_file(), "papers/README.md")

    for source in records:
        check_source_pdf(checks, source, args.pdf_dir)

    # Exact coefficient directions from the predecessor certificate.
    Q = 2**28
    A = 76_981_049
    B1 = 207_142_911
    B3 = 386_810_365
    record(checks, "pred:coefficient_A", A**1000 * 2**1802 <= Q**1000, "A^1000*2^1802 <= Q^1000")
    record(checks, "pred:coefficient_B1", B1**1000 * 2**1802 <= Q**1000 * 3**901, "B1^1000*2^1802 <= Q^1000*3^901")
    record(checks, "pred:coefficient_B3", B3**1000 * 2**901 <= Q**1000 * 3**901, "B3^1000*2^901 <= Q^1000*3^901")

    appendix_rows = [
        (2_134_179_986_800_640, A * 6_357_317 + B1 * 7_945_915),
        (1_036_938_517_676_032, A * 13_483_121),
        (1_706_529_287_831_552, A * 2_896_800 + B3 * 3_838_338),
    ]
    for idx, (lhs, rhs) in enumerate(appendix_rows, start=1):
        record(checks, f"pred:appendix_row_{idx}", lhs <= rhs, {"lhs": lhs, "rhs": rhs, "margin": rhs - lhs})

    delta = 5.0 - 3.0 * math.log2(3.0)
    record(checks, "pred:adaptive_delta_positive", delta > 0.0, delta)
    record(
        checks,
        "pred:nonzero_selector_fraction",
        484_085 + 716 == 484_801,
        {"nonzero": 484_801, "family_rows": 43_046_721, "fraction": 484_801 / 43_046_721},
    )

    # Exact clock and exponent identities from the natural-density paper.
    d0 = Fraction(6993, 200000)
    cap = Fraction(5, 143)
    record(checks, "nd:d0_below_cap", d0 < cap, str(cap - d0))
    record(checks, "nd:d0_exact_margin", cap - d0 == Fraction(1, 28_600_000), str(cap - d0))
    record(checks, "nd:raw_clock_numerator_identity", 1_509_503 == 3 * 501_501 + 5_000, "1509503 = 3*501501 + 5000")

    c_syr = 501_501 / (5_000 * math.log(2.0))
    c_coll = 1_509_503 / (5_000 * math.log(2.0))
    record(checks, "nd:C_Syr_lt_145", c_syr < 145.0, c_syr)
    record(checks, "nd:C_Coll_lt_436", c_coll < 436.0, c_coll)
    record(checks, "nd:C_Coll_identity", math.isclose(c_coll, 3.0 * c_syr + 1.0 / math.log(2.0), rel_tol=0.0, abs_tol=1e-12), c_coll)
    record(checks, "nd:rhin_phase_cap", Fraction(1, 2) / Fraction(143, 10) == Fraction(5, 143), "1/(2*(143/10)) = 5/143")

    required_docs = {
        "README.md": ["EXTERNAL SOURCE-QUALIFIED", "0.901", "not redistributed"],
        "CLAIM_MATRIX.md": ["MZ-BRIDGE-001", "PENDING NARROW REVIEW"],
        "predecessor-x090.md": ["5f76a170e74ea5b0c37c56683bd4c1e9d72e5e3f", "215,233,605", "1.13%"],
        "natural-density-log-time.md": ["ca3dd0d63920411213403092aecc6946619eb082", "beta<0.901"],
        "synthesis-and-roadmap.md": ["Bridge theorem", "beta<gamma", "not currently established"],
        "NOTICE.md": ["Lech Mazur", "not redistributed"],
        "papers/README.md": ["cbae5d71", "08a46dd1", "--pdf-dir"],
    }
    for relative, needles in required_docs.items():
        text = (ROOT / relative).read_text(encoding="utf-8")
        for needle in needles:
            record(checks, f"doc:{relative}:{needle}", needle in text, needle)

    passed = all(item["ok"] for item in checks)
    report = {
        "schema_version": "1.0",
        "scope": "source metadata, optional supplied-PDF integrity, and small exact arithmetic only; no Lean or large-payload replay",
        "pdf_replay_mode": "supplied_files" if args.pdf_dir is not None else "metadata_only",
        "passed": passed,
        "checks": checks,
    }
    if not args.no_write_report:
        REPORT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"passed": passed, "check_count": len(checks), "pdf_replay_mode": report["pdf_replay_mode"]}, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
