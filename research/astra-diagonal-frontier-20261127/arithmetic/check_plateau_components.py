"""Component lifetimes and finite signed-clock bounds on literal odd grids."""
from fractions import Fraction
from math import prod
import json


def require(ok, msg):
    if not ok:
        raise ArithmeticError(msg)


def raw(n, cutoff):
    if 3*n <= cutoff:
        return 3*n
    z = 3*n+1
    return z if z//(z&-z) <= cutoff else z+2


def next_edge(x, n):
    z = raw(x, n)
    twos = z & -z
    return z//twos, twos.bit_length()-1


def graph(n):
    seen = set()
    out = {}
    for x0 in range(1, n+1, 2):
        trail = []
        ind = {}
        x = x0
        while x not in seen and x not in ind:
            ind[x] = len(trail)
            trail.append(x)
            x, _ = next_edge(x, n)
        if x in ind:
            cyc = trail[ind[x]:]
            j = cyc.index(min(cyc))
            cyc = cyc[j:]+cyc[:j]
            key = tuple((u, raw(u, n)-3*u) for u in cyc)
            A = sum(next_edge(u, n)[1] for u in cyc)
            out[key] = Fraction(A, len(cyc))
        seen.update(trail)
    require(len(set(out.values())) == 1, "all literal components have one rotation")
    return out


def one_clock(n):
    x = 1
    t = w = 0
    visited = {}
    while x not in visited:
        visited[x] = (t, w)
        x, a = next_edge(x, n)
        t += 1
        w += a
    p, A = visited[x]
    return Fraction(w-A, t-p)


def main():
    last = 801
    graphs = {n:graph(n) for n in range(1, last+1, 2)}
    hist = {}
    for n, g in graphs.items():
        for key in g:
            hist.setdefault(key, []).append(n)
    for key, cutoffs in hist.items():
        lo = max(u for u, d in key)
        deaths = [3*u if d == 1 else (3*u+1)//2 for u, d in key if d]
        require(deaths, "positive component uses some correction")
        hi = min(deaths)
        require(cutoffs == list(range(lo, min(hi, last+2), 2)),
                "birth at maximum odd part and death at first exact blocker")
    origins = environments = 0
    for cutoff, comps in graphs.items():
        h = 0
        while 3**h < 2*cutoff:
            h += 1
        h += 2
        for key, th in comps.items():
            q = len(key)
            A = th.numerator
            labels = []
            raw_labels = []
            for u, d in key:
                z = u
                while 2*z <= cutoff:
                    z *= 2
                labels.append(z)
                raw_labels.append((3*u+d)*(z//u))
            by_size = {z:r for r, z in enumerate(sorted(labels))}
            signatures = {}
            env = set()
            for i, z0 in enumerate(labels):
                B = 0
                bs, cs, allowed = [], [], []
                for j in range(h):
                    t = (i+j) % q
                    z = labels[t]
                    dest = labels[(t+1)%q]
                    quotient, rem = divmod(raw_labels[t], dest)
                    require(not rem and quotient&(quotient-1)==0,
                            "exact normalized octave advance")
                    b = quotient.bit_length()-1
                    B += b
                    require(B == (by_size[z0]+(j+1)*A)//q, "windings at every subwindow")
                    bs.append(b)
                    cs.append(raw_labels[t]-3*z)
                    allowed.append(3*z>2*cutoff)
                require(2**B>cutoff, "injective integer-source modulus")
                signature = (tuple(bs), tuple(cs))
                require(signature not in signatures, "all individual window origins distinguished")
                signatures[signature] = z0
                env.add((tuple(bs), tuple(allowed)))
                origins += 1
            require(len(env) <= 4*h+4, "mechanical joint environment count")
            environments += len(env)
    require(20**520 < 19**494*3**100, "entropy threshold using mu < 26/5")
    require(3**103*1000**128 < 2421**128, "component lifetime ratio using mu < 128/25")
    require(Fraction(56,81)>Fraction(330,489), "endpoint decimal using the elementary log two bound")
    products = nonempty = multiple = survived = 0
    for lo, first in graphs.items():
        for hi in range((3*lo+1)//2, min(last, 3*lo)+1):
            if hi % 2 == 0 or 2*hi < 3*lo+1:
                continue
            active = first.keys() & graphs[hi].keys()
            if not active:
                continue
            nonempty += 1
            multiple += len(active)>1
            survived += len(active)
            th = first[next(iter(active))]
            # A/q is reduced, and every actual periodic component has q vertices.
            q, A = th.denominator, th.numerator
            require(all(len(key)==q for key in active), "reference period independent of origin")
            states = set()
            used = []
            for key in active:
                for u, d in key:
                    require(u not in states, "different components are disjoint at the same cut")
                    states.add(u)
                    require(d == 0 or (d == 1 and 3*u>hi), "single high-arc correction")
                    if d:
                        used.append(u)
            eligible = [u for u in range(1, lo+1, 2) if 3*u>hi]
            require(set(used) <= set(eligible), "literal high correction list")
            left_num, left_den = (1 << A)**len(active), 3**(q*len(active))
            used_num = prod(3*u+1 for u in used)
            used_den = prod(3*u for u in used)
            rhs_num = prod(3*u+1 for u in eligible)
            rhs_den = prod(3*u for u in eligible)
            require(left_num*used_den == left_den*used_num, "complete exact correction products")
            require(left_num*rhs_den <= left_den*rhs_num, "finite aggregate drift cap")
            products += 1
    require(nonempty>0, "actual components surviving the full tested interval")
    invariant_edges = 0
    for b in (1, 2):
        for bnext in (1, 2):
            for z in range(-3, 4):
                if b == 1 and z % 2:
                    continue
                for d in ([0] if b == 1 else range(-6, 7)):
                    u, rem = divmod(3*z+d,1 << b)
                    if rem or bnext == 1 and u % 2:
                        continue
                    require(abs(u)<=3 and (bnext==2 or abs(u)<=2),
                            "bounded zero-invariant on the exact local transducer")
                    require(z*u>=0, "nonzero signs cannot cross")
                    if bnext==2 and u%4==0:
                        require(u==0, "forced two-row vanishes inside the invariant")
                    invariant_edges += 1
    selected = [(21,79,Fraction(8,5)), (117,291,Fraction(27,17)),
                (1341,2155,Fraction(65,41)), (17217,20491,Fraction(317,200)),
                (126573,157323,Fraction(485,306))]
    for lo, hi, v in selected:
        # Monotonicity proves constancy throughout. These four independently
        # recomputed endpoints certify precisely the maximal interval.
        require(one_clock(lo-2)>v and one_clock(lo)==v and one_clock(hi)==v
                and one_clock(hi+2)<v, "both strict endpoints of the exact reference plateau")
    return {"literal_cutoff_maximum":last, "distinct_components":len(hist),
            "lifetime_incidence_checks":sum(map(len,hist.values())),
            "long_interval_nonempty_checks":nonempty,"multiple_survivor_checks":multiple,
            "persistent_component_cases":survived, "exact_product_caps":products, "curvature_invariant_edges":invariant_edges,
            "window_origins_checked":origins, "joint_environment_checks":environments,
            "maximal_plateau_examples":[[lo,hi,str(v)] for lo,hi,v in selected]}


if __name__ == "__main__":
    print(json.dumps(main(), indent=2, sort_keys=True))
