#!/usr/bin/env python3
"""Reviewer-owned exact spot and finite-corpus checks; no source-module imports.
No all-depth, formal-build, or external payload verification is implied.
"""
from __future__ import annotations
import argparse, hashlib, itertools, json, math, subprocess, sys
from fractions import Fraction as F
from pathlib import Path

BASE='9704bcf1ff33cc9e2b729e0c40137a1e55b95397'
HEADS={'87':'e9adc409031a61f3801c4ee1e1e6deeb34188eb7','88':'c28922fb6d1c070bf86a76192f40bc9ea3edd67c','90':'78ac7c8489f1df81230402808b1f4b77b18fae73'}

def need(ok, label):
    if not ok: raise ValueError(label)
def step(n): return (3*n+1)//2 if n%2 else n//2
def vp(n,p=3):
    n=abs(n); need(n>0,'zero valuation'); e=0
    while n%p==0:n//=p;e+=1
    return e
def rank(n):return (2*n+1)**2//3**vp(2*n+1)
def physical(n,word):
    for b in word:
        need(n%2==int(b),'parity guard');n=step(n);need(n>0,'positive source')
    return n
def data(w):
    # Backward affine composition independently constructs the forward formula.
    a,b=F(1),F(0)
    for bit in reversed(w):
        if bit=='1':a*=F(2,3);b=(2*b-1)/3
        else:a*=2;b*=2
    P=1<<len(w); Q=int(F(P)/a); A=int(-b*Q)
    return P,Q,A,2*A+P-Q

def ret(n):
    need(n>1 and n%3==1,'section domain');x=step(n)
    for _ in range(100000):
        if x%3==1:return x
        x=step(x)
    raise ValueError('section budget')
def fan(y):
    # Physical inverse traversal, stop at first section entry.
    out=[]; todo=[2*y]
    while todo:
        z=todo.pop()
        if z%3==1:out.append(z);continue
        if z%3==0:continue
        todo.append(2*z)
        if z%3==2:todo.append((2*z-1)//3)
    return sorted(out)
def explicit_fan(y):
    h=vp(2*y+1);u=(2*y+1)//3**h
    out=[2*(2**j*3**(h-j)*u-1) for j in range(h)]
    z=2**h*u-1
    if z%3==1:out.append(z)
    return sorted(out)
def inv_ball(y,depth,boundary_only=False):
    seen={y}; layer={y}
    for _ in range(depth):
        nxt=set()
        for z in layer:
            if z==1:continue
            xs=fan(z)
            if boundary_only:
                h=vp(2*z+1);u=(2*z+1)//3**h
                xs=[3*2**h*u-2]+([2**h*u-1] if (2**(h+1)*u-1)%3==0 else [])
            nxt.update(xs)
        seen.update(nxt);layer=nxt
    return seen

def constants():
    tests={
      'pred_A':76981049**1000*2**1802<=2**28000,
      'pred_B1':207142911**1000*2**1802<=2**28000*3**901,
      'pred_B3':386810365**1000*2**901<=2**28000*3**901,
      'adaptive_delta':3**3<2**5,
      'fh_floor':19501**6309<2**10000*6500**6309,
      'fh_entropy':10000**10000<2**9500*3691**3691*6309**6309,
      'dyadic_closure':2*93**10<100**10,
      'rate_margin':F(5,143)-F(6993,200000)==F(1,28600000),
      'raw_clock':1509503==3*501501+5000,
      'core_predecessor_exponent_reserve':F(901,1000)-F(9,10)==F(1,1000),
    }
    # Outward rational lower bound on ln 2 from its atanh series.
    ln2lo=2*sum((F(1,(2*j+1)*3**(2*j+1)) for j in range(16)),F(0))
    tests['Csyr145']=F(501501,5000)<145*ln2lo
    tests['Craw436']=F(1509503,5000)<436*ln2lo
    A,B1,B3=76981049,207142911,386810365
    for k,(lhs,rhs) in enumerate(((2134179986800640,A*6357317+B1*7945915),(1036938517676032,A*13483121),(1706529287831552,A*2896800+B3*3838338)),1):
        tests['appendix_row_'+str(k)]=lhs<=rhs
    for k,v in tests.items():need(v,k)
    return {'passed':sorted(tests),'ln2_lower':str(ln2lo)}

def cylinders():
    checked=rot=0;rows=[]
    for L in range(1,13):
        words={};sc=nd=0
        for n in range(1,2**L+1):
            x=n; w='';q=0;ballot=True;desc=False
            for j in range(1,L+1):
                b=x%2;w+=str(b);q+=b;ballot &=3**q>=2**j;x=step(x);desc |=x<n
            need(w not in words,'parity bijection');words[w]=n%2**L
            P,Q,A,B=data(w);need((Q*n+A)//P==x and (Q*n+A)%P==0,'affine endpoint')
            need(((-A*pow(Q,-1,P))%P)==n%P,'canonical root')
            if ballot:sc+=1;need(not desc,'ballot descent')
            if not desc:nd+=1
            if Q>P:
                good=False
                for shift in range(L):
                    q0=0;ok=True;v=w[shift:]+w[:shift]
                    for j,b in enumerate(v,1):
                        q0+=int(b)
                        if 3**q0<2**j:ok=False;break
                    if ok:good=True;break
                need(good,'cyclic rotation');rot+=1
            checked+=1
        need(len(words)==2**L,'coverage')
        rows.append([L,sc,nd])
    return {'max_depth':12,'sources':checked,'positive_surplus_rotation_words':rot,'rows':rows}

def first_passage():
    rows=[]
    for X,Y,L in ((256,16,8),(512,32,10)):
        direct={}
        for n in range(Y+1,X+1):
            x=n;w=''
            for j in range(1,L+1):
                w+=str(x%2);x=step(x)
                if x<=Y:direct[n]=(j,x,w);break
        compiled={}
        for j in range(1,L+1):
            for bits in itertools.product('01',repeat=j-1):
                w=''.join(bits)+'0';P,Q,A,_=data(w)
                lo=Y//2+1;hi=min(Y,(A+Q*X)//P)
                for i in range(j):
                    Pi,Qi,Ai,_=data(w[:i])
                    lo=max(lo,(Qi*A+Q*(Pi*Y-Ai))//(Qi*P)+1)
                for y in range(lo,hi+1):
                    if (P*y-A)%Q:continue
                    n=(P*y-A)//Q;need(n not in compiled,'duplicate passage');compiled[n]=(j,y,w)
        need(direct==compiled,'first-passage complete AP/source equality')
        rows.append({'X':X,'Y':Y,'clock':L,'defined':len(direct),'unresolved':X-Y-len(direct)})
    need([r['defined'] for r in rows]==[99,233],'published first-passage counts')
    return rows

def drift_certificate():
    # Reconstruct the published deliberately enlarged finite-X bound, not source code.
    def ceilfrac(x):return -(-x.numerator//x.denominator)
    def bound(m,r):
        AA=[ceilfrac(F(8,5)**i*(m+2)) for i in range(r)]
        BB=[ceilfrac(F(8,5)**(i+1)*(m+2)) for i in range(r)]
        D=[]
        for i in range(r+1):
            pref=math.prod(AA[j]*BB[j] for j in range(i))
            D.append(pref*F(25,2)**(r-i)*F(5,4)**sum(AA[i:]))
        e=F(1,2**(m//2)); p=F(173,200)
        return F(9,8)**r*(p**r+e*sum((p**(r-i) for i in range(1,r+1)),F(0))+F(2,2**m)*(D[0]+e*sum(D[1:])))
    rows=[]
    for r,start,cap in ((1,18,F(99,100)),(2,128,F(19,20))):
        for m in range(start,start+25):
            b=bound(m,r);need(b<cap,'cofinal base');rows.append([r,m,str(b)])
    ratios=[F(5,4)**25/2**25,F(9,4)**2/2**37,F(5,4)**65/2**25,F(6,5)**2*F(5,4)**40/2**37,F(6,5)**4/2**37]
    need(all(x<1 for x in ratios),'cofinal induction ratios')
    # Direct pressure upper bound, using safe rational radical enclosures.
    p=F(1732051,1000000)/((2*F(1414213,1000000)-F(1732051,1000000))*(2*F(1414213,1000000)-1))
    need(F(1414213,1000000)**2<2 and F(1732051,1000000)**2>3 and p<F(173,200),'pressure radicals')
    return {'base_count':len(rows),'base_digest':hashlib.sha256(json.dumps(rows).encode()).hexdigest(),'induction_ratios':list(map(str,ratios))}

def rank_checks():
    fans=0;radius=0;residual=0
    residual_classes={139,427,571,859,1003}
    for y in range(4,16385,3):
        xs=fan(y);need(xs==explicit_fan(y),'complete fan');need(all(ret(x)==y for x in xs),'fan physical returns');fans+=1
        h=vp(2*y+1);u=(2*y+1)//3**h;k=vp(2**(h+1)*u-1)
        I=2**h*u-1 if k else 3*2**h*u-2
        need(rank(I)==min(map(rank,xs)),'one-generation minimum')
        if y<4096:
            bs=[3*2**h*u-2]+([2**h*u-1] if k else [])
            candidates=[y]+bs+[min(fan(b),key=rank) for b in bs]
            need(min(map(rank,candidates))==min(map(rank,inv_ball(y,2))),'radius-two five-candidate theorem');radius+=1
        if y%2 and h==2:
            candidates=[ret(y),ret(ret(y)),*xs]
            if vp(y+1,2)==2 and y%16==3:candidates.append((3*y-1)//8)
            if min(map(rank,candidates))>=rank(y):
                need(y%1296 in residual_classes,'h2 necessary residual');residual+=1
    need(min(inv_ball(208363,3),key=rank)==4445077,'interior counterexample')
    need(min(inv_ball(208363,3,True),key=rank)==208363,'boundary-only counterexample')
    need(physical(69619,'110010')==29371,'non-greedy witness')
    low=[n for n in range(1,121) if rank(n)<rank(121)]
    closure=set();todo=low[:]
    while todo:
        x=todo.pop()
        if x in closure:continue
        closure.add(x);todo.append(step(x))
    need(low==[1,2,3,4,5,6,7,10,13,22,40],'complete lower-rank set')
    x=121;j=0
    while x not in closure:x=step(x);j+=1
    need((j,x)==(54,40),'minimum forward meeting clock')
    need(121 not in closure and all(step(x) in closure for x in closure),'all-depth inverse obstruction')
    # Complete T^5 word test, retaining all-zero/nonpositive denominators.
    fixed=[]
    for bits in itertools.product('01',repeat=5):
        w=''.join(bits);P,Q,A,_=data(w)
        if P>Q and A>0 and A%(P-Q)==0:fixed.append((w,A//(P-Q)))
    need(not fixed,'period-five exclusion')
    named=[(769,'10',1822,'01111000'),(859,'1101110101011100',517,'1'),(661,'1000001',73,'1011100'),(8779,'1101000001',975,'1111001100')]
    for n,v,x,w in named:need(physical(n,v)==physical(x,w) and rank(x)<rank(n),'named merging diagram')
    return {'complete_fans':fans,'radius_two_balls':radius,'h2_residual_no_violation':residual,'lower_rank_121':low,'closure_121':sorted(closure),'minimum_clock_121':54,'T5_words':32,'named_diagrams':len(named)}

def phase_checks():
    rows=[]
    for n,x in ((13,1),(859,95)):
        paths=[]
        for v in (n,x):
            path=[v]
            while path[-1]!=1:
                need(len(path)<10000,'phase budget');path.append(step(path[-1]))
            paths.append(path)
        need((len(paths[0])-len(paths[1]))%2==1,'opposite eventual cycle phases')
        for j in range(max(map(len,paths))+2):
            a=paths[0][j] if j<len(paths[0]) else (1 if (j-len(paths[0])+1)%2==0 else 2)
            b=paths[1][j] if j<len(paths[1]) else (1 if (j-len(paths[1])+1)%2==0 else 2)
            need(a!=b,'synchronous counterexample')
        rows.append([n,x,len(paths[0])-1,len(paths[1])-1])
    return rows

def green():
    X=2**18; K=256; bits=80; cache={1:0}; counts=[]
    sums={k:0 for k in (16,32,64,128,256)}; unresolved=0
    geoms=[F(0)];term=F(1)
    for _ in range(257):geoms.append(geoms[-1]+term);term*=F(65,64)
    for n in range(2,X+1):
        x=n;path=[]
        while x not in cache and len(path)<=K:path.append(x);x=step(x)
        if x in cache:
            t=cache[x]
            for y in reversed(path):t+=1;cache[y]=t
            t=cache[n]
        else:t=K+1
        if t>K:unresolved+=1
        for k in sums:
            g=geoms[min(t,k+1)]
            sums[k]+=(3**vp(n+1)*g.numerator*2**bits)//((n+1)**2*g.denominator)
    e=0
    while 3**(e+1)<=X+2:e+=1
    tail=F(2*e+5,X+2)
    for k,s in sums.items():
        lo=F(s,2**bits);hi=lo+F(X-1,2**bits)+tail*geoms[k+1]
        counts.append({'K':k,'floor_sum':str(s),'lower':str(lo),'upper':str(hi)})
    need(unresolved==1,'Green unresolved count')
    need(F(counts[-1]['lower'])>F(86140,10000) and F(counts[-1]['upper'])<F(89619,10000),'Green global enclosure')
    return {'sources':X-1,'unresolved_at_256':unresolved,'all_source_tail':str(tail),'rows':counts}

def transported():
    H=2**18;bits=80;points=list(range(H+1,2*H,2));rows=[]
    # Direct packet law, killed on <=H. Original input stays fixed in denominator.
    for j in range(25):
        s=0;alive=0
        for i,x in enumerate(points):
            if not x:continue
            n=H+1+2*i
            s+=math.isqrt(((x+1)*2**(2*bits))//(n+1));alive+=1
        fac=F(9,8)**j*F(2,H)
        lo=fac*F(s,2**bits);hi=fac*F(s+alive,2**bits)+F(1,2**120)
        if j in (0,1,2,21,22,23,24):rows.append({'j':j,'lower':str(lo),'upper':str(hi),'alive':alive})
        if j<24:
            for i,x in enumerate(points):
                if not x:continue
                # Literal maximal odd run then even run; no affine packet evaluation.
                while x%2:x=step(x)
                while x%2==0:x//=2
                points[i]=x if x>H else 0
    by={r['j']:r for r in rows}
    for j in (21,22,23):need(F(by[j+1]['lower'])>F(by[j]['upper']),'actual transported drift counterexample')
    p=-(-(((F(8,5)**24-1)/2).numerator)//((F(8,5)**24-1)/2).denominator)
    need(p==39614 and -4*(2**19-H)+21*p+24==-216658,'omitted shell exponent')
    return {'initial_odd_sources':H//2,'packet_horizon':24,'rows':rows,'omitted_source_mass_upper':'2^-216657'}

def shadow_frontier():
    # A physical signed inverse walk, not the source affine fan implementation.
    def signed_edges(y):
        out=[]; cur=2*y; suffix='0'; h=vp(2*y+1)
        while cur%3==2:
            w='0'+suffix; out.append((2*cur,w,h-w.count('1')))
            cur=(2*cur-1)//3; suffix='1'+suffix
            if cur%3==1:
                out.append((cur,suffix,0)); break
            if cur%3==0: break
        return out
    tables=[]; thresholds=[]
    found={-2:(0,'')}; layer=[-2]
    for r in range(11):
        cost=1+max(w.count('1')+vp(2*x+1) for x,(d,w) in found.items())
        need(cost<=(r+1)**2+1,'shadow polynomial budget')
        thresholds.append(cost); tables.append([r,len(found),cost])
        nxt=[]
        for y in layer:
            for x,w,_ in signed_edges(y):
                need(x not in found and x<=-2,'negative tree uniqueness')
                full=w+found[y][1]; z=x
                for bit in full:need(z%2==int(bit),'signed parity');z=step(z)
                need(z==-2,'signed replay')
                found[x]=(r+1,full);nxt.append(x)
        layer=nxt
    def ball(root,D,reduced):
        seen={root};front={root}
        for d in range(D):
            nxt=set()
            for y in front:
                if y==1:continue
                for x,w,gap in signed_edges(y):
                    if reduced and gap>=thresholds[D-d-1]:continue
                    if x not in seen:nxt.add(x)
            seen|=nxt;front=nxt
        return seen
    cases=[(n,d) for n in range(4,194,3) for d in range(1,7)]
    cases += [(208363,3),(29371,2),(121,8),(859,6)]
    for n,d in cases:
        complete,pruned=ball(n,d,False),ball(n,d,True)
        need(min(map(rank,complete))==min(map(rank,pruned)),'depth-aware pruning')
    need(min(ball(208363,3,True),key=rank)==4445077,'restored interior')
    need(thresholds==[2,2,3,4,6,7,13,14,15,16,19],'published precision table')
    return {'negative_table':tables,'complete_vs_pruned_cases':len(cases),
            'scope':'all negative nodes through radius 10; modest physical positive-root sample only'}

def optimized_acceptance_probe():
    # Exact acceptance-function structure of X-ASTRA-003 verify.py at the frozen
    # source SHA. This is an isolated reproduction, NOT a run of that full file.
    text = """import hashlib,json
from fractions import Fraction as F
def digest(payload):
    return hashlib.sha256(json.dumps(payload,sort_keys=True,separators=(',',':'),ensure_ascii=True).encode()).hexdigest()
def validate(report, expected):
    assert set(report)=={'payload','sha256'},'report fields'
    assert digest(report['payload'])==report['sha256'],'digest'
    assert set(report['payload'])==set(expected),'payload coverage'
    for section in expected:
        assert report['payload'][section]==expected[section],f'incorrect {section} mathematics, scope, or coverage'
expected={'scope':'finite only','coverage':237}
wrong={'scope':'all-time Collatz proof','coverage':1}
r={'payload':wrong,'sha256':digest(wrong)}
validate(r,expected)
print('ACCEPTED')
"""
    normal=subprocess.run([sys.executable,'-c',text],text=True,capture_output=True)
    optimized=subprocess.run([sys.executable,'-O','-c',text],text=True,capture_output=True)
    need(normal.returncode!=0 and 'AssertionError' in normal.stderr,'normal source-style rejection')
    need(optimized.returncode==0 and optimized.stdout.strip()=='ACCEPTED','optimized acceptance reproduction')
    return {'source':'experiments/X-ASTRA-003-run-renewal/verify.py',
            'source_sha':HEADS['90'],'normal':'rejected','optimized':'accepted',
            'scope':'isolated acceptance function reproduced; full source command not executed',
            'reproducer_sha256':hashlib.sha256(text.encode()).hexdigest()}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--full-finite',action='store_true');a=ap.parse_args()
    out={'schema':'reviewer-a-exact-v1','scope':'finite reviewer reconstructions only; no Collatz proof, Lean build, PDF hash replay, or large external payload','baseline':BASE,'source_heads':HEADS,
         'constants':constants(),'cylinders':cylinders(),'first_passage':first_passage(),'cofinal_drift':drift_certificate(),'rank':rank_checks(),'phase':phase_checks(),'shadow_frontier':shadow_frontier(),'optimized_acceptance':optimized_acceptance_probe()}
    if a.full_finite:out.update(green=green(),transported=transported())
    serial=json.dumps(out,sort_keys=True,separators=(',',':'));report={'payload':out,'sha256':hashlib.sha256(serial.encode()).hexdigest()}
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(report,sort_keys=True,indent=2)+'\n');print(report['sha256']);print('REVIEWER EXACT CHECKS PASS')
if __name__=='__main__':main()
