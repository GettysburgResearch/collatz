"""Exact octave rounding maps. Every assertion also runs with python -O."""
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def level(m):
    return m & -m


def nodes(base, top):
    require(base > 0 and base % 2 == 1 and base <= top < 8 * base, "band")
    return [m for m in range(4 * base, 8 * base)
            if level(m) <= 4 and base <= m // level(m) <= top]


def edge(base, top, m, upward):
    y = 3 * m + level(m)
    b = 2 if y >= 16 * base else 1
    den = 1 << b
    w = (y + den - 1) // den if upward else y // den
    while w < 8 * base and (level(w) > 4 or not base <= w // level(w) <= top):
        w += 1 if upward else -1
    if w == 8 * base:
        return 4 * base, b + 1
    require(4 * base <= w < 8 * base, "octave")
    return w, b


def periodic(base, top, upward):
    seen = {}
    path = []
    m, clock = 4 * base, 0
    while m not in seen:
        seen[m] = (len(path), clock)
        path.append(m)
        m, b = edge(base, top, m, upward)
        clock += b
    begin, offset = seen[m]
    return clock - offset, path[begin:]


def orbit_check(base, top, full=False):
    result = {}
    for up, name in [(False, "lower"), (True, "upper")]:
        h, loop = periodic(base, top, up)
        result[name] = [h, len(loop), loop] if full else [h, len(loop)]
    return result


def actual_loop(base, top):
    allowed = nodes(base, top)
    allowed_set = set(allowed)
    for m in allowed:
        seen = set()
        while m in allowed_set:
            if m in seen:
                return True
            seen.add(m)
            a, b = edge(base, top, m, False)
            if 3 * m + level(m) != (1 << b) * a:
                break
            m = a
    return False


def check():
    control = {}
    for b in (1, 9, 11, 21):
        u = min((16 * b + 7) // 3, 8 * b - 1)
        control[str(b)] = orbit_check(b, u, full=True)
    wide = {}
    for b in (9, 11):
        entry = orbit_check(b, 8 * b - 1, full=True)
        require(entry["lower"][:2] == entry["upper"][:2] == [8, 5], "false lock")
        require(not actual_loop(b, 8 * b - 1), "no on-grid cycle")
        wide[str(b)] = entry
    require(control["1"]["lower"][:2] == control["1"]["upper"][:2] == [2, 1], "known cycle")
    # Increasing bands certify all odd minima 3..1,000,001 without tracing the forward basin of one.
    bands = []
    left = 3
    while left <= 1_000_001:
        right = min(1_000_001, left + 2 * (left // 10))
        while True:
            top = (16 * right + 7) // 3
            require(top < 8 * left, "monotone support")
            bounds = orbit_check(left, top)
            (h, p), (k, q) = bounds["lower"], bounds["upper"]
            if h * q < k * p:
                break
            require(right > left, "no separating interval at this anchor")
            right = left + 2 * ((right - left) // 4)
        bands.append([left, right, h, p, k, q])
        left = right + 2
    # Cross-check the edge routine by scanning the actual two adjacent dyadic levels.
    for b in range(1, 160, 2):
        t = min((16 * b + 7) // 3, 8 * b - 1)
        ns = nodes(b, t)
        lifted = sorted((v << j, v, j) for j in (1, 2, 3) for v in ns)
        for m in ns:
            y = 3 * m + level(m)
            lo = max(row for row in lifted if row[0] <= y)
            hi = min(row for row in lifted if row[0] >= y)
            require(lo[1:] == edge(b, t, m, False), "lower reference")
            require(hi[1:] == edge(b, t, m, True), "upper reference")
    return {"actual_ceiling": control, "wider_false_locks": wide, "intervals": len(bands),
            "first_interval": bands[0], "last_interval": bands[-1],
            "largest_certified_odd_minimum": bands[-1][1]}


if __name__ == "__main__":
    print(json.dumps(check(), indent=2))
