# L-9701 verification: exact-arithmetic checks of parts (3) and (4)
# on finite truncations, plus a 3n-1 control. Standard library only, deterministic.
import random
from fractions import Fraction

def T(m):  # shortcut Collatz on N_0
    return m // 2 if m % 2 == 0 else (3 * m + 1) // 2

def U(m):  # 3n-1 shortcut control on positive integers
    return m // 2 if m % 2 == 0 else (3 * m - 1) // 2

def check(map_fn, domain_start, N, two_fiber_residue, tag):
    # Columns n in [domain_start, N); rows m in [domain_start, 2N).
    # Truncation lemma: every m with map_fn(m) < N satisfies m < 2N
    # (even m: m/2 < N iff m < 2N; odd m: map_fn(m) >= m), so the truncated
    # matrix represents F exactly on span{e_n : n < N}.
    rows = list(range(domain_start, 2 * N))
    cols = list(range(domain_start, N))
    for m in range(2 * N, 4 * N):           # spot-check the truncation lemma
        assert map_fn(m) >= N, (tag, m)
    fib = {n: 0 for n in cols}              # fiber counts #map^{-1}(n)
    for m in rows:
        t = map_fn(m)
        if t in fib:
            fib[t] += 1
    for n in cols:                          # Part 0a / Part 3 column norms
        pred = 2 if n % 3 == two_fiber_residue else 1
        assert fib[n] == pred, (tag, n, fib[n], pred)
    assert max(fib.values()) == 2 and min(fib.values()) == 1
    rng = random.Random(12345)
    for _ in range(25):
        a = {n: Fraction(rng.randint(-9, 9), rng.randint(1, 9)) for n in cols}
        b = {m: Fraction(rng.randint(-9, 9), rng.randint(1, 9)) for m in rows}
        Fa = {m: a.get(map_fn(m), Fraction(0)) for m in rows}
        # Part (3): exact norm identity and sqrt(2) upper bound
        norm2_Fa = sum(v * v for v in Fa.values())
        assert norm2_Fa == sum(fib[n] * a[n] * a[n] for n in cols)
        assert norm2_Fa <= 2 * sum(v * v for v in a.values())
        # Part (4): <Fa, b> == <a, F* b> with (F* b)_n = sum_{map(m)=n} b_m
        lhs = sum(Fa[m] * b[m] for m in rows)
        Fstar_b = {n: sum(b[m] for m in rows if map_fn(m) == n) for n in cols}
        rhs = sum(a[n] * Fstar_b[n] for n in cols)
        assert lhs == rhs
    print(tag, "all checks passed (N =", N, ")")

check(T, 0, 60, 2, "T (3n+1, on N_0)")   # two preimages iff n = 2 mod 3
check(U, 1, 60, 1, "U (3n-1 control)")   # two preimages iff n = 1 mod 3
