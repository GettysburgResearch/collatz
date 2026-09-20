#!/usr/bin/env python3
"""All-gap long-block compiler and delayed signed shadows. Proposed mathematics."""
import argparse
import functools
import hashlib
import importlib.util
import json
from pathlib import Path
from fractions import Fraction

GAP_MODES = ('long','old','long_alt')


def need(ok, msg):
    if not ok: raise ValueError(msg)


def v2(n):
    need(type(n) is int and n > 0, 'valuation domain')
    return (n & -n).bit_length()-1


def T(n):
    need(type(n) is int, 'integer')
    return (3*n+1)//2 if n % 2 else n//2


def trace(n,L):
    w=''
    for _ in range(L):
        w+=str(n%2);n=T(n)
    return n,w


_GAP_CACHE = {}


def gap(g,mode='long'):
    """Iterative recursion/unwind, so integer bit length is not a Python recursion limit."""
    need(type(g) is int and g >= 1, 'positive gap')
    need(mode in ('long','old','long_alt'), 'gap mode')
    original=g;stack=[]
    while (g,mode) not in _GAP_CACHE:
        if g==1:
            _GAP_CACHE[g,mode]=(32,5,'10001','01100') if mode=='long_alt' else (8,4,'001','100')
            break
        if g%2==0:
            stack.append((g,g//2,0,''));g//=2;continue
        if mode=='old' or (mode in ('long','long_alt') and g==3):
            j=1;sign='minus' if g%4==3 else 'plus'
            h=(3*g-1)//4 if sign=='minus' else (3*g+1)//4
        else:
            sign='minus' if g%4==1 else 'plus'
            j=v2(3*g+(1 if sign=='minus' else -1))
            h=(((3*g+1)//2**j-1)//2 if sign=='minus' else ((3*g-1)//2**j+1)//2)
        need(0 <= h < g, 'strict gap descent')
        if h==0:
            need(sign=='minus','zero branch')
            _GAP_CACHE[g,mode]=(2**(j+1),2**j,'0'*j+'1','1'+'0'*j)
            break
        stack.append((g,h,j,sign));g=h
    while stack:
        g,h,j,sign=stack.pop();M,B,w,z=_GAP_CACHE[h,mode]
        if j==0:
            _GAP_CACHE[g,mode]=(2*M,2*B,'0'+w,'0'+z);continue
        P=2**(j+1);subtract=2**j if sign=='minus' else 1
        target=subtract*pow(P,-1,3)%3
        t=(target-B)*pow(M,-1,3)%3
        newB=(P*(B+M*t)-subtract)//3
        need(0<newB<P*M,'positive canonical source')
        prew='0'*j+'1' if sign=='minus' else '1'+'0'*j
        prez='1'+'0'*j if sign=='minus' else '0'*j+'1'
        _GAP_CACHE[g,mode]=(P*M,newB,prew+w,prez+z)
    return _GAP_CACHE[original,mode]


def affine_replay(M,B,w):
    need(type(M) is int and M>0 and type(B) is int,'affine input')
    for bit in w:
        need(M%2==0 and B%2==int(bit),'whole-cylinder parity')
        if bit=='1': M,B=3*M//2,(3*B+1)//2
        else: M,B=M//2,B//2
    return M,B


def gap_row(g,mode):
    M,B,w,z=gap(g,mode)
    need(len(w)==len(z) and M==2**len(w),'length/modulus')
    need(w.count('1')==z.count('1'),'odd count')
    endpoint=affine_replay(M,B,w)
    need(endpoint==affine_replay(M,B+g,z),'gap endpoint')
    if mode=='long':
        # Rational, weaker consequence of the proved logarithmic exponent bound.
        need(g==1 or M**4 <= 16**4*(g-1)**9,'9/4 bound')
    return {'kind':'gap','g':g,'mode':mode,'M':M,'B':B,'words':[w,z], 'endpoint':list(endpoint)}


@functools.lru_cache(maxsize=None)
def shadow(a,b,k,seed=1):
    """seed 1: -2^k; seed 3: -3*2^k -> -1 in k+3 steps."""
    need(type(a) is int and a>=1 and type(b) is int and type(k) is int and k>=0,'shadow inputs')
    need(seed in (1,3),'seed')
    e=k+(2 if seed==3 else 0)
    c=3**a*seed*2**k-b
    if c<=2**(a+e): return None
    x=-c; w='';evens=0
    while evens<a+e:
        need(x < -1, 'negative path must avoid fixed point')
        p=x%2;w+=str(p);evens+=1-p;x=T(x)
    L=len(w); h=-x
    lower=('0'*k+'100'+'1'*(L-k-3)) if seed==3 else ('0'*k+'1'*(L-k))
    need(L>=k+(3 if seed==3 else 0),'lower preperiod completed')
    need(trace(-seed*2**k,L)==(-1,lower),'lower signed prefix')
    need(h>1 and lower.count('1')-w.count('1')==a,'balanced shadow')
    return L,h,w,lower


def shadow_row(a,b,k,seed=1,mode='long'):
    data=shadow(a,b,k,seed)
    need(data is not None,'shadow guard')
    L,h,w,z=data
    M,B,p,q=gap(h-1,mode)
    slope=3**z.count('1')
    u=(B+h)*pow(slope,-1,M)%M
    if u==0: u=M
    d=2**L*u-seed*2**k
    period=2**L*M
    # Keep a positive tail without changing the residue class.
    while d<=0 or 3**a*d+b<=0:
        d+=period
    W=w+p;Z=z+q
    E=affine_replay(3**a*period,3**a*d+b,W)
    need(E==affine_replay(period,d,Z),'affine cylinder equality')
    need(v2(d)==k,'exact valuation')
    return {'kind':'shadow','a':a,'b':b,'k':k,'seed':seed,'mode':mode,
            'L':L,'h':h,'prefixes':[w,z],'d':d,'period':period,'words':[W,Z], 'endpoint':list(E)}


def direct_gate(C,seed,mode):
    k=v2(C);a=2;b=2
    data=shadow(a,b,k,seed)
    if data is None:return None
    L,h,w,z=data
    if (C+seed*2**k)%2**L:return None
    u=(C+seed*2**k)//2**L
    low=3**z.count('1')*u-h
    if low<=0:return None
    M,B,p,q=gap(h-1,mode)
    if low%M!=B:return None
    return w+p,z+q,'delayed-'+str(seed)+'-'+mode


def balanced_probe(C,depth=12):
    """Actual prefixes only; reject coefficient imbalance and core-assisted probes."""
    x,y=9*C+2,C;w=z='';delta=2
    for _ in range(depth):
        if min(x,y)<=2:return None
        px,py=x%2,y%2;delta+=px-py
        w+=str(px);z+=str(py);x,y=T(x),T(y)
        if delta!=0:continue
        if x==y:return w,z,'balanced-direct'
        low,high=min(x,y),max(x,y)
        for mode in GAP_MODES:
            M,B,p,q=gap(high-low,mode)
            if low%M!=B:continue
            return (w+p,z+q,'balanced-'+mode) if x<y else (w+q,z+p,'balanced-'+mode)
    return None


def new_gate(C):
    for seed in (1,3):
        for mode in GAP_MODES:
            ans=direct_gate(C,seed,mode)
            if ans:return ans
    return balanced_probe(C)


def load_parent():
    path=Path(__file__).resolve().parents[1]/'anchored-returns'/'run.py'
    raw=path.read_bytes()
    need(hashlib.sha1(('blob '+str(len(raw))+'\0').encode()+raw).hexdigest()==
         '0ba3954be102188790e05cefa3630e3cb0dbccbc','pinned parent blob')
    spec=importlib.util.spec_from_file_location('anchor_parent',path)
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    return mod


def classify(C,parent):
    source=C;W=Z='';swapped=False;tags=[]
    for _ in range(1000):
        gate=new_gate(C)
        if gate:
            w,z,tag=gate
            W+=z if swapped else w;Z+=w if swapped else z;tags.append(tag)
            endpoint,actualW=trace(9*source+2,len(W));other,actualZ=trace(source,len(Z))
            need(actualW==W and actualZ==Z and endpoint==other,'original new replay')
            return {'kind':'comparison','C':source,'status':'MERGE','endpoint':endpoint,'words':[W,Z],'tags':tags}
        old=parent.transition(C,True)
        if old is None:return {'kind':'comparison','C':source,'status':'OUTSIDE','last':C,'tags':tags}
        status,out,L,tag=old
        _,w=trace(9*C+2,L);_,z=trace(C,L)
        W+=z if swapped else w;Z+=w if swapped else z;tags.append(tag)
        if status=='MERGE':
            need(trace(9*source+2,len(W))==(out,W) and trace(source,len(Z))==(out,Z),'parent replay')
            return {'kind':'comparison','C':source,'status':'MERGE','endpoint':out,'words':[W,Z],'tags':tags}
        C=out;swapped=not swapped
    return {'kind':'comparison','C':source,'status':'BUDGET','last':C,'tags':tags}


def lifted_row(k,seed):
    family=shadow_row(2,2,k,seed)
    M,B=family['period'],family['d'];w,z=family['words']
    gamma=current=Fraction(9)
    for bit in w:
        current*=Fraction(3 if bit=='1' else 1,2)
        gamma=min(gamma,current)
    r=2
    while gamma*3**(r-1)<=8*2**r:r+=1
    modulus=3**r
    target=3**(r-1)*pow(2**r,-1,3)%modulus
    t=(target-(4*B+1))*pow(4*M,-1,modulus)%modulus
    C=B+M*t;u=(4*C+1)//3**(r-1);n=2**r*u-1;m=(n-3)//4
    endpoint,W=trace(n,r+2+len(w));other,Z=trace(m,r+len(z))
    need(endpoint==other and 0<4*m<n and n%3==0,'lift')
    x=n;low=None
    for _ in W:
        x=T(x);low=x if low is None else min(low,x)
    need(low>n,'strict all-states bound')
    return {'kind':'lift','k':k,'seed':seed,'r':r,'u':u,'n':n,'m':m,'C':C,
            'words':[W,Z],'endpoint':endpoint,'minimum':low}


def first_meeting_row(C,budget=1000):
    x,y=9*C+2,C;w=z=''
    for _ in range(budget):
        if x==y:
            return {'kind':'meeting_type','C':C,'words':[w,z],'endpoint':x,
                    'type':'ROBUST' if z.count('1')-w.count('1')==2 else 'ISOLATED_ONLY'}
        w+=str(x%2);z+=str(y%2);x,y=T(x),T(y)
    raise ValueError('meeting test budget')


def neighborhood_row(C,extra):
    first=first_meeting_row(C);need(first['type']=='ISOLATED_ONLY','isolated meeting')
    P=len(first['words'][0])+extra
    y,w=trace(9*C+2,P);y2,z=trace(C,P);need(y==y2,'common continuation')
    q1=2+w.count('1');q2=z.count('1');s=min(q1,q2);a=abs(q1-q2)
    child=shadow_row(a,-(3**a-1)*y,0)
    d,K=child['d'],child['period'];modulus=3**s
    v=(y-d)*pow(K,-1,modulus)%modulus
    t=(d+K*v-y)//modulus
    while t<=0:v+=modulus;t+=K
    B=C+2**P*t;M=2**P*K
    need(t%K!=0,'isolated point cannot enter resulting cylinder')
    W=w+child['words'][0 if q1>q2 else 1]
    Z=z+child['words'][1 if q1>q2 else 0]
    E=affine_replay(9*M,9*B+2,W)
    need(E==affine_replay(M,B,Z),'neighborhood cylinder')
    return {'kind':'neighborhood','isolated_C':C,'prefix_length':P,'B':B,'M':M,
            'words':[W,Z],'endpoint':list(E)}


def dense_gate_row(C,P):
    """Construct a merger cylinder inside ANY prescribed positive-source prefix cell."""
    x,w=trace(9*C+2,P);y,z=trace(C,P)
    q1,q2=2+w.count('1'),z.count('1');s=min(q1,q2)
    if q1==q2:
        if x==y:
            return {'kind':'dense_gate','C':C,'P':P,'B':C+2**P,'M':2**P,
                    'words':[w,z],'endpoint':list(affine_replay(9*2**P,9*(C+2**P)+2,w))}
        low=min(x,y);K,d,p,q=gap(abs(x-y))
        t=(d-low)*pow(3**s,-1,K)%K
        if t==0:t=K
        W=w+(p if x<y else q);Z=z+(q if x<y else p)
    else:
        a=abs(q1-q2);low=y if q1>q2 else x;high=x if q1>q2 else y
        b=high-3**a*low;k=0
        while shadow(a,b,k) is None:k+=1
        child=shadow_row(a,b,k);K,d=child['period'],child['d'];modulus=3**s
        v=(low-d)*pow(K,-1,modulus)%modulus;t=(d+K*v-low)//modulus
        while t<=0:v+=modulus;t+=K
        W=w+child['words'][0 if q1>q2 else 1];Z=z+child['words'][1 if q1>q2 else 0]
    B=C+2**P*t;M=2**P*K;E=affine_replay(9*M,9*B+2,W)
    need(E==affine_replay(M,B,Z),'arbitrary prefix cylinder')
    return {'kind':'dense_gate','C':C,'P':P,'B':B,'M':M,'words':[W,Z],'endpoint':list(E)}


def main():
    global GAP_MODES
    ap=argparse.ArgumentParser();ap.add_argument('--full',type=Path,required=True);ap.add_argument('--summary',type=Path,required=True)
    ap.add_argument('--limit',type=int,default=65536);args=ap.parse_args()
    need(args.limit>0,'limit')
    parent=load_parent();digest=hashlib.sha256();kinds={};counts={'MERGE':0,'OUTSIDE':0,'BUDGET':0};old_success=set();new_success=set();mod3=0
    selected=[]
    with args.full.open('w',encoding='utf-8') as f:
        def emit(row):
            text=json.dumps(row,sort_keys=True,separators=(',',':'))+'\n';f.write(text);digest.update(text.encode())
            kinds[row['kind']]=kinds.get(row['kind'],0)+1
        for g in range(1,4097):
            for mode in GAP_MODES:emit(gap_row(g,mode))
        for k in (32,64,127,256,512):
            for g in (2**k-1,2**k+1,3*2**k-1,5*2**k+7):emit(gap_row(g,'long'))
        for a in range(1,9):
            for b in (-100,-10,-1,0,2,10,100,10000):
                for seed in (1,3):
                    k0=0
                    while shadow(a,b,k0,seed) is None:k0+=1
                    for k in (k0,k0+1,k0+4):emit(shadow_row(a,b,k,seed))
        for k in range(0,21):
            for seed in (1,3):emit(shadow_row(2,2,k,seed))
        for k in range(21):
            for seed in (1,3):emit(lifted_row(k,seed))
        for C in (1,7,17,71,439,735):emit(first_meeting_row(C))
        for C in (1,7,17,71):
            for extra in (0,4,16,64):emit(neighborhood_row(C,extra))
        for P in range(9):
            for residue in range(2**P):emit(dense_gate_row(residue or 2**P,P))
        for C in (2,17):emit(dense_gate_row(C,256))
        for C in range(1,args.limit+1):
            old=parent.classify(C,True)
            if old['status']=='MERGE':old_success.add(C)
            row=classify(C,parent);counts[row['status']]+=1
            if row['status']=='MERGE':
                new_success.add(C);mod3+=C%3==2
                w,z=row['words'];M=2**len(w)
                need(affine_replay(9*M,9*C+2,w)==affine_replay(M,C,z),'comparison whole cylinder')
                if C not in old_success and len(selected)<12:selected.append({'C':C,'length':len(row['words'][0]),'endpoint':row['endpoint'],'tags':row['tags']})
            emit(row)
    need(old_success<=new_success,'parent successes lost')
    GAP_MODES=('old',)
    old_compiler_only={C for C in range(1,args.limit+1) if classify(C,parent)['status']=='MERGE'}
    GAP_MODES=('long','old','long_alt')
    need(old_compiler_only<=new_success,'old compiler gate lost')
    report={'old_gap_compiler_only_same_selector':len(old_compiler_only),
            'new_gap_gates_increment':len(new_success-old_compiler_only),'status':'PROPOSED','limit':args.limit,'kinds':kinds,'counts':counts,'merge_mod3_2':mod3,
            'parent_mergers':len(old_success),'added':len(new_success-old_success),'first_additions':selected,'rows_sha256':digest.hexdigest(),
            'scope':'bounded procedure evidence, not coverage of every positive source; no independent review'}
    args.summary.write_text(json.dumps(report,sort_keys=True,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,sort_keys=True,indent=2))

if __name__=='__main__':main()
