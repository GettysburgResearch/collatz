"""Exact ordinary inverse-window tests, including the full cost-tie question."""
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def odd_path(x, exponents):
    values = [x]
    for a in exponents:
        top = 3*x + 1
        require(a > 0 and top % (2 << a) == 1 << a, "wrong forward valuation")
        x = top >> a
        values.append(x)
    return values


def cylinder(word):
    a = carry = 0
    for e in word:
        carry = 3*carry + (1 << a)
        a += e
    modulus = 2 << a
    seed = ((1 << a)-carry) * pow(3**len(word), -1, modulus) % modulus
    return seed, modulus


def balanced_family(radius, horizon):
    # Successive integer differences of floor(i log_2 3), then ceil(i log_2 3).
    floor = [(3**i).bit_length()-1 for i in range(radius+1)]
    ceil = [0] + [i+1 for i in floor[1:]]
    fw = [b-a for a, b in zip(floor, floor[1:])]
    bw = [b-a for a, b in zip(ceil, ceil[1:])]
    ternary = 3**radius
    r = 0
    for a in reversed(bw):
        r = (3*r+1)*pow(1 << a, -1, ternary) % ternary
    x, modulus = cylinder(fw)
    s = x + ((r-x)*pow(modulus, -1, ternary) % ternary)*modulus
    stride = modulus*ternary*3**(horizon+1)
    s += modulus*ternary

    def members(u):
        back = [u]
        for a in bw:
            num = (back[-1] << a)-1
            require(num % 3 == 0, "wrong inverse cylinder")
            back.append(num//3)
        return list(reversed(back)) + odd_path(u, fw)[1:]

    base = members(s)
    plus = members(s+stride)
    inc = [b-a for a, b in zip(base, plus)]
    for x, d in zip(base, inc):
        require(s <= x < 2*s and stride <= d < 2*stride, "ordinary strip lift")
        require(d % (3**(horizon+1)) == 0, "ternary class across lifts")
    require(s % 18 == 1 and stride % 18 == 0, "integer q on each lift")
    return s, stride, base, inc, list(reversed(bw))+fw


def visit(z, dz, depth, budget, used, leaf):
    if depth == 0:
        leaf(z, dz, used)
        return
    if z % 3 == 0:
        return
    first = 1 if z % 3 == 2 else 2
    for a in range(first, budget-depth+2, 2):
        num = (z << a)-1
        require(num > 0 and num % 3 == 0 and dz % 3 == 0, "illegal predecessor")
        visit(num//3, (dz << a)//3, depth-1, budget-a, used+a, leaf)


def ordinary_windows():
    radius, horizon = 32, 24
    s, ds, values, increments, word = balanced_family(radius, horizon)
    require(s > 2*3**horizon, "uniform inverse budget")
    windows = leaves = ties = 0
    for i, (y, dy) in enumerate(zip(values, increments)):
        for k in range(1, min(i, horizon)+1):
            # If a predecessor is <=2s, the intercept estimate gives
            # 2^B < 4*3^k. This uniform cutoff also covers A+1 in this band.
            cap = (4*3**k).bit_length()-1
            native = sum(word[i-k:i])
            require(native <= cap, "native cost cap")
            best, triple = cap+1, cap+1

            def check_leaf(z, dz, clocks):
                nonlocal leaves, best, triple
                leaves += 1
                best = min(best, clocks)
                require(4*z >= 3*s+1 and 4*dz >= 3*ds, "cutoff witness")
                if z % 3 == 0:
                    triple = min(triple, clocks)
                    require(z >= 2*s+1 and dz >= 2*ds, "smaller multiple")

            visit(y, dy, k, cap, 0, check_leaf)
            require(native-2 <= best <= native, "uniform native optimum test")
            require(triple >= native-1, "multiple near-optimum test")
            if i-k == radius and k >= 3:
                require((best, triple) == (native, native+1), "exact pair at minimum")
                ties += 1
            windows += 1
    return dict(radius=radius, maximum_depth=horizon, windows=windows,
                complete_budget_leaves=leaves, exact_pairs_at_minimum=ties,
                ordinary_initial_minimum=str(s), stride=str(ds))


def forbidden():
    w = tuple(map(int, "1221212222121212121"[::-1]))
    v = tuple(map(int, "3341221111111111111"[::-1]))
    x, mx = cylinder(w)
    z, mz = cylinder(v)
    require((x, mx, z, mz) == (1686831099, 2**31, 421707775, 2**29), "cylinders")
    require(x+1 == 4*z and mx == 4*mz, "quarter identity")
    end = odd_path(x, w)[-1]
    require(end == odd_path(z, v)[-1] == 1825894037, "common endpoint")
    require(len(w) == len(v) == 19 and sum(w) == 30 and sum(v) == 28, "costs")
    require((x+mx) % 3 == 2 and (z+mz) % 3 == 0, "ternary phase")
    # Compare the width of all 20 relative backward products without logarithms.
    from fractions import Fraction
    sizes = [Fraction(1)]
    for a in map(int, "12212122221212121211"):
        sizes.append(sizes[-1]*Fraction(2**a, 3))
    require(max(sizes) < 4*min(sizes), "witness geometric width")
    return dict(binary_seed=x, multiple_row_seed=x+mx, full_stride=3*mx,
                native_reverse="".join(map(str, reversed(w))),
                rival_reverse="".join(map(str, reversed(v))),
                width_numerator=(max(sizes)/min(sizes)).numerator,
                width_denominator=(max(sizes)/min(sizes)).denominator)


def small_starts():
    longest = 0
    for start in range(1, 729):
        x = start
        steps = 0
        while x != 1 and steps < 1000:
            x = (3*x+1)//2 if x % 2 else x//2
            steps += 1
        require(x == 1, "unresolved finite start")
        longest = max(longest, steps)
    require(32*(1458+13*729+7)*3 <= 1458*729, "five-step margin at origin")
    require(32*13*3 < 1458, "positive margin slope")
    return dict(checked=728, longest_shortcut_time=longest)


if __name__ == "__main__":
    print(json.dumps(dict(small_starts=small_starts(), forbidden=forbidden(),
                          ordinary_control=ordinary_windows()), indent=2, sort_keys=True))
