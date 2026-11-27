"""Rational return-word and additive-energy certificates for binary clock corridors."""
from fractions import Fraction as F
from math import comb
import json


def check(condition, message):
    if not condition:
        raise ValueError(message)


def log_unit(x, terms=30):
    """Enclose log(x) for 1 <= x <= 3 using positive atanh terms."""
    check(1 <= x <= 3, "log reduction")
    t = (x - 1) / (x + 1)
    lo = 2 * sum(t ** (2*j + 1) / (2*j + 1) for j in range(terms))
    hi = lo + 2*t ** (2*terms + 1) / ((2*terms + 1)*(1-t*t))
    return lo, hi


LN2 = log_unit(F(2))
LN3 = log_unit(F(3))
ALPHA = F(58496250072115, 10**14), F(58496250072116, 10**14)
WINDOW = F(9853, 10000), F(9854, 10000)
STEPS = 147


def log3_bounds(x):
    """Exact rational bounds for positive log_3(x), allowing large rational x."""
    check(x >= 1, "positive log")
    k = x.numerator.bit_length() - x.denominator.bit_length()
    if F(2)**k > x:
        k -= 1
    rlo, rhi = log_unit(x / F(2)**k)
    return (k*LN2[0] + rlo)/LN3[1], (k*LN2[1] + rhi)/LN3[0]


def cuts(a, w):
    entries = [(w, ("left",)), (F(1), ("right",))]
    for j in range(1, STEPS+1):
        for origin, name in [(F(0), "seam"), (w, "return")]:
            raw = origin - j*a
            floor = raw.numerator // raw.denominator
            value = raw - floor
            if w < value < 1:
                entries.append((value, (name, j, floor)))
    return sorted(entries)


def arrangement_signature(a, w):
    # Keep the complete circle order to certify no cut enters/leaves the window
    # between the four corners. All labels carry their unwrapped integer.
    entries = [(F(0), ("zero",)), (w, ("left",)), (F(1), ("right",))]
    for j in range(1, STEPS+1):
        for origin, name in [(F(0), "seam"), (w, "return")]:
            raw = origin - j*a
            floor = raw.numerator // raw.denominator
            entries.append((raw-floor, (name, j, floor)))
    entries.sort()
    check(len({x for x, _ in entries}) == len(entries), "coincident cuts")
    return tuple(label for _, label in entries)


def first_word(a, w, f):
    answer = []
    for _ in range(STEPS):
        f += a
        up = f >= 1
        f -= int(up)
        answer.append(up)
        if f > w:
            return tuple(answer)
    raise ValueError("uncovered open return")


def catalogue(a, w):
    points = [x for x, _ in cuts(a, w)]
    durations = {}
    for x, y in zip(points, points[1:]):
        word = first_word(a, w, (x+y)/2)
        durations[word] = durations.get(word, F(0)) + y-x
    ell = 1-w
    u, v = 53*a-31, 55-94*a
    expected = {53: ell-u, 94: ell-v, 147: u+v-ell}
    check(len(durations) == len(expected), "different words of equal length")
    check({len(k): v for k, v in durations.items()} == expected, "return frequencies")
    return {len(word): word for word in durations}


def advance(k, word, counts):
    for rising in word:
        if rising:
            counts = [sum(counts[j]*comb(k-j,l-j)**2 for j in range(l+1))
                      for l in range(k+1)]
        else:
            counts = [sum(counts[j]*comb(j,l)**2 for j in range(l,k+1))
                      for l in range(k+1)]
    return counts


def scaled_bounds(interval, scale):
    lo, hi = interval
    return [lo.numerator * scale // lo.denominator,
            -((-hi.numerator * scale)//hi.denominator)]


def run():
    check(ALPHA[0] < LN3[0]/LN2[1]-1 <= LN3[1]/LN2[0]-1 < ALPHA[1],
          "logarithm ratio enclosure")
    corners = [(a,w) for a in ALPHA for w in WINDOW]
    signatures = [arrangement_signature(a,w) for a,w in corners]
    # Global cuts away from the return interval may change their order. Every
    # pair touching the return interval is tested with its position relative
    # to both ends at each corner, using its unwrapped affine formula.
    def relevant_order(sig):
        left, right = sig.index(("left",)), sig.index(("right",))
        return sig[left:right+1], frozenset(sig[:left])
    check(len({relevant_order(sig) for sig in signatures}) == 1, "return cuts crossed")
    check(len({frozenset(sig) for sig in signatures}) == 1, "integer label changed")
    words = catalogue(*corners[0])
    for a,w in corners[1:]:
        check(catalogue(a,w) == words, "return catalogue changed")
    energies = {n: advance(2, w, [1,0,0])[0] for n,w in words.items()}
    log_energies = {n: log3_bounds(F(e)) for n,e in energies.items()}

    def rate(w):
        bounds = []
        for a in ALPHA:
            ell = 1-w
            u, v = 53*a-31, 55-94*a
            weights = {53:ell-u, 94:ell-v, 147:u+v-ell}
            check(min(weights.values()) > 0, "empty return type")
            bounds.append([sum(weights[n]*log_energies[n][i] for n in weights)
                           for i in range(2)])
        return min(x[0] for x in bounds), max(x[1] for x in bounds)

    root_lo, root_hi = F(98534327,10**8), F(98534329,10**8)
    check(rate(root_lo)[1] < 1 < rate(root_hi)[0], "critical cap bracket")
    # Numerical constants are input rational barriers, not fitted arithmetic
    # decisions. Integer matrix products and certified logs check each one.
    tests = [
        (1, [1000000,620204], F(42,100), None),
        (2, [1000000,1866354,321361], F(1005,1000), F(10054,10000)),
        (3, [1000000,3862925,1912064,150141], F(16751,10000), None),
    ]
    for k, v, lower, upper in tests:
        for n, word in words.items():
            for new, old in zip(advance(k,word,v),v):
                lo, hi = log3_bounds(F(new,old))
                check(lo > lower*n and (upper is None or hi < upper*n),
                      f"transfer barrier, moment {2*k}, length {n}")
    check(F(16751,10000)-F(10054,10000)>F(2,3), "log-convex slope")
    return {
        "alpha_bracket": list(map(str, ALPHA)),
        "cap_bracket": list(map(str, WINDOW)),
        "return_word_energies": {str(n): energies[n] for n in sorted(energies)},
        "critical_fractional_cap_bracket": [str(root_lo),str(root_hi)],
        "forced_log3_rates_scaled_1e9": {
            str(w):scaled_bounds(rate(w), 10**9) for w in (*WINDOW,root_lo,root_hi)
        },
        "unforced_comparison_vectors": [
            {"copies_per_side":k, "vector":v, "lower":str(lo),
             "upper":None if hi is None else str(hi)} for k,v,lo,hi in tests
        ],
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
