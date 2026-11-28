"""Compare fixed-source rational first-landing fibres to direct ordinary/native trajectories."""
from collections import Counter
from fractions import Fraction
import json
from check_line_shadow_structure import require


def odd_prefix(x,n):
    y = x
    bits = []
    grade = 0
    while grade < n:
        bit = y % 2
        bits.append(bit)
        y = (3*y+1)//2 if bit else y//2
        grade += bit
    return tuple(bits), y


def pure(n,m):
    bits = []
    h,d = n,m
    require(d % 3, "unreduced source")
    while h:
        b = d % 2
        h -= b
        bits.append(b)
        d,r = divmod(d+b*3**h,2)
        require(r == 0 and (not h or d % 3), "incorrect reduced signed evolution")
    return tuple(bits), d


def main():
    c = Counter()
    for n in range(1,8):
        q = 3**n
        sources = [(m, *pure(n,m)) for m in range(1,2*q) if m%3]
        for x in (1,2,3,7,9,13,17,27,31,41,63,73,127,255,27*2**7):
            word,z = odd_prefix(x,n)
            b = 2**len(word)
            L = Fraction(q,b)
            A = Fraction(z,1)/L - x
            require(z % 3 == 2 and A > 0, "post-odd residue or carry")
            for W in (Fraction(1,2),Fraction(1),Fraction(7,4),Fraction(2)):
                direct = {N:m for m,w,N in sources if m < W*q and w == word}
                left, right = A*L,(A+W)*L
                allowed = {N:q*x-b*(z-N) for N in range(int(left),int(right)+1)
                           if left<N<right and N%3!=2}
                require(direct == allowed, "physical real interval and root grid differ")
                require(abs(len(direct) - Fraction(2,3)*W*L) <= 2, "cohort size error")
                c["integer_window_fibres"] += 1
                c["distinct_source_terminal_checks"] += len(direct)
                c["empty_fibres"] += not direct
            for mark in (-12,-5,0,1,3,4,10,75,103):
                if mark % 3 == 2:
                    continue
                m = q*x+b*(mark-z)
                require(m % 3 and pure(n,m) == (word,mark), "signed first landing")
                c["signed_preimages"] += 1
                c["negative_rational_inputs"] += m < 0
    for d in range(2,12):
        z = 2**d - 1
        for y in range(1,z):
            a,b = y,z
            for _ in range(d):
                a = (3*a+1)//2 if a%2 else a//2
                b = (3*b+1)//2 if b%2 else b//2
                require(a < b, "premature smaller-source merger on all-odd control")
                c["ordinary_nonmerger_dates"] += 1
    print(json.dumps(dict(scope="Finite first-landing, mask, signed-preimage and nonmerger checks",
                          counts=dict(c)), sort_keys=True,indent=2))


if __name__ == "__main__":
    main()
