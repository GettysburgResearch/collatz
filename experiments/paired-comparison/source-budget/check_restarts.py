#!/usr/bin/env python3
"""Scoped independent raw-path and exact-rational checks for RSA-001--004."""
from fractions import Fraction
import json

def need(condition, diagnostic):
    if not condition:
        raise RuntimeError(diagnostic)

def T(n):
    need(type(n) is int and n > 0, 'Original line 9: type(n) is int and n > 0')
    return (3 * n + 1) // 2 if n % 2 else n // 2

def path(n, steps):
    values = [n]
    for _ in range(steps):
        values.append(T(values[-1]))
    return values

def word(values):
    return ''.join((str(n % 2) for n in values[:-1]))

def v2(n):
    need(n > 0, 'Original line 25: n > 0')
    return (n & -n).bit_length() - 1

def canonical(C):
    q = v2(C)
    k, epsilon = divmod(q, 2)
    v = C >> q
    return (k, epsilon, 3 ** (k + 1) * v)

def check_stage(C):
    k, epsilon, M = canonical(C)
    if epsilon:
        upper = path(9 * C + 2, 2 * k + 2)
        lower = path(M, 1)
        need(word(upper) == '01' * k + '00', "Original line 41: word(upper) == '01'*k+'00'")
        need(word(lower) == '1', "Original line 42: word(lower) == '1'")
        need(upper[-1] == lower[-1], 'Original line 43: upper[-1] == lower[-1]')
        return None
    s = v2(M + 1)
    u = M + 1 >> s
    Q = 3 ** s * u
    upper = path(9 * C + 2, 2 * k + s + 2)
    lower = path(M, s + 2)
    need(upper[2 * k] == 3 * M + 2, 'Original line 50: upper[2*k] == 3*M+2')
    if Q % 4 == 3:
        need(word(upper) == '01' * k + '1' * s + '00', "Original line 52: word(upper) == '01'*k+'1'*s+'00'")
        need(word(lower) == '1' * s + '01', "Original line 53: word(lower) == '1'*s+'01'")
        need(upper[-1] == lower[-1] == (3 * Q - 1) // 4, 'Original line 54: upper[-1] == lower[-1] == (3*Q-1)//4')
        return None
    need(Q % 4 == 1, 'Original line 56: Q % 4 == 1')
    D = (Q - 1) // 4
    need(D > 0, 'Original line 58: D > 0')
    need(word(upper) == '01' * k + '1' * s + '01', "Original line 59: word(upper) == '01'*k+'1'*s+'01'")
    need(word(lower) == '1' * s + '00', "Original line 60: word(lower) == '1'*s+'00'")
    need(upper[-1] == 9 * D + 2, 'Original line 61: upper[-1] == 9*D+2')
    need(lower[-1] == D, 'Original line 62: lower[-1] == D')
    return (D, M, s)

def check_ledger(C, max_stages):
    _, _, M0 = canonical(C)
    P = Fraction(1)
    normalized = Fraction(M0 + 1)
    count = 0
    for _ in range(max_stages):
        result = check_stage(C)
        if result is None:
            break
        D, M, s = result
        k1, epsilon1, M1 = canonical(D)
        a = Fraction(3 ** (s + 1 + k1), 2 ** (s + 2 + 2 * k1 + epsilon1))
        b = 1 - Fraction(3 ** (k1 + 1), 2 ** (2 * k1 + epsilon1 + 2))
        need(Fraction(1, 4) <= b < 1, 'Original line 79: Fraction(1, 4) <= b < 1')
        need(M1 + 1 == a * (M + 1) + b, 'Original line 80: M1+1 == a*(M+1)+b')
        if 3 ** (s + k1) <= 2 ** (s + 2 * k1 + epsilon1):
            need(0 <= 4 * (M1 - 3) < 3 * (M - 3), 'Original line 82: 0 <= 4*(M1-3) < 3*(M-3)')
            need(M1 < M, 'Original line 83: M1 < M')
        P *= a
        previous = normalized
        normalized += b / P
        need(normalized > previous, 'Original line 87: normalized > previous')
        need(M1 + 1 == P * normalized, 'Original line 88: M1+1 == P*normalized')
        if not epsilon1 and k1 == 0 and (canonical(C)[0] == 0):
            need(8 * (D + 1) >= 9 * (C + 1), 'Original line 90: 8*(D+1) >= 9*(C+1)')
        C = D
        count += 1
    return count

def check_guarded_normalizer(C):
    _, _, M0 = canonical(C)
    initial_M = M0
    total_steps = 0
    accepted = 0
    while True:
        k0, epsilon0, M0 = canonical(C)
        need(M0 <= initial_M, 'Original line 103: M0 <= initial_M')
        if M0 == 3:
            need(C in (1, 2), 'Original line 105: C in (1, 2)')
            core_steps = 6 if C == 1 else 2
            core = path(9 * C + 2, core_steps)
            need(word(core) == ('110100' if C == 1 else '00'), "Original line 108: word(core) == ('110100' if C == 1 else '00')")
            need(core[-1] == T(3) == 5, 'Original line 109: core[-1] == T(3) == 5')
            return (accepted, total_steps + core_steps, 'MERGE')
        result = check_stage(C)
        if result is None:
            if epsilon0:
                total_steps += 2 * k0 + 2
            else:
                total_steps += 2 * k0 + v2(M0 + 1) + 2
            return (accepted, total_steps, 'MERGE')
        D, M, s = result
        need(M == M0, 'Original line 119: M == M0')
        total_steps += 2 * k0 + s + 2
        k1, epsilon1, M1 = canonical(D)
        if 3 ** (s + k1) > 2 ** (s + 2 * k1 + epsilon1):
            return (accepted, total_steps, 'FAILED_DEBT_GUARD')
        need(0 <= 4 * (M1 - 3) < 3 * (M0 - 3), 'Original line 124: 0 <= 4*(M1-3) < 3*(M0-3)')
        need(M1 < M0, 'Original line 125: M1 < M0')
        C = D
        accepted += 1

def check_unbounded_guard_family(s, epsilon):
    modulus = 2 ** (4 * s + epsilon + 3)
    a = (1 + 2 ** (4 * s + epsilon + 2)) * pow(3 ** s, -1, modulus) % modulus
    b = 7 * pow(2 ** s, -1, 9) % 9
    u = a + modulus * ((b - a) * pow(modulus, -1, 9) % 9)
    need(u > 0 and u % 2 == 1, 'Original line 135: u > 0 and u % 2 == 1')
    M = 2 ** s * u - 1
    C = M // 3
    N = (16 * C + 1) // 3
    D = (3 ** s * u - 1) // 4
    need(3 * C == M, 'Original line 140: 3*C == M')
    need(C % 3 == 2, 'Original line 141: C % 3 == 2')
    need(3 * N == 16 * C + 1, 'Original line 142: 3*N == 16*C+1')
    need(M < N, 'Original line 143: M < N')
    need(v2(N + 1) == 2, 'Original line 144: v2(N+1) == 2')
    need(v2(M + 1) == s, 'Original line 145: v2(M+1) == s')
    need(v2(D) == 4 * s + epsilon, 'Original line 146: v2(D) == 4*s+epsilon')
    k1, epsilon1, M1 = canonical(D)
    need((k1, epsilon1) == (2 * s, epsilon), 'Original line 148: (k1, epsilon1) == (2*s, epsilon)')
    need(3 ** (s + k1) <= 2 ** (s + 2 * k1 + epsilon1), 'Original line 149: 3**(s+k1) <= 2**(s+2*k1+epsilon1)')
    need(0 <= 4 * (M1 - 3) < 3 * (M - 3), 'Original line 150: 0 <= 4*(M1-3) < 3*(M-3)')
    need(M1 < M < N, 'Original line 151: M1 < M < N')
    upper = path(N, s + 6)
    lower = path(M, s + 2)
    need(word(upper) == '1101' + '1' * s + '01', "Original line 154: word(upper) == '1101'+'1'*s+'01'")
    need(upper[4] == 9 * C + 2, 'Original line 155: upper[4] == 9*C+2')
    need(upper[-1] == 9 * D + 2, 'Original line 156: upper[-1] == 9*D+2')
    need(lower[-1] == D, 'Original line 157: lower[-1] == D')
    if epsilon:
        whole = path(N, 5 * s + 8)
        need(word(whole) == '1101' + '1' * s + '01' + '01' * (2 * s) + '00', "Original line 160: word(whole) == '1101'+'1'*s+'01'+'01'*(2*s)+'00'")
        need(whole[-1] == T(M1), 'Original line 161: whole[-1] == T(M1)')
    return N.bit_length()

def check_power_family(j):
    s = 6 * j + 2
    need(j >= 1, 'Original line 167: j >= 1')
    N = 13 * (2 ** (s + 4) - 1) // 9
    C = (13 * 2 ** s - 1) // 3
    M0 = 13 * 2 ** s - 1
    D = (13 * 3 ** s - 1) // 4
    M1 = 3 * D
    need(9 * N == 13 * (2 ** (s + 4) - 1), 'Original line 173: 9*N == 13*(2**(s+4)-1)')
    need(3 * C == M0, 'Original line 174: 3*C == M0')
    need(C % 2 == D % 2 == 1, 'Original line 175: C % 2 == D % 2 == 1')
    need(C % 3 == 2, 'Original line 176: C % 3 == 2')
    need(v2(N + 1) == 2, 'Original line 177: v2(N+1) == 2')
    need(v2(M0 + 1) == s, 'Original line 178: v2(M0+1) == s')
    need(M0 < N < M1, 'Original line 179: M0 < N < M1')
    upper = path(N, s + 6)
    lower = path(M0, s + 2)
    need(word(upper) == '1101' + '1' * s + '01', "Original line 182: word(upper) == '1101'+'1'*s+'01'")
    need(word(lower) == '1' * s + '00', "Original line 183: word(lower) == '1'*s+'00'")
    need(upper[4] == 9 * C + 2, 'Original line 184: upper[4] == 9*C+2')
    need(upper[-1] == 9 * D + 2, 'Original line 185: upper[-1] == 9*D+2')
    need(lower[-1] == D, 'Original line 186: lower[-1] == D')
    need(min(upper[1:]) > N, 'Original line 187: min(upper[1:]) > N')
    need(canonical(D) == (0, 0, M1), 'Original line 188: canonical(D) == (0, 0, M1)')
    need(Fraction(9 * N + 13, 208) == 2 ** s, 'Original line 190: Fraction(9*N+13, 208) == 2**s')
    need(Fraction(M1, 1) + Fraction(3, 4) == Fraction(39, 4) * 3 ** s, 'Original line 191: Fraction(M1, 1)+Fraction(3, 4) == Fraction(39, 4)*3**s')
    return {'j': j, 's': s, 'N': N, 'M0': M0, 'M1': M1, 'upper_steps': s + 6, 'min_upper': min(upper[1:])}

def crt_source(K):
    modulus = 2 ** (5 * K + 2)
    residue = (2 ** (5 * K + 1) - 19) * pow(49, -1, modulus) % modulus
    return next((residue + t * modulus for t in range(3) if residue + t * modulus > 0 and (residue + t * modulus) % 3 == 2))

def check_expanding_family(K):
    C = crt_source(K)
    initial_C = C
    N = (16 * C + 1) // 3
    need(3 * N == 16 * C + 1, 'Original line 207: 3*N == 16*C+1')
    need(v2(N + 1) == 2, 'Original line 208: v2(N+1) == 2')
    need(3 * C < N, 'Original line 209: 3*C < N')
    need(v2(49 * C + 19) == 5 * K + 1, 'Original line 210: v2(49*C+19) == 5*K+1')
    upper = path(N, 4 + 5 * K)
    need(word(upper) == '1101' + '11101' * K, "Original line 212: word(upper) == '1101'+'11101'*K")
    need(min(upper[1:]) > N, 'Original line 213: min(upper[1:]) > N')
    need(upper[4] == 9 * C + 2, 'Original line 214: upper[4] == 9*C+2')
    for j in range(K):
        need(C % 32 == 29, 'Original line 216: C % 32 == 29')
        need(C % 2 == 1, 'Original line 217: C % 2 == 1')
        D = (81 * C + 19) // 32
        need(32 * D == 81 * C + 19, 'Original line 219: 32*D == 81*C+19')
        need(D > C, 'Original line 220: D > C')
        lower = path(3 * C, 5)
        need(word(lower) == '11100', "Original line 222: word(lower) == '11100'")
        need(lower[-1] == D, 'Original line 223: lower[-1] == D')
        need(upper[4 + 5 * (j + 1)] == 9 * D + 2, 'Original line 224: upper[4+5*(j+1)] == 9*D+2')
        need(v2(49 * D + 19) == 5 * (K - j - 1) + 1, 'Original line 225: v2(49*D+19) == 5*(K-j-1)+1')
        need(D % 2 == 1, 'Original line 226: D % 2 == 1')
        need(3 * D > N, 'Original line 227: 3*D > N')
        C = D
    need(C % 32 != 29, 'Original line 229: C % 32 != 29')
    need(v2(49 * C + 19) == 1, 'Original line 230: v2(49*C+19) == 1')
    need(Fraction(C, 1) + Fraction(19, 49) == Fraction(81, 32) ** K * (Fraction(initial_C, 1) + Fraction(19, 49)), 'Original line 231: Fraction(C, 1)+Fraction(19, 49) == (\n        Fraction(81, 32)**K * (Fraction(initial_C, 1)+Fraction(19, 49)))')
    return {'K': K, 'N_bits': N.bit_length(), 'upper_steps': 4 + 5 * K, 'first_C': initial_C, 'final_C': C}

def main():
    stage_cases = 20000
    for C in range(1, stage_cases + 1):
        check_stage(C)
    chain_count = 0
    for C in range(1, 2001):
        chain_count += check_ledger(C, 30)
    guarded_outcomes = {'MERGE': 0, 'FAILED_DEBT_GUARD': 0}
    guarded_stages = 0
    guarded_max_stages = 0
    for C in range(1, 20001):
        stages, clock, outcome = check_guarded_normalizer(C)
        _, _, M0 = canonical(C)
        if M0 == 3:
            need(stages == 0, 'Original line 251: stages == 0')
            bound = 0
        else:
            bound = 0
            while 3 ** bound * (M0 - 3) >= 4 ** bound:
                bound += 1
            need(stages <= bound, 'Original line 257: stages <= bound')
        K0 = 0
        while 3 ** (K0 + 2) <= M0:
            K0 += 1
        S0 = (M0 + 1).bit_length() - 1
        B0 = max(6, 2 * K0 + S0 + 2)
        need(clock <= (bound + 1) * B0, 'Original line 263: clock <= (bound+1)*B0')
        guarded_outcomes[outcome] += 1
        guarded_stages += stages
        guarded_max_stages = max(guarded_max_stages, stages)
    unbounded_guard_bits = [check_unbounded_guard_family(s, epsilon) for s in range(1, 25) for epsilon in (0, 1)]
    need(check_stage(5) == (20, 15, 4), 'Original line 270: check_stage(5) == (20, 15, 4)')
    need(canonical(20) == (1, 0, 45), 'Original line 271: canonical(20) == (1, 0, 45)')
    need(15 < 27 < 45, 'Original line 272: 15 < 27 < 45')
    powers = [check_power_family(j) for j in range(1, 7)]
    expanding = [check_expanding_family(K) for K in range(1, 25)]
    for C in range(1, 20001):
        predicted = v2(49 * C + 19) // 5
        current = C
        actual = 0
        while current % 32 == 29:
            current = (81 * current + 19) // 32
            actual += 1
        need(actual == predicted, 'Original line 283: actual == predicted')
    result = {'status': 'PASS', 'canonical_stage_inputs': stage_cases, 'ledger_initial_sources': 2000, 'ledger_hard_steps_checked': chain_count, 'ledger_max_steps_per_source': 30, 'guarded_normalizer_initial_parameters': 20000, 'guarded_normalizer_outcomes': guarded_outcomes, 'guarded_normalizer_accepted_stages': guarded_stages, 'guarded_normalizer_max_stages': guarded_max_stages, 'unbounded_guard_family_cases': len(unbounded_guard_bits), 'unbounded_guard_family_s_max': 24, 'unbounded_guard_family_max_root_bits': max(unbounded_guard_bits), 'power_family': powers, 'expanding_family_count': len(expanding), 'expanding_family_max_K': expanding[-1]['K'], 'expanding_family_max_root_bits': max((r['N_bits'] for r in expanding)), 'fixed_source_countdown_inputs': 20000, 'N27_control': '15 < 27 < 45 retained', 'limits': 'finite scoped arithmetic checks; no all-source proof or repository-wide validation'}
    print(json.dumps(result, indent=2))
if __name__ == '__main__':
    main()
