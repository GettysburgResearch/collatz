"""Small exact checks for intercept coding and finite-place cycle forcing."""
from collections import deque,Counter
from itertools import product
from math import gcd
import json

def require(test,name):
    if not test:raise ValueError(name)

def affine(word):
    A=Q=0
    for i,b in enumerate(word):
        if b:A=3*A+(1<<i);Q+=1
    return len(word),Q,A

def main():
    counts=Counter()
    for length in range(1,11):
        seen=set()
        for word in product((0,1),repeat=length):
            n,q,A=affine(word)
            require(A<=3**n-2**n and (q,A) not in seen,'native intercept injectivity')
            seen.add((q,A))
            source=-A*pow(3**q,-1,1<<n)%(1<<n)
            x=source
            for bit in word:
                require(x%2==bit,'native source word')
                x=(3*x+1)//2 if bit else x//2
            for cut in {0,n//2,n}:
                L,q1,A1=affine(word[:cut]);_,q2,A2=affine(word[cut:])
                require(A==3**q2*A1+(1<<L)*A2,'two-chart concatenation')
                counts['split_native_intercepts']+=1
    for Q in (5,7,11,13,25,35):
        inv=pow(2,-1,Q)
        operators=[(inv,0),((3*inv)%Q,inv)]
        def compose(u,v):return ((u[0]*v[0])%Q,(u[0]*v[1]+u[1])%Q)
        todo=deque([(1,0)]);group=set(todo)
        while todo:
            u=todo.popleft()
            for op in operators:
                z=compose(op,u)
                if z not in group:group.add(z);todo.append(z)
        require((1,pow(4,-1,Q)) in group,'one-quarter translation')
        for target in range(Q):
            f=inv,inv*target%Q
            require(f in group and (f[0]*target+f[1])%Q==target,'forced fixed residue')
            counts['prime_to_six_targets']+=1
        counts['enumerated_group_elements']+=len(group)
    for h in range(1,6):
        modulus=3**h
        for r in range(modulus):
            if r%3==0:continue
            y=r if r%2 else r+modulus
            reverse=[]
            for _ in range(h):
                e=next(e for e in range(1,7) if (2**e*y-1)%3==0 and (2**e*y-1)%9)
                y=(2**e*y-1)//3;reverse.append(e)
            for start in (0,1,2,7):
                u=start
                for e in reversed(reverse):u=(3*u+1)*pow(2**e,-1,modulus)%modulus
                require(u==r,'ternary unit forced regardless of incoming residue')
                counts['ternary_reset_rows']+=1
    return counts

if __name__=='__main__':print(json.dumps(main(),indent=2,sort_keys=True))
