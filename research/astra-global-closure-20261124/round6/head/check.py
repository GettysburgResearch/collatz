"""Check actual clocks, the least-rank exchanges, and bounded cut examples."""

import json
from collections import deque


def require(test, label):
    if not test:
        raise ValueError(label)


def step(n):
    return (3*n + 1)//2 if n % 2 else n//2


def at(n, depth):
    for _ in range(depth):
        n = step(n)
    return n


def trace(n, cap=100000):
    out = [n]
    while out[-1] != 1:
        require(len(out) < cap, "ordinary trace cap")
        out.append(step(out[-1]))
    return out


def split(n, p):
    count = 0
    while n % p == 0:
        count += 1
        n //= p
    return count, n


def finite_cut(start, target, peak, ceiling):
    """Exhaust the cutoff graph minus its certified separating vertex."""
    live = deque([start])
    seen = {start}
    while live:
        x = live.popleft()
        candidates = [step(x), 2*x]
        if x % 3 == 2:
            candidates.append((2*x - 1)//3)
        for y in candidates:
            if 1 <= y <= ceiling and y != peak and y not in seen:
                live.append(y)
                seen.add(y)
    require(target not in seen, "path in cutoff graph avoided the peak")
    return len(seen)


def main():
    odd = even = cone = 0
    for k in range(2**15):
        v = 9*k+2
        orig, child = 4*v, 8*v+1
        require(at(orig, 2) == v and at(child, 3) == 9*v+2, "original endpoints")
        h, b = split((4*v+1)//9, 3)
        r = 2**h*b
        require(r % 3 and b % 2, "rank units")
        require(at(9*r-1, h) == orig, "forward normalized antecedent")
        require(at(8*r-1, h+2) == child, "forward normalized child")
        if v % 2:
            m, a = split(3*v+1, 2)
            z = 3**(m+1)*a-1
            odd += 1
        else:
            m, a = split(v, 2)
            z = 9*3**(m//2)*a + (1 if m%2 else 2)
            even += 1
            cone += 22*z < r
        require(at(v, m) == a and at(9*v+2, m) == z, "physical run alignment")

    large_even = []
    for a in (1, 5, 7, 11):
        residue = next(m for m in range(1, 7) if (2**m*a) % 9 == 2)
        for shift in (60, 120, 240):
            m = residue+shift
            v = 2**m*a
            h, b = split((4*v+1)//9, 3)
            r = 2**h*b
            z = at(9*v+2, m)
            require(z == 9*3**(m//2)*a + (1 if m%2 else 2), "even tail")
            require(22*z < r, "large even representative")
            large_even.append({"a": a, "m": m, "h": h})
    # The first 3-adic rescuing cylinder is beyond most of the native census.
    power = 3**15
    c = pow(16, -1, power)
    rescues = []
    for r in (c, c+2*power, c+4*power):
        q = (16*r-1)//power
        w = 2**15*q-1
        require(16*r == power*q+1 and 22*w < r, "rank rescue")
        require(at(w, 15) == 2*(8*r-1), "inverse path")
        rescues.append({"r": r, "representative": w})

    examples = []
    for m in (4, 8, 16, 24, 40, 80, 160):
        u = 7*pow(pow(2, m, 27), -1, 27) % 27
        a = u if u % 2 else u+27
        for _ in range(2000):
            v = (2**m*a-1)//3
            orig, child = 4*v, 8*v+1
            left, right = trace(orig), trace(child)
            z = 3**(m+1)*a-1
            if max(left) == orig:
                break
            a += 54
        else:
            raise ValueError("example search cap")
        require(v % 9 == 2 and left[-1] == right[-1] == 1, "ordinary convergence")
        require(right[m+3] == z and z*2**m > 3**m*child, "forced peak")
        require(set(left).isdisjoint(right[:m+4]), "premature meeting")
        record = {"m": m, "a": a, "k": (v-2)//9, "peak": str(z),
                  "left_clock": len(left)-1, "right_clock": len(right)-1}
        if m == 4:
            record["cutoff"] = 4*z
            record["visited_without_peak"] = finite_cut(child, orig, z, 4*z)
        examples.append(record)
    print(json.dumps({"status": "PASS", "parameters": odd+even, "odd": odd,
                      "even": even, "even_below_rank_cutoff": cone,
                      "ternary_rescues": rescues, "large_even_lifts": large_even,
                      "convergent_pairs": examples},
                     indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
