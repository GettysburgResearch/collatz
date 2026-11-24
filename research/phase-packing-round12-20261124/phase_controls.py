"""Exact finite controls; not a proof of universal Collatz or a Lean replay."""
from fractions import Fraction as F
from itertools import product
from math import ceil, isqrt
import json


def need(ok, message):
    if not ok:
        raise ArithmeticError(message)


def step(q):
    v = 3*q+1
    g = (v & -v).bit_length()-1
    return v >> g, g


def split(t):
    c = ceil(t-F(1,2))-1
    return t-c, c


def charge(word):
    a = 0
    for b in word:
        a = 3*a+b
    return F(a, 3**len(word)-1)


def affine(word):
    D, C = 1, 0
    for b in word:
        C = 3*C+D
        D <<= b
    return D, 3**len(word), C


def phase(p):
    b = []
    f = p
    while True:
        z, g = split(3*f)
        need(1 <= g <= 3, 'canonical gap')
        b.append(g)
        f = z
        if f == p:
            return b


def profile(word):
    D,A,C = affine(word)
    need(D>A, 'contracting canonical word')
    z0 = F(C,D-A)
    z = z0
    R, Rmax, zmax = F(1),F(1),z0
    for b in word:
        R *= F(3,2**b)
        z = (3*z+1)/2**b
        Rmax = max(Rmax,R)
        zmax = max(zmax,z)
    need(z == z0 and R == F(A,D), 'canonical cycle and slope')
    x = 4*zmax**3
    Q = isqrt(x.numerator//x.denominator)
    return z0,zmax,R,Rmax,Q


def guard(q,t):
    return t > F(1,2) and 3*t <= q.bit_length()+3


def known_orbit(q):
    qs=[q]; gs=[]
    while q != 1:
        need(len(gs)<10000,'bounded oracle exhausted')
        q,g=step(q); qs.append(q); gs.append(g)
    hs=[F(1)]
    for g in reversed(gs):
        hs.append((g+hs[-1])/3)
    return qs,gs,list(reversed(hs))


def decide(q,t):
    # Valid only for supplied rational candidates whose eventual canonical
    # periodic phase contracts. Every early rejection is sound regardless.
    clock=0
    while t.denominator % 3 == 0:
        if q == 1: return t == 1,clock
        if not guard(q,t): return False,clock
        q,g=step(q); t=3*t-g; clock+=1
    if q==1: return t==1,clock
    if not guard(q,t): return False,clock
    p,_=split(t); word=phase(p)
    _,zmax,R,Rmax,_=profile(word)
    remaining=Rmax*q; n=0
    while remaining>1:
        remaining*=R; n+=1
    for _ in range(n*len(word)):
        if q==1: return t==1,clock
        if not guard(q,t): return False,clock
        q,g=step(q); t=3*t-g; clock+=1
    x=4*(zmax+1)**3
    Q=isqrt(x.numerator//x.denominator)
    seen={}; gaps=[]
    for _ in range(Q+1):
        if q==1: return t==1,clock
        if not guard(q,t): return False,clock
        need(q<=Q,'post-burn guarded height')
        if q in seen:
            # Current q is on a literal cycle; charge computes its exact scalar.
            return t==charge(gaps[seen[q]:]),clock
        seen[q]=len(gaps)
        q,g=step(q); gaps.append(g); t=3*t-g; clock+=1
    raise ArithmeticError('finite guarded-state pigeonhole failed')


def finite_graph(Q):
    # An edge exiting [1,Q] is deleted. This classifies confined cycles only.
    color=bytearray((Q+1)//2)
    cycles=[]
    for q in range(1,Q+1,2):
        if color[q//2]: continue
        path=[]; x=q
        while x<=Q and color[x//2]==0:
            color[x//2]=1; path.append(x); x,_=step(x)
        if x<=Q and color[x//2]==1:
            cyc=path[path.index(x):]
            cycles.append(sorted(cyc))
        for x in path: color[x//2]=2
    return sorted(cycles)


def check():
    actual_edges=0; prefix_checks=0; residue_checks=0
    for q in range(1,2002,2):
        qs,gs,hs=known_orbit(q)
        ps,cs=zip(*(split(t) for t in hs))
        A=B=K=0
        for i,g in enumerate(gs):
            b=3*ps[i]-ps[i+1]
            need(b.denominator==1 and 1<=b<=3,'actual canonical gap')
            b=int(b); c,d=cs[i],cs[i+1]
            need(g+d==b+3*c and c>=0 and d>=0,'complete carry')
            need(8**d*(c+1)**4<=8**(3*c)*(d+1)**4,'SC1 local')
            Y,Z=F(qs[i],2**c),F(qs[i+1],2**d)
            need(Z==3*Y/2**(b+2*c)+F(1,2**(b+3*c)), 'exact normalization')
            need(Z<=(3*Y+1)/2**b,'canonical majorant')
            need(Y>=1 and qs[i]**2<=4*Y**3,'guard height')
            A+=g; B+=b; K+=c
            need(A+d==B+2*K+cs[0],'prefix telescope')
            need(8**B*(cs[0]+1)**4<=8**A*(d+1)**4,'prefix SC1')
            actual_edges+=1; prefix_checks+=1
            # Past gaps fix the ordinary endpoint mod 3^m, retaining full C.
            for m in range(1,min(i+1,5)+1):
                D,P,C=affine(gs[i+1-m:i+1])
                need(D*qs[i+1]==P*qs[i+1-m]+C,'past affine')
                need(qs[i+1]%P == C*pow(D,-1,P)%P,'past residue')
                residue_checks+=1
    decisions=0; accepted=0; max_clock=0; phases=set()
    for n in range(1,5):
        for w in product((1,2,3),repeat=n):
            D,A,C=affine(w)
            if D<=A: continue
            p=charge(w)
            phases.add(p)
    for q in range(1,130,2):
        actual=known_orbit(q)[2][0]
        for p in phases:
            for c in range(3):
                t=p+c; result,clock=decide(q,t)
                need(result==(t==actual),'candidate verdict')
                decisions+=1; accepted+=int(result); max_clock=max(max_clock,clock)
        result,clock=decide(q,actual)
        need(result,'true triadic candidate')
        decisions+=1; accepted+=int(result); max_clock=max(max_clock,clock)
    # Balanced near-critical contracting canonical words (not actual cycle words).
    samples={}; maxQ=0
    for n in range(1,201):
        A=(3**n).bit_length()
        w=[A*(i+1)//n-A*i//n for i in range(n)]
        need(sum(w)==A and all(1<=b<=3 for b in w),'balanced phase')
        _,zmax,_,_,Q=profile(w)
        maxQ=max(maxQ,Q)
        if n in (1,3,5,17,29,41,147,200): samples[str(n)]=Q
    cycles=finite_graph(maxQ)
    need(cycles==[[1]],'unexpected confined positive cycle')
    return dict(scope='finite exact arithmetic only; Lean not run', actual_edges=actual_edges,
                prefix_checks=prefix_checks,past_residue_checks=residue_checks,
                contracting_phases=len(phases),candidate_decisions=decisions,accepted=accepted,
                max_candidate_clock=max_clock,balanced_words=200,largest_cycle_bound=maxQ,
                odd_graph_vertices=(maxQ+1)//2,confined_cycles=cycles,sample_bounds=samples)

if __name__=='__main__':
    print(json.dumps(check(),sort_keys=True))
