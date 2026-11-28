"""Exact witnesses for the original Mersenne site, with source-exponent primality.

Large 2**p is represented by its affine expression and required residue.
The reference paths and the states in the constructive proof are ordinary.
"""
from math import gcd
import json


def first_hit(x, odd_cap, shortcut_cap):
    odds = clock = 0
    while x != 1 and odds < odd_cap and clock < shortcut_cap:
        twice = 3*x+1
        e = (twice & -twice).bit_length()-1
        x = twice >> e
        odds += 1
        clock += e
    return (odds,clock) if x == 1 else None


def minimum_reference(K, L):
    # Every reference of length <= L is below 2**L/3**K.
    limit = 2**L // 3**K
    best = L+1
    witnesses = []
    for w in range(1,limit+1,2):
        first = first_hit(w,K,L)
        if first is None:
            continue
        k,h = first
        length = h+2*(K-k)
        if length < best:
            witnesses = []
            best = length
        if length == best:
            witnesses.append(w)
    if best > L:
        raise ValueError("initial upper bound unproved")
    return best, witnesses, limit


def final_run(K,L):
    m = 0
    while 2**(L+m) >= 3**(K+m):
        m += 1
    return m


def verify_row(w,K,L,J,p,base,exhaust):
    if first_hit(w,K,L) != (K,L):
        raise ValueError(("reference trace",w))
    m = final_run(K,L)
    F = 3**(K-1)
    if ((p-1)%F or F*F <= p or pow(base,p-1,p)!=1 or
            gcd(pow(base,(p-1)//3,p)-1,p)!=1):
        raise ValueError(("Pocklington",p))
    if (p+1)%2**(J-2):
        raise ValueError(("dyadic exponent condition",p))
    modulus = 3**(K+m)
    displacement = (pow(2,p,modulus)-2)%modulus
    if displacement % 3**K:
        raise ValueError("missing input precision")
    u = displacement//3**K
    if (w+1+2**L*u)%3**m or u%3==0:
        raise ValueError("terminal odd-run or exact depth")
    result = dict(reference=w,K=K,reference_clock=L,extra_odd_run=m,
                  input_prime_exponent=p,prime_digits=len(str(p)),
                  primality_base=base,J=J,odd_cost=K+m,shortcut_cost=L+m,
                  residual_u_mod_3_to_m=u)
    if exhaust:
        minimum, roots, cutoff=minimum_reference(K,L)
        if minimum!=L or w not in roots:
            raise ValueError(("not an optimal reference",minimum,roots))
        result.update(minimum_proved=True, all_minimizers=roots,
                      checked_reference_cutoff=cutoff)
    else:
        result.update(minimum_proved=False)
    return result


if __name__ == "__main__":
    rows = [
        (27,41,70,11,685977866821782195406220287,2,True),
        (156159,141,241,15,
         1922907455821840273706387443029921972856266266204523817399735911449945003753984238362623,
         2,True),
        (63728127,357,592,17,
         950649762832521245991274269012877607271393242840065713661870504861713332692786041213186545645781109525513906800949598604639001044203344167963209142688281231718501822893631113872614952258588182937599,
         2,False),
    ]
    print(json.dumps([verify_row(*row) for row in rows], indent=2))
