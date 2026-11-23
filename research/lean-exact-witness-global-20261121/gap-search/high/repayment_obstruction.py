#!/usr/bin/env python3
"""Replay one exact obstruction to universal clock-funded prefix repayment.

This is not a search and has no adjustable cutoff.  The finite replay reaches
the target's terminal odd value.  A checked gap-two self-loop then proves the
same obstruction for every length of terminal source padding.

All checks remain active under python -O.
"""

import json


SOURCE_ODD = 17
SOURCE_EVEN_EXPONENT = 1
SOURCE_GAPS = (2, 3, 4)
TARGET = 63
TARGET_GAPS = (
    1, 1, 1, 1, 1, 4, 1, 2, 1, 1, 2, 1, 1,
    1, 2, 3, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1,
    3, 1, 1, 1, 4, 2, 2, 4, 3, 1, 1, 5, 4,
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def odd_edge(n, gap):
    require(n > 0 and n % 2 == 1, "edge source must be positive and odd")
    require(gap > 0, "gap must be positive")
    numerator = 3 * n + 1
    denominator = 1 << gap
    require(numerator % denominator == 0, "specified gap is not integral")
    endpoint = numerator // denominator
    require(endpoint > 0 and endpoint % 2 == 1, "gap is not the exact odd gap")
    return endpoint


def replay(n, gaps):
    values = [n]
    for gap in gaps:
        n = odd_edge(n, gap)
        values.append(n)
    return values


def correction(gaps):
    result = 0
    suffix_length = 0
    for gap in reversed(gaps):
        result = 3 ** suffix_length + (1 << gap) * result
        suffix_length += 1
    return result


def verify():
    source = (1 << SOURCE_EVEN_EXPONENT) * SOURCE_ODD
    source_values = replay(SOURCE_ODD, SOURCE_GAPS)
    target_values = replay(TARGET, TARGET_GAPS)

    require(source_values == [17, 13, 5, 1], "unexpected source path")
    require(target_values[-1] == 1, "target path must end at one")
    require(1 not in target_values[:-1], "target path must stop at its first one")
    require(len(TARGET_GAPS) == 39, "unexpected odd-step count")
    require(sum(TARGET_GAPS) == 68, "unexpected target clock")
    require(
        3 ** len(SOURCE_GAPS) * SOURCE_ODD + correction(SOURCE_GAPS)
        == 1 << sum(SOURCE_GAPS),
        "source complete-certificate identity failed",
    )
    require(
        3 ** len(TARGET_GAPS) * TARGET + correction(TARGET_GAPS)
        == 1 << sum(TARGET_GAPS),
        "target complete-certificate identity failed",
    )

    # This lies in the narrow e=1 strip left by the enlarged odd-source cap.
    require(0 < TARGET <= 2 * source + 1, "old interval failed")
    require(3 * SOURCE_ODD + 2 < TARGET, "target is not above the odd-source cap")
    require(TARGET % 4 == 3, "target is outside the relevant residue class")
    require(all(gap <= 4 for gap in SOURCE_GAPS), "source alphabet exceeded four")

    source_clock = 0
    target_clock = 0
    consumed_maximum = 0
    source_odd = SOURCE_ODD
    rows = []

    for index, target_gap in enumerate(TARGET_GAPS, 1):
        source_gap = SOURCE_GAPS[index - 1] if index <= len(SOURCE_GAPS) else 2
        source_odd = odd_edge(source_odd, source_gap)
        source_clock += source_gap
        target_clock += target_gap
        consumed_maximum = max(consumed_maximum, source_gap)

        # A proposed child exponent f needs f >= e+A-B.
        required_exponent = SOURCE_EVEN_EXPONENT + source_clock - target_clock

        # The funded-prefix theorem permits f=e, or f<a for a consumed gap a.
        # Here the permitted exponents are exactly 0 through this maximum.
        funding_cap = max(SOURCE_EVEN_EXPONENT, consumed_maximum - 1)
        margin = required_exponent - funding_cap
        require(margin > 0, f"funded repayment unexpectedly exists at prefix {index}")
        require(
            target_clock < source_clock,
            f"proper-prefix clock domination failed at prefix {index}",
        )
        rows.append(
            {
                "prefix": index,
                "source_clock": source_clock,
                "target_clock": target_clock,
                "required_even_exponent": required_exponent,
                "largest_funded_exponent": funding_cap,
                "target_endpoint": target_values[index],
                "margin": margin,
            }
        )

    require(source_odd == 1, "padded source must have reached one")
    require(source_clock == 81, "unexpected padded source clock")
    require(rows[-1]["required_even_exponent"] == 14, "unexpected terminal deficit")
    require(rows[-1]["largest_funded_exponent"] == 3, "unexpected terminal funding cap")
    require(min(row["margin"] for row in rows) == 1, "unexpected minimal margin")

    # Every further odd step at either terminal one is exactly a gap-two loop.
    # The remaining deficit is therefore unchanged for every padding length:
    # e+(A+2)-(B+2) = e+A-B = 14, while the largest consumed gap remains four.
    require(odd_edge(1, 2) == 1, "terminal self-loop failed")
    deficit = SOURCE_EVEN_EXPONENT + source_clock - target_clock
    require(
        SOURCE_EVEN_EXPONENT + (source_clock + 2) - (target_clock + 2) == deficit,
        "terminal deficit is not invariant",
    )
    require(deficit > 3, "terminal loop would permit funding")

    # For a source padding length m, its word ends at odd-step index 3+m.
    # If 3+m <= 39, all eligible prefixes occur in the checked rows.
    # If 3+m > 39, every later prefix has invariant deficit 14 and cap 3.
    # These two cases cover all m >= 0; no padding bound is assumed.
    return {
        "status": "exact_obstruction_verified",
        "source": source,
        "odd_source": SOURCE_ODD,
        "source_gaps": list(SOURCE_GAPS),
        "target": TARGET,
        "target_odd_steps": len(TARGET_GAPS),
        "target_shortcut_clocks": sum(TARGET_GAPS),
        "target_gaps": list(TARGET_GAPS),
        "minimum_unfunded_margin": min(row["margin"] for row in rows),
        "terminal_required_even_exponent": deficit,
        "terminal_largest_funded_exponent": 3,
        "terminal_padding_lengths": "every nonnegative integer",
        "scope": "equal-odd-count clock-funded prefix repayment",
    }


if __name__ == "__main__":
    print(json.dumps(verify(), sort_keys=True))
