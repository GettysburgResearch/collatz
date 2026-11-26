"""Exact finite controls of deterministic pair forcing and first-descent excursions."""
import json
from fractions import Fraction


def step(n):
    return (3 * n + 1) // 2 if n & 1 else n // 2


def first_one(x, limit=250_000):
    for h in range(limit + 1):
        if x == 1:
            return h
        x = step(x)
    raise ValueError("Control did not reach 1 within its finite verification budget")


def choose_parity(h, c):
    if h:
        return int(c == 0 or c % 2 != 0)
    if c == 0:
        raise ValueError("A fused pair needs no further bit")
    return int(c % 4 == 3)


def ray_step(x, y, h, c):
    if y != 3**h * x + c:
        raise ValueError("Incorrect initial affine relation")
    next_h = h + (y & 1) - (x & 1)
    a, b = step(x), step(y)
    if next_h < 0:
        a, b, next_h = b, a, -next_h
    return next_h, b - 3**next_h * a


def test_forcing():
    max_steps = 0
    starts = 0
    for h0 in range(10):
        for c0 in range(-128, 129):
            h, c = h0, c0
            seen = set()
            while h or c:
                if (h, c) in seen:
                    raise ValueError("Deterministic forcing entered a loop")
                seen.add((h, c))
                b = choose_parity(h, c)
                x = 2 * (abs(c) + 1) + b
                h, c = ray_step(x, 3**h * x + c, h, c)
            starts += 1
            max_steps = max(max_steps, len(seen))
    return {"initial_affine_states": starts, "maximum_forced_steps": max_steps}


def floor_alpha(i):
    return (3**i).bit_length() - 1


def rotate_under(word):
    out = list(word)
    while (1 << sum(out)) >= 3**len(out):
        out.append(1)
    a = 0
    weights = [Fraction(1)]
    for i, e in enumerate(out, 1):
        a += e
        weights.append(Fraction(1 << a, 3**i))
    cut = weights.index(max(weights)) % len(out)
    return out[cut:] + out[:cut]


def append_compensation(word, r):
    a, n = sum(word), len(word)
    previous = 0
    extra = []
    for i in range(1, r + 1):
        partial = (floor_alpha(i * (n + r)) - i * a) // r
        if i == r:
            partial += 1
        extra.append(partial - previous)
        previous = partial
    return word + extra


def append_twos(word):
    w = list(word)
    while 1 << sum(w) < 3**len(w):
        w.append(2)
    return w


def upper_class(word):
    clock, carry = 0, 0
    for gap in word:
        if gap < 1:
            raise ValueError("Zero gap")
        carry = 3 * carry + (1 << clock)
        clock += gap
    power = 3**len(word)
    modulus = 1 << (clock + 1)
    n = ((1 << clock) - carry) * pow(power, -1, modulus) % modulus
    q = n * pow(3, -1, modulus) % modulus
    cutoff_n = carry // ((1 << clock) - power) + 1
    return q, clock + 1, cutoff_n


def fuse(q, bits, specs):
    rays = []
    for d, offset in specs:
        x = 3**d * q + offset
        h = d
        for _ in range(bits):
            h += x & 1
            x = step(x)
        rays.append((h, x))
    original_bits = bits
    for target in range(1, len(rays)):
        while rays[0] != rays[target]:
            left, right = (0, target) if rays[0][0] <= rays[target][0] else (target, 0)
            h = rays[right][0] - rays[left][0]
            c = rays[right][1] - 3**h * rays[left][1]
            bit = (choose_parity(h, c) - rays[left][1]) % 2
            new_rays = []
            for p, a in rays:
                entry = a + bit * 3**p
                new_rays.append((p + (entry & 1), step(entry)))
            q += bit << bits
            bits += 1
            rays = new_rays
    return q, bits, rays[0], bits - original_bits


def certify(name, word, specs, ternary_residue, ternary_modulus):
    q, bits, lower_n = upper_class(word)
    base, bits, (p, a), extra_bits = fuse(q, bits, specs)
    period = 1 << bits
    t = (ternary_residue - base) * pow(period, -1, ternary_modulus) % ternary_modulus
    while 3 * (base + period * t) < lower_n or min(3**d*(base + period*t)+b for d,b in specs) <= 0:
        t += ternary_modulus
    q = base + period * t
    if q % ternary_modulus != ternary_residue:
        raise ValueError("Ternary choice failed")
    target = a + 3**p * t
    target_to_one = first_one(target)
    for d, b in specs:
        x = 3**d * q + b
        for _ in range(bits):
            x = step(x)
        if x != target:
            raise ValueError("Actual integer ray failed to fuse")
    n = 3 * q
    x = n
    physical = 0
    for e in word:
        if x % 2 != 1:
            raise ValueError("Nonodd gap source")
        v = 3*x+1
        if (v & -v).bit_length() - 1 != e:
            raise ValueError("Incorrect accelerated gap on actual ordinary source")
        for _ in range(e):
            x = step(x)
            physical += 1
            if physical < sum(word) and x <= n:
                raise ValueError("Earlier physical descent")
    if not (x % 2 and n < 2*x and x < n):
        raise ValueError("Wrong final crossing or floor")
    return {"name": name, "ordinary_q": str(q), "ray_specifications": specs,
            "ternary_q": [ternary_residue, ternary_modulus], "gaps": word,
            "first_descent_clock": physical, "first_descent_value": str(x),
            "coupled_clock": bits, "extra_forcing_bits": extra_bits,
            "common_terminal": str(target), "terminal_to_one_clocks": target_to_one}


def main():
    if not (3**100000 < 2**158499 and
            164179**164179 < 64179**64179 * 100000**100000 * 3**100000 and
            Fraction(5680, 64179) > Fraction(177, 2000)):
        raise ValueError("Entropy component mass interval failed")
    neg_one = append_compensation(rotate_under([1]*18), 4)
    neg_five = append_compensation(rotate_under([2, 1]*12), 3)
    mech = [floor_alpha(i+1)-floor_alpha(i) for i in range(31)]
    critical = append_twos(rotate_under(mech))
    sparse = append_compensation(rotate_under([1,1,4,1,1,1,1]*3), 5)
    mixed = append_compensation(rotate_under([1]*20 + [2,1]*10), 4)
    controls = [
        certify("negative fixed phase", neg_one, [(0, 0), (1, 0)], 2, 9),
        certify("negative two-gap period", neg_five, [(0, 0), (1, 0), (0,-2),(1,-6)], 4, 9),
        certify("critical bounded-gap mechanical block", critical, [(0, 0), (1, 0)], 8, 27),
        certify("longer sparse-gap period", sparse, [(0,0),(1,0),(2,1)], 1, 3),
        certify("mixture block", mixed, [(0,0),(1,0),(0,-4)], 0, 3),
    ]
    print(json.dumps({"forcing": test_forcing(), "component_mass_lower_bound": "5680/64179",
                      "ordinary_excursions": controls}, indent=2))


if __name__ == "__main__":
    main()
