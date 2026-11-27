"""Exact finite negative controls for the global sparse-grade and sparse-valuation transport."""
from collections import Counter
from fractions import Fraction as F
import json

def check(value):
 if not value:raise ValueError("global sparse control failed")

def raw_residue(ms,z,drift):
 dates=[0]
 for i,m in enumerate(ms):dates.append(dates[-1]+m+z[i]-z[i+1])
 mod=2**dates[-1]
 return sum(-drift*2**t*pow(3,-i-1,mod) for i,t in enumerate(dates[:-1]))%mod

def canon_words(ms):
 n=len(ms);a=[0]
 def rec(i):
  if i==n:
   if a[-1]==0:yield tuple(a[:-1])
   return
  for zz in range(a[-1]+ms[i]):
   a.append(zz);yield from rec(i+1);a.pop()
 yield from rec(0)

def run():
 totals=Counter()
 for P in range(5,10):
  for A in range((3*P)//2+1,(5*P)//3+1):
   ms=[((i+1)*A)//P-(i*A)//P for i in range(P)]
   if any(all(ms[(i+j)%P]==2 for j in range(3)) for i in range(P)):continue
   if any(ms[i]==ms[(i+1)%P]==1 for i in range(P)):continue
   for z in canon_words(ms):
    totals['cyclic_grade_words']+=1
    e=[ms[i]+z[i]-z[(i+1)%P] for i in range(P)]
    c=[min(1,x) for x in z];u=c[:]
    # The directed closure repeated to its fixed point is independent of its one-sided description.
    for j in range(P+1):
     for i,m in enumerate(ms):
      t=(i+1)%P
      if m==2:u[i]=min(u[i],u[t])
      else:u[t]=min(u[t],u[i])
    changed={i for i in range(P) if u[i]!=z[i]}
    bad={i for i in range(P) if e[i]>=3 or z[i]>=2}
    check(changed<=bad|{(i-1)%P for i in bad})
    check(all(ms[i]+u[i]-u[(i+1)%P] in (1,2) for i in range(P)))
    totals['changed_slots']+=len(changed)
    if any(c[i]!=u[i] for i in range(P)):totals['would_fail_clip_only']+=1
    # Fixed mark levels restore global trajectories literally, including profiles with height >=3.
    for start in range(P):
     if start in changed:continue
     for b in [3,min(P,6),P+2]:
      if (start+b)%P in changed:continue
      zie=[z[(start+i)%P] for i in range(b+1)];uz=[u[(start+i)%P] for i in range(b+1)];m=[ms[(start+i)%P] for i in range(b)]
      inds=[i for i in range(b+1) if zie[i]!=uz[i]]
      if not inds:continue
      M=[0]
      for x in m:M.append(M[-1]+x)
      K=M[-1]+zie[0]-zie[-1];mod=2**K
      for drift in [1,5]:
       raw=raw_residue(m,zie,drift);rel=raw_residue(m,uz,drift)
       delta=sum(-drift*(2**(M[i]+zie[0]-zie[i])-2**(M[i]+zie[0]-uz[i]))*pow(3,-i-1,mod) for i in inds)%mod
       check(raw==(rel+delta)%mod)
       totals['translated_moduli']+=1
       if raw!=rel:totals['detect_omitted_translation']+=1
      if max(zie)>=3:totals['unbounded_grade_interface']+=1
 eta=F(1,10**6);tau=F(1,2*10**6);c=F(1,10**8);gamma=F(4,3)-F(1,10**4)
 C=(4*eta+gamma*(1-eta)+(5+eta)*21*tau)/(4+eta)
 check(8**15>2000000*3**15 and (3+c)*C<1 and (4+eta)*c<eta/2)
 return dict(counts=dict(totals),source_exponent_upper=str(C),strict_product_deficit=str(1-(3+c)*C),retained_fraction_lower=str(1-6*c-3*c/tau))
if __name__=='__main__':print(json.dumps(run(),indent=2,sort_keys=True))
