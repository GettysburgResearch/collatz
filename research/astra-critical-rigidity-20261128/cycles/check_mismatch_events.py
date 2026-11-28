"""Exact post-mismatch window multiplicity, endpoint and height-area controls."""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import prod
import json

from check_rotation_occupation import lifted, primitive_necklace, require


def verify(w, q, y, lag, counts):
    p = len(w)
    marks = [t for t in range(p) if w[(t-1)%p] != w[(t+lag-1)%p]]
    s = len(marks)
    require(s>0,"primitive pair has a mismatch")
    weights = [(y[t]+q)*(y[(t+lag)%p]+q) for t in marks]
    event_product = prod(weights)
    m = min(y)
    area = prod(Fraction(z,m) for z in y)
    require(event_product <= (m+q)**(2*s)*area**2, "exact multiplicative area ledger")
    counts["paired_rotations"] += 1
    for k in sorted({1,2,3,s,s+1,2*s+3}):
        length = 0
        payments = 1
        for i,b in enumerate(marks):
            n,j = divmod(i+k,s)
            c = n*p + marks[j]
            mismatch = sum(w[t%p]!=w[(t+lag)%p] for t in range(b,c))
            require(c>b and mismatch==k, "exact mismatch count on actual open paths")
            length += c-b
            payments *= max(y[b],y[(b+lag)%p])+q
            payments *= min(y[c%p],y[(c+lag)%p])+q
            counts["actual_open_windows"] += 1
            counts["windows_longer_than_one_lap"] += c-b>p
        require(length==k*p and payments==event_product,
                "native window lengths and all endpoint weights telescope")
        counts["summed_window_systems"] += 1


def main():
    counts = Counter()
    for p in range(2,7):
        for w in product((1,2,3), repeat=p):
            if not primitive_necklace(w):
                continue
            src=lifted(w)
            if src is None:
                continue
            q,y=src
            counts["primitive_rational_cycles"] += 1
            counts["proper_nontrivial_denominator_cancellations"] += 1<q<2**sum(w)-3**p
            for lag in range(1,p):
                verify(w,q,y,lag,counts)
    require(len(counts)==6 and all(counts.values()), "all finite control regimes exercised")
    return dict(counts)


if __name__=="__main__":
    print(json.dumps(main(),indent=2,sort_keys=True))
