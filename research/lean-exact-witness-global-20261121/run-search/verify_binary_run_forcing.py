#!/usr/bin/env python3
"""Focused exact replay of the signed-shadow binary-run forcing theorem.

Generation uses a modular power and a signed odd trace. Verification replays
the POSITIVE ordinary orbit one clock at a time, then checks the independent
signed gap equations, binary borrow, and claimed high pattern. Forty selected
representatives exercise unbounded families; they are not a search to a
conjectural stopping bound. The all-parameter proof is in the adjacent note
and the SignedShadow/DyadicCoset/BinaryRunForcing Lean modules.

Every rejection uses an explicit exception and remains active under python -O.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[3]
PACKET = ROOT / "research/lean-exact-witness-global-20261121"
DEFAULT_OUTPUT = ROOT / "reports/lean-exact-witness-global-20261121/global-synthesis/binary-run-cases.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def run_count_text(n: int) -> int:
    """Generator's high-to-low textual count."""
    require(n >= 0, "negative run-count argument")
    previous = "0"
    count = 0
    for bit in bin(n)[2:]:
        count += bit == "1" and previous == "0"
        previous = bit
    return count


def run_count_bits(n: int) -> int:
    """Verifier's independent count: top bit of every maximal one-run."""
    require(n >= 0, "negative run-count argument")
    return (n & ~(n >> 1)).bit_count()


def signed_next(z: int) -> tuple[int, int]:
    require(z % 2 == 1, "signed source must be odd")
    q = 3 * z + 1
    a = 0
    while q % 2 == 0:
        require(q != 0, "zero signed numerator")
        q //= 2
        a += 1
    require(a > 0, "odd signed edge needs a positive gap")
    return a, q


def encode(n: int) -> str:
    return hex(n)


def decode(value: Any) -> int:
    require(isinstance(value, str), "integer certificate must be a hex string")
    return int(value, 16)


def make_case(label: str, s: int, u: int, d: int, low: int,
              family: dict[str, Any] | None = None) -> dict[str, Any]:
    require(s >= 1 and u > 0 and u % 2 == 1 and low % 2 == 1, "invalid input")
    j_bound = 4 ** s - 1
    require((4 ** j_bound) * abs(low) < 2 ** d, "insufficient initial separation")
    source = (1 << d) * u + low
    require(source > 0, "source must be positive")
    alternating = (4 ** s - 1) // 3
    patterns = (1 + 8 * alternating, (4 ** (s + 1) - 1) // 3)
    modulus = 1 << (2 * s + 2)
    residue = u % modulus
    h = 0
    while residue not in patterns:
        h += 1
        require(h <= j_bound, "modular forcing bound failed")
        residue = 3 * residue % modulus
    shadow = low
    gaps: list[int] = []
    for _ in range(h):
        a, shadow = signed_next(shadow)
        gaps.append(a)
    clock = sum(gaps)
    require(clock < d, "shadow clock consumed its separation")
    high = 3 ** h * u
    endpoint = (1 << (d - clock)) * high + shadow
    return {
        "label": label,
        "s": s,
        "source": encode(source),
        "high": encode(u),
        "separation": d,
        "low": encode(low),
        "odd_clock": h,
        "ordinary_clock": clock,
        "gaps": gaps,
        "shadow_endpoint": encode(shadow),
        "endpoint": encode(endpoint),
        "high_residue": residue,
        "source_bits": source.bit_length(),
        "source_runs": run_count_text(source),
        "endpoint_runs": run_count_text(endpoint),
        "family": family,
    }


def verify_case(case: dict[str, Any]) -> None:
    """Positive-path replay does not use the generator's endpoint recurrence."""
    s = case["s"]
    d = case["separation"]
    h = case["odd_clock"]
    clock = case["ordinary_clock"]
    gaps = case["gaps"]
    n, u, low = (decode(case[key]) for key in ("source", "high", "low"))
    require(type(s) is int and s >= 1, "invalid cap")
    require(type(d) is int and d >= 1, "invalid binary separation")
    require(n > 0 and n % 2 == 1, "ordinary source is not positive odd")
    require(u > 0 and u % 2 == 1 and low % 2 == 1, "invalid signed split parity")
    require(n == (1 << d) * u + low, "wrong source split")
    require(4 ** (4 ** s - 1) * abs(low) < 2 ** d, "false separation guard")
    require(type(h) is int and 0 <= h < 4 ** s, "wrong odd-event budget")
    require(isinstance(gaps, list) and len(gaps) == h, "wrong gap-word length")
    require(all(type(a) is int and a > 0 for a in gaps), "nonpositive gap")
    require(type(clock) is int and clock == sum(gaps), "wrong ordinary clock")
    require(clock < d and clock <= n.bit_length() - 1, "wrong physical clock bound")

    actual = n
    signed = low
    elapsed = 0
    high = u
    for j, a in enumerate(gaps, 1):
        # Literal positive shortcut replay, checking every branch in the word.
        require(actual > 0 and actual % 2 == 1, "nonphysical odd boundary")
        actual = (3 * actual + 1) // 2
        elapsed += 1
        for _ in range(a - 1):
            require(actual > 0 and actual % 2 == 0, "nonphysical halving branch")
            actual //= 2
            elapsed += 1
        require(actual > 0 and actual % 2 == 1, "gap was not the exact valuation")

        # Independent signed arithmetic, using only the supplied claimed gap.
        numerator = 3 * signed + 1
        require(numerator != 0 and numerator % (1 << a) == 0, "false signed gap")
        signed = numerator // (1 << a)
        require(signed % 2 == 1, "signed endpoint is not odd")
        high *= 3
        require(elapsed < d, "intermediate shadow exhausted separation")
        require((1 << elapsed) * abs(signed) <= 4 ** j * abs(low),
                "cleared signed magnitude bound failed")
        require(actual == (1 << (d - elapsed)) * high + signed,
                "signed shadow does not match actual positive path")

    require(elapsed == clock, "replayed clock disagrees")
    require(signed == decode(case["shadow_endpoint"]), "wrong shadow endpoint")
    require(actual == decode(case["endpoint"]), "wrong ordinary endpoint")
    remaining = d - clock
    require(0 < abs(signed) < (1 << remaining), "false final low-block bound")
    require(actual == (1 << remaining) * high + signed, "wrong final split")

    # Explicit borrow/concatenation audit, including high=1 and signed=-1.
    if signed < 0:
        borrowed = (1 << remaining) + signed
        require(borrowed > 0 and (high - 1) % 2 == 0, "invalid negative borrow")
        require(actual == (1 << remaining) * (high - 1) + borrowed,
                "negative borrow arithmetic failed")
        require(run_count_bits(actual) == run_count_bits(high - 1) + run_count_bits(borrowed),
                "negative borrow joined across a zero boundary")
        require(run_count_bits(high - 1) + 1 >= run_count_bits(high),
                "subtracting one lost more than one run")
    else:
        join = int(bool(signed & (1 << (remaining - 1))))
        require(run_count_bits(actual) == run_count_bits(high) + run_count_bits(signed) - join,
                "positive concatenation join failed")
    require(run_count_bits(actual) >= run_count_bits(high), "high runs were not retained")

    residue = high % (1 << (2 * s + 2))
    pattern_one = 1 + 8 * sum(1 << (2 * i) for i in range(s))
    pattern_five = sum(1 << (2 * i) for i in range(s + 1))
    require(residue in (pattern_one, pattern_five), "missing forced pattern")
    require(residue == case["high_residue"], "wrong claimed residue")
    require(run_count_bits(residue) == s + 1, "pattern does not have the claimed runs")
    require(run_count_bits(actual) > s, "run cap did not exit")
    require(case["source_bits"] == n.bit_length(), "wrong source bit length")
    require(case["source_runs"] == run_count_bits(n), "wrong source run count")
    require(case["endpoint_runs"] == run_count_bits(actual), "wrong endpoint run count")

    family = case.get("family")
    if family is not None:
        require(family["kind"] == "alternating_signed_endpoints", "unknown family")
        exponents = family["exponents"]
        b = 2 * 4 ** s - 1
        require(exponents == [i * (b + 1) for i in range(2 * s)], "wrong endpoint family")
        reconstructed = sum((-1 if i % 2 == 0 else 1) * (1 << e)
                            for i, e in enumerate(exponents))
        require(reconstructed == n, "wrong family source")
        require(run_count_bits(n) == s, "family source is not initially capped")
        require(n.bit_length() - 1 >= (2 * s - 1) * b, "family is below the core cutoff")


def selected_cases() -> list[dict[str, Any]]:
    cases: list[dict[str, Any]] = []
    for s in range(1, 5):
        b = 2 * 4 ** s - 1
        exponents = [i * (b + 1) for i in range(2 * s)]
        terms = [(-1 if i % 2 == 0 else 1) * (1 << e)
                 for i, e in enumerate(exponents)]
        # Every cut of the one displayed source; both low signs occur for s>1.
        for cut in range(1, len(exponents)):
            d = exponents[cut]
            low = sum(terms[:cut])
            u = sum(terms[cut:]) // (1 << d)
            cases.append(make_case(
                f"endpoint_family_s{s}_cut{cut}", s, u, d, low,
                {"kind": "alternating_signed_endpoints", "exponents": exponents, "cut": cut},
            ))
        for u, low in ((1, -1), (1, 1), (3, -5), (5, 3), (7, -11), (3, 7)):
            d = 2 * (4 ** s - 1) + abs(low).bit_length() + 1
            cases.append(make_case(f"signed_s{s}_u{u}_low{low}", s, u, d, low))
    return cases


def mutation_checks(case: dict[str, Any]) -> list[dict[str, str]]:
    def change_first_gap(c: dict[str, Any]) -> None:
        c["gaps"][0] += 1
        c["ordinary_clock"] += 1

    def compatible_source_shift(c: dict[str, Any]) -> None:
        c["source"] = encode(decode(c["source"]) + 2)
        c["low"] = encode(decode(c["low"]) + 2)

    mutations = (
        ("source", lambda c: c.__setitem__("source", encode(decode(c["source"]) + 2))),
        ("high", lambda c: c.__setitem__("high", encode(decode(c["high"]) + 2))),
        ("low_sign", lambda c: c.__setitem__("low", encode(-decode(c["low"])))),
        ("low_parity", lambda c: c.__setitem__("low", encode(decode(c["low"]) + 1))),
        ("separation", lambda c: c.__setitem__("separation", c["separation"] - 1)),
        ("odd_clock", lambda c: c.__setitem__("odd_clock", c["odd_clock"] + 1)),
        ("ordinary_clock", lambda c: c.__setitem__("ordinary_clock", c["ordinary_clock"] + 1)),
        ("coherent_first_gap_and_clock", change_first_gap),
        ("coherent_source_and_low_shift", compatible_source_shift),
        ("missing_gap", lambda c: c["gaps"].pop()),
        ("zero_gap", lambda c: c["gaps"].__setitem__(0, 0)),
        ("shadow_endpoint", lambda c: c.__setitem__("shadow_endpoint", encode(decode(c["shadow_endpoint"]) + 2))),
        ("ordinary_endpoint", lambda c: c.__setitem__("endpoint", encode(decode(c["endpoint"]) + 2))),
        ("residue", lambda c: c.__setitem__("high_residue", c["high_residue"] + 1)),
        ("endpoint_runs", lambda c: c.__setitem__("endpoint_runs", c["endpoint_runs"] + 1)),
        ("zero_cap", lambda c: c.__setitem__("s", 0)),
    )
    result = []
    require(case["gaps"], "mutation fixture needs a nonempty word")
    for name, mutate in mutations:
        changed = copy.deepcopy(case)
        mutate(changed)
        try:
            verify_case(changed)
        except ValueError as exc:
            result.append({"mutation": name, "status": "rejected", "reason": str(exc)})
        else:
            raise ValueError(f"accepted damaged certificate: {name}")
    return result


def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build_report() -> dict[str, Any]:
    cases = selected_cases()
    for case in cases:
        verify_case(case)
    files = [Path(__file__).resolve()] + [
        PACKET / "lean/Collatz" / name
        for name in ("SignedShadow.lean", "DyadicCoset.lean", "BinaryRunForcing.lean")
    ]
    return {
        "status": "exact_selected_replay_passed",
        "scope": "Forty selected representatives of unbounded proved families; no exhaustive orbit or core census.",
        "formal_boundary": "Signed physical coupling and modular forcing are Lean checked; binary run compactness and density are complete written proofs.",
        "case_count": len(cases),
        "caps": [1, 2, 3, 4],
        "maximum_source_bits": max(case["source_bits"] for case in cases),
        "maximum_ordinary_clock": max(case["ordinary_clock"] for case in cases),
        "maximum_odd_clock": max(case["odd_clock"] for case in cases),
        "source_sha256": {str(path.relative_to(ROOT)): file_hash(path) for path in files},
        "pr141_attribution": {
            "commit": "5025ef464d4b6d4f4a412a3e33c3477de68dfa8b",
            "bounded_popcount": "research/ay-persistent-20261031/PROOF.md",
            "ordered_run_antecedent": "research/ay-swarm-20261030/carry-geometry.md",
            "distinction": "The predecessor gives popcount finite cores and an exact ordered-run transducer, but does not state bounded-run compactness, signed-endpoint finite cores, or the new run occupation theorem.",
        },
        "mutations": mutation_checks(cases[0]),
        "cases": cases,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--verify", type=Path)
    args = parser.parse_args()
    if args.verify is not None:
        report = json.loads(args.verify.read_text())
        require(report["case_count"] == len(report["cases"]), "wrong case count")
        for case in report["cases"]:
            verify_case(case)
        require(report["mutations"] == mutation_checks(report["cases"][0]), "wrong mutation receipt")
        for relative, expected in report["source_sha256"].items():
            require(file_hash(ROOT / relative) == expected, f"changed source: {relative}")
        print(json.dumps({"verified_cases": len(report["cases"]), "rejected_mutations": len(report["mutations"])}))
        return
    report = build_report()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({key: report[key] for key in (
        "status", "case_count", "maximum_source_bits", "maximum_ordinary_clock", "maximum_odd_clock"
    )}, sort_keys=True))


if __name__ == "__main__":
    main()
