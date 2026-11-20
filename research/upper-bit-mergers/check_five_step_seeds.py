"""Replay the paired lifts, W512-060 seed test, and Mersenne five comparisons."""

from check import step


def advance(value, clocks):
    for _ in range(clocks):
        value = step(value)
    return value


def bounded_hit(value, limit):
    """Return (clock, odd inputs) at first arrival, if it is within the clock budget."""
    odd_count = 0
    for clock in range(limit + 1):
        if value == 1:
            return clock, odd_count
        if clock < limit:
            odd_count += value % 2
            value = step(value)
    return None


def first_hit_prefixes(value, word):
    """Validate the entire supplied word and keep only the strict first-hit prefixes."""
    clock = 0
    prefixes = []
    for rank, exponent in enumerate(word, 1):
        even = 3 * value + 1
        exact = (even & -even).bit_length() - 1
        if exponent != exact:
            raise ValueError("incorrect exponent in supplied upper witness")
        value = even >> exact
        clock += exact
        if value != 1:
            prefixes.append((rank, clock, value))
    if value != 1:
        raise ValueError("upper witness does not terminate at 1")
    return prefixes


def applicable_bases(k, word):
    if k <= 0 or k % 4 == 0:
        raise ValueError("ineligible index")
    bases = set()
    for rank, clock, value in first_hit_prefixes(128 * k + 1, word):
        change, rem = divmod((value - 1) << clock, 128 * 3**rank)
        base = k - change
        if rem or not 0 < base < k or base % 4 == 0:
            continue
        depth = (change & -change).bit_length() - 1
        upper = bounded_hit(128 * base + 1, clock)
        lower = bounded_hit(64 * base + 1, depth + 5)
        if upper is None or lower is None:
            continue
        upper_height = upper[0] - 2 * upper[1]
        lower_height = lower[0] - 2 * lower[1]
        threshold = max(2, upper[0] - 6, lower[0] - 5, lower_height, 5 - 4 * upper_height)
        if depth >= threshold and 1 - upper_height + lower_height >= 0:
            bases.add(base)
    return sorted(bases)


def endpoint_and_odd_count(value, clocks):
    odd_count = 0
    for _ in range(clocks):
        odd_count += value % 2
        value = step(value)
    return value, odd_count


def check_paired_lifts():
    seed, endpoint, length, odd_count = 6375551795, 1215835, 71, 37
    for scale in [1, 5]:
        if endpoint_and_odd_count(scale * seed, length) != (scale * endpoint, odd_count):
            raise AssertionError("incorrect proportional return")
    value = seed
    for exponent in [1, 3, 3, 3, 3, 3, 3]:
        even = 3 * value + 1
        if (even & -even) != 2**exponent:
            raise AssertionError("incorrect accelerated prefix")
        value = even >> exponent
    # Construct modest-sized ordinary examples with a deliberately even endpoint.
    # Modular division chooses the odd q first, so the lift has the requested b.
    for extra_bits, ternary_digits, residue, b in [(0, 1, 1, 24), (15, 3, 5, 40), (150, 8, 1, 160)]:
        ternary_modulus = 3**(odd_count + ternary_digits)
        target_modulus = 3**ternary_digits
        kappa = (residue - seed) * pow(2**length, -1, target_modulus) % target_modulus
        target = endpoint + 3**odd_count * kappa
        q = target * pow(2**b, -1, ternary_modulus) % ternary_modulus
        if q % 2 == 0:
            q += ternary_modulus
        lift_index, rem = divmod((q << b) - endpoint, 3**odd_count)
        x = seed + (lift_index << length)
        modulus = 2**(length + extra_bits)
        center = seed - (endpoint << length) * pow(3**odd_count, -1, modulus)
        if rem or lift_index < 0 or (x - center) % modulus or (x - residue) % target_modulus:
            raise AssertionError("wrong lift residues")
        if any(advance(scale * x, length + b) != scale * q for scale in [1, 5]):
            raise AssertionError("prescribed endpoints not attained")

    for q in range(1, 54, 2):  # all odd representatives of the unit residues mod 27
        if q % 3 == 0:
            continue
        first = next(i for i in range(6, 12) if (2**i * q - 7) % 9 == 0)
        lifts = [(i, (2**i * q - 7) // 9) for i in (first, first + 6)]
        clock, x = next((i, x) for i, x in lifts if x % 3)
        if x % 64 != 49 or not 0 < 9 * x < 2**17 * q:
            raise AssertionError("small-constant unit lift failed")
        if any(advance(scale * x, clock) != scale * q for scale in [1, 5]):
            raise AssertionError("short ladder did not preserve both endpoints")


def check_base_search():
    k = 1 + 2**71
    value = 128 * k + 1
    word = []
    for _ in range(2000):
        if value == 1:
            break
        even = 3 * value + 1
        exponent = (even & -even).bit_length() - 1
        word.append(exponent)
        value = even >> exponent
    if value != 1 or 1 not in applicable_bases(k, word + [2, 2]):
        raise AssertionError("positive seed fixture failed")
    try:
        applicable_bases(k, word + [3])
    except ValueError:
        pass
    else:
        raise AssertionError("invalid terminal padding accepted")
    for c in [1, 3, 4, 5, 56, 110]:
        a = next(a for a in range(4, 166, 2) if ((2**a - 1) * 2**c - 12) % 486 == 0)
        index = ((2**a - 1) * 2**c - 12) // 486
        if applicable_bases(index, [2, 2, 2, c, a]):
            raise AssertionError(("unexpected rank-five base", c, a))


def check_multiplier_paths():
    if (55 * 176106)**2 * 3**119 >= 4**119:
        raise AssertionError("insufficient uniform height margin")
    for j in range(10):
        e = 119 + 162 * j
        h = e + 1
        x = (1024 * 2**e - 2573) // 243
        if (x - 1) % 256 or ((x - 1) // 256) % 16 != 7:
            raise AssertionError("wrong P-rule class for the Mersenne family")
        if advance((x + 1) // 2, 9) != 2**e - 1:
            raise AssertionError("missing companion checkpoint")
        if advance(2**e - 1, e + 2) != advance(2**h - 1, h + 2):
            raise AssertionError("Mersenne meeting failed")
        for r in (1 if j % 2 else 2, 101 if j % 2 else 20):
            q, rem = divmod(3**r * 2**(h-r) - 1, 5)
            if rem or q % 2 != 1 or q % 3 == 0 or advance(2**h - 1, r) != 5 * q:
                raise AssertionError("invalid five source")
            s = e - r
            u = step(q)
            w = advance(u, 3 * (s // 3))
            v = advance(5 * u, 2 * (s // 2))
            if u % 2 != 1 or 5 * w != 2**(s % 3) * 3**(r + 1 + s // 3) + 1:
                raise AssertionError("wrong source checkpoint")
            if v != 2**(s % 2) * 3**(r + 1 + s // 2) + 1:
                raise AssertionError("wrong multiplied successor checkpoint")
            if r <= 2:
                if 4 * q >= x or 176106 * max(v, w) >= 2**e:
                    raise AssertionError("small-comparison bound failed")
            else:
                b = 54 * (j + 1 + j % 2)
                if w % 2 or (w // 2) % 2 != 1 or 5 * (w // 2) != step(3**(b - 1)):
                    raise AssertionError("rank-four component mismatch")


if __name__ == "__main__":
    check_paired_lifts()
    check_base_search()
    check_multiplier_paths()
    print("Paired source lifts, seed applicability, and Mersenne five comparisons passed.")
