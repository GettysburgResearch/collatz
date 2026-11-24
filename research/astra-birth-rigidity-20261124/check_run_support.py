"""Exact finite controls for the digit-one run bound and global count exponent."""

from fractions import Fraction as F
from itertools import product
from math import comb, log, sqrt


def require(condition, description):
    if not condition:
        raise ValueError(description)


def cubic(t):
    return t**3 - 2*t**2 - t + 1


def quintic(t):
    return t**5 + t**3 - 2*t**2 - t + 1


def log_bounds(y, terms=75):
    """Positive rational argument, enclosure from the atanh series."""
    require(y >= 1, "log argument")
    t = (y - 1) / (y + 1)
    partial = 2 * sum(t**(2*j + 1) / (2*j + 1) for j in range(terms))
    error = 2*t**(2*terms+1) / ((2*terms+1)*(1-t*t))
    return partial, partial+error


def global_exponent_check():
    root_lo, root_hi = F(55495, 100000), F(55496, 100000)
    require(cubic(root_lo) > 0 > cubic(root_hi), "cubic bracket")
    a_hi, split = F(317, 200), F(47, 40)
    require(3**200 < 2**317, "alpha upper")
    l3, _ = log_bounds(F(3))
    _, t1 = log_bounds(split)
    _, t2 = log_bounds(1 / (split-1))
    _, d = log_bounds(1 / root_lo)
    phi_upper = split*t1 + (split-1)*t2
    left = 1-split/a_hi+phi_upper/l3
    right = 1-split/a_hi+(2*(split+a_hi)/3-1)*d/l3
    require(left < F(709,1000) and right < F(709,1000), "split lanes")
    require(8*root_lo**2 > 1, "decreasing second lane")
    print("isolated cubic root in (0.55495,0.55496)")
    print("run-only split exponents < 709/1000 < 71/100")
    root_lo, root_hi = F(58457, 100000), F(58458, 100000)
    require(quintic(root_lo) > 0 > quintic(root_hi), "bounded-birth root")
    split = F(23,20)
    _, t1 = log_bounds(split)
    _, t2 = log_bounds(1 / (split-1))
    _, d = log_bounds(1 / root_lo)
    phi_upper = split*t1 + (split-1)*t2
    left = 1-split/a_hi+phi_upper/l3
    right = 1-split/a_hi+(2*(split+a_hi)/3-1)*d/l3
    require(left < F(6799,10000) and right < F(6799,10000), "birth lanes")
    require(8*root_lo**2 > 1, "decreasing birth lane")
    print("bounded-birth quintic root in (0.58457,0.58458)")
    print("bounded-birth split exponents < 6799/10000 < 17/25")


def comps(parts, total):
    if parts == 1:
        yield (total,)
        return
    for a in range(total + 1):
        for tail in comps(parts-1, total-a):
            yield (a,) + tail


def segment_lengths(w):
    start = 0
    for i, b in enumerate(w):
        if b > 1:
            yield i+1-start
            start = i+1
    yield len(w)+1-start


def coefficient_control():
    # For a component of l vertices and carry sum t>0, choose the number
    # of positive entries j and their positive composition of t.
    budget, cases = 6, 0
    for m in range(6):
        for w in product((1,2,3), repeat=m):
            pred = [1] + [0]*budget
            for length in segment_lengths(w):
                block = [1] + [
                    sum(comb(t-1,j-1) for j in range(1,min(t,length)+1))
                    for t in range(1,budget+1)
                ]
                pred = [sum(pred[t-i]*block[i] for i in range(t+1))
                        for t in range(budget+1)]
            for t in range(budget+1):
                direct = sum(all(b > 1 or v[i] > 0 or v[i+1] == 0
                                 for i,b in enumerate(w))
                             for v in comps(m+1,t))
                require(direct == pred[t], "coefficient mismatch")
                cases += 1
    print(f"finite run-polynomial coefficient equalities: {cases}")


def bounded_birth_control():
    rows = 0
    for x in (F(1,10), F(1,3), F(171,500), F(49,100)):
        D = (1-x)/(1-2*x)
        lam = 1+D*x
        def weight(c):
            return 1 if c == 0 else D*x**c
        for c in range(15):
            for b in (1,2,3):
                edge = x**c * sum(weight(v) for v in range(3*c+b))
                factor = 1+D*sum(x**j for j in range(1,b))
                require(edge <= factor*weight(c), "one-step weight bound")
                require(factor <= lam**(b-1), "digit budget")
                rows += 1
    print(f"exact bounded-birth transfer rows: {rows}")


def phase_stats(p):
    b = []
    start = p
    while True:
        pnext = 3*p
        while pnext > F(3,2):
            pnext -= 1
        b.append(int(3*p-pnext))
        p = pnext
        if p == start:
            break
    rho, beta = F(sum(a > 1 for a in b), len(b)), F(sum(b), len(b))
    return b, rho, beta


def phase_examples():
    for p, expected in [(F(7,8),[2,1]),(F(729,1456),[1]*6+[2]*5+[3])]:
        b, rho, beta = phase_stats(p)
        require(b == expected, "phase word")
        delta=(log(3)/log(2)-float(beta))/2
        e=3*delta+float(rho)
        x=2*delta/(e+sqrt(e*e-8*delta*delta))
        ent=-delta*log(x)+float(rho)*log((1-x)/(1-2*x))
        # Specified exact rational test points, not a numerical optimum.
        point = F(76858 if p == F(7,8) else 1626, 10**6)
        D = (1-point)/(1-2*point)
        l3, l3_hi = log_bounds(F(3))
        l2, _ = log_bounds(F(2))
        # Use exact power-of-two scaling before the log series near zero.
        n = (point.denominator//point.numerator).bit_length()-1
        scaled = (1/point)/(2**n)
        _, log_scaled_hi = log_bounds(scaled)
        _, log_two_hi = log_bounds(F(2))
        minus_logx_hi = log_scaled_hi+n*log_two_hi
        _, log_l2_hi = log_bounds(1+D*point)
        _, log_l3_hi = log_bounds(1+D*(point+point**2))
        cap = (l3_hi/l2-beta)/2*minus_logx_hi
        cap += F(b.count(2),len(b))*log_l2_hi+F(b.count(3),len(b))*log_l3_hi
        bound = F(736,100) if p == F(7,8) else F(18174,100)
        require(l3 > bound*cap, "phase-specific supported height")
        print(f"phase {p}, beta={beta}, rho={rho}, run-only height approx {log(3)/ent:.8f}, bounded-birth height > {bound}")


if __name__ == "__main__":
    global_exponent_check()
    coefficient_control()
    bounded_birth_control()
    phase_examples()
