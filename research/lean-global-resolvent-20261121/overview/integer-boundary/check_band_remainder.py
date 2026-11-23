"""Exact finite controls for the parameterized band-remainder proof.

These executions do not prove convergence of the infinite family or Collatz.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def step(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def control(k: int) -> dict[str, int]:
    require(k >= 2, "k must be at least two")
    a, h = 3 * k, 2 * k + 1
    r, q = (1 << h) - 1, (1 << a) + (1 << h) - 1
    require(q.bit_length() - 1 == a, "wrong binary height")
    require((a + 1) * (q - (1 << a)) <= 4 * (1 << a), "band inequality")
    require(3 ** h > (1 << a) + (1 << h), "power comparison")
    x, y, odd = r, q, 0
    minimum = None
    for j in range(a + 1):
        require(y == x + (1 << (a - j)) * 3 ** odd, "lifting identity")
        if j:
            require(y > q, "descent before common horizon")
            minimum = y if minimum is None else min(minimum, y)
        if j == h:
            require(y == 3 ** h * ((1 << (k - 1)) + 1) - 1, "odd-run endpoint")
        if j < a:
            require(x % 2 == y % 2, "parity agreement")
            odd += x % 2
            x, y = step(x), step(y)
    require((x - y) % 2 == 1, "parity splits at horizon")
    return {"k": k, "a": a, "h": h, "q": q, "r": r,
            "q_at_a": y, "r_at_a": x, "odd_count": odd,
            "minimum_positive_clock_through_a": minimum}


def first_descent_and_hit(n: int, cap: int = 100000) -> tuple[int, int]:
    x, descent = n, None
    for j in range(1, cap + 1):
        x = step(x)
        if descent is None and x < n:
            descent = j
        if x == 1:
            require(descent is not None, "nontrivial source must descend before hitting one")
            return descent, j
    raise ValueError("finite convergence control exceeded its explicit cap")


def main() -> None:
    rows = [control(k) for k in range(2, 129)]
    convergence = []
    for row in rows[:8]:
        q_descent, q_hit = first_descent_and_hit(row["q"])
        r_descent, r_hit = first_descent_and_hit(row["r"])
        require(q_descent > row["a"], "family descent must outlast a")
        require(r_descent > row["a"], "remainder descent must outlast a")
        convergence.append({"k": row["k"], "q": row["q"], "r": row["r"],
                            "q_first_descent": q_descent, "q_first_hit_one": q_hit,
                            "r_first_descent": r_descent, "r_first_hit_one": r_hit})
    result = {
        "scope": "127 exact finite horizon controls, eight finite convergent pairs; not a global convergence proof",
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "all_horizon_controls_passed": len(rows),
        "max_k": rows[-1]["k"],
        "convergent_controls": convergence,
        "smallest_horizon_control": rows[0],
        "largest_horizon_control": rows[-1],
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
