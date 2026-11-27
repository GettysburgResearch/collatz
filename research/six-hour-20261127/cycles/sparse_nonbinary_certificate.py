"""Check the exceptional mechanical-run repair on exact small positive-gap paths."""
from collections import Counter, defaultdict
from fractions import Fraction as F
from math import floor
import json
from sparse_grade_certificate import languages, need, numeral, constants


def repair(m, w, exceptional):
    changed=list(w)
    indices=set()
    i=0
    while i<len(m):
        if m[i]!=2:
            i+=1
            continue
        j=i
        while j<len(m) and m[j]==2:
            j+=1
        need(j-i<=2,'three consecutive mechanical twos')
        if exceptional.intersection(range(i,j)):
            indices.update(range(i,j+1))
            for k in range(j-1,i-1,-1):
                changed[k]=min(changed[k],changed[k+1])
        i=j
    return tuple(changed),indices


def run():
    a=F(31,53)
    c=F(49,50)
    paths=repairs=groups_count=0
    joint=0
    maxgap=0
    for t in (F(0),F(1,4),c,F(499,500)):
        rawphase=[t+a*i for i in range(8)]
        f=tuple(x%1 for x in rawphase)
        m=[1+floor(y)-floor(x) for x,y in zip(rawphase,rawphase[1:])]
        for start in (0,1,2,3):
            classes=defaultdict(list)
            for z,e in languages(m,start,False):
                deep=tuple((i,v) for i,v in enumerate(z) if v+f[i]>1+c)
                w=tuple(min(v,1) if u<=c else 0 for v,u in zip(z,f))
                bad={i for i,u in enumerate(e) if u>=3}
                repaired,record=repair(m,w,bad)
                steps=tuple(k+u-v for k,u,v in zip(m,repaired,repaired[1:]))
                need(all(v in (1,2) for v in steps),'repair left a nonbinary edge')
                need(all(v==0 or u<=c for v,u in zip(repaired,f)),'repair broke real cap')
                key=(z[0],z[-1],deep,tuple(sorted(bad)),tuple((i,w[i]) for i in sorted(record)))
                classes[key].append((numeral(e),numeral(steps),repaired[0]))
                paths+=1
                repairs+=(repaired!=w)
                joint+= bool(deep and bad and repaired!=w)
                maxgap=max(maxgap,max(e))
            for (head,tail,deep,bad,rec),pool in classes.items():
                need(len({v-2**(head-c0)*w for v,w,c0 in pool})==1,'record affine collision')
                need(len({w for v,w,c in pool})==len(pool),'repaired path not injective')
                groups_count+=1
    pars=constants(F(1,10000),F(1,80000),F(1,100000),F(999,1000),24)
    return {'paths':paths,'nontrivial_repairs':repairs,'records':groups_count,
            'nontrivial_repairs_with_both_marks':joint,'maximum_actual_gap':maxgap,
            'margins':pars}

if __name__=='__main__':
    print(json.dumps(run(),indent=2,sort_keys=True))
