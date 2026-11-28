"""Exact controls for protected prefix removals, including altered residue edges."""
import json
from math import comb


def check(value, message):
    if not value:
        raise AssertionError(message)


def original_step(x):
    return (3*x+1)//2 if x%2 else x//2


def classify(r,k):
    x,ones,word,first=r,0,0,0
    for j in range(1,k+1):
        bit=x%2
        word |= bit << (j-1)
        ones+=bit
        x=original_step(x)
        if not first and 3**ones < 2**j:
            first=j
    return first,word


def edges(r,k,up):
    mod=2**k
    low=((3*r if up else r)+(r%2))//2 % mod
    return low,(low+mod//2)%mod


def residue_models(k):
    mod=2**k
    labels=[classify(r,k) for r in range(mod)]
    words={w:r for r,(_,w) in enumerate(labels)}
    check(len(words)==mod,"parity-residue bijection")
    policy=[bool(r%2 and t) for r,(t,_) in enumerate(labels)]
    removed=sum(not t for t,_ in labels)
    graph=[edges(r,k,policy[r]) for r in range(mod)]
    ms=[0]*mod
    for j in range(1,k+1):
        ms=[int(policy[r])+max(ms[u],ms[v]) for r,(u,v) in enumerate(graph)]
        for r,(t,_) in enumerate(labels):
            if (t or 1) == j:
                check(3**ms[r] < 2**j,"all modified continuations contract by designated time")
    critical=min(j for j in range(k+1) if 3**j>mod)
    unused={w for w in words if w.bit_count()==critical}
    necklaces=0
    while unused:
        w0=w=next(iter(unused))
        while w in unused:
            unused.remove(w)
            v=(w >> 1) | ((w & 1) << (k-1))
            check(words[v] in edges(words[w],k,(w&1)==1),"original cyclic-window edge")
            w=v
        check(w==w0,"expanding necklaces disjoint")
        necklaces+=1
    check(necklaces<=removed and k*necklaces>=comb(k,critical),"disjoint lower and removal upper")
    return removed,necklaces


def series(depth):
    survivor=[1]
    endpoint=[0]
    last=[1]
    for k in range(1,depth+1):
        nxt=[0]*(k+1)
        for j,v in enumerate(last):
            for r in (j,j+1):
                if 3**r>2**k:
                    nxt[r]+=v
        survivor.append(sum(nxt))
        endpoint.append(sum(comb(k,j) for j in range(k+1) if 3**j>2**k))
        check(k*survivor[k]==sum(endpoint[j]*survivor[k-j] for j in range(1,k+1)),
              "Sparre Andersen coefficient identity in integers")
        last=nxt
    return survivor


def actual_bad(x):
    if x==1:
        return False
    y=x
    for _ in range(x.bit_length()-1):
        y=original_step(y)
        if y<x:
            return False
    return True


def adaptive_controls(bound):
    changed=protected=0
    for x in range(2,bound+1):
        if actual_bad(x):
            check(x%2==1 and (x+1)//2<x,"immediate modified descent")
            changed+=1
        else:
            y=x
            for _ in range(x.bit_length()-1):
                check(not actual_bad(y),"every intermediate protected")
                protected+=1
                y=original_step(y)
                if y<x:
                    break
            check(y<x,"ordinary descent retained")
    return changed,protected


def negative_control():
    k,mod=15,2**15
    a0,d=-130562173,5960299
    a=a0
    ups=changes=0
    seen=set()
    for _ in range(23):
        check(a not in seen,"primitive Wren negative cycle")
        seen.add(a)
        r=a*pow(d,-1,mod)%mod
        first,w=classify(r,k)
        raw_up=bool(r%2 and 3**w.bit_count()<mod)
        safe_up=bool(r%2 and first)
        changes+=(raw_up!=safe_up)
        ups+=raw_up
        a=((3*a if raw_up else a)+(a%2)*d)//2
    check(a==a0 and ups==15 and 3**ups>2**23 and changes,
          "terminal-count counterexample and protected rule difference")
    return changes


def main():
    surv=series(128)
    totals=[]
    for k in range(1,15):
        r,c=residue_models(k)
        check(r==surv[k],"physical residue enumeration versus ballot count")
        totals.append([k,r,c])
    bad,protected=adaptive_controls(12000)
    print(json.dumps({"residue_levels":totals,"strict_ballot_coefficients":128,
                      "adaptive_inputs":11999,"adaptive_switches":bad,
                      "protected_true_steps":protected,
                      "changed_choices_on_wren_negative_cycle":negative_control()},sort_keys=True))


if __name__=="__main__":
    main()
