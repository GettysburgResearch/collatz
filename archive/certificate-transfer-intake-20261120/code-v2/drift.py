import random, math, sys
sys.path.insert(0,'.')
from chain import step, P3
random.seed(7)
LOGA={0:math.log(0.5),1:math.log(1.5)}
def excursion(z, cap=200000):
    """from departure state (0,z), z odd: run to next departure (a=0,e odd) or absorption.
       also checks the one-step inequality |f'| <= alpha|f|+beta along the way."""
    a,e=0,z; n=0; viol=0
    while True:
        bit=random.getrandbits(1)
        f=abs(e)/P3[abs(a)]
        a2,e2=step(a,e,bit)
        f2=abs(e2)/P3[abs(a2)]
        alpha,beta=(0.5,1/6) if bit==0 else (1.5,0.5)
        if a!=0 or e%2: # steps inside the excursion (a=0 idle steps have beta=0)
            if f2>alpha*f+beta+1e-9*max(1,f): viol+=1
        a,e=a2,e2; n+=1
        if a==0 and e==0: return ('abs',n,0,viol)
        if a==0 and e%2: return ('dep',n,e,viol)
        if n>=cap: return ('cap',n,e,viol)
for mag in [1,10**3,10**6,10**12,10**30]:
    res=[]; viol=0; absb=0; cap=0
    N=4000
    for _ in range(N):
        z=random.randrange(mag,10*mag+2)|1
        if random.getrandbits(1): z=-z
        kind,n,e,v=excursion(z); viol+=v
        if kind=='abs': absb+=1
        elif kind=='cap': cap+=1
        else: res.append(math.log(abs(e))-math.log(abs(z)))
    res.sort()
    print(f"|z|~{mag:.0e}: mean dlog|Z| = {sum(res)/len(res):8.2f}  median {res[len(res)//2]:7.2f}  max {res[-1]:6.2f}  absorbed {absb/N:.3f}  capped {cap/N:.3f}  ineq-violations {viol}")
