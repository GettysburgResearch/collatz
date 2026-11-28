"""Finite checks of character support, primitive words and motif order transfer."""
from collections import Counter
import json
from math import gcd, prod

import sympy as sp

from check_prime_grade_denominators import carry, replay, require


def complete_denominator(length, odds):
    d = 2**length-3**len(odds)
    require(d > 0 and odds == sorted(set(odds)) and 0 <= odds[0] <= odds[-1] < length,
            "invalid positive native word")
    return d//gcd(d, carry(odds))


def address_classes(h, primes, counts):
    p = h*prod(primes)
    t = sp.Symbol("t")
    delta = [int(any(j%h == a and j%ell == 0 for a, ell in enumerate(primes)))
             for j in range(p)]
    require(all(delta != delta[u:]+delta[:u] for u in range(1, p)), "short address period")
    coefficients = sp.Poly.from_list([2**d for d in reversed(delta)], t, domain=sp.ZZ)
    circle = sp.Poly(t**p-1, t, domain=sp.ZZ)
    s = p - circle.gcd(coefficients).degree()
    require(s == h*(1+sum(ell-1 for ell in primes)), "wrong rational Fourier support")
    for n in (3, 5, 8):
        dates = [j*n+d for j, d in enumerate(delta)]
        length = p*n
        q = replay(length, dates, counts)
        require(q == complete_denominator(length, dates), "direct rational replay discrepancy")
        require(q <= (2**n+3)**s, "uniform denominator bound")
        template_factor = 2**n-3
        retained = template_factor//gcd(template_factor, sum(2**d for d in delta))
        require(q % retained == 0, "lost mandatory motif denominator")
    counts["address_families"] += 1
    return {"p": p, "cyclic_support": s}


def check_motif(length, model, shifts, counts):
    N = len(shifts)
    positions = [i*length+v+s for i,s in enumerate(shifts) for v in model]
    q = complete_denominator(N*length, positions)
    q0 = complete_denominator(length, model)
    loss = sum(2**(s-min(shifts)) for s in shifts)
    mandatory = q0//gcd(q0, loss)
    require(q % mandatory == 0, "bad translated-motif divisibility")
    # Small baseline modulus suffices to check the order implication using q's
    # mandatory divisor. This avoids factoring a much larger full denominator.
    order0 = 1 if q0 == 1 else int(sp.n_order(3, q0))
    order1 = 1 if mandatory == 1 else int(sp.n_order(3, mandatory))
    require(order0 % order1 == 0 and order0 <= gcd(q0, loss)*order1, "order-kernel bound")
    counts["motif_tests"] += 1
    counts["negative_shifts"] += min(shifts) < 0
    counts["nontrivial_losses"] += mandatory < q0


def main():
    counts = Counter()
    rows = [address_classes(h, primes, counts) for h, primes in
            ((2, (3, 5)), (3, (5, 7)), (5, (7, 11)))]
    for n in range(6, 14):
        for model in ([1], [1, 2], [1, 3], [1, 2, 3]):
            for shifts in ([0], [0, 1], [-1, 1, 0], [0, 1, 0, 1, 2]):
                check_motif(n, model, shifts, counts)
    require(counts["nontrivial_losses"] and counts["negative_shifts"], "unexercised motif branch")
    print(json.dumps({"counts":dict(counts), "address_data":rows}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
