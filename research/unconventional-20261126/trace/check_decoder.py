"""Exact congruence decoder certificate for every bounded-C=2 ordinary word."""
import hashlib
import json
from collections import defaultdict
from itertools import product


def require(value, message):
    if not value:
        raise RuntimeError(message)


def admissible(word):
    for i in range(len(word)):
        amount=0
        ternary=1
        for e in word[i:]:
            amount+=e
            ternary*=3
            if 2**amount>4*ternary:
                return False
    return True


def cylinder(word):
    modulus=3**len(word)
    r=0
    for e in reversed(word):
        r=((3*r+1)*pow(2,-e,modulus))%modulus
    return r


def digest(values):
    return hashlib.sha256(bytes(values)).hexdigest()


def main():
    h=10
    words=[w for w in product((1,2,3),repeat=h) if admissible(w)]
    residues={w:cylinder(w) for w in words}
    allowed=defaultdict(set)
    for w,b in residues.items():
        allowed[b].add(w[0])
    guess=[min(allowed[b]) if b in allowed else 1 for b in range(3**h)]
    for b in (34445,52589):
        require(allowed[b]=={1,3},'unexpected special residue')
        guess[b]=3
    verts=sorted({w[:-1] for w in words} | {w[1:] for w in words})
    pos={v:i for i,v in enumerate(verts)}
    edges=[(pos[w[:-1]],pos[w[1:]],9*int(guess[residues[w]]!=w[0])-1) for w in words]

    # Finite relaxation finds an integer potential. The certificate is the
    # final exact inequality on every edge, not a convergence assumption.
    d=[0]*len(verts)
    for _ in range(len(verts)):
        changed=False
        for u,v,c in edges:
            if d[u]+c>d[v]:
                d[v]=d[u]+c
                changed=True
        if not changed:
            break
    require(all(d[v]>=d[u]+c for u,v,c in edges),'positive defect cycle')
    require(min(d)==0 and max(d)==10,'potential range')
    for w,b in residues.items():
        # Each target class has an ordinary positive odd representative.
        a=b if b%2 else b+3**h
        target=a
        for e in w:
            numerator=(a<<e)-1
            require(numerator%3==0,'nonordinary residue')
            a=numerator//3
            require(a>0 and a%2==1,'bad inverse state')
        for e in reversed(w):
            v=3*a+1
            require((v & -v).bit_length()-1==e,'wrong ordinary exact exponent')
            a=v>>e
        require(a==target,'bad ordinary replay')
    print(json.dumps({'window':h,'modulus':3**h,'ordinary_words':len(words),
        'graph_vertices':len(verts),'attained_residues':len(allowed),
        'ambiguous_residues':sum(len(es)>1 for es in allowed.values()),
        'override_with_three':[34445,52589],
        'decoder_byte_sha256':digest(guess),'potential_byte_sha256':digest(d),
        'minimum_potential':min(d),'maximum_potential':max(d),
        'all_length_bound':'9 * mistakes <= n + 82'},indent=2))


if __name__=='__main__':
    main()
