"""Independent exact controls for signed anchor scores, word coding and finite DAG compilation."""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from math import gcd, inf, log
import json
import random


def require(condition, reason):
    if not condition:
        raise RuntimeError(reason)


def v(n, prime):
    if n == 0:
        return inf
    result = 0
    while n % prime == 0:
        n //= prime
        result += 1
    return result


def true_depth(x, t):
    return v(x*t.denominator+t.numerator, 3)-v(t.denominator, 3)


def make_ball(h, signed=True):
    lo = -h if signed else 1
    return {Fraction(p, q) for q in range(1, h+1) for p in range(lo, h+1)
            if gcd(p, q) == 1}


def forward(x):
    b = 3*x+1
    e = v(b, 2)
    return b >> e, e


def local_control():
    c = Counter()
    for h in (1, 2, 4, 7, 11):
        ball = make_ball(h)
        for n in range(1, 320, 2):
            states = [n]
            es = []
            for i in range(15):
                y, e = forward(states[-1])
                states.append(y)
                es.append(e)
            scores = [max((true_depth(x, t),t) for t in ball) for x in states]
            start = 0
            thresh = h*h*(n+1)
            forced_length = thresh.bit_length()
            forced_seen = False
            for i, e in enumerate(es):
                d, t = scores[i]
                f, u = scores[i+1]
                x, y = states[i:i+2]
                require(t.denominator % 3 and u.denominator % 3, 'chosen non-unit at 3')
                require(d >= 0 and f >= 0, 'family maximum')
                p,q=t.as_integer_ratio()
                a,b=u.as_integer_ratio()
                defect=(1 << e)*q*a-b*(3*p-q)
                require(defect==(1 << e)*q*(b*y+a)-3*b*(q*x+p), 'physical residual')
                if defect:
                    require(v(defect,3)>=min(d+1,f), 'signed depth minimum')
                    c['defects_with_infinite_endpoint'] += d==inf or f==inf
                    c['discrepancies'] += 1
                    if i < forced_length:
                        forced_seen = True
                    start = i+1
                else:
                    t0=scores[start][1]
                    disp=t0.denominator*states[start]+t0.numerator
                    if disp:
                        require((u.denominator*disp) % (1<<sum(es[start:i+1])) == 0,
                                'dyadic denominator budget')
                        require((1<<(i+1-start))<=h*h*(states[start]+1), 'run length')
                    c['exact'] += 1
            if n>h and forced_length<=len(es):
                require(forced_seen, 'fully signed forced discrepancy')
                c['fully_funded_windows'] += 1
    c['dyadic_terminal_factor_witness'] = int(
        Fraction(3,1)+(1) == 4 and (3*Fraction(5,4)-1)/4 == Fraction(11,16))
    require(true_depth(1,Fraction(3**50-1))==50, 'unbounded superset control')
    return dict(sorted(c.items()))


def words(graph,h):
    """Every terminal path from every vertex, then audit grading on vertex paths."""
    @lru_cache(maxsize=None)
    def all_paths(t):
        if not graph[t]:
            return [(t,(),(t,))]
        return [(z,(e,)+w,(t,)+path)
                for e,u in graph[t] for z,w,path in all_paths(u)]

    largest=0
    paths_checked=0
    nontrivial=0
    storage=0
    graded_segments=0
    grade_crossings=0
    for t in graph:
        seen={}
        for z,w,path in all_paths(t):
            k=len(w)
            total=sum(w)
            endpoint_key=z,k
            require(endpoint_key not in seen, 'endpoint-length code collision')
            seen[endpoint_key]=w
            require(total==v(z.denominator,2)-v(t.denominator,2), 'tail budget')
            require((1<<total)<=h, 'height budget')
            encoded=1
            for i in range(k-1,-1,-1):
                encoded=3**(k-1-i)+(1<<w[i])*encoded
            require(encoded==3**k*t+(1<<total)*(1-z), 'affine code identity')
            decoded=[]
            value=encoded
            for i in range(k):
                delta=value-3**(k-i-1)
                a=v(delta,2)
                require(0<a<inf,'positive word decoding')
                decoded.append(a)
                value=delta >> a
            require(tuple(decoded)==w and value==1,'full word decode')
            paths_checked += 1
            nontrivial += bool(w)
        largest=max(largest,len(seen))
        require(len(seen)<=len(graph)**2,'global terminal path cap')

    def count(t):
        return len(all_paths(t))

    for radix in (2, 3, 5):
        def grade(t):
            g=0
            n=count(t)
            while n>=radix:
                g+=1
                n//=radix
            return g

        @lru_cache(maxsize=None)
        def grade_paths(t):
            same=[(e,u) for e,u in graph[t] if grade(u)==grade(t)]
            if not same:
                return [()]
            return [(e,)+w for e,u in same for w in grade_paths(u)]

        for t in graph:
            chunks=grade_paths(t)
            require(len(chunks)<radix, 'prefix-incomparable grade count')
            require(all((1<<sum(w))<=h for w in chunks), 'grade chunk budget')
            storage+=sum(sum(w) for w in chunks)
            for _, w, path in all_paths(t):
                start=0
                while start<len(w):
                    j=start
                    while j<len(w) and grade(path[j+1])==grade(path[start]):
                        j+=1
                    fragment=w[start:j]
                    require(any(a[:len(fragment)]==fragment for a in grade_paths(path[start])),
                            'same-grade factor')
                    graded_segments += bool(fragment)
                    if j<len(w):
                        require(grade(path[j+1])<grade(path[start]),'grade order')
                        grade_crossings+=1
                    start=j+1
    return paths_checked,nontrivial,largest,storage,graded_segments,grade_crossings


def compile_control():
    rng=random.Random(251161)
    stats=Counter()
    maxpaths=0
    # The dyadic tree also forces many nonintegral paths to share their first vertex.
    for h in (8, 15, 28, 48, 96):
        pool=sorted(t for t in make_ball(h) if t.denominator%3)
        for num,den in ((1, 1), (2, 3), (1, 3)):
            nodes={t for t in pool if rng.randrange(den)<num}
            graph={t:[] for t in nodes if not t.denominator%2}
            for t in nodes:
                edges=[]
                for e in range(1,(4*h*h).bit_length()+1):
                    u=(3*t-1)/(1<<e)
                    if u in nodes:
                        edges.append((e,u))
                typ=(t.numerator%2,t.denominator%2)
                if typ==(1,1):
                    require(sum((u.numerator%2 and u.denominator%2) for _,u in edges)<=1,
                            'signed dyadic unit core')
                elif typ==(0,1):
                    require(all(not u.denominator%2 for _,u in edges), 'integer even transition')
                else:
                    require(all(v(u.denominator,2)==v(t.denominator,2)+e for e,u in edges),
                            'denominator DAG')
                    graph[t]=edges
            count,nontrivial,largest,stored,segs,cross=words(graph,h)
            stats['graphs']+=1
            stats['terminal_paths']+=count
            stats['nonempty_terminal_paths']+=nontrivial
            stats['three_radix_storage_sum']+=stored
            stats['decoded_same_grade_segments']+=segs
            stats['decoded_grade_boundary_letters']+=cross
            stats['branching_vertices']+=sum(len(edges)>1 for edges in graph.values())
            maxpaths=max(maxpaths,largest)
    stats['largest_terminal_path_count']=maxpaths
    return dict(sorted(stats.items()))


if __name__=='__main__':
    print(json.dumps({'local':local_control(),'compiler':compile_control(),
                      'yu_unrounded_coefficient':int(19*1200**3*6*(5+log(2))/log(3))},
                     indent=2,sort_keys=True))
