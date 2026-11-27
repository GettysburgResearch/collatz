"""Exact dyadic ceilings on actual ordinary edges and one-vertex surgeries."""
from bisect import bisect_left, bisect_right
from fractions import Fraction
import json


def require(ok, detail):
    if not ok:
        raise ArithmeticError(detail)


def oddpart(z):
    return z // (z & -z)


def native(x):
    raw = 3*x+1
    a = (raw & -raw).bit_length()-1
    return a, raw >> a


class OctaveGrid:
    def __init__(self, N):
        self.N = N
        # Integer units of one eighth up to the largest raw triple tested.
        # At a source x with 4*x>=N-1, a reduced denominator >=16 would
        # have odd numerator >N. The same holds at its larger raw image.
        self.points = sorted({n << k for n in range(1, N+1, 2)
                              for k in range((128*N).bit_length()+1)})

    def ceiling(self, x8):
        return self.points[bisect_left(self.points, 3*x8)]

    def band(self, x):
        return self.points[bisect_right(self.points, 8*x):
                           bisect_right(self.points, 8*(x+1))]


def components(N):
    def raw(x):
        if 3*x <= N:
            return 3*x
        y = 3*x+1
        return y if oddpart(y) <= N else y+2

    seen = set()
    cycles = []
    for root in range(1, N+1, 2):
        if root in seen:
            continue
        paths = []
        index = {}
        x = root
        while x not in seen and x not in index:
            index[x] = len(paths)
            paths.append(x)
            x = oddpart(raw(x))
        if x in index:
            cyc = paths[index[x]:]
            winding = sum((raw(u) & -raw(u)).bit_length()-1 for u in cyc)
            cycles.append((set(cyc), Fraction(winding, len(cyc))))
        seen.update(paths)
    require(len({r for _, r in cycles}) == 1, "one common exact rotation")
    return cycles


def main():
    edges = choices = optional = controlled = 0
    vals = set()
    for n in range(1, 320, 2):
        grid = OctaveGrid(n)
        for x in range(1, 2*n, 2):
            a, y = native(x)
            if min(x, y)*4 < n or max(x, y)+1 > 2*n:
                continue
            edges += 1
            vals.add(a)
            J = grid.band(x)
            K = grid.band(y)
            require(J == [v for v in (8*x+4, 8*x+8)
                          if v == 8*x+8 or 2*x+1 <= n], "exact upper bundle")
            optional += len(J) == 2
            require(grid.ceiling(J[0]) == (K[0] << a),
                    "strict dyadic successor intertwines with the native edge")
            for v in J:
                dest = grid.ceiling(v)
                require(dest % (1 << a) == 0 and (dest >> a) in K,
                        "literal grid image of every available member")
                ghost = 2*y+1 <= n and (a >= 2 or v == 8*x+4)
                require(dest == ((8*y+8-4*ghost) << a),
                        "literal two-choice update, including nonbinary valuations")
                choices += 1
            if n < 2*min(x, y)+1:
                require(grid.ceiling(8*x+8) == ((8*y+8) << a),
                        "unrestricted plus shift before the first smaller member")
                controlled += 1
    require(max(vals)>=4 and optional>0, "wide native valuations and both choices")

    critical = {}
    odd_minima = {1}
    for s in range(3, 721, 2):
        a0, y = native(s)
        if y < s or s % 3 == 0:
            continue
        require(a0 == 1, "a nontrivial local minimum increases by exponent one")
        old, new = OctaveGrid(4*s-1), OctaveGrid(4*s+1)
        for a in range(2, 9):
            m, rem = divmod((1 << a)*s-1, 3)
            if rem or m > 4*s+1 or m % 2 != 1:
                continue
            require(native(m) == (a, s), "actual ordinary predecessor at claimed valuation")
            labels = old.band(m)
            if a == 2:
                require((2*m-1)//3<s and 2*m+1 <= 4*s-1, "previous exponent-one source too small")
                labels = [8*m+4]
            for v in labels:
                # Use scale 4/2^a at the critical insertion; the result
                # remains an eighth-grid point for these genuine local paths.
                require((4*v) % (1 << a) == 0, "critical source scale")
                z = (4*v) >> a
                require(old.ceiling(z) == 8*(4*s+2), "changed outgoing edge on old candidate bundle")
                require(new.ceiling(z) == 8*(4*s+1), "new edge into the added vertex")
                require(new.ceiling(8*s+2) == 8*(3*s+1), "quarter point meets the native successor")
                critical[a] = critical.get(a, 0)+1
                odd_minima.add(s)

    # Real graph phenomena without positing a nontrivial positive cycle.
    for n in (1, 3):
        require(components(n)[0][1] == 2, "genuine unit cycle on the entire promised interval")
    lower = components(3)
    upper = components(5)
    require(len(lower) == len(upper) == 1 and lower[0][1] > upper[0][1],
            "strict drop for the actual cycle of minimum one")
    lower = components(75)
    upper = components(77)
    require(len(lower) == 2 and len(upper) == 1 and lower[0][1] == upper[0][1]
            and 77 not in upper[0][0], "component loss without a rotation drop is possible")

    # Full rational cycle with odd period three, complete determinant five.
    nums = [23, 37, 29]
    word = [1, 2, 2]
    q = 5
    require((1 << sum(word))-3**len(word)==q and all(x % q for x in nums),
            "entire positive-word denominator retained")
    for j, a in enumerate(word):
        require(3*nums[j]+q == (1 << a)*nums[(j+1)%3], "literal reduced rational edges")
    s, X = Fraction(min(nums), q), Fraction(max(nums), q)
    bad = 17
    require((X+1)/2 <= bad <= 4*s and components(bad)[0][1] != Fraction(sum(word), len(word)),
            "the all-width ceiling inference genuinely needs integer phases")
    return {"ordinary_edges":edges, "literal_bundle_images":choices, "two_choice_sources":optional,
            "valuations":sorted(vals), "plus_only_checks":controlled,
            "local_critical_incoming_valuations":critical, "local_minimum_candidates":len(odd_minima)-1,
            "unit_cycle_critical_drop":"2 to 5/3", "generic_cut_77":"two components to one at 8/5",
            "rational_control":{"numerators":nums, "full_denominator":q, "cutoff":bad,
                                "native_clock":"5/3", "ceiling_clock":"13/8"}}


if __name__ == "__main__":
    print(json.dumps(main(), sort_keys=True, indent=2))
