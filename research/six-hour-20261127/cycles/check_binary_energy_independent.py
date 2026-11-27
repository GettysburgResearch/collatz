"""Independent exact arithmetic checks for the binary-cycle review. Standard library only."""
from collections import Counter
from fractions import Fraction as Q
from itertools import combinations, product
from math import ceil, floor, gcd
import json


def check(test, reason):
    if not test:
        raise ArithmeticError(reason)


Z, R, N = Q(0), Q(49, 50), 53
A, B = Q(584961, 1000000), Q(584964, 1000000)
STATES = [s for s in product((0, 1), repeat=4) if s[0] + s[1] == s[2] + s[3]]
ZERO = (0,) * 4


def relevant_lines():
    """Unwrapped t = c - j alpha that touch the closed parameter rectangle."""
    lines = set()
    for j in range(N + 1):
        for cap in (Z, R):
            for k in range(ceil(j*A - cap), floor(1 + j*B - cap) + 1):
                lines.add((j, k + cap))
    lines |= {(0, Q(0)), (0, Q(1))}
    return sorted(lines)


def time_itinerary(alpha, t):
    phases = [t + j*alpha for j in range(N + 1)]
    floors = [floor(x) for x in phases]
    forced = [x - i > R for x, i in zip(phases, floors)]
    letters = [1 + j - i for i, j in zip(floors, floors[1:])]
    return tuple(letters), tuple(forced)


def arrangement_checks():
    # Endpoints, faces, slopes, and their incidences are all exact.
    check((2**1584961 < 3**1000000 < 2**1584964), 'critical slope not enclosed')
    lines = relevant_lines()
    unequal_slopes = 0
    for (j, u), (k, v) in combinations(lines, 2):
        if j == k:
            continue
        unequal_slopes += 1
        alpha = (u-v) / (j-k)
        if A <= alpha <= B:
            t = u - j*alpha
            check(not (0 <= t <= 1), ('incident faces', alpha, t))
    endpoint_profiles = []
    for alpha in (A, (A+B)/2, B):
        cuts = sorted(c-j*alpha for j,c in lines if 0 <= c-j*alpha <= 1)
        check(len(set(cuts)) == len(cuts), 'duplicate cut')
        check(cuts[0] == 0 and cuts[-1] == 1, 'rectangle faces')
        samples = [v for a,b in zip(cuts, cuts[1:]) for v in (a, (a+b)/2)]
        endpoint_profiles.append([time_itinerary(alpha, t) for t in samples])
    check(endpoint_profiles[0] == endpoint_profiles[1] == endpoint_profiles[2], 'boundary or open face drift')
    return endpoint_profiles[1], len(lines), unequal_slopes


def is_eligible(s, t, mech):
    return all(mech + x - y in (1,2) for x,y in zip(s,t))


COUNT_EDGES = {m: {s: [t for t in STATES if is_eligible(s,t,m)] for s in STATES}
               for m in (1, 2)}


def state_count(letters, forced, head, tail):
    if forced[0] and head != ZERO:
        return 0
    counts = Counter({head: 1})
    for m, zero_only in zip(letters, forced[1:]):
        new = Counter()
        for s, count in counts.items():
            for t in COUNT_EDGES[m][s]:
                if not zero_only or t == ZERO:
                    new[t] += count
        counts = new
    return counts[tail]


def paths(letters, forced, head, tail):
    if forced[0] and head:
        return
    stack = [(0, head, (head,), (0,))]
    while stack:
        i, current, states, times = stack.pop()
        if i == len(letters):
            if current == tail:
                yield states, times
            continue
        for t in (0,1):
            jump = letters[i] + current - t
            if jump in (1,2) and (not forced[i+1] or t == 0):
                stack.append((i+1,t,states+(t,),times+(times[-1]+jump,)))


def ordinary_num(times):
    ans = 0
    for date in times[:-1]:
        ans = 3*ans + 2**date
    return ans


def raw_pair_energy(letters, forced, head=0, tail=0):
    nums = [ordinary_num(ts) for _,ts in paths(letters, forced, head, tail)]
    sums = Counter(a+b for a in nums for b in nums)
    return len(nums), sum(x*x for x in sums.values())


def return_and_local_checks(profiles):
    hits = Counter()
    types = Counter()
    full_itineraries = set()
    for letters, forced in profiles:
        first = next(i for i, x in enumerate(forced[1:], 1) if x)
        if forced[0]:
            energy = state_count(letters[:first], forced[:first+1], ZERO, ZERO)
            check(energy**1000 < 3**(999*first), 'energy exponent')
            types[(first, energy)] += 1
        else:
            hits[first] += 1
        full_itineraries.add((letters[:8], forced[:9]))
    ex = sorted(types)
    check(ex == [(12,388224), (41,30840400948687284336), (53,17778623164916750424132973)], ex)
    direct_count = 0
    for ls, fs in full_itineraries:
        for head, tail in product((0,1), repeat=2):
            _, energy = raw_pair_energy(ls,fs,head,tail)
            check(energy == state_count(ls,fs,(head,)*4,(tail,)*4), 'direct pair energy')
            direct_count += 1
    length12 = set()
    for ls, fs in profiles:
        if fs[0] and next(i for i,x in enumerate(fs[1:],1) if x) == 12:
            length12.add(raw_pair_energy(ls[:12],fs[:13]))
    check(length12 == {(size,388224) for size, _ in length12}, 'first return raw pair sums')
    return dict(first_free_hit_max=max(hits), eligible_forced_faces=sum(types.values()),
                all_return_types=[dict(n=n,E=e,face_count=types[(n,e)]) for n,e in ex],
                direct_eight_letter_conditioned_cases=direct_count,
                direct_12_letter_word_count_and_energy=sorted(length12))


def reciprocity_checks():
    count = 0
    same_carry = 0
    wrap_observed = 0
    for d in (1,5,7,11,29,55,125):
        for a in range(2,5):
            for odd_offset, head_time, K in ((2,3,16),(9,15,36),(19,31,59)):
                m, n = K - head_time, odd_offset + a
                tested = []
                for word in product((1,2), repeat=a):
                    ts = [0]
                    for e in word:
                        ts.append(ts[-1] + e)
                    if d >= 2**(m-ts[-2]):
                        continue
                    W = Zc = 0
                    for i,r in enumerate(ts[:-1]):
                        v, w = m-r, odd_offset+i+1
                        h = d*pow(2**v,-1,3**w) % 3**w
                        z = -d*pow(3**w,-1,2**v) % 2**v
                        check(2**v*h-d == 3**w*z, 'single residue reciprocity')
                        W += 3**(a-1-i)*h
                        Zc += 2**r*z
                    num = ordinary_num(ts)
                    check(2**m*W - 3**n*Zc == d*num, 'segment reciprocity')
                    direct = (-d*sum(2**(head_time+r)*pow(3,-(i+odd_offset+1),2**K)
                                     for i,r in enumerate(ts[:-1]))) % 2**K
                    check((Zc << head_time) % 2**K == direct, 'physical source contribution')
                    tested.append((Zc,W,num))
                    count += 1
                h = min(4, m)
                stride = 2**(m-h)
                buckets = {}
                for i,u in enumerate(tested):
                    for j,vv in enumerate(tested):
                        residue = ((u[0]%2**m)//stride + (vv[0]%2**m)//stride) % 2**h
                        sig = tuple(x+y for x,y in zip(u,vv))
                        if residue not in buckets:
                            buckets[residue] = sig
                            continue
                        zd, wd, bd = (x-y for x,y in zip(sig,buckets[residue]))
                        # Recover the same integral carry by rounding once; grid equality
                        # implies error < 2*stride, and h=4 makes that carry unique.
                        k = floor(Q(zd,2**m)+Q(1,2))
                        b0, a0 = zd-k*2**m, wd-k*3**n
                        check(abs(b0)<2*stride, 'grid carry width')
                        check(2**m*a0-3**n*b0 == d*bd, 'same carry in both coordinates')
                        same_carry += 1
                        wrap_observed += bool(k)
    check(wrap_observed > 0, 'nonzero circular carry not tested')
    return dict(ordinary_raw_segment_checks=count, matching_grid_pair_checks=same_carry,
                nonzero_carry_checks=wrap_observed)


def produce_trajectory(word, cut):
    b = len(word)
    left, right = word[:cut], word[cut:]
    def cylinder(xs):
        ts = [0]
        for x in xs:
            ts.append(ts[-1]+x)
        return ts[-1], ordinary_num(ts)
    ls, lc = cylinder(left)
    rs, rc = cylinder(right)
    mod3, mod2 = 3**len(left), 2**(rs+1)
    ter = lc*pow(2**ls,-1,mod3) % mod3 if mod3>1 else 0
    dy = (2**rs-rc)*pow(3**len(right),-1,mod2) % mod2
    x = ter + mod3*((dy-ter)*pow(mod3,-1,mod2) % mod2)
    M = mod3*mod2
    lo = 100*3**b
    x += ceil(Q(lo-x,M))*M
    check(lo <= x <= 120*3**b, 'midpoint placement')
    states = [x]
    for e in reversed(left):
        y, rem = divmod(2**e*states[-1]-1,3)
        check(rem == 0 and y%2, 'backward gap')
        states.append(y)
    states.reverse()
    for e in right:
        y, rem = divmod(3*states[-1]+1,2**e)
        check(rem == 0 and y%2,'forward gap')
        states.append(y)
    check(all(y>states[0] for y in states[1:]), 'prefix decrease')
    check(min(states) >= 20*3**b and max(states) <= 500*3**b, 'trajectory placement')
    return x


def two_ended_checks():
    cnt = 0
    for b in range(1,13):
        floor_values = [(3**i).bit_length()-1 for i in range(b+1)]
        ls = [v-u for u,v in zip(floor_values,floor_values[1:])]
        fs = [False]*(b+1)
        words = []
        for tail in (0,1):
            for _,ts in paths(ls,fs,0,tail):
                words.append(tuple(v-u for u,v in zip(ts,ts[1:])))
        check(len(words) == len(set(words)), 'word collision')
        for cut in range(b+1):
            mids = [produce_trajectory(word,cut) for word in words]
            check(len(set(mids)) == len(words), 'midpoint collision')
            cnt += len(mids)
    return cnt


def necklaces(word):
    return [word[i:]+word[:i] for i in range(len(word))]


def cycle_controls():
    primitive_cycles = 0
    rotated_sources = 0
    long_horizons = 0
    for p in range(1,14):
        for w in product((1,2),repeat=p):
            rots = necklaces(w)
            if len(set(rots)) != p or w != min(rots):
                continue
            A = sum(w)
            D = 2**A - 3**p
            if D <= 0:
                continue
            starts, dates = [], []
            for v in rots:
                ts=[0]
                for e in v:
                    ts.append(ts[-1]+e)
                starts.append(Q(ordinary_num(ts), D))
                dates.append(ts)
            d = starts[0].denominator
            Y = max(x.numerator for x in starts)
            check(gcd(d, 6)==1 and all(x.denominator==d for x in starts),'common denominator')
            check(all(2**e*v == 3*u+1 for u,v,e in zip(starts,starts[1:]+starts[:1],w)),
                  'cycle carries')
            b=1
            while 2*3**b < Y:
                b+=1
            factors={tuple(w[(i+j)%p] for j in range(b)) for i in range(p)}
            check(len(factors)==p,'terminal packing')
            long_horizons+=int(b>p)
            for ts,x in zip(dates,starts):
                residues=[p*date-j*A for j,date in enumerate(ts)]
                if max(residues)-min(residues)>Q(99,50)*p:
                    continue
                z = [floor(Q(A*j+max(residues),p))-date for j,date in enumerate(ts)]
                f = [Q(A*j+max(residues),p)%1 for j in range(p+1)]
                check(all(bit in (0,1) and (t<=R or bit==0) for t,bit in zip(f,z)),
                      'real-width encoding at actual source')
                check((x.numerator+d*sum(2**k*pow(3,-j-1,2**A)
                                          for j,k in enumerate(ts[:-1])))%2**A==0,
                      'full physical source')
                rotated_sources+=1
            primitive_cycles+=1
    return dict(positive_primitive_binary_necklaces=primitive_cycles, max_period=13,
                packing_cases_longer_than_period=long_horizons,
                actual_rotated_sources_at_width_cap=rotated_sources)


def run():
    profiles, lines, pairs = arrangement_checks()
    return dict(slope_interval=[str(A),str(B)], width="99/50",
                lines_on_closed_parameter_rectangle=lines, different_slope_line_pairs=pairs,
                interior_vertex_count=0, intercept_faces_per_slope=len(profiles),
                slope_slices_with_full_itineraries_compared=3,
                exact_return_controls=return_and_local_checks(profiles),
                exact_reciprocity_controls=reciprocity_checks(),
                positive_midpoint_controls=two_ended_checks(),
                primitive_cycle_controls=cycle_controls())

if __name__ == '__main__':
    print(json.dumps(run(), indent=2, sort_keys=True))
