"""Exact finite controls for the simultaneous ordinary octave cut theorem."""
from bisect import bisect_left
from fractions import Fraction
from math import gcd
from itertools import combinations
import json


def require(prop, message):
    if not prop:
        raise ArithmeticError(message)


def lowbit(n):
    return n & -n


def rotation_at(start, step):
    marks = {}
    tick = clock = 0
    point = start
    while point not in marks:
        marks[point] = (tick, clock)
        point, elapsed = step(point)
        clock += elapsed
        tick += 1
    tick0, clock0 = marks[point]
    return Fraction(clock-clock0, tick-tick0)


def rotations_fast(s, with_orbits=False):
    """S is an odd positive integer, so L=4S is an eligible first point."""
    require(s > 0 and s % 2 == 1, "odd scale")
    left = 4*s

    def step(point, upper):
        raw = 3*point + lowbit(point)
        shift = 1 + int(raw >= 4*left)
        unit = 1 << shift
        if upper:
            after = (raw+unit-1)//unit
            after += int(after % 8 == 0)
            if after >= 2*left:
                after, shift = left, shift+1
        else:
            after = raw//unit
            after -= int(after % 8 == 0)
        require(left <= after < 2*left and after % 8 != 0, "fundamental label")
        return after, shift

    if not with_orbits:
        return tuple(rotation_at(left, lambda z: step(z, upper)) for upper in (False, True))
    cycles = []
    for upper in (False, True):
        visited = {}
        rows = []
        u = left
        while u not in visited:
            visited[u] = len(rows)
            v,b = step(u,upper)
            rows.append((u,3*u+lowbit(u),(1<<b)*v))
            u=v
        cycles.append(rows[visited[u]:])
    return cycles


def witness_interval(rows):
    """All cut parameters retaining this literal projected cycle."""
    integers = [u//lowbit(u) for u,_,_ in rows]
    smallest, largest = min(integers),max(integers)
    lo,hi = Fraction(largest,8),Fraction(smallest)
    blockers = set()
    for _,raw,target in rows:
        if raw==target:
            continue
        low,high = sorted((raw,target))
        # On a witness discovered at an odd cut S, raw and target lie in
        # [8S,32S] and the only relevant blockers lie between S/8 and 64S.
        for b in range(-4,10):
            den = 1 << max(b,0)
            mul = 1 << max(-b,0)
            a = (low*mul + den-1)//den
            z = high*mul//den
            for candidate in range(a+int(a%2==0),z+1,2):
                if candidate*den==target*mul:
                    continue
                if largest < 8*candidate and candidate < 8*smallest:
                    blockers.add(candidate)
    require(not any(smallest<=z<=largest for z in blockers),"blocker inside recognized orbit hull")
    for z in blockers:
        if z<smallest:
            lo=max(lo,Fraction(z))
        else:
            hi=min(hi,Fraction(z,8))
    return lo,hi


def survives(rows,s):
    """Independent literal nearest-grid test of the recorded lifted edges."""
    left = 4*s
    nodes = [n for n in range(1,int(8*s)+1,2) if s<=n<8*s]
    for u,raw,target in rows:
        if u//lowbit(u) not in nodes or target//lowbit(target) not in nodes:
            return False
        if raw==target:
            continue
        low,high=sorted((raw,target))
        for n in nodes:
            scaled=Fraction(n)
            while scaled>low:
                scaled/=2
            while scaled<low:
                scaled*=2
            if low<=scaled<=high and scaled!=target:
                return False
            if scaled==target and 2*scaled<=high:
                return False
    return True


def interval_controls():
    cases = 0
    for s0 in (1,3,5,9,11,13,17,23):
        for rows in rotations_fast(s0,with_orbits=True):
            lo,hi=witness_interval(rows)
            require(lo<s0<=hi,"own cut in exact interval")
            for i in range(1,8*31+1):
                s=Fraction(i,8)
                require(survives(rows,s)==(lo<s<=hi),"exact rounded-orbit persistence")
                cases+=1
    return cases


def reference(s, span=8, sign=1, all_starts=False, subset=None):
    """Build literal dyadic grids; handles arbitrary rational S and subgrids."""
    left = (span//2)*s
    phases = subset or [z for z in range(1, int(span*s)+1, 2) if s <= z < span*s]
    require(phases and all(s <= z < span*s for z in phases), "valid reference grid")
    lifted = {}
    for z in phases:
        v = z
        while v < left:
            v *= 2
        lifted[v] = v//z
    base = sorted(lifted)
    size = len(base)
    cover = [v*(1 << b) for b in range(5) for v in base]
    maps = []
    for upper in (False, True):
        rows = {}
        full_indices = []
        for v in base:
            value = 3*v + sign*lifted[v]
            index = bisect_left(cover, value)
            require(0 < index < len(cover), "target in literal cover")
            if not upper and cover[index] != value:
                index -= 1
            elapsed, k = divmod(index, size)
            rows[v] = (base[k], elapsed)
            full_indices.append(index)
        require(all(a<=b for a,b in zip(full_indices,full_indices[1:]+[full_indices[0]+size])), "monotone degree one")
        rotations = {rotation_at(v, rows.__getitem__) for v in (base if all_starts else base[:1])}
        require(len(rotations)==1,"common rotation")
        maps.append(rotations.pop())
    return tuple(maps)


def mechanical(p, h):
    numerator = clock = 0
    word = [((i+1)*h)//p-(i*h)//p for i in range(p)]
    for e in word:
        numerator = 3*numerator + (1 << clock)
        clock += e
    det = (1 << h)-3**p
    q = det//gcd(det,numerator)
    start = Fraction(numerator,det)
    point = start
    orbit = []
    for e in word:
        require(point.denominator==q and point.numerator % 2, "complete denominator and exact odd quotient")
        orbit.append(point)
        point = (3*point+1)/(1 << e)
    require(point==start and len(set(orbit))==p, "closed primitive rational cycle")
    return q, min(orbit), max(orbit)


def physical_span(x0, sign):
    z = x0
    phases = []
    clock = 0
    while z not in phases:
        phases.append(z)
        raw = 3*z+sign
        b = lowbit(raw).bit_length()-1
        z = raw >> b
        clock += b
    require(z==x0, "comparison trajectory closed")
    return phases, Fraction(clock,len(phases))


def main():
    replayed = 0
    for s in range(1,402,2):
        require(reference(s,all_starts=s<=31)==rotations_fast(s), "two exact algorithms disagree")
        replayed += 1
    checked = 50000
    locks = []
    for s in range(1,2*checked,2):
        lo,hi = rotations_fast(s)
        require(lo<=hi,"envelope order")
        if lo==hi:
            locks.append([s,str(lo)])
    require(locks==[[1,"2"],[9,"8/5"],[11,"8/5"]], "finite census")

    # S may be rational. All rational cells and endpoints in the selected interval
    # are sampled. This includes the change of fundamental representatives.
    trials = []
    for start,sign,span in ((1,1,8),(5,-1,4)):
        phases,slope = physical_span(start,sign)
        lower = Fraction(max(phases),span)
        upper = Fraction(min(phases))
        cuts = {lower,upper}
        for n in range(1,int(span*upper)+1,2):
            for t in (Fraction(n),Fraction(n,span)):
                if lower < t <= upper:
                    cuts.add(t)
        cuts = sorted(cuts)
        tests = sorted(set(cuts[1:])|{(a+b)/2 for a,b in zip(cuts,cuts[1:])})
        for t in tests:
            require(reference(t,span,sign,all_starts=True)==(slope,slope),"integer locking interval")
            require(reference(t,span,sign,all_starts=True,subset=phases)==(slope,slope),"exact subgrid")
        trials.append({"sign":sign,"minimum":min(phases),"maximum":max(phases),"slope":str(slope),"tested_cells_and_endpoints":len(tests)})
    tested_words = 0
    for cuts in combinations(range(1,8),4):
        events = (0,)+cuts
        carry = sum(3**(4-i) * (1<<v) for i,v in enumerate(events))
        require(carry%13!=0,"unexpected integer period-five clock-eight source")
        tested_words += 1
    rational = []
    for p,h in ((5,8),(41,65),(306,485)):
        q,minimum,maximum = mechanical(p,h)
        t = int(minimum)
        t -= int(t%2==0)
        require(maximum/8 < t <= minimum and q>1,"rational phase sits in claimed physical band")
        lo,hi = rotations_fast(t)
        require(lo != hi and (lo!=Fraction(h,p) or hi!=Fraction(h,p)),"ordinary rounding differs")
        rational.append({"p":p,"h":h,"q_bits":q.bit_length(),"ordinary_scale":t,
                         "lower":str(lo),"upper":str(hi)})
    return {"direct_orbit_interval_checks":interval_controls(),"paired_independent_algorithms":replayed,"odd_scales_checked":checked,
            "complete_finite_list_of_locks":locks,"genuine_integer_controls":trials,
            "integer_period_five_words_excluded":tested_words,"genuine_nonintegral_controls":rational}


if __name__=="__main__":
    print(json.dumps(main(),indent=2,sort_keys=True))
