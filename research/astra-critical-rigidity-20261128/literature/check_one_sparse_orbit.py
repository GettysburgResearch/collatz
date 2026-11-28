"""Check actual stopped paths, trapped rays, edge sizes and the unit change law."""
import hashlib
import json
from collections import Counter
from functools import lru_cache


def require(condition, context):
    if not condition:
        raise ArithmeticError(context)


def step(n):
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def oddpart(n):
    return n // (n & -n)


def next_multiple(s):
    k, remainder = divmod(s - 3, 6)
    require(remainder == 0 and s >= 9, ("spine input", s))
    return 6 * ((3 * k + 1) // 2) + 3


@lru_cache(None)
def true_path(n):
    if n == 1:
        return (1,)
    return (n,) + true_path(step(n))


def scenario(anchor, limit):
    first = 9 if anchor == 1 else step(anchor) + 1
    high = set()
    if anchor == 1:
        high.add(3)
    s = first
    largest = max(max(true_path(n)) for n in range(1, limit + 1))
    while s <= max(largest, limit) * 2:
        high.add(s)
        following = next_multiple(s)
        require(following % 6 == 3 and 3 * following >= 4 * s, "strict growth")
        require(following - step(s) in (-2, 1), ("edge size", s))
        s = following

    def modified(n):
        if n == anchor:
            return 3 if anchor == 1 else first
        if n == 3 and anchor == 1:
            return 9
        if n in high:
            return next_multiple(n)
        return step(n)

    counts = Counter()
    digest = hashlib.sha256()
    for n in range(1, limit + 1):
        orig = true_path(n)
        on_ray = oddpart(n) in high
        require(any(y in high for y in orig) == on_ray, "true ternary preimages")
        eligible = anchor in orig
        landing = None
        path = []
        state = n
        for j in range(len(orig) + 1):
            path.append(state)
            if state in high or state == anchor:
                landing = j
                break
            if state == 1:
                break
            state = modified(state)
        require((landing is not None) == (on_ray or eligible), "component membership")
        if landing is not None:
            require(modified(path[-1]) > path[-1], "directed escape")
            minimum = min(path)
            stopped = tuple(path[:path.index(minimum) + 1])
        else:
            stopped = tuple(path)
        require(stopped == orig[:len(stopped)], "shared finite history")
        if not on_ray and anchor == 1:
            require(stopped == orig, "exact minimum-path coupling")
        if not on_ray and anchor > 1 and eligible:
            r = stopped[-1]
            require(r > 1 and len(orig) - len(stopped) ==
                    true_path(r).index(anchor) + len(true_path(anchor)) - 1,
                    ("bounded clock gap", n, anchor))
        if not on_ray and not eligible:
            require(stopped == orig, "unchanged remaining basin")
        if stopped != orig:
            counts["different_stopped_paths"] += 1
        counts["true_predecessors"] += int(eligible)
        counts["initial_dyadic_ray"] += int(on_ray)
        counts["modified_captured"] += int(landing is not None)
        counts["complete_sources"] += 1
        digest.update(f"{n} {eligible} {on_ray} {len(stopped)} {stopped[-1]}\n".encode())
    for n in range(1, 2 * limit + 1):
        require(abs(modified(n) - step(n)) <= (4 if anchor == 1 else 2), "global bound")
        require(n % 2 or modified(n) == n // 2, "exact even edges")
    return {"anchor": anchor, "counts": dict(counts), "trace_sha256": digest.hexdigest()}


def run():
    limit = 16384
    checked = 0
    for n in range(1, 32769):
        choices = [z for z in range(step(3 * n) - 1, step(3 * n) + 2) if z % 3 == 0]
        if n % 2:
            require(choices == [3 * step(n)], "unique odd unit-perturbation lift")
        else:
            require(step(3 * n) == 3 * step(n), "even conjugacy")
        checked += 1
    return {"scope": "Exact finite ordinary paths certified through 1, modifications up to the first growing spine, all one-unit ternary candidates at 32768 inputs. No limiting density or divergent original orbit is inferred.",
            "sources_per_scenario": limit, "unit_comparisons": checked,
            "scenarios": [scenario(a, limit) for a in (1, 5, 85, 341)]}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
