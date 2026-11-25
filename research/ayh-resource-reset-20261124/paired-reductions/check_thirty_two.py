"""Direct positive-integer executions for the 32-comparator theorem."""
from math import inf


def v2(n):
    return (n & -n).bit_length()-1 if n else inf


def demand(flag, detail):
    if not flag:
        raise RuntimeError(detail)


def trace(n, horizon):
    odds = 0
    for h in range(horizon+1):
        yield h,n,odds
        b = n % 2
        n = (3*n+1)//2 if b else n//2
        odds += b


def ascent_exponent(n):
    n += 1
    twos = v2(n)
    n >>= twos
    threes = 0
    while n%3 == 0:
        n//=3
        threes+=1
    return twos+threes if n==1 else None


def run(v):
    d=v2(v)
    k,r=divmod(d,3)
    W=3**(2*v); j=66*v-5
    z=((32<<(66*v))-527)//81
    npeak={i: W**i-1 for i in range(1,33)}
    u={i:x >> v2(x) for i,x in npeak.items()}
    for i,n in u.items():
        if i<=20: demand((n<<40)<z, "floor")
    hcount=0
    tcount=0
    collisions=0
    obs=[(22,d,d+4,3**d*u[22]-1),
         (21,2*k,3*k+3,(3**(2*k)*u[21]<<r)-5)]
    peaks = {}
    for i,peak in npeak.items():
        for t,n,p in trace(peak,v):
            peaks.setdefault(n,[]).append((i,t,p))
            tcount+=1
    for e,b,beta,start in obs:
        demand(start>(z<<(v//2-5)), "query ceiling")
        for h,n,p in trace(start,v):
            a=ascent_exponent(n)
            demand(a is None or a% (2*v) or not 1<=a//(2*v)<=32,
                   "32-candidate ascent")
            demand(h>v//8 or a is None or a>=j or a==0, "general ascent")
            hcount+=1
            for i,t,p2 in peaks.get(n,()):
                demand(i==e and t==h+beta and p2==b+p,"post-peak clock")
                collisions+=1
    return hcount,tcount,collisions


if __name__=="__main__":
    # The residue condition and odd-cofactor valuations are checked explicitly.
    values=[166,220,274,328,436,544,652,760]
    demand(all(v>=128 and v%27==4 and v%2==0 for v in values),"family")
    totals=[sum(row) for row in zip(*(run(v) for v in values))]
    print(f"{len(values)} supplied members, {totals[0]} checkpoint values, "
          f"{totals[1]} Mersenne post-peak values, {totals[2]} matched comparisons.")
