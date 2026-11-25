"""Physical small-source audit and exact modular lifting for the -17 pump."""

from fractions import Fraction


def require(ok, label):
    if not ok:
        raise ValueError(label)


def step(x):
    return (3 * x + 1) // 2 if x % 2 else x // 2


def rational_orbit(x, steps):
    odds = 0
    for _ in range(steps):
        odd = x.numerator % 2
        odds += odd
        x = (3 * x + 1) / 2 if odd else x / 2
    return x, odds


def check_small():
    hits = []
    peak = longest = 0
    for w in range(17, 3236, 48):
        x, h, p = w, 0, 0
        while x != 1:
            peak = max(peak, x)
            for r in (11, 12):
                if 3**r - 2**(r-11) <= x < 3**r:
                    hits.append((w, h, p, r))
            h, p, x = h + 1, p + (x & 1), step(x)
            require(h <= 107, 'small path timeout')
        longest = max(longest, h)
    require(peak == 638468 and longest == 107, 'small trajectories')
    require(hits == [(3233, 18, 15, 11)], 'cutoff trap')
    print('Small audit: 68 ordinary inputs, maximum clock 107, maximum height 638468,',
          'unique trap (3233,18,15,11).')


def check_anchors():
    c = Fraction(-2399, 81)
    b = Fraction(-2692031, 531441)
    require(c-b == Fraction(-13047808, 3**12), 'center separation')
    require(rational_orbit(c, 7) == (-17, 4), 'lower entry')
    require(rational_orbit(3*c, 7) == (-55, 4), 'upper entry')
    for phase in (-17, -55):
        require(rational_orbit(Fraction(phase), 11) == (phase, 7), 'period')
    require(rational_orbit(b, 18) == (-1, 12), 'lower exit')
    require(rational_orbit(3*b, 20) == (0, 11), 'upper exit')
    for n in range(17):
        bn = c + Fraction(2048, 2187)**n * (b-c)
        require(bn.denominator == 3**(12+7*n), 'reduced denominator')
        require(rational_orbit(bn, 18+11*n) == (-1, 12+7*n), 'pumped lower exit')
        require(rational_orbit(3*bn, 20+11*n) == (0, 11+7*n), 'pumped upper exit')
    print('Signed anchors and two arms checked at lap counts 0 through 16.')


def lift_residue(n):
    digits = 8 + 7*n
    modulus = 3**(digits+5)
    rhs = pow(2, -11*n, modulus) * 3**digits * 2561 - 13047808
    require(pow(2, 29, 243) == rhs % 243, 'entry at five ternary digits')
    m, stride, mod = 0, 1, 243
    for _ in range(digits):
        mod *= 3
        matches = [m + i*stride for i in range(3)
                   if pow(2, 29 + 162*(m+i*stride), mod) == rhs % mod]
        require(len(matches) == 1, 'one ternary lift')
        m, stride = matches[0], 3*stride
    require(pow(2, 162*stride, modulus) == 1, 'period')
    for index in [m, m+stride, m+2*stride]:
        base = pow(2, 29 + 162*index, modulus)
        num = pow(2, 11*n, modulus)*(base + 13047808) - 2399*3**digits
        require(num % modulus == 2*3**(12+7*n), 'necessary and sufficient ternary residue')
        require((base + 13047808) % (3**(digits+1)) in (3**digits, 2*3**digits),
                'exact valuation')
    return m, stride


def physical(m, n):
    exponent = 11 + 162*m
    power = 1 << exponent
    z, rem = divmod(128*power - 271, 81)
    require(rem == 0, 'parent integrality')
    w, rem = divmod(2**(11*n) * (2**18 * power + 13047808)
                    - 2399*3**(8+7*n), 3**(12+7*n))
    require(rem == 0 and w % 48 == 17 and 0 < w < z, 'ordinary source')
    x, odds = w, 0
    for _ in range(18+11*n):
        odds, x = odds + x % 2, step(x)
    require(x == power - 1 and odds == 12+7*n, 'ordinary lower trace')
    y, odds = 3*w, 0
    for _ in range(20+11*n):
        odds, y = odds + y % 2, step(y)
    require(y == power//4 and odds == 11+7*n, 'ordinary upper trace')


def main():
    check_small()
    check_anchors()
    old = {5903, 5903+6561, 5903+13122, 1286, 1286+6561, 1286+13122,
           2258, 11889, 44, 1124, 1529, 5174, 13347, 1502, 12221, 2582, 2987}
    for n in range(17):
        m, stride = lift_residue(n)
        if n:
            require(m % 19683 == 3122 and (m % 19683) not in old, 'new progression')
        if n <= 3:
            print(f'Lap count {n}: m = {m} mod {stride}.')
        if n <= 1:
            physical(m, n)
    print('17 parameter lifts, three representatives per lift, and complete positive',
          'merger traces for lap counts 0 and 1.')


if __name__ == '__main__':
    main()
