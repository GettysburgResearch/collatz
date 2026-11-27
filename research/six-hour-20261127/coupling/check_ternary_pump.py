"""Ternary addresses, ordinary prefix checks and exact source-density accounting."""
import json
from fractions import Fraction


def require(condition, label):
    if not condition:
        raise ArithmeticError(label)


def lift_digits(length, accepts):
    value, stride = 0, 1
    for depth in range(1, length + 1):
        candidates = [value + digit*stride for digit in range(3)]
        accepted = [x for x in candidates if accepts(x, depth)]
        require(len(accepted) == 1, "unique next trit")
        value, stride = accepted[0], 3*stride
    return value


def power_class(goal, digits):
    return lift_digits(digits, lambda j, depth:
                       (pow(2, 17+162*j, 3**(depth+5))-goal) % 3**(depth+5) == 0)


def delayed_class(j, digits):
    def accepts(k, depth):
        modulus = 3**depth
        numerator = 2*(pow(2, 18*k, 27*modulus)-1)
        q, rem = divmod(numerator, 27)
        return rem == 0 and (q-j) % modulus == 0
    return lift_digits(digits, accepts)


def trace(x, clocks):
    odds = 0
    for _ in range(clocks):
        if x % 2:
            x = (3*x+1)//2
            odds += 1
        else:
            x //= 2
    return x, odds


def literal(s, j):
    m = 11+162*j
    N = 2**m
    B, rem = divmod(64*N-95, 3**s)
    require(rem == 0 and B % 3 and (2**(s+1)*B) % 27 == 14, "ordinary ternary unit")
    w, rem = divmod(2**(s+1)*B-23, 9)
    z, zrem = divmod(128*N-271, 81)
    V = 2**(s-3)*B-1
    require(rem == zrem == 0 and 0 < w < z and w % 48 == 17, "ordinary canonical source")
    require(trace(w, 4) == (V, 2), "ordinary lower entrance")
    require(trace(w, s) == (z, s-2), "ordinary parent return")
    require(trace(w, s+7) == (N-1, s+2), "ordinary Mersenne join")
    require(trace(3*w, s+14) == (2**(m-7)+1, s+1), "ordinary upper turn")
    terminal = 3**((m-7)//2)+1
    require(2**40*terminal < z, "literal positive upper below floor")
    full_upper = m <= 9000
    if full_upper:
        require(trace(3*w, s+14+m-7) == (terminal, s+1+(m-7)//2), "full upper trajectory")
    return {"s": s, "j": j, "m": m, "lower_clocks_to_parent": s,
            "lower_clocks_to_mersenne": s+7, "lower_odds_to_mersenne": s+2,
            "upper_clocks_to_turn": s+14, "upper_odds_to_turn": s+1,
            "upper_final_bits": terminal.bit_length(), "full_upper_iteration": full_upper}


def main():
    rows = []
    finite = Fraction()
    for s in range(6, 73):
        B0 = (14*pow(2, -s-1, 27)) % 27
        digits = s-2
        goal = 95+3**s*B0
        j = power_class(goal, digits)
        k = delayed_class(j, digits)
        modulus = 3**digits
        require(pow(2, 17+162*j, 3**(s+3)) == goal % 3**(s+3), "final power address")
        closed_j = 2*(pow(2, 18*k, 27*modulus)-1)//27
        require((closed_j-j) % modulus == 0, "final delayed address")
        rows.append({"s": s, "unit_mod_27": B0, "ternary_digits": digits, "j": j, "k": k})
        finite += Fraction(1, modulus)
    require((rows[0]["j"], rows[0]["k"]) == (50, 64), "rank-eight specialization")
    deep_j = power_class(95, 68)
    deep_k = delayed_class(deep_j, 68)
    for row in rows:
        for col, deep in [("j", deep_j), ("k", deep_k)]:
            require((row[col]-deep) % 3**min(row["ternary_digits"], 68) != 0,
                    "deep ball disjoint")
            for other in rows[:row["s"]-6]:
                require((row[col]-other[col]) % 3**other["ternary_digits"] != 0,
                        "distinct shells disjoint")
    density = finite+Fraction(1, 3**68)
    require(density == Fraction(1, 54)+Fraction(17, 18*3**68), "exact combined density")
    require(2**40*2**69 < 3**69 and 2**40*2**68 >= 3**68, "sharp whole-shift depth")
    require(1024*2**4 < 243*3**4 and 1024*2**3 >= 243*3**3, "cycle-floor threshold")
    samples = [literal(row["s"], row["j"]) for row in rows[:3]]
    print(json.dumps({"canonical_shells": rows, "deep_shell": {"s_at_least": 73,
                      "ternary_digits": 68, "j": deep_j, "k": deep_k},
                      "density": [density.numerator, density.denominator],
                      "ordinary_prefix_controls": samples}, indent=2))


if __name__ == "__main__":
    main()
