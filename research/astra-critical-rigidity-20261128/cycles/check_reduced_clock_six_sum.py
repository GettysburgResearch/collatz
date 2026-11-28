"""Exact modular-inverse spatial grids on primitive multisheet rational cycles."""
import json
from fractions import Fraction
from math import gcd

from check_rational_six_sum import clock_word, floor_log2, native_cycle, require


def check(B, P, sheets, seed):
    E, q, y = native_cycle(clock_word(P, B, sheets, seed))
    p, A, minimum = len(y), E[-1], min(y)
    require(gcd(A, p) == sheets and A * P == p * B and max(y) < 3 * minimum,
            "genuine reduced clock and sub-three width")
    tau = pow(B, -1, P)
    k, rel = divmod(tau * B, P)
    require(rel == 1 and sheets > 1 and minimum > p*q, "inverse and large floor")
    require(pow(3, P*sheets, q) == pow(2, B*sheets, q) and
            all(pow(3, P*t, q) != pow(2, B*t, q) for t in range(1, sheets)),
            "complete denominator sees every sheet")

    def native(t):
        laps, i = divmod(t, p)
        return laps*A + E[i]

    def floor(t):
        return native(t) + floor_log2(4*y[t % p], 7*minimum)

    def label(t, j):
        pos = t+j*tau
        u = native(pos)-floor(t)-k*j
        return Fraction(y[pos % p] << max(u, 0), 1 << max(-u, 0))

    anchor = min(range(p), key=lambda t: label(t, 0))
    fundamental = [label(anchor, j) for j in range(P)]
    require(all(z.denominator == 1 for z in fundamental), "full q-scaled spatial grid")
    edges = 0
    interior = 0
    width = 4
    for r in range(P):
        t = anchor + r*tau
        require((t*B-anchor*B) % P == r, "one representative of each reduced rank")
        for j in range(width+1):
            pos = t+j*tau
            u = native(pos)-floor(t)-k*j
            require(u in (0, 1), "genuine unwrapped tags")
            winding = floor(t+1)-floor(t)
            require(winding in (1, 2) and
                    (1 << winding)*label(t+1, j) == 3*label(t, j)+q*(1 << u),
                    "true chronological affine law")
            require(label(t-p, j) == label(t, j) == label(t+p, j),
                    "one full physical return")
            edges += 1
        if r+width < P and floor(t) == floor(anchor)+k*r:
            require(all(label(t, j)==fundamental[r+j] for j in range(width+1)),
                    "exact interior grid with physical sheets")
            interior += 1
    # The de-meaned drift identity in multiplicative form.  Raising to P
    # removes the P-th root in the correction ratio; cancel 2^(kj+j/P)
    # first to avoid allocating integers whose sizes scale with sample laps.
    for left in (-p-1, anchor, p+1):
        for j in (-2*P-1, -P, -1, 0, 1, P//2, P+1, 3*P+1):
            right = left+j*tau
            exponent = P*(native(right)-native(left)-k*j)-j
            reduced = P*(E[right % p]-E[left % p])-B*((right % p)-(left % p))
            require(exponent == reduced, "full-lap cancellation in drift identity")
            ratio=Fraction(y[right % p], y[left % p])
            require(ratio > 0 and gcd(y[left % p],q)==gcd(y[right % p],q)==1,
                    "physical reduced numerator factors")
    prior=(anchor-(2*P+1)*tau)//p
    final=(anchor+(3*P+1)*tau)//p
    require(interior >= P//2 and final-prior > 10, "genuinely repeated lap crossings")
    return dict(B=B, P=P, p=p, A=A, sheets=sheets, full_denominator_bits=q.bit_length(),
                floor_over_period_millionths=minimum*10**6//(q*p), native_inverse_stride=tau,
                k=k, period_span_in_signed_samples=final-prior, exact_interior_starts=interior,
                full_period_grid_edge_tests=edges)


if __name__ == "__main__":
    cases=[(65,41,2,1),(65,41,3,2),(485,306,2,1),(485,306,3,2)]
    print(json.dumps([check(*case) for case in cases],indent=2))
