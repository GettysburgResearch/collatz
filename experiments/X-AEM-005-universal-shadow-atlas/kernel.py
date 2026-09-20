"""Exact research kernel. Every finite search limit is an explicit limitation."""
import hashlib,json
from collections import Counter

def encode(x): return json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=True).encode()
def sha(x):return hashlib.sha256(encode(x)).hexdigest()
def integer(x,lo=0):
    if type(x) is not int or x<lo:raise ValueError('exact integer outside domain')
    return x

def T(x):return (3*x+1)//2 if x%2 else x//2

def v2(x):
    integer(x,1);return (x&-x).bit_length()-1

def trace(x,w):
    integer(x,1)
    if type(w) is not str:raise ValueError('word must be text')
    out=[x]
    for b in w:
        if b not in '01' or x%2!=int(b):raise ValueError('illegal positive path')
        x=T(x);out.append(x)
    return out

def cert(n,m,F,B,kind,meta=None):
    integer(n,2);integer(m,1)
    if m>=n:raise ValueError('original-source order failed')
    a,b=trace(n,F),trace(m,B)
    if a[-1]!=b[-1]:raise ValueError('not a meeting')
    return {'n':n,'m':m,'F':F,'B':B,'a':len(F),'b':len(B),'E':a[-1],
            'min_forward':min(a[1:]) if F else n,'kind':kind,'meta':meta or {}}

def gap(delta):
    """Compile one guaranteed uniform same-clock merger for EVERY fixed gap."""
    integer(delta,1);ds=[];d=delta
    while d>1:
        if d%2==0: ds.append((0,d));d//=2
        elif d%4==1:ds.append((1,d));d=(3*d+1)//4
        else:ds.append((3,d));d=(3*d-1)//4
    r,M,F,B=4,8,'100','001' # F from y+delta, B from y
    for typ,_ in reversed(ds):
        if typ==0:r,M,F,B=2*r,2*M,'0'+F,'0'+B
        elif typ==1:r,M,F,B=((4*r-1)*pow(3,-1,4*M))%(4*M),4*M,'01'+F,'10'+B
        else:r,M,F,B=((4*r-2)*pow(3,-1,4*M))%(4*M),4*M,'10'+F,'01'+B
    return {'delta':delta,'r':r,'modulus':M,'F':F,'B':B,'gaps':[x[1] for x in ds]+[1]}

def word_data(w):
    P,A,D=1,0,1
    for bit in w:
        if bit=='1':P,A=3*P,3*A+D
        elif bit!='0':raise ValueError('invalid parity word')
        D*=2
    return P,A,D

def prefix_family(w,translate=0):
    integer(translate)
    P,A,D=word_data(w);q=w.count('1')
    if not w or q==0:raise ValueError('nonempty word with an odd step required')
    r=(-A*pow(P,-1,D))%D;e=(P*r+A)//D
    g=gap(e+1);M=g['modulus'];t=((g['r']+1)*pow(P,-1,M))%M
    if t==0:t=M
    t+=M*translate
    n=D*t+r;m=2**q*t-1
    row=cert(n,m,w+g['F'],'1'*q+g['B'],'arbitrary_prefix',{'w':w,'t':t,'r':r,'e':e,'delta':e+1,'gap_r':g['r'],'gap_modulus':M})
    if 2**(len(w)-q)*m>=n:raise ValueError('compression inequality')
    return row

def universal_entry(n):
    integer(n,2)
    if n%2==0:return {'n':n,'m':n//2,'F':'0','B':'','type':'merge','parameter':n//2}
    r=v2(n+1);u=(n+1)//2**r;m=(n-1)//2;z=3**(r-1)*u-1
    if z%4==2:
        F='1'*r+'00';B='1'*(r-1)+'01';typ='merge';parameter=(3*z+2)//4
    elif z%4==0 and z>0:
        F='1'*r+'01';B='1'*(r-1)+'00';typ='H';parameter=z//4
    else:raise ValueError('entry partition failed')
    a,b=trace(n,F),trace(m,B)
    expected=(parameter,parameter) if typ=='merge' else (9*parameter+2,parameter)
    if (a[-1],b[-1])!=expected:raise ValueError('entry endpoints')
    return {'n':n,'m':m,'F':F,'B':B,'type':typ,'parameter':parameter}

def chart_step(d,b,y):
    integer(d);integer(y,1);integer(3**d*y+b,1)
    if b%2==0:
        if y%2==0:return d,b//2,y//2,False
        return d,(3*b+1-3**d)//2,(3*y+1)//2,False
    if y%2==0:return d+1,(3*b+1)//2,y//2,False
    if d:return d-1,(b-3**(d-1))//2,(3*y+1)//2,False
    return 1,(1-3*b)//2,(y+b)//2,True

def compile_atlas(d,cap=18):
    """Complete cylinders AND isolated positive meetings through cap, for odd Z.
    Formal affine intercepts may be negative; witnesses require positive sources.
    """
    if type(d) is not int:raise ValueError('integer shift')
    integer(cap,1)
    A=3**max(d,0);B=3**max(-d,0)
    # residue, modulus, X slope/intercept, Y slope/intercept, physical words
    nodes=[(1,2,2*A,A-5,2*B,B-1,'','')]
    rules=[];points={};front=[]
    for depth in range(cap+1):
        new=[]
        for r,M,ax,bx,ay,by,F,G in nodes:
            if ax==ay and bx==by:
                rules.append([r,M,F,G]);continue
            if ax!=ay and (by-bx)%(ax-ay)==0:
                t=(by-bx)//(ax-ay);Z=r+M*t
                if t>=0 and A*Z-5>0 and B*Z-1>0 and Z not in points:
                    points[Z]=[Z,F,G]
            if depth==cap:
                front.append([r,M,F,G]);continue
            lifts=(0,1) if ax%2 or ay%2 else (None,)
            for bit in lifts:
                if bit is None:rr,MM,Ax,Bx,Ay,By=r,M,ax,bx,ay,by
                else:rr,MM,Ax,Bx,Ay,By=r+bit*M,2*M,2*ax,bx+bit*ax,2*ay,by+bit*ay
                px=Bx%2;py=By%2
                new.append((rr,MM,(3*Ax if px else Ax)//2,(3*Bx+1 if px else Bx)//2,
                            (3*Ay if py else Ay)//2,(3*By+1 if py else By)//2,F+str(px),G+str(py)))
        nodes=new
    rules.sort(key=lambda v:(len(v[2]),v[0]));ps=sorted(points.values());front.sort(key=lambda v:v[0])
    # Prefix-free uniform leaves + depth-cap frontier cover every odd Z.
    denominator=2**max(cap,1)
    units=sum(denominator//r[1] for r in rules)+sum(denominator//r[1] for r in front)
    if units!=denominator//2:raise ValueError('incomplete dyadic partition')
    summary={'d':d,'cap':cap,'rules':len(rules),'points':len(ps),'frontier':len(front),
             'rules_sha256':sha(rules),'points_sha256':sha(ps),'frontier_sha256':sha(front),
             'partition_units':units,'partition_denominator':denominator}
    return {'summary':summary,'rules':rules,'points':ps}

def indices(atlas):
    ret={}
    for d,obj in atlas.items():
        rules={}
        for r,M,F,B in obj['rules']:rules.setdefault(M,{})[r]=(F,B)
        ret[d]=(rules,{Z:(F,B) for Z,F,B in obj['points']})
    return ret

def resonance(k,u,d,budget=8):
    integer(k,1);integer(u,1)
    if d not in (1,3) or u%2==0 or 2*k-d<1:return None
    j=2*k-d;Z=3**j*u;e=v2(Z+1);s=e-d-2
    if s<0:return None
    b=(Z+1)//2**e;good=pow(3,s+d+1,4)*b%4==1
    n=8**k*u-5;m=2**j*u-1
    F='110'*k+'0'*(d+2)+'1'*s+('01' if good else '00')
    B='1'*j+'0'+'1'*(s+d+1)+('00' if good else '01')
    meta={'k':k,'u':u,'d':d,'s':s,'odd_quotient':b,'returns':[]}
    if good:return cert(n,m,F,B,'resonance',meta)
    C=(3**(s+d)*b-1)//4;flip=True
    for _ in range(budget):
        r=v2(C+2)-1
        if r<3:return None
        w=(C+2)//2**(r+1);good=pow(3,r,4)*w%4==1
        f='0000'+'1'*(r-3)+('01' if good else '00');g='0'+'1'*r+('00' if good else '01')
        F+=g if flip else f;B+=f if flip else g
        meta['returns'].append([r,'merge' if good else 'hard'])
        if good:return cert(n,m,F,B,'resonance_return',meta)
        C=(3**(r-1)*w-1)//4;flip=not flip
    return None

def resonance_source(k,d,s,t=0):
    j=2*k-d
    if j<1 or s<0 or d not in (1,3):raise ValueError('resonance parameters')
    e=s+d+2;M=2**(e+2);b0=pow(3,s+d+1,4)
    u=((2**e*b0-1)*pow(3**j,-1,M))%M
    eps=1 if k%2 else 2
    u+=M*((eps-u)*pow(M,-1,3)%3)
    return u+3*M*t

def choose(k,u,idx,cap=18):
    integer(k,1);integer(u,1)
    if u%2==0:raise ValueError('odd u')
    n=8**k*u-5;options=[]
    for d in (1,3):
        x=resonance(k,u,d)
        if x:options.append(x)
    tried=0
    for j in range(1,3*k):
        m=2**j*u-1
        if not 0<m<n:continue
        d=2*k-j
        if d not in idx:continue
        tried+=1;Z=3**min(2*k,j)*u;rules,points=idx[d]
        matches=[]
        for M,lut in rules.items():
            if Z%M in lut:matches.append((*lut[Z%M],False,M))
        if Z in points:matches.append((*points[Z],True,0))
        if matches:
            f,b,isolated,M=min(matches,key=lambda p:(len(p[0]),p[2]))
            options.append(cert(n,m,'110'*k+f,'1'*j+b,'atlas_point' if isolated else 'atlas_cylinder',
                                {'k':k,'u':u,'d':d,'j':j,'Z':Z,'modulus':M}))
    if not options:return {'n':n,'status':'NO_CERTIFICATE','k':k,'u':u,'shadows_tested':tried}
    c=min(options,key=lambda x:(x['m'],x['a']+x['b'],x['F'],x['B']));c['status']='MERGE';return c
