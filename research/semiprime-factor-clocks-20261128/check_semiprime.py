"""Exact arithmetic certificate for a long rising semiprime in PR 217's family."""
from math import gcd, isqrt, lcm


def require(value, reason):
    if not value:
        raise AssertionError(reason)


def prime_by_trial(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def mersenne_prime(exponent):
    require(prime_by_trial(exponent), "prime Mersenne exponent")
    m = 2**exponent - 1
    v = 4
    for _ in range(exponent - 2):
        v = (v*v - 2) % m
    require(v == 0, "Lucas–Lehmer test")
    return m


def find_q(p, k, r):
    modulus = 2**k
    residue = ((-pow(p, -1, modulus) - 1) * pow(r, -1, modulus)) % modulus
    small_primes = [x for x in range(2, 400) if prime_by_trial(x)]
    for index in range(20000):
        b = residue + index * modulus
        q = r*b + 1
        if q >= r*r:
            break
        if any(q % ell == 0 for ell in small_primes):
            continue
        if pow(2, q-1, q) == 1 and gcd(pow(2, b, q) - 1, q) == 1:
            # Any prime s|q then has r|ord_s(2)|s-1: otherwise
            # ord_s(2)|(q-1)/r, since q-1=r*b and gcd(r,b)=1 follows b<r.
            # A composite q has at least two prime factors, each >= r+1.
            return index, q
    raise ValueError("certificate search exhausted")


def step(v):
    return (3*v + 1)//2 if v % 2 else v//2


def trajectory(p, q, k):
    n = p*q
    require(n % 2**k == 2**k-1, "required all-odd residue")
    v = n
    first_q = first_p = first_n = None
    peak = n
    for t in range(1, 60000):
        old = v
        v = step(v)
        if t <= k:
            require(old % 2 == 1 and v > old, "strict initial ascent")
            require(v + 1 == 3**t * ((n+1)//2**t), "exact prefix formula")
        peak = max(peak, v)
        if first_n is None and v < n:
            first_n = t
        if first_q is None and v < q:
            first_q = t
        if first_p is None and v < p:
            first_p = t
        if v == 1:
            return first_n, first_q, first_p, t, peak.bit_length()
    raise ArithmeticError("explicit search budget reached before hitting one")


def prefix(start, length):
    path = [start]
    for _ in range(length):
        path.append(step(path[-1]))
    return path


def finite_controls():
    """Check the word distribution, floor inequality and every small merger."""
    for k in range(1, 10):
        words = {tuple(v % 2 for v in prefix(n, k)[:-1])
                 for n in range(1, 2**k, 2)}
        require(len(words) == 2**(k-1) and all(w[0] for w in words),
                "odd-start parity bijection")

    floors = 0
    for n in range(1, 129):
        path = prefix(n, 10)
        for t in range(1, len(path)):
            departures = path[:t]
            q = min(departures)
            s = sum(x % 2 for x in departures)
            require(3**s*n <= 2**t*path[t], "lower affine product")
            require(q**s * 2**t*path[t] <= (3*q+1)**s*n, "upper floor product")
            floors += 1

    meetings = 0
    for p in (5, 7, 11, 13):
        for q in range(1, 65):
            a, b = prefix(p*q, 10), prefix(q, 10)
            for i, x in enumerate(a):
                for j, y in enumerate(b):
                    if x != y:
                        continue
                    h = max(i, j)
                    require(q + 2**h <= 3**h, "integer merger height")
                    odd = [v for v in a[:i] + b[:j] if v % 2]
                    require(odd and 3*min(odd) <= h*(p*2**abs(i-j)+1),
                            "time-lag merger floor")
                    meetings += 1
    return floors, meetings


def cycle_path(start):
    """Record exact first appearances up to the first repeated vertex."""
    dates, path = {}, []
    v = start
    while v not in dates:
        require(len(path) < 60000, "cycle search budget reached")
        dates[v] = len(path)
        path.append(v)
        v = step(v)
    return dates, path, dates[v]


def value_at(path, cycle_entry, t):
    if t < len(path):
        return path[t]
    return path[cycle_entry + (t - cycle_entry) % (len(path) - cycle_entry)]


def check_meetings(n, q):
    dates_n, path_n, entry_n = cycle_path(n)
    dates_q, path_q, entry_q = cycle_path(q)
    require((entry_n, entry_q) == (6921, 4577), "first cycle-entry dates")
    require((dates_n[1], dates_q[1]) == (6922, 4578), "first-one dates")
    common = dates_n.keys() & dates_q.keys()
    meeting = min((max(dates_n[v], dates_q[v]), dates_n[v], dates_q[v], v)
                  for v in common)
    require(meeting == (6916, 6916, 4572, 20), "earliest asynchronous meeting")
    period = lcm(len(path_n) - entry_n, len(path_q) - entry_q)
    for t in range(max(entry_n, entry_q) + period):
        v = value_at(path_n, entry_n, t)
        if v == value_at(path_q, entry_q, t):
            require((t, v) == (6921, 2), "earliest synchronous meeting")
            return meeting, (t, v)
    raise ArithmeticError("no synchronous meeting")


if __name__ == "__main__":
    controls = finite_controls()
    require(controls == (1280, 543), "control coverage")
    print("floor and merger controls:")
    print(*controls)
    p, k = 2003, 480
    require(prime_by_trial(p), "small prime")
    r = mersenne_prime(521)
    j, q = find_q(p, k, r)
    n = p*q
    require(p < q and n.bit_length() < p and (n.bit_length()-1)**2 > 4*p,
            "factor interval by 1/2 < log 2 < 1")
    require((j, n.bit_length(), len(str(n))) == (168, 1020, 307), "witness size")
    clocks = trajectory(p, q, k)
    require(clocks == (1793, 1814, 6838, 6922, 1302), "factor clocks and peak")
    asynchronous, synchronous = check_meetings(n, q)
    print("p, k, lift index, product binary digits, decimal digits:")
    print(p, k, j, n.bit_length(), len(str(n)))
    print("q =", q)
    print("first below product, larger factor, smaller factor, first one, peak bits:")
    print(*clocks)
    print("first asynchronous meeting (horizon, product date, prime date, value):")
    print(*asynchronous)
    print("first synchronous meeting (date, value):")
    print(*synchronous)
