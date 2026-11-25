"""Replay signed switches, physical denominator cancellation, and rotation orders."""
from fractions import Fraction
from math import gcd, isqrt, lcm, prod


def check(truth, message):
    if not truth:
        raise ValueError(message)


def valuation(x, prime):
    count = 0
    while x and x % prime == 0:
        count += 1
        x //= prime
    return count


def subset_sum(weights, target, modulus):
    reached = {0: ()}
    for i, w in enumerate(weights):
        for prior, bits in tuple(reached.items()):
            reached.setdefault((prior + w) % modulus, bits + (i,))
        if target in reached:
            return reached[target]
    raise ValueError("target absent")


def test_switches():
    primes = (5, 7, 11)
    k = 21
    n = isqrt(k - 1) + 1
    v = 2
    m = lcm(*(s-1 for s in primes))
    modulus = prod(s**k for s in primes)
    tested = 0
    for prime in primes:
        b = valuation(v**m - 1, prime)
        for d in range(n*b, k):
            whole, extra = divmod(d-n*b, n)
            ts = [m*2**i*prime**(whole + (i >= n-extra))
                  * prod(s**n for s in primes if s != prime) for i in range(n)]
            positive, negative = {0}, set()
            for t in ts:
                shifted_pos = {e+t for e in positive}
                shifted_neg = {e+t for e in negative}
                check(min(shifted_pos | shifted_neg) > max(positive | negative),
                      "support separation")
                positive, negative = shifted_pos | negative, shifted_neg | positive
            delta = (sum(pow(v, e, modulus) for e in positive)
                     - sum(pow(v, e, modulus) for e in negative)) % modulus
            expected = prod(pow(v, t, modulus)-1 for t in ts) % modulus
            check(delta == expected and valuation(delta, prime) == d, "exact digit")
            check(all(delta % s**k == 0 for s in primes if s != prime), "other primes")
            span = sum(ts) + 1
            digits = [(delta * pow(v, c * span, modulus) % modulus) // prime**d % prime
                      for c in range(prime-1)]
            for target in range(1, prime):
                ids = subset_sum(digits, target, prime)
                check(sum(digits[i] for i in ids) % prime == target, "reachable digit")
                tested += 1
    return tested


def physical_example():
    p, h = 306, 485
    d = h-p
    D = 2**h - 3**p
    prime = 929
    Q = prime**valuation(D, prime)
    check(Q == prime, "actual primary factor")
    # ap+bh=1 gives the exact unit inverse local generator.
    b = pow(h, -1, p)
    a = (1-b*h)//p
    u = pow(2, a, Q)*pow(3, b, Q) % Q
    v = pow(u, -1, Q)
    check(pow(v,p,Q)*2%Q == 1 and pow(v,h,Q)*3%Q == 1, "clock generator")
    bits = [int(0 < r <= p//3 and r%5 in (0,1,3)) for r in range(p)]
    todo = [p-1]
    forced = set()
    while todo:
        r = todo.pop()
        if r < 0 or r in forced:
            continue
        forced.add(r)
        bits[r] = 1
        todo.extend((r-d, r-(p-d)))
    reserve = [r for r in range(1,28) if r not in forced]
    for r in reserve:
        bits[r] = 0
    weights = [pow(v,r,Q) for r in range(p)]
    need = sum((2-bit)*w for bit,w in zip(bits,weights)) % Q
    for i in subset_sum([weights[r] for r in reserve], need, Q):
        bits[reserve[i]] = 1
    order = [i*h%p for i in range(p)]
    word = []
    C = A = 0
    for r in order:
        wrap, target = divmod(r+h,p)
        gap = wrap + bits[r] - bits[target]
        check(gap in (1,2), "legal exponent")
        C = 3*C + 2**A
        A += gap
        word.append(gap)
    x0 = Fraction(C,D)
    check(A == h and C%Q == 0 and gcd(x0.denominator,Q) == 1, "local cancellation")
    check(x0.denominator > 1, "nonordinary remaining denominator")
    x = x0
    mantissas, physical, odd = {}, [], []
    for r, gap in zip(order, word):
        check(x.numerator%2 == 1, "odd phase")
        odd.append(x)
        physical.append(x)
        mantissas[r] = x/2**bits[r]
        x = (3*x+1)/2
        if gap == 2:
            check(x.numerator%2 == 0, "even intermediate phase")
            physical.append(x)
            x /= 2
    check(x == x0 and min(odd) == x0 and len(set(odd)) == p, "primitive cycle")
    check(sorted(mantissas,key=mantissas.get) == list(range(p)), "dyadic order")
    ternary = [y if y < 3*x0 else y/3 for y in physical]
    check(all(x0 <= y < 3*x0 for y in ternary), "ternary range")
    ranks = {y:i for i,y in enumerate(sorted(ternary))}
    check([ranks[y] for y in ternary] == [-i*p%h for i in range(h)], "ternary order")
    check(3*x0 < max(odd) < 4*x0, "elevated width")
    mismatches = min(sum(b != bits[(i+t)%p] for i,b in enumerate(bits))
                     for t in range(1,p))
    check(40*mismatches > p, "all-shift mismatch")
    return p, h, Q, x0.denominator.bit_length(), mismatches


if __name__ == "__main__":
    print("Synthetic single-digit targets reached:", test_switches())
    p, h, factor, bits, mismatches = physical_example()
    print(f"Physical p={p}, h={h}, full tested factor={factor}, "
          f"remaining denominator bits={bits}, minimum shift mismatches={mismatches}.")
