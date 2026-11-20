#!/usr/bin/env python3
"""Independent arithmetic review of the four alternative-route notes.

The author's JSON files supply explicit word parameters only. No author
Python module is imported. All fixed points and paths are reconstructed.
"""
from fractions import Fraction as F
from hashlib import sha256
from math import gcd
from pathlib import Path
import argparse
import json

BASE = None


def need(test, message):
    if not test:
        raise ValueError(message)


def vp(n, p):
    n = abs(n)
    need(n != 0, 'valuation of zero')
    a = 0
    while n % p == 0:
        n //= p
        a += 1
    return a


def odd(n):
    z = 3 * n + 1
    a = vp(z, 2)
    return z >> a, a


def affine(word):
    q, c = 0, 0
    for k, bit in enumerate(word):
        if bit == '1':
            q += 1
            c = 3 * c + (1 << k)
        else:
            need(bit == '0', 'nonbinary word')
    return q, c


def rational_hash(n):
    return sha256(n.to_bytes((n.bit_length() + 7) // 8, 'big')).hexdigest()


def review_cycles():
    counts = {'cycle_roots': 0, 'shortcut_edges': 0, 'extra_moduli': [], 'integer_targets': 0}
    inputs = [('adic-real-density-report.json', 'cycle_cases'),
              ('finite-places-report.json', 'cases')]
    for filename, key in inputs:
        cases = json.loads((BASE / filename).read_text())[key]
        for case in cases:
            prefix = case['prefix']
            a, b = case['a'], case['b']
            word = prefix + '1' * b + '0' * a
            q, c = affine(word)
            d_unreduced = (1 << len(word)) - 3**q
            need(c > 0 and d_unreduced > 0, 'positive fixed point')
            root = F(c, d_unreduced)
            u, d = root.numerator, root.denominator
            need(d > 1 and gcd(d, 6) == 1, 'noninteger denominator units')
            need(rational_hash(u) == case['numerator_sha256_big_endian'], 'root numerator digest')
            need(rational_hash(d) == case['denominator_sha256_big_endian'], 'root denominator digest')
            need(8 * q - 5 * len(word) == case['critical_lap_score'] > 0, 'positive score')
            target = F(case['real_target']['numerator'], case['real_target']['denominator'])
            error = F(case['real_error']['numerator'], case['real_error']['denominator'])
            need(abs(root - target) < error, 'real neighborhood')
            for p, precision_key, residue_key in (
                (2, 'binary_precision', 'binary_residue'),
                (3, 'ternary_precision', 'ternary_residue'),
            ):
                modulus = p ** case[precision_key]
                need((u - case[residue_key] * d) % modulus == 0, 'local residue')
            if 'extra_modulus' in case:
                modulus = case['extra_modulus']
                residue = case['extra_residue']
                need(gcd(d, modulus) == 1 and (u - residue * d) % modulus == 0,
                     'extra rational congruence')
                inv = pow(1 << len(word), -1, modulus)
                need((3**q * inv) % modulus == 2 % modulus, 'full modular slope')
                need((c * inv) % modulus == -residue % modulus, 'full modular offset')
                counts['extra_moduli'].append(modulus)
                original = 2 ** case['original_binary_precision']
                need((u - case['original_binary_residue'] * d) % original == 0,
                     'original binary prefix preserved')
            numerator = u
            phase_after_prefix = u if not prefix else None
            for index, bit in enumerate(word):
                need((numerator & 1) == int(bit), 'actual rational parity')
                need(gcd(numerator, d) == 1 and numerator % 3 != 0,
                     'phase denominator or ternary unit')
                numerator = (3 * numerator + d) // 2 if bit == '1' else numerator // 2
                need(numerator > 0, 'positive cycle phase')
                if index + 1 == len(prefix):
                    phase_after_prefix = numerator
                counts['shortcut_edges'] += 1
            need(numerator == u, 'actual cycle failed to close')
            need(phase_after_prefix is not None, 'prefix phase absent')
            need((phase_after_prefix + d) % (1 << b) == 0, 'odd-run divisibility')
            need(phase_after_prefix + d >= 1 << b, 'denominator growth floor')
            if target.denominator == 1:
                n = target.numerator
                K = case.get('original_binary_precision', case['binary_precision'])
                M = case['ternary_precision']
                modulus = 2**K * 3**M * case.get('extra_modulus', 1)
                if (u - n * d) % modulus == 0:
                    need(d * abs(root - n) >= modulus, 'diagonal denominator cost')
                    counts['integer_targets'] += 1
            counts['cycle_roots'] += 1
    return counts


def review_fixed_pins():
    checked = returns = 0
    for n in range(1, 122):
        state, q, c = n, 0, 0
        for K in range(1, 41):
            if state % 2:
                c = 3 * c + 2 ** (K - 1)
                q += 1
                state = (3 * state + 1) // 2
            else:
                state //= 2
            need(2**K * state == 3**q * n + c, 'actual affine prefix')
            if not q:
                continue
            D, h = 2**K - 3**q, state - n
            pin = F(c, D)
            if h == 0:
                need(pin == n, 'return pin')
                returns += 1
                continue
            g = gcd(c, abs(D))
            need(g == gcd(h, abs(D)), 'pin gcd identity')
            need(pin.denominator == abs(D) // g, 'reduced pin denominator')
            need(pin - n == F(2**K * h, D), 'pin difference')
            u, v = vp(h, 2), vp(h, 3)
            ratio = pin.denominator * abs(pin - n) / (2 ** (K + u) * 3**v)
            h0 = abs(h) // (2**u * 3**v)
            need(ratio == F(h0, g) and ratio.denominator == 1 and ratio >= 1,
                 'exact positive integer threshold')
            checked += 1
    return {'nonreturn_pins': checked, 'actual_return_controls': returns,
            'source_limit': 121, 'shortcut_horizon': 40}


def review_shifted_pairs():
    products = first_defects = canceled = excess = 0
    for source in range(1, 302, 2):
        if source % 3 == 0:
            continue
        values, sums, gaps, seen = [source], [0], [], {source}
        for _ in range(40):
            image, a = odd(values[-1])
            if image in seen:
                break
            values.append(image)
            sums.append(sums[-1] + a)
            gaps.append(a)
            seen.add(image)
        lambdas = [F(2**A, 3**j) for j, A in enumerate(sums)]
        shifted = [lam * (n + 1) for n, lam in zip(values, lambdas)]
        formal_L = shifted[-1]
        for j, (n, A, lam, M) in enumerate(zip(values, sums, lambdas, shifted)):
            s, t = vp(n + 1, 2), vp(n + 1, 3)
            raw_p, raw_q = 2**A * (n + 1), 3**j
            g = gcd(raw_p, raw_q)
            need(g == 3 ** min(j, t), 'shifted primitive gcd')
            p, q = raw_p // g, raw_q // g
            need(gcd(p, q) == 1, 'primitive pair')
            local_2 = F(1, 2 ** (vp(p, 2) + vp(q, 2)))
            local_3 = F(1, 3 ** (vp(p, 3) + vp(q, 3)))
            product = abs(formal_L * q - p) * q * local_2 * local_3
            defect = sum((lambdas[i] * (2 ** gaps[i] - 2) / 3
                          for i in range(j, len(gaps))), F(0))
            need(defect == formal_L - M, 'sum of future non-one defects')
            need(product == defect / (lam * 2**s * 3**t), 'shifted product')
            need((formal_L - lam * n) / lam >= 1, 'unshifted formal floor')
            if j + s < len(values):
                need(product >= F(1, 3 ** (s + t)), 'observed first-defect floor')
                first_defects += 1
            need(q * (source + 1) >= 2**j, 'primitive height lower bound')
            for target in (F(0), F(2), F(7, 3)):
                target_product = abs(target * q - p) * q * local_2 * local_3
                need(target_product >= abs(target - M) / M, 'wrong fixed target')
            products += 1
            canceled += g > 1
            excess += t > j
    sharpness = []
    for s in range(1, 12, 2):
        n = 2**s - 1
        state, lam = n, F(1)
        for j in range(s):
            image, a = odd(state)
            need(a == (1 if j < s - 1 else 2), 'formal control ordinary prefix')
            lam *= F(2**a, 3)
            state = image
        formal_L = lam * (state + 1)
        shifted_product = (formal_L - (n + 1)) / 2**s
        need(shifted_product == F(1, 3**s), 'formal shrinking floor sharpness')
        sharpness.append(s)
    return {'primitive_products': products, 'observed_first_defect_bounds': first_defects,
            'ternary_cancellations': canceled, 't_greater_than_j': excess,
            'formal_sharpness_odd_s': sharpness,
            'formal_tail_is_not_an_actual_infinite_orbit': True}


def main():
    global BASE
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-root', type=Path, required=True,
                        help='Directory containing the two cycle-seed reports')
    BASE = parser.parse_args().source_root
    report = {'status': 'PASS independent exact arithmetic checks',
              'cycle_reconstruction': review_cycles(),
              'fixed_pins': review_fixed_pins(),
              'shifted_pairs': review_shifted_pairs(),
              'scope': 'finite replay and independent proof audit; no Collatz closure'}
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
