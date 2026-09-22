"""Exact physical return library. Status: PROPOSED; no universal coverage.
Prior VL/AR formulas are credited in SOURCES_AND_LIMITS.md.
"""
from fractions import Fraction

def require(ok, message):
    if not ok:
        raise ValueError(message)

def positive(n):
    require(type(n) is int and n > 0, 'expected a positive non-boolean integer')
    return n


def v2(n):
    positive(n)
    return (n & -n).bit_length()-1

def T(n):
    positive(n)
    return (3*n+1)//2 if n%2 else n//2

def walk(n,L):
    positive(n); require(type(L) is int and L>=0, 'nonnegative clock required')
    w=''; states=[n]
    for _ in range(L):
        w+=str(n%2); n=T(n); states.append(n)
    return n,w,states

def finish(D):
    positive(D)
    s=v2(D+1); z=3**s*((D+1)>>s)
    return ('MERGE',(3*z-1)//4,s+2) if z%4==3 else ('RETURN',(z-1)//4,s+2)

def prior(C):
    if C%2==0:
        v=v2(3*C-2)
        if v<3 or v%2==0:return None
        k=(v-3)//2;D=(3**(k+1)*((3*C-2)>>v)+1)//2;pre=2*k+4
    else:
        v=v2(3*C-1)
        if v<4 or v%2:return None
        k=(v-4)//2;D=(3**(k+2)*((3*C-1)>>v)+1)//2;pre=2*k+5
    s,o,l=finish(D);return s,o,pre+l,'VL'

def qtail(E):
    if E<=1 or E%2==0 or v2(E-1)%2==0:return None
    j=(v2(E-1)-1)//2
    F=(3**(j+1)*((E-1)>>(2*j+1))+1)//2
    s,o,l=finish(F);return s,o,2*j+2+l

def adjacent(q):
    l=0
    if q%2:
        if q<=1 or v2(q-1)%2:return None
        s=v2(q-1)//2;q=3**s*((q-1)>>(2*s))+1;l=2*s
    a=v2(q)
    if a==2:return 'MERGE',(3*(q//4)+1)//2,l+3
    if a>=3:return 'RETURN',q//8,l+3
    s,o,e=finish((3*q+2)//4);return s,o,l+2+e

def a_bridge(C):
    if C%8!=7:return None
    v=(C+1)//8;a=v2(9*v-1)
    if a%2==0:return None
    k=(a-1)//2;E=(3**(k+1)*((9*v-1)>>a)+1)//2
    ans=qtail(E)
    if ans is None:return None
    s,o,l=ans;return s,o,2*k+5+l,'AR-A'

def b_bridge(C):
    if C%32!=31:return None
    Y=243*((C+1)//32)
    if Y%4!=1:return None
    ans=adjacent((Y-5)//4)
    if ans is None:return None
    s,o,l=ans;return s,o,7+l,'AR-B'

def r_step(D):
    positive(D); require(D>=2, 'R requires D>=2')
    if D==2:return None
    if D%4==2:return (3*D+2)//4,'01','01','A'
    if D%16==13:return (9*D+11)//16,'1100','1001','B'
    if D%32==23:return (27*D+19)//32,'10101','11100','C'
    if D%32768==191:return (19683*D+41635)//32768,'101101010111100','111111010001001','D'
    return None

def r_normalize(D):
    """Return actual words and a terminal parameter; an outside guard is not success."""
    positive(D); require(D>=2, 'R requires D>=2')
    W='';Z='';labels=[]
    while True:
        ans=r_step(D)
        if ans is None:break
        old=D;D,w,z,lab=ans
        require(2<=D<old and 7*(D-2)<=6*(old-2), 'common rank violation')
        W+=w;Z+=z;labels.append(lab)
    return D,W,Z,labels

def r_exit(D):
    if D==2:return 'MERGE',2,0
    if D%4==0:
        ans=qtail(D//4)
        if ans is None:return None
        s,o,l=ans;return s,o,l+2
    if D%4==3:
        Y=9*(D+1)//4
        if Y%4!=1:return None
        ans=adjacent((Y-5)//4)
        if ans is None:return None
        s,o,l=ans;return s,o,l+4
    return None

def new_bridge(C):
    if C%8!=7:return None
    D=27*((C+1)//8)-1
    D,W,Z,labs=r_normalize(D)
    ans=r_exit(D)
    if ans is None:return None
    s,o,l=ans;return s,o,3+len(W)+l,'R-'+''.join(labs)

def tr(C,extended=False):
    positive(C); require(type(extended) is bool, 'mode must be boolean')
    for fun in (prior,a_bridge,b_bridge,new_bridge) if extended else (prior,a_bridge,b_bridge):
        ans=fun(C)
        if ans is not None:return ans
    return None

def classify(C,extended=False,budget=1000):
    """Retain the last accepted H checkpoint; a failed trial adds no clock."""
    positive(C); require(type(extended) is bool, 'mode must be boolean')
    require(type(budget) is int and budget>=0, 'nonnegative stage budget required')
    L=0;tags=[]
    for _ in range(budget):
        ans=tr(C,extended)
        if ans is None:return 'OUTSIDE',C,L,tags
        s,o,l,tag=ans;L+=l;tags.append(tag)
        if s=='MERGE':return s,o,L,tags
        C=o
    return 'BUDGET',C,L,tags

def compile_returns(word):
    require(type(word) is str and word and set(word)<=set('ABCD'), 'nonempty ABCD word required')
    r,M=12,64
    specs={'A':(2,3,2),'B':(4,9,11),'C':(5,27,19),'D':(15,19683,41635)}
    for tag in reversed(word):
        ell,P,A=specs[tag]
        # F(D)=(P*D+A)/2**ell, exact selected residue of input too
        rr=((2**ell*r-A)*pow(P,-1,2**ell*M))%(2**ell*M)
        r,M=rr,2**ell*M
    return r,M

def h_class(word):
    r,M=compile_returns(word)
    # D=27v-1, C=8v-1
    v=((r+1)*pow(27,-1,M))%M
    return 8*v-1,8*M



SPECS = {
    'A': (2, 3, 2, 2, 4, '01', '01'),
    'B': (4, 9, 11, 13, 16, '1100', '1001'),
    'C': (5, 27, 19, 23, 32, '10101', '11100'),
    'D': (15, 19683, 41635, 191, 32768, '101101010111100', '111111010001001'),
}

def outcome(C, extended):
    status,out,L,tags=classify(C,extended)
    ans={'status':status,'out':out,'clock':L,'tags':tags}
    if status=='MERGE':
        a,w,_=walk(9*C+2,L);b,z,_=walk(C,L)
        require(a==b==out,'physical merger')
        ans['words']=[w,z]
    return ans

def gate(word):
    D,M=compile_returns(word);C,Hmod=h_class(word)
    W='101'+''.join(SPECS[c][5] for c in word)+'000001'
    Z='111'+''.join(SPECS[c][6] for c in word)+'001100'
    E,w,_=walk(9*C+2,len(W));e,z,_=walk(C,len(Z))
    require(e==E and (w,z)==(W,Z),'gate merger and actual words')
    return {'sequence':word,'r_base':D,'r_modulus':M,'C':C,'modulus':Hmod,
            'words':[W,Z],'endpoint':[3**Z.count('1'),E]}

def lift(word, r_extra=0, translate=0):
    require(type(r_extra) is int and r_extra>=0, 'nonnegative r_extra required')
    require(type(translate) is int and translate>=0, 'nonnegative translate required')
    g=gate(word);C0,M=g['C'],g['modulus'];W,Z=g['words'];L=len(W)
    gamma=min(Fraction(9*3**W[:j].count('1'),2**j) for j in range(L+1))
    r=2
    while gamma*3**(r-1)<=8*2**r:r+=1
    r+=r_extra
    mod=4*M
    u=((4*C0+1)*pow(3**(r-1),-1,mod))%mod
    u+=mod*((pow(2**r,-1,3)-u)*pow(mod,-1,3)%3)
    u+=3*mod*translate
    n=2**r*u-1;m=(n-3)//4;C=(3**(r-1)*u-1)//4
    fw='1'*r+'01'+W;bw='1'*(r-2)+'01'+Z
    E,w,states=walk(n,len(fw));e,z,_=walk(m,len(bw))
    require((w,z)==(fw,bw) and e==E,'lift words')
    require(min(states[1:])>n and n%3==0 and 0<4*m<n,'lift order and all-state bound')
    return {'sequence':word,'r_extra':r_extra,'translate':translate,'r':r,'u':u,
            'u_modulus':3*mod,'n':n,'m':m,'C':C,'clocks':[len(fw),len(bw)],
            'words':[fw,bw],'endpoint':E,'minimum':min(states[1:]),
            'gamma':[gamma.numerator,gamma.denominator],'baseline':outcome(C,False)}
