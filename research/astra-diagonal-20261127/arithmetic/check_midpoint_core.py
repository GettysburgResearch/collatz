"""Central-state elimination for both signed midpoint cones, including both seams."""

from functools import cache
from itertools import product
import json

from audit_three_grade_curvature import DANGER, NEGATIVE_DANGER, delta, rows
from check_three_grade_curvature import high_return

WORDS = (("S",)*3, ("D",)*3, ("DS","DS","SD"), ("DS","SD","SD"))
BLOCKS = ((0,1,1), (0,1,1,1), (0,1,1,2,1,1), (0,1,1,3,1,1))
CORE = {(0,1,1), (0,2,2)}
CENTRAL = (DANGER | {(-h,x,y) for h,x,y in NEGATIVE_DANGER} |
           {(0,x,y) for x,y in product((1,2,3),repeat=2) if (2*y-x)%4})


@cache
def transitions(start, spec):
    h,x,y = start
    words = WORDS[spec]
    d = (4,8,32,32)[spec]
    n = (3,9,27,27)[spec]
    sources = (x,y,(2*y-x+h)%4)
    candidates = [tuple(r for r in rows(w) if r[0]==v) for w,v in zip(words,sources)]
    outputs = set()
    for rs in product(*candidates):
        dst = tuple(v[1] for v in rs)
        carries = tuple(v[2] for v in rs)
        v = n*h+delta(carries)
        if (v-d*delta(dst))%(4*d)==0:
            outputs.add(((v//d,dst[0],dst[1]), len(set(carries))>1))
    return outputs


@cache
def physical_transitions(start, spec):
    """Forward check from every true integer residue with its unshifted curvature."""
    h,first,middle = start
    words = WORDS[spec]
    d,n = (4,8,32,32)[spec],(3,9,27,27)[spec]
    out = set()
    for sx,sy in product(range(0,4*d,4),repeat=2):
        x,y = 4096+first+sx,4096+middle+sy
        inputs = (x,y,2*y-x+h)
        ends = []
        carries = []
        for initial,word in zip(inputs,words):
            current = initial
            for letter in word:
                current = high_return(current,letter)
                if current is None:
                    break
            if current is None:
                break
            ends.append(current)
            carries.append(d*current-n*initial)
        if len(ends)==3:
            out.add(((delta(ends),ends[0]%4,ends[1]%4),len(set(carries))>1))
    return out


def block_edges(specs, transition=transitions):
    edges = set()
    for s in CENTRAL:
        current = {(s,False)}
        for word in specs:
            current = {(v,f or g) for t,f in current for v,g in transition(t,word)}
        edges.update((s,t,changed) for t,changed in current if t in CENTRAL)
    return edges


def main():
    all_edges = [block_edges(b) for b in BLOCKS]
    actual_edges = [block_edges(b,physical_transitions) for b in BLOCKS]
    assert actual_edges == all_edges
    for edges in all_edges:
        assert all(s in CORE and not changed for s,t,changed in edges if t in CORE)
    outside = CENTRAL-CORE
    stages = [len(outside)]
    regular = all_edges[0] | all_edges[1]
    while outside:
        nxt = {s for s,t,_ in regular if s not in CORE and t in outside}
        assert nxt < outside
        outside = nxt
        stages.append(len(outside))
    print(json.dumps(dict(
        independent_physical_edges_agree=True,
        central_states=sorted(CENTRAL), core=sorted(CORE),
        outside_ordinary_backward_pruning=stages,
        central_block_counts=[len(rows) for rows in all_edges],
        incoming_core_edges=[sorted((s,t,flag) for s,t,flag in es if t in CORE)
                             for es in all_edges]
    ),indent=2))


if __name__=="__main__":
    main()
