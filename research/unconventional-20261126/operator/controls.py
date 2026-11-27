"""Deterministic exact finite checks for the ordinary graph operator packet."""
import json
from collections import Counter
from decimal import Decimal, localcontext
from fractions import Fraction
from math import ceil


def require(truth, message):
    if not truth:
        raise RuntimeError(message)


def step(n):
    if n % 2:
        return (3 * n + 1) // 2
    return n // 2


def children(n):
    ans = [2 * n]
    if n % 3 == 2:
        ans.append((2 * n - 1) // 3)
    return ans


def unit_children(n):
    return [y for y in children(n) if y % 3]


def graph_checks():
    rows = []
    depths = [4, 5, 6, 7, 8]
    for depth in depths:
        modulus = 3 ** (depth + 1)
        counts = Counter()
        for root in range(1, modulus):
            if root % 3 == 0:
                continue
            level = [root]
            for _ in range(depth):
                level = [y for x in level for y in unit_children(x)]
            require(len(level) == len(set(level)), "equal-depth collision")
            counts[len(level)] += 1
        rows.append(dict(depth=depth, modulus=modulus, minimum=min(counts),
                         maximum=max(counts), roots=sum(counts.values())))
    require(rows[0]["minimum"] == 2, "four-step minimum")
    level = [7]
    for _ in range(3):
        level = [y for x in level for y in unit_children(x)]
    require(level == [56] and sorted(unit_children(56)) == [37, 112], "sharp depth")
    offsets = {}
    for root in (1, 2, 4, 5, 7, 8):
        cycle = [root * 2**k % 9 for k in range(6)]
        offsets[root] = dict(branch=next(k for k, x in enumerate(cycle) if x in (2, 8)),
                             attachment=cycle.index(5))
    return dict(unit_inverse_levels=rows, first_doubling_offsets=offsets)


def tagged_neighbors(n):
    return [(step(n), "out")] + [(x, "in") for x in children(n)]


def ball_signature(root, radius, modulus):
    """Return an oriented, residue-labelled rooted tree, rejecting any cycle."""
    dist = {root: 0}
    layer = [root]
    for level in range(1, radius + 1):
        upcoming = []
        for x in layer:
            for y, _ in tagged_neighbors(x):
                if y not in dist:
                    dist[y] = level
                    upcoming.append(y)
        layer = upcoming
    edge_count = sum(step(x) in dist for x in dist)
    require(edge_count + 1 == len(dist), "ball contains a directed cycle")

    def encode(x, parent):
        branches = [(tag, encode(y, x)) for y, tag in tagged_neighbors(x)
                    if y != parent and y in dist]
        return x % modulus, tuple(sorted(branches))
    return encode(root, None), len(dist)


def copies_checks():
    results = []
    for n, radius, a, b in [(27, 4, 1, 1), (45, 3, 2, 1), (19, 2, 1, 2),
                            (40, 2, 2, 0), (7, 3, 0, 2)]:
        colors = 2**a * 3**b
        marked, vertices = ball_signature(n, radius, colors)
        A, B = a + radius + 1, b + radius + 1
        m, k, q = n, 0, 0
        while k < A or m % 3 == 0:
            q += m % 2
            m = step(m)
            k += 1
        modulus = 3 ** (q + B)
        period = 2 * (modulus // 3)
        residue = 1
        exponent = 0
        while residue != m % modulus and exponent < period:
            exponent += 1
            residue = 2 * residue % modulus
        require(exponent < period, "unit discrete logarithm")
        exponent += period
        target = 1 << exponent
        root = n + (1 << k) * ((target - m) // 3**q)
        require((root - n) % (2**A * 3**B) == 0, "source cylinder")
        replay = root
        for _ in range(k):
            replay = step(replay)
        require(replay == target, "physical endpoint")
        copied, copied_size = ball_signature(root, radius, colors)
        require(copied == marked and copied_size == vertices, "labelled ball copy")
        results.append(dict(source=n, radius=radius, modulus=colors, vertices=vertices,
                            prefix_steps=k, target_power_of_two=exponent,
                            copied_root_bit_length=root.bit_length()))
    return results


def interval_grid(adic_depth, rounds, scale):
    """Enclose the infinite first-parent hitting probability on each cylinder."""
    m = 3**adic_depth
    units = [r for r in range(m) if r % 3]
    lo, hi = {r: scale // 2 for r in units}, {r: 7 * scale // 8 for r in units}
    for _ in range(rounds):
        low, high = {}, {}
        for r in units:
            even = 2 * r % m
            lower, upper = lo[even], hi[even]
            degree = 2
            if r % 9 in (2, 8):
                degree = 3
                lifts = [((2 * (r + j * m) - 1) // 3) % m for j in range(3)]
                lower += min(lo[y] for y in lifts)
                upper += max(hi[y] for y in lifts)
            denominator_lo = degree * scale - lower
            denominator_hi = degree * scale - upper
            low[r] = max(lo[r], scale**2 // denominator_lo)
            high[r] = min(hi[r], -((-scale**2) // denominator_hi))
            require(low[r] <= high[r], "empty Riccati interval")
        if lo == low and hi == high:
            break
        lo, hi = low, high
    return units, lo, hi


def log_interval(inv_ratio, terms=16):
    """Enclose log(inv_ratio), 1 <= inv_ratio <= 2, by the atanh series."""
    x = (inv_ratio - 1) / (inv_ratio + 1)
    require(0 <= x <= Fraction(1, 3), "atanh series domain")
    x2 = x*x
    power = x
    lower = Fraction()
    for j in range(terms):
        lower += 2 * power / (2*j+1)
        power *= x2
    return lower, lower + 2 * power / ((2*terms+1) * (1 - x2))


def oscillation_certificate(units, higher, scale, modulus):
    """Construct positive rational supervectors and verify every row exactly."""
    pos = {x: i for i, x in enumerate(units)}
    inverse2 = pow(2, -1, modulus)
    a = [higher[x]**2 for x in units]
    even = [pos[2*x % modulus] for x in units]
    halve = [pos[x*inverse2 % modulus] for x in units]
    odd_forward = [pos[(3*x+1)*inverse2 % modulus] for x in units]
    lifts = [[pos[((2*(x+j*modulus)-1)//3) % modulus] for j in range(3)]
             if x % 9 in (2, 8) else [] for x in units]

    def sup_rows(w):
        return [a[i]*(19*w[even[i]] + 40*max((w[j] for j in lifts[i]), default=0))
                for i in range(len(units))]

    def sum_rows(w):
        return [29*a[j]*w[j]+25*a[k]*w[k] for j,k in zip(halve, odd_forward)]

    def check(rows, denominator):
        weight_scale = 10**12
        w = [weight_scale]*len(units)
        for _ in range(160):
            new = rows(w)
            divisor = max(new)
            w = [weight_scale*y//divisor for y in new]
        require(min(w)>0, "nonpositive supervector")
        ratios = [Fraction(y, denominator*x) for x,y in zip(w, rows(w))]
        largest = max(ratios)
        require(largest<1, "failed finite oscillation supervector")
        return dict(rows=len(units), normalized_rounds=160, max_ratio_ceiling_ppm=ceil(largest*10**6))

    require(19*29**5 < 40*25**5, "one-sixth exponent comparison")
    return dict(uniform_q="19/40", sum_lambda="29/25",
                uniform=check(sup_rows,19*scale**2),
                total=check(sum_rows,29*scale**2))


def height_certificate(units, higher, scale, modulus):
    # Decimal proposes rational multipliers. The two integer power comparisons
    # independently certify which side of each algebraic number they are on.
    num, den = 9691, 25000
    multiplier_scale = 10**12
    with localcontext() as ctx:
        ctx.prec = 50
        exponent = Decimal(num)/den
        even_factor = ceil(multiplier_scale*(Decimal(2)**exponent))
        odd_factor = ceil(multiplier_scale*((Decimal(2)/3)**exponent))
    require(even_factor**den >= (2**num)*multiplier_scale**den,
            "upper approximation to the even height multiplier")
    require((3**num)*odd_factor**den >= (2**num)*multiplier_scale**den,
            "upper approximation to the odd height multiplier")

    states = {r:i for i,r in enumerate(units)}
    half = pow(2,-1,modulus)
    even = [states[r*half % modulus] for r in units]
    odd = [states[(3*r+1)*half % modulus] for r in units]
    denominator = scale*multiplier_scale
    floor_weight = 10**12
    w = [floor_weight]*len(units)

    def row(i, current):
        return higher[units[i]]*max(even_factor*current[even[i]],
                                    odd_factor*current[odd[i]])

    for iteration in range(1,2501):
        new = [max(floor_weight, -((-row(i,w))//denominator))
               for i in range(len(w))]
        if new == w:
            break
        w = new
    else:
        raise RuntimeError("height supervector search did not terminate")
    require(all(row(i,w) <= denominator*w[i] for i in range(len(w))),
            "height supervector verification")
    return dict(exponent_numerator=num, exponent_denominator=den,
                row_count=len(w), rational_multiplier_denominator=multiplier_scale,
                even_upper_numerator=even_factor, odd_upper_numerator=odd_factor,
                iterations=iteration, min_weight=min(w), max_weight=max(w))


def exponent_check():
    depth, rounds, scale, report_scale = 7, 80, 10**9, 10**8
    units, lower, upper = interval_grid(depth, rounds, scale)
    # Round individual log bounds before addition to avoid huge common denominators.
    log_lo = log_hi = 0
    for r in units:
        lo, _ = log_interval(Fraction(scale, upper[r]))
        _, hi = log_interval(Fraction(scale, lower[r]))
        log_lo += (lo * report_scale).__floor__()
        log_hi += ceil(hi * report_scale)
    average_lo = Fraction(log_lo, report_scale * len(units))
    average_hi = Fraction(log_hi, report_scale * len(units))
    ln2_lo, ln2_hi = log_interval(Fraction(2))
    exponent_lo = average_lo / ln2_hi
    exponent_hi = average_hi / ln2_lo
    outscale = 10**6
    return dict(modulus=3**depth, cylinders=len(units), iterations_at_most=rounds,
                fixed_point_scale=scale,
                h_min_lower=min(lower.values()), h_max_upper=max(upper.values()),
                widest_h_cell=max(upper[r]-lower[r] for r in units),
                oscillation_supervectors=oscillation_certificate(units, upper, scale, 3**depth),
                height_supervector=height_certificate(units, upper, scale, 3**depth),
                exponent_denominator=outscale, exponent_lower=(exponent_lo*outscale).__floor__(),
                exponent_upper=ceil(exponent_hi*outscale))


def resolvent_check():
    # z=1/2 has the exact half-line decaying root 1/2.
    z, rho = Fraction(1, 2), Fraction(1, 2)
    sample = [Fraction(5, 9) * rho**j for j in range(24)]
    for j in range(1, 23):
        require((2+z)*sample[j] == sample[j-1]+sample[j+1], "hair recurrence")
    require(sample[0]-sample[1] == (1-rho)*sample[0], "attachment admittance")
    require(rho + 1/rho == 2+z, "correct root")
    return dict(z="1/2", decaying_root="1/2", internal_equations=22)


def main():
    result = dict(graph=graph_checks(), ordinary_ball_copies=copies_checks(),
                  green_dyadic_exponent=exponent_check(), half_line=resolvent_check())
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
