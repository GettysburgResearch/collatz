"""Integer replay for moving origins, depth composition and inverse prices."""
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def step(n):
    return (3 * n + 1) // 2 if n % 2 else n // 2


def run(n, clocks):
    odds = 0
    for _ in range(clocks):
        odds += n % 2
        n = step(n)
    return n, odds


def first_hit(n, limit=20000):
    odds = 0
    for clocks in range(limit + 1):
        if n == 1:
            return clocks, odds
        odds += n % 2
        n = step(n)
    raise ValueError("finite hit guard exhausted")


def moving_origins():
    charts = 0
    continuations = 0
    for v in range(1, 41):
        for carry in range(1, 20):
            for e in range(1, 24):
                lower, p = run(v + carry, e)
                upper, r = run(v, e)
                if (lower, upper) != (1, 1) or min(p, r) == 0:
                    continue
                charts += 1
                for u in (1, 3, 7, 15, 33):
                    x, y = v + carry + (u << e), v + (u << e)
                    require(run(x, e + 1)[0] == step(3 ** (p - 1) * u), "lower merger")
                    for k in (0, 1, 4, 11):
                        terminal, price = run(y, e + 1 + k)
                        other, charge = run(3 ** (r - 1) * u, 1 + k)
                        require((terminal, price) == (other, r - 1 + charge), "upper suffix")
                        continuations += 1
    return {"reference_pairs_and_clocks": charts, "ordinary_upper_suffixes": continuations}


def source(index):
    return 89585 + 48 * 2**19 * index


def direct_chains():
    source_rows = 0
    replacements = 0
    costs = 0
    max_bits = 0
    for depth in (0, 1, 2, 3, 8, 16, 32):
        for seed in (0, 1, 17, 99):
            index = seed
            for _ in range(depth):
                index = 204954140672 * index + 729593939
            z = source(index)
            origin = z
            max_bits = max(max_bits, z.bit_length())
            for _ in range(depth):
                require((z - 89585) % (48 * 2**19) == 0, "outside direct cylinder")
                index = (z - 89585) // (48 * 2**19)
                w = 1121 + 48 * 3**8 * index
                a, b, p, r = z, 3 * z, 0, 0
                for _ in range(14):
                    require(p < 1 + r, "early grade tie")
                    p, r = p + a % 2, r + b % 2
                    a, b = step(a), step(b)
                require((a, b, p, r) == (10 + 32*w, 3 + 32*w, 8, 7), "first carry")
                require((run(z, 20)[0], run(3*z, 20)[0]) ==
                        (step(w), step(3*w)), "paired physical endpoints")
                require(w % 48 == 17 and 0 < w < z, "strict canonical return")
                z = w
                replacements += 1
            source_rows += 1
            for k in (1, 3, 23):
                for original, final in ((origin, z), (3*origin, 3*z)):
                    terminal, cost = run(original, 19*depth + k)
                    other, final_cost = run(final, k)
                    require((terminal, cost) == (other, 8*depth + final_cost), "composed transfer")
                    costs += 1
    return {"prescribed_depths": [0, 1, 2, 3, 8, 16, 32], "sources": source_rows,
            "individual_drops": replacements, "composed_comparisons": costs,
            "largest_source_bits": max_bits}


def unaligned_floor():
    rows = []
    for k in (0, 1, 4, 40, 83, 84, 85, 121):
        cofactor = (13 * pow(2 ** (14 + 2*k), -1, 81)) % 81
        if not cofactor % 2:
            cofactor += 81
        for u in (cofactor, cofactor + 162):
            numerator = 251 + 2 ** (18 + 2*k) * u
            z, rest = divmod(numerator, 27)
            require(rest == 0 and z % 48 == 17, "source integrality")
            y, upper_q = run(3*z, 5)
            x, lower_q = run(z, 5)
            require((x-y, y % 16, upper_q, lower_q) == (1, 8, 2, 3), "native alignment")
            small = 3 ** (5+k) * u
            require(run(z, 19+2*k)[0] == step(small), "bad representative")
            h, p = first_hit(3*z)
            dest, price = run(3 ** (4+k)*u, h - 18 - 2*k)
            require((dest, 6+k+price) == (1, p), "rank/clock accounting")
            require((2**40 * small < z) == (k >= 84), "floor threshold")
            rows.append([k, u, h, p])
    return {"first_hits": rows}


def mersenne_deadline():
    result = []
    for m in (11, 173, 335, 497):
        z = (2 ** (m+7) - 271) // 81
        require(81*z+271 == 2**(m+7) and z % 48 == 17, "Mersenne source")
        x, _ = run(z, 5)
        y, _ = run(3*z, 5)
        require(x == y+1 and 3*y+8 == 4*2**m, "Mersenne carry")
        tested = 0
        for e in range(y.bit_length()):
            high, v = divmod(y, 2**e)
            if high % 2 == 0:
                high -= 1
                v += 2**e
            require(high >= 1 and v+2**e*high == y, "least compatible representative")
            # Every larger compatible representative increases the lower
            # endpoint by a positive multiple of 3**odds (high-bit identity).
            endpoint, _ = run(v+1, e)
            require(endpoint > 1, "unexpected moving origin")
            tested += 1
        result.append([m, tested])
    return {"exponent_and_native_depths": result}


def inverse_envelope():
    tested = 0
    for w in range(1, 201):
        for r in range(5):
            x, q = 3**r*w, 0
            for h in range(17):
                s = 2**h*(x+1) - 3**(r+q)*w
                require(0 < s <= 2**(h-q)*3**q, "affine correction")
                i, u = 0, x+1
                while u % 3 == 0:
                    i, u = i+1, u//3
                if r+q <= i:
                    require(2**q*3**(i-q)*u <= w+1, "inverse height")
                    tested += 1
                q += x % 2
                x = step(x)
    attained = 0
    for i in range(24):
        for q in range(i+1):
            for u in range(1, 9):
                w = 2**q*3**(i-q)*u - 1
                require(run(w, q) == (3**i*u-1, q), "sharp minimum")
                attained += 1
    return {"affine_paths": 200*5*17, "admissible_envelopes": tested,
            "attained_minima": attained}


def smallest_power(x, precision):
    """Lift the exponent modulo the exact order of 2 at powers of three."""
    modulus, period = 3, 2
    clock = 0 if (517727*x - 203816) % 3 == 0 else 1
    for _ in range(1, precision):
        modulus *= 3
        options = [clock + digit*period for digit in range(3)
                   if (517727*x*pow(2, clock + digit*period, modulus) - 203816) % modulus == 0]
        require(len(options) == 1, "exponent lift is not unique")
        clock = options[0]
        period *= 3
    return clock


def fixed_component():
    numerical_entries = []
    physical = 0
    for n in (0, 1, 2, 4, 8, 16, 32):
        precision = 8*n+3
        modulus = 3**precision
        for x in (1, 5, 17, 1121):
            k = smallest_power(x, precision)
            require((517727*x*pow(2, k, modulus)-203816) % modulus == 0, "entry congruence")
            numerical_entries.append([n, x, k])
        for k in (0, 1, 5, 17):
            # Real moderate clocks, choosing the fixed input for this test
            # after the depth. The modular test above keeps each x fixed.
            x = (203816*pow(517727*2**k, -1, modulus)) % modulus + 2*modulus
            v, rem = divmod((x << k)-1, 9)
            require(rem == 0, "physical entry")
            w = 1+16*v
            require(w % 48 == 17 and w > x, "terminal height")
            final = w
            for _ in range(n):
                idx, rem = divmod(w-1121, 48*3**8)
                require(rem == 0 and idx >= 0, "required inverse rewrite")
                w = source(idx)
            require(2**(19*n)*(517727*final+40337) == 3**(8*n)*(517727*w+40337),
                    "signed rational fixed point")
            for start, result, price in ((final, x, 2), (3*final, 3**(k+1)*x-1, 2+k)):
                require(run(start, 4+k) == (result, price), "paid backtrace")
            require(run(w, 19*n+4+k) == (x, 8*n+2), "fixed component entry endpoint")
            require(run(3*w, 19*n+4+k) == (3**(k+1)*x-1, 8*n+2+k), "paired endpoint")
            physical += 1
    return {"fixed_inputs_and_least_exponents": numerical_entries,
            "constructed_both_arm_source_examples": physical}


if __name__ == "__main__":
    print(json.dumps({"moving_origins": moving_origins(), "direct_chains": direct_chains(),
                      "floor": unaligned_floor(), "missing_origins": mersenne_deadline(),
                      "inverse": inverse_envelope(), "fixed_component": fixed_component()}, indent=2, sort_keys=True))
