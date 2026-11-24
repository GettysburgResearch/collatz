"""Independent ordinary lifts and literal target words for the mixed controller."""
from check import boundaries, require, step

# free, tile opening, two L left, one before singleton, one before pair,
# first of pair, final P (including a singleton).
NEXT = ((0, 1), (2,), (3, 4), (6,), (5,), (6,), (0, 1))
NUMERATOR = ((183, 1), (183, 1), (549, 131), (549, -13),
             (549, -13), (549, -175), (183, -37))
TARGET = ("110", "111", "011", "001", "011", "10000", "11000")


def trace(x, clocks):
    out = []
    for _ in range(clocks):
        out.append(str(x % 2))
        x = step(x)
    return x, "".join(out)


def shadow(q, phase):
    a, b = NUMERATOR[phase]
    y, rem = divmod(a*q+b, 256)
    require(rem == 0 and y > 2, "ordinary shadow")
    return y


def mark(bits):
    a, b, c, d = bits
    if a:
        return 5 if b else 6
    if b:
        return 4 if c else 3
    if c:
        return 2
    return 1 if d else 0


def run():
    paths = [(s,) for s in range(7)]
    for _ in range(11):
        paths = [w+(t,) for w in paths for t in NEXT[w[-1]]]
    edges = floors = strict_mixtures = 0
    for path in paths:
        full = list(path)
        for _ in range(5):
            full.append(NEXT[full[-1]][0])
        bits = [s >= 5 for s in full]
        for j, s in enumerate(path):
            require(mark(bits[j:j+4]) == s, "raw marking")
        if 4 in path and 3 in path:
            strict_mixtures += 1
        q0, modulus = boundaries(bits)
        for q in (q0, q0+modulus):
            qs = [q]
            for p in bits:
                r, word = trace(q, 5 if p else 3)
                require(word == ("11000" if p else "101"), "literal input")
                qs.append(r)
                q = r
            for j, (s,t) in enumerate(zip(path, path[1:])):
                q, r = qs[j:j+2]
                y = shadow(q,s)
                yp, word = trace(y, len(TARGET[s]))
                require(word == TARGET[s] and yp == shadow(r,t), "literal comparison")
                if s <= 1:
                    m = y
                else:
                    p = j
                    while not bits[p]:
                        p += 1
                    m = qs[p+1]
                mid = (3*q+1)//(2 if bits[j] else 4)
                require(m % 2 == 1 and 0 < m < min(q,mid), "both ordinary floors")
                edges += 1
                floors += 1
    require(strict_mixtures > 0, "both package types")
    print(f"{len(paths)} phase paths, {strict_mixtures} with both singleton and pair")
    print(f"{edges} literal mixed shadow edges, {floors} simultaneous floor comparisons")


if __name__ == "__main__":
    run()
