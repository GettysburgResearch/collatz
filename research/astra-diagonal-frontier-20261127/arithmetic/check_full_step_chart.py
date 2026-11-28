"""Complete-grid checks for the two monotone extensions and literal ordinary edges."""

from fractions import Fraction
from math import gcd
import json


def require(check, detail):
    if not check:
        raise ArithmeticError(detail)


def oddpart(n):
    return n//(n&-n)


def step(z):
    return 3*z+1 if z%2 else z//2


def mark(w):
    return (0,1,0,0,0,1,6,3,0,0,0,1)[w%12]


def fold(c,x):
    return 6*x if x<6*c else x


def maps(c,up):
    graph={}
    for w in range(6*c,36*c):
        y=3*w+mark(w)
        if y<36*c:
            graph[w]=y,0
        else:
            graph[w]=(y+(5 if up else 0))//6,1
    return graph


def clocks(graph):
    visited=set()
    established=set()
    for start in graph:
        if start in visited:
            continue
        x=start
        i=h=0
        seen={}
        while x not in seen and x not in visited:
            seen[x]=(i,h)
            x,d=graph[x]
            i+=1
            h+=d
        if x in seen:
            j,k=seen[x]
            require(gcd(h-k,i-j)==1,"primitive cyclic order")
            established.add(Fraction(h-k,i-j))
        visited.update(seen)
    require(len(established)==1,"same rotation on distinct components")
    return established.pop()


def verify():
    total_edges=align=split=0
    first_split=None
    range_grid=120
    for c in range(1,range_grid+1):
        low,high=maps(c,False),maps(c,True)
        for graph in (low,high):
            values=[v*6**b for v,b in graph.values()]
            require(all(x<=y for x,y in zip(values,values[1:])) and values[-1]<=6*values[0],"global lifted order")
        a,b=clocks(low),clocks(high)
        require(a<=b,"rotation order")
        if a==b:align+=1
        elif first_split is None:first_split=[c,str(a),str(b)]
        split+=a!=b
        # Maximal integer X satisfying X<9c+2, and the c-level minimum.
        X=9*c+1
        for x in range(c,3*X+2):
            if x%3==0 or not c<=oddpart(x)<=X:
                continue
            y=step(x)
            if not c<=oddpart(y)<=X or y<c or y>3*X+1:
                continue
            u,v=fold(c,x),fold(c,y)
            e=(x<6*c)+(x%2==0)-(y<6*c)
            require(u in low and v in low and e in (0,1),"eligible native source and target")
            require(low[u]==high[u]==(v,e),"one true edge in both completed maps")
            total_edges+=1
    # Nontrivial ordinary mock circulations would not qualify: check the one
    # actual ordinary circuit via its full native states, plus the separate
    # rational example to test loss of the denominator-one hypothesis.
    cyc=[1,4,2]
    low,high=maps(1,False),maps(1,True)
    for x in cyc:
        require(low[fold(1,x)]==high[fold(1,x)] and low[fold(1,x)][0]==fold(1,step(x)),"full ordinary period")
    require(clocks(low)==Fraction(2,3),"unaccelerated A/(p+A), not an odd-step period")
    x,y=Fraction(5,7),Fraction(11,7)
    require(2*y==3*x+1 and 8*x==3*y+1 and gcd(2,4)==2 and y/x<9,"separate rational control")
    return {"cutoffs_checked":range_grid,"completions_agree":align,"completions_split":split,
            "first_split":first_split,"literal_native_edges":total_edges,
            "ordinary_full_cycle":[1,4,2],"ordinary_base_six_rotation":"2/3",
            "rational_numerators":[5,11],"rational_denominator":7,"rational_period_clock_gcd":2}


if __name__=="__main__":
    print(json.dumps(verify(),indent=2,sort_keys=True))
