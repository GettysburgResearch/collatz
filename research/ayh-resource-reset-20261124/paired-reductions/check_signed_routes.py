"""Replay the complete affine rows and the finite signed-anchor census."""
from fractions import Fraction
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent


def require(test, message):
    if not test:
        raise ValueError(message)


def signed_word(x, clocks):
    odd_count = 0
    x = Fraction(x)
    for _ in range(clocks):
        require(x.denominator % 2 == 1, "even signed denominator")
        odd = x.numerator % 2
        x = (3*x+1)/2 if odd else x/2
        odd_count += odd
    return x, odd_count


def cycles():
    seen = set()
    for base in [0, 1, -1, -5, -17]:
        s = base
        while s not in seen:
            seen.add(s)
            s = int(signed_word(s, 1)[0])
        require(s == base, "cycle phase")
    require(max(map(abs, seen)) == 136, "cycle radius")
    return seen


def finite_anchor_census():
    points = cycles()
    surviving = []
    for h in range(12):
        r = (-271 * pow(81, -1, 2**h)) % (2**h)
        endpoint, odds = signed_word(r, h)
        for wanted in points:
            quotient = (wanted-endpoint) / 3**odds
            if quotient.denominator != 1:
                continue
            a = r + 2**h * int(quotient)
            require(signed_word(a, h)[0] == wanted, "anchor inversion")
            if signed_word(3*a, h)[0] in points:
                surviving.append((h,a))
    require(surviving == [(0,0), (4,1), (5,1)], "integer reference census")
    return surviving


def rational_queries():
    source = (HERE / "MersenneTwoCenter.lean").read_text()
    data = [tuple(map(int, match)) for match in re.findall(
        r"\| (?:\d+|_) => ⟨(\d+), (\d+), (\d+), (\d+), (\d+), (\d+)⟩", source)]
    require(len(data) == 13, "number of query rows")
    covered = set()
    for first, period, den, numerator, h, residue in data:
        a = Fraction(-numerator, den)
        low, low_odds = signed_word(a, h)
        high, high_odds = signed_word(3*a, h+2)
        require(low == -1 and 3**low_odds == den, "signed lower query")
        require(high == 0 and 3**(high_odds+1) == den, "signed upper query")
        mod = 48*den
        power = pow(2, 9+162*first, mod)
        require(power == residue and pow(2, 162*period, mod)*power % mod == power,
                "exponent period")
        W = 2**(h+2)
        require((W*power - numerator) % den == 0, "nonintegral query")
        w0 = (W*power-numerator) // den
        require(w0 > 0 and w0%48 == 17, "query base")
        z0, remainder = divmod(512*power-271, 81)
        require(remainder == 0 and z0%48 == 17 and w0 < z0, "parent base")
        require(81*W < 512*den and mod%81 == 0, "strict slope drop")
        require(signed_word(w0, h)[0] == signed_word(z0, 7)[0] == 4*power-1,
                "ordinary base lower clock")
        require(signed_word(3*w0, h+2)[0] == power, "ordinary base upper clock")
        members = set(range(first, 19683, period))
        require(members.isdisjoint(covered), "overlapping parameter rows")
        covered.update(members)
    require(len(covered) == 17, "distinct exponent classes")
    return len(data), len(covered)


def trace(a, b, word):
    for move in word:
        if move == "D":
            a, b = 2*a, 2*b
        elif move == "E":
            require(a%2 == b%2 == 0, "even branch")
            a, b = a//2, b//2
        elif move == "O":
            require(a%2 == 0 and b%2 == 1, "odd branch")
            a, b = 3*a//2, (3*b+1)//2
        elif move == "I":
            require(a%3 == 0 and b%3 == 2, "inverse branch")
            a, b = 2*a//3, (2*b-1)//3
        else:
            raise ValueError(f"unknown move {move}")
    return a,b


def guarded_rows():
    source = (HERE / "GuardedResidueCover.lean").read_text()
    data = re.findall(r'⟨\((\d+),(\d+)\),\((\d+),(\d+)\),"([DEOI]*)","([DEOI]*)",(true|false)⟩', source)
    require(len(data) == 16, "guarded bank length")
    covered, guarded = set(), set()
    for mod, r, a, b, head, tail, direct in data:
        mod, r, a, b = map(int, (mod, r, a, b))
        require(trace(mod, r, head) == (a,b), "left walk")
        members = set(range(r, 12288, mod))
        require(12288%mod == 0 and members.isdisjoint(covered), "source rows")
        if direct == "true":
            require((a,b) == (3*mod,3*r) and not tail, "ordinary terminal")
        else:
            require(a%48 == 0 and b%48 == 17 and a<=mod and 0<b<r, "query guard")
            require(trace(3*a,3*b,tail) == (3*mod,3*r), "right walk")
            guarded.update(members)
        covered.update(members)
    require(len(covered) == 55 and len(guarded) == 13, "guarded census")
    return len(covered), len(guarded)


if __name__ == "__main__":
    print("Small-horizon simultaneous signed anchors:", finite_anchor_census())
    print("Different rational-center rows, classes modulo 19683:", rational_queries())
    print("All-rank residue classes, classes using a smaller tripling:", guarded_rows())
