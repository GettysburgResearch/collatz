"""Signed seam classification, residue-compatible rank lattices and AP propagation."""
from collections import Counter
from itertools import product
from math import gcd
import json

from clock_order_certificate import make_cycle, necklaces


def canonical(word,ns):
    P=len(word);A=sum(word);tot=0;dis=[]
    for i,e in enumerate(word):dis.append(P*tot-i*A);tot+=e
    j=dis.index(max(dis));w=word[j:]+word[:j];ns=ns[j:]+ns[:j]
    z=[];tot=0
    for i,e in enumerate(w):z.append(i*A//P-tot);tot+=e
    return w,ns,z


def analyze(word,d,numerators,c,out):
    P=len(word);A=sum(word);g=gcd(A,P);q=P//g;a=A//g
    if not P<A<2*P or q<2:return
    w,N,z=canonical(word,numerators);H=max(z)
    if H>2:return
    s=a-q
    ell=[1<<(H-x) for x in z];K=[l*n for l,n in zip(ell,N)]
    f=[i*s%q for i in range(P)];m=[1+int(r+s>=q) for r in f]
    def rho(h):return pow(3,h,d)*pow(2,-(h*A//P),d)%d
    omega=rho(q);unit=1%d;U={pow(omega,j,d) for j in range(g)}
    assert len(U)==g
    l=pow(s,-1,q);beta=rho(l);v=unit;T=None
    assert (pow(beta,q,d)*pow(omega,-l,d))%d==2%d
    assert (pow(beta,a,d)*pow(omega,-(l*a//q),d))%d==3%d
    for h in range(1,P):
        t=h*s%q;rh=rho(h)
        if not t:continue
        gaps=[];curv=[];dr=[]
        for i in range(P):
            rr=f[i];idx=[(i+j*h)%P for j in range(3)]
            B=[K[k]<<((rr+j*t)//q) for j,k in enumerate(idx)]
            low=[ell[k]<<((rr+j*t)//q) for j,k in enumerate(idx)]
            assert (B[1]-rh*B[0])%d==0
            gaps.append(B[1]-B[0]);curv.append(B[2]-2*B[1]+B[0]);dr.append(low[2]-2*low[1]+low[0])
        assert sum(curv)==sum(gaps[(i+h)%P] for i in range(P) if f[i]+t>=q)
        for i in range(P):
            assert (curv[(i+1)%P]<<m[i])==3*curv[i]+d*dr[i]
            c['genuine_arbitrary_offset_interfaces']+=1
            c['genuine_wrapped_interfaces']+=int(f[i]+2*t>=q)
    for t in range(1,q):
        v=v*beta%d
        if v in U:T=t;break
    offsets={}
    for h in range(1,P):
        t=h*s%q
        if rho(h)!=unit:continue
        if t==0:raise AssertionError('nontrivial compatible resonance')
        assert t not in offsets
        offsets[t]=h
        for i in range(P):
            k=(i+h)%P;cc=int(f[i]+t>=q);G=(K[k]<<cc)-K[i]
            assert G>0 and G%d==0
            c['compatible_positive_comparisons']+=1
    assert sorted(offsets)==([] if T is None else list(range(T,q,T)))
    c['height_at_most_two_cycles']+=1
    if T is None:return
    h=offsets[T];assert all(offsets[t]==h*(t//T)%P for t in offsets)
    c['nonempty_lattices']+=1
    if g>1:c['nonempty_multicovers']+=1
    key=('multicover' if g>1 else 'singlecover')
    if key not in out or (q//T)>out[key]['ranks_per_lane']:
        out[key]=dict(period=P,word=list(word),denominator=d,gcd=g,rank_step=T,ranks_per_lane=q//T,compatible_lag=h,canonical_height=H)
    if H>1 or 2*T>=q:return
    # Normalize to H=1 even for the H=0 subcase.
    K=[(2>>x)*n for x,n in zip(z,N)];ell=[2>>x for x in z]
    gaps=[];curv=[];dr=[]
    for i in range(P):
        labs=[K[(i+j*h)%P]<<((f[i]+j*T)//q) for j in range(3)]
        low=[ell[(i+j*h)%P]<<((f[i]+j*T)//q) for j in range(3)]
        gaps.append(labs[1]-labs[0]);curv.append(labs[2]-2*labs[1]+labs[0]);dr.append(low[2]-2*low[1]+low[0])
    assert sum(gaps)==sum(K[(i+h)%P] for i in range(P) if f[i]+T>=q)
    assert sum(curv)==sum(gaps[(i+h)%P] for i in range(P) if f[i]+T>=q)
    for i in range(P):
        assert curv[i]%d==0 and (curv[(i+1)%P]<<m[i])==3*curv[i]+d*dr[i]
        c['exact_multilabel_curvatures']+=1
        if f[i]+2*T>=q:c['actual_wrapped_curvatures']+=1
    if min(curv)>=d:
        for t,k in offsets.items():
            sums=[(K[(i+k)%P]<<int(f[i]+t>=q))-K[i] for i in range(P)]
            assert max(Counter(sums).values())<=g*T
            for i in range(P):
                delta=(sums[(i+h)%P]<<int(f[i]+T>=q))-sums[i]
                assert delta>=t//T*d
                c['conditional_convex_fibre_interfaces']+=1


def run():
    c=Counter();ex={}
    opts=set(product((1,2),repeat=3))
    ss=[{a-2*b+e for a,b,e in opts},{a-2*b+2*e for a,b,e in opts},{a-4*b+2*e for a,b,e in opts}]
    assert [(min(x),max(x)) for x in ss]==[(-2,2),(-1,4),(-5,2)]
    for j,types in enumerate(ss):
        for k,t,m in product(range(-12,13),types,(1,2) if j==0 else (2,)):
            v=3*k+t
            if v%(1<<m):continue
            kk=v//(1<<m);assert k*kk>=0
            if k<0 and kk==0:assert (j,k,t)==(1,-1,3)
            if k>0 and kk==0:assert (j,k,t)==(2,1,-3)
            c['abstract_seam_interfaces']+=1
    for d,a,g in product((1,5,7,11,17,41,101,997),range(1,160),range(1,90)):
        B=[a,a+d*g,a+2*d*g];L=[v&-v for v in B]
        if max(L)>2:continue
        if g%2:assert L==[1,2,1]
        else:assert len(set(L))==1
        for m in (1,2):
            F=[3*v+d*l for v,l in zip(B,L)]
            if any(v%(1<<m) for v in F):continue
            T=[v>>m for v in F];diff=T[2]-2*T[1]+T[0]
            if g%2:assert diff<0 and diff*(1<<m)==-2*d
            else:assert diff==0 and (T[1]-T[0])*(1<<m)==3*d*g
            c['exact_drift_AP_interfaces']+=1
    data=set()
    for alph,n in [(2,17),(3,10)]:
        for P in range(2,n+1):
            for w in necklaces(P,alph):
                if alph==3 and max(w)<3:continue
                C=make_cycle(w)
                if C is not None:
                    d,N=C;analyze(w,d,N,c,ex);data.add((d,min(N)))
    # A second source of cycles, generated directly by 3n+d from small odd seeds.
    for d in range(1,150,2):
        if d%3==0:continue
        done=set()
        for seed in range(1,1600,2):
            if seed in done or gcd(seed,d)>1:continue
            run=[];at={};x=seed
            while x not in done and x not in at and len(run)<500 and x.bit_length()<100:
                at[x]=len(run);raw=3*x+d;e=(raw&-raw).bit_length()-1;run.append((x,e));x=raw>>e
            done.update(at)
            if x not in at:continue
            cyc=run[at[x]:];N=[x for x,e in cyc];w=tuple(e for x,e in cyc)
            if (d,min(N)) in data:continue
            data.add((d,min(N)));analyze(w,d,N,c,ex)
    for d in range(1,300,2):
        if d%3==0:continue
        unit=1%d;S={unit};work=[unit]
        for v in work:
            for k in (2,3):
                a=v*k%d
                if a not in S:S.add(a);work.append(a)
        for q in (5,7,11,13,17,19):
            a=q+q//2+1
            om=pow(3,q,d)*pow(2,-a,d)%d;l=pow(a,-1,q)
            beta=pow(3,l,d)*pow(2,-(l*a//q),d)%d
            U={unit};v=om
            while v not in U:U.add(v);v=v*om%d
            T=1;v=beta
            while v not in U:T+=1;v=v*beta%d
            assert len(S)==T*len(U)
            for t in range(1,q):
                choices=[]
                for j in range(len(U)):
                    h=l*t+j*q
                    if (pow(3,h,d)*pow(2,-(h*a//q),d))%d==unit:choices.append(h%(q*len(U)))
                assert len(choices)==int(t%T==0)
                c['finite_group_offset_faces']+=1
                c['genuine_compatible_modular_offsets']+=bool(choices)
    return {'counts':dict(c),'examples':ex,'seam_drift_sets':[sorted(x) for x in ss]}
if __name__=='__main__':print(json.dumps(run(),indent=2,sort_keys=True))
