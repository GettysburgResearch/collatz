"""Exact division minima at 589 and positive controls for the overhead construction."""
import json


def require(ok, label):
    if not ok:
        raise ArithmeticError(label)


def odd_step(x):
    numerator = 3*x+1
    two = numerator & -numerator
    return numerator//two, two.bit_length()-1


def path(x, q):
    exponents = []
    for _ in range(q):
        x, e = odd_step(x)
        exponents.append(e)
    return x, exponents


def depth_minima(cutoff):
    # Every finite orbit inspected here hits one or the nonperiodic anchor.
    memo = {1: None, 589: (0, 0)}
    minima = {}
    smallest = {}
    for w in range(1, cutoff+1, 2):
        x = w
        stack = []
        while x not in memo:
            xnext, e = odd_step(x)
            stack.append((x, e))
            require(len(stack) <= 1000, "finite control horizon")
            x = xnext
        endpoint = memo[x]
        for x, e in reversed(stack):
            if endpoint is not None:
                q, d = endpoint
                endpoint = (q+1, d+e)
            memo[x] = endpoint
        if endpoint is not None:
            q, d = endpoint
            minima[q] = min((d, w), minima.get(q, (d, w)))
            smallest.setdefault(q, w)
    return minima, smallest


def power_index(target, digits):
    # N=2^(11+162j), j=2(2^(18k)-1)/27. Both addresses lift one trit.
    j = k = 0
    for t in range(digits):
        step = 3**t
        mod = 3*step
        choices = [j+a*step for a in range(3)
                   if pow(2, 11+162*(j+a*step), 243*mod) == target % (243*mod)]
        require(len(choices) == 1, "unique exponent address")
        j = choices[0]
        choices = [k+a*step for a in range(3)
                   if (2*(pow(2, 18*(k+a*step), 27*mod)-1)//27-j) % mod == 0]
        require(len(choices) == 1, "unique delayed parameter address")
        k = choices[0]
    return j, k


def construction(R, d, w, smallest, cutoff):
    require(589*2**d <= cutoff*3**R, "all equal-or-lower division sources scanned")
    projected, exp = path(w, R)
    require(projected == 589 and sum(exp) == d, "minimizer ordinary path")
    wprime = w if (w+1) % 3 else 4*w+1
    anchor, adjusted = path(wprime, R)
    dprime = sum(adjusted)
    require(anchor == 589 and dprime in (d, d+2) and (wprime+1) % 3, "unit adjustment")
    p = 1
    while 3**(p+R) < 2**(p+44+d):
        p += 1
    require(3**(p-1+R) < 2**(p-1+44+d), "least budget depth")
    modulus = 3**(p+3)
    req = 11*pow(2, -p, 27)*3**p
    Q = ((req-wprime-1)*pow(2, -dprime, modulus)) % modulus
    if Q % 2:
        Q += modulus
    while 590+3**R*Q < 2**80:
        Q += 2*modulus
    require(Q % 3 and Q % 2 == 0, "exact positive shell")
    N = 590+3**R*Q
    z, rem = divmod(128*N-271, 81)
    require(rem == 0 and z % 48 == 17, "ordinary anchor chart parent")
    Y = wprime+2**dprime*Q
    c, rem = divmod(Y+1, 3**p)
    require(rem == 0 and 2**p*c % 27 == 11, "cofactor steering")
    V = 2**p*c-1
    W, rem = divmod(16*V-7, 9)
    require(rem == 0 and W > 0 and W % 48 == 17 and 2**40*W < z, "canonical subfloor")
    end, exponents = path(W, R+p+2)
    require(end == N-1 and exponents == [2, 2]+[1]*p+adjusted, "all full odd exponents")
    digits = R+p-2
    j, k = power_index(N, digits)
    return {"R": R, "minimum_divisions": d, "attaining_source": w,
            "smallest_source_at_R": smallest, "adjusted_source": wprime,
            "paid_ones": p, "total_odd_steps": R+p+2, "j": j, "k": k,
            "address_digits": digits, "ordinary_chart_N": N,
            "ordinary_chart_W": W, "ordinary_division_sum": sum(exponents)}


def main():
    x = 589
    visits = []
    while x != 1:
        require(x not in visits, "589 forward path simple")
        visits.append(x)
        x, _ = odd_step(x)
    require(len(visits) == 42, "589 first hit of one")
    cutoff = 800001
    minima, smallest = depth_minima(cutoff)
    rlist = [6, 7, 12, 18, 24, 30, 40, 50, 60]
    controls = [construction(R, *minima[R], smallest[R], cutoff) for R in rlist]
    print(json.dumps({"anchor": 589, "first_odd_hit_of_one": len(visits),
                      "ordinary_source_cutoff": cutoff, "controls": controls}, indent=2))


if __name__ == "__main__":
    main()
