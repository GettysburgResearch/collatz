#!/usr/bin/env python3
"""Second finite reconstruction: physical inverse walks and parity residues.

Does not import the generator or any repository module. This is same-author
implementation independence, not independent mathematical acceptance.
"""
from __future__ import annotations
import argparse
import copy
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

BASE="69b1ed57ce90fe8c9d6d7c80c69760a86eb0fd2a"
SCOPE={"all_parameter_claims":"PROPOSED_PENDING_INDEPENDENT_REVIEW",
       "collatz_proved":False,"complete_selector":False,
       "rank":"P(n)=(2n+1)^2/3^v3(2n+1)",
       "clock":"first positive-time returns to n=1 mod3; absorb at1",
       "box":"0<=r,s<=D; witness x in the positive section",
       "finite_tests_only":True}


def check(ok: bool, why: str) -> None:
    if not ok: raise ValueError(why)


def seal(obj: object) -> str:
    return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def ihex(n: int) -> str:
    return hashlib.sha256(hex(n).encode('ascii')).hexdigest()


def ordp(n: int,p: int=3) -> int:
    check(n!=0,'zero valuation')
    if p==2:
        # Count zero binary suffix without using the generator's low-bit formula.
        return len(bin(abs(n)))-len(bin(abs(n)).rstrip('0'))
    power,count=3,0
    while n%power==0:
        power*=3;count+=1
    return count


def oq(x: Q) -> int:
    return ordp(x.numerator)-ordp(x.denominator)


def inv(a: int,m: int) -> int:
    u,v,s,t=a,m,1,0
    while v:
        q=u//v;u,v=v,u-q*v;s,t=t,s-q*t
    check(u==1,'noncoprime moduli')
    return s%m


def T(n: int) -> int:
    return (n+(2*n+1)*(n&1))//2


def P(n: int) -> int:
    check(n>0,'positive source')
    z=2*n+1;return z*(z//3**ordp(z))


def C(n: int) -> int:
    z=n+5;return z*(z//3**ordp(z))


def ret(n: int) -> tuple[int,int]:
    check(n>0 and n%3==1,'section source')
    if n==1:return 1,0
    x=n
    for k in range(1,2*n.bit_length()+5):
        x=T(x)
        if x%3==1:return x,k
    raise ValueError('first return clock exceeded')


def parents(y: int,threshold: int | None=None) -> list[tuple[int,int,int,int]]:
    """Literal signed inverse walk; filters only after constructing a real edge."""
    check(y%3==1 and y!=1,'signed section endpoint')
    h=ordp(2*y+1);cur=2*y;j=0;out=[]
    while cur%3==2:
        gap=h-j
        if threshold is None or gap<threshold:
            out.append((2*cur,j,2,gap))
        previous=(2*cur-1)//3
        check(T(previous)==cur and previous%2,'ordinary odd predecessor')
        j+=1;cur=previous
    if cur%3==1:
        out.append((cur,j,1,0))
    out.sort(key=lambda row:(row[2]==1,-row[1]))
    return out


def ball(n: int,D: int,reduced: bool) -> dict[int,tuple[int,int,int]]:
    answer={n:(0,0,0)};queue=[n];index=0
    while index<len(queue):
        y=queue[index];index+=1
        q0,k0,d=answer[y]
        if d==D or y==1:continue
        for x,q,e,g in parents(y,4*(D-d)-2 if reduced else None):
            if x not in answer:
                answer[x]=(q0+q,k0+q+e,d+1);queue.append(x)
    return answer


def inverse_tests() -> dict:
    cases=[(n,d) for n in range(4,388,3) for d in range(7)]
    cases.extend([(208363,3),(29371,2),(121,8),(859,6)])
    rows=[]
    for n,d in cases:
        f,g=ball(n,d,False),ball(n,d,True)
        a,b=min(f,key=P),min(g,key=P)
        check(a==b,'different inverse minimum')
        for x,(q,k,dd) in f.items():
            check(x<=n*4**dd and 3**q*x<=2**k*n and k-q<=2*dd,'height/clock bounds')
        rows.append([n,d,a,len(f),len(g)])
    return {'cases':len(rows),'full_nodes_sum':sum(x[3] for x in rows),
            'pruned_nodes_sum':sum(x[4] for x in rows),'rows_sha256':seal(rows)}


def negative_tests() -> dict:
    nodes={-2:(0,0,0)};layers=[[-2]];table=[]
    for d in range(11):
        if d:
            new=[]
            for y in layers[-1]:
                q0,k0,_=nodes[y]
                for x,q,e,g in parents(y):
                    check(x not in nodes and x<=-2,'negative repeat/sign')
                    nodes[x]=(q0+q,k0+q+e,d);new.append(x)
            layers.append(new)
        B=max(q+ordp(2*n+1)+1 for n,(q,k,t) in nodes.items())
        check(d//3+2<=B<=4*d+2,'linear precision bound')
        table.append([d,len(nodes),B])
    product_rows=[]
    for v,(q,k,t) in sorted(nodes.items()):
        x=v;odds=[]
        for _ in range(k):
            if x&1:odds.append(abs(x))
            x=T(x)
        check(x==-2 and len(odds)==q and len(set(odds))==q,'negative ordinary word')
        # Product compared as separate integer numerators/denominators.
        a=b=1
        for i,m in enumerate(sorted(odds),1):
            check(m>=2*i+1,'distinct odd magnitudes')
            a*=3*m-1;b*=3*m
        check((q+1)*a**5>=b**5,'product lower bound')
        m=q+ordp(2*v+1)
        check(3**(5*m)<=32*m*4**(5*t)*2**(5*m),'precision consequence')
        product_rows.append([v,q,k,t,m])
    y=-2;q=0;greedy=[]
    for d in range(65):
        check(q>=d//3,'greedy odd frequency')
        greedy.append([d,y,q])
        odds=[x for x,qq,ee,g in parents(y) if qq==1 and ee==1]
        if odds:
            y=odds[0];q+=1
        else:y*=4
    # Elementary coefficient expansion, independently via polynomial products.
    def mul(a,b):
        z=[0]*(len(a)+len(b)-1)
        for i,u in enumerate(a):
            for j,v in enumerate(b):z[i+j]+=u*v
        return z
    a=b=[1]
    for _ in range(5):a=mul(a,[2,6]);b=mul(b,[3,6])
    a=mul(a,[1,1]);b=mul(b,[0,1])
    diff=[u-v for u,v in zip(a,b)]
    check(diff==[32,269,930,1800,2160,1296,0],'polynomial coefficient identity')
    prows=[]
    for i in range(1,129):
        value=sum(c*i**j for j,c in enumerate(diff))
        check(value>0,'strict polynomial comparison')
        prows.append([i,value])
    check(Q(3,2)**50>320*4**10 and Q(81,64)**5>Q(7,5),'induction base and ratio')
    return {'precision_table':table,'negative_vertices':len(nodes),
            'product_rows_sha256':seal(product_rows),'greedy_edges':64,
            'greedy_sha256':seal(greedy),'polynomial_cases':128,'polynomial_sha256':seal(prows)}


def remainder_tests() -> dict:
    rows=[]
    for k in range(1,13):
        minima={};codes=set()
        for source in range(2**k):
            n=source;q=0;word=[]
            for _ in range(k):
                bit=n&1;word.append(bit);q+=bit;n=T(n)
            codes.add(tuple(word))
            B=2**k*(2*n+1)-3**q*(2*source+1)
            minima[q]=min(minima.get(q,B),B)
        check(len(codes)==2**k,'physical parity coverage')
        for q,b in sorted(minima.items()):
            check(b==3**q+2**k-2**(q+1),'minimum B formula')
            rows.append([k,q,b])
    check(all(10*8**r>8*4**r for r in range(1,65)),'ghost comparison')
    return {'words':sum(2**j for j in range(1,13)),'minima_sha256':seal(rows),'ghost_lengths_checked':64}


def symbolic_test(D: int) -> dict:
    Arows=[];Brows=[];highs=[];t0=5*2**(4*D+1);K=36*D+20
    for r in range(D+1):
        # Reconstruct the ordinary forward affine map on two symbolic inputs.
        a,b=Q(1,2),Q(-1,2)
        for _ in range(r):a,b=9*a/8,(9*b+5)/8
        queue=[(a,b,0,0,0)];pos=0
        while pos<len(queue):
            a,b,q,k,d=queue[pos];pos+=1
            check((b*2**(3*r+1)).denominator==1 and abs(b)+2<=12*8**D,'A comparison size')
            if 2*b+1==0:
                p=q-2*r
                check(k==3*r and a==Q(1,2)*Q(3)**(-p) and -2*r<=p<=0,'homogeneous alternatives')
                highs.append([r,d,p])
                if d==D:continue
                # Use an ordinary high comparison with depth h0-p; pick exactly
                # the gap-limited roots, then recover their slope in t.
                h0=4*D+1
                high_comparison=(3**(h0-p)*5-1)//2
                root_edges=parents(high_comparison,4*(D-d)-2)
                for root,qq,ee,gap in root_edges:
                    bb=Q(-1 if ee==1 else -2)
                    aa=Q(root-bb,t0)
                    check(root<2**(10*D+5) and aa>=1,'B root')
                    pending=[(root,aa,bb,0,0)];at=0
                    while at<len(pending):
                        xx,aa,bb,odd,dd=pending[at];at+=1
                        H=ordp(2*xx+1)
                        check(xx<2**(12*D+5) and H<=12*D+6,'B height bound')
                        check(odd<=24*D+10 and oq(2*aa)>=-odd and K+1+oq(2*aa)>H,'B frozen precision')
                        check(aa>=Q(2,3)**odd and abs(bb)+2<=4**(D+1),'B affine bounds')
                        Brows.append([r,d,p,dd,odd,H,str(aa),str(bb)])
                        if dd==D-d-1:continue
                        for child,qedge,ev,g in parents(xx):
                            slope=Q(2**(qedge+ev),3**qedge)
                            constant=Q(child)-slope*xx
                            pending.append((child,slope*aa,slope*bb+constant,odd+qedge,dd+1))
                continue
            H=oq(2*b+1)
            check(1<=H<=4*D+4 and q<=min(4*D*(D+1),24*D+16),'A ternary depth')
            check(a>=Q(1,2)*Q(2,3)**q and oq(2*a)==2*r-q,'A slope')
            Arows.append([r,d,q,k,H,str(a),str(b)])
            if d==D:continue
            # Compose rational backward shortcut maps one edge at a time.
            ca,cb=2*a,2*b
            for j in range(H):
                queue.append((2*ca,2*cb,q+j,k+j+2,d+1))
                ca,cb=2*ca/3,(2*cb-1)/3
            check(cb.denominator%3!=0,'dyadic terminal comparison')
            if cb.numerator*inv(cb.denominator,3)%3==1:
                queue.append((ca,cb,q+H,k+H+1,d+1))
    Arows.sort();Brows.sort();highs.sort()
    return {'D':D,'A_low_nodes':len(Arows),'A_high_nodes':len(highs),'B_nodes':len(Brows),
            'A_sha256':seal(Arows),'high_sha256':seal(highs),'B_sha256':seal(Brows)}


def make_family(D: int,extra: int,lift: int,full: bool) -> dict:
    h=256*(D+1)+extra;K=36*D+20;L=2*(h+D+2);N=3*D+L+1
    # Reverse the prescribed physical word from the symbolic odd endpoint
    # 1 mod2; final affine integrality fixes the source residue.
    word='110'*D+'0'*L+'1'
    q=2*D+1
    A=15*(9**D-8**D)+2**(3*D+L)
    residue=(-A*inv(3**q,2**N))%(2**N)
    mod2=2**(N+1);mod3=3**(K+1)
    a=((2*residue+1)*inv(3**h,mod2))%mod2
    b=(5*2**(4*D+1)*inv(pow(2,h,mod3),mod3))%mod3
    u=a+mod2*((b-a)*inv(mod2,mod3)%mod3)+lift*mod2*mod3
    n=(3**h*u-1)//2
    check(n>0 and n%2 and ordp(2*n+1)==h and u%2 and u%3,'CRT source')
    check((2**h*u-5*2**(4*D+1))%mod3==0,'CRT precision')
    y=n;rows=[];total=0
    for r in range(D+1):
        short=ball(y,D,True)
        check(min(short,key=P)==n,'bounded section box minimum')
        longer=ball(y,D,False) if full else None
        if longer is not None:check(min(longer,key=P)==n,'unpruned box minimum')
        rows.append([r,len(short),len(longer) if longer is not None else None]);total+=len(short)
        if r<D:
            z,cost=ret(y)
            check(cost==3 and z>y and 64*C(z)==9*C(y),'alternate rank')
            if r==0:
                check(P(n)<C(n)<P(z) and P(n)<C(z),'minimum/maximum both increase')
            y=z
    check(ordp(y,2)==L,'terminal length')
    m=y//2**L
    check(m%2 and m%3==1 and 4*P(m)<P(n),'P repayment')
    check(64**D*C(y)==9**D*C(n),'corridor identity')
    x=n
    for bit in word[:-1]:
        check(x%2==int(bit),'actual repayment bit');x=T(x)
    check(x==m,'actual endpoint')
    return {'D':D,'h':h,'K':K,'lift':lift,'L':L,
            'source_bits':n.bit_length(),'endpoint_bits':m.bit_length(),
            'source_sha256':ihex(n),'unit_sha256':ihex(u),'endpoint_sha256':ihex(m),
            'box':rows,'full_box_replayed':full,'pruned_nodes':total,
            'repayment_shortcut_steps':3*D+L,'repayment_section_returns':D+L//2,
            'P_quarter_drop':True,'corridor_rank_each_ratio':[9,64],'naive_min_max_increase':True}


def control_tests() -> dict:
    low=[x for x in range(1,122) if P(x)<243]
    U=set()
    for x in low:
        seen=set()
        while x not in seen:
            check(len(seen)<128,'control clock');seen.add(x);U.add(x);x=T(x)
        check(x in (1,2),'finite cycle control')
    x=121;steps=returns=0
    while x not in U:
        x,cost=ret(x);steps+=cost;returns+=1
    check([returns,steps,x]==[16,54,40],'121 exact meeting')
    old={208363};layer={208363}
    for _ in range(3):
        layer={x for y in layer for x,q,e,g in parents(y) if g<=1};old.update(layer)
    allnodes=ball(208363,3,False)
    check(min(old,key=P)==208363 and min(allnodes,key=P)==4445077,'old boundary pruning')
    return {'lower_rank_pool_121':low,'forward_union':sorted(U),'first_meeting_121':[16,54,40],
            'old_pruning_control':[208363,4445077]}



def compressed_test(D: int) -> dict:
    h=256*(D+1);K=36*D+20;M=h+2*D+K+1;mod=3**M
    desired=(9**(D+1)-10*8**D+3**(h+2*D)*5*2**(4*D+1)*inv(2**h,mod))%mod
    desired=desired*inv(2**(3*D+1),mod)%mod
    check(desired%3==1,'principal unit')
    # Remove the selected digit from the residual target, rather than build
    # the generator's accumulated product.
    residual=desired;unit=4;unit_inverse=inv(4,mod);position=1;power=9;value=0;digits=[]
    for _ in range(M-1):
        options=[d for d in (0,1,2) if pow(unit,d,power)==residual%power]
        check(len(options)==1,'ternary log digit')
        d=options[0];digits.append(d);value+=d*position
        residual=residual*pow(unit_inverse,d,mod)%mod
        unit=unit*unit*unit%mod;unit_inverse=unit_inverse**3%mod;position*=3;power*=3
    check(residual==1 and pow(4,value,mod)==desired,'full modular logarithm')
    while value<h+D+2:value+=position
    L=2*value
    check(L>=2*(h+D+2),'terminal lower bound')
    numerator=(pow(2,3*D+L+1,mod)+10*8**D-9**(D+1))%mod
    check(ordp(numerator)==h+2*D,'compressed depth')
    u=numerator//3**(h+2*D)
    check((pow(2,h,3**(K+1))*u-5*2**(4*D+1))%3**(K+1)==0,'compressed cofactor')
    return {'D':D,'h':h,'K':K,'modulus_exponent':M,
            'terminal_even_steps_hex':hex(L),'exponent_lifting_digits_sha256':seal(digits),
            'source_expression':'(2^(3D+L)+5*(8^D-9^D))/9^D',
            'exact_word':'(110)^D 0^L','endpoint':1,
            'ordinary_source_materialized':False,'all_steps_literally_replayed':False,
            'modular_guards_replayed':True}


def reconstruct() -> dict:
    rows=[make_family(D,e,l,D<=2 and e==0 and l==0) for D in (1,2,3,4) for e,l in ((0,0),(0,1),(1,0))]
    body={'schema':'X-ALF-001/v1','base':BASE,'scope':SCOPE,
          'negative':negative_tests(),'inverse':inverse_tests(),'remainders':remainder_tests(),
          'symbolic':[symbolic_test(D) for D in range(1,6)],'families':rows,'compressed_convergence':[compressed_test(D) for D in (1,2,3,4)],'controls':control_tests()}
    return {'body':body,'sha256':seal(body)}


def validate(report: dict,expected: dict) -> None:
    check(set(report)=={'body','sha256'},'report keys')
    check(report['sha256']==seal(report['body']),'bad seal')
    check(report==expected,'mathematics, coverage, or scope mismatch')


def self_test(expected: dict) -> int:
    edits=[lambda b:b['scope'].update(collatz_proved=True),
           lambda b:b['scope'].update(box='all ordinary raw-clock witnesses'),
           lambda b:b['families'].pop(),lambda b:b['families'][0].update(K=0),
           lambda b:b['negative']['precision_table'][6].__setitem__(2,2),
           lambda b:b['symbolic'][0].update(B_nodes=0),
           lambda b:b['controls'].__setitem__('first_meeting_121',[15,53,40]),
           lambda b:b['inverse'].update(cases=1),
           lambda b:b['families'][0].update(P_quarter_drop=False),
           lambda b:b['remainders'].update(words=1),
           lambda b:b['compressed_convergence'][0].update(all_steps_literally_replayed=True),
           lambda b:b['compressed_convergence'][0].update(terminal_even_steps_hex='0x2')]
    for mutate in edits:
        bad=copy.deepcopy(expected);mutate(bad['body'])
        check(bad['body']!=expected['body'],'no-op mutation')
        bad['sha256']=seal(bad['body'])
        try:validate(bad,expected)
        except ValueError as e:
            check('mismatch' in str(e),'rejected by seal instead of semantics')
        else:raise ValueError('resealed false report accepted')
    return len(edits)


def main() -> None:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('report',type=Path);p.add_argument('--self-test',action='store_true')
    p.add_argument('--output',type=Path)
    args=p.parse_args();expected=reconstruct()
    validate(json.loads(args.report.read_text(encoding='utf-8')),expected)
    if args.output:args.output.write_bytes(json.dumps(expected,sort_keys=True,indent=2).encode()+b'\n')
    print('SEPARATE RECONSTRUCTION PASS',expected['sha256'])
    if args.self_test:print('RESEALED CORRUPTIONS REJECTED',self_test(expected))


if __name__=='__main__':main()
