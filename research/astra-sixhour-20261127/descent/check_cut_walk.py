"""Realize the shifted-charge criterion by positive, slope-controlled cut walks."""
from fractions import Fraction
from json import dumps


def require(test, reason):
    if not test:
        raise ValueError(reason)


def hitting_word(x):
    out = []
    while x != 1 and len(out) < 20000:
        op = "O" if x % 2 else "E"
        out.append(op)
        x = (3*x+1)//2 if op == "O" else x//2
    require(x == 1, "finite control did not converge in its stated clock budget")
    return "".join(out)


def shifted(z):
    low, high = hitting_word(z), hitting_word(3*z)
    return len(low)-2*low.count("O")-len(high)+2*high.count("O")+2


def reverse(word):
    return word[::-1].translate(str.maketrans("EO", "DI"))


def slope(word):
    return (word.count("D")+word.count("I")-word.count("E")-word.count("O"),
            word.count("O")-word.count("I")+word.count("J"))


def coefficient(a, b):
    return Fraction(2)**a*Fraction(3)**b


def cost_sum(z):
    need = shifted(z)
    odd_seed = need % 2
    even_need = (need-15*odd_seed)//2
    negative_seeds = max(0, (-even_need+5)//6)
    positive_seeds = even_need+6*negative_seeds
    queries = [17]*positive_seeds+[65]*odd_seed+[161]*negative_seeds
    require(sum(shifted(v) for v in queries) == need, "failed charge sum")
    return queries


def design(z):
    require(z > 161 and z % 48 == 17, "canonical control required")
    queries = cost_sum(z)
    word = hitting_word(z)
    for seed in queries:
        approach = reverse(hitting_word(seed))
        a, b = slope(word+approach)
        k = 0
        while coefficient(a-2*k, b+k) >= 1:
            k += 1
        word += "OE"*k+approach+"J"+hitting_word(3*seed)+"DI"*k
    finish = reverse(hitting_word(3*z))
    a, b = slope(word+finish)
    require(a+2*b == 2, "remaining slope is not a cycle power")
    correction = b-1
    word += ("DI"*correction if correction >= 0 else "OE"*(-correction))+finish
    require(slope(word) == (0, 1), "wrong final slope")
    a = b = amin = bmin = 0
    for op in word:
        if op == "J":
            require(coefficient(a, b) < 1, "query does not stay below original cut")
        da, db = slope(op)
        a += da
        b += db
        amin = min(amin, a)
        bmin = min(bmin, b)
    return word, queries, (4-amin, 1-bmin)


def physical(word, z):
    x = z
    jumps = []
    for op in word:
        if op == "O":
            require(x % 2 == 1, "wrong forward odd branch")
            x = (3*x+1)//2
        elif op == "E":
            require(x % 2 == 0, "wrong forward even branch")
            x //= 2
        elif op == "D":
            x *= 2
        elif op == "I":
            require((2*x-1) % 3 == 0, "wrong odd inverse")
            x = (2*x-1)//3
            require(x % 2 == 1, "inverse did not reach odd input")
        else:
            require(op == "J" and x % 48 == 17 and x < z, "illegal cut jump")
            jumps.append(x)
            x *= 3
        require(x > 0, "nonpositive physical site")
    require(x == 3*z, "wrong physical endpoint")
    return jumps


def main():
    require([shifted(n) for n in (17, 65, 161)] == [2, 15, -12], "seed charges")
    rows = []
    for z in (209, 257, 353, 545, 833, 1025, 4913, 12305):
        word, queries, (a, b) = design(z)
        require(physical(word, z) == queries, "wrong seed queries")
        modulus = 2**a*3**b
        for t in (1, 3, 81):
            physical(word, z+t*modulus)
        rows.append({"z": z, "shifted_charge": shifted(z), "jumps": len(queries),
                     "ordinary_clocks": len(word)-len(queries), "modulus_v2": a,
                     "modulus_v3": b, "actual_positive_lifts_checked": 3})
    print(dumps({"controls": rows}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
