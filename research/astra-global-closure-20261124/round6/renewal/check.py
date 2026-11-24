"""Exact finite checks of fixed-total paired branches, Haar rows and renewals."""

from collections import Counter, defaultdict
from fractions import Fraction
import json


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def step(x):
    return (3*x+1)//2 if x % 2 else x//2


def marked_trace(x, n):
    """Return ordinary paired odd marks, the two counts, and both endpoints."""
    y = 5*x
    p = s = 0
    marks = []
    for t in range(1, n+1):
        p += x % 2
        s += y % 2
        x, y = step(x), step(y)
        if x % 2 and p == s and y == 5*x:
            marks.append((t, x))
    return marks, p, s, x, y


def unit(x):
    return x > 0 and x % 2 == 1 and x % 3 != 0


class PairDictionary:
    def __init__(self, n):
        require(n > 0 and n % 162 == 0, "period coverage")
        self.n = n
        self.e = n+11
        self.b = 1 << self.e
        self.degree = n//81
        self.carries = {t: 7*(1 << t)+63 for t in range(6, n+6)}
        self.by_mod = defaultdict(list)
        for t, c in self.carries.items():
            self.by_mod[c % 243].append(t)

    def children(self, q):
        require(unit(q), "supplied state is an ordinary unit")
        outputs = []
        target = self.b*q
        for r in (1, 2):
            for t in self.by_mod[(target-81*r) % 243]:
                x, rem = divmod(target-self.carries[t], 81)
                require(rem == 0 and unit(x), "integral unit endpoint")
                y, rem = divmod((q << (self.e-t))-7, 9)
                require(rem == 0 and unit(y), "integral unit intermediate")
                require((y << t) == 9*x+7, "inner word row")
                outputs.append((t, x, y))
        require(len(outputs) == self.degree, "complete ordinary row degree")
        return outputs


def natural_depth():
    d = PairDictionary(162)
    units = {r for r in range(243) if r % 3}
    require(set(d.by_mod) == units and all(len(v) == 1 for v in d.by_mod.values()),
            "one unit occurrence per 162-label period")
    routes = set()
    physical = 0
    for r in sorted(units):
        q = r if r % 2 else r+243
        for t, x, y in d.children(q):
            require((q, x) not in routes, "duplicate fixed-clock child")
            routes.add((q, x))
            marks, p, s, a, b = marked_trace(x, d.e)
            require((marks, p, s, a, b) == ([(t,y),(d.e,q)], 4, 4, q, 5*q),
                    "first-return parsing and paired endpoints")
            require(55*81*x >= d.b*(55*q-7) and 81*x < d.b*q, "real offset")
            physical += 1

    modulus = 3**9
    hist = Counter((d.b*l+81*r) % modulus for l in d.carries.values()
                   for r in d.carries.values())
    require(set(hist) == {a for a in range(modulus) if a % 3},
            "two-pair support through natural depth plus one")
    require(set(hist.values()) == {2}, "complete Fourier zeros through conductor nine")
    return dict(padding_labels=d.n, ternary_unit_parent_classes=len(units),
                two_block_clock=d.e, complete_physical_pair_replays=physical,
                four_block_carry_words=d.n**2, four_block_unit_cells=len(hist),
                multiplicity_at_natural_depth_plus_one=2)


def exact_routes():
    results = []
    for precision, d, roots in ((2, PairDictionary(486), (1,5,7,13,205)),
                                (3, PairDictionary(1458), (1,7,205))):
        modulus = 3**precision
        instances = physical = appended = 0
        for q in roots:
            layer = [(q, ())]
            for _ in range(precision):
                following = []
                for y, history in layer:
                    following.extend((x, history+(t,)) for t, x, _ in d.children(y))
                layer = following
            require(len({x for x, _ in layer}) == len(layer) == d.degree**precision,
                    "distinct fixed-clock ordinary reconstructions")
            tally = Counter(x % modulus for x, _ in layer)
            require(set(tally) == {r for r in range(modulus) if r % 3} and
                    set(tally.values()) == {len(layer)//len(tally)},
                    "every target unit cell has the exact Haar count")
            for x, _ in layer:
                require(55*81**precision*x >= d.b**precision*(55*q-7) and
                        81**precision*x < d.b**precision*q, "composed real interval")
                if precision == 3:
                    z, rem = divmod(64*x-7, 9)
                    if not rem and unit(z):
                        appended += 1
            for x, history in (layer[0], layer[len(layer)//2], layer[-1]):
                t = 0
                expected = []
                for label in reversed(history):
                    t += label
                    expected.append(t)
                    t += d.e-label
                    expected.append(t)
                marks, p, s, a, b = marked_trace(x, d.e*precision)
                require(([h for h, _ in marks],p,s,a,b) ==
                        (expected,4*precision,4*precision,q,5*q),
                        "all forward marked stops in chronological order")
                physical += 1
            instances += len(layer)
        if precision == 3:
            require(9*appended == instances, "exact appended six-clock row average")
        results.append(dict(precision=precision, padding_labels=d.n, ordinary_roots=list(roots),
                            common_clock=d.e*precision, common_odd_count=4*precision,
                            distinct_sources_over_all_roots=instances,
                            full_physical_paths_replayed=physical,
                            appended_six_clock_words=(appended if precision == 3 else None)))
    return results


def renewal_grid(horizon=14):
    first = Counter()
    all_marks = Counter()
    grid = 1 << horizon
    for x in range(1, 2*grid, 2):
        y = 5*x
        p = s = 0
        seen = False
        for h in range(1, horizon+1):
            p += x % 2
            s += y % 2
            x, y = step(x), step(y)
            if x % 2 and p == s and 5*x == y:
                all_marks[h,p] += 1
                if not seen:
                    first[h] += 1
                    seen = True
    u = {h: sum(v for (e,_),v in all_marks.items() if e == h)/Fraction(grid)
         for h in range(1, horizon+1)}
    u[0] = Fraction(1)
    for h in range(1, horizon+1):
        require(u[h] == sum(Fraction(first[j],grid)*u[h-j] for j in range(1,h+1)),
                "ordinary-grid renewal convolution")
    for (h,_), count in all_marks.items():
        require((count << h) % grid == 0, "row mass is a whole number of sentinelled words")
    return dict(physical_horizon=horizon, odd_binary_cylinders=grid,
                nonempty_complete_rows=len(all_marks), tested_renewal_equations=horizon,
                total_positive_mark_visits=sum(all_marks.values()))


if __name__ == "__main__":
    print(json.dumps(dict(natural_depth=natural_depth(), exact_routes=exact_routes(),
                          renewal_grid=renewal_grid()), indent=2, sort_keys=True))
