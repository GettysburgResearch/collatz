from pathlib import Path
from collections import Counter
from math import gcd
from sys import argv
import json
rows=json.loads(Path(argv[1]).read_bytes())

def advance(initial,den,ordinary,offset,tg):
    # Keep the odd denominator fixed even when the fraction reduces.
    center=initial
    phys=ordinary
    odd=0
    word=[]
    while center not in tg:
        bit=center%2
        assert (phys&1)==bit and phys>0
        assert den*phys-center == offset
        if bit:
            center=(3*center+den)//2
            phys=(3*phys+1)//2
            offset=(3*offset)//2
            odd+=1
        else:
            center//=2
            phys//=2
            offset//=2
        word.append(bit)
        assert len(word)<=700
    assert phys>0 and den*phys-center==offset
    return len(word),odd,center//den,phys

M=3**10
bucket=Counter()
words=Counter()
resids=[]
maxnums=[0,0,0,0]; walk=0
for row in rows:
    d,t,E,m=(row[v] for v in ('depth','index','evens','numerator'))
    den=3**d
    j=97+162*t
    p=d+E
    period=3**(d-4)
    assert 0<=t<period
    jet=1<<j
    numerator=(jet<<p)-m
    parent=(1024*jet-527)//81
    w=numerator//den
    assert 81*parent==1024*jet-527 and parent%48==17
    assert w%48==17 and den*w==numerator and 0<w<parent
    assert (1<<p)*81<1024*den and 2**97>527*den and 2**97>m
    # Stable raw power 2^(j+p) modulo 48*3^d, verified without cancelling 2.
    Q=48*den
    base=pow(2,j+p,Q)
    assert (base-m)%Q==17*den and base*pow(2,162*period,Q)%Q==base
    L=advance(-m,den,w,1<<(j+p),{-den})
    U=advance(-3*m,den,3*w,3<<(j+p),{0,den})
    h,o,minus,lower=L
    H,O,c,upper=U
    assert h<=j+p and H<=j+p and j>=o-d>=0 and h-o==E
    assert lower==3**(o-d)*(1<<(j-(o-d)))-1
    assert O+1>=d and upper==3**(O+1-d)*(1<<(j+p-H))+c
    if c==0:
        assert upper.bit_count()==1
        mode='power'; k=0
    else:
        # Choose k by the raw integer coefficient inequality, then replay all positive steps.
        k=0
        while 81*(1<<(40+p))*3**(O+1-d+k) >= 512*(1<<(H+2*k)):
            k+=1
        assert j+p-H>=2*k
        for _ in range(k):
            assert upper%4==1
            nxt=(3*upper+1)//2
            assert nxt%2==0
            upper=nxt//2
        assert upper==3**(O+1-d+k)*(1<<(j+p-H-2*k))+1
        assert 2**40*upper<parent
        mode='contraction'
    if t==181 and d==11:
        assert (p,m,j,h,o,H,O,c)==(21,3170149,29419,21,11,24,10,1)
        assert 81*2**40*3**100 < (512*8)*4**100 and 3**100*(1<<(j-203))+1 < parent//(1<<40)
        print('example',j,L[:3],U[:3],k)
    words[d,mode]+=1
    bucket[d,mode]+=M//period
    resids.append((t,period))
    walk+=h+H+2*k
    maxnums=[max(maxnums[0],h),max(maxnums[1],H),max(maxnums[2],k),max(maxnums[3],j)]
# Independent residue disjointness via CRT criterion, not cross-updating lift sets.
for i,(a,b) in enumerate(resids):
    for c,d in resids[:i]:
        assert (a-c)%gcd(b,d)
print('rows by depth/kind',sorted(words.items()))
print('lifts by depth/kind',sorted(bucket.items()))
print('totals',len(resids),sum(v for (d,m),v in bucket.items() if m=='power'),sum(v for (d,m),v in bucket.items() if m=='contraction'),M-sum(bucket.values()))
print('clocks replayed',walk,'max h,H,pairs,j',maxnums)
