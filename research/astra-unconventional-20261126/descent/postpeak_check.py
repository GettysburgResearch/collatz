"""Fixed-ordinary and modular replay of the signed postpeak adversary."""

import json
from fractions import Fraction


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def step(x):
    if isinstance(x, int):
        return (3*x+1)//2 if x%2 else x//2
    return (3*x+1)/2 if x.numerator%2 else x/2


def orbit(x, steps):
    values = {x}
    for _ in range(steps):
        x = step(x)
        values.add(x)
    return values


def check():
    k = 1
    m = 12*2**(18*k)-1
    h = 18*k+4
    j = (m-11)//162
    require(m==11+162*j and m.bit_length()==h, "hard source and physical scale")
    require(pow(3,m+1,2**h)==1 and pow(3,m+1,2**(h+1))!=1, "binary precision")
    power = 3**m
    full = orbit(power-1,h)
    for s in range(1,h):
        earlier = power//3**s-1
        require(not (full & orbit(earlier,h)), "literal asynchronous earlier meeting")
        signed = Fraction(1,3**(s+1))-1
        require(not ({Fraction(-2,3),Fraction(-1,3),Fraction(0)} & orbit(signed,2*h+4)),
                "signed peak intersection")
    require(3**(m-h)>2*6**h, "coefficient dominance")
    for d in range(1,7):
        modulus=3**d
        j_values={(2*(pow(2,18*i,27*modulus)-1)//27)%modulus for i in range(modulus)}
        require(len(j_values)==modulus, "ternary address exhaustion")
    return {"k":k, "m":m, "j":j, "deadline":h,
            "earlier_gaps_physically_replayed":list(range(1,h)),
            "earlier_gaps_excluded_by_size_from":h,
            "independent_clock_pairs_per_replayed_gap":(h+1)**2,
            "ternary_powers_checked":[1,2,3,4,5,6]}


if __name__=="__main__":
    print(json.dumps(check(),indent=2,sort_keys=True))
