"""Direct two-orbit drift alphabet, ternary endpoint and final strict margins."""
from fractions import Fraction as Q
from itertools import product
from math import factorial,gcd
from collections import Counter
import json

def allowed(m,x,y):
    return m+x-y>=1

def run():
    stats=Counter()
    for q in range(5,28):
      for s in range(q//2+1,q):
        if gcd(q,s)>1:continue
        for r in range(q):
          m=[1+int((r+j*s)%q+s>=q) for j in range(7)]
          assert all(not(a==b==1) for a,b in zip(m,m[1:]))
          words={() : {(x,y) for x in (0,1) for y in (0,1)}}
          for step in m:
            nxt={}
            for ds,roots in words.items():
              for x,y in roots:
                key=ds+(x-y,)
                nxt.setdefault(key,set()).update((xx,yy) for xx in (0,1) for yy in (0,1) if allowed(step,x,xx) and allowed(step,y,yy))
            words=nxt
          k=m[:-1].count(1)
          assert len(words)==7**k*3**(len(m)-2*k)
          # Signed digits {-1,0,1} give unique ternary endpoint residue at a fixed word length.
          mod=3**len(m);E=sum(m);res=set()
          for ds in words:
             B=t=0
             for j,h in zip(ds,m):B=3*B+(1<<t)*j;t+=h
             res.add(B*pow(1<<E,-1,mod)%mod)
          assert len(res)==len(words)
          stats['calendars']+=1;stats['direct_signed_drift_strings']+=len(words)
    assert 3**200<2**317 and (Q(9,7)-1)/(Q(9,7)+1)==Q(1,8)
    partial=sum(Q(753,160)**j/factorial(j) for j in range(12))
    assert partial>110 and (1+Q(753,160))/55==Q(83,800)
    return {'exact_controls':dict(stats),'exponential_partial_sum_slack':str(partial-110),'microscopic_terminal_entropy_lower':'83/800 (strict)','audited_source':'b3d7c8e2fb62da60ad0574b78eca9ab102119e796c39d40147f20bf0667cb8ce'}
if __name__=='__main__':print(json.dumps(run(),indent=2,sort_keys=True))
