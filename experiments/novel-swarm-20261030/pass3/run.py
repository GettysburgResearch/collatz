#!/usr/bin/env python3
"""Pass 3 exact bounded experiments; four processes, not independent agents.
Standard library only, Python >=3.11. Checks remain active under -OO.
A completed census or a closed finite span is not a full Collatz proof.
"""
import argparse, hashlib, json, sys
from concurrent.futures import ProcessPoolExecutor
from fractions import Fraction as F
from math import comb
from itertools import product
from random import Random

def matvec(M,v,p):return tuple(sum(a*b for a,b in zip(row,v))%p for row in M)
def dot(u,v,p):return sum(a*b for a,b in zip(u,v))%p
def evaluate(model,n):
 p,u,v,M0,M1=model
 if n<1:raise ValueError('positive source required')
 while n:
  v=matvec((M0,M1)[n&1],v,p);n>>=1
 return dot(u,v,p)
def basis_search(initial, step, output,p):
 # Basis vectors retained with words that generate them; reduced rows are auxiliary.
 pivots={};basis=[];words=[];queue=[(initial,())];i=0
 while i<len(queue):
  v,w=queue[i];i+=1
  if output(v)%p:return {'witness':w,'value':output(v)%p,'basis_size':len(basis)}
  z=list(v)
  for j in sorted(pivots):
   if z[j]:
    a=z[j];z=[(x-a*y)%p for x,y in zip(z,pivots[j])]
  j=next((j for j,x in enumerate(z) if x),None)
  if j is None:continue
  inv=pow(z[j],-1,p);pivots[j]=tuple(x*inv%p for x in z)
  basis.append(v);words.append(w)
  for b in (0,1):queue.append((step(b,v),w+(b,)))
 return {'basis':basis,'words':words}
def systems(model):
 p,u,v,M0,M1=model;d=len(v);M=(M0,M1)
 def plain(b,z):return matvec(M[b],z,p)
 ev=tuple((a-b)%p for a,b in zip(matvec(M0,v,p),v))
 def eout(z):return dot(u,plain(1,z),p)
 ov=matvec(M1,v,p)+(0,)*(2*d)+v
 def ostep(b,z):
  out=list(plain(b,z[:d]))+[0]*(3*d)
  for c in range(3):
   y=(3*b+c)%2;cp=(3*b+c)//2
   zz=plain(y,z[(c+1)*d:(c+2)*d])
   for i,a in enumerate(zz):out[(cp+1)*d+i]=(out[(cp+1)*d+i]+a)%p
  return tuple(out)
 def terminal(z):
  result=dot(u,z[:d],p)
  for c in range(3):
   y=z[(c+1)*d:(c+2)*d]
   cc=c
   while cc:y=plain(cc&1,y);cc>>=1
   result-=dot(u,y,p)
  return result%p
 def oout(z):return terminal(ostep(1,z))
 return (ev,plain,eout),(ov,ostep,oout)
def certify(model):
 p,u,v,*_=model;d=len(v)
 certs=[]
 for lane,(initial,step,output) in enumerate(systems(model)):
  r=basis_search(initial,step,output,p)
  if 'witness' in r:
   w=r['witness'];k=(1<<len(w))+sum(b<<i for i,b in enumerate(w))
   n=2*k+lane
   if evaluate(model,n)==evaluate(model,n//2 if n%2==0 else (3*n+1)//2):raise RuntimeError(('bad',lane,r,model,n))
   if n>=1<<(4*d+1):raise RuntimeError('bound')
   return {'kind':'edge','lane':lane,'word':w,'n':n,'basis_size':r['basis_size']}
  certs.append(r)
 return {'kind':'invariant','spans':certs}

def require(ok,message):
 if not ok:raise ValueError(message)
def digest(x):
 return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def rat(x):return [x.numerator,x.denominator]
def oddstep(n):
 require(type(n) is int and n>0 and n%2==1,'positive odd input')
 z=3*n+1;a=(z&-z).bit_length()-1
 return z>>a,a
def path(n,cap=4096):
 states=[];seen=set();q=A=0
 while True:
  require(n not in seen and q<=cap,'trajectory repeated or exhausted before 1')
  seen.add(n);states.append((n,q,A))
  if n==1:return states
  n,a=oddstep(n);q+=1;A+=a

def const_certificate(model):
 p,u,v,M0,M1=model;c=evaluate(model,1);d=len(v)
 initial=v+(1,)
 def step(b,z):return matvec((M0,M1)[b],z[:d],p)+(z[d],)
 def out(z):
  y=step(1,z);return (dot(u,y[:d],p)-c*y[d])%p
 r=basis_search(initial,step,out,p)
 require('witness' not in r,'invariant/nonconstant: rigidity contradiction')
 return {'value':c,'basis':r['basis'],'words':r['words']}

def linear_track():
 R=Random(20261031);counts={'edge':0,'invariant':0};records=[];samples=[]
 def inspect(m,sample=False):
  r=certify(m);counts[r['kind']]+=1
  if r['kind']=='invariant':r={'kind':'constant','certificate':const_certificate(m)}
  records.append([digest(m),digest(r)])
  if sample:samples.append({'model':m,'result':r})
 for d in (1,2):
  for bits in product(range(2),repeat=2*d*d+2*d):
   u=bits[:d];v=bits[d:2*d];z=bits[2*d:]
   M0=tuple(tuple(z[i*d+j] for j in range(d))for i in range(d))
   M1=tuple(tuple(z[d*d+i*d+j] for j in range(d))for i in range(d))
   m=(2,u,v,M0,M1)
   inspect(m,len(samples)<16 and (sum(bits)%3==0))
 for d in (3,4,8,16,32):
  for p in (2,3,5):
   for k in range(12):
    m=(p,tuple(R.randrange(p)for _ in range(d)),tuple(R.randrange(p)for _ in range(d)),
       *(tuple(tuple(R.randrange(p)for _ in range(d))for _ in range(d))for _ in range(2)))
    inspect(m,k==0 and d<=8)
 nilpotent=[]
 for d in (4,8,16,32,48):
  u=(0,)*(d-1)+(1,);v=(1,)+(0,)*(d-1)
  I=tuple(tuple(int(i==j)for j in range(d))for i in range(d))
  N=tuple(tuple(int(i==j+1)for j in range(d))for i in range(d))
  m=(2,u,v,I,N);r=certify(m);inspect(m,True)
  nilpotent.append({'dimension':d,'source':r['n'],'witness_bits':r['n'].bit_length(),
                    'basis_size':r['basis_size']})
 # Hidden/unreachable dimensions must not obstruct a constant certificate.
 for d in (2,4,8):
  p=5;M=[[[R.randrange(p)for _ in range(d)]for _ in range(d)]for _ in range(2)]
  for mat in M:
   for j in range(d):mat[0][j]=int(j==0)
  m=(p,(1,)+(0,)*(d-1),(3,)+(0,)*(d-1),*(tuple(map(tuple,a))for a in M))
  inspect(m,True)
 # Check carry termination/leading digits against direct source evaluation.
 carry_checks=0
 for sample in samples:
  m=sample['model'];p=m[0];(_,_,_), (initial,step,out)=systems(m)
  for k in range(1,257):
   low=bin(k)[3:][::-1];z=initial
   for b in low:z=step(int(b),z)
   require(out(z)==(evaluate(m,2*k+1)-evaluate(m,3*k+2))%p,'carry closure')
   carry_checks+=1
 return {'models':len(records),'outcomes':counts,'model_result_sha256':digest(records),
         'carry_closure_checks':carry_checks,'nilpotent_witnesses':nilpotent,'certificates':samples}

def pressure_track():
 X=65535;targets=(1,3,5,7,13,27,41,127);moments=(1,2)
 mass={(t,s):F(0)for t in targets for s in moments};counts={t:0 for t in targets}
 rows=[];min_ratio=F(1);minimum_source=1;steps=raw_steps=0;enclosures=[];profile={}
 for x in range(1,X+1,2):
  pp=path(x);steps+=len(pp)-1;row=[]
  for n,q,A in pp:
   J=F(3**q,1<<A)
   profile[n]=profile.get(n,F(0))+J*J
   if n not in counts:continue
   r=J*x/n
   require(F(1,1<<100)<r<=1,'first-hit uniform distortion')
   if r<min_ratio:min_ratio=r;minimum_source=x
   counts[n]+=1;row.append([n,q,A])
   for s in moments:mass[n,s]+=J**s
  # A different clock implementation: unaccelerated shortcut steps.
  n=x;q=clock=0;seen_targets={};expected={t:(q,A)for t,q,A in row}
  while True:
   if n%2 and n in targets and n not in seen_targets:seen_targets[n]=(q,clock)
   if n==1:break
   if n%2:n=(3*n+1)//2;q+=1
   else:n//=2
   clock+=1;raw_steps+=1
   require(clock<=8192,'raw clock budget')
  require(seen_targets==expected,'independent clock mismatch')
  rows.append([x,row])
  if x in (255,1023,4095,16383,65535):
   H=mass[1,2];G=F(16,7)*H;upper=G+F(16,7)*F(1,2*(x+1))
   enclosures.append({'source_cap':x,'H1_partial':rat(mass[1,1]),'G2_lower':rat(G),'G2_upper':rat(upper)})
 # A repeated cycle is deliberately NOT a first-hit path.
 require(F(3,4)**256<F(1,1<<100),'cycle distortion countercontrol')
 profile_rows=[[t,*rat(H)]for t,H in sorted(profile.items())]
 return {'source_cap':X,'sources':len(rows),'odd_steps':steps,'raw_steps':raw_steps,
         'global_profile':{'support_size':len(profile),'maximum_support':max(profile),
            'normalized_uniform_error':rat(F(1,2*(X+1))),'sha256':digest(profile_rows)},
         '_profile':profile_rows,
         'record_sha256':digest(rows),'target_counts':counts,'min_discount':rat(min_ratio),
         'min_discount_source':minimum_source,'prefix_enclosures':enclosures,
         'cycle_countercontrol':{'source':1,'repetitions':256,'discount':rat(F(3,4)**256)}}

def transport_track():
 X=4095;seeds=(27,31,41,97,703,871);paths={n:path(n)for n in seeds}
 targets=set(n for pp in paths.values()for n,_,_ in pp);bank={t:{}for t in targets}
 steps=0
 for x in range(1,X+1,2):
  pp=path(x);steps+=len(pp)-1
  for t,q,A in pp:
   if t in bank:bank[t][x]=F(3**q,1<<A)
 records=[];cohort_checks=0;normalization_decrease=None
 for n,pp in paths.items():
  old={};oldK=F(0);oldV=None;trace=[]
  for t,q,A in pp:
   D=F(3**q,1<<A);ell={x:J/D for x,J in bank[t].items()}
   require(set(old)<=set(ell),'fixed-source bank not nested')
   require(all(ell[x]==z for x,z in old.items()),'transport changed old-source weight')
   new={x:z for x,z in ell.items()if x not in old};cohort_checks+=len(new)
   K=sum((z*z for z in ell.values()),F(0));increment=sum((z*z for z in new.values()),F(0))
   require(K==oldK+increment,'exact incoming cohort ledger')
   require(K<F(5,4)*(n*(1<<100))**2,'uniform transported simple-path budget')
   H=sum((J*J for J in bank[t].values()),F(0));V=H/(t*t)
   if oldV is not None and V<oldV and normalization_decrease is None:
    normalization_decrease={'seed':n,'target':t,'previous':rat(oldV),'current':rat(V)}
   trace.append({'target':t,'q':q,'A':A,'K':rat(K),'incoming':len(new),'increment':rat(increment)})
   old,oldK,oldV=ell,K,V
  records.append({'seed':n,'trace':trace})
 require(normalization_decrease is not None,'retain endpoint-only normalization failure')
 # All-history pressure grows after repeated cycles under forward deflation.
 cycleK=F(16,7)/F(3,4)**600
 require(cycleK>F(5,4)*(1<<200),'cycle crosses divergence budget')
 return {'source_cap':X,'sources':(X+1)//2,'odd_steps':steps,'cohort_memberships':cohort_checks,
         'ledger_entries':sum(len(x['trace'])for x in records),'traces':records,
         'endpoint_only_decrease':normalization_decrease,'cycle_K_at_300':rat(cycleK)}

def cylinder_track():
 words=cases=0;rows=[]
 for k in range(1,7):
  for w in product(range(1,5),repeat=k):
   A=C=0;P=1
   for a in w:C=3*C+(1<<A);P*=3;A+=a
   Q=1<<A;mod=2*Q;r=((Q-C)*pow(P,-1,mod))%mod;words+=1
   for lift in (0,1,3):
    n=r+lift*mod;x=n;qs=[]
    for a in w:
     y,actual=oddstep(x);require(actual==a,'cylinder exact valuation');qs.append(x);x=y
    require(Q*x==P*n+C,'full affine identity')
    require(F(C,Q)<=F(3,2)**k-1,'affine remainder bound')
    product_correction=F(x*Q,n*P)
    direct=F(1)
    for z in qs:direct*=F(3*z+1,3*z)
    require(direct==product_correction,'multiplicative correction identity')
    cases+=1
   rows.append([list(w),r,C])
 # Exact rational version of the inherited low-lane and power-margin algebra.
 for q in range(1,97):
  m=5*q//3
  S=sum((F(comb(A-1,q-1),1<<A)for A in range(q,m+1)),F(0))
  bound=F(5,4)**m*F(2,3)**q
  require(S<=bound and bound**3<=F(3125,3456)**q,'Chernoff bound')
 require(8*3125**24<3456**24,'rational power margin')
 # Finite path endpoints outside its inspected horizon need not stay distinct.
 vals=[3,5,1];images=[]
 for n in vals:
  for _ in range(3):n,_=oddstep(n)
  images.append(n)
 require(images==[1,1,1],'terminal discard countercontrol')
 # Known 5x+1 cycle: pressure summability is not cycle exclusion.
 n=13;A=0;cycle=[n]
 for _ in range(3):
  z=5*n+1;a=(z&-z).bit_length()-1;n=z>>a;A+=a;cycle.append(n)
 require(cycle==[13,33,83,13] and A==7,'5x+1 cycle control')
 return {'words':words,'ordinary_lifts':cases,'word_sha256':digest(rows),'exact_low_lane_checks':96,
         'terminal_discard_control':{'sources':vals,'three_step_images':images},
         'five_x_cycle':cycle,'five_x_loop_derivative':rat(F(125,128))}

TRACKS={'linear':linear_track,'pressure':pressure_track,'transport':transport_track,'cylinders':cylinder_track}
def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--serial',action='store_true')
 ap.add_argument('--track',choices=TRACKS);ap.add_argument('--output',required=True);a=ap.parse_args()
 selected={a.track:TRACKS[a.track]}if a.track else TRACKS
 if a.serial or a.track:results={k:f()for k,f in selected.items()}
 else:
  with ProcessPoolExecutor(max_workers=4)as pool:
   jobs={k:pool.submit(f)for k,f in selected.items()};results={k:v.result()for k,v in jobs.items()}
 profile=results.get('pressure',{}).pop('_profile',None)
 if profile is not None:
  with open(a.output+'.profile.json','w',encoding='utf-8')as f:json.dump(profile,f,separators=(',',':'));f.write('\n')
 out={'schema':'collatz-pass3-v1','scope':'bounded exact tests, not mathematical proof checking','tracks':results}
 with open(a.output,'w',encoding='utf-8')as f:json.dump(out,f,sort_keys=True,indent=2);f.write('\n')
 print(json.dumps({'output':a.output,'semantic_sha256':digest(out),'tracks':list(results)},sort_keys=True))
if __name__=='__main__':main()
