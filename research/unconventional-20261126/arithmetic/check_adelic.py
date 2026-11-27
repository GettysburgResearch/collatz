"""Exact checks of finite interfaces. No finite run establishes an asymptotic bound."""
import hashlib
import json
from math import gcd


def check(condition, message):
    if not condition:
        raise ArithmeticError(message)


def clock(index, phase_num=0, phase_den=1):
    """floor(index log_2(3) + phase_num/phase_den), including negative dates."""
    check(0 <= phase_num < phase_den, "invalid intercept")
    if index == 0:
        return 0
    power = 3 ** (abs(index) * phase_den)
    top = power.bit_length() - 1
    # No positive power of three is a power of two.
    integral_numerator = top if index > 0 else -top - 1
    return (integral_numerator + phase_num) // phase_den


def v2(number):
    check(number != 0, "v2(0) not used in this check")
    return (number & -number).bit_length() - 1


def local_residues(phase, depth):
    num, den = phase
    p = {i: clock(i, num, den) for i in range(-depth, depth + 2)}
    binary_modulus = 2 ** (p[depth] + 1)
    ternary_modulus = 3 ** depth
    binary = -sum(2 ** p[i] * pow(3 ** (i + 1), -1, binary_modulus)
                  for i in range(depth + 1)) % binary_modulus
    ternary = sum(3 ** (j - 1) * pow(2 ** -p[-j], -1, ternary_modulus)
                  for j in range(1, depth + 1)) % ternary_modulus
    return p, binary, ternary


def forward(source):
    value = 3 * source + 1
    exponent = v2(value)
    return exponent, value >> exponent


def recover_cut(source, left, right, p):
    states = {0: source}
    for i in range(right):
        e, states[i + 1] = forward(states[i])
        check(e == p[i + 1] - p[i], "forward phase mismatch")
    for j in range(1, left + 1):
        e = p[-j + 1] - p[-j]
        numerator = (states[-j + 1] << e) - 1
        parent, rem = divmod(numerator, 3)
        check(rem == 0 and parent % 2 == 1, "reverse phase invalid")
        states[-j] = parent
        check(forward(parent) == (e, states[-j + 1]), "signed return")
    return states


def audit_cuts():
    depth = 20
    sampled = stressed = repeated_checks = 0
    max_total = 0
    phases = ((0, 1), (1, 3), (1, 2), (2, 3))
    for phase in phases:
        p, binary, ternary = local_residues(phase, depth)
        for source in range(1, 4096, 2):
            r = next((j for j in range(depth)
                      if (source - binary) % 2 ** (p[j + 1] + 1)), depth)
            l = next((j for j in range(depth)
                      if (source - ternary) % 3 ** (j + 1)), depth)
            states = recover_cut(source, l, r, p)
            if r < depth:
                check(forward(states[r])[0] != p[r + 1] - p[r], "right not maximal")
            if l < depth:
                e = p[-l] - p[-l - 1]
                check(((states[-l] << e) - 1) % 3 != 0, "left not maximal")
            sampled += 1
            max_total = max(max_total, l + r)
        for l in range(1, 13):
            for r in range(1, 13):
                m2, m3 = 2 ** (p[r] + 1), 3 ** l
                crt = (binary + m2 * ((ternary - binary) * pow(m2, -1, m3) % m3)) % (m2 * m3)
                source = crt + m2 * m3
                states = recover_cut(source, l, r, p)
                check(all(x > 0 for x in states.values()), "wanted a positive control")
                check(len(set(states.values())) == l + r + 1, "repeat in positive fixture")
                m = (l + r - 1) // 2
                if m:
                    known = {}
                    collision = False
                    for i in range(-l, r - m + 1):
                        word = tuple(p[k + 1] - p[k] for k in range(i, i + m))
                        if word in known:
                            prev = known[word]
                            modulus = 2 ** (sum(word) + 1)
                            check((states[i] - states[prev]) % modulus == 0, "separation")
                            check(abs(states[i] - states[prev]) >= modulus > 3 ** m,
                                  "distinct separation loss")
                            collision = True
                            repeated_checks += 1
                        else:
                            known[word] = i
                    check(collision, "missing repeated factor")
                stressed += 1
    return {"odd_source_and_intercept_pairs": sampled, "CRT_two_sided_windows": stressed,
            "sum_of_repeated_factor_checks": repeated_checks, "max_observed_total": max_total}


def audit_cycle(pair, modulus):
    P, Q, K, R = pair
    check(P * R - K * Q == 1 and 2 ** K < 3 ** R and 3 ** Q < 2 ** P, "bracket")
    a = (P - K) % modulus or modulus
    b = (-P) % modulus or modulus
    while gcd(a, b) != 1:
        b += modulus
    A, p = a * P + b * (P - K), a * Q + b * (Q - R)
    check(1 <= a <= modulus and 1 <= b <= modulus ** 2, "primitive lift")
    check(A % modulus == 0 and (p - 1) % modulus == 0, "target residues")
    check(gcd(A, p) == 1 and A * Q - p * P == b, "unimodularity")
    check(p > Q and (P - K) * p > (Q - R) * A, "slope")
    D = 2 ** A - 3 ** p
    check(D > 1 and gcd(D, 6) == 1, "denominator")
    primes = [ell for ell in range(5, 62) if all(ell % h for h in range(2, ell))
              and modulus % (ell - 1) == 0]
    check(all((D + 2) % ell == 0 for ell in primes), "finite prime avoidance")
    C = 0
    ternary_power = 1
    for j in range(p):
        e = ((j + 1) * A + p - 1) // p - (j * A + p - 1) // p
        C = (C << e) + ternary_power
        ternary_power *= 3
    check(gcd(C, D) == 1, "lost full denominator")
    u = C
    for j in range(p):
        next_num = 3 * u + D
        e = v2(next_num)
        check(e == (j + 1) * A // p - j * A // p, "cycle gap")
        u = next_num >> e
        check(C <= u < 2 * C, "minimum/width")
        check((u == C) == (j + 1 == p), "least period")
    clocks, u2, u3 = local_residues((0, 1), Q - 1)
    m2, m3 = 2 ** (clocks[Q - 1] + 1), 3 ** (Q - 1)
    check((C - D * u2) % m2 == 0 and (C - D * u3) % m3 == 0, "two-place shadow")
    for j in range(1, Q):
        check(j * A // p == clock(j), "floor section")
        check((j * A + p - 1) // p == -clock(-j), "ceiling section")
    check(Q * A // p != clock(Q), "first distinguishing denominator")
    digest = hashlib.sha256(D.to_bytes((D.bit_length() + 7) // 8, "big")).hexdigest()
    return {"upper_convergent": [P, Q], "preceding_lower": [K, R], "L": modulus,
            "clock": A, "least_odd_period": p, "denominator_bits": D.bit_length(),
            "denominator_sha256_unsigned_big_endian": digest, "certified_rough_primes": primes,
            "floor_of_real_minimum": C // D, "certified_past_and_future_gaps": Q - 1}


if __name__ == "__main__":
    models = [((65, 41, 19, 12), L) for L in (4, 12, 60)]
    models += [((485, 306, 84, 53), L) for L in (1, 12, 24)]
    print(json.dumps({"finite_cut_controls": audit_cuts(),
                      "rational_cycles": [audit_cycle(pair, mod) for pair, mod in models]},
                     indent=2))
