"""Finite arithmetic checks for the ordinary critical-count and partition notes."""

from __future__ import annotations

from collections import Counter
from math import log, sqrt


def check(condition: bool, detail: str) -> None:
    if not condition:
        raise ValueError(detail)


def step(n: int) -> int:
    return (3 * n + 1) // 2 if n % 2 else n // 2


def count_at(n: int, horizon: int) -> tuple[int, int]:
    count = 0
    for _ in range(horizon):
        count += n % 2
        n = step(n)
    return n, count


def until_one(n: int) -> tuple[int, int]:
    count = 0
    clock = 0
    seen = set()
    while n != 1:
        check(n not in seen, "finite test encountered another cycle")
        seen.add(n)
        count += n % 2
        n = step(n)
        clock += 1
    return clock, count


def first_cap_label(n: int, prefix: int, cap: int) -> tuple[str, int]:
    minimum = n
    state = n
    for _ in range(prefix):
        state = step(state)
        minimum = min(minimum, state)
    if minimum > cap:
        return "unresolved", n
    visited = {}
    state = minimum
    while state <= cap and state not in visited:
        visited[state] = len(visited)
        state = step(state)
    if state > cap:
        return "exit", state
    cycle_start = visited[state]
    return "cycle", min(x for x, i in visited.items() if i >= cycle_start)


def check_critical(limit: int) -> tuple[float, float, float]:
    natural_log = log(limit)
    critical = 2 * natural_log / log(4 / 3)
    horizons = [round(critical + z * sqrt(natural_log)) for z in (-2, 0, 2)]
    psi_sums = [0.0] * len(horizons)
    for n in range(1, limit + 1):
        hit, odd_at_hit = until_one(n)
        for i, horizon in enumerate(horizons):
            terminal, odd = count_at(n, horizon)
            if horizon >= hit:
                tail = horizon - hit
                check(2 * (odd - odd_at_hit) - tail == tail % 2, "posthit score mismatch")
                check(terminal == (2 if tail % 2 else 1), "cycle phase mismatch")
            else:
                arrival, remaining_odd = count_at(terminal, hit - horizon)
                check(arrival == 1 and odd + remaining_odd == odd_at_hit, "prehit count mismatch")
            score = (odd - horizon / 2) / sqrt(natural_log)
            psi_sums[i] += score / (1 + abs(score))
    return tuple(value / limit for value in psi_sums)


def check_partitions(limit: int) -> None:
    for prefix, cap in [(0, 4), (4, 10), (12, 50), (436 * limit.bit_length(), 2)]:
        labels = Counter(first_cap_label(n, prefix, cap) for n in range(1, limit + 1))
        check(sum(labels.values()) == limit, "partition lost a source")
        largest = max(labels.values())
        check(
            limit**2 - sum(size**2 for size in labels.values()) <= 2 * limit * (limit - largest),
            "partition collision bound failed",
        )
        counts = Counter()
        for (kind, _), size in labels.items():
            counts[kind] += size
        print(f"prefix={prefix:d} cap={cap:d} labeled sources={dict(sorted(counts.items()))}")
        if prefix == 436 * limit.bit_length():
            check(labels == {("cycle", 1): limit}, "full finite classifier missed the observed cycle")


if __name__ == "__main__":
    check_partitions(1024)
    for limit in [256, 4096, 16384]:
        values = check_critical(limit)
        print(f"X={limit:d} diagnostic mean bounded score z=(-2,0,2)={tuple(round(t, 6) for t in values)}")
