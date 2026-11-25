"""Independent finite controls for the octave certificate and physical scale changes."""

from math import comb


def check(condition, message):
    if not condition:
        raise ValueError(message)


def step(x):
    return (3*x+1)//2 if x % 2 else x//2


def run(t, x):
    for _ in range(t):
        x = step(x)
    return x


def children(q):
    pairs = []
    for e in range(1, 7):
        x, rem = divmod((q << e)-1, 3)
        if not rem and x % 2 and x % 3:
            pairs.append((e, x))
    check(len(pairs) == 2 and pairs[0][0] <= 4, "two-child budget")
    return pairs


def banks():
    total = 0
    for q in range(1, 48, 2):
        if q % 3 == 0:
            continue
        rows = [(q, 0, 0)]
        for k in range(8):
            for j in range(k+1):
                budget = 4*k+2*j
                X = ((1 << budget)*q + 3**k-1)//3**k
                lifted = set()
                for x, costly, clock in rows:
                    if costly > j:
                        continue
                    check(clock <= budget and 3**k*x <= (1 << budget)*q, "height")
                    z, shifts = x, 0
                    while z < X:
                        z *= 2
                        shifts += 1
                    check(z < 2*X and run(shifts+clock, z) == q, "ordinary endpoint")
                    lifted.add(z)
                expected = sum(comb(k, i) for i in range(j+1))
                check(len(lifted) == expected, "distinct representatives")
                total += expected
            rows = [(y, costly+index, clock+e) for x, costly, clock in rows
                    for index, (e, y) in enumerate(children(x))]
    return total


def hit_time(x, y, deadline):
    for t in range(deadline+1):
        if x == y:
            return t
        x = step(x)
    return None


def stage_controls():
    check([z for z in range(107, 214) if hit_time(z, 4, 75) is None] == [171],
          "one-hole certificate")
    stages = []
    for k in range(1, 5):
        j = k//2
        X = (1 << (4*k+2*j))*(k+1)//3**k+1
        quota = sum(comb(k, i) for i in range(j+1))
        times = [hit_time(z, 4, 300) for z in range(X, 2*X)]
        check(None not in times, "bounded replay deadline")
        times.sort()
        H = times[len(times)-quota]
        misses = sum(t > H for t in times)
        check(misses < quota <= sum(t >= H for t in times), "first passing time")
        stages.append((k, X, H, misses))
    check(stages == [(1, 11, 12, 0), (2, 342, 90, 0),
                     (3, 2428, 130, 3), (4, 64727, 210, 7)], "octave stages")
    return stages


def transport_controls():
    rays = 0
    for b in range(9):
        for d in range(4):
            for e in range(4):
                for m in range(1, 16):
                    x = (2**b*m-1) << d
                    y = (3**b*m-1) << e
                    check(run(b+d, x) == run(e, y), "affine rays")
                    rays += 1
    tiles = 0
    for h in (0, 4, 16, 32, 64):
        for n in range(1, 257):
            four = [run(h, 4*n+i) for i in range(4)]
            three = [run(h, 3*n+j) for j in range(3)]
            if len(set(four)) == len(set(three)) == 1:
                check(run(2, four[0]) == three[0], "twelve physical comparisons")
                tiles += 1
    check(tiles > 0, "positive fusion control")
    return rays, tiles


if __name__ == "__main__":
    print("Distinct octave representatives checked", banks())
    print("Stages (k, X, H, misses)", stage_controls())
    print("Affine rays and fused block pairs", transport_controls())
