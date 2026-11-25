"""Exact paths accepted by finite inverse tests in the ideal rotation model."""
from fractions import Fraction
from functools import lru_cache
import numpy as np

K = 17
H = 90
# Saturation leaves headroom for adding two predecessor counts in uint64.
CAP = 2 * 3**(H//3)
WIDTH = Fraction(16,3)
MARGIN = Fraction(1001,1000)


def norm(x):
    while x < 1:
        x *= 2
    while x >= 2:
        x /= 2
    return x


def cost_thresholds():
    """Exact necessary lower x/s from all affordable ancestors in two families."""
    counts = 1 << K
    lower = [Fraction(1)]*counts
    for offset, floor in ((1,Fraction(2)), (0,Fraction(3,4))):
        for k in range(1,K+1-offset):
            # x equals the forward image of zero modulo 3^(k+offset)
            # when the depth-k start is arbitrary (offset 0) or a multiple of 3.
            precision = k+offset
            modulus = 3**precision
            top = int(floor*3**k).bit_length()-1
            if top < k:
                continue
            inverses = [pow(2,-a,modulus) for a in range(max(3,top+1))]
            cheapest = {}
            def generate(x, length, extra):
                if not length:
                    cost = top-extra
                    cheapest[x] = min(cheapest.get(x,cost), cost)
                    return
                for e in range(extra+1):
                    y = (3*x+1)*inverses[1+e] % modulus
                    generate(y,length-1,extra-e)
            generate(0,k,top-k)
            residues = [0]
            for _ in range(precision):
                residues = [(3*x+1)*inverses[a]%modulus for x in residues for a in (1,2)]
            for i,x in enumerate(residues):
                if x in cheapest:
                    threshold = floor*3**k / 2**cheapest[x]
                    for z in range(i,counts,1<<precision):
                        lower[z] = max(lower[z],threshold)
    values = sorted(set(lower))
    lookup = {value:i for i,value in enumerate(values)}
    return values, np.array([lookup[value] for value in lower],dtype=np.int16)


def canonical_past(z):
    digits = []
    for _ in range(K):
        old = norm(z/3)
        gap = 1 if 3*old < 4 else 2
        digits.append(gap-1)
        z = old
    word = 0
    for bit in reversed(digits):
        word = 2*word + bit
    return word


def main():
    from bisect import bisect_right
    vals, ix = cost_thresholds()
    half = 1<<(K-1)
    @lru_cache(None)
    def guards(lo, hi):
        return tuple(bisect_right(vals, lo*2**j / MARGIN)-1
                     if hi*2**j * MARGIN <= WIDTH else -1 for j in range(3))
    def count(left, right):
        z = (left + right)/2
        lo_ratio, hi_ratio = left/z, right/z
        D = np.zeros((3,2*half), dtype=np.uint64)
        start = canonical_past(z)
        if ix[start] > guards(z*lo_ratio, z*hi_ratio)[1]:
            return 0
        D[1,start] = 1
        for i in range(1,H+1):
            b = 1 if 3*z < 4 else 2
            z = 3*z / 2**b
            E = np.zeros_like(D)
            for jnew,cut in enumerate(guards(z*lo_ratio, z*hi_ratio)):
                if cut < 0 or (i > H-K-1 and jnew != 1):
                    continue
                for a in (1,2):
                    jold = jnew+a-b
                    if 0 <= jold <= 2:
                        E[jnew,a-1::2] = np.minimum(D[jold,:half]+D[jold,half:], CAP)
                E[jnew,ix>cut] = 0
            D = E
        return int(D[1,canonical_past(z)])
    # The gap b and canonical suffix are constant over each half-open cell.
    # Use its worst-case lower and upper heights at every time in that cell.
    cuts = sorted({Fraction(1), Fraction(2)} |
                  {norm(Fraction(3)**d) for d in range(-H-2,K+3)})
    minimum = min(count(left,right) for left,right in zip(cuts,cuts[1:]))
    print(f"K={K}, H={H}, {len(cuts)-1} phase intervals, "
          f"minimum capped count={minimum}, cube-root threshold={3**(H//3)}")
    if minimum < CAP:
        raise ValueError("the capped count did not exceed the entropy target")


if __name__ == "__main__":
    main()
