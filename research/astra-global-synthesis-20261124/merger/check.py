"""Exact finite checks accompanying the paired-tail proof. Stdlib only."""
from fractions import Fraction
from itertools import product


def require(test, label):
    if not test:
        raise ArithmeticError(label)


def step(n):
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def run(n, k):
    for _ in range(k):
        n = step(n)
    return n


def boundaries(word):
    total, odds, carry = 0, 0, 0
    for paid in word:
        carry = 9 * carry + (5 if paid else 7) * 2**total
        odds += 2
        total += 5 if paid else 3
    modulus = 2 ** (total + 1)
    source = ((2**total - carry) * pow(3**odds, -1, modulus)) % modulus
    return source, modulus


OFFSET = (1381, 1381, 2405, 3557, 4853, 5287, 1639)
CARRY = (5, 7, 7, 7, 5, 5, 11)
NEXT = ((0, 1), (2,), (3,), (4,), (5,), (6,), (0, 1))


def paired_controls():
    walks = [(j,) for j in range(7)]
    for _ in range(10):
        walks = [walk + (j,) for walk in walks for j in NEXT[walk[-1]]]
    edges = 0
    for walk in walks:
        full = list(walk)
        for _ in range(4):
            full.append(NEXT[full[-1]][0])
        source, modulus = boundaries([s >= 5 for s in full])
        for q in (source, source + modulus):
            for s, t in zip(walk, walk[1:]):
                a = 5 if s >= 5 else 3
                qp = run(q, a)
                require((1 << a)*qp == 9*q + (5 if s >= 5 else 7), "input")
                num = 3123*q + OFFSET[s]
                y, rem = divmod(num, 4096)
                yp = run(y, a)
                require(rem == 0 and y % 2 == 1, "integrality")
                require(4096*yp == 3123*qp + OFFSET[t], "real shadow")
                require((1 << a)*yp == 9*y + CARRY[s], "carry")
                if s <= 1:
                    m = (8*y - 5)//9
                    require(run(m, 3) == y, "two inverse odds")
                elif s <= 4:
                    m = (2*y - 1)//3
                    require(step(m) == y, "one inverse odd")
                else:
                    m = y
                mid = (3*q+1)//(2 if s >= 5 else 4)
                require(m % 2 == 1 and 0 < m < min(q, mid), "floor")
                q = qp
                edges += 1
    return len(walks), edges


def reset_controls():
    n = 0
    for r, s in product((2,3,4,7,18,39), (2,3,4,9,21,52)):
        word = [False]*r + [True]*2 + [False]*s
        q, mod = boundaries(word)
        for x in (q, q+mod):
            m = (x+7)//16-7
            z = run(x, 3*r+10+3*s)
            require(run(m, 3*r+7+3*s) == (z-7)//2, "reset")
            require(0 < m < min(x,(3*x+1)//4), "reset floor")
            n += 1
    return n


def small_glue():
    results = []
    for d in (1,3,6):
        for n in range(1, 2**d, 2):
            slope = Fraction(n, 2**d)
            lists = []
            for m, H in ((1,1),(2,41)):
                seeds = set()
                for a in (5,7):
                    sign = 1 if a == 5 else -1
                    for mask in range(4):
                        E = sum(sign*Fraction(9,8)**j/4 for j in range(2)
                                if (mask >> j) & 1)
                        z = -a + E - slope*166*H/9**m
                        if z.numerator % 2 and z.denominator % 2:
                            seeds.add(z)
                lists.append(sorted(seeds))
            if all(lists):
                results.append((slope, *lists))
    require(results == [
        (Fraction(3,8), [Fraction(-35,3)], [Fraction(-979,27)]),
        (Fraction(5,8), [Fraction(-169,9)], [Fraction(-4841,81)])],
        "small candidates")
    return len(results)


if __name__ == "__main__":
    walks, edges = paired_controls()
    print(f"paired phase paths {walks}; literal edges {edges}")
    print(f"finite asynchronous resets {reset_controls()}")
    print(f"surviving small common odd seeds {small_glue()}")
