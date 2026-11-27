"""Check signed-offset compensation through paired native word automata."""
from collections import deque

def reach(q,d):
    p=q-d
    def bound(a,b,D):
        return -(3**q-3**a)<=2*D<=3**d*(3**p-3**b)
    pred={}
    todo=deque()
    def add(prev,a,b,D,e,h):
        if a+e>q or b+h>p: return
        z=D+e*3**a-h*3**(d+b)
        if z&1: return
        D=3*z//2
        a+=e;b+=h
        if not bound(a,b,D): return
        key=(a,b,D)
        if key not in pred:
            pred[key]=(prev,e,h);todo.append(key)
    # Manually force both initial E and the residual upper O immediately after.
    if p<1: return [],None
    D=3*(1-3**d)//2
    if not bound(1,1,D): return [],None
    for lo in (0,1):
        add(None,1,1,D,0,lo)
    dest=(q,p,0)
    while todo and dest not in pred:
        state=todo.popleft()
        for e in (0,1):
            for h in (0,1):
                add(state,*state,e,h)
    pair=None
    if dest in pred:
        a=[];b=[];key=dest
        while key is not None:
            key,e,h=pred[key];a.append('E' if e else 'O');b.append('E' if h else 'O')
        pair='E'+''.join(reversed(a)),'E'+''.join(reversed(b))
    return list(pred),pair

if __name__=='__main__':
    for q in range(2,7):
        for d in range(1,q):
            states,witness=reach(q,d)
            print(q,d,len(states),witness)
