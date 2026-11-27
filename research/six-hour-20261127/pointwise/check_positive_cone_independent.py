"""Independent finite interfaces for the positive-cone inverse minimum proof."""
from fractions import Fraction
import json

def require(ok, message):
    if not ok:
        raise ValueError(message)

def edge(n, sign):
    value = 3*n+sign
    require(value>0, 'positive signed magnitude')
    clock=0
    while value%2==0:
        value//=2
        clock+=1
    return value,clock

def first_hit(n, targets, sign):
    seen=set(); q=clock=0
    while n not in targets and n not in seen:
        seen.add(n)
        n,e=edge(n,sign)
        q+=1;clock+=e
    return (n,q,clock) if n in targets else None

phases=[]; n=17
while n not in phases:
    phases.append(n)
    n,_=edge(n,-1)
require(n==17 and phases==[17,25,37,55,41,61,91], 'marked cycle')
classes={t:[] for t in phases}
for n in range(1,92,2):
    if n in phases:
        continue
    hit=first_hit(n,set(phases),-1)
    if hit:
        classes[hit[0]].append(n)
f=lambda n:Fraction(3*n-1,3*n)
ratios=[]
for length in range(1,15):
    eligible=(classes[phases[length%7]]+list(range(93,123,2)))[:length]
    actual=reference=Fraction(1)
    for n in eligible:
        actual*=f(n)
    for i in range(length):
        reference*=f(phases[i%7])
    ratios.append(actual/reference)
require(min(ratios)==Fraction(9730834,9637047), 'strict phase-matched product bound')
pool=set()
for n in range(1,17,2):
    seen=set()
    while n not in seen:
        seen.add(n); pool.add(n)
        n,_=edge(n,1)
    require(n==1,'small positive starts must have complete checked orbits')
require(pool=={1,3,5,7,9,11,13,15,17,23,35,53},'positive pool')
rows=[];same_rank=[]
for D in range(1,6):
    for c in sorted(pool):
        if not 2**D<c<17*2**D:
            continue
        m=17*2**D-c
        hit=first_hit(m,{17},-1)
        rows.append([D,c,m,hit])
        if hit and hit[1]%7==0:
            same_rank.append([D,c,hit[1],hit[2]])
            require(hit[2]-11*(hit[1]//7)!=D,'unexcluded positive-cone witness')
require(len(rows)==33,'finite residual coverage')
require(same_rank==[[1,17,0,0],[2,35,7,12]],'same-rank candidates')
y=45295; n=y; exponents=[]
for _ in range(11):
    n,e=edge(n,1);exponents.append(e)
require(n==61219 and y<57327 and 57327%3==0, 'four-extra ordinary witness')
print(json.dumps({'scope':'independent finite interfaces, not the infinite proof','cycle':phases,'first_entry_classes':classes,'phase_matched_product_ratios':[str(r) for r in ratios],'minimum_ratio':str(min(ratios)),'positive_pool':sorted(pool),'complete_residual_pairs':rows,'same_rank_rows':same_rank,'four_extra_witness':{'source':y,'target':n,'principal':57327,'exponents':exponents}},indent=2))
