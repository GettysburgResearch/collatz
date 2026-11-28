"""Independent nontrivial fixture for periodicizing literal downstep changes."""
from collections import deque
import json


def check(value, message):
    if not value:
        raise AssertionError(message)


UP = {1,3,7,11,17,27,31,41,47,71}


def is_up(x):
    return x%256 in UP


def step(x,up):
    return ((3*x if up else x)+(x%2))//2


def contraction(bits,policy):
    m=2**bits
    up=[bool(policy(r)) for r in range(m)]
    edges=[]
    for r in range(m):
        low=step(r,up[r])%m
        edges.append((low,(low+m//2)%m))
    top=[0]*m
    for h in range(1,80):
        top=[int(up[r])+max(top[u],top[v]) for r,(u,v) in enumerate(edges)]
        j=max(top)
        if 3**j<2**h:
            # Additive error <= (3/2)^h - 1, so all x at cutoff or above descend.
            cutoff=(3**h-2**h)//(2**h-3**j)+1
            return h,j,cutoff
    raise AssertionError("no finite certificate found")


def first_descent_or_repeat(x):
    v=x;visited=set()
    while v>=x and v not in visited:
        visited.add(v)
        v=step(v,is_up(v))
    return v<x


def main():
    h,up,cut=contraction(8,is_up)
    exceptional={x for x in range(2,cut+1) if not first_descent_or_repeat(x)}
    check(exceptional=={3,7,27},"all true no-descent starts")
    def patched(x):
        return step(x,is_up(x) and x not in exceptional)
    jset=set()
    queue=deque(exceptional)
    while queue:
        x=queue.popleft()
        if x in jset:
            continue
        jset.add(x)
        queue.append(step(x,is_up(x)))
        if x in exceptional:
            queue.append(step(x,False))
    maximum={x:0 for x in jset}
    for length in range(1,5000):
        maximum={x:max([int(is_up(x))+maximum[step(x,is_up(x))]]+
                       ([maximum[step(x,False)]] if x in exceptional else []))
                 for x in jset}
        top=max(maximum[x] for x in exceptional)
        if 2*3**(h+top)<2**(h+length):
            break
    else:
        raise AssertionError("optional physical graph has no gain certificate")
    ell=length+max(8,max(jset).bit_length()+2)
    missed=matched=0
    for e in sorted(exceptional):
        for lift_index in (1,2,3,4,5,15,31):
            small=e
            large=e+(lift_index<<ell)
            for i in range(length):
                mod=1<<(ell-i)
                check((large-small)%mod==0,"remaining shadow precision")
                switch=large%(1<<ell) in exceptional and is_up(large)
                check(not switch or small in exceptional,"no spurious switches")
                if small in exceptional and not switch:
                    missed+=1
                choice=is_up(large) and not switch
                check(choice==is_up(small) or small in exceptional,"optional physical graph")
                small=step(small,choice)
                large=step(large,choice)
                check(small in jset,"bounded companion")
                matched+=1
    check(missed>0,"later periodic switches actually missed")
    periodic=[]
    for bits in range(8,13):
        m=2**bits
        f=lambda x:is_up(x) and x%m not in exceptional
        hh,jj,bb=contraction(bits,f)
        for start in range(1,bb+1):
            seen=set()
            x=start
            while x!=1:
                check(x not in seen,"finite check reaches (1,2)")
                seen.add(x)
                x=step(x,f(x))
        periodic.append([bits,hh,jj,bb])
    print(json.dumps({"base_horizon_maximum_ups_cutoff":[h,up,cut],"no_descent_starts":sorted(exceptional),
                      "optional_graph_size":len(jset),"uniform_optional_shadow_length":length,
                      "large_modulus_bits":ell,"checked_shadow_dates":matched,
                      "missed_intended_switches":missed,"exact_periodic_convergence_rows":periodic},
                     sort_keys=True))


if __name__=="__main__":
    main()
