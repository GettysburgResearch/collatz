"""Every reduced-sublap crossing and the proper-modulus rational control."""
from fractions import Fraction as F
from itertools import combinations
from math import gcd, prod


def require(value, message):
    if not value:
        raise ArithmeticError(message)


def states(word):
    h = len(word)
    times = [0]
    for a in word:
        times.append(times[-1]+a)
    carry = sum(3**(h-1-i)*2**times[i] for i in range(h))
    D = 2**times[-1]-3**h
    if D <= 0:
        return []
    result = [F(carry,D)]
    for a in word:
        result.append((3*result[-1]+1)/2**a)
    require(result[0]==result[-1], 'rational return')
    return result[:-1]


def exact_count(word):
    xs = states(word)
    if not xs or len(set(xs))!=len(xs):
        return 0,0
    p=len(word); A=sum(word); g=gcd(p,A)
    U=p//g; N=A//g
    for k in range(1,g):
        t=k*U
        es=[sum(word[(i+j)%p] for j in range(t))-k*N for i in range(p)]
        ratios=[F(2)**es[i]*xs[(i+t)%p]/xs[i] for i in range(p)]
        stride=gcd(p,t)
        for j in range(stride):
            require(prod(ratios[j::stride])==1, 'fiber product')
        require(all(r!=1 for r in ratios), 'untied odd rays')
        found=False
        for i,v in enumerate(ratios):
            if v>1>ratios[(i+1)%p]:
                d=-es[i]; r=xs[(i+t)%p]-2**d*xs[i]
                require(d>0 and 0<3*r<2**d-1, 'physical crossing')
                found=True
        require(found, 'missing signed lag')
    return 1,g-1


def main():
    cases=lags=0
    for p in range(2,8):
        for total in range(p,15):
            if gcd(p,total)==1:continue
            for cuts in combinations(range(1,total),p-1):
                endpoints=(0,)+cuts+(total,)
                word=tuple(y-x for x,y in zip(endpoints,endpoints[1:]))
                c,l=exact_count(word);cases+=c;lags+=l
    word=(1,2,1,1,1,1,2,1,5,1,1,3)
    xs=states(word)
    require(xs[0]==F(797,295) and xs[6]==8*xs[0]+1, 'literal affine pair')
    require(max(xs)/min(xs)==F(7763,737) and len(set(xs))==12,'width and period')
    D=2**10-3**6
    C=D*xs[0]+2**7
    require(C==925 and F(C,D).denominator==59, 'rational proper determinant')
    print(f'{cases} primitive rational words, {lags} individual directed sublap witnesses; '
          'literal affine-pair and padded denominator controls passed')


if __name__ == '__main__':
    main()
