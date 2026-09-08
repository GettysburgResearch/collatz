#!/usr/bin/env python3
"""Independent finite families, rank sublevels and schema controls; not universal proofs."""
from __future__ import annotations
import json
from collections import Counter
from fractions import Fraction as F
from hashlib import sha256
from math import isqrt
from review_checks import need,T,g,R,Gamma,Gamma_detail,rho,val,affine,iterate,P,inverse_min,inverse_ball,A,B,safe

WORDS=['1','110','1110','111010','1110110','11101110110','1110'*4+'110','1110'*8+'110']

def digest(x):return sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def periodic_parameters(w):
    m=len(w);Q,P0,A0=affine(map(int,w));D=Q-P0;avs=[];ds=[]
    need(D>0 and all(w!=w[:d]*(m//d) for d in range(1,m) if m%d==0),'primitive expanding')
    for i in range(m):
        v=w[i:]+w[:i];av=affine(map(int,v))[2];avs.append(av)
        for r in range(1,m):
            qr,dr,ar=affine(map(int,v[:r]));c=D*ar-(qr-dr)*av
            need(c!=0,'proper phase repeat');ds.append(val(c,3))
    b=max([0]+ds);j=1
    while Q**j<2**(m+1)*P0**j:j+=1
    K=(j+1)*m;M=2*3**K+max(avs)+1;H=b+1
    while 3**H<=4*(D+1)**2*3**b:H+=1
    return m,Q,P0,A0,D,b,j,K,M,H,6*P0*D,max(avs)


def periodic_tests():
    rows=[];positions=0;old_edges=0
    for w in WORDS:
        m,Q,P0,A0,D,b,j,K,M,H0,U,AM=periodic_parameters(w)
        for extra in (0,2):
            H=H0+extra
            for L in (1,3):
                threshold=3**(H+w.count('1')*(L+1))*U*U;c=0
                while 4**c<threshold:c+=1
                a=1
                while P0**a<=2*D*U+2*D*M+2*AM or Q**a<2**(c+1)*P0**a:a+=1
                N=a+L+1
                residue=(A0*pow(P0**N*3**H,-1,D))%D if D>1 else 0
                us=[residue+t*D for t in range(7) if 0<residue+t*D<=6*D and (residue+t*D)%6 in(1,5)]
                need(len(us)==2,'unit representatives')
                for u in us:
                    n=(P0**N*3**H*u-A0)//D;x=n;z0=P0**(2*N)*3**H*u*u;q=0
                    for r in range(m*L+1):
                        z,ks=Gamma_detail(x)
                        need(ks==[m] and z*4**r==3**q*z0,'global phase prefix minimum')
                        positions+=1
                        if w=='111010' and r<m*L and r%6 in (0,4):
                            need(not safe(x),'old unsafe phase');old_edges+=1
                        if r<m*L:need(x%2==int(w[r%m]),'actual phase word');q+=x%2;x=T(x)
                    need(x>n,'expanding period endpoint')
                    rows.append([w,H,L,u,N,n.bit_length()])
    return dict(families=len(rows),phase_positions=positions,old_unsafe_edges=old_edges,rows=rows)


def ball_tests():
    out=[]
    for M in (1,4,16,64,256,1024,4096,16384,65536):
        ns=[n for n in range(2,M+1) if Gamma(n)<=M]
        K=(M.bit_length()-1)//2
        need(len(ns)**2<25*(K+1)**2*M and len(ns)>=isqrt(M)-1,'Gamma ball bounds')
        out.append(dict(M=M,count=len(ns),maximum=max(ns,default=0),sources_sha256=digest(ns)))
    return out


def linear_families():
    rows=[]
    for D in (1,2,3,4):
        for extra,lift in ((0,0),(0,1),(1,0)):
            h=256*(D+1)+extra;K=36*D+20;L=2*(h+D+2);N=3*D+L+1;t0=5*2**(4*D+1)
            rr=(8**D*(5+2**L)*pow(9**D,-1,2**N)-5)%(2**N)
            mod2=2**(N+1);mod3=3**(K+1)
            aa=((2*rr+1)*pow(3**h,-1,mod2))%mod2
            bb=(t0*pow(2**h,-1,mod3))%mod3
            u=aa+mod2*((bb-aa)*pow(mod2,-1,mod3)%mod3)+lift*mod2*mod3
            n=(3**h*u-1)//2;z=n
            need(val(2*n+1,3)==h,'linear depth')
            for r in range(D+1):
                need(inverse_min(z,D)==P(n),'complete pruned box minimum')
                if D<=2 and extra==0 and lift==0:
                    need(min(map(P,inverse_ball(z,D)))==P(n),'unpruned box control')
                if r<D:
                    nxt=iterate(z,3);need(nxt>z,'corridor growth')
                    need(64*g(nxt+5)==9*g(z+5),'alternate rank')
                    z=nxt
            need(val(z,2)==L,'repayment word length');m=z//2**L
            need(m%2 and m%3==1 and 4*P(m)<P(n),'positive section repayment')
            rows.append([D,h,lift,n.bit_length(),m.bit_length(),D+L//2])
    return rows


def fixed_tail_spikes():
    out=[]
    for j in (2,4,6,8):
        M=3**(2**j);n=4*M-5;a=j+4;y,c,p=A(n)
        need(c==a+1 and R(n)==16*M and 9*R(y)==(y+5)**2,'canonical unsafe spike')
        need(not safe(n) and not safe(y) and B(n)[0]==y,'both unsafe guards')
        need(F(R(y),R(n)**2)>F(9,4)**a/1152,'weak rank moment divergence family')
        out.append([j,n.bit_length(),c])
    for k in (1,2,3,4,8,12,16):
        for extra in (0,1,3,8):
            n=3**(2*k+2+extra);y=iterate(n,k)
            need(R(y)*36**(k+1)>=n*n,'fixed clock lower bound')
    return dict(unsafe_family=out,fixed_clock_power_cases=28)


def schema_tests():
    # Exact validation predicate used in X-ATT-001 and X-ATT-003:
    # seal(payload) is checked against the supplied seal, but bare payload
    # equality is checked against reconstruction. Python erases number types.
    expected={'count':1,'scope':False,'source_cutoff':4096}
    controls=[{'count':True,'scope':False,'source_cutoff':4096},
              {'count':1.0,'scope':False,'source_cutoff':4096},
              {'count':1,'scope':0,'source_cutoff':4096},
              {'count':1,'scope':False,'source_cutoff':4096.0}]
    for body in controls:
        report={'payload':body,'sha256':digest(body)}
        need(report['sha256']==digest(report['payload']) and body==expected,'original predicate reproduction')
        need(json.dumps(body,sort_keys=True)!=json.dumps(expected,sort_keys=True),'strict comparator rejection')
    return {'resealed_type_substitutions_accepted_by_original_predicate':4,
            'rejected_by_canonical_typed_comparison':4,'scope':'isolated exact predicates, not full original verifier execution'}

def compressed_families():
    """Verify exponent congruences; never materialize 2**L or its source."""
    rows=[]
    for D in (1,2,3,4):
        h=256*(D+1);K=36*D+20;M=h+2*D+K+1;mod=3**M;t0=5*2**(4*D+1)
        target=(9**(D+1)-10*8**D+3**(h+2*D)*t0*pow(2**h,-1,mod))*pow(2**(3*D+1),-1,mod)%mod
        need(target%3==1,'principal unit')
        exponent=0;step=1;modsmall=9;current=1;generator=4
        for j in range(M-1):
            valid=[d for d in range(3) if current*pow(generator,d,modsmall)%modsmall==target%modsmall]
            need(len(valid)==1,'unique exponent lift')
            digit=valid[0];exponent+=digit*step
            current=current*pow(generator,digit,mod)%mod
            generator=pow(generator,3,mod);step*=3;modsmall*=3
        need(pow(4,exponent,mod)==target,'complete exponent congruence')
        while exponent<h+D+2:exponent+=step
        L=2*exponent
        numerator=(pow(2,3*D+L+1,mod)+10*8**D-9**(D+1))%mod
        need(val(numerator,3)==h+2*D,'exact compressed depth')
        need((pow(2,h,3**(K+1))*(numerator//3**(h+2*D))-t0)%3**(K+1)==0,'compressed cofactor')
        rows.append(dict(D=D,modulus_exponent=M,L_hex=hex(L),materialized_source=False,literal_full_path_replay=False))
    return rows


def rho_phases():
    w='111010';phases=[73,101,143,206,103,146];rows=[]
    # All competing words are actually enumerated at these 21 positions.
    for e in (33,49,65):
        n=(3**e*64-73)//17;x=n;q=0
        for j in range(7):
            expected=3**(e+q)*2**(2*(6-j))
            need(17*x+phases[j%6]==3**(e+q)*2**(6-j),'rho physical phase')
            need(rho(x)==expected,'full rho minimum')
            rows.append([e,j,x,expected])
            if j<6:need(x%2==int(w[j]),'rho parity');q+=x%2;x=T(x)
        # Exit lower bounds use the written all-word argument, not an
        # infeasible enumeration of the successor's entire dictionary.
        need(x%8==2 and 17*x+73==3**(e+4),'exit premises only')
    return dict(positions=len(rows),rows_sha256=digest(rows),phase_depths=[33,49,65])


def unsafe_unit_shadows():
    rows=[]
    for J in (1,2,4,8,16,32,52,64,128):
        K=(J+1)//2+1;mod=2**(6*(K+1));r=(-73*pow(17,-1,mod))%mod
        x=r+mod*((10-r)*pow(mod,-1,243)%243);source=x
        for _ in range(J):
            need(not safe(x),'unsafe unit source')
            y,clock,safe_count,peak=B(x)
            need(y>1 and safe_count==0 and not safe(y),'unsafe unit shadow')
            x=y
        rows.append([J,source,x])
    return dict(cases=len(rows),maximum_returns=128,rows_sha256=digest(rows),source_mass=1,surviving_mass=1)


if __name__=='__main__':
    result=dict(compressed=compressed_families(),rho_phases=rho_phases(),unsafe_shadows=unsafe_unit_shadows(),periodic=periodic_tests(),Gamma_balls=ball_tests(),linear_families=linear_families(),
                tail_spikes=fixed_tail_spikes(),schema=schema_tests(),
                rank_nonordering=[[7,rho(7),Gamma(7)],[14,rho(14),Gamma(14)]])
    print(json.dumps(result,sort_keys=True,indent=2))
