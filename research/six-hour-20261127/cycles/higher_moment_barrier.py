"""Even-order obstruction for the full binary corridor, using six coordinate copies."""
import json
from math import comb
from bridge_energy_certificate import LO,HI,WIDTH_FRACTION,STEPS,arrangement

def check(ok,reason):
    if not ok:raise ValueError(reason)

def transfer(x,up):
    k=len(x)-1
    if up:
        return tuple(sum(x[s]*comb(k-s,j-s)**2 for s in range(j+1)) for j in range(k+1))
    return tuple(sum(x[s]*comb(s,j)**2 for s in range(j,k+1)) for j in range(k+1))

def images(alpha,vec):
    ed=[f for f,_ in arrangement(alpha)]
    points=ed[:-1]+[(s+t)/2 for s,t in zip(ed,ed[1:])]
    ans={}
    for f in points:
        if f<=WIDTH_FRACTION:continue
        x=vec
        for j in range(1,STEPS+1):
            f+=alpha
            up=f>=1
            if up:f-=1
            x=transfer(x,up)
            if f>WIDTH_FRACTION:break
        if j in ans:check(ans[j]==x,'conflicting matrix action')
        ans[j]=x
    return ans

alpha=(LO+HI)/2
out={}
for k,vec,lo in [(1,(100000,62020),21),(3,(100000,386292,191206,15014),16749)]:
    den=50 if k==1 else 10000
    vals=images(alpha,vec)
    for n,x in vals.items():
        for a,b in zip(x,vec):
            check(a**den>b**den*3**(lo*n),'cone lower failed')
    out[str(k)]={'vector':vec,'three_images':vals,'lower_log3_rate':f'{lo}/{den}'}
print(json.dumps(out,indent=2,sort_keys=True))
