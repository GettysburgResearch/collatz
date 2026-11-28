"""Finite prime brackets. Every primality check is a Pocklington certificate."""
from math import gcd
import json


def check_prime(p, factor, exponent, witness):
    if factor not in (3, 5):  # these small factors are prime
        raise ValueError("unproved prime factor")
    F = factor**exponent
    if ((p-1) % F or F*F <= p or pow(witness,p-1,p) != 1 or
            gcd(pow(witness,(p-1)//factor,p)-1,p) != 1):
        raise ValueError(("invalid Pocklington certificate", p, witness))


def orbit(p, budget=10_000):
    sites = [p]
    while sites[-1] != 1 and len(sites) <= budget:
        x = sites[-1]
        sites.append(x//2 if x%2 == 0 else (3*x+1)//2)
    if sites[-1] != 1:
        raise ValueError(("hit-1 budget", p))
    return sites


def bracket():
    H,J,K,A = 56,2,1,200
    m_odd = 3**K*5**A
    period = 2**(H+J)*m_odd
    binary = (2**H*pow(3,-H-1,2**J)-1) % 2**(H+J)
    a = binary + 2**(H+J)*((1-binary)*pow(2**(H+J),-1,m_odd) % m_odd)
    rows = []
    for target, indices in [(41, (94_109,108_314,122_519)),
                            (61, (239_087,242_264,245_441)),
                            (7,  (235_917,242_602,249_287))]:
        primes = [a+period*i for i in indices]
        if not primes[0] < primes[1] < primes[2] or primes[0]+primes[2] != 2*primes[1]:
            raise ValueError("not a nonconstant prime arithmetic progression")
        trajectories = []
        checks = []
        for p, goal in zip(primes, (5,target,85)):
            witness = next(w for w in range(2,200) if
                           pow(w,p-1,p) == 1 and gcd(pow(w,(p-1)//5,p)-1,p)==1)
            check_prime(p,5,A,witness)
            sites = orbit(p)
            if goal not in sites or p%3**K != 1:
                raise ValueError(("target or class",p,goal))
            if [(x%2) for x in sites[:H+J]] != [1]*H+[0,1]:
                raise ValueError(("wrong word",p))
            checks.append(dict(primality_witness=witness, bits=p.bit_length(), target=goal,
                               first_target=sites.index(goal), first_one=len(sites)-1,
                               five_bit_deadline=5*p.bit_length()))
            trajectories.append(sites)
        if not all(checks[i]["first_one"] <= checks[i]["five_bit_deadline"] for i in (0,2)):
            raise ValueError("exterior deadline")
        center_fast = checks[1]["first_one"] <= checks[1]["five_bit_deadline"]
        if (target == 7) != center_fast:
            raise ValueError("wrong middle control")
        short_clock = (primes[0].bit_length()-1)//2
        pieces = [set(t[:short_clock+1]) for t in trajectories]
        if any(pieces[i] & pieces[j] for i in range(3) for j in range(i+1,3)):
            raise ValueError("early native meeting")
        rows.append(dict(input_source=27 if target==41 else target, target=target,
                         indices=indices, checks=checks, independent_no_meeting_through=short_clock,
                         midpoint_fast=center_fast))
    return dict(H=H,J=J,K=K, extra_power_of_five=A, rows=rows)


if __name__ == "__main__":
    print(json.dumps(bracket(), indent=2))
