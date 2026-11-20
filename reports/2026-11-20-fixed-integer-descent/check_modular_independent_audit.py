#!/usr/bin/env python3
"""Independent cyclic maximum: start at 1/5, join initial/final good runs.

This does not import the original scanner or adaptive-core code. It checks
the four modulus-2^24 constants needed by the cap-five and cap-six theorems.
"""

import json
from pathlib import Path


def require(condition, message):
    if not condition:
        raise ValueError(message)


def main():
    modulus = 1 << 24
    period = 1 << 22
    plan = [(cap, delta) for cap in (5, 6) for delta in (0, 1)]
    results = {key: 0 for key in plan}
    counts = 0
    for seed in (1, 5):
        current = [0] * 4
        prefix = [0] * 4
        maximum = [0] * 4
        seen_bad = [False] * 4
        value = seed
        for _ in range(period):
            runs = [((value << 1) ^ value).bit_count() // 2,
                    (((value - 1) << 1) ^ (value - 1)).bit_count() // 2]
            for i, (cap, delta) in enumerate(plan):
                if runs[delta] <= cap:
                    current[i] += 1
                    maximum[i] = max(maximum[i], current[i])
                else:
                    if not seen_bad[i]:
                        prefix[i] = current[i]
                        seen_bad[i] = True
                    current[i] = 0
            counts += 1
            value = 3 * value % modulus
        require(value == seed, "multiplicative cycle did not close")
        for i, key in enumerate(plan):
            require(seen_bad[i], "complete cycle has no target")
            results[key] = max(results[key], maximum[i], prefix[i] + current[i])

    reference = json.loads(Path(
        "reports/2026-11-20-fixed-integer-descent/modular-run-hitting.json"
    ).read_text(encoding="utf-8"))
    for key, bound in results.items():
        row = next(row for row in reference["rows"]
                   if row["bits"] == 24 and row["cap"] == key[0]
                   and row["delta"] == key[1])
        require(bound == row["maximum_modular_wait"], "independent maximum differs")

    report = {
        "schema": "independent-prefix-suffix-run-audit-v1",
        "bits": 24,
        "actual_residue_states_visited": counts,
        "cap_shift_tests": 4 * counts,
        "rows": [{"cap": cap, "delta": delta, "maximum": bound}
                 for (cap, delta), bound in results.items()],
        "scope": "independent maxima only; root ordered digests are not independently reproduced",
    }
    frozen = Path("reports/2026-11-20-fixed-integer-descent/modular-independent-audit.json")
    require(report == json.loads(frozen.read_text(encoding="utf-8")),
            "independent audit report changed")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
