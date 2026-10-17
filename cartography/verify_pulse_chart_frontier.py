#!/usr/bin/env python3
"""Independent checks for the frozen pulse-chart frontier artifact.

The verifier independently exhausts depths through 20 using the direct affine
word formula, verifies every frozen minimizing word by physical chart replay,
and checks the depth-max physical Collatz block replay.  It does not independently
repeat the full 2^31 search, so the depth-31 minimum remains an exact source
computation rather than an independently reproduced result.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path


def step(x: int) -> tuple[int, int] | None:
    if x % 8 == 0:
        return 9 * x // 8, 0
    if x % 16 == 7:
        return (9 * x + 1) // 16, 1
    return None


def v2(n: int) -> int:
    return (n & -n).bit_length() - 1


def accelerated(n: int) -> tuple[int, int]:
    y = 3 * n + 1
    a = v2(y)
    return y >> a, a


def independent_frontier(max_depth: int) -> list[tuple[int, str, int] | None]:
    """Enumerate one lift residue for every binary prefix through max_depth."""
    best: list[tuple[int, str, int] | None] = [None] * (max_depth + 1)

    def visit(depth: int, residue: int, exponent: int, current: int,
              pow9: int, bits: str) -> None:
        if depth:
            least = residue if residue else 1 << exponent
            row = (least, bits, exponent)
            if best[depth] is None or least < best[depth][0]:
                best[depth] = row
        if depth == max_depth:
            return
        for epsilon in (0, 1):
            digit_bits = 3 + epsilon
            modulus = 1 << digit_bits
            coefficient = (pow9 * 9) % modulus
            rhs = (9 * current + epsilon) % modulus
            q0 = (-rhs * pow(coefficient, -1, modulus)) % modulus
            visit(
                depth + 1,
                residue + (q0 << exponent),
                exponent + digit_bits,
                (9 * (current + pow9 * q0) + epsilon) >> digit_bits,
                pow9 * 9,
                bits + str(epsilon),
            )

    visit(0, 0, 0, 0, 1, "")
    return best


def verify_row(row: dict[str, object]) -> tuple[int, str]:
    x = int(str(row["least_x"]))
    bits = str(row["word_bits"])
    depth = int(row["depth"])
    assert len(bits) == depth
    actual = []
    for expected_char in bits:
        out = step(x)
        assert out is not None
        x, epsilon = out
        actual.append(str(epsilon))
        assert str(epsilon) == expected_char
    return x, "".join(actual)


def main() -> None:
    path = Path(sys.argv[1] if len(sys.argv) > 1 else "pulse-chart-frontier.json")
    data = json.loads(path.read_text())
    assert data["schema"] == "collatz.cartography.pulse-chart-frontier.v1"
    rows = data["rows"]
    assert len(rows) == int(data["max_depth"])

    previous = 0
    for row in rows:
        least = int(row["least_x"])
        assert least >= previous
        previous = least
        verify_row(row)

    # Independently written exhaustive implementation at the affordable control range.
    control = independent_frontier(20)
    for depth in range(1, 21):
        assert control[depth] is not None
        least, bits, E = control[depth]
        row = rows[depth - 1]
        assert int(row["least_x"]) == least
        assert row["word_bits"] == bits
        assert int(row["modulus_bits"]) == E

    last = rows[-1]
    x0 = int(last["least_x"])
    x = x0
    symbols = []
    for _ in range(int(data["least_x_exact_survival_depth"])):
        out = step(x)
        assert out is not None
        x, epsilon = out
        symbols.append(epsilon)
    assert step(x) is None
    assert str(x) == data["first_illegal_x"]
    assert 42 * x0 - 5 == int(data["depth_max_physical_n"])

    # Physical replay for the full exact survival prefix.
    n = 42 * x0 - 5
    x = x0
    for epsilon in symbols:
        expected_vals = (1, 2) if epsilon == 0 else (2, 2)
        for expected in expected_vals:
            n, actual = accelerated(n)
            assert actual == expected
        out = step(x)
        assert out is not None
        x, _ = out
        assert n == 42 * x - 5

    print(
        json.dumps(
            {
                "status": "PASS",
                "independent_exhaustive_depth": 20,
                "frozen_max_depth": data["max_depth"],
                "depth_max_least_x": data["depth_max_least_x"],
                "depth_max_physical_n": data["depth_max_physical_n"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
