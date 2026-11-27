"""Replay the finite carry and physical-path claims in the cycle packet.

Use Python 3.8+; all congruences are integer operations. For huge clocks,
each edge is replayed at descending ternary precision with its full b-part.
"""
from hashlib import sha256
import json
from math import gcd


def require(test, message):
    if not test:
        raise ArithmeticError(message)


def lcm(a, b):
    return a // gcd(a, b) * b


def v3(n):
    require(n > 0, "positive valuation input")
    v = 0
    while n % 3 == 0:
        n //= 3
        v += 1
    return v


def ord2(b):
    if b == 1:
        return 1
    n, v = 1, 2 % b
    while v != 1:
        n += 1
        v = 2*v % b
    return n


def bands(q, r=1):
    layers = [(12, 25)]
    while True:
        low, high = layers[-1]
        k = 2 + len(layers)
        if high-low >= 3**(k+r)*q:
            return layers
        layers.append((3*low+8, 3*high+(high-low)//5))


def digits(n, layers):
    result = []
    for low, high in reversed(layers[:-1]):
        gap = max(1, n-3*high)
        start = (gap-1).bit_length()
        for e in range(start, start+4):
            value = 1 << e
            if (n-value) % 3 == 0 and (n-value) % 9 != 0:
                tail = (n-value)//3
                if low <= tail <= high:
                    result.append(e)
                    n = tail
                    break
        else:
            raise ArithmeticError("digit selection")
    for a in range(9):
        for b in range(9):
            if n == (1 << a) + 3*((1 << b)+3):
                return result + [a, b, 0]
    raise ArithmeticError("terminal carry")


def lift_at_least(residue, low, modulus):
    return low + (residue-low) % modulus


def path_exponents(raw, period, clock_residue=0):
    cumulative = [0]
    for digit in reversed(raw[:-1]):
        cumulative.append(lift_at_least(digit, cumulative[-1]+2, period))
    cumulative.append(lift_at_least(clock_residue, cumulative[-1]+2, period))
    return list(reversed([y-x for x, y in zip(cumulative, cumulative[1:])]))


def step(value, e, d, modulus):
    scaled = (pow(2, e, modulus)*value-d) % modulus
    require(scaled % 3 == 0, "illegal inverse edge")
    return scaled//3


def replay(y, d, b, es, a, v, r=1):
    # An independently restarted replay retains exactly the requested
    # b residue and one remaining ternary digit after every division.
    modulus = b*3**(len(es)+r)
    value = y % modulus
    for e in es:
        require(e >= 2 and value % 3, "invalid guarded edge")
        value = step(value, e, d, modulus)
        modulus //= 3
    require(value % b == a % b and value % 3**r == v % 3**r, "final congruence")
    if sum(es) > 40000:
        return None
    actual = y
    for e in es:
        prev, rem = divmod((actual << e)-d, 3)
        require(rem == 0 and prev >= actual and prev % 2, "integer inverse")
        f = 3*prev+d
        exponent = (f & -f).bit_length()-1
        require(exponent == e and (f >> exponent) == actual, "forward replay")
        actual = prev
    require(actual % (3**r*b) == value, "integer/modular disagreement")
    return actual.bit_length()


def route(y, d, b, a, *, unit=1, two_period=None, r=1, total=None,
          with_word=False):
    require(min(d, y, b) >= 1 and gcd(y, 6) == gcd(d, 6) == gcd(b, 6) == 1
            and y >= d and r >= 1, "initial data")
    g = gcd(d, b)
    q = b//g
    layers = bands(q, r)
    k = len(layers)+2
    pk = 3**k
    L = lcm(lcm(6, two_period or ord2(b)), 2*3**r)
    if total is None:
        total = 4*L*k
    clock_residue = total % L
    head_b = pow(2, clock_residue, b)*y % b
    require((head_b-pk*a) % g == 0, "ineligible residue")
    u = 3**r*pk
    mod_q = ((head_b-pk*a)//g*pow(d//g, -1, q)) % q if q > 1 else 0
    mod_u = ((pow(2, clock_residue, u)*y-pk*unit)*pow(d, -1, u)) % u
    residue = mod_q + q*((mod_u-mod_q)*pow(q, -1, u) % u)
    low, high = layers[-1]
    carry = lift_at_least(residue, low, q*u)
    require(low <= carry <= high and carry % 3, "CRT band")
    raw = digits(carry, layers)
    check_carry = 0
    for j in reversed(raw):
        check_carry = (1 << j) + 3*check_carry
    require(check_carry == carry and len(raw) == k, "free carry representation")
    require(pow(2, L, b) == 1 % b, "false binary period")
    virtual = path_exponents(raw, lcm(L, 2*3**(k+r-1)), clock_residue)
    t = 1 + v3(L)
    precision = 3**t
    require(pow(2, L, precision*3) in (precision+1, 2*precision+1),
            "digit freedom")
    modulus = b * 3**(k+t+1)
    actual = shadow = y % modulus
    compressed = []
    for exponent in virtual:
        shadow = step(shadow, exponent, d, modulus)
        first = lift_at_least(exponent, 2, L)
        for e in (first, first+L, first+2*L):
            value = step(actual, e, d, modulus)
            if (value-shadow) % (b*precision) == 0:
                actual = value
                compressed.append(e)
                break
        else:
            raise ArithmeticError("ternary precision repair")
        modulus //= 3
    extra = total-sum(compressed)
    require(extra >= 0 and extra % L == 0, "common clock")
    compressed[-1] += extra
    bit_length = replay(y, d, b, compressed, a, unit, r)
    details = {
        "odd_depth": k, "shortcut_clock": total, "binary_period": L,
        "final_residue": a % b, "final_unit": unit,
        "source_bits_if_materialized": bit_length,
        "exponent_sha256": sha256(json.dumps(compressed, separators=(",", ":"))
                                  .encode()).hexdigest(),
    }
    return (details, compressed) if with_word else details


def all_residues(y, d, b):
    g = gcd(d, b)
    k = len(bands(b//g))+2
    eligible = [a for a in range(b) if (3**k*a-y) % g == 0]
    clocks = set()
    bits = []
    digest = sha256()
    for unit in (1, 2):
        for a in eligible:
            witness = route(y, d, b, a, unit=unit)
            clocks.add(witness["shortcut_clock"])
            if witness["source_bits_if_materialized"] is not None:
                bits.append(witness["source_bits_if_materialized"])
            digest.update(bytes.fromhex(witness["exponent_sha256"]))
    require(len(eligible) == b//g and len(clocks) == 1, "fiber cardinality")
    return {"root": y, "d": d, "b": b, "fiber_size": len(eligible),
            "reachable_at_both_ternary_units": 2*len(eligible),
            "odd_depth": k, "common_shortcut_clock": clocks.pop(),
            "sources_replayed_as_integers": len(bits),
            "source_bit_range": [min(bits), max(bits)] if bits else None,
            "all_exponent_lists_sha256": digest.hexdigest()}


def mixed_modulus(y, s, t, b):
    modulus = (2**s)*(3**t)*b
    j = max(1, s)
    r = j+t
    k_prefix = len(bands(b, r))+2
    L = lcm(lcm(6, ord2(b)), 2*3**r)
    suffixes = []
    for n in range(1, 2*modulus, 2):
        if any(n % modulus == old[0] % modulus for old in suffixes):
            continue
        v = n
        forward = []
        for _ in range(j):
            f = 3*v+1
            e = (f & -f).bit_length()-1
            v = f >> e
            forward.append(e)
        suffixes.append((n, v, list(reversed(forward))))
    common = (3*L+1)*k_prefix+max(sum(es) for _, _, es in suffixes)+7
    k = k_prefix+j
    largest = 0
    digest = sha256()
    for E in (common, common+1):
        for n, v, suffix in suffixes:
            _, prefix = route(y, 1, b, v % b, unit=v % 3**r, r=r,
                              total=E-sum(suffix), with_word=True)
            es = prefix+suffix
            require(sum(es) == E and len(es) == k, "mixed common grade")
            actual = y
            for e in es:
                actual, remainder = divmod((actual << e)-1, 3)
                require(remainder == 0 and actual >= 1 and actual % 2,
                        "mixed physical edge")
            require(actual % modulus == n % modulus, "all-prime class")
            largest = max(largest, actual.bit_length())
            digest.update(json.dumps(es, separators=(",", ":")).encode())
    return {"root": y, "modulus": modulus, "admissible_classes": len(suffixes),
            "odd_depth": k, "two_consecutive_clocks": [common, common+1],
            "materialized_paths": 2*len(suffixes), "largest_source_bits": largest,
            "all_exponent_lists_sha256": digest.hexdigest()}


def true_step(n, d=1):
    return n//2 if n % 2 == 0 else (3*n+d)//2


def small_cycle_labels(d, xs):
    """Classify each requested ray by an actual repeated odd state."""
    cycle = set(xs)
    terminal_minima = set()
    checked = 0

    def bad(n):
        nonlocal checked
        checked += 1
        while n % 2 == 0:
            n //= 2
        seq, seen = [], {}
        while n not in seen and n not in cycle:
            seen[n] = len(seq)
            seq.append(n)
            f = 3*n+d
            n = f//(f & -f)
        if n in cycle:
            return True
        terminal_minima.add(min(seq[seen[n]:]))
        return False

    exps = []
    qs = []
    for j, x in enumerate(xs):
        f = 3*x+d
        e = (f & -f).bit_length()-1
        exps.append(e)
        require(e in (1, 2) and f >> e == xs[(j+1) % len(xs)], "native rational cycle")
        for z in (x-d, x+d, 2*x-d):
            require(z > 0 and not bad(z), "rational good neighbor")
        if (2*x+d) % 3 == 0:
            q = (2*x+d)//3
            require(not bad(q) and bad(3*q), "rational unit-packet labels")
            qs.append(q)
    for q, qnext in zip(qs, qs[1:]+qs[:1]):
        f = 3*q+d
        e = (f & -f).bit_length()-1
        base = f >> e
        require(e >= 2 and 3**(e-2)*base == qnext, "rational packet cocycle")
        require(all(not bad(3**j*base) for j in range(e-1)), "rational good tripling tower")
    return {"denominator": d, "minimum_numerator": min(xs), "odd_period": len(xs),
            "native_exponents": exps, "all_neighbor_labels_checked": 3*len(xs),
            "disagreement_numerators": qs, "actual_label_queries": checked,
            "distinct_good_terminal_minima": sorted(terminal_minima)}


def full_lap_floor(d, S, exponents):
    """Check the first entrance below S on any reverse word of up to one lap."""
    xs, x = [], S
    for e in exponents:
        xs.append(x)
        f = 3*x+d
        require((f & -f) == 1 << e, "full-lap native valuation")
        x = f >> e
    require(x == S and min(xs) == S and 2*S > d, "full-lap root")
    visits = 0

    def visit(y, depth, budget):
        nonlocal visits
        visits += 1
        require(y >= S, "first subminimum rational ancestor")
        if depth == 0 or y % 3 == 0:
            return
        first = 1 if (2*y-d) % 3 == 0 else 2
        for e in range(first, budget-depth+2, 2):
            z = ((y << e)-d)//3
            if z > 0:
                visit(z, depth-1, budget-e)

    for k in range(1, len(xs)+1):
        upper = S*(6*S)**k
        for y in xs:
            lower = y*(2*S-d)**k
            # The budget has strict inequality, as the possible source is <S.
            budget = max(0, upper.bit_length()-lower.bit_length()+1)
            while budget > 0 and (lower << budget) >= upper:
                budget -= 1
            visit(y, k, budget)
    return {"all_endpoint_depth_pairs": len(xs)**2, "visited_nodes": visits,
            "no_positive_ancestor_below_minimum": True}


def clipped_basin(S, d, xs, factor):
    ceiling = factor*S
    layer = set(xs)
    visited = set(xs)
    least_triple = None
    nonempty_layers = 0
    while layer:
        following = set()
        nonempty_layers += 1
        for y in layer:
            if y % 3 == 0:
                least_triple = y if least_triple is None else min(y, least_triple)
                continue
            e = 1 if (2*y-d) % 3 == 0 else 2
            z = ((y << e)-d)//3
            while z <= ceiling:
                if z > 0 and z not in visited:
                    visited.add(z)
                    following.add(z)
                # Advancing e by 2 adds the next legal numerator exactly.
                z = 4*z+d
        layer = following
    require(min(visited) == S and least_triple == 2*S+d, "clipped global floors")
    return {"ceiling_as_multiple_of_minimum": factor, "closed_odd_numerators": len(visited),
            "nonempty_breadth_first_layers": nonempty_layers,
            "least_source": min(visited), "least_multiple_of_three": least_triple}


def holonomy_controls():
    checked = 0
    samples = []
    for d in (1, 13, 25, 1631, 44835377399):
        for y in (1, 5, 7, 655, 10865, 29340952507853):
            if gcd(d, y) != 1:
                continue
            e = 8
            while (1 << e)*y <= 85*d or (pow(2, e, 27)*y-31*d) % 27:
                e += 1
            roots = []
            for word in ((e-4, 3, 1), (e-6, 4, 2)):
                n = y
                for j in word:
                    n, rem = divmod((n << j)-d, 3)
                    require(not rem and n > 0 and n % 2, "physical twin edge")
                roots.append(n)
            require(roots[0]-roots[1] == 2*d, "primitive translation")
            checked += 1
            if y == 1:
                samples.append([d, e])
    return {"physical_twins": checked, "small_terminal_clock_by_d": samples}


def minimum_control():
    # The constructive path to a multiple of three works in any component.
    # Each chosen reduction here is checked by an actual common forward value.
    count = 0
    max_odd_clock = max_factor = 0
    for n in range(2, 20000):
        if not n % 2 or n % 3 != 1:
            continue
        u = n+1
        m = (u & -u).bit_length()-1
        b = u >> m
        R = 3**m*b
        partner = (n-1)//2 if R % 4 == 1 else 2*n+1
        rhs = 0
        x, y = n, partner
        seen = {x}
        for _ in range(m+4):
            x = true_step(x)
            seen.add(x)
        while y not in seen and rhs <= m+4:
            y = true_step(y)
            rhs += 1
        require(y in seen and (partner < n or partner % 3 == 0), "ordinary run witness")
        count += 1
        max_odd_clock = max(max_odd_clock, m)
        max_factor = max(max_factor, partner)
    return {"odd_one_mod_three_starts": count, "largest_initial_odd_run": max_odd_clock,
            "largest_partner_tested": max_factor}


def main():
    # Round 13's 41-phase real/rational strip control.
    D = 2**65-3**41
    d = 44835377399
    y = 29340952507853
    factors = [19, 29, 17021, d]
    factor_product = binary_period = 1
    for f in factors:
        factor_product *= f
        binary_period = lcm(binary_period, f-1)
    require(factor_product == D and pow(2, binary_period, D) == 1,
            "41-phase binary period")
    rational_k = len(bands(D//d))+2
    accessible = y*pow(3, -rational_k, d) % d
    require(D % d == 0 and gcd(d, y) == 1 and accessible != 0, "rational obstruction")
    p41_word = list(map(int, "12112121212211222212212121221122212211222"))
    p41_xs = []
    value = y
    for exponent in p41_word:
        p41_xs.append(value)
        value = (3*value+d) >> exponent
    require(value == y, "41-phase list")
    return {
        "small_fibers": [all_residues(*example) for example in
                         [(1, 1, 1), (655, 1, 13), (283, 13, 13),
                          (283, 13, 65), (73, 25, 125), (655, 1, 31)]],
        "mersenne_composite": route(655, 1, 511, 123),
        "mixed_modulus": mixed_modulus(655, 2, 1, 5),
        "native_floor_p41": full_lap_floor(d, y, p41_word),
        "height_clipped_basin_p41": clipped_basin(y, d, p41_xs, 100000),
        "rational_neighbor_labels": [
            small_cycle_labels(13, [283, 431, 653, 493, 373]),
            small_cycle_labels(1631, [10865, 17113, 26485, 40543, 30815, 23519, 18047, 13943]),
            small_cycle_labels(d, p41_xs)],
        "relative_holonomy": holonomy_controls(),
        "ordinary_floor_witnesses": minimum_control(),
        "full_determinant": {"D": D, "p": 41, "h": 65,
            "nearby_ordinary_root": 655, "zero_reached":
            route(655, 1, D, 0, two_period=binary_period),
            "rational_numerator": y, "reduced_denominator": d,
            "zero_excluded_all_depths_by_gcd": gcd(y, d) == 1 and d > 1,
            "eligible_nonzero_example": route(y, d, D, accessible, two_period=binary_period)},
    }


if __name__ == "__main__":
    print(json.dumps(main(), sort_keys=True, indent=2))
