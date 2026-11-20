"""Exact finite checks of the signed checkpoint, its exits and its counting law."""

from itertools import product

from check import step, walk


def valuation(n, prime):
    exponent = 0
    while n % prime == 0:
        n //= prime
        exponent += 1
    return exponent


def check_small_witness(m, n, k, a, clock, excess):
    """Split an actual meeting into its three odd-count segments and recover beta."""
    z = m
    cuts = []
    odd = 0
    for time in range(1, clock + 1):
        bit = z % 2
        z = step(z)
        odd += bit
        if bit and odd in (excess, excess + a):
            cuts.append((time, z))
    if odd != 2 * k + a + excess or len(cuts) != 2:
        raise AssertionError(("split", m, n, clock, cuts))
    (first, v), (second, _) = cuts
    length = second - first
    b = clock - second - 3 * k
    if b < 0:
        raise AssertionError(("short suffix", m, n, b))
    beta = v - 2 ** (length + b) * (n // 3**a)
    if beta <= 0 or 2**excess * (beta + 1) >= 5 * 3**excess:
        raise AssertionError(("small witness", m, n, beta, excess))
    if walk(beta, length)[1] != a or 2 ** (excess + length) >= 3 ** (excess + a):
        raise AssertionError(("witness prefix", m, n, beta, length, a))


def check_smaller_sources(limit, clock):
    # Store the smallest odd cost seen at each state, among strictly earlier starts.
    cheapest = {}
    tested = meetings = witnesses = 0
    for n in range(1, limit + 1):
        k = valuation(n + 5, 2) // 3
        if k:
            a = valuation(n, 3)
            z, odd = n, 0
            for i in range(3 * k + 1):
                if z in cheapest:
                    cost, source, source_clock = cheapest[z]
                    if cost <= odd + a + (a >= 6):
                        raise AssertionError(("smaller source", n, source, z, cost, odd, a))
                    meetings += 1
                    if a:
                        check_small_witness(source, n, k, a, source_clock + 3 * k - i, cost - odd - a)
                        witnesses += 1
                tested += 1
                odd += z % 2
                z = step(z)
        z, odd = n, 0
        seen = set()
        for j in range(clock + 1):
            if z in seen:
                break
            seen.add(z)
            if z not in cheapest or cheapest[z][0] > odd:
                cheapest[z] = (odd, n, j)
            odd += z % 2
            z = step(z)
    return tested, meetings, witnesses


def check_targets():
    tested = 0
    for k, a, u in product(range(1, 4), range(3), (1, 5, 7)):
        modulus = 3 ** (2 * k + a)
        period = 2 * modulus // 3
        rhs = 5 * (9**k - 8**k) * pow(8**k * u, -1, modulus) % modulus
        power = 1
        for exponent in range(period):
            if power == rhs:
                break
            power = 2 * power % modulus
        else:
            raise AssertionError(("missing target residue", k, a, u))
        r = ((9**k) // 8**k).bit_length()
        for length in (exponent + period, exponent + 2 * period):
            y = 2**length * u
            t, remainder = divmod(y + 5, 9**k)
            n = 8**k * t - 5
            if remainder or n % 3**a or walk(n, 3 * k) != (y, 2 * k):
                raise AssertionError(("checkpoint target", k, a, u, length))
            z = n
            for time in range(1, 3 * k + r + 1):
                z = step(z)
                if (z < n) != (time == 3 * k + r):
                    raise AssertionError(("first descent", n, time))
            if walk(n, 3 * k + length)[0] != u:
                raise AssertionError(("target not reached", k, a, u, length))
            tested += 1
    return tested


def check_density(k, horizon):
    low_modulus = 8**k
    low_period = low_modulus // 4
    first = next(a for a in range(1, low_period + 1) if pow(3, a, low_modulus) == low_modulus - 5)
    period = low_period * 2**horizon
    base = period * (1 + (4 * (3 * k + horizon) + 8) // period)
    observed = {}
    for high in range(2**horizon):
        n = 3 ** (base + first + low_period * high)
        z, odd = walk(n, 3 * k)
        if odd != 2 * k or z < n:
            raise AssertionError(("initial word", k, n))
        parity = []
        descended = False
        for _ in range(horizon):
            parity.append(z % 2)
            z = step(z)
            descended |= z < n
        key = tuple(parity)
        if key in observed:
            raise AssertionError(("repeated exit word", k, horizon, key))
        observed[key] = descended
    for word in product((0, 1), repeat=horizon):
        odd = 0
        predicted = False
        for j, bit in enumerate(word, start=1):
            odd += bit
            predicted |= 9**k * 3**odd < 8**k * 2**j
        if observed[word] != predicted:
            raise AssertionError(("first passage", k, horizon, word))
    return len(observed)


if __name__ == "__main__":
    tested, meetings, witnesses = check_smaller_sources(16384, 128)
    targets = check_targets()
    words = sum(check_density(k, horizon) for k in range(1, 4) for horizon in range(9))
    print(f"{tested} checkpoint positions, {meetings} with an actual earlier source")
    print(f"{witnesses} small ordinary witnesses recovered from actual mergers")
    print(f"{targets} prescribed-target orbits, {words} exponent lifts checked against first passage")
