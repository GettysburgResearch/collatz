"""Independent exact replay. Input is the frozen written certificate, not its control program."""
from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import re
import sys

def must(value, msg):
    if not value:
        raise ValueError(msg)

source = Path(sys.argv[1]).read_bytes()
must(sha256(source).hexdigest() == '1d036bb16dd0623a95d09124d8e88ec06d071a8981ba5d126ff92eaa175fed60', 'audit target changed')
s = source.decode()
trap = set(map(int, re.search(r'E = \{([^}]+)\}', s).group(1).replace('\n','').split(',')))
rows = re.findall(r'^\| n \|(.+)\|\n\|---[^\n]+\n\| e \|(.+)\|',s,re.M)
overrides = {}
for nrow, powerrow in rows:
    ns = [int(n.strip()) for n in nrow.split('|')]
    es = [int(n.strip()) for n in powerrow.split('|')]
    must(len(ns)==len(es),'malformed certificate')
    overrides.update(zip(ns,es))
phases={}
x=17
odd=0
c=0
while c==0 or x!=17:
    if x&1:
        phases[x]=(odd,c)
        odd+=1
        x=(3*x-1)//2
    else:
        x//=2
    c+=1
must((odd,c)==(7,11),'period')
mapminus=lambda n: (n//2 if not n&1 else n+(n-1)//2)
P=lambda n: (9*n)**7 if n not in overrides else 170**7*2**overrides[n]
must(max(overrides)==244 and len(overrides)==22,'support')
must(not (set(phases)&trap),'terminal intersection')
must(all(mapminus(u) in trap for u in trap),'trap not closed')
must(set(range(1,21,2))-{17} <= trap,'incomplete exclusion')
for n in range(245):
    must(P(n)>=(9*n)**7,(n,'floor'))
    if n not in trap:
        must(P(n) * (2048 if n%2 else 1) <= P(mapminus(n))*128,(n,'edge'))
for t,(a,h) in phases.items():
    must(128**h*P(t)==2048**a*170**7,(t,'not calibrated'))
must(110**7 >= 2048*37**7 and 297**7 < 2048*100**7 and 2048<3**7 and 54*99**6 > 50*100**6,'tail or constants')

def test(R,z,t,a,h):
    k=(R-a)//7
    p,H=7*k+a,11*k+h
    target=2*3**R*z-t
    bound=2**(H+1)*3**(R-p)*z-17
    hits=[]
    states={target:1}
    for q in range(R+1):
        for u,mult in states.items():
            if u<=bound:
                hits.append((u,q,mult))
        if q==R:
            break
        left=R-q-1
        # Every source at most bound can reach its (at most left)-edge
        # suffix root v only if v+1 <= (3/2)**left*(bound+1).
        # For an odd step with exponent e, 2*(U(u)+1)<=3*(u+1).
        cap=(bound+1)*3**left//2**left-1
        frontier=Counter()
        for u,mult in states.items():
            if not u%3:
                continue
            b=2*u
            while b<=3*cap+1:
                if b%3==1:
                    v=(b-1)//3
                    must(v%2==1 and v>0,('not an odd positive ancestor',u,v))
                    frontier[v]+=mult
                b*=2
        states=frontier
    must(hits==[(bound,p,1)],(R,z,t,hits, bound,p))

if __name__=='__main__':
    trials=0
    for R in range(7,30):
        for z in (1,2,11,29):
            for t,(a,h) in phases.items():
                test(R,z,t,a,h)
                trials+=1
    print(json.dumps({'claims':'all unsigned-integer comparisons passed', 'phases_in_order':list(phases),'first_principal_equality':17,'R_range':[7,29], 'cofactors':[1,2,11,29],'unique_winner_bfs_checks':trials, 'finite_edge_checks':245-len(trap)}))
