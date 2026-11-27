"""Exact factor, resultant and fully closed generalized-orbit controls."""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import gcd, isqrt, prod
import json

import sympy as sp


X = sp.Symbol("X")


def require(condition, message):
    if not condition:
        raise ValueError(message)


def rank_data(h, letters):
    p = len(letters)
    D = 2**h-3**p
    a = pow(p, -1, h)
    b = (1-p*a)//h
    u = pow(2, a, D)*pow(3, b, D) % D
    require(pow(u, p, D) == 2 % D and pow(u, h, D) == 3 % D, "Bezout unit")
    F = sp.Poly.from_list(letters, X, domain=sp.ZZ)
    carry = sum(3**(p-1-j)*2**(j*h//p)*letters[j*h%p] for j in range(p))
    require((carry-int(F.eval(u))*pow(u, (h-1)*(p-1), D)) % D == 0, "chronological carry")
    return D, u, F, carry


def relations(p, h, t):
    R = 2*(isqrt(t)+1)+isqrt(p)+1
    B = (6*p+R-1)//R
    require((R+1)**2*(B+1) > 3*p*R+t*B+1, "pigeonhole")
    seen, choices = {}, {}
    for i, j, k in product(range(R+1), range(R+1), range(B+1)):
        value = i*p+j*h+k*t
        if value in seen:
            a, b, c = seen[value]
            shift = (i-a, j-b, k-c)
            choices.setdefault(b != j, shift)
            if len(choices) == 2:
                break
        else:
            seen[value] = (i, j, k)
    require(choices, "missing short relation")
    return R, B, choices


def cyclotomic_order(poly):
    if not poly.is_cyclotomic:
        return None
    # phi(v) >= sqrt(v/2), by looking separately at the prime 2.
    for v in range(1, 2*poly.degree()**2+1):
        if sp.totient(v) == poly.degree() and sp.Poly(sp.cyclotomic_poly(v, X), X) == poly:
            return v
    raise ValueError("cyclotomic order")


def factor_ledger(h, letters):
    p = len(letters)
    D, u, F, carry = rank_data(h, letters)
    content, factors = F.factor_list()
    require(gcd(int(content), D) == 1, "content and D")
    ledger, rows = 1, []
    for G, mult in factors:
        t = gcd(*(j for (j,), _ in G.terms() if j))
        H = sp.Poly.from_dict({(j//t,): a for (j,), a in G.terms()}, X, domain=sp.ZZ)
        g = gcd(D, int(G.eval(u)))
        require(H.compose(sp.Poly(X**t, X)) == G and H.is_irreducible, "compression")
        require(int(H.LC()*H.TC()) % 3 != 0, "endpoint reduction")
        ledger *= g**mult
        row = {"degree": int(G.degree()), "t": t, "compressed_degree": int(H.degree()),
               "multiplicity": mult, "gcd": g}
        v = cyclotomic_order(G)
        if v is not None:
            require((pow(u, v, g)-1) % g == 0 and g <= 6**isqrt(v), "cyclotomic divisor")
            row["cyclotomic_order"] = v
        else:
            R, B, choices = relations(p, h, t)
            row["witnesses"] = []
            for has_j, (i, j, k) in sorted(choices.items()):
                require(i*p+j*h+k*t == 0, "weighted collision")
                if has_j:
                    P = sp.Poly(2**max(i, 0)*3**max(j, 0)*X**max(k, 0)
                                - 2**max(-i, 0)*3**max(-j, 0)*X**max(-k, 0), X)
                    require(len(P.set_modulus(3).terms()) == 1, "single surviving term")
                else:
                    common = gcd(p, t)
                    P = sp.Poly(X**(p//common)-2**(t//common), X)
                    require(P.is_irreducible, "positive-root binomial")
                res = abs(int(H.resultant(P)))
                require(res > 0 and res % g == 0, "whole gcd in nonzero resultant")
                require(int(P.eval(pow(u, t, D))) % D == 0, "common modular root")
                require(P.degree() <= B and sum(map(abs, P.all_coeffs())) <= 2*6**R, "size")
                upper = (2*6**R)**H.degree()*sum(map(abs, H.all_coeffs()))**B
                require(res <= upper, "integer version of resultant estimate")
                row["witnesses"].append({"relation": [i, j, k], "abs_resultant": res})
        rows.append(row)
    full_gcd = gcd(D, carry)
    require(ledger % full_gcd == 0 and gcd(D, int(F.eval(u))) == full_gcd, "divisor ledger")
    return {"p": p, "h": h, "D": D, "u": u, "full_gcd": full_gcd,
            "denominator": D//full_gcd, "factors": rows}


def odd_step(y, d):
    z = 3*y+d
    a = (z & -z).bit_length()-1
    return z >> a, a


def basin_census(d, odd):
    S, p = min(odd), len(odd)
    require(odd[0] == S and len(set(odd)) == p, "cyclic minimum")
    h, physical = 0, []
    for j, y in enumerate(odd):
        nxt, a = odd_step(y, d)
        require(nxt == odd[(j+1)%p] and a in (1, 2) and gcd(y, d) == 1, "odd edges")
        physical.append(y)
        if a == 2:
            physical.append(2*nxt)
        h += a

    def normalize(y, base):
        z, k = Fraction(y), 0
        while z >= base*S:
            z, k = z/base, k+1
        require(S <= z < base*S, "octave or triple")
        return z, k

    dyadic = sorted((normalize(y, 2), j) for j, y in enumerate(odd))
    require(len({z for ((z, _), _) in dyadic}) == p and
            all((dyadic[(r+h)%p][1]-dyadic[r][1]) % p == 1 for r in range(p)), "dyadic order")
    ks = [k for ((_, k), _) in dyadic]
    ternary = sorted((normalize(y, 3)[0], j) for j, y in enumerate(physical))
    require(len({z for z, _ in ternary}) == h and
            all((ternary[(r-p)%h][1]-ternary[r][1]) % h == 1 for r in range(h)), "ternary order")
    letters = [4 >> k for k in ks]
    D, _, _, carry = rank_data(h, letters)
    require(Fraction(carry, D) == Fraction(4*S, d), "actual rational denominator")
    require(3 <= len(set(odd)) and (2*S+d) % 3 == 0, "least disagreement candidate")
    Q = (2*S+d)//3
    basin, cycles = {}, {}

    def close(start):
        path, local, y = [], {}, start
        while y not in basin and y not in local:
            local[y] = len(path)
            path.append(y)
            y = odd_step(y, d)[0]
        if y in basin:
            rep = basin[y]
        else:
            cycle = path[local[y]:]
            rep = min(cycle)
            cycles[rep] = cycle
        for value in path:
            basin[value] = rep
        return rep

    small = range(1, S, 2)
    multiples = range(3, 2*S+d, 6)
    require(all(close(y) != S for y in small), "all smaller odd numerators")
    require(all(close(y) != S for y in multiples), "all smaller odd multiples of three")
    require(close(S) == S and close(3*Q) == S and close(Q) != S, "least numerators")
    ref, q_class = close(1), close(Q)
    if d == 13:
        require(all((close(x) == ref) == (close(3*x) == ref) for x in (1, 3, 5)) and
                close(7) == ref and close(21) == 131, "earlier target-one disagreement")
    for y, rep in basin.items():
        require(basin[odd_step(y, d)[0]] == rep, "every saved forward edge closes")
    for rep, cycle in cycles.items():
        require(rep == min(cycle) and all(odd_step(y, d)[0] == cycle[(j+1)%len(cycle)]
                for j, y in enumerate(cycle)), "every terminal cycle closes")

    return {"denominator": d, "p": p, "h": h, "odd_numerators": odd, "S": S, "Q": Q,
            "least_triple_in_component": 3*Q, "cycle_min_for_Q": q_class,
            "cycle_min_for_one": ref, "wide_ratio": str(Fraction(max(odd), S)), "bands": ks,
            "hamming_by_rank_shift": [sum(k != ks[(r+t)%p] for r, k in enumerate(ks))
                                      for t in range(p)],
            "smaller_odd_starts": len(small), "smaller_triples": len(multiples),
            "closed_nodes": len(basin), "largest_numerator_checked": max(basin),
            "cycle_periods_by_min": {str(rep): len(cycle) for rep, cycle in sorted(cycles.items())}}


def main():
    census = [basin_census(1631, [10865, 17113, 26485, 40543, 30815, 23519, 18047, 13943]),
              basin_census(13, [283, 431, 653, 493, 373])]
    require(census[0]["cycle_min_for_Q"] == 6625 and census[1]["cycle_min_for_Q"] == 1,
            "targets of the two controls")
    exhaustive, by_gcd = 0, Counter()
    for tail in product((1, 2, 4), repeat=4):
        row = factor_ledger(8, [4, *tail])
        by_gcd[row["full_gcd"]] += 1
        exhaustive += 1
    require(by_gcd == {1: 74, 13: 7}, "all length-five rank words")
    examples = [("full_divisor_unphysical", 8, [4, 1, 2, 2, 2]),
                ("dilation", 17, [2]*5+[1]*5),
                ("repeated_cyclotomic", 8, [1, 2, 2, 2, 1]),
                ("repeated_prime_divisor", 33, [4]+[2]*13+[1, 2, 1, 4, 2]),
                ("wide_physical", 13, [4 >> k for k in census[0]["bands"]])]
    ledgers = {name: factor_ledger(h, word) for name, h, word in examples}
    require(ledgers["repeated_prime_divisor"]["full_gcd"] == 25*307 and
            ledgers["dilation"]["full_gcd"] == 7, "repeated prime and diluted gcd")
    return {"sympy": sp.__version__, "length_five_words": exhaustive,
            "gcd_histogram": dict(sorted(by_gcd.items())),
            "factor_controls": ledgers,
            "rational_basin_controls": census}


if __name__ == "__main__":
    print(json.dumps(main(), indent=2))
