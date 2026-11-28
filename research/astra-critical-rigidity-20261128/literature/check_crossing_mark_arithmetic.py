"""Check the exact inputs to the prime-power bounds, including high-level windows."""

from collections import Counter, defaultdict
from fractions import Fraction
import sys

sys.dont_write_bytecode = True
from check_ordered_crossings import words


def verify(condition, explanation):
    if not condition:
        raise ArithmeticError(explanation)


def valuation(n, prime):
    verify(n != 0, "valuation of a nonzero integer")
    n = abs(n)
    count = 0
    while n % prime == 0:
        n //= prime
        count += 1
    return count


def trajectory(x, y, g, h, length, stats):
    records = []
    for _ in range(length):
        j = abs(g-h)
        a, b = x.numerator % 2, y.numerator % 2
        xx, yy = (3**a*x+a)/2, (3**b*y+b)/2
        gg, hh = g+a, h+b
        # Keep one orientation through both endpoints of each step.
        direction = 1 if (g>h or (g==h and gg>=hh)) else -1

        def determinant(X, Y, G, H):
            return direction*(3**max(G-H,0)*Y-3**max(H-G,0)*X)

        u, v = determinant(x,y,g,h), determinant(xx,yy,gg,hh)
        verify(u.denominator == v.denominator == 1, "integral oriented endpoints")
        if not (u and v):
            break
        u, v = int(u), int(v)
        c = max(gg,hh)-max(g,h)
        kind = "even"
        if a!=b:
            kind = "out" if abs(gg-hh)>j else "in"
        elif a:
            kind = "double" if j else "tie"
        high = j-1 if kind=="in" else j if kind=="double" else None
        low = int(kind in ("out","double"))
        impulse = (3**high if high is not None else 0)-low
        verify(2*v==3**c*u+impulse, "physical signed recurrence")
        if j:
            verify(u%3!=0, "ternary unit at positive level")
            if u>0:
                verify(v>0, "positive excursion suffix persists")
            if high is not None:
                if 9*abs(u)<3**j and u<0:
                    verify(v>0, "negative to positive at small magnitude")
                    stats["negative_to_positive"] += 1
                if u>0:
                    verify((3**c*u+impulse)*9 >= 3**c*max(u,3**j),
                           "positive step deficit lower inequality")
        records.append((j,u,v,c,high,low,kind,direction))
        x,y,g,h = xx,yy,gg,hh
    return records


def check_windows(records, stats, group):
    marks = [i for i,row in enumerate(records) if row[4] is not None or row[5]]
    for index,s in enumerate(marks):
        j = records[s][0]
        if records[s][4] is None:
            continue
        for m in (1,2,3,5,8):
            if j<=m+2:
                continue
            emax=marks[index+m] if index+m<len(marks) else len(records)
            # Compare all native endpoints through the first unprocessed mark.
            for e in range(s+1,emax+1):
                d=e-s
                slice_=records[s:e]
                h=sum(row[3] for row in slice_)
                verify(h<=m, "slope paid by marks only")
                verify(all(row[7]==slice_[0][7] for row in slice_), "fixed sign")
                last_index=0
                P=Q=0
                for k,row in enumerate(slice_):
                    remaining=sum(item[3] for item in slice_[k+1:])
                    if row[4] is not None:
                        power=row[4]+remaining-(j-m-1)
                        verify(0<=power<=3*m+2,"separated ternary powers")
                        P+=2**k*3**power
                        last_index=k
                    if row[5]:
                        Q+=2**k*3**remaining
                        last_index=k
                verify(P>0 and Q>=0, "same sign high/low grouping")
                verify(max(P,Q)<=m*2**last_index*3**(3*m+2),
                       "moving coefficient height uses only last included mark")
                u,v=slice_[0][1],slice_[-1][2]
                N=3**(j-m-1)*P-Q
                verify(2**d*v-3**h*u==N, "full collapsed equation")
                for prime in (2,5,7,11):
                    modulus=prime**min(valuation(u,prime),valuation(v,prime))
                    verify(N%modulus==0, "joint endpoint valuation")
                verify(N%2**min(d,valuation(u,2))==0, "one-point dyadic guard")
                if Q:
                    ratio=Fraction(3**(j-m-1)*P,Q)
                    error=ratio-1
                    if error:
                        verify(valuation(error.numerator,2)-valuation(error.denominator,2)
                               == valuation(N,2)-valuation(Q,2), "moving-quotient loss")
                stats[group+"_short_windows"]+=1
                stats["zero_low_group" if not Q else "nonzero_low_group"]+=1
                if u<0:
                    stats["negative_start_windows"]+=1
                stats["largest_positive_level_checked"]=max(stats["largest_positive_level_checked"],j)


def main():
    stats=Counter()
    for L in range(1,16):
        bygrade=defaultdict(dict)
        for positions,carry in words(L):
            bygrade[len(positions)][carry]=positions
        for p,bycarry in bygrade.items():
            D=2**L-3**p
            for cu in bycarry:
                cv=cu-D
                if cv in bycarry:
                    rows=trajectory(Fraction(cu,D),Fraction(cv,D),0,0,L,stats)
                    verify(len(rows)==L,"closed pair never merges")
                    check_windows(rows,stats,"closed")
                    stats["closed_adjacent_pairs"]+=1
    # Both choices of the leading arm, with signed unit determinants and
    # positive physical integer states. The input grades are open-window data.
    for j in (7,17,61,107):
        for x0,y0 in ((37,5),(5,37),(1,1),(19,17),(2**31-1,11)):
            for x in (x0,3**j*(y0+1)+x0,3**j*y0+1,3**j*y0+2**83):
                if x%3==0:
                    continue
                for swap in (False,True):
                    args=(x,y0,j,0) if not swap else (y0,x,0,j)
                    rows=trajectory(Fraction(args[0]),Fraction(args[1]),*args[2:],35,stats)
                    check_windows(rows,stats,"open")
                    stats["high_start_integer_pairs"]+=1
    # One-odd rational cycle provides long same-even gaps and constant large level.
    for L in (7,10,13,17):
        q=2**L-3
        power=3%q
        j=1
        while power!=1:
            power=3*power%q
            j+=1
        if j>3000:
            continue
        rows=trajectory(Fraction(1,q),Fraction(1,q),j,0,3*L,stats)
        check_windows(rows,stats,"thin")
        stats["thin_periodic_windows_sources"]+=1
    for key in ("closed_adjacent_pairs","open_short_windows","thin_short_windows",
                "zero_low_group","nonzero_low_group","negative_start_windows","negative_to_positive"):
        verify(stats[key]>0,key)
    for key in sorted(stats):
        print(f"{key}={stats[key]}")


if __name__=="__main__":
    main()
