"""Exact geometric ternary source overlap at rational tilts, no word cutoff."""
from fractions import Fraction

from check_window_transfer import log_bounds


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def next_level(previous, old_den, p, q):
    old = len(previous)
    modulus = 3*old
    period = 2*old
    tail = q-p
    orbit = [1]
    for _ in range(1,period):
        orbit.append(2*orbit[-1] % modulus)
    require(2*orbit[-1]%modulus == 1 and len(set(orbit)) == period, "unit orbit")
    values = [previous[(x-1)//3] if x%3 == 1 else 0 for x in orbit]
    K = q**period-tail**period
    first, weight = 0, 1
    for e in range(period,0,-1):
        first = tail*first + p*weight*values[e%period]
        weight *= q
    current = [0]*modulus
    z = first
    for d in range(period-1,-1,-1):
        z,res = divmod(tail*z + p*K*values[(d+1)%period], q)
        require(res == 0, "common denominator recurrence")
        current[orbit[d]] = z
    den = old_den*K
    require(z == first and sum(current) == den, "normalization")
    for i,numer in enumerate(previous):
        require(sum(current[i::old]) == numer*K, "projection")
    if old <= 27:
        for j,x in enumerate(orbit):
            num = sum(p*tail**(e-1)*q**(period-e)*values[(j+e)%period]
                      for e in range(1,period+1))
            require(current[x] == num, "direct finite geometric sum")
    return current,den


def main():
    near = Fraction(609089768,10**9)
    for end,sign in [(near-Fraction(1,10**9),1),(near,-1)]:
        a,b = log_bounds(1/end)
        c,d = log_bounds(1/(1-end))
        lo,hi = log_bounds(Fraction(3))
        if sign == 1:
            require(a+(1-end)*c/end > hi, "critical lower parameter bound")
        else:
            require(b+(1-end)*d/end < lo, "critical upper parameter bound")
    for p,q in [(3,5),(609089768,10**9),(2,3)]:
        # The middle row is a stated rational parameter near, but unequal to,
        # the implicit definition of the entropy-critical tilt.
        cells,den = [1],1
        prev = Fraction(1)
        for k in range(1,8):
            cells,den = next_level(cells,den,p,q)
            m = len(cells)
            overlap = Fraction(sum(min(m*c,den) for c in cells),m*den)
            require(0 < overlap <= prev, "overlap refinement")
            if k in [3,5,7]:
                ppm = (10**6*overlap.numerator)//overlap.denominator
                print(f"theta={p}/{q} depth={k} Haar overlap in [{ppm},{ppm+1}]/1000000")
            if Fraction(p,q) == near and k == 7:
                radius = Fraction(k,600000000)
                require(overlap-radius > Fraction(33384,100000), "true critical finite lower")
                print("true entropy-critical depth-seven Haar overlap >33384/100000")
            prev = overlap


if __name__ == "__main__":
    main()
