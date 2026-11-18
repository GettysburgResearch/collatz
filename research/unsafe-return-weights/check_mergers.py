"""Finite physical replay of the precision-gated repayment and merger formulas."""
from fractions import Fraction
from itertools import product
from pathlib import Path
import runpy

base = Path(__file__).resolve().parents[2]
source = runpy.run_path(str(base / "experiments/X-ASTRA3-005-spectrum-switch/run.py"))
rank, component, step, module = (source[name] for name in ("rank", "ra", "step", "module"))


def require(value, message):
    if not value:
        raise ValueError(message)


def word_data(word):
    q = c = 0
    for i, bit in enumerate(word):
        if bit == "1":
            c = 3*c + 2**i
            q += 1
    modulus = 2**len(word)
    return q, c, (-c * pow(3**q, -1, modulus)) % modulus


def replay(n, word):
    path = []
    for bit in word:
        require(n % 2 == int(bit), "illegal physical word")
        n = step(n)
        path.append(n)
    return path


def crt(a, m, b, n):
    return a + m * ((b-a)*pow(m, -1, n) % n)


def aligned_controls():
    cases = 0
    for a in range(9):
        d, c = 3**a - 2**(a+1), 3**a - 2**a
        aligned = "1"*a + "0"
        words = ["".join(w) for w in product("01", repeat=7)] + [aligned, aligned*2]
        for word in words:
            t = len(word)
            q, offset, residue = word_data(word)
            h = 110
            power = 3**h
            # z_a(n) = 3^h modulo 3^(h+1) fixes the exact component valuation.
            ternary = ((power - c)*pow(d, -1, 3*power)) % (3*power)
            n = crt(residue, 2**t, ternary, 3*power) + 2**t * 3*power
            require(component(n, a) == rank(n), "tested component is not minimal")
            require(power > 200*abs(d)**3 * 8**t, "wrong precision guard")
            y = replay(n, word)[-1]
            require(y == (3**q*n + offset)//2**t, "word formula mismatch")
            lowers = t % len(aligned) == 0 and word == aligned*(t//len(aligned))
            require((rank(y) < rank(n)) if lowers else (rank(y) > rank(n)),
                    "misclassified early repayment")
            cases += 1
    return cases


def two_sided_controls():
    classes = set()
    checked = 0
    max_clock = 4
    for a in range(4):
        d, c = 3**a - 2**(a+1), 3**a - 2**a
        power = 3**65
        require(power > 1000*abs(d)**3 * 27**max_clock, "wrong merger guard")
        ternary = ((power-c)*pow(d, -1, 3*power)) % (3*power)
        for residue in range(2**max_clock):
            n = crt(residue, 2**max_clock, ternary, 3*power) + 2**max_clock * 3*power
            require(rank(n) == component(n, a), "wrong source rank")
            y = n
            v = ""
            for t in range(max_clock+1):
                qv, cv, _ = word_data(v)
                virtual_y = (3**qv * Fraction(-c, d) + cv) / 2**t
                for s in range(max_clock+1):
                    for bits in product("01", repeat=s):
                        w = "".join(bits)
                        qw, cw, wr = word_data(w)
                        m, remainder = divmod(2**s*y-cw, 3**qw)
                        if remainder or m <= 1 or m % 2**s != wr or rank(m) >= rank(n):
                            continue
                        checked += 1
                        eta = (2**s * virtual_y-cw) / 3**qw
                        hm = source["vp"](2*m+1, 3)
                        for b in {0, 1, 2, hm}:
                            if component(m, b) != rank(m):
                                continue
                            db, cb = 3**b - 2**(b+1), 3**b - 2**b
                            if eta == Fraction(-cb, db):
                                classes.add("aligned")
                                ratio = Fraction(db, d)**2 * Fraction(4)**(s-t) * Fraction(3)**(qv-qw)
                                require(ratio == Fraction(rank(m), rank(n)), "wrong aligned ratio")
                            else:
                                require(eta == Fraction(-1, 2) and b == hm, "third merger class")
                                classes.add("half")
                v += str(y % 2)
                y = step(y)
    require("aligned" in classes, "missing exact-alignment witness")
    return checked


def moving_family(h, extra, good):
    word = "111111101100001101"
    other = "1111101110111100"
    tail = word + "1"*extra
    _, _, residue = word_data(tail)
    power = 3**h
    dyadic = 2**(len(tail)-1)
    u2 = (residue-1)//2 * pow(power, -1, dyadic) % dyadic
    d = power - 2**(h+1)
    ternary = power**2 if good else 3
    u3 = (-1 if good else 1) * pow(d, -1, ternary) % ternary
    u = crt(u2, dyadic, u3, ternary) + dyadic * ternary
    n, m = 1+2*power*u, (power*u-1)//2
    require(3**h > 1000*27**18, "two-source precision too small")
    path = replay(n, tail)
    require(path[17] == replay(m, other)[-1], "physical arms fail to merge")
    require(min(path) > n and m < n//4+1, "wrong numerical guard")
    require(rank(module(n)[0]) > rank(n) and module(n)[1:] == (7, 1, 8), "unsafe guard")
    require(rank(n) == 4*power*u*u, "source rank formula")
    if good:
        require(rank(m) == component(m, h) and 16*rank(m) <= rank(n), "uncertified rank drop")
    else:
        require(rank(m) > rank(n), "missing precision rejection")


def main():
    cases = aligned_controls()
    pairs = two_sided_controls()
    for h in (120, 147):
        for extra in (0, 37):
            for good in (True, False):
                moving_family(h, extra, good)
    print(f"{cases} physical forward comparisons; {pairs} small-clock lower mergers; "
          "8 moving-index examples and wrong-residue controls.")


if __name__ == "__main__":
    main()
