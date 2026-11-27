"""Independent finite arithmetic controls for the corrected moving-shadow source."""
from collections import Counter
from fractions import Fraction
from functools import reduce
from itertools import combinations, product
from math import floor, gcd, lcm, prod
import json


def demand(ok):
    if not ok:
        raise ArithmeticError("failed independent control")


def valuation(n, p):
    demand(n != 0)
    n = abs(n)
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def physical(x):
    e = valuation(3*x+1, 2)
    return e, (3*x+1) >> e


def states(x, length):
    result = [x]
    gaps = []
    for _ in range(length):
        e, x = physical(x)
        result.append(x)
        gaps.append(e)
    return result, gaps


def cuts(length):
    for mask in range(1 << (length-1)):
        bounds = [0] + [j for j in range(1, length) if mask & (1 << (j-1))] + [length]
        yield list(zip(bounds, bounds[1:]))


def prunings(entries):
    """Keep every reachable irreducible vector for this short packet."""
    pending = {tuple(range(len(entries)))}
    answers = set()
    while pending:
        ids = pending.pop()
        zeros = [set(chunk) for k in range(2, len(ids)+1)
                 for chunk in combinations(ids, k) if sum(entries[i][0] for i in chunk) == 0]
        if zeros:
            pending.update(tuple(i for i in ids if i not in chunk) for chunk in zeros)
        else:
            answers.add(ids)
    return answers


def check_packets():
    labels = [None, Fraction(-1, 2), Fraction(5, 7), Fraction(1)]
    counts = Counter()
    for n in range(1, 202, 2):
        _, gaps = states(n, 4)
        # Adding this full binary modulus preserves all four accelerations.
        large_n = n + (1 << (sum(gaps)+1)) * 200_000_000
        xs, test_gaps = states(large_n, 4)
        demand(test_gaps == gaps)
        ep = [sum(gaps[:i]) for i in range(5)]
        for segments in cuts(4):
            choices = [labels if end == start+1 else labels[1:] for start, end in segments]
            for given in product(*choices):
                H = 1
                boundary_denominators = []
                backwards = []
                for (i, j), t in reversed(list(zip(segments, given))):
                    if t is None:
                        # Direct reverse one-edge substitution, before its earlier multipliers.
                        backwards.append((Fraction(-1), ep[j], 4-j))
                        backwards.append((Fraction(2), ep[i], 4-j))
                        continue
                    path = [t]
                    for e in gaps[i:j]:
                        path.append((3*path[-1]-1)/(1 << e))
                    H = max(H, *(max(abs(q.numerator), q.denominator) for q in path))
                    boundary_denominators.extend((t.denominator, path[-1].denominator))
                    backwards.append((path[-1]-1, ep[j], 4-j))
                    backwards.append((1-t, ep[i], 4-i))
                C = lcm(*boundary_denominators)
                m = len(segments)
                demand(C % 3 and C <= H**(2*m) and min(xs)>4*m*(H+1))
                entries = []
                for c, a, b in reversed(backwards):
                    if c:
                        ci = C*c
                        demand(ci.denominator == 1)
                        entries.append((int(ci)*(1 << a)*3**b, int(ci), a, b))
                root, total = C * (1 << ep[4]) * (xs[4]+1), C*3**4*(xs[0]+1)
                demand(root + sum(r[0] for r in entries)==total)
                demand(all(r[2]<=s[2] and r[3]>=s[3] for r,s in zip(entries,entries[1:])))
                demand(2 * sum(abs(r[0]) for r in entries) < root)
                counts["packets"] += 1
                counts["all_singleton_packets"] += all(t is None for t in given)
                counts["even_clearings"] += C%2 == 0
                counts["corrected_singleton_after_shadow"] += any(given[j] is None and given[j-1] is not None
                                                              for j in range(1,len(given)))
                outcomes = prunings(entries)
                counts["packets_with_multiple_irreducible_outcomes"] += len(outcomes)>1
                M = 2*(H+1)**(2*m+1)
                for ids in outcomes:
                    if not ids:
                        demand(all(e==1 for e in gaps))
                        continue
                    z = [root]+[entries[i][0] for i in ids]
                    g = reduce(gcd,z)
                    aa = [q//g for q in z]
                    prime_height = max(map(abs,aa))
                    demand(prime_height==root//g)
                    demand(prime_height*M*(xs[0]+1)>=1<<ep[4])
                    q = Fraction(prod(map(abs,aa)),
                                 2**sum(valuation(s,2) for s in aa) *
                                 3**(valuation(sum(aa),3)+sum(valuation(s,3) for s in aa[1:])))
                    demand(q*3**4 <= C*(xs[-1]+1)*M**(2*m))
                    counts["nondegenerate_primitive_outcomes"] += 1
    # Frozen unrepaired text uses one additional 3 on the incoming singleton.
    e, last = physical(17)
    root = (1 << e)*(last+1)
    demand((e,last,root) == (2,13,56))
    demand(root-4+2 == 3*(17+1) == 54 and root-4+6 == 58)
    return dict(sorted(counts.items()))


def check_mesh():
    # In units of one mesh cell. Coefficient logs split into two prime parts
    # and the rest; all three add to at most one. No roundoff is used.
    counts = Counter()
    K = 40_000
    values = [Fraction(0), Fraction(1,3), Fraction(99,100), Fraction(K,3), Fraction(K,2),
              Fraction(K)-Fraction(1,1000), Fraction(K)]
    for a,b in product(values,repeat=2):
        for i in range(5):
            for j in range(5-i):
                for k in range(5-i-j):
                    e2,e3,er = Fraction(i,4),Fraction(j,4),Fraction(k,4)
                    if a+b+e2+e3+er>K:
                        continue
                    actual = [-a-e2,-b-e3,a+b+e2+e3+er-K]
                    rounded = [-floor(a),-floor(b),min(0,floor(a)+floor(b)+3-K)]
                    demand(all(y>=x and y<=0 for x,y in zip(actual,rounded)))
                    demand(sum(rounded)-sum(actual)<8)
                    counts["single_coordinate_mesh_samples"] += 1
    return dict(counts)


if __name__ == "__main__":
    print(json.dumps({"packets":check_packets(),"mesh":check_mesh()},indent=2,sort_keys=True))
