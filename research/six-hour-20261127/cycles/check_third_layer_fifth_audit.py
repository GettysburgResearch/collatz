"""Independent exact finite controls for a narrow third grade in the fifth moment."""
from collections import Counter, defaultdict
from fractions import Fraction as F
from hashlib import sha256
from math import factorial, gcd
from itertools import product
import json

CAP = F(1, 100000)


def require(test, detail):
    if not test:
        raise RuntimeError(detail)


def schedule(slope, phase, length):
    floors = [(phase + j * (1 + slope)) // 1 for j in range(length + 1)]
    caps = [2 if (phase + j * slope) % 1 <= CAP else 1 for j in range(length + 1)]
    return tuple(floors), tuple(caps)


def controls_by_phase():
    slopes = [F(584961, 1000000), F(117, 200), F(584964, 1000000)]
    endpoints = [0, 0]
    histogram = Counter()
    tests = raw = 0
    for length in (1, 2, 3, 5, 7, 8):
        for slope in slopes:
            cuts = sorted({(b - j * slope) % 1 for j in range(length + 1)
                           for b in (0, CAP)})
            faces = cuts + [(l + r) / 2 for l, r in zip(cuts, cuts[1:] + [1])]
            for phase in faces:
                dates, caps = schedule(slope, phase, length)
                gaps = [r - l for l, r in zip(dates, dates[1:])]
                for i, cap in enumerate(caps):
                    if cap != 2:
                        continue
                    if i:
                        require((caps[i-1], gaps[i-1]) == (1, 2), 'left bridge')
                    if i < length:
                        require((caps[i+1], gaps[i]) == (1, 1), 'right bridge')
                    endpoints[0] += i == 0
                    endpoints[1] += i == length
                # Independently enumerate the physical valuation word from a fixed
                # incoming grade. Grade is recovered at every cut from actual time.
                for incoming in range(caps[0] + 1):
                    actual = defaultdict(Counter)
                    for exponents in product((1, 2), repeat=length):
                        cursor = b = 0
                        for i, e in enumerate(exponents):
                            b = 3 * b + (1 << cursor)
                            cursor += e
                            grade = dates[i+1] + incoming - cursor
                            if not 0 <= grade <= caps[i+1]:
                                break
                        else:
                            actual[grade][b] += 1
                            raw += 1
                    # Matrix polynomial propagated using just fine digital characters.
                    states = {incoming: Counter({0: 1})}
                    scalar = 0
                    for i, gap in enumerate(gaps):
                        factor = (1 << dates[i]) * 3**(length - 1 - i)
                        scalar += 4 * factor
                        future = defaultdict(Counter)
                        for z, poly in states.items():
                            digit = 4 - (1 << (2-z))
                            for dest in range(caps[i+1] + 1):
                                if gap + z - dest in (1, 2):
                                    for h, c in poly.items():
                                        future[dest][h+digit*factor] += c
                        states = future
                    for dest in range(caps[-1]+1):
                        transformed = Counter()
                        for h, mult in states.get(dest, {}).items():
                            b4 = (1 << incoming)*(scalar-h)
                            require(b4 % 4 == 0, 'numerator dilation')
                            transformed[b4//4] += mult
                        require(actual[dest] == transformed, 'fixed-cuts identity')
                        tests += 1
                    histogram[(caps[0], caps[-1])] += 1
    require(all(endpoints), 'unpaired endpoint controls')
    return dict(fixed_cut_tests=tests, actual_paths=raw, eligible_endpoints=tuple(endpoints),
                endpoint_cap_patterns={str(k): v for k, v in sorted(histogram.items())})


def full_fine_history():
    # The finite source N is a multiple of 3**length, with independent 5-adic
    # factor. Condition on every earlier value, so the fine threefold law is tested
    # even after arbitrarily dependent amplitude information from preceding letters.
    histories = ties = 0
    for length in (2, 3, 4, 5):
        N = 5 * 3**length
        for gaps in product((1, 2), repeat=length):
            factors, m = [], 0
            for i, gap in enumerate(gaps):
                factors.append((1 << m) * 3**(length-1-i))
                m += gap
            groups = [defaultdict(Counter) for _ in gaps]
            for v in range(N):
                obs = tuple(f*v % N for f in factors)
                for i, fine in enumerate(obs):
                    groups[i][(obs[:i], 3*fine % N)][fine] += 1
            for i, group in enumerate(groups):
                for (past, state), mult in group.items():
                    roots = set(mult)
                    require(len(roots) == 3 and len(set(mult.values())) == 1, 'law')
                    u = min(roots)
                    require(roots == {(u+j*N//3) % N for j in range(3)}, 'roots')
                    coarse = {(2*w) % N for w in roots}
                    require(len(coarse) == 3 and all(3*w % N == 2*state % N for w in coarse),
                            'clean cochain pullback')
                    if past:
                        require((1 << gaps[i-1])*past[-1] % N == state, 'next state')
                        ties += 1
                    histories += 1
    return dict(full_past_fibres=histories, noninitial_fibres=ties)


def bridge_characters():
    # Entrywise polynomials in previous v and current u, before imposing their
    # ternary relation. Coefficients count the intermediate grades exactly.
    layers = [[Counter() for _ in range(2)] for _ in range(2)]
    for left, middle, right in product(range(2),range(3),range(2)):
        if 2+left-middle in (1,2) and 1+middle-right in (1,2):
            layers[right][left][(2*left,4-(1 << (2-middle)))] += 1
    expected = [[{(0,0):1,(0,2):1}, {(2,2):1}],
                [{(0,2):1},{(2,2):1,(2,3):1}]]
    require(layers == expected, 'digital characters through bridge')
    abs_matrix = [[sum(entry.values()) for entry in row] for row in layers]
    require(abs_matrix==[[2,1],[1,2]], 'absolute matrix')
    baseline = F(9,100)
    charge = F(3*3**5,4)/baseline
    evel = sum(F(1,factorial(j)) for j in range(5))
    require(charge == 2025 and evel**8 > charge, 'bridge charge')
    require(F(1,7000)-8*CAP > F(1,16000) and
            sum(F(5,4)**j/factorial(j) for j in range(4)) > 3 and
            F(5,4)/20000 == F(1,16000), 'logarithmic margin')
    return dict(bridge_composite=abs_matrix, bridge_factor=int(charge))


def affine_block(exponents):
    # Compose affine maps x -> (3 x + 1)/2**e in chronological order.
    if len(exponents) == 1:
        return 3, exponents[0], 1
    mid = len(exponents)//2
    first, e1, b = affine_block(exponents[:mid])
    last, e2, c = affine_block(exponents[mid:])
    return first*last, e1+e2, last*b+(c << e1)


def witness():
    period, total = 190537, 301994
    s = total-period
    require(gcd(period,total) == 1, 'primitive clocks')
    middle = pow(s,-1,period)
    special = {(middle+j)%period:z for j,z in ((-1,1),(0,2),(1,1),(2,1))}
    e = []
    width = []
    for i in range(period):
        phase = (i*s)%period
        now = special.get(i,0)
        nxt = special.get((i+1)%period,0)
        e.append(1+(phase+s>=period)+now-nxt)
        width.append(phase+period*now)
    require(set(e) == {1,2} and sum(e) == total, 'actual e')
    span = F(max(width)-min(width),period)
    require(span == 2+F(1,period) and 2 < span < 2+CAP, 'exact width')
    multiplier,binary,b = affine_block(e)
    det = (1 << binary)-multiplier
    require(det>0 and b%2==1 and multiplier==3**period, 'physical affine identity')
    g = gcd(b,det)
    numerator,denominator = b//g,det//g
    check = numerator
    record = []
    # A complete circuit is proved by the affine identity. Its initial and
    # final 40 exact valuations independently check ordinary odd interpretation.
    for v in e[:40]:
        value = 3*check+denominator
        require((value & -value).bit_length()-1 == v, 'forward valuation')
        check = value >> v
        record.append(v)
    check = numerator
    for v in reversed(e[-40:]):
        value = (check << v)-denominator
        require(value%3==0 and (value//3)%2==1, 'backward reconstruction')
        check = value//3
    require((numerator << binary) == multiplier*numerator+denominator*b,
            'complete physical return')
    return dict(period=period, total_gap=total, width=str(span), positive=True,
                numerator_bits=numerator.bit_length(),denominator_bits=denominator.bit_length(),
                word_sha256=sha256(bytes(e)).hexdigest(), affine_gcd_bits=g.bit_length())


if __name__ == '__main__':
    print(json.dumps({"bridge":bridge_characters(),"fixed_cuts":controls_by_phase(),
                      "fine_law":full_fine_history(),"physical_witness":witness()},
                     indent=2,sort_keys=True))
