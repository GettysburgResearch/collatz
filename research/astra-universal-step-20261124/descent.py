"""Exact cross-checks of the integral smoothing recurrence and powered carries."""
from fractions import Fraction as F
from itertools import product


def require(ok, message):
    if not ok:
        raise ArithmeticError(message)


def trace_constants():
    require(F(336, 100)**4 < 2**7 < F(337, 100)**4, "dyadic bounds")
    require(3**7 < F(685, 100)**4, "ternary bound")
    require(F(3, 2)**7 < F(204, 100)**4, "odd coefficient bound")
    t = F(101, 100)
    rho_bound = (F(337, 100) + F(685, 100)) * (t / F(336, 100))**2
    require(t * (1/F(336, 100) + F(204, 300)) < 1, "Haar budget")
    require(rho_bound < F(925, 1000), "core budget")
    require(2*t*F(204, 100) < F(413, 100), "flank factor")
    require(F(925, 1000)**25 * F(413, 100) < 1, "flanked budget")
    require(F(1006, 1000)**200 > 3, "interpolation factor")
    require((t / F(336, 100))*F(1006, 1000) < F(303, 1000), "interpolated ratio")
    require(rho_bound*F(1006, 1000)**2 < F(937, 1000), "interpolated core budget")
    require(F(937, 1000)**25 * F(413, 100) < F(995, 1000)**25, "interpolated flanks")
    # (1 - 1/80)^(-3/2) < 51/50, compared after squaring.
    require(F(80, 79)**3 < F(51, 50)**2, "physical correction")
    # λ_(3/2) = (sqrt(2)+sqrt(6))/4; clear both square roots.
    bound = 16 / F(51, 50)**2 - 8
    require(bound > 0 and bound**2 > 48, "strict tilt")


def profile_controls():
    # Rational branch coefficients test the affine and Haar identities independently
    # of the irrational coefficients used in the analytic estimates.
    e, o, r = F(2, 5), F(4, 5), F(7, 8)
    level = [F(1)]
    last = [F(1)]
    for depth in range(1, 6):
        q = 3**depth
        values = [1 + e * level[2*x % len(level)]
                  + (o * level[((2*x-1)//3) % len(level)] if x % 3 == 2 else 0)
                  for x in range(q)]
        weights = [F(0)] * q
        for j in range(1, depth):
            stride = 3**j
            per_residue = (1-r) * r**(j-1) / (q//stride)
            for offset in range(0, q, stride):
                weights[offset] += per_residue
        weights[0] += r**(depth-1)
        require(sum(weights) == 1, "projected probability")
        smoothed = [sum(w*values[(x+d) % q] for d, w in enumerate(weights) if w)
                    for x in range(q)]
        mean = sum(level)/len(level)
        for x, value in enumerate(smoothed):
            proposed = 1 + e * last[2*x % len(last)]
            if x % 3 == 2:
                proposed += o*(r*last[((2*x-1)//3) % len(last)] + (1-r)*mean)
            require(value == proposed, "ordinary smoothing identity")
        level, last = values, smoothed


def power_controls():
    cases = 0
    for h in range(1, 7):
        for word in product((0, 1), repeat=h):
            v, carry = 0, 0
            for i, bit in enumerate(word):
                if bit:
                    carry = 3*carry + 2**i
                    v += 1
            require(carry <= 2**(h-v)*(3**v-2**v), "ordered-carry bound")
            D = 2**h-3**v
            for copies in (2, 3):
                length = h*copies
                total = carry*(2**length-3**(v*copies))//D
                modulus = 2**length
                seed = (-total*pow(3, -v*copies, modulus)) % modulus
                for start in (seed or modulus, seed+modulus, seed+2*modulus):
                    y = start
                    for bit in word*copies:
                        require(y % 2 == bit, "physical parity")
                        y = (3*y+1)//2 if bit else y//2
                    require(2**length*(D*y-carry) == 3**(v*copies)*(D*start-carry),
                            "powered determinant identity")
                    if D*y != carry:
                        require(3**(v*copies) <= abs(D*y-carry)
                                <= 3*2**(h-v)*3**v*y, "positive endpoint bound")
                    cases += 1
    return cases


def matched_controls():
    def carry(word):
        c = 0
        for i, bit in enumerate(word):
            if bit:
                c = 3*c + 2**i
        return c

    def physical(word):
        u, H = sum(word), len(word)
        m = 2**H
        b = (-carry(word)*pow(3, -u, m)) % m + m
        z = b
        for bit in word:
            require(z % 2 == bit, "matched word realization")
            z = (3*z+1)//2 if bit else z//2
        return b, z

    distinct_pairs = absent_references = 0
    for h in range(1, 5):
        words = list(product((0, 1), repeat=h))
        for ref in words:
            v, c, Q = sum(ref), carry(ref), 2**h
            P = 3**v
            for left in words:
                if sum(left) != v or (carry(left)-c) % P:
                    continue
                b, z = physical(left+ref)
                lhs = Q**2*((Q-P)*z-c)
                rhs = P**2*((Q-P)*b-carry(left))+P*Q*(carry(left)-c)
                require(lhs == rhs and ((Q-P)*z-c) % P**2 == 0, "matched determinant")
                distinct_pairs += left != ref
            if h > 3:
                continue
            goal = carry(3*ref) % P**3
            for candidate in product((0, 1), repeat=3*h):
                if sum(candidate) != 3*v or carry(candidate) % P**3 != goal:
                    continue
                _, z = physical(candidate)
                require(((Q-P)*z-c) % P**3 == 0, "long reference transport")
                if not any(candidate[i:i+h] == ref for i in range(2*h+1)):
                    absent_references += 1
    require(distinct_pairs > 0, "need distinct matched words")
    # An explicit nonperiodic word is unnecessary to test the algebra, but the
    # reference-absent example verifies the combinatorial enlargement is strict.
    if absent_references == 0:
        from itertools import combinations
        for h in range(4, 9):
            for ref_index in range(h):
                ref = tuple(int(i == ref_index) for i in range(h))
                goal = carry(3*ref) % 27
                for inds in combinations(range(3*h), 3):
                    w = tuple(int(i in inds) for i in range(3*h))
                    if carry(w) % 27 != goal or any(w[i:i+h] == ref for i in range(2*h+1)):
                        continue
                    _, z = physical(w)
                    require(((2**h-3)*z-carry(ref)) % 27 == 0, "absent-reference example")
                    absent_references += 1
                    break
                if absent_references:
                    break
            if absent_references:
                break
    require(absent_references > 0, "need one word omitting its reference")
    require(F(303, 1000)**2 * F(1011, 100) < F(937, 1000), "pair rate")
    require(F(303, 1000)**3 * F(3033, 100) < F(85, 100), "long reference rate")
    require((1+1/(1-F(606, 1000)))*384*200**5 < 10**15, "uniform constant")
    return distinct_pairs, absent_references


if __name__ == "__main__":
    trace_constants()
    profile_controls()
    print("Exact drift and flanked-power constants, five smoothing levels,",
          power_controls(), "physical powered histories passed.")
    print("Matched distinct pairs and reference-absent samples:", matched_controls())