"""Construct finite witnesses for WR-1 and verify selected WR-2 certificates."""
from itertools import product


def require(condition, label):
    if not condition:
        raise ValueError(label)


def step(n):
    return (3*n+1)//2 if n % 2 else n//2


def trace(n, length):
    bits = []
    for _ in range(length):
        bits.append(n % 2)
        n = step(n)
    return tuple(bits), n


def affine(word):
    carry = 0
    for i, bit in enumerate(word):
        carry = 3**bit * carry + (bit << i)
    return sum(word), carry


def dyadic_log(target, m):
    """Solve 2^D = target modulo 3^m by lifting one ternary digit."""
    exponent = int(target % 3 == 2)
    modulus = 3
    period = 2
    for _ in range(1, m):
        modulus *= 3
        choices = [exponent+i*period for i in range(3)
                   if pow(2, exponent+i*period, modulus) == target % modulus]
        require(len(choices) == 1, "unique ternary lift")
        exponent, = choices
        period *= 3
    return exponent, period


def certificate(q, lower_word, extra):
    h = len(lower_word)
    p, carry = affine(lower_word)
    low_u = -carry*pow(3**p, -1, 1 << h) % (1 << h)
    tmod = (2*low_u+1)*pow(3**q, -1, 1 << (h+1)) % (1 << (h+1))
    prefix, _ = trace(tmod, h+1)
    tail_word = prefix + (1,)*extra
    rank, carry = affine(tail_word)
    d = len(tail_word)
    c = 1648*pow(2, -(q+7), 243) % 243
    rhs = carry + 3**rank*c
    exponent, period = dyadic_log(rhs, rank+5)
    floor = max(d+2, carry.bit_length()+2, (3**rank).bit_length()+d+2)
    exponent += max(0, (floor-exponent+period-1)//period)*period
    require(pow(2, exponent, 3**(rank+5)) == rhs % 3**(rank+5), "upper endpoint")
    require((3**rank*tmod+carry) % (1 << (h+1)) == 0, "upper dyadic class")
    require(trace(low_u, h)[0] == lower_word, "lower dyadic class")
    require(pow(2, q+7, 243)*c % 243 == 1648 % 243, "source residue")
    return exponent, carry, d, rank, tail_word


def literal(q, lower_word, data):
    exponent, carry, d, rank, upper_word = data
    t, remainder = divmod((1 << exponent)-carry, 3**rank)
    require(remainder == 0 and t % 2 == 1, "terminal integer")
    z, remainder = divmod((t << (q+7))-271, 81)
    require(remainder == 0 and z % 48 == 17, "source integer")
    path, lower = trace(z, 7)
    require(lower+1 == t << q, "lower take-off")
    path, lower = trace(lower, q)
    require(path == (1,)*q and lower+1 == 3**q*t, "lower ascent")
    require(trace(step(lower), len(lower_word))[0] == lower_word, "specified word")
    path, upper = trace(3*z, q+7)
    require(sum(path) == 3 and upper == t, "three-odd upper macro")
    path, endpoint = trace(t, d)
    require(path == upper_word and endpoint == 1 << (exponent-d), "terminal power")
    first_odds = 0
    upper = 3*z
    clock = 0
    while upper != 1:
        first_odds += upper % 2
        upper = step(upper)
        clock += 1
        require(clock <= q+7+exponent, "missed first hit")
    require(clock == q+7+exponent and first_odds == 3+rank, "first-hit rank")


def main():
    cases = direct = 0
    largest_literal_clock = 0
    for q in range(2, 7):
        for h in range(5):
            for w in product((0, 1), repeat=h):
                for extra in range(4):
                    data = certificate(q, w, extra)
                    cases += 1
                    if data[0] <= 6000:
                        literal(q, w, data)
                        direct += 1
                        largest_literal_clock = max(largest_literal_clock, q+7+data[0])
    print(f"{cases} exact congruence constructions; {direct} complete literal first hits;"
          f" longest literal first hit {largest_literal_clock}")
    count = 0
    for q in (2, 7, 11):
        for a in range(5):
            for w in product((0, 1), repeat=a):
                combined = w + (0,)*(q+40+a)
                rank = q+44+2*a
                forced = 3+certificate(q, combined, 0)[3]
                require(forced <= rank, "uniform exact-rank threshold")
                data = certificate(q, combined, rank-forced)
                require(3+data[3] == rank, "dense progression rank")
                count += 1
    print(f"{count} symbolic dense-descent certificates at the uniform rank cutoff")
    for q in (2, 3, 7, 11, 17, 32):
        h = q+40
        data = certificate(q, (0,)*h, 0)
        print(f"all-even q={q}, length={h}, upper rank={data[3]+3},"
              f" terminal power exponent={data[0]-data[2]} (congruence construction)")


if __name__ == "__main__":
    main()
