"""Exact rational label controls and polynomial first-crossing checks on a whole ray."""
from fractions import Fraction
from math import gcd
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def cycle(word):
    clocks = carry = 0
    for a in word:
        carry = 3*carry + (1 << clocks)
        clocks += a
    D = (1 << clocks) - 3**len(word)
    x = Fraction(carry, D)
    points = []
    for a in word:
        points.append(x)
        x = (3*x+1) / (1 << a)
    require(x == points[0] and len(set(points)) == len(word), "primitive lap")
    i = points.index(min(points))
    return points[i:] + points[:i], word[i:] + word[:i], D


def label_control(word):
    points, word, D = cycle(word)
    p, h, d = len(word), sum(word), points[0].denominator
    m = pow(p, -1, h)
    u = pow(2, m, d)*pow(3, (1-p*m)//h, d) % d
    require(pow(u,p,d) == 2%d and pow(u,h,d) == 3%d, "rank root")
    # Explore a bounded selection of actual numerator-lattice inverse words;
    # this part verifies the formula and does not claim a full inverse census.
    findings = {}
    clocks = 0
    for i, x in enumerate(points):
        stack = [(x.numerator, 0, i*h-p*clocks)]
        while stack:
            n, k, tag = stack.pop()
            require((n - points[0].numerator*pow(u,tag,d))%d == 0, "residue tag")
            require(n not in findings or findings[n] == tag, "continuation changed tag")
            findings[n] = tag
            if k == 3:
                continue
            for e in range(1, 6):
                t = (n << e)-d
                if t > 0 and t%3 == 0:
                    stack.append((t//3, k+1, tag+p*e-h))
        clocks += word[i]
    counts = dict(pairs=0, integer=0, adjacent=0, proper_partial=0,
                  equal_label=0)
    rows = sorted(findings.items())
    for j, (m, a) in enumerate(rows):
        for n,b in rows[j+1:]:
            shift = abs(a-b)
            full = d//gcd(d,pow(u,shift,d)-1)
            require(Fraction(n-m,d).denominator == full, "exact difference denominator")
            if shift == 1:
                require(full == d, "adjacent lost denominator")
            if a == b:
                require((n-m)%(2*d) == 0, "odd-lattice spacing")
            counts["pairs"] += 1
            counts["integer"] += full == 1
            counts["adjacent"] += shift == 1
            counts["proper_partial"] += 1 < full < d
            counts["equal_label"] += a == b
    require(counts["adjacent"] and counts["equal_label"], "missing label controls")
    return dict(p=p, h=h, D=D, d=d, points=len(rows), **counts)


def high_control():
    p, h, K = 190537, 301994, 4*190537
    power = 3**p
    D = (1 << h)-power
    require(D > 0 and gcd(p,h) == 1 and D%6 in (1,5), "critical clocks")
    # Minimum at rank zero is at least p*3^p/(6D).
    require(power > 81*p*D, "minimum > (27/2)*p^2")
    # ln 2 > 2/3, for example by integrating the tangent to 1/x at x=3/2.
    m = p//10
    require(2*p+6*K+9*m < 27*p, "strict separation budget")
    return dict(p=p, h=h, d_bits=D.bit_length(), all_endpoint_depth=K,
                maximum_residue_modulus=m)


def floor_log(i):
    if i >= 0:
        return (3**i).bit_length()-1
    return -(3**(-i)).bit_length()


def v2(n):
    return (n & -n).bit_length()-1


def ray(K, last):
    first = -K-1
    positions = range(first, last)
    F = {i: floor_log(i) for i in range(first, last+1)}
    C = A = 0
    for i in positions:
        C = 3*C + (1 << A)
        A += F[i+1]-F[i]
    M = 2 << A
    n = ((1 << A)-C)*pow(3, -(last-first), M) % M + 4*M
    # Preserve every shifted clock cylinder, every source residue mod 3,
    # and the binary offset phase at the extreme right endpoint.
    stride = 48*M
    xs, ds = {first:n}, {first:stride}
    for i in positions:
        e = F[i+1]-F[i]
        require(v2(3*n+1)==e and stride%(1 << e)==0, "native ray")
        n = (3*n+1) >> e
        stride = (3*stride) >> e
        xs[i+1], ds[i+1] = n, stride
    s, delta = xs[0], ds[0]
    require(s%18==1 and delta%18==0 and s>=12*K, "minimum inputs")
    for i in xs:
        require(s<=xs[i]<2*s and delta<=ds[i]<2*delta, "single octave")
    return xs, ds, F


def mechanical(K=384, last=7):
    xs, ds, F = ray(K,last)
    s, delta = xs[0], ds[0]
    tested = steps = hits = 0
    for k in range(1,K+1):
        for h in range(last+1):
            i = h-k
            A = F[h]-F[i]
            for j in range(-2,2):
                B = A+j
                if B<k:
                    continue
                div, mul = 1 << max(-j,0), 1 << max(j,0)
                center = xs[i]*mul//div
                inc, rem = divmod(ds[i]*mul,div)
                require(rem==0 and inc%(2 << B)==0 and inc%3==0, "rival ray stride")
                for z in range(center-3*k,center+3*k+2):
                    if z%2==0:
                        continue
                    # Exclude only if the relevant comparison holds on EVERY lift.
                    if 4*z>=3*s+1 and 4*inc>=3*delta:
                        if z%3 or (z>=2*s+1 and inc>=2*delta):
                            continue
                    if 3*z<s and 3*inc<=delta:
                        continue
                    tested += 1
                    b, n, drift = 0, z, inc
                    for t in range(k):
                        top = 3*n+1
                        e = v2(top)
                        if b+e+k-1-t>B:
                            # All input lifts have the same low remaining budget bits.
                            break
                        b += e
                        n = top >> e
                        drift = (3*drift) >> e
                        steps += 1
                        if 4*n<3*s+1 and 4*drift<=3*delta:
                            break
                    else:
                        if b==B and n==xs[h]:
                            require(drift==ds[h], "equal slopes")
                            # All possible boundary lift comparisons have been retained.
                            hits += 1
    require(hits==0, "new cheap source on the mechanical rays")
    return dict(max_depth=K, endpoints=last+1, windows=K*(last+1),
                candidate_rays=tested, completed_odd_steps=steps,
                unexcluded_mergers=hits)


if __name__ == "__main__":
    small = [label_control(tuple(map(int,w))) for w in
             ("11222","11122222","12112212212212121212212121221221212121222")]
    require(any(row["proper_partial"] for row in small), "no partial gcd case")
    print(json.dumps(dict(rational=small, large=high_control(), ordinary=mechanical()),
                     sort_keys=True, indent=2))
