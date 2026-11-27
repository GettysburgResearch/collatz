"""Six labeled states, exact return itineraries, both endpoint conventions."""
from fractions import Fraction
from itertools import product
import json

BITS = [x for x in product((0,1), repeat=4) if x[0]+x[1] == x[2]+x[3]]
CUT = Fraction(49,50)
V = (1000000,1866354,321361)


def insist(condition, detail):
    if not condition:
        raise ArithmeticError(detail)


def phase_vectors(alpha):
    # Endpoints for all threshold and wrap tests through 53 iterations.
    rows = sorted(((t-k*alpha) % 1, t, k, (t-k*alpha)//1)
                  for k in range(54) for t in (0,CUT))
    labels = [(t,k,winding) for _,t,k,winding in rows]
    xs = [x for x,*_ in rows] + [1]
    insist(len(xs)==len(set(xs)), "duplicate circle cut")
    itinerary = set()
    delay = 0
    for x in xs[:-1] + [(a+b)/2 for a,b in zip(xs,xs[1:])]:
        word = []
        for step in range(1,54):
            previous = (x+(step-1)*alpha) % 1
            new = (x+step*alpha) % 1
            word.append(int(new<previous))
            if new > CUT:
                if x>CUT:
                    itinerary.add(tuple(word))
                else:
                    delay = max(step,delay)
                break
        else:
            raise ArithmeticError("no return")
    return labels,itinerary,delay


def six_step(v,letter):
    def compatible(x,y):
        return all(a<=b for a,b in zip(x,y)) if letter else all(a>=b for a,b in zip(x,y))
    return tuple(sum(m for x,m in zip(BITS,v) if compatible(x,y)) for y in BITS)


def aggregate(v):
    return tuple(sum(m for x,m in zip(BITS,v) if x[0]+x[1]==g) for g in range(3))


def run():
    lower, upper = Fraction(584961,10**6), Fraction(584964,10**6)
    catalogs = [phase_vectors(a) for a in (lower,(lower+upper)/2,upper)]
    insist(catalogs[0]==catalogs[1]==catalogs[2], "slope identity")
    labels, words, delay = catalogs[0]
    # The unequal grade-one initial coordinates provide a separate aggregation test.
    initial = [0]*6
    for s,v in zip(((0,0,0,0),(0,1,0,1),(1,1,1,1)),V):
        initial[BITS.index(s)] = v
    images=[]
    for word in sorted(words,key=len):
        full=tuple(initial)
        for e in word:
            full = six_step(full,e)
        img=aggregate(full)
        n=len(word)
        insist(all(v**200>q**200*3**(201*n) and v**5000<q**5000*3**(5031*n)
                   for v,q in zip(img,V)), "one-sided exact vector bound")
        images.append((n,img))
    for pair in ((0,1),(1,0)):
        for state in BITS:
            count=tuple(int(x==state) for x in BITS)
            for e in pair:
                count=six_step(count,e)
            insist(min(aggregate(count))>0,"two-step entrance positivity")
    return {"cut_count":len(labels),"initial_delay":delay,"images":images,
            "directed_mixed_entrance_checks":12}

if __name__ == '__main__':
    print(json.dumps(run(),sort_keys=True,indent=2))
