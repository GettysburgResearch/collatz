#!/usr/bin/env python3
"""Independent exact checker for the centered-recurrence review.

No author or repository code is imported. Integer/Fraction assertions are
corroboration and counterexample search, not substitutes for universal proofs.
"""
from __future__ import annotations
import argparse, hashlib, itertools, json, math, platform, random, sys
from fractions import Fraction
from pathlib import Path

SEED=0x93159318
R=random.Random(SEED)

def digest(x):
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def companion(M,N,period,n):
    r=Fraction(M,N); p=len(period); phase=n%p
    s=sum(Fraction(period[(phase+j)%p])*r**j for j in range(p))
    return Fraction(N-M,N)*s/(1-r**p)

def cylinder(M,N,e):
    Rs=[0]; Cs=[0]; qs=[]; mp=np=1; inv=pow(N,-1,M)
    for k in range(len(e)-1):
        d=e[k]-e[k+1]
        q=(-pow(inv,k+1,M)*(N*Cs[-1]+d))%M
        num=N*(Cs[-1]+q*np)+d
        assert num%M==0
        qs.append(q); Rs.append(Rs[-1]+q*mp); Cs.append(num//M)
        mp*=M; np*=N
    return Rs,qs,Cs

def direct_R(M,N,e):
    K=len(e)-1
    if K==0:return 0
    mod=M**K
    return (-sum((e[i]-e[i+1])*M**i*pow(N,-i-1,mod) for i in range(K)))%mod

def replay(M,N,e,B0):
    B=[B0]
    for i in range(len(e)-1):
        z=N*B[-1]+e[i]-e[i+1]; assert z%M==0; B.append(z//M)
    return B

def thue(n):return n.bit_count()&1

def thue_word(n,flip=0):return [thue(i)^flip for i in range(n)]

def factor_complexity(w,n):return len({tuple(w[i:i+n]) for i in range(len(w)-n+1)})

def check_errors():
    charts=pos=signs=endpoints=0
    for M in range(2,15):
      for N in range(M+1,21):
       if math.gcd(M,N)>1:continue
       charts+=1
       for p in range(1,6):
        for per in itertools.product((0,1),repeat=p):
         x=[companion(M,N,per,n) for n in range(p)]
         u=[Fraction(per[n]-x[n],M) for n in range(p)]
         for n in range(p):
          j=(n+1)%p; assert N*u[n]-M*u[j]==per[n]-per[j]; assert abs(u[n])<=Fraction(1,N);pos+=1
          if len(set(per))>1: assert u[n]!=0 and abs(u[n])<Fraction(1,N) and ((u[n]>0)==bool(per[n]));signs+=1
         for z in (Fraction(1,N),Fraction(-1,N)):
          a=[(c,Fraction(N*z-c,M)) for c in (-1,0,1) if abs(Fraction(N*z-c,M))<=Fraction(1,N)]
          assert a==[(1 if z>0 else -1,Fraction(0))];endpoints+=1
    return {"charts":charts,"periodic_phase_positions":pos,"strict_nonconstant_sign_checks":signs,"endpoint_transition_checks":endpoints}

def check_cylinders():
    ex=dr=traces=positions=0; maxd=0
    for M,N in [(2,3),(3,4),(4,5),(5,7),(8,9),(16,17),(64,81)]:
      top=8 if M==64 else 7
      for K in range(1,top):
       for e in itertools.product((0,1),repeat=K+1):
        Rs,qs,Cs=cylinder(M,N,e); assert Rs[-1]==direct_R(M,N,e); assert replay(M,N,e,Rs[-1])[-1]==Cs[-1]
        assert all(Rs[k+1]==Rs[k]+qs[k]*M**k for k in range(K));ex+=1;dr+=1;maxd=max(maxd,K)
    charts=[(M,N) for M in range(2,25) for N in range(M+1,35) if math.gcd(M,N)==1]
    for _ in range(500):
      M,N=R.choice(charts); K=R.randint(12,80); e=[R.randrange(2) for _ in range(K+1)]
      Rs,_,_=cylinder(M,N,e); B0=Rs[-1]+R.randint(1,4)*M**K; replay(M,N,e,B0)
      period=tuple(e[-R.randint(1,min(9,len(e))):])
      if len(set(period))==1:period=(0,1)
      for n in range(len(period)):
       x=companion(M,N,period,n);u=Fraction(period[n]-x,M);y=Fraction(B0)+u
       assert abs(u)<Fraction(1,N) and ((u>0)==bool(period[n])); assert math.ceil(M*y)==M*B0+period[n]
       positions+=1
      traces+=1;maxd=max(maxd,K)
    return {"exhaustive_prefixes":ex,"direct_residue_checks":dr,"random_general_chart_traces":traces,"centered_trace_positions":positions,"max_depth":maxd}

def finite_survivor(e,A0):
    A=[A0]
    for c in e:
      z=81*A[-1]-17*c
      if z%64:return None
      A.append(z//64)
    return A

def check_recurrence():
    words=long=chains=nextc=cone=0
    def audit(e,A):
      nonlocal chains,nextc,cone
      L=len(e);seen={}
      for ell in range(1,min(48,L)+1):
       seen.clear()
       for t in range(L-ell+1):
        f=tuple(e[t:t+ell])
        if f in seen:
         r=seen[f];D=[A[r+i]-A[t+i] for i in range(ell+1)]
         assert all(64*D[i+1]==81*D[i] for i in range(ell)); assert D[0]!=0
         assert 64**ell<=abs(D[0]); assert ell<math.log(A[0],64)+math.log(81/64,64)*t;chains+=1;cone+=1
         if t+ell<L and e[r+ell]!=e[t+ell]: assert 64*(A[r+ell+1]-A[t+ell+1])-81*D[-1] in (-17,17);nextc+=1
        else:seen[f]=t
    for K in range(3,11):
     for e in itertools.product((0,1),repeat=K+1):
      Rs,_,_=cylinder(64,81,list(e)+[0]); A0=64*(Rs[-1]+64**len(e))+e[0];A=finite_survivor(e,A0);assert A;audit(e,A);words+=1
    for _ in range(300):
     K=R.randint(80,180);e=[R.randrange(2) for _ in range(K+1)];Rs,_,_=cylinder(64,81,e+[0]);A0=64*(Rs[-1]+R.randint(1,3)*64**len(e))+e[0];A=finite_survivor(e,A0);assert A;audit(e,A);long+=1
    return {"exhaustive_finite_survivor_words":words,"random_long_finite_survivor_words":long,"repeated_factor_chains":chains,"first_nonzero_difference_carries":nextc,"global_recurrence_cone_checks":cone,"max_random_depth":180}

def check_thue(limit):
    e=thue_word(limit+1);_,q,C=cylinder(64,81,e);zeros=[i for i,x in enumerate(q) if x==0];run=best=0
    for x in q:run=run+1 if x==0 else 0;best=max(best,run)
    sq=0;maxm=0
    for m in range(16):
     L=1<<m
     if 3*L>len(e):break
     assert e[L:2*L]==e[2*L:3*L];sq+=1;maxm=m
    for k,x in enumerate(q):
     d=e[k]-e[k+1];assert x==(-pow(pow(81,-1,64),k+1,64)*(81*C[k]+d))%64
    return {"blocks_checked":limit,"nonzero_blocks":limit-len(zeros),"zero_blocks":len(zeros),"longest_zero_run":best,"first_50_zero_positions":zeros[:50],"last_zero_position":zeros[-1],"square_witnesses":sq,"max_square_m":maxm,"max_square_length":1<<maxm}

def morph(w,img):return [b for c in w for b in img[c]]
def check_morph():
    cases=0;dist=Fraction(0)
    for _ in range(300):
     img={c:tuple(R.randrange(2) for _ in range(R.randint(1,10))) for c in (0,1)};a=min(map(len,img.values()));b=max(map(len,img.values()));dist=max(dist,Fraction(b,a));L=1<<R.randint(3,10);w=thue_word(3*L);o=morph(w,img);r=len(morph(w[:L],img));t=len(morph(w[:2*L],img));blk=morph(w[L:2*L],img);assert blk==morph(w[2*L:3*L],img) and o[r:r+len(blk)]==o[t:t+len(blk)] and len(blk)>=a*L and t<=2*b*L;cases+=1
    return {"random_non_erasing_morphisms":cases,"transferred_factor_checks":cases,"maximum_tested_distortion":f"{dist.numerator}/{dist.denominator}"}

def check_transducers():
    cases=0;maxQ=12
    for _ in range(400):
     Q=R.randint(1,maxQ);delta=[[R.randrange(Q) for _ in (0,1)] for _ in range(Q)];out=[[tuple(R.randrange(2) for _ in range(R.randint(1,5))) for _ in (0,1)] for _ in range(Q)];init=[R.randrange(2) for _ in range(R.randint(0,6))];a=min(len(out[s][c]) for s in range(Q) for c in (0,1));b=max(len(out[s][c]) for s in range(Q) for c in (0,1));shift=R.randint(0,31);L=1<<R.randint(6,10);raw=thue_word((2*Q+3)*L+shift,R.randrange(2));inp=raw[shift:];state=0;states=[0];pos=[len(init)];bits=list(init)
     for c in inp:bits+=out[state][c];state=delta[state][c];states.append(state);pos.append(len(bits))
     starts=[j*L-shift for j in range(2*Q+2) if thue(j)==1];assert len(starts)==Q+1 and min(starts)>=0;seen={};pair=None
     for x in starts:
      if states[x] in seen:pair=(seen[states[x]],x);break
      seen[states[x]]=x
     assert pair;r,t=pair;assert bits[pos[r]:pos[r+L]]==bits[pos[t]:pos[t+L]];assert pos[r+L]-pos[r]>=a*L and pos[t]<=len(init)+b*(2*Q+1)*L;cases+=1
    return {"random_transducers":cases,"synchronized_state_pairs":cases,"identical_output_factor_checks":cases,"max_states":maxQ}

def completion_fraction(period):
    p=len(period);S=sum((period[j]-period[(j+1)%p])*64**j*81**(p-j-1) for j in range(p));return -S,81**p-64**p

def base64_digits(num,den,n):
    inv=pow(den,-1,64);o=[]
    for _ in range(n):q=(num*inv)%64;o.append(q);num=(num-q*den)//64
    return o

def check_complexity():
    ce=[]
    for bit in (0,1):
     e=[bit]*65;_,q,_=cylinder(64,81,e);assert all(factor_complexity(e,n)==1 for n in range(1,17)) and not any(q);ce.append({"word":f"{bit}^infinity","factor_complexity":"p(n)=1","liminf_p_over_n":0,"cylinder_blocks":"q_K=0 for every K"})
    scanned=best=0;wit=None;depth=2048
    for p in range(1,14):
     words=itertools.product((0,1),repeat=p) if p<=10 else [tuple(R.randrange(2) for _ in range(p)) for _ in range(96)]
     for per in words:
      if len(set(per))==1:continue
      num,den=completion_fraction(per);q=base64_digits(num,den,depth);run=0
      for x in reversed(q):
       if x:break
       run+=1
      if run>best:best=run;wit={"period":"".join(map(str,per)),"run":run}
      scanned+=1
    return {"T-9318_section3_counterexamples":ce,"nonconstant_periodic_words_scanned":scanned,"periodic_scan_depth":depth,"largest_terminal_zero_run":best,"largest_terminal_zero_run_witness":wit}

def run(limit):
    checks={"centered_error_paths":check_errors(),"cylinders_and_reconstruction":check_cylinders(),"orbit_difference_and_recurrence":check_recurrence(),"thue_morse_blocks":check_thue(limit),"morphic_transfer":check_morph(),"transducer_transfer":check_transducers(),"factor_complexity_and_refutation":check_complexity()}
    p={"reviewer":"gpt56-review-9315-01","target_commit":"900ba417c968d8a41bc56a30d3ccc941284d8ce2","seed":SEED,"checks":checks};p["semantic_digest"]=digest(p);return p

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--output",type=Path);ap.add_argument("--check-results",type=Path);ap.add_argument("--thue-limit",type=int,default=32768);a=ap.parse_args();p=run(a.thue_limit);s=json.dumps(p,indent=2,sort_keys=True)+"\n"
    if a.output:a.output.write_text(s)
    if a.check_results and p!=json.loads(a.check_results.read_text()):print("frozen result mismatch",file=sys.stderr);return 1
    print(s,end="");print(json.dumps({"python":platform.python_version(),"platform":platform.platform()},sort_keys=True),file=sys.stderr);return 0
if __name__=="__main__":raise SystemExit(main())
