"""Verify forward closure, its inverse algorithm, and stopped paths on finite inputs."""
from functools import lru_cache
import json


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def true(n):
    return (3 * n + 1) // 2 if n % 2 else n // 2


def rounded(n):
    require(n % 2 == 1, "positive odd input required")
    y = true(n)
    return y + (y % 2 == 0)


def previous(y):
    parents = []
    if y % 2:
        for offset in (1, 3):
            n, remainder = divmod(2 * y - offset, 3)
            if remainder == 0 and n > 0 and n % 2 and rounded(n) == y:
                parents.append(n)
    require(len(parents) <= 1, "odd rounding was not injective")
    return next(iter(parents), None)


def run(cutoff, limit):
    # Physical ternary residues of three positive odd gaps of total four.
    legal = {sum(3**i * pow(2, -s, 27) for i, s in enumerate(partials)) % 27
             for partials in ((1, 2, 4), (1, 3, 4), (2, 3, 4))}

    def seed(y):
        return y > cutoff and y % 2 and y % 27 in legal

    def in_closure(y):
        while y is not None:
            if seed(y):
                return True
            y = previous(y)
        return False

    explicit = set()
    for n in range(1, limit + 1):
        if seed(n):
            y = n
            depth = 0
            while y <= limit:
                explicit.add(y)
                require((3**depth) * n <= (2**depth) * y <= (3**depth) * (n + 3),
                        ("geometric tail", n, depth))
                require(previous(rounded(y)) == y, ("true smaller inverse", y))
                y = rounded(y)
                depth += 1
    for n in range(1, limit + 1):
        require(in_closure(n) == (n in explicit), ("forward/reverse closure", n))
        if n in explicit:
            require(n > cutoff and n % 2 and 0 <= rounded(n) - true(n) <= 1,
                    ("edge budget or cutoff", n))

    changed = sum(rounded(n) != true(n) for n in explicit)
    discrepancies = captures = early = 0
    for n in range(1, 8001):
        state = n
        original = [n]
        while state != 1:
            state = true(state)
            original.append(state)
        hit = next((i for i, y in enumerate(original) if in_closure(y)), None)
        state = n
        modified = [n]
        for _ in range(len(original)):
            if in_closure(state) or state == 1:
                break
            state = true(state)
            modified.append(state)
        if hit is None:
            require(tuple(modified) == tuple(original), ("uncaptured", n))
            continue
        captures += 1
        require(original[:hit + 1] == modified, ("first physical entrance", n))
        require(in_closure(state) and rounded(state) > state, ("absorbing", n))
        minimum = min(modified)
        t_new = modified.index(minimum)
        t_old = len(original) - 1
        discrepancies += t_new != t_old
        for k in (2, 3, 4):
            if hit <= k and len(original) > 16 * k and (original[16 * k] << k) < n:
                require(t_new <= k < t_old, ("later real witness", n, k))
                early += 1
    return dict(cutoff=cutoff, seeds=sum(bool(seed(n)) for n in range(1, limit + 1)),
                in_closure=len(explicit), changed=changed, starts=8000,
                captured=captures, different_stopped_paths=discrepancies,
                later_smaller_witnesses=early)


if __name__ == "__main__":
    print(json.dumps({"finite_fixed_grade_fixture": [run(cutoff, 30000)
                                                    for cutoff in (2, 100, 1000)]},
                     sort_keys=True, indent=2))
