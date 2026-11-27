"""Finite exact modular fourth-energy certificate for the binary real strip 121/50."""
from collections import Counter, defaultdict
from fractions import Fraction as Q
from functools import lru_cache
from itertools import product
import json

N = 64
CAP = Q(21,50)
LEFT, RIGHT = Q(584961,10**6), Q(584964,10**6)


def cuts(alpha):
    rows = [(0, ('end', 0)), (1, ('end', 1))]
    for j in range(N+1):
        for offset, label in ((0,'wrap'),(CAP,'cap')):
            x = offset - j*alpha
            rows.append((x % 1, (label,j,x//1)))
    return [(x,tuple(sorted(label for pos,label in rows if pos==x))) for x in sorted(set(pos for pos,label in rows))]


def schedule(alpha, phase):
    levels=[]
    steps=[]
    for j in range(N+1):
        f = (phase+j*alpha) % 1
        levels.append(1+int(f<=CAP))
        if j<N:steps.append(1+int(f+alpha>=1))
    return levels[0],tuple(zip(steps,levels[1:]))


@lru_cache(None)
def moves(state,step,cap):
    a,b,c,d=state
    delta=(4>>a)+(4>>b)-(4>>c)-(4>>d)
    def targets(z):
        return tuple(w for w in (z, z+(-1 if step==1 else 1)) if 0<=w<=cap)
    return delta,tuple(product(*map(targets,state)))


def residue_energy(cap,steps):
    counts = {(state,0):1 for state in product(range(cap+1),repeat=4)}
    for step, newcap in steps:
        out=defaultdict(int)
        for (state,carry),ways in counts.items():
            delta,targets=moves(state,step,newcap)
            value=3*carry+delta
            if value % (1<<step): continue
            nextcarry=value>>step
            for target in targets: out[target,nextcarry]+=ways
        counts=out
    return sum(counts.values())


def direct(cap,steps):
    words=[(z,0) for z in range(cap+1)]
    m=0
    for step,h in steps:
        words=[(w,3*b+(4>>z)*(1<<m)) for z,b in words for w in (z,z+(-1 if step==1 else 1)) if 0<=w<=h]
        m+=step
    mod=1<<m
    values=Counter(b%mod for _,b in words)
    two=Counter()
    for x,c in values.items():
        for y,c2 in values.items():two[(x+y)%mod]+=c*c2
    diff=Counter()
    for x,c in two.items():
        for y,c2 in two.items():diff[(x-y)%mod]+=c*c2
    assert diff[0]==max(diff.values())
    return diff[0]


def run():
    mid=(LEFT+RIGHT)/2
    a,b,c=map(cuts,(LEFT,mid,RIGHT))
    assert [y for _,y in a]==[y for _,y in b]==[y for _,y in c]
    def faces(rows):
        return [item for j in range(len(rows)-1) for item in (rows[j][0],(rows[j][0]+rows[j+1][0])/2)]
    def words(alpha,rows):return [schedule(alpha,x) for x in faces(rows)]
    sig=words(mid,b)
    assert sig==words(LEFT,a)==words(RIGHT,c)
    short=set((v,w[:6]) for v,w in sig)
    for v,w in short: assert residue_energy(v,w)==direct(v,w)
    energies={t:residue_energy(*t) for t in set(sig)}
    e=max(energies.values()); assert e**5<3**(6*N)
    return {'N':N,'cap':str(CAP),'slope_interval':[str(LEFT),str(RIGHT)],'faces_at_each_slope':len(sig),'unique_full_schedules':len(energies),'direct_short_schedule_tests':len(short),'max_exact_modular_energy':e,'min_exact_modular_energy':min(energies.values()),'maximizing_midpoint_faces':[str(faces(b)[j]) for j,t in enumerate(sig) if energies[t]==e],'exact_power_bound':'E^5 < 3^(6 N)','source_count_exponent':'2/5','height_exponent':'5/2'}

if __name__=='__main__':print(json.dumps(run(),indent=2,sort_keys=True))
