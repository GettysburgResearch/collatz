"""Exact scalar consequences of Wren's reported W22 minimum slack."""
from fractions import Fraction as Q


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def log_unit(x, terms=42):
    """Rational lower/upper bounds for 1 <= x <= 2."""
    require(1 <= x <= 2, "log_unit domain")
    z = (x - 1) / (x + 1)
    base = sum(2 * z ** (2*j+1) / (2*j+1) for j in range(terms))
    return base, base + 2*z**(2*terms+1)/((2*terms+1)*(1-z*z))


def log_bounds(x):
    require(x >= 1, "log_bounds domain")
    k = 0
    while x >= 2:
        x /= 2
        k += 1
    lo, hi = log_unit(x)
    l2, u2 = log_unit(Q(2))
    return lo+k*l2, hi+k*u2


def main():
    D = 10**6
    old = Q(569908, D)
    theta = old + Q(90000000, 3*D*D)
    span = Q(13537636, D)
    require(theta == Q(569938, D), "scaled slack")
    require(int(span/theta)+1 == 24, "regrouped cap")
    # Check all genuine reduced unit transitions modulo nine.
    for s in [1, 2, 4, 5, 7, 8]:
        legal = [e for e in range(1,25) if (2**e*s-1) % 9 in [3, 6]]
        require(len(legal) == 8, "number of alternatives")
        for base in legal:
            alternatives = [e for e in legal if e != base]
            best = min(alternatives)
            require(best <= 6, "small alternate")
            average = Q(999,1000)*best + Q(sum(alternatives),1000*len(alternatives))
            require(average <= Q(3009,500), "alternate mean")
    l2, u2 = log_bounds(Q(2))
    l3, u3 = log_bounds(Q(3))
    for denom, coefficient, count in [(575000,Q(373,25),Q(1,4750)),
                                      (100000,Q(149,10),Q(1,950))]:
        e = Q(1,denom)
        A = (1-e+e*span)/theta + Q(3009,500)*e
        g_lo, g_hi = A*l2-u3, A*u2-l3
        entropy_lo = e*log_bounds(1/e)[0] + (1-e)*log_bounds(1/(1-e))[0]
        require(g_lo > 0 and A > coefficient*g_hi, "coefficient margin")
        require(entropy_lo > count*g_hi, "count exponent margin")
        print(f"epsilon=1/{denom} c={coefficient} eta={count} "
              f"A={A} coefficient_margin>1e-6:{A-coefficient*g_hi > Q(1,10**6)} "
              f"entropy_margin>1e-8:{entropy_lo-count*g_hi > Q(1,10**8)}")
    print("scaled theta=284969/500000; 48 cap-24 baseline/row alternatives checked")


if __name__ == "__main__":
    main()
