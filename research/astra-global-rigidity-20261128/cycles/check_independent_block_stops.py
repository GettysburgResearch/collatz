"""Exact controls on ordinary and denominator-cleared independently stopped paths."""
from fractions import Fraction as F
from math import gcd,prod

from check_repeated_block_drawdown import pv, require


def native(x,q,steps):
    ys=[x]; aa=[]; scales=[F(1)]
    for _ in range(steps):
        n=3*ys[-1]+q
        a=(n&-n).bit_length()-1
        require(a>0,'odd source over odd denominator')
        aa.append(a); ys.append(n >> a); scales.append(scales[-1]*F(1 << a,3))
    return ys,aa,scales


def run():
    total=equal=unequal=zero=neg=0
    for q in (1,5,7,11):
        for small in range(1,64,2):
            if gcd(small,q)>1:
                continue
            A,aa,bs=native(small,q,17)
            for L in (1,3,6,9):
                Ac=sum(aa[:L]); large=small+2*q*(1 << Ac)
                B,bb,cs=native(large,q,17)
                require(aa[:L]==bb[:L] and bs[L]==cs[L], 'supplied common word')
                for k1,k2 in ((L,L),(L,L+1),(L+1,L+1),(L+4,L+2),(L+2,L+7)):
                    x,z=A[k1], B[k2]
                    U=small-large; V=bs[k1]*x; W=cs[k2]*z
                    E=U-V+W
                    rhs=F(q,3)*(sum(cs[L:k2])-sum(bs[L:k1]))
                    require(E==rhs,'independent end formula')
                    ratio=max([F(1)]+[b/bs[L] for b in bs[L:k1]]+[c/cs[L] for c in cs[L:k2]])
                    local=abs(E*V*W)*prod(pv(v,t) for v in (U,V,W) for t in (2,3))
                    require(local<=(k1+k2)*q*x*z*ratio/3**L, 'local product upper')
                    require(pv(U,3)<=1 and pv(V,3)==3**k1 and pv(W,3)==3**k2, 'ternary charges')
                    total+=1; equal+=k1==k2; unequal+=k1!=k2; zero+=E==0; neg+=E<0
    require(min(equal,unequal,zero,neg)>0,'case diversity')
    print(f'{total} two-stop pairs, {equal} equal and {unequal} unequal lengths, '
          f'{zero} exact cancellations and {neg} negative remainders')


if __name__=='__main__':
    run()
