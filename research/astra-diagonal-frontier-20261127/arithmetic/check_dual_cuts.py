"""Exact reciprocal cutoffs and independent integer lift-winding controls."""

from bisect import bisect_left, bisect_right
from fractions import Fraction
from math import gcd
import json


def require(check, detail):
    if not check:
        raise ArithmeticError(detail)


def components(graph):
    seen = set()
    result = []
    for start in graph:
        if start in seen:
            continue
        path = []
        local = {}
        item = start
        while item not in local and item not in seen:
            local[item] = len(path)
            path.append(item)
            item = graph[item][0]
        if item in local:
            loop = path[local[item]:]
            result.append((loop, sum(graph[x][1] for x in loop)))
        seen.update(path)
    return result


def fundamental_graph(m, base):
    multiplier = 5-base
    grid = sorted((k*(base**e), k, e)
                  for e in range(4) for k in range(m, base*m))
    values = [row[0] for row in grid]
    graph = {}
    for z in range(m, base*m):
        target = multiplier*z
        i = bisect_left(values, target) if base==2 else bisect_right(values, target)-1
        _, k, e = grid[i]
        graph[z] = k, e
    return graph


def duality(limit):
    branches = pairs = 0
    count = 0
    for m in range(1,limit+1):
        upper, lower = fundamental_graph(m,2), fundamental_graph(m,3)
        six = range(m,6*m)
        f = {x:(3*x,0) if x<2*m else ((x+1)//2,1) for x in six}
        g = {x:(2*x,0) if x<3*m else (x//3,1) for x in six}
        for graph, basegraph, stop in ((f,upper,2*m),(g,lower,3*m)):
            for x, dest in basegraph.items():
                y,j = graph[x]
                while y>=stop:
                    y,h = graph[y]
                    j+=h
                require((y,j)==dest,"first return against sorted precision grid")
                branches+=1
        if m<=45:
            for x in six:
                y,e=f[x]
                for z in six:
                    w,h=g[z]
                    for scale in (1,6):
                        require((y*6**e<=scale*z)==(6*x<=scale*w*6**h),"adjunction on both seam lifts")
                        pairs+=1
        us = {Fraction(w,len(o)) for o,w in components(upper)}
        ls = {Fraction(w,len(o)) for o,w in components(lower)}
        require(len(us)==len(ls)==1 and us.pop()*ls.pop()==1,"reduced rotations at all components")
        count+=len(components(upper))*len(components(lower))
    return {"cut_pairs":limit,"all_component_pairs":count,"literal_grid_returns":branches,
            "local_order_comparisons":pairs}


def triadic_graph(M):
    units = [x for x in range(1,M+1) if x%3]
    grid = sorted((n*3**e,n,e) for n in units for e in range(8))
    values = [v for v,_,_ in grid]
    return {x:grid[bisect_right(values,2*x)-1][1:] for x in units}


def winding():
    cases = [(1,(1,),(2,)),(7,(5,11),(1,3)),(5,(1,),(3,))]
    all_components = edges = witnesses = 0
    sample = []
    for q,odd,word in cases:
        micro = []
        for i,x in enumerate(odd):
            y = odd[(i+1)%len(odd)]
            a = word[i]
            require(2**a*y==3*x+q and gcd(q,x)==1,"full reduced test circuit")
            micro.extend((2**j*y,2**(j+1)*y if j<a-1 else 3*x) for j in range(a))
        for M in range(max(z for z,_ in micro),161):
            graph = triadic_graph(M)
            for loop,h in components(graph):
                hits=0
                for z,Y in micro:
                    for n in loop:
                        y,e=graph[n]
                        for j in range(-7,8):
                            v=Fraction(n)*Fraction(3)**j
                            w=Fraction(y)*Fraction(3)**(j+e)
                            require(not (v>=z and w<Y),"eligible target forbids negative event")
                            actual=(v<z and w>=Y)
                            require(actual==(v<z and 2*v>=Y),"strict half-open winding condition")
                            hits+=actual
                    edges+=1
                require(hits==len(micro)*h-len(odd)*len(loop),"full signed determinant")
                if q==1 and M<(27*min(odd)+1)//2:
                    require(hits==sum((9*x+1)//2 in loop for x in odd),"denominator-three reduction")
                if q==1 and M in (2,4,5,12,13,14,27,80,160):
                    sample.append([M,h,len(loop),hits])
                witnesses+=hits
                all_components+=1
    return {"ordinary_and_reduced_numerator_circuits":len(cases),"periodic_components":all_components,
            "circuit_edges_compared":edges,"positive_witnesses":witnesses,"trivial_cycle_examples":sample}


if __name__=="__main__":
    print(json.dumps({"duality":duality(180),"winding":winding()},indent=2,sort_keys=True))
