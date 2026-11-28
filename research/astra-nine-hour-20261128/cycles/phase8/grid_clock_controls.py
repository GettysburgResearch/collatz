"""Exact finite checks of the rotation-clock dictionary and its local obstruction."""

from fractions import Fraction


def require(condition, message):
    if not condition:
        raise ValueError(message)


def native(y):
    raw = 3*y + 1
    low = raw & -raw
    return raw // low, low.bit_length() - 1


def log_floor(n, d):
    shift = n.bit_length() - d.bit_length()
    return shift if ((n >= d << shift) if shift >= 0 else (n << -shift >= d)) else shift - 1


def prefix(Y, a):
    return sum(log_floor(y, a) for y in Y)


def check_prefix():
    cases = 0
    for Y in [(1,), (5, 7, 11, 13, 17), (19, 25, 29, 43, 143), (35, 41, 53)]:
        ends, exps = zip(*(native(y) for y in Y))
        for a in range(1, 16*max(Y)+9):
            E = prefix(ends, 3*a) - prefix(Y, a) + sum(exps)
            digital = 0
            for y in Y:
                level = 4
                while level*y < a:
                    digital += 3*(a-level*y) <= level
                    level *= 2
            require(E == digital, "digital prefix discrepancy")
            if a <= 4*min(Y):
                require(E == 0, "early discrepancy")
            if a == 4*min(Y)+1:
                require(E == 1, "attained threshold")
            cases += 1
    print(f"{cases} actual-edge prefix identities and first positive thresholds passed.")


def forward(K, x):
    b = 1 if 3*x < 4*K else 2
    target = (3*x+(1 << b)-1) >> b
    residual = (target << b) - 3*x
    if target == 2*K:
        return K, b+1, residual
    return target, b, residual


def backward(K, x):
    b = 1 if 2*x >= 3*K else 2
    target, residual = divmod(x << b, 3)
    return target, b, residual


def eventual_clock(K, step, start=None):
    x = K if start is None else start
    history = {}
    t = total = 0
    while x not in history:
        history[x] = (t, total)
        x, b, _ = step(K, x)
        t += 1
        total += b
    t0, s0 = history[x]
    return Fraction(total - s0, t - t0)


def check_clocks():
    previous = None
    jumps = 0
    visited = set()
    for K in range(1, 2049):
        eta = eventual_clock(K, forward)
        require(eta == eventual_clock(K, backward), "nested adjoints")
        if previous is not None:
            determinant = previous.numerator*eta.denominator - previous.denominator*eta.numerator
            require(determinant in (0, 1), "adjacent Farey determinants")
            jumps += determinant
        visited.add(eta)
        if K < 36:
            for x in range(K, 2*K):
                require(eventual_clock(K, forward, x) == eta, "common forward winding")
                require(eventual_clock(K, backward, x) == eta, "common backwards winding")
        previous = eta
    require(forward(2, 3)[0] == 3 and backward(2, 2)[0] == 2 and
            forward(2, 2)[0] != 2 and backward(2, 3)[0] != 3, "disjoint support control")
    for K, ratio in ((1078, Fraction(65,41)), (1080, Fraction(474,299)),
                     (78662, Fraction(485,306)), (78663, Fraction(10754,6785))):
        require(eventual_clock(K, forward) == ratio, "convergent plateau calibration")
    for q in range(1, 42):
        a = (3**q).bit_length()
        upper = Fraction(a, q)
        best = all(upper <= Fraction((3**j).bit_length(), j) for j in range(1, q+1))
        if best:
            require(upper in visited, "best upper rational absent")
    print(f"2048 nested adjoint clocks, {jumps} strict Farey jumps, all best uppers through q=41.")
    print("Disjoint periodic supports at K=2 passed.")
    print("Exact upper-clock transitions near K=1079 and 78663 passed.")


def check_horizons():
    cases = 0
    for N in (16, 24, 40, 64, 96, 140, 200):
        angle = Fraction(7, 6)
        calendar = []
        for _ in range(N):
            b = 1 if 3*angle < 4 else 2
            angle = 3*angle/(1 << b)
            calendar.append(b)
        for mode in ("zero", "max", "alternating"):
            residuals = [(1 << b)-1 if mode == "max" or (mode == "alternating" and i % 2)
                         else 0 for i, b in enumerate(calendar)]
            numerator = 0
            B = 0
            for b, r in zip(calendar, residuals):
                numerator = 3*numerator + (r << B)
                B += b
            power = 1 << B
            x = power + (-numerator * pow(3**N, -1, power)) % power
            K = (6*x+3)//7
            for b, r in zip(calendar, residuals):
                x, actual_b, actual_r = forward(K, x)
                require((b, r) == (actual_b, actual_r), "physical horizon mismatch")
            cases += 1
    print(f"{cases} prescribed integer rounding segments through 200 dates passed.")


if __name__ == "__main__":
    check_prefix()
    check_clocks()
    check_horizons()
