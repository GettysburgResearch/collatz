"""Independent return-time sieve and interval-length formulas for real cap 1.985."""
from fractions import Fraction as F
from math import floor
import json

L,H=F(5849625007,10**10),F(5849625008,10**10)
cap=F(197,200)
h=1-cap

def check(x,msg):
    if not x:raise RuntimeError(msg)

def profile(a):
    # Only these four positive times can intersect the initially forced interval at all.
    candidates=[]
    for k in range(1,148):
        f=(k*a)%1
        if min(f,1-f)<h:candidates.append(k)
        check(f not in (0,h,1-h),'non-strict candidate')
    check(candidates==[53,94,106,147],'additional short return')
    u=53*a-31;v=55-94*a
    # Intermediate time 106 is a positive second 53-shift, and cannot be a first return.
    check(0<u<v<h and h<u+v and h>2*u,'return endpoint order')
    weights={53:h-u,94:h-v,147:u+v-h}
    pts={53:(cap+1-u)/2,94:(cap+v+1)/2,147:(1-u+cap+v)/2}
    E={}
    for n,f in pts.items():
        vct=(1,0,0)
        for j in range(n):
            f+=a;up=f>=1
            if up:f-=1
            X,Y,Z=vct
            vct=(X,4*X+Y,X+Y+Z) if up else (X+Y+Z,Y+4*Z,Z)
            check((f>cap)==(j+1==n),'earlier return')
        E[n]=vct[0]
    check(sum(n*w for n,w in weights.items())==1,'tower mass')
    upper=1+sum(weights[n]*k/1024 for n,k in [(53,-80),(94,132),(147,420)])
    for n,k in [(53,-80),(94,132),(147,420)]:
        check(3**(n*1024+k-1)<E[n]**1024<=3**(n*1024+k),'discrete log bound')
    check(upper<F(9999,10000),'insufficient weighted margin')
    return E,weights,upper

left,wl,ul=profile(L);right,wr,ur=profile(H)
# A wrap or classification crossing anywhere in the slope slab requires a crossing
# of one of the exact n*alpha endpoints 0,h,1-h modulo one, excluded throughout.
for k in range(1,148):
    for c in [F(0),h,1-h]:
        check(floor(k*L-c)==floor(k*H-c),'hidden slope crossing')
check(left==right,'changing word')
# All initial prefix entry boundaries including both equality-faces, using only modular
# integer arithmetic at the chosen test slope.
a=(H+L)/2;Q=a.denominator*200;t=a.numerator*(Q//a.denominator);cut=197*Q//200
edges=sorted({0,Q}|{(-j*t)%Q for j in range(148)}|{(cut-j*t)%Q for j in range(148)})
xs=edges[:-1]+[F(x+y,2) for x,y in zip(edges,edges[1:])]
initial=[]
for x in xs:
    if x<=cut:
        initial.append(next(j for j in range(1,148) if (x+j*t)%Q>cut))
check(max(initial)==146,'initial wait')
print(json.dumps({'eligible_intersection_times':[53,94,106,147],
                  'max_preentry':max(initial),'phase_faces':len(xs),
                  'actual_return_energy':{str(k):str(v) for k,v in left.items()},
                  'left_mass':{str(k):str(v) for k,v in wl.items()},
                  'right_mass':{str(k):str(v) for k,v in wr.items()},
                  'limiting_exponent_upper':str(max(ul,ur))},indent=2,sort_keys=True))
