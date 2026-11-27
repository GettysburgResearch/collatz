"""Exact mock rank populations with convexity, prescribed grades, and ternary midpoint rigidity."""
from itertools import product
import json

def root_floor(n, k):
    hi=1<<((n.bit_length()+k-1)//k)
    lo=0
    while lo+1<hi:
        mid=(lo+hi)//2
        if mid**k<=n:lo=mid
        else:hi=mid
    return hi if hi**k<=n else lo

def cap(values):
    if len(values)<3:return True
    levels={c:{v//3 for v in values if v%3==c} for c in range(3)}
    return len([c for c in levels if levels[c]])<=2 and all(cap(v) for v in levels.values())

def binary_part(values):
    if len(values)<3:return set(values)
    levels=sorted(((len([x for x in values if x%3==c]),c) for c in range(3)),reverse=True)
    return {3*y+c for _,c in levels[:2] for y in binary_part({v//3 for v in values if v%3==c})}

def lowcode(i):
    if i==0:return 0
    return 3*lowcode(i//2)+i%2

def mask(j):
    return 2 if j==0 or ((j*173+51)%97)<42 else 1

def check(x):
    n=len(x)
    assert len(set(x))==n and cap(set(x))
    l=[12*v+mask(j) for j,v in enumerate(x)]
    assert all((v&-v)==mask(j) and v%3 for j,v in enumerate(l))
    assert len({v//(v&-v) for v in l})==n and cap(set(l))
    for version in (x,l):
        v=version+[2*w for w in version[:2]]
        g=[b-a for a,b in zip(v,v[1:])]
        assert all(g[i+1]>g[i]>0 for i in range(n))
    return l

def smooth_example(p):
    B=100*p*p
    f=[root_floor((B**p)<<j,p) for j in range(p)]
    rest=set(f);colors={}
    while rest:
        part=binary_part(rest)
        assert part and cap(part)
        c=len(set(colors.values()))
        colors.update((v,c) for v in part)
        rest-=part
    ncol=len(set(colors.values()))
    D=3**(ncol-1).bit_length()
    x=[D*v+lowcode(colors[v]) for v in f]
    l=check(x)
    for j in range(p):
        assert abs(l[j]-12*D*f[j])<12*D+3
    return ncol

def one_cube(p):
    q=1;b=0
    while q<p:q*=3;b+=1
    covered={lowcode(j):(0,j) for j in range(1<<b)}
    shifts=[]
    while len(covered)<q:
        v=max(range(q),key=lambda y:len(set(covered)|{(s+y)%q for s in covered}))
        old=dict(covered)
        for z,(x,j) in old.items():covered.setdefault((z+v)%q,(x+(1<<len(shifts)),j))
        shifts.append(v)
        assert len(covered)>len(old)
    a=len(shifts);D=3**a
    F=[(12*p+1)*j+3*j*j for j in range(p+1)]
    u=[lowcode(covered[v%q][0]) for v in F]
    f=[D*v+w for v,w in zip(F,u)]
    shift=f[p]-2*f[0]
    x=[v+shift for v in f[:p]]
    l=check(x)
    assert len({v%(D*q) for v in x})==p
    weights=[3**i+D*v for i,v in enumerate(shifts)]+[D*3**j for j in range(b)]
    for j in range(p):
        h,t=covered[F[j]%q]
        bits=[(h>>i)&1 for i in range(a)]+[(t>>i)&1 for i in range(b)]
        assert (sum(e*w for e,w in zip(bits,weights))+shift-x[j])%(D*q)==0
        assert (l[j]-(12*shift+1)-(mask(j)-1)-sum(12*e*w for e,w in zip(bits,weights)))%(3*D*q)==0
    return (a,b)

def main():
    smooth={p:smooth_example(p) for p in (3,6,9,16,27,41,64,81,127,169,251)}
    cubes={p:one_cube(p) for p in (3,6,9,16,27,41,64,81)}
    print(json.dumps({'smooth_colors':smooth,'single_cube_depths':cubes,
                      'smooth_populations_checked':sum(smooth),'cube_populations_checked':sum(cubes)},indent=2))
if __name__=='__main__':main()
