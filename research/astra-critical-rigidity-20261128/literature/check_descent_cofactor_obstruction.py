"""Construct the CRT witnesses and replay every prescribed parity on reduced positive rationals."""
from collections import Counter
from itertools import groupby
import json
import math


def require(ok, message):
    if not ok:
        raise ArithmeticError(message)


def combine(residue, modulus, value, other):
    return residue + modulus * ((value - residue) * pow(modulus, -1, other) % other), modulus * other


def spread(duration, count, reverse=False):
    sizes = [duration * (i + 1) // count - duration * i // count for i in range(count)]
    if reverse:
        sizes.reverse()
    return "".join("0" * (size - 1) + "1" for size in sizes)


def replay(N, q, word, primes, stats):
    Q = q * 3**N
    D, k = len(word), word.count("1")
    require(k <= N and (k < N or word.endswith("1")), "landing convention")
    cutoff = 30 * math.prod(2*p for p in primes if p not in (2,3))
    require(Q >= cutoff * 2**D * (k+1)**len(primes), "available precision")
    carry, grade, marks = 0, 0, []
    for t, bit in enumerate(word):
        if bit == "1":
            marks.append((t, grade, carry))
            carry = 3*carry + 2**t
            grade += 1
    first = -Q * carry * pow(3**k, -1, 2**D) % 2**D
    residue, modulus = 0, 1
    for p in (3, 5) if q % 5 == 0 else (3,):
        z = next(i for i in range(p) if (first + 2**D*i) % p)
        residue, modulus = combine(residue, modulus, z, p)
    for p in sorted(set(primes) - {2, 3}):
        if q % p == 0:
            continue
        power = p
        while power < 2*(k+1):
            power *= p
        forbidden = set()
        for t, g, local_carry in marks:
            raw = first + q*3**(N-g)*local_carry
            require(raw % 2**t == 0, "cylinder parity")
            forbidden.add(-(raw >> t)*pow(2**(D-t), -1, power) % power)
        z = next(i for i in range(power) if i not in forbidden)
        residue, modulus = combine(residue, modulus, z, power)
    initial = first + 2**D * residue
    period = 2**D*modulus
    low = (Q+1)//2
    b = initial + ((low-initial+period-1)//period)*period
    require(low <= b <= Q and math.gcd(b,Q) == 1, "complete reduced source")
    R = max((len(list(values)) for bit,values in groupby(word) if bit=="0"), default=0)
    removal = math.prod(2*p*(k+1) for p in primes if p not in (2,3))
    u, h = b, N
    for t, bit in enumerate(word):
        require((u & 1) == int(bit), "physical word")
        require(math.gcd(u,q*3**h)==1, "complete current denominator")
        if bit == "1":
            cofactor = u
            for p in primes:
                while cofactor % p == 0:
                    cofactor //= p
            require(cofactor * (1 << (R+1)) * removal >= q*3**h, "marked cofactor inequality")
            u = (u+q*3**(h-1))//2
            h -= 1
            stats["marked_full_cofactors"] += 1
        else:
            u //= 2
    require(h==N-k and math.gcd(u, q*3**h)==1, "reduced endpoint")
    stats["actual_sources"] += 1
    stats["actual_steps"] += D
    stats["complete_paths"] += int(k==N)
    stats["unit_residual_denominator_sources"] += int(q==1)
    stats["largest_residual_denominator_bits"] = max(stats["largest_residual_denominator_bits"],q.bit_length())


def main():
    stats = Counter()
    for primes in ((2,3), (2,3,5,7), (2,3,5,7,11)):
        for N in (96, 128, 195, 256):
            k = math.isqrt(N)
            D = N
            for word in (spread(D,k), spread(D,k,True), "0"*(D-k)+"1"*k, "1"*k+"0"*(D-k), "0"*D):
                replay(N,1,word,primes,stats)
        for N in (3,6,10):
            for D in (N, 4*N+5, 8*N+3):
                for word in (spread(D,N), "0"*(D-N)+"1"*N):
                    q = 5**((D+N+40)**2)
                    replay(N,q,word,primes,stats)
    print(json.dumps(dict(sorted(stats.items())), indent=2))


if __name__=="__main__":
    main()
