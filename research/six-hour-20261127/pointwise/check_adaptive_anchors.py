"""Exact checks of the signed-edge identity and bounded-cost path compilation."""
import itertools
import json
from fractions import Fraction
from math import gcd


def require(condition, description):
    if not condition:
        raise ArithmeticError(description)


def projected_ancestry(n, length):
    values = [n]
    exponents = []
    for _ in range(length):
        v = 3*n+1
        d = (v & -v).bit_length()-1
        n = v >> d
        values.append(n)
        exponents.append(d)
    return values, exponents


def v3(n):
    require(n != 0, "valuation of zero")
    answer = 0
    while n % 3 == 0:
        n //= 3
        answer += 1
    return answer


def check_edges():
    anchors = sorted({Fraction(p, q) for p in range(1, 8) for q in range(1, 8)
                      if q % 3 and gcd(p, q) == 1})
    edges = 0
    defects = 0
    exact = 0
    for n in (*range(1, 400, 2), *(2**k-1 for k in range(3, 16))):
        values, exponents = projected_ancestry(n, 37)
        def chosen(x):
            rank, phase = max((v3(t.denominator*x+t.numerator),t) for t in anchors)
            return rank, phase
        choices = [chosen(x) for x in values]
        for i, e in enumerate(exponents):
            x, y = values[i:i+2]
            r, anchor = choices[i]
            s, following = choices[i+1]
            p,q = anchor.as_integer_ratio()
            u,v = following.as_integer_ratio()
            D = (1 << e)*q*u-v*(3*p-q)
            require(D == (1 << e)*q*(v*y+u)-3*v*(q*x+p), ("edge", n, i))
            if D:
                require(v3(D) >= min(r+1,s), ("rank", n, i))
                defects += 1
            else:
                exact += 1
            edges += 1
    # Even terminal denominators may be essential. The ordinary orbit here is 1.
    t = Fraction(3)
    count = 3
    for _ in range(count):
        t = (3*t-1)/4
    require(t == Fraction(11,16), "even denominator endpoint")
    require(2**count > 1+3 and 2**(2*count) <= t.denominator*(1+3), "terminal factor")
    return {"ordinary_edges": edges, "matching_edges": exact, "discrepant_edges": defects,
            "height_seven_rational_anchors": len(anchors),
            "even_denominator_example": [3, 1, t.numerator, t.denominator]}


def graph_data(successors):
    size = len(successors)
    cycle = set()
    for first in range(size):
        path = []
        n = first
        while n != -1 and n not in path:
            path.append(n)
            n = successors[n]
        if n != -1:
            cycle.update(path[path.index(n):])
    sinks = {i for i, out in enumerate(successors) if out == -1}
    boundary = cycle | sinks
    distance = {}
    for first in range(size):
        n = first
        d = 0
        while n not in boundary:
            d += 1
            n = successors[n]
        if d:
            distance[first] = d
    return cycle, boundary, distance


def compile_paths(successors, radix):
    size = len(successors)
    cycle, boundary, dist = graph_data(successors)
    levels = [set(dist)]
    modulus = 1
    residue = 0
    words = []
    total_edges = len(cycle)
    while modulus <= size:
        candidates = [residue+i*modulus for i in range(radix)]
        modulus *= radix
        groups = [{v for v in levels[-1] if dist[v] % modulus == c}
                  for c in candidates]
        chosen = min(range(radix), key=lambda i: (len(groups[i]), i))
        residue = candidates[chosen]
        nxt = groups[chosen]
        rows = {}
        for v in levels[-1]:
            path = []
            y = v
            while y not in nxt and y not in boundary:
                path.append(y)
                y = successors[y]
            require(len(path) <= modulus, ("landmark distance", successors, v))
            rows[v] = tuple(path)
            total_edges += len(path)
        words.append(rows)
        levels.append(nxt)
    require(not levels[-1], "last layer")
    require(total_edges <= (len(words)*radix+1)*size, "storage cost")
    return cycle, boundary, words, total_edges


def test_graph(successors, radix):
    cycle, boundary, words, total = compile_paths(successors, radix)
    size = len(successors)
    checked = 0
    maxpieces = 0
    for first in range(size):
        n = first
        direct = []
        for _ in range(2*size+1):
            if successors[n] == -1:
                break
            direct.append(n)
            n = successors[n]
        for cut in range(len(direct)+1):
            emitted = []
            n = first
            pieces = 0
            for layer in words:
                if len(emitted) == cut or n in boundary:
                    break
                segment = layer[n]
                take = min(len(segment), cut-len(emitted))
                if take:
                    pieces += 1
                    emitted.extend(segment[:take])
                    n = successors[segment[take-1]]
            if len(emitted) < cut:
                require(n in cycle, "uncovered transient")
                pieces += 1
                while len(emitted) < cut:
                    emitted.append(n)
                    n = successors[n]
            require(emitted == direct[:cut], ("wrong path", first, cut, successors))
            require(pieces <= len(words)+1, "piece count")
            maxpieces = max(maxpieces,pieces)
            checked += 1
    return checked, maxpieces, total


def main():
    count = 0
    cuts = 0
    maxpieces = 0
    maxstored = 0
    for size in range(1,6):
        for successors in itertools.product(range(-1,size), repeat=size):
            ncut, pieces, storage = test_graph(successors, 2)
            count += 1
            cuts += ncut
            maxpieces = max(maxpieces,pieces)
            maxstored = max(maxstored,storage)
    # Include longer directed chains, many sources converging on one tail, and cycles.
    for n in (31,63,127):
        for graph in (tuple([*range(1,n),-1]), tuple([*range(1,n),0]),
                      tuple(min(n-1,i+1) if i<n//2 else i%(n//2) for i in range(n))):
            for radix in (2,3,5):
                ncut,pieces,storage = test_graph(graph,radix)
                cuts += ncut
                count += 1
                maxpieces = max(maxpieces,pieces)
                maxstored = max(maxstored,storage)
    print(json.dumps({"edges":check_edges(), "functional_graphs":count,
          "decoded_paths_with_terminal_cuts":cuts, "maximum_used_pieces":maxpieces,
          "maximum_stored_edges":maxstored}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
