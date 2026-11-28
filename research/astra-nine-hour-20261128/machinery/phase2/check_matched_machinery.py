"""Exact finite controls for the second machinery checkpoint."""

from fractions import Fraction
from itertools import accumulate


def require(condition, message):
    if not condition:
        raise ValueError(message)


def step(z):
    return (3 * z + 1) // 2 if z % 2 else z // 2


def trace(z, ticks):
    odds = 0
    for _ in range(ticks):
        odds += z % 2
        z = step(z)
    return z, odds


def check_blocks():
    copies = 0
    negative_shifts = 0
    for ticks in range(1, 15):
        for anchor in range(1, 1001, 2):
            endpoint, count = trace(anchor, ticks)
            if not endpoint % 2:
                continue
            for width in (2, 3, 4, 6):
                if any(trace(anchor + i, ticks) != (endpoint, count)
                       for i in range(1, width)):
                    break
                for shift in (-3, -1, 0, 1, 5):
                    target = endpoint + 3**count * shift
                    if target <= 0:
                        continue
                    base = anchor + 2**ticks * shift
                    require(base > 0, "positive target had nonpositive preimage")
                    for offset in range(width):
                        require(trace(base + offset, ticks) == (target, count),
                                "counted copy lost its endpoint or odd count")
                    copies += 1
                    negative_shifts += int(shift < 0)
    require(copies > 100 and negative_shifts > 20, "insufficient signed block sample")
    print(f"counted block copies={copies}, negative displacements={negative_shifts}")


def v2(n):
    return (n & -n).bit_length() - 1


def pnorm(n, prime):
    if n == 0:
        return Fraction(0)
    den = 1
    while n % prime == 0:
        n //= prime
        den *= prime
    return Fraction(1, den)


def check_forms_and_minima():
    checked = clean = 0
    signed_equalities = {b: 0 for b in range(-4, 5)}
    for m in range(1, 250, 2):
        states, valuations = [m], []
        for _ in range(15):
            numerator = 3 * states[-1] + 1
            valuation = v2(numerator)
            states.append(numerator >> valuation)
            valuations.append(valuation)
        cumulative = list(accumulate(valuations, initial=0))
        terminal = len(valuations)
        heights = [Fraction(states[-1] * 2**(cumulative[-1] - s),
                            3**(terminal - j)) for j, s in enumerate(cumulative)]
        intercept = heights[0] - states[0]
        rate = Fraction(6, 5)
        scaled = [h / rate**j for j, h in enumerate(heights)]
        minima = [min(scaled[j:]) for j in range(len(scaled))]
        good = [j for j in range(terminal) if scaled[j] == minima[j]]
        require(minima[-1] <= minima[0] * (Fraction(3, 2) / rate)**len(good),
                "finite suffix-minimum count failed")
        for j in good:
            require(heights[j] - states[j] <= 1 / (3 * (1 - 1 / rate)),
                    "finite clean correction exceeded geometric bound")
        clean += len(good)
        num = 0
        for j, (s, a) in enumerate(zip(cumulative, states)):
            q = 3**j
            require(q * m + num == 2**s * a, "affine numerator")
            for b in signed_equalities:
                z = a + b
                if 0 < z < q:
                    u = num + b * 2**s
                    real = abs((intercept * q - u) * q)
                    finite = pnorm(u + m * q, 2) * pnorm(q, 2)
                    finite *= pnorm(u, 3) * pnorm(q, 3)
                    for p in (5, 7):
                        finite *= pnorm(u + m * q, p) * pnorm(q, p)
                    product = abs(heights[j] - a - b)
                    for p in (2, 3, 5, 7):
                        product *= pnorm(z, p)
                    require(real * finite == product, "shifted adelic product")
                    checked += 1
                for k in range(j + 1, min(terminal, j + 4) + 1):
                    r, d = k - j, cumulative[k] - s
                    equal = 2**d * (states[k] + b) == 3**r * (a + b)
                    same_word = (a + b) % (2**d) == 0
                    closed = same_word and trace(-b, d) == (-b, r)
                    require(equal == closed, "signed closed-word exception")
                    signed_equalities[b] += int(equal)
            num = 3 * num + 2**s
    require(checked > 1000 and clean > 20, "insufficient arithmetic sample")
    print(f"adelic products={checked}, bounded-tail dates={clean}, "
          f"closed signed windows={sum(signed_equalities.values())}")


def has_end_square(word):
    return any(sum(word[-h:]) == sum(word[-2*h:-h])
               for h in range(1, len(word) // 2 + 1))


def square_free_sample(length):
    def extend(word):
        if len(word) == length:
            return word
        for z in range(1, 7):
            candidate = word + [z]
            if not has_end_square(candidate):
                found = extend(candidate)
                if found is not None:
                    return found
        return None
    sample = extend([])
    require(sample is not None, "short finite avoiding sample absent")
    return sample


def check_valuation_codes():
    w = square_free_sample(48)
    binary = [((i * i + 3 * i + 5) % 17) % 2 for i in range(len(w) + 1)]
    v = [3 * x + binary[j + 1] - binary[j] for j, x in enumerate(w)]
    require(all(not has_end_square(v[:j]) for j in range(1, len(v) + 1)),
            "decoration added an additive square")
    period = 25
    e = [1] * (period * len(w))
    for j, x in enumerate(v):
        e[j * period] += 2 * x + 1
    sums = list(accumulate(e, initial=0))
    windows = 0
    for h in range(period, len(e) // 2 + 1):
        for i in range(len(e) - 2*h + 1):
            require(sums[i] + sums[i + 2*h] != 2 * sums[i + h],
                    "long equal adjacent valuation clocks")
            windows += 1
    # Binary cylinder: solve 3^j z + B = 2^s modulo 2^(s+1).
    j = 75
    num = 0
    for s in sums[:j]:
        num = 3 * num + 2**s
    s = sums[j]
    modulus = 2**(s + 1)
    z = ((2**s - num) * pow(3**j, -1, modulus)) % modulus
    require(z > 0 and z % 2 == 1, "finite binary lift not ordinary odd")
    for expected in e[:j]:
        numerator = 3 * z + 1
        require(v2(numerator) == expected, "finite physical lift mismatch")
        z = numerator >> expected
    print(f"avoiding seed letters={len(w)}, long adjacent-window tests={windows}, "
          f"true prescribed valuations at one finite source={j}")


if __name__ == "__main__":
    check_blocks()
    check_forms_and_minima()
    check_valuation_codes()
