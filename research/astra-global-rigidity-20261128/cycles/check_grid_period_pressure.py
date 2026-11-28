"""Exact finite controls for GRID_PERIOD_PRESSURE, with no floating evaluations."""

from collections import deque


def require(condition, detail):
    if not condition:
        raise ValueError(detail)


def grid_step(k, x):
    # Choose the local pre-rounding octave, then handle its upper endpoint.
    winding = 1 if 3 * x < 4 * k else 2
    scale = 1 << winding
    target = (3 * x + scale - 1) // scale
    digit = scale * target - 3 * x
    if target == 2 * k:
        target //= 2
        winding += 1
    require(k <= target < 2 * k, (k, x, target))
    require(0 <= digit < 1 << winding, (k, x, winding, digit))
    return target, winding, digit


def periodic_pool(k, edges):
    incoming = {x: 0 for x in range(k, 2 * k)}
    for neighbor, _, _ in edges.values():
        incoming[neighbor] += 1
    queue = deque(x for x in incoming if incoming[x] == 0)
    while queue:
        source = queue.popleft()
        target = edges[source][0]
        incoming[target] -= 1
        if incoming[target] == 0:
            queue.append(target)
    return sorted(x for x in incoming if incoming[x] > 0)


def inspect_grid(k):
    edges = {x: grid_step(k, x) for x in range(k, 2 * k)}
    pool = periodic_pool(k, edges)
    ranks = {x: rank for rank, x in enumerate(pool)}
    count = len(pool)
    shift = sum(edges[x][1] for x in pool)
    n, power = 0, 1
    while power < 2 * k:
        power *= 3
        n += 1
    observed = set()
    calendars = set()
    bins = 5
    for start_rank, x in enumerate(pool):
        target = x
        calendar = []
        digit_word = []
        accumulated = 0
        for step in range(n):
            rank = ranks[target]
            neighbor, winding, digit = edges[target]
            expected_winding, next_rank = divmod(rank + shift, count)
            require((winding, ranks[neighbor]) == (expected_winding, next_rank),
                    (k, x, step, "rank"))
            calendar.append((bins * rank // count, winding))
            digit_word.append(digit)
            target = neighbor
            accumulated += winding
        require(accumulated == (start_rank + n * shift) // count,
                (k, x, "winding sum"))
        require(1 << accumulated >= k, (k, x, "residue horizon"))
        label = (tuple(calendar), tuple(digit_word))
        require(label not in observed, (k, x, "word collision"))
        observed.add(label)
        calendars.add(label[0])
    require(len(calendars) <= (bins + 2) * n, (k, "calendar count"))
    return count


def check_geometric_pressure_products():
    # Finite exact geometric-series identity on rational rotations.  For clock
    # a/q, 2^q plays the role of grid dilation and 2^a that of raw tripling.
    checked = 0
    for q in range(1, 6):
        for a in range(q + 1, 2 * q + 1):
            raw = 1 << a
            dyadic_product = 1
            constant_product = 1
            for i in range(q):
                winding, next_rank = divmod(i + a, q)
                weight = 1 << (q - i)
                next_weight = 1 << (q - next_rank)
                alphabet = 1 << (q * winding)
                require(alphabet * weight == raw * next_weight, (a, q, i))
                denominator = (1 << weight) - 1
                dyadic_product *= ((1 << (alphabet * weight)) - 1) // denominator
                constant_product *= ((1 << (raw * weight)) - 1) // denominator
            require(dyadic_product == constant_product, (a, q, "pressure"))
            checked += 1
    return checked


if __name__ == "__main__":
    total = sum(inspect_grid(k) for k in range(2, 513))
    print("511 integer grids;", total, "pooled periodic representatives;",
          check_geometric_pressure_products(), "exact geometric products")
