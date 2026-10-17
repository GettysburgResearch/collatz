#!/usr/bin/env python3
"""Independent exact checks for the fixed-original-source research pass.

No import from either a repository generator or a candidate proof kernel.
Arithmetic progressions are verified by affine parity induction, not samples.
Finite samples are explicitly reported as finite checks.
"""

from fractions import Fraction
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def shortcut(n):
    require(type(n) is int and n > 0, "positive ordinary source required")
    return (3 * n + 1) // 2 if n % 2 else n // 2


def valuation(n):
    require(type(n) is int and n > 0, "positive valuation argument required")
    return (n & -n).bit_length() - 1


def actual_word(n, length):
    states = [n]
    for _ in range(length):
        states.append(shortcut(states[-1]))
    return "".join(str(x % 2) for x in states[:-1]), states


def progression_word(slope, intercept, word):
    require(slope > 0 and intercept > 0, "whole positive family required")
    states = [(slope, intercept)]
    for i, digit in enumerate(word):
        require(digit in "01", "invalid parity letter")
        require(slope % 2 == 0, f"nonconstant parity at step {i}")
        require(intercept % 2 == int(digit), f"wrong source parity at step {i}")
        if digit == "1":
            slope, intercept = 3 * slope // 2, (3 * intercept + 1) // 2
        else:
            slope, intercept = slope // 2, intercept // 2
        require(slope > 0 and intercept > 0, "nonpositive member")
        states.append((slope, intercept))
    return states


def reject_wrong_word():
    try:
        progression_word(4478976, 14463, "011111101")
    except ValueError:
        return
    raise ValueError("wrong parity mutation was accepted")


def run():
    odd_count = even_count = return_count = 0
    for k in range(10):
        for v in range(1, 400, 2):
            c = 2 ** (2 * k + 1) * v
            m = 3 ** (k + 1) * v
            word, states = actual_word(9 * c + 2, 2 * k + 2)
            require(word == "01" * k + "00", "odd valuation word")
            require(states[-1] == shortcut(m), "odd valuation endpoint")
            odd_count += 1

            c = 2 ** (2 * k) * v
            m = 3 ** (k + 1) * v
            word, states = actual_word(9 * c + 2, 2 * k)
            require(word == "01" * k, "even valuation prefix")
            require(states[-1] == 3 * m + 2, "even valuation comparison")
            s = valuation(m + 1)
            q = 3 ** s * ((m + 1) // 2 ** s)
            uw, up = actual_word(3 * m + 2, s + 2)
            lw, low = actual_word(m, s + 2)
            if q % 4 == 3:
                require(uw == "1" * s + "00", "even good upper word")
                require(lw == "1" * s + "01", "even good lower word")
                require(up[-1] == low[-1] == (3 * q - 1) // 4, "even merger")
            else:
                d = (q - 1) // 4
                require(q % 4 == 1 and d > 0, "hard positive parameter")
                require(uw == "1" * s + "01", "even hard upper word")
                require(lw == "1" * s + "00", "even hard lower word")
                require(up[-1] == 9 * d + 2 and low[-1] == d, "even return")
            even_count += 1

    rules = [
        (4, 2, 3, 2, 2, "01", "01"),
        (16, 13, 9, 11, 4, "1100", "1001"),
        (32, 23, 27, 19, 5, "10101", "11100"),
        (32768, 191, 19683, 41635, 15, "101101010111100", "111111010001001"),
    ]
    for modulus, residue, p, a, length, uw, lw in rules:
        for t in range(500):
            d = modulus * t + residue
            if d == 2:
                continue
            e = (p * d + a) // 2 ** length
            uactual, up = actual_word(3 * d - 4, length)
            lactual, low = actual_word(d, length)
            require(uactual == uw and lactual == lw, "R-return words")
            require(up[-1] == 3 * e - 4 and low[-1] == e, "R-return endpoint")
            require(0 <= 7 * (e - 2) <= 6 * (d - 2) and e < d, "common R rank")
            return_count += 1

    n = (4478976, 14463)
    m = (4194304, 13543)
    upper = progression_word(*n, "111111101")
    lower = progression_word(*m, "11101110101111111100")
    require(upper[-1] == lower[-1] == (57395628, 185348), "new family merger")
    require(all(a > n[0] and b > n[1] for a, b in upper[1:]), "whole-arm no descent")
    require(n[0] > m[0] > 0 and n[1] > m[1] > 0, "original-source order")
    require(n[0] % 3 == n[1] % 3 == 0, "whole family multiples of three")
    hc = (upper[-1][0] // 9, (upper[-1][1] - 2) // 9)
    require(hc == (6377292, 20594), "first H family")
    require(hc[0] % 4 == 0 and hc[1] % 4 == 2, "exact valuation one")
    old_m = (3 * hc[0] // 2, 3 * hc[1] // 2)
    require(old_m[0] > n[0] and old_m[1] > n[1], "old whole-stratum root failure")
    reject_wrong_word()

    f_count = 0
    for stages in range(1, 30):
        modulus = 2 ** (5 * stages)
        c = (-19 * pow(49, -1, modulus)) % modulus
        c += modulus * ((2 - c) * pow(modulus, -1, 3) % 3)
        require(c > 0 and c % 3 == 2, "positive first-entry CRT source")
        nroot = (16 * c + 1) // 3
        require(valuation(nroot + 1) == 2 and 3 * c < nroot, "initial root safety")
        for j in range(stages):
            require(c % 32 == 29, "expanding guard")
            d = (81 * c + 19) // 32
            uw, up = actual_word(9 * c + 2, 5)
            lw, low = actual_word(3 * c, 5)
            require(uw == "11101" and lw == "11100", "expanding actual words")
            require(up[-1] == 9 * d + 2 and low[-1] == d, "expanding endpoint")
            require(32 * (49 * d + 19) == 81 * (49 * c + 19), "expanding countdown")
            require(d > c and 3 * d > nroot, "irreversible root loss within F word")
            c = d
            f_count += 1

    # A complete family where the next parameter has a nontrivial even valuation.
    upper2 = progression_word(8192, 27, "110111110101")
    companion2 = progression_word(4608, 15, "111100")
    require(upper2[10] == (52488, 182), "compressed countercontrol upper H")
    require(companion2[-1] == (5832, 20), "compressed countercontrol lower C")
    require(all(a > 8192 and b > 27 for a, b in upper2[1:]), "countercontrol no descent")
    require(13122 > 8192 and 45 > 27, "compressed next candidate exceeds root")

    # Independently reconstruct the new 4Z+3 splice on whole CRT families.
    splice_families = 0
    for r in range(6, 20):
        for a in range(4, 13):
            u16 = 9 * pow(3 ** (r - 1), -1, 16) % 16
            ua = pow(2 ** (r + 2), -1, 3 ** a)
            u0 = u16 + 16 * ((ua - u16) * pow(16, -1, 3 ** a) % 3 ** a)
            uslope = 16 * 3 ** a
            require(u0 > 0 and u0 % 2 == 1, "positive least CRT root")
            n_slope, n_base = 2 ** r * uslope, 2 ** r * u0 - 1
            b_slope, b_base = 4 * n_slope // 3 ** a, (4 * n_base + 3) // 3 ** a
            m_slope, m_base = 2 ** a * b_slope, 2 ** a * b_base - 1
            up = progression_word(n_slope, n_base, "1" * r + "01")
            low = progression_word(m_slope, m_base, "1" * a + "0" + "1" * (r + 1) + "00")
            require(up[-1] == low[-1], "4Z+3 whole-family endpoint")
            require(n_slope > m_slope > 0 and n_base > m_base > 0, "4Z+3 root order")
            require(all(x > n_slope and y > n_base for x, y in up[1:]), "4Z+3 whole-arm minimum")
            require(n_slope % 3 == n_base % 3 == 0, "4Z+3 multiples of three")
            c_slope, c_base = up[-1][0] // 9, (up[-1][1] - 2) // 9
            require(c_slope % 4 == 0 and c_base % 4 == 2, "4Z+3 old candidate valuation")
            require(3 * c_slope // 2 > n_slope and 3 * c_base // 2 > n_base, "4Z+3 old root failure")
            require((8 * n_base + 3) % 3 == 0 and (8 * n_base + 3) % 9 != 0, "old 8Z+3 guard absent")
            require((8 * n_slope) % 9 == 0, "8Z+3 exact valuation across family")
            if (r, a) == (6, 4):
                require((n_slope, n_base) == (82944, 53439), "literal new root family")
                require((m_slope, m_base) == (65536, 42223), "literal new companion family")
                require(up[-1] == (708588, 456536), "literal new endpoint family")
            splice_families += 1

    ledger_steps = guarded_steps = 0
    for c in range(1, 20001):
        e = valuation(c)
        if e % 2:
            continue
        kin = e // 2
        m0 = 3 ** (kin + 1) * (c // 2 ** e)
        s = valuation(m0 + 1)
        q = 3 ** s * ((m0 + 1) // 2 ** s)
        if q % 4 != 1:
            continue
        d = (q - 1) // 4
        kout, eps = divmod(valuation(d), 2)
        m1 = 3 ** (kout + 1) * (d // 2 ** (2 * kout + eps))
        gamma = Fraction(3 ** (kout + 1), 2 ** (2 * kout + eps))
        gain = gamma * Fraction(3 ** s, 2 ** (s + 2))
        offset = 1 - gamma / 4
        require(Fraction(1, 4) <= offset < 1, "ledger offset range")
        require(m1 + 1 == gain * (m0 + 1) + offset, "exact ledger")
        ledger_steps += 1
        if 3 ** (s + kout) <= 2 ** (s + 2 * kout + eps):
            require(m0 > 3, "minimum candidate cannot pass guard")
            require(0 <= 4 * (m1 - 3) < 3 * (m0 - 3), "new strict common contraction")
            guarded_steps += 1

    sharp_members = 0
    for j in range(1, 15):
        s = 6 * j + 2
        nroot = 13 * (2 ** (s + 4) - 1) // 9
        c = (13 * 2 ** s - 1) // 3
        m0 = 13 * 2 ** s - 1
        d = (13 * 3 ** s - 1) // 4
        m1 = 3 * d
        word, states = actual_word(nroot, s + 6)
        lw, lower = actual_word(m0, s + 2)
        require(word == "1101" + "1" * s + "01", "sharp exponent upper word")
        require(lw == "1" * s + "00", "sharp exponent lower word")
        require(states[4] == 9 * c + 2 and states[-1] == 9 * d + 2, "sharp H endpoints")
        require(lower[-1] == d and m0 < nroot < m1, "sharp root order")
        require(all(x > nroot for x in states[1:]), "sharp no-descent prefix")
        require(9 * nroot + 13 == 208 * 2 ** s, "sharp exact power identity")
        require(4 * m1 + 3 == 39 * 3 ** s, "sharp exact upper power identity")
        sharp_members += 1

    return {
        "status": "PASS",
        "finite_raw_checks": {
            "odd_valuation_instances": odd_count,
            "even_valuation_instances": even_count,
            "R_return_instances": return_count,
            "F_word_stages": f_count,
            "hard_ledger_steps": ledger_steps,
            "guarded_contractions": guarded_steps,
            "sharp_exponent_members": sharp_members,
        },
        "whole_progressions": {
            "new_companion_endpoint": [57395628, 185348],
            "new_companion_order_margin": [284672, 920],
            "old_candidate_excess": [5086962, 16428],
            "compressed_restart_countercontrol": [8192, 27],
            "4Z_plus_3_CRT_families": splice_families,
        },
        "negative_controls": ["wrong parity word rejected", "old candidate larger than immutable root"],
        "scope": "Scoped exact checks only; no global coverage or Collatz proof asserted.",
    }


if __name__ == "__main__":
    print(json.dumps(run(), sort_keys=True))
