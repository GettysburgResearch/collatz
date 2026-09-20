#!/usr/bin/env python3
"""Separate whole-word/cylinder reconstruction. Imports no generator or kernel."""
import argparse,copy,hashlib,itertools,json
from collections import Counter
from pathlib import Path

PARENT='7e996feb24cc5d8579d75b39e0b909ffc03b3bcb';SHIFTS=range(-5,12);CAP=18

def enc(x):return json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=True).encode()
def digest(x):return hashlib.sha256(enc(x)).hexdigest()
def need(ok,msg):
    if not ok:raise ValueError(msg)
def positive(n):need(type(n) is int and n>0,'positive exact integer')
def tick(n):return (n+n+n+1)>>1 if n&1 else n>>1

def valuation(n):
    positive(n);c=0
    while n%2==0:n//=2;c+=1
    return c

def walk(n,l):
    positive(n);need(type(l) is int and l>=0,'clock')
    p=[n];bits=''
    for _ in range(l):bits+=str(n%2);n=tick(n);p.append(n)
    return p,bits

def witness(n,m,a,b,kind,meta):
    positive(n);positive(m);need(m<n,'immutable source order')
    p,F=walk(n,a);q,B=walk(m,b);need(p[-1]==q[-1],'endpoints do not meet')
    return {'n':n,'m':m,'F':F,'B':B,'a':a,'b':b,'E':p[-1],
            'min_forward':min(p[1:]) if a else n,'kind':kind,'meta':meta}

def check_witness(c):
    for key in ['n','m','a','b']:need(type(c[key]) is int,'typed witness')
    w=witness(c['n'],c['m'],c['a'],c['b'],c['kind'],c['meta'])
    need(enc(c)==enc(w),'witness reconstruction differs')

def affine(w):
    odd,c,L=0,0,0
    for bit in w:
        need(bit in '01','bit')
        if bit=='1':odd+=1;c=3*c+2**L
        L+=1
    return 3**odd,c,2**L

def compile_gap(delta):
    positive(delta);d=delta;F=B='';P,A,L=1,0,0;r=0;M=1;ds=[]
    while True:
        ds.append(d)
        if d==1:target,h,f,b=4,3,'100','001';newd=0
        elif d%2==0:target,h,f,b=0,1,'0','0';newd=d//2
        elif d%4==1:target,h,f,b=1,2,'01','10';newd=(3*d+1)//4
        else:target,h,f,b=2,2,'10','01';newd=(3*d-1)//4
        N=2**(L+h);r1=((2**L*target-A)*pow(P,-1,N))%N
        need(r1%M==r,'incompatible nested guards');r,M=r1,N
        F+=f;B+=b;P,A,_=affine(B);L+=h
        if newd==0:break
        need(newd<d,'gap rank did not decrease');d=newd
    need(len(F)==len(B) and M==2**len(F),'gap clocks')
    Pf,Af,Df=affine(F);Pb,Ab,Db=affine(B)
    need(Pf==Pb and Pf*delta+Af==Ab,'uniform gap identity')
    for t in [0,1,3]:
        y=r+M*t;p,f=walk(y+delta,L);q,b=walk(y,L)
        need(f==F and b==B and p[-1]==q[-1],'gap physical guard')
    return {'delta':delta,'r':r,'modulus':M,'F':F,'B':B,'gaps':ds}

def prefix(w,tshift=0):
    need('1' in w,'odd step needed');r=0
    for i,bit in enumerate(w):
        z=r
        for _ in range(i):z=tick(z)
        if z%2!=int(bit):r+=2**i
    e=r
    for _ in w:e=tick(e)
    q=w.count('1');P=3**q;g=compile_gap(e+1);M=g['modulus']
    t=((g['r']+1)*pow(P,-1,M))%M
    if not t:t=M
    t+=M*tshift;n=2**len(w)*t+r;m=2**q*t-1
    ans=witness(n,m,len(w)+len(g['F']),q+len(g['B']),'arbitrary_prefix',
                {'w':w,'t':t,'r':r,'e':e,'delta':e+1,'gap_r':g['r'],'gap_modulus':M})
    need(ans['F']==w+g['F'] and ans['B']=='1'*q+g['B'],'prefix lift')
    need(2**(len(w)-q)*m<n,'even-count source compression')
    return ans

def entry(n):
    positive(n);need(n>1,'source at least two')
    if n%2==0:return {'n':n,'m':n//2,'F':'0','B':'','type':'merge','parameter':n//2}
    r=valuation(n+1);m=(n-1)//2;p,F=walk(n,r+2);q,B=walk(m,r+1)
    if p[-1]==q[-1]:typ,C='merge',q[-1]
    else:
        typ,C='H',q[-1];need(p[-1]==9*C+2,'universal H entry')
    return {'n':n,'m':m,'F':F,'B':B,'type':typ,'parameter':C}

def atlas_one(d,cap):
    A=3**max(d,0);B=3**max(-d,0)
    # whole-word numerator data: q counts and affine constants, not point slopes
    nodes=[(1,2,0,0,0,0,'','')];rules=[];points={};front=[]
    for l in range(cap+1):
        nxt=[]
        for r,M,q,c,s,e,F,G in nodes:
            P,Q=3**q,3**s;sx,tx=P*A,c-5*P;sy,ty=Q*B,e-Q
            if sx==sy and tx==ty:rules.append([r,M,F,G]);continue
            if sx!=sy and (ty-tx)%(sx-sy)==0:
                Z=(ty-tx)//(sx-sy)
                if Z>=r and Z%M==r and A*Z-5>0 and B*Z-1>0 and Z not in points:points[Z]=[Z,F,G]
            if l==cap:front.append([r,M,F,G]);continue
            lifts=[r] if l==0 else [r,r+M]
            newM=M if l==0 else 2*M
            for R in lifts:
                need((sx*R+tx)%2**l==0 and (sy*R+ty)%2**l==0,'finite word legality')
                px=((sx*R+tx)//2**l)%2;py=((sy*R+ty)//2**l)%2
                nxt.append((R,newM,q+px,3*c+2**l if px else c,s+py,3*e+2**l if py else e,F+str(px),G+str(py)))
        nodes=nxt
    rules.sort(key=lambda x:(len(x[2]),x[0]));ps=sorted(points.values());front.sort(key=lambda x:x[0])
    den=2**cap;units=sum(den//v[1] for v in rules+front);need(units==den//2,'complete finite partition')
    for r,M,F,G in rules:
        P,c,D=affine(F);Q,e,_=affine(G)
        need(P*A==Q*B and c-5*P==e-Q,'whole-leaf affine equality')
        need((P*(A*r-5)+c)%D==0 and (Q*(B*r-1)+e)%D==0,'whole-leaf congruence')
    for Z,F,G in ps:
        p,f=walk(A*Z-5,len(F));q,g=walk(B*Z-1,len(G));need(f==F and g==G and p[-1]==q[-1],'isolated witness')
    summary={'d':d,'cap':cap,'rules':len(rules),'points':len(ps),'frontier':len(front),
             'rules_sha256':digest(rules),'points_sha256':digest(ps),'frontier_sha256':digest(front),
             'partition_units':units,'partition_denominator':den}
    return {'summary':summary,'rules':rules,'points':ps}

def resonant_u(k,d,s,t):
    j=2*k-d;e=s+d+2;R=3**(j+1);eps=1 if k%2 else 2
    b=((1+eps*3**j)*pow(2**e,-1,R))%R
    b+=R*((pow(3,s+d+1,4)-b)*pow(R,-1,4)%4)
    need(b>0 and (2**e*b-1)%3**j==0,'ternary CRT')
    return (2**e*b-1)//3**j+3*2**(e+2)*t

def resonance_check(k,u,d):
    j=2*k-d
    if j<1:return None
    Z=3**j*u;e=valuation(Z+1);s=e-d-2
    if s<0:return None
    b=(Z+1)//2**e;n=8**k*u-5;m=2**j*u-1
    a=3*k+s+d+4;bb=2*k+s+4
    pn,_=walk(n,a);pm,_=walk(m,bb);x,y=pn[-1],pm[-1]
    meta={'k':k,'u':u,'d':d,'s':s,'odd_quotient':b,'returns':[]}
    if x==y:return witness(n,m,a,bb,'resonance',meta)
    need(y==9*x+2,'resonance complementary H orientation')
    for _ in range(8):
        C=min(x,y);r=valuation(C+2)-1
        if r<3:return None
        q,_=walk(x,r+3);z,_=walk(y,r+3);x,y=q[-1],z[-1];a+=r+3;bb+=r+3
        good=x==y;meta['returns'].append([r,'merge' if good else 'hard'])
        if good:return witness(n,m,a,bb,'resonance_return',meta)
        need(max(x,y)==9*min(x,y)+2,'reusable pair lost')
    return None

def selector(k,u,ix):
    n=8**k*u-5;opts=[]
    for d in (1,3):
        row=resonance_check(k,u,d)
        if row:opts.append(row)
    tried=0
    for j in range(1,3*k):
        m=2**j*u-1;d=2*k-j
        if m<=0 or m>=n or d not in ix:continue
        tried+=1;Z=3**min(j,2*k)*u;lut,pts=ix[d];matches=[]
        for M,items in lut.items():
            if Z%M in items:matches.append((*items[Z%M],False,M))
        if Z in pts:matches.append((*pts[Z],True,0))
        if matches:
            f,g,point,M=min(matches,key=lambda v:(len(v[0]),v[2]))
            c=witness(n,m,3*k+len(f),j+len(g),'atlas_point' if point else 'atlas_cylinder',
                      {'k':k,'u':u,'d':d,'j':j,'Z':Z,'modulus':M})
            need(c['F']=='110'*k+f and c['B']=='1'*j+g,'atlas source lift')
            opts.append(c)
    if not opts:return {'n':n,'status':'NO_CERTIFICATE','k':k,'u':u,'shadows_tested':tried}
    c=min(opts,key=lambda x:(x['m'],x['a']+x['b'],x['F'],x['B']));c['status']='MERGE';return c

def reconstruct():
    atlas={d:atlas_one(d,CAP) for d in SHIFTS};ix={}
    for d,obj in atlas.items():
        look={}
        for r,M,F,G in obj['rules']:look.setdefault(M,{})[r]=(F,G)
        ix[d]=(look,{Z:(F,G) for Z,F,G in obj['points']})
    deltas=list(range(1,257))+[2**e-1 for e in [16,32,64,128,256]]+[2**e+1 for e in [16,32,64,128,256]]+[3**100+7]
    gaps=[compile_gap(d) for d in deltas];prefixes=[]
    for L in range(1,9):
        for w in itertools.product('01',repeat=L):
            w=''.join(w)
            if '1' in w:prefixes.append(prefix(w))
    for w in ['110'*50,'11110111000'*12,'1101001101011110001001'*4]:prefixes.append(prefix(w,2))
    families=[]
    for d in (1,3):
        minimum=(d+2)//2
        for k in sorted(set([minimum,minimum+1,6,24,36,80,200])):
            for s in [0,1,2,3,4,8,16,32,64,128]:
                for t in [0,1,3]:
                    u=resonant_u(k,d,s,t);row=resonance_check(k,u,d);need(row and row['kind']=='resonance','all-parameter family')
                    need(row['n']%12==3,'old residual specialization')
                    if 2**(k+d)>5:need(2**(k+d)*row['m']<row['n'],'strong factor')
                    strong=9**k>=2**(d+3)*8**k
                    if strong:need(row['min_forward']>row['n'],'all-state minimum')
                    row['strong_bound']=strong;families.append(row)
    escapes=[]
    for k in [1,2,6,24,36,80,200]:
        for s in [2,3,4,8,16,32,64,128]:
            for t in [0,1]:
                j=2*k-1;e=s+3;R=3**(j+1);eps=1 if k%2 else 2
                b=((1+eps*3**j)*pow(2**e,-1,R))%R
                b+=R*((5*pow(3**s,-1,8)-b)*pow(R,-1,8)%8)
                u=(2**e*b-1)//3**j+3*2**(s+6)*t
                row=resonance_check(k,u,1);v=9**(k-1)*u
                old_q=(9*v-13)//8
                need(v%16==5 and old_q%4==2,'old adjacent entry')
                root=old_q//2;old_s=valuation(root+1)
                old_end=tick(root)
                for _ in range(old_s-1):old_end=tick(old_end)
                need(old_end%4==0,'old hard adjacent exit')
                C=old_end//4;need(C%2==1 and row is not None,'old return cannot apply')
                row['old_H_parameter']=C;escapes.append(row)
    grid=[selector(k,u,ix) for k in range(1,7) for u in range(1,8192,2)]
    entries=[entry(n) for n in range(2,8193)]
    chart_count=0
    for d in range(6):
        for b in range(-50,51):
            for y in range(1,35):
                x=3**d*y+b
                if x<1:continue
                # Test each printed chart formula against direct map, without kernel.
                if b%2==0:
                    D=d;B=b//2 if y%2==0 else (3*b+1-3**d)//2;Y=tick(y);flip=False
                elif y%2==0:D=d+1;B=(3*b+1)//2;Y=y//2;flip=False
                elif d:D=d-1;B=(b-3**(d-1))//2;Y=tick(y);flip=False
                else:D=1;B=(1-3*b)//2;Y=x//2;flip=True
                pair=(3**D*Y+B,Y)
                if flip:pair=pair[::-1]
                need(pair==(tick(x),tick(y)),'complete chart formula');chart_count+=1
    controls={'wrong_gap_guard':{'delta':1,'y':1,'F':'100','B':'001'},
              'phase_pair':[2,1],'source_order_bad':{'n':3,'m':3},
              'entry_7':entry(7),'finite_library':{'shifts':list(SHIFTS),'tail_steps':CAP}}
    examples=[resonance_check(1,37,1),resonance_check(36,5,3)]
    p={'parent':PARENT,'config':{'shifts':list(SHIFTS),'tail_steps':CAP,'hard_return_stages':8,'grid_k':[1,6],'grid_odd_u_max':8191},
       'atlas':[atlas[d]['summary'] for d in SHIFTS],
       'gap_count':len(gaps),'gap_sha256':digest(gaps),'prefix_count':len(prefixes),'prefix_sha256':digest(prefixes),
       'family_count':len(families),'families_sha256':digest(families),
       'escape_count':len(escapes),'escape_sha256':digest(escapes),'strong_family_count':sum(v['strong_bound'] for v in families),
       'grid_counts':dict(Counter(v['status'] for v in grid)),'grid_sha256':digest(grid),
       'entry_counts':dict(Counter(v['type'] for v in entries)),'entry_sha256':digest(entries),
       'chart_checks':chart_count,'controls':controls,'examples':examples}
    return {'schema':'collatz-aua-005-v1','payload':p,'sha256':digest(p)}

def validate(env,expected):
    need(type(env) is dict and set(env)=={'schema','payload','sha256'},'envelope schema')
    need(type(env['sha256']) is str and env['sha256']==digest(env['payload']),'seal')
    need(enc(env)==enc(expected),'independent typed reconstruction differs')

def hostile(expected):
    cases=[]
    for key in ['gap_count','prefix_count','family_count','strong_family_count','chart_checks']:
        for replacement in [True,1.0,-1]:
            e=copy.deepcopy(expected);e['payload'][key]=replacement;cases.append(e)
    for field in ['rules','points','frontier','partition_units']:
        e=copy.deepcopy(expected);e['payload']['atlas'][0][field]+=1;cases.append(e)
    for field in ['a','b','E','m','n']:
        e=copy.deepcopy(expected);e['payload']['examples'][0][field]+=1;cases.append(e)
    rejected=0
    for e in cases:
        e['sha256']=digest(e['payload'])
        try:validate(e,expected)
        except ValueError:rejected+=1
        else:raise ValueError('resealed mutation accepted')
    direct=[];c=copy.deepcopy(expected['payload']['examples'][0])
    for field,value in [('m',c['n']),('n',True),('a',c['a']+1),('F','0'+c['F']),('E',c['E']+1)]:
        z=copy.deepcopy(c);z[field]=value;direct.append(z)
    for z in direct:
        try:check_witness(z)
        except ValueError:pass
        else:raise ValueError('bad witness accepted')
    for bad in [0,-1,True,1.0]:
        try:compile_gap(bad)
        except ValueError:pass
        else:raise ValueError('bad gap accepted')
    # A pair can remain permanently out of phase; do not call entry a merger.
    x,y=2,1
    for _ in range(20):need(x!=y,'phase control');x,y=tick(x),tick(y)
    need(entry(7)['type']=='H','entry was promoted to success')
    return {'resealed_rejected':rejected,'direct_witnesses_rejected':len(direct),'bad_gap_inputs_rejected':4}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('artifact',type=Path);p.add_argument('--self-test',action='store_true');a=p.parse_args()
    expected=reconstruct();submitted=json.loads(a.artifact.read_text());validate(submitted,expected)
    extra=hostile(expected) if a.self_test else {}
    print(json.dumps({'status':'PASS','sha256':expected['sha256'],**extra},sort_keys=True))
if __name__=='__main__':main()
