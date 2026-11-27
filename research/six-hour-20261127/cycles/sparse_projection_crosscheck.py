"""Independent path enumeration for the clipped affine numerator on marked segments."""
from collections import defaultdict
from itertools import combinations_with_replacement
import json

def insist(ok, message):
    if not ok:
        raise RuntimeError(message)

def carry(gaps):
    c, scale = 0, 1
    for e in gaps:
        c = 3*c + scale
        scale <<= e
    return c

def check(binary):
    den, step, numer_cap = 600, 351, (588 if binary else 384)
    n = 13
    groups = defaultdict(list)
    paths = high = 0
    for intercept in [0,33,384,401,588,599]:
        fs = [(intercept+i*step)%den for i in range(n+1)]
        m = [1+int(fs[i]+step>=den) for i in range(n)]
        def rec(zs):
            nonlocal paths, high
            i = len(zs)-1
            if i==n:
                if zs[-1]>1 or zs[-1]*den+fs[-1]>den+numer_cap:
                    return
                paths+=1
                high=max(high,max(zs))
                clipped=[min(z,1) if f<=numer_cap else 0 for z,f in zip(zs,fs)]
                e=[m[k]+zs[k]-zs[k+1] for k in range(n)]
                ec=[m[k]+clipped[k]-clipped[k+1] for k in range(n)]
                insist(all(v>=1 and (not binary or v<=2) for v in ec),'projection invalid')
                marks=tuple((k,z) for k,z in enumerate(zs) if z*den+fs[k]>den+numer_cap)
                # These two placements force both marked and unmarked entrances.
                for l,r in [(3,10),(5,12)]:
                    tag=(intercept,marks,l,r,zs[l],zs[r])
                    groups[tag].append((carry(e[l:r]),carry(ec[l:r]),zs[l]-clipped[l],tuple(zs[l:r+1]),tuple(clipped[l:r+1])))
                return
            low=max(0,m[i]+zs[-1]-2) if binary else 0
            for z2 in range(low,min(m[i]+zs[-1]-1,4)+1):
                rec(zs+[z2])
        for z0 in [0,1]:
            if z0*den+fs[0]<=den+numer_cap:
                rec([z0])
    nontriv=reverse_fail=pair_checks=0
    for rows in groups.values():
        values=set(rows)
        ds={a-(b<<s) for a,b,s,_,_ in values}
        insist(len(ds)==1,'affine projection shift varied')
        tab={}
        for a,b,s,orig,proj in values:
            if proj in tab:
                insist(tab[proj]==orig,'noninjective at fixed record')
            tab[proj]=orig
        small=list(dict.fromkeys((a,b,s) for a,b,s,_,_ in values))[:7]
        if len(small)>1 and small[0][2]>0:
            nontriv+=1
            if len({(a<<s)-b for a,b,s in small})>1:reverse_fail+=1
        sums={}
        for p,q in combinations_with_replacement(small,2):
            a,b=p[0]+q[0],p[1]+q[1];pair_checks+=1
            if a in sums:insist(sums[a]==b,'unequal projected pair sums')
            sums[a]=b
        insist(len(set(sums.values()))==len(sums),'unchanged projected pair sums hid inequality')
    insist(nontriv and reverse_fail==nontriv,'missing scale control')
    return dict(paths=paths,max_grade=high,groups=len(groups),distinct_marked_entrance_groups=nontriv,wrong_scaling_refuted=reverse_fail,pair_sum_checks=pair_checks)
print(json.dumps({k:check(v) for k,v in [('binary',True),('all',False)]},sort_keys=True,indent=2))
