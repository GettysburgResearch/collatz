"""Exact finite controls for signed tails and the local-form product."""

from fractions import Fraction as F
from itertools import combinations
from math import gcd, lcm, prod


def require(ok, why):
    if not ok:
        raise ValueError(why)


def pv(x, prime):
    if x == 0:
        return F(0)
    x = F(x)
    a,b = abs(x.numerator), x.denominator
    e = 0
    while a % prime == 0:
        a //= prime
        e += 1
    while b % prime == 0:
        b //= prime
        e -= 1
    return F(prime)**(-e)


def check(a):
    p, A = len(a), sum(a)
    D = (1 << A) - 3**p
    if D<=0:
        return (0,0,0,0)
    sums=[0]
    for e in a:
        sums.append(sums[-1]+e)
    B=[F(1 << m, 3**i) for i,m in enumerate(sums)]
    x0=sum(B[:-1],F(0))/(3*(B[p]-1))
    q=x0.denominator
    ys=[x0.numerator]
    for e in a:
        z=3*ys[-1]+q
        require(z % (1 << e) == 0, 'native divisibility')
        ys.append(z >> e)
    require(ys[-1]==ys[0] and all(y%2 and y%3 for y in ys), 'true unit numerators')
    if len(set(ys[:-1]))!=p:
        return (0,0,0,0)
    counts=[0,0,0,0]
    V=B[p]*ys[0]
    for h in range(1,p):
        for r in range(h,p-1):
            for L in range(1,p-r):
                if a[r-h:r-h+L]!=a[r:r+L]:
                    break
                m=sums[r+L]-sums[r]
                delta=ys[r]-ys[r-h]
                require(delta != 0 and delta % (1 << m)==0, 'shared odd quotient')
                G=delta >> m
                w=B[r]/B[r-h]; U=B[r]*(1 << m)*G; W=w*V
                tail=F(q,3)*(w*sum(B[r-h+L:p])-sum(B[r+L:p]))
                E=U-V+W
                require(E==tail, 'signed tail identity')
                J=max(B[j]/B[e] for e in (r-h+L,r+L) for j in range(e,p))
                bound=F(2*p*q,3)*J*B[r+L]
                require(abs(E)<=bound, 'two tail bound')
                local=abs(E*V*W)*prod(pv(z,v) for z in (U,V,W) for v in (2,3))
                require(local<=F(2*p*q*ys[0]**2,3)*J/3**L, 'fixed-place product')
                require(pv(U,3)<=3**r and pv(V,3)==3**p and pv(W,3)==3**(p+h),
                        'separated ternary valuations')
                counts[0]+=1
                counts[1]+=r-h+L>r
                counts[2]+=E<0
                counts[3]+=E>0
    return tuple(counts)


def main():
    ans=[0,0,0,0]
    for p in range(3,8):
        for A in range(max(p,(3**p).bit_length()), min(14,2*p)+1):
            for marks in combinations(range(1,A),p-1):
                env=(0,)+marks+(A,)
                a=tuple(v-u for u,v in zip(env,env[1:]))
                ans=[a+b for a,b in zip(ans,check(a))]
    require(all(x>0 for x in ans),'nonempty signed and overlapping samples')
    print(f'{ans[0]} long-block identities at finite scale, {ans[1]} overlaps, '
          f'{ans[2]} negative and {ans[3]} positive signed remainders')


if __name__=='__main__':
    main()
