"""Exact ternary union of all first crossings, for finite grade K.

Rows cover all binary scales 2^delta and all eligible odd signed origins.
Only the tabulated finite K values are counted. The written estimate
holds at every K without using this computation.
"""

def require(condition, message):
    if not condition:
        raise ValueError(message)

def signed_origins(max_even):
    by_even=[[] for _ in range(max_even+1)]
    for m in range(1,(1<<max_even)+1,2):
        x=m
        odds=evens=0
        while x!=1 and evens<=max_even and odds<=3*max_even+2:
            if x&1:
                x=(3*x-1)//2
                odds+=1
            else:
                x//=2
                evens+=1
        if x==1 and evens<=max_even:
            by_even[evens].append(m)
    return by_even

def counts(K):
    power3=[3**b for b in range(K+1)]
    N=power3[-1]
    max_a=(N//(1<<K)).bit_length()-1
    origins=signed_origins(max_a)
    seen=[set() for _ in range(K+1)]
    nodes=0
    for a in range(max_a+1):
        magnitudes=[m for row in origins[:a+1] for m in row]
        stack=[(0,0,0)]
        while stack:
            d,b,C=stack.pop()
            nodes+=1
            if 1<<(a+d)<power3[b]:
                modulus=power3[b]
                inverse=pow(1<<(a+d),-1,modulus)
                for M in magnitudes:
                    n=((C+(M<<d))*inverse-1)%modulus
                    seen[b].add(n)
                continue
            if b==K or 1<<(a+d+K-b)>=N:
                continue
            stack.append((d+1,b,2*C))
            stack.append((d+1,b+1,2*C+power3[b]))
    blocked=bytearray(N)
    for b,rows in enumerate(seen):
        modulus=power3[b]
        fill=bytes([1])*(N//modulus)
        for r in rows:
            if not blocked[r]:
                blocked[r::modulus]=fill
    hard=[sum(1 for x in range(r,N,3) if not blocked[x]) for r in range(3)]
    return K,N,nodes,hard

if __name__=='__main__':
    print('K, denominator, reverse-tree nodes, hard residue counts within n mod 3 = 0,1,2')
    for k in (1,2,3,4,5,6,7,8,9,10,11,12,13,14):
        k,n,visited,hard=counts(k)
        require(hard[0]*20>=3*n, f'K={k} failed the zero-class lower bound')
        require(sum(hard)*960>=259*n, f'K={k} failed the common-set lower bound')
        print(k,n,visited,*hard,flush=True)
