"""
Verifies PR #149's rational-cycle barrier (constructing exact positive rational cycles
in Z_2 cap Z_3 and factoring their p >= 5 denominators D = 2^K - 3^L) and computes
continued-fraction convergents of log2(3) for effective CUBE-4 [PR #148].
"""
import json
import math
from fractions import Fraction


def cycle_rational(word_str: str):
    w = [int(c) for c in word_str]
    K = len(w)
    L = sum(w)
    C = 0
    pow3 = 3 ** L
    for i, bit in enumerate(w):
        if bit == 1:
            pow3 //= 3
            C += pow3 * (1 << i)
    D = (1 << K) - (3 ** L)
    q = Fraction(C, D)
    # Prime factorization of |D|
    tmp = abs(D)
    primes = []
    p = 2
    while p * p <= tmp:
        while tmp % p == 0:
            primes.append(p)
            tmp //= p
        p += 1
    if tmp > 1:
        primes.append(tmp)
    return {
        "word": word_str,
        "K": K,
        "L": L,
        "C": C,
        "D": D,
        "x0": str(q),
        "x0_float": round(float(q), 5),
        "in_Z2_cap_Z3": (math.gcd(abs(D), 6) == 1),
        "D_prime_factors": primes,
        "is_integer": (q.denominator == 1)
    }


def log2_3_convergents():
    cf = [1, 1, 1, 2, 2, 3, 1, 5, 2, 23, 2, 2]
    p_prev, p_curr = 1, cf[0]
    q_prev, q_curr = 0, 1
    log2_3 = math.log2(3)
    out = []
    for a in cf[1:]:
        p_next = a * p_curr + p_prev
        q_next = a * q_curr + q_prev
        p_prev, p_curr = p_curr, p_next
        q_prev, q_curr = q_curr, q_next
        diff = abs(p_curr * math.log(2) - q_curr * math.log(3))
        out.append({
            "K": p_curr,
            "L": q_curr,
            "K_over_L": round(p_curr / q_curr, 7),
            "abs_Klog2_minus_Llog3": f"{diff:.3e}",
            "sign_2K_minus_3L": "+" if p_curr > q_curr * log2_3 else "-"
        })
    return out


def main():
    words = ["10", "1110", "110", "11010", "11100", "11111000", "11110010", "1111110000"]
    out = {
        "rational_cycles": [cycle_rational(w) for w in words],
        "log2_3_convergents": log2_3_convergents()
    }
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
