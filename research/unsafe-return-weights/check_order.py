"""Exact linear synchronizer and order-scale guarded merger replays."""
from pathlib import Path
import runpy

base = runpy.run_path(str(Path(__file__).with_name("check_mergers.py")))
crt, rank, component, word_data, require, step = (
    base[name] for name in ("crt", "rank", "component", "word_data", "require", "step")
)


def synchronized_words(d, offset):
    left, right = [], []
    bound = abs(offset)+3**d
    initial_d = d

    def append(x, y):
        left.extend(x)
        right.extend(y)

    while d:
        power = 3**d
        valuation = ((power-1) & -(power-1)).bit_length()-1
        if offset % (1 << (valuation+1)) == 0:
            append("1", "1")
            offset = (3*offset+1-power)//2
        while offset % 2 == 0:
            append("0", "0")
            offset //= 2
        append("0", "1")
        offset = (offset-power//3)//2
        d -= 1
    require(2*len(left) <= 7*initial_d, "exponent phase exceeds linear budget")
    positive = offset >= 0
    gap = abs(offset)
    while gap:
        if gap % 2 == 0:
            lower, upper, gap = "0", "0", gap//2
        elif gap == 1:
            lower, upper, gap = "001", "100", 0
        elif gap % 4 == 1:
            lower, upper, gap = "10", "01", (3*gap+1)//4
        else:
            lower, upper, gap = "01", "10", (3*gap-1)//4
        append(upper, lower) if positive else append(lower, upper)
    require(len(left) <= 7*initial_d//2+6*bound.bit_length()+3, "word budget")
    return "".join(left), "".join(right)


def prefix(n, length):
    q = c = 0
    for i in range(length):
        if n % 2:
            c = 3*c + 2**i
            q += 1
        n = step(n)
    return n, q, c


def order_scale(a, order):
    d = 3**a-2**(a+1)
    c = 3**a-2**a
    generator = 3*pow(2, -1, d) % d
    require(pow(generator, order, d) == 1, "order multiple failed")
    z = order
    prime = 2
    while prime*prime <= z:
        if z % prime == 0:
            require(pow(generator, order//prime, d) != 1, "nonminimal order")
            while z % prime == 0:
                z //= prime
        prime += 1
    if z > 1:
        require(pow(generator, order//z, d) != 1, "nonminimal final order factor")
    j = order % (a+1)
    p = (order+a*j)//(a+1)
    h = 10*(p+a)+10
    power = 3**h
    n0 = crt(1, 8, ((power-c)*pow(d, -1, 3*power)) % (3*power), 3*power)
    stride = 8*3*power
    b, rb = divmod((3**p-2**j)*c, d)
    require(rb == 0, "nonintegral centered intercept")
    m0, rm = divmod(2**j*n0-b, 3**p)
    require(rm == 0, "nonintegral companion")
    big, qn, cn = prefix(n0, 3)
    small, qm, cm = prefix(m0, 3+j)
    gap_power = p+qn-qm
    offset = big-3**gap_power*small
    require(offset * 2**(3+j) == 3**qn*b + 2**j*cn - 3**gap_power*cm, "offset")
    left, right = synchronized_words(gap_power, offset)
    _, _, y_residue = word_data(right)
    modulus = 2**len(right)
    small_slope = 3**(h+1-p+qm)
    lift = ((y_residue-small)*pow(small_slope, -1, modulus)) % modulus
    n = n0 + stride*(lift+modulus)
    m = (2**j*n-b)//3**p
    yn = prefix(n, 3)[0]
    ym = prefix(m, 3+j)[0]
    end_n = base["replay"](yn, left)[-1] if left else yn
    end_m = base["replay"](ym, right)[-1] if right else ym
    require(end_n == end_m and rank(m) < rank(n), "ordinary merger")
    require(rank(n) == component(n, a) and rank(base["module"](n)[0]) > rank(n), "initial unsafe")
    cap = (order-1)//(2*a+1)
    require(3**h > 1000*d**3*27**cap and cap < 3+j+len(right), "lower clock guard")
    return cap, 3+j+len(right)


def main():
    for d in range(12):
        for b in (0, -1, 11, 2**(d+3), -2**(d+2)):
            w, v = synchronized_words(d, b)
            _, _, residue = word_data(v)
            y = residue + 2**len(v)*(abs(b)+2)
            require(prefix(3**d*y+b, len(w))[0] == prefix(y, len(v))[0], "affine compiler control")
    for a, order in ((5, 178), (7, 1930), (8, 1441), (9, 9108)):
        low, high = order_scale(a, order)
        print(f"a={a}, order={order}, every lower clock >{low}, actual merger clock {high}")


if __name__ == "__main__":
    main()
