"""Independently replay the positive, finite parts of the pinned-target results."""
import json


def check(condition, message):
    if not condition:
        raise ValueError(message)


def step(n):
    return (3 * n + 1) // 2 if n % 2 else n // 2


def prefix(n, h):
    odds = 0
    for _ in range(h):
        odds += n % 2
        n = step(n)
    return n, odds


def first(n, target):
    seen = set()
    while n != target and n not in seen:
        seen.add(n)
        n = step(n)
    return len(seen) if n == target else None


def control():
    rows = []
    for r, h, y, p in [(99, 8, 11, 3), (237, 9, 38, 4)]:
        inputs = [r - 1, r + 1, 3 * r - 1, 3 * r + 1]
        paths = [prefix(n, h) for n in inputs]
        check(paths == [(y, p)] * 2 + [(y, p - 1)] * 2, (r, paths))
        for t in [1, 21, 331, 2**67 + 3]:
            X = r + (2**h) * t
            for n in [X - 1, X + 1, 3 * X - 1, 3 * X + 1]:
                check(prefix(n, h)[0] == y + (3**p) * t, (t, n))
        rows.append(dict(r=r, h=h, target=y, grades=[p, p, p - 1, p - 1]))
    gaps = []
    for a in range(1, 512, 2):
        pos = a
        for k in range(128):
            if pos % 256 == 99 or pos % 512 == 237:
                gaps.append(k)
                break
            pos = (pos * 3) % 512
        else:
            raise ValueError(('missing exponent', a))
    p, u = 113, step(3 * 113)
    dates = {f'{x}_to_{g}': first(x, g) for x, g in [(p, 1), (u, 1), (p, u),
              (u, p), (p, 5), (u, 5), (455907, p), (3 * 455907, u)]}
    check(dates['113_to_1'] == 10 and dates['509_to_1'] == 33, dates)
    check(dates['113_to_509'] is None and dates['509_to_113'] is None, dates)
    check(dates['455907_to_113'] is not None and dates['1367721_to_509'] is not None, dates)
    return dict(collar_rows=rows, odd_residues=len(gaps), largest_first_wheel_index=max(gaps),
                canonical_source=p, upper_head=u, ordinary_visits=dates)


if __name__ == '__main__':
    print(json.dumps(control(), indent=2, sort_keys=True))
