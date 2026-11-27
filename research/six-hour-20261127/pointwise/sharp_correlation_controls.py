"""Integer controls for conditional uniform transpositions and the tensor rank bound."""
from collections import Counter
from itertools import combinations,product
from math import comb
import json

def need(test, field):
    if not test:
        raise ValueError(field)

def coupling():
    rows=Counter()
    for length in range(2,11):
        for ones in range(1,length):
            # The length denotes the unrevealed coordinates of one reference block.
            left=[]
            right=[]
            for selected in combinations(range(length),ones):
                word=tuple(int(j in selected) for j in range(length))
                (left if word[0]==0 else right).append(word)
            counts=Counter()
            for word in left:
                for other in range(1,length):
                    if word[other]==0:
                        continue
                    swapped=list(word)
                    swapped[0],swapped[other]=swapped[other],swapped[0]
                    counts[tuple(swapped)]+=1
                    rows['conditional_uniform_edges']+=1
                    # A prefix-padding suffix realizes an arbitrary offset position.
                    full=(0,1)+word+(1,0)
                    changed=(0,1)+tuple(swapped)+(1,0)
                    for r in (1,2,3):
                        offsets=tuple(2*i for i in range(r))
                        nstart=len(full)-offsets[-1]
                        before=Counter(tuple(full[i+h] for h in offsets) for i in range(nstart))
                        after=Counter(tuple(changed[i+h] for h in offsets) for i in range(nstart))
                        need(all(abs(before[u]-after[u])<=2*r for u in before.keys()|after.keys()),'swap count range')
                        rows['bounded_range_pattern_tables']+=1
            need(set(counts)==set(right) and set(counts.values())=={length-ones},'second conditional distribution uniform')
            need(len(left)*ones==len(right)*(length-ones),'regular degrees normalize')
            rows['conditional_hypergeometric_rows']+=1
    return rows

def gram():
    rows=Counter()
    for d in range(4,11):
        k=d//2
        windows=tuple(combinations(range(d),k))
        N=len(windows)
        # v=(d*b-k)_j. All v have the same squared norm dk(d-k).
        norm=d*k*(d-k)
        dots=Counter()
        A=set(windows[0])
        for w in windows:
            dots[d*d*len(A.intersection(w))-d*k*k]+=N
        need(sum(dots.values())==N*N and dots[norm]>=N,'exact Gram multiplicities')
        for degree in range(1,7):
            R=comb(d+degree-1,degree)
            need(R*sum(ways*value**(2*degree) for value,ways in dots.items())
                 >=N*N*norm**(2*degree),'trace/Frobenius tensor power')
            rows['exact_tensor_gram_rows']+=1
    return rows

if __name__=='__main__':
    print(json.dumps(dict(transposition=dict(coupling()),symmetric_power=dict(gram())),indent=2,sort_keys=True))
