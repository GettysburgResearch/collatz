"""Finite ordinary certified child graph on odd dyadic residues."""
from collections import deque
from sys import argv

def fusion_time(x, sign, clocks):
    y = 3*x + 2*sign
    a = b = 0
    for h in range(1, clocks+1):
        bx = x & 1
        by = y & 1
        a += bx
        b += by
        x = (3*x+1)//2 if bx else x//2
        y = (3*y+1)//2 if by else y//2
        if x == y and a == b+1:
            return h
    return 0

def graph(h):
    mod = 1 << h
    n = mod//2
    flags = [tuple(fusion_time(2*i+1,s,h) for s in (1,-1)) for i in range(n)]
    exits = [[] for _ in range(n)]
    parents = [[] for _ in range(n)]
    for i, good in enumerate(flags):
        q = 2*i+1
        for e in range(1,h+3):
            if not good[(e+1)%2]:
                continue
            s = 1 if e%2 else -1
            v = ((1 << e)*(3*q+2*s)-1)//3
            j = v%mod//2
            exits[i].append((e,j))
            parents[j].append(i)
    degree = [len(x) for x in exits]
    queue = deque(i for i,d in enumerate(degree) if not d)
    while queue:
        i = queue.popleft()
        for parent in parents[i]:
            degree[parent] -= 1
            if not degree[parent]:
                queue.append(parent)
    living = [i for i,d in enumerate(degree) if d]
    print(h, 'certified_signs',sum(sum(t>0 for t in g) for g in flags),
          'living',len(living), 'multiple_live_branches',sum(degree[i]>1 for i in living))
    return {2*i+1: [(e,2*j+1) for e,j in exits[i] if degree[j]] for i in living}

if __name__ == '__main__':
    for arg in argv[1:]:
        g = graph(int(arg))
        for x, edges in list(g.items())[:8]:
            print(' ',x,edges)
