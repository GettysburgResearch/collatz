"""Finite exact checks for SUBSTITUTION_SUBSHIFT_MEASURE. No asymptotics are sampled."""

from fractions import Fraction
from itertools import product
import json


def require(x, label):
    if not x:
        raise ValueError(label)


def words(n):
    return list(product((0, 1), repeat=n))


def trace(w, x, y):
    even = Fraction()
    odd = Fraction()
    end = Fraction(1)
    for bit in w:
        if bit:
            odd += end
            end *= y
        else:
            even += end
            end *= x
    return even, odd, end


def two_order(q):
    require(q != 0, "zero in a claimed nonzero valuation")
    a, b = abs(q.numerator), q.denominator
    return (a & -a).bit_length() - (b & -b).bit_length()


def substitution_checks():
    totals = dict(morphisms=0, finite_words=0, shifted_prefixes=0, leading_orders=0)
    for k in (2, 3):
        for p, q in product(words(k), repeat=2):
            if p == q:
                continue
            totals["morphisms"] += 1
            first_mismatch = next(i for i in range(k) if p[i] != q[i])
            x, y = Fraction(2), Fraction(2, 3)
            for j in range(3):
                _, u0, next_x = trace(p, x, y)
                _, u1, next_y = trace(q, x, y)
                A = u1 - u0 * (1 - next_y) / (1 - next_x)
                require(two_order(A) == first_mismatch * k**j, "first mismatch valuation")
                totals["leading_orders"] += 1
                for u in ((0,), (1,), (0, 1), (1, 0, 1), (0, 1, 1, 0)):
                    w = sum((p if a == 0 else q for a in u), ())
                    z0, z1, end = trace(u, next_x, next_y)
                    _, H, target_end = trace(w, x, y)
                    require(end == target_end, "substituted multiplier")
                    require(H == u0*z0 + u1*z1, "substituted reward")
                    require((1-next_x)*H == (1-end)*u0 +
                            ((1-next_x)*u1-(1-next_y)*u0)*z1, "eliminated scalar identity")
                    for d in range(k):
                        _, prefix_mass, prefix_scale = trace(w[:d], x, y)
                        _, tail_mass, _ = trace(w[d:], x, y)
                        require(H == prefix_mass + prefix_scale * tail_mass, "shift identity")
                        require(two_order(A/prefix_scale) == (first_mismatch-d)*k**j,
                                "shifted slope valuation")
                        totals["shifted_prefixes"] += 1
                    totals["finite_words"] += 1
                x, y = next_x, next_y
    return totals


def conjugacy_checks():
    nchecks = 0
    for n in range(1, 257):
        z, w = n, []
        for length in range(1, 14):
            bit = z % 2
            w.append(bit)
            z = (3*z+1)//2 if bit else z//2
            _, H, end = trace(w, Fraction(2), Fraction(2, 3))
            r = -H/3
            require(Fraction(n) == r + end*z, "actual physical remainder")
            require(r.denominator % 2 == 1, "unexpected binary denominator")
            require((r.numerator - n*r.denominator) % (2**length) == 0, "inverse congruence")
            nchecks += 1
    return nchecks


def support_checks():
    # A few cellular reductions for the specific support-preserving coding.
    count = 0
    for n in range(8):
        for w in words(n):
            for weight, prime in ((Fraction(3), 5), (Fraction(1, 3), 2),
                                  (Fraction(7, 5), 11), (Fraction(-3, 2), 7)):
                ones = 0
                for bit in w:
                    coeff = bit * weight**ones
                    reduced = coeff.numerator * pow(coeff.denominator, -1, prime) % prime
                    require((reduced != 0) == bool(bit), "finite-field support")
                    count += 1
                    ones += bit
    return count


if __name__ == "__main__":
    print(json.dumps(dict(substitution=substitution_checks(), actual=conjugacy_checks(),
                          support=support_checks()), indent=2, sort_keys=True))
