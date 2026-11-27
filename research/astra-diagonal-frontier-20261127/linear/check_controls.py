"""Exact independent controls for the binary span and prescribed predecessor results."""

from collections import deque
from itertools import product


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def step(n):
    return (3 * n + 1) // 2 if n % 2 else n // 2


def run(n, clocks):
    odds = 0
    for _ in range(clocks):
        odds += n % 2
        n = step(n)
    return n, odds


def gf_apply(rows, vector):
    return sum(((row & vector).bit_count() % 2) << i for i, row in enumerate(rows))


def vector_value(initial, maps, n):
    state = initial
    for bit in bin(n)[3:]:
        state = gf_apply(maps[int(bit)], state)
    return state


def insert_basis(pivots, vector):
    while vector:
        leading = vector.bit_length() - 1
        if leading not in pivots:
            pivots[leading] = vector
            return True
        vector ^= pivots[leading]
    return False


def span_and_direct(maps, initial, label, floor):
    d = len(maps[0])
    ceiling = floor << (4 * d)
    values = [0] * (3 * ceiling)
    values[1] = initial
    for n in range(2, len(values)):
        values[n] = gf_apply(maps[n % 2], values[n // 2])

    def probes(n):
        return ((label & (values[2 * n] ^ values[n])).bit_count() % 2,
                (label & (values[2 * n + 1] ^ values[3 * n + 2])).bit_count() % 2)

    direct = any(any(probes(n)) for n in range(floor, ceiling))
    queue = deque(range(floor, 2 * floor))
    pivots = {}
    processed = 0
    witness = None
    while queue:
        n = queue.popleft()
        vs = [vector_value(initial, maps, j) for j in (n, 3*n, 3*n+1, 3*n+2)]
        packed = sum(value << (i*d) for i, value in enumerate(vs))
        processed += 1
        if not insert_basis(pivots, packed):
            continue
        if witness is None and any(probes(n)):
            witness = n
        queue.extend((2*n, 2*n+1))
    require(processed <= floor + 8*d, "too many vector candidates")
    require((witness is not None) == direct, "basis and directly enumerated band differ")
    return direct, len(pivots)


def check_vectors():
    cases = detected = 0
    rank_max = 0
    # All dimensions one and two, with every ordered matrix pair in dimension two.
    for dimension in (1, 2):
        end = 1 << dimension
        matrices = list(product(range(end), repeat=dimension))
        for a, b in product(matrices, repeat=2):
            for floor in (1, 3):
                initial = end-1
                label = 1
                defect, rank = span_and_direct((a, b), initial, label, floor)
                cases += 1
                detected += int(defect)
                rank_max = max(rank_max, rank)
    return cases, detected, rank_max


def build_preimage(k, r, y, d, H):
    """d initial extra odds followed by one movable odd."""
    t, q = run(r, k)
    A = 3 * (3**d - 2**d)
    mod = 3**(q+d+1)
    period = 2 * (mod//3)
    relevant = ((1 << H)*y - A - 3**(d+1)*t) % mod
    residues = {(pow(2, j, mod)): j for j in range(d, d+period)}
    j = residues[relevant]
    numerator = (1 << H)*y - A - (1 << j)
    require(numerator % 3**(d+1) == 0, "failed to clear reverse word")
    z = numerator // 3**(d+1)
    require(z >= t and (z-t) % 3**q == 0, "integer not in the terminal head")
    x = r + (1 << k) * ((z-t)//3**q)
    require(x > 0 and x % (1 << k) == r, "invalid starting integer")
    require(run(x, k+H) == (y, q+d+1), "physical endpoint or odd count differs")
    require(run(x, k)[0] == z, "prescribed native prefix was not realized")
    bits = []
    v = z
    for _ in range(H):
        bits.append(v % 2)
        v = step(v)
    require([i for i, bit in enumerate(bits) if bit] == list(range(d)) + [j],
            "the actual odd positions differ")
    return x


def check_lifts():
    cases = 0
    for k in range(6):
        for r in range(1 << k):
            t, q = run(r, k)
            for d in range(3):
                period = 2 * 3**(q+d)
                H = d + period + 3
                for clock in (H, H+1):
                    for y in (1, 2, 5, 7, 10, 17):
                        build_preimage(k, r, y, d, clock)
                        cases += 1
    # Show necessity of positive cofactor / endpoint-unit guard. No word with
    # an odd branch ends at a multiple of three.
    require(all(run(n, 8)[0] % 3 != 0 for n in range(1, 513) if run(n, 8)[1]),
            "invalid multiple-of-three control")
    # A smaller actual visitor need not exist. No source among 1..6 ever hits 7.
    for n in range(1, 7):
        visited = set()
        while n not in visited:
            require(n != 7, "unexpected preimage of 7 below 7")
            visited.add(n)
            n = step(n)
    return cases


if __name__ == "__main__":
    print("linear models, defects, maximum observed rank:", *check_vectors())
    print("physical lifts:", check_lifts())
