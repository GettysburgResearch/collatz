"""Independent finite proof arithmetic using geometric logarithms and interval CF extraction."""
from collections import Counter
from fractions import Fraction as Q
from hashlib import sha256
from itertools import product
from math import gcd
import json

CAP=10**1000
BITS=7389
SCALE=1<<BITS
FLOOR=1<<71
T=7000


def require(ok,tag):
    if not ok:
        raise ArithmeticError(tag)


def geometric_log(u,v):
    # -log(1-u/v). Iterated fixed-point floors need not be exact floors
    # of powers. Their error is <v/(v-u)<=3 at every date.
    x=SCALE
    n=0
    lower=0
    while x:
        n+=1;x=x*u//v
        lower+=x//n
    # Per-term loss < 4 fixed-point units. The remaining geometric tail
    # of scaled true powers beyond the first zero is bounded by 9.
    return lower,lower+4*n+9


def enclosure():
    lo2,hi2=geometric_log(1,2)
    lo3,hi3=geometric_log(2,3)
    return Q(lo3,hi2),Q(hi3,lo2)


def interval_convergents(lo,hi):
    # Compute partial quotients simultaneously for all reals in [lo,hi].
    # After removing the common integer, reciprocation reverses the interval.
    L=lo;U=hi;a0,a1=0,1;b0,b1=1,0
    rows=[];outside=0
    while outside<3:
        h=L.numerator//L.denominator
        require(h==U.numerator//U.denominator,'CF ambiguity in precision enclosure')
        a0,a1=a1,h*a1+a0;b0,b1=b1,h*b1+b0
        rows.append((a1,b1))
        require(abs(a1*b0-a0*b1)==1,'unimodularity')
        L,U=1/(U-h),1/(L-h)
        outside+=int(b1>CAP)
    return rows


def upper_fence(rows,N,lo,hi):
    for (a,b),(c,d) in zip(rows,rows[1:]):
        if min(b,d)<=N:
            continue
        lower,upper=sorted((Q(a,b),Q(c,d)))
        require(lower<lo<=hi<upper,'whole log inside unimodular fence')
        return upper
    raise ArithmeticError('no fence')


def clocks_and_spans():
    out=Counter()
    for P in (7,11,13,17,23,29,37,41,43):
        for k in range(P//2+1,P):
            if gcd(k,P)!=1:
                continue
            for b in (2,3,5,8,11):
                records={}
                for r in range(P):
                    back=[(r-j*k)%P for j in range(b+1)]
                    if P-1 in back:
                        continue
                    m=[]
                    for lo,dest in zip(back[::-1],back[-2::-1]):
                        step=(lo+k)//P+1
                        require((lo+1+k)//P+1==step and dest==(lo+k)%P,'common unwrapped letter')
                        m.append(step)
                    m=tuple(m)
                    require(all(a!=1 or c!=1 for a,c in zip(m,m[1:])),'calendar no adjacent ones')
                    w=((P-k)*(b-1))//P
                    require(m[:-1].count(1)>=w,'number of disjoint pair restrictions')
                    # Right-continuous floor cells, independent of exclusions.
                    cell=sum(jk<=r for jk in {j*k%P for j in range(1,b+1) if j*k%P})
                    if cell not in records:
                        records[cell]=[m,[]]
                    require(m==records[cell][0],'constant calendar on a terminal cell')
                    records[cell][1].append(r)
                    out['retained_terminal_calendar_interfaces']+=1
                require(len(records)<=b+1,'number of schedule cells')
                # Artificial strictly increasing gaps with many missing integers.
                # Digital intervals computed only over surviving ranks, whose
                # convex hulls stay disjoint because the underlying cells are ordered.
                g=[(P+1)**3+2*r*r+r for r in range(P)]
                span=sum(g[rs[-1]]-g[rs[0]] for _,rs in records.values())
                require(span<=g[-1]-g[0]<g[0],'sum of numeric spans once')
                for cal,rs in records.values():
                    V=g[rs[-1]]-g[rs[0]]
                    hist=Counter(g[r]%3**b for r in rs)
                    require(max(hist.values())<=1+V//3**b,'per-residue span bound')
                require(P-sum(len(rs) for _,rs in records.values())<=b+1,'seam rank count')
                out['exact_cell_partitions']+=1
    # enumerate actual adjacent bit trajectories on all no-consecutive-one
    # calendars through length eight independently of the symbolic 7/9 rule.
    for b in range(2,9):
        for m in product((1,2),repeat=b-1):
            if any(a==c==1 for a,c in zip(m,m[1:])):
                continue
            outcomes={(v,u,(v-u,)) for u,v in product((1,2),repeat=2)}
            for e in m:
                outcomes={(vp,up,ds+(vp-up,)) for v,u,ds in outcomes for up,vp in product((1,2),repeat=2)
                          if e==2 or (up>=u and vp>=v)}
            words={ds for v,u,ds in outcomes}
            W=m.count(1)
            require(len(words)==7**W*3**(b-2*W),'attained discrete drift words')
            out['actual_drift_words_counted']+=len(words)
            out['short_path_calendars']+=1
    return dict(out)


def run():
    lo,hi=enclosure()
    require(hi-lo<Q(1,1<<7300),'independent log enclosure precision')
    rows=interval_convergents(lo,hi)
    small=upper_fence(rows,10**6,lo,hi);large=upper_fence(rows,CAP,lo,hi)
    require(small.denominator*10**6<FLOOR and 4*CAP*large.denominator < 1<<T,'finite convexity fences')
    closest=1;when=None
    # Exact distance to the nearest integer from the complete interval j[lo,hi].
    for j in range(1,T+4):
        xl=j*lo;xu=j*hi;floor=xl.numerator//xl.denominator
        require(xu<floor+1,'multiple crosses an integer')
        sep=min(xl-floor,floor+1-xu)
        if sep<closest:closest,when=sep,j
    require(closest>Q(1,20000) and 10**6*(closest-Q(T+3,FLOOR))>4,'explicit short-time separation')
    profile=sum(Q(1,1)/(Q(3,2)+Q(j,8)+Q(j*j,128)-Q(1,10**6)) for j in range(8))
    reciprocal=Q(200,207)*(Q(1,8)+Q(1,10**6))*profile
    require(reciprocal<Q(484763,10**6)<Q(1,2),'eight-cell reciprocal profile')
    power3=[1]
    while power3[-1]<4*CAP*large.denominator:power3.append(3*power3[-1])
    digest=sha256();worst=Q(0);worst_case=None;tested=0;upper_total=0;pre_floor=0
    for A,P in rows:
        if P>CAP:continue
        require(A>P*hi or A<P*lo,'convergent side unresolved')
        if A<P*lo or P<=10**6:continue
        upper_total+=1
        d=A-P*hi
        if FLOOR*d>=P:
            pre_floor+=1
            continue
        Y=(d.denominator+d.numerator-1)//d.numerator
        # An independent range includes the author's window choices.
        k=0
        while power3[k+1]<=Y:k+=1
        best=(None,None,None)
        for b in range(max(2,k-20),k+3):
            w=((2*P-A)*(b-1))//P
            require(0<=2*w<=b,'disjoint digit pairs')
            numerator=(b+1)*9**w+(Y+(b+1)*power3[b])*7**w
            denominator=9**w
            top=numerator//denominator
            if best[0] is None or top<best[0]:
                best=top,b,w
        top,b,w=best
        require(top<P,'candidate survives period census')
        digest.update(f'{A},{P},{Y},{b},{w},{top}\n'.encode('ascii'))
        r=Q(top,P)
        if r>worst:worst=r;worst_case=dict(A=A,P=P,g0_cap=Y,b=b,ones=w,integer_upper=top)
        tested+=1
    return dict(independent_log_base='positive power series for -log(1-x), x=1/2,2/3',
                working_bits=BITS,small_upper_fence=str(small),large_upper_fence_denominator_digits=len(str(large.denominator)),
                common_convergents=len(rows),upper_above_small_before_floor=upper_total,
                floor_removals=pre_floor,finite_candidates_excluded=tested,complete_witness_digest=digest.hexdigest(),
                min_multiple_index=when,min_short_distance_lower_billionth=(closest*10**9).__floor__(),
                reciprocal_upper_millionth=-((-reciprocal*10**6).__floor__()),
                worst_ratio_upper_millionth=-((-worst*10**6).__floor__()),worst_case=worst_case,
                finite_calendar_controls=clocks_and_spans())


if __name__=='__main__':
    print(json.dumps(run(),sort_keys=True,indent=2))
