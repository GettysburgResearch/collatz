"""Enumerate compensated signed offsets by upper even count, independent of time.

An odd-coordinate layer chooses the numbers of upper/lower even departures
before the next odd. The carry is normalized by (3/2)^r. At a successful
word it is integral and bounded by the two remaining geometric sums.
"""
from collections import deque

def residual(q,delta):
    lower=q-delta
    if lower<1:
        return [],None
    # A state records all layers strictly below its current odd coordinate.
    bound=(1<<q)-1+3**delta*((1<<lower)-1)
    todo=deque()
    back={}
    def emit(prev,A,B,D,a,b):
        z=D+(1<<A)*((1<<a)-1)-3**delta*(1<<B)*((1<<b)-1)
        na,nb=A+a,B+b
        if z&1:
            return None
        nd=3*z//2
        if not -((1<<q)-(1<<na)) <= nd <= 3**delta*((1<<lower)-(1<<nb)): return None
        key=na,nb,nd
        if key not in back:
            back[key]=(prev,a,b)
            todo.append(key)
        return key
    for b in range(1,lower+1):
        emit(None,0,0,0,1,b)
    dest=q,lower,0
    while todo and dest not in back:
        A,B,D=todo.popleft()
        for a in range(q-A+1):
            for b in range(lower-B+1):
                emit((A,B,D),A,B,D,a,b)
    witness=None
    if dest in back:
        k=dest; witness=[]
        while k is not None:
            prev,a,b=back[k];witness.append((a,b));k=prev
        witness.reverse()
    return list(back),witness

if __name__=="__main__":
    for q in range(2,11):
        for d in range(1,q):
            nodes,w=residual(q,d)
            if nodes:
                print(q,d,len(nodes),w,flush=True)
