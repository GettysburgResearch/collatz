#!/usr/bin/env python3
"""Exact finite-input return calculus and positive .84 renewal certificate.

No search success is interpreted as universal Collatz convergence.  All
checks use explicit exceptions and remain active under python -O.
"""
from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
import hashlib
import itertools
import json

S_NUM, S_DEN = 21, 25
SCALE = 10**10
DEPTH = 6
ONES = ((3, 6), (5, 6), (8, 8), (9, 9))


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def v2(n):
    require(isinstance(n, int) and n > 0, "v2 domain")
    return (n & -n).bit_length() - 1


def correction(word):
    clock = const = 0
    for a in word:
        require(isinstance(a, int) and a >= 1, "positive exponent required")
        const = 3 * const + (1 << clock)
        clock += a
    return const, clock


def target_positions(source_const, odd_count):
    """Unique p-term correction representation of 5 B, or None."""
    require(source_const > 0 and odd_count > 0, "correction domain")
    value = 5 * source_const
    positions = [0]
    for remaining in range(odd_count - 1, 0, -1):
        residual = value - 3**remaining
        if residual <= 0 or residual % 2:
            return None
        step = v2(residual)
        value = residual >> step
        positions.append(positions[-1] + step)
    return tuple(positions) if value == 1 else None


def return_word(word):
    """Complete recognition within equal-clock, equal-odd-count returns."""
    if not word:
        return None
    const, clock = correction(word)
    pos = target_positions(const, len(word))
    if pos is None or pos[-1] >= clock:
        return None
    return tuple(pos[i + 1] - pos[i] for i in range(len(pos) - 1)) + (clock - pos[-1],)


def odd_step(n):
    require(n > 0 and n % 2, "positive odd source required")
    m = 3 * n + 1
    a = v2(m)
    return m >> a, a


def replay(n, word, first_hit=False):
    require(n > 0 and n % 2, "positive odd source required")
    out = [n]
    for a in word:
        if first_hit:
            require(n != 1, "input passed its first hit")
        n, actual = odd_step(n)
        require(actual == a, "exponent mismatch")
        out.append(n)
    return n, out


def inverse(word, endpoint=1):
    n = endpoint
    for a in reversed(word):
        m = (1 << a) * n - 1
        if m % 3:
            return None
        n = m // 3
        if n <= 0 or n % 2 == 0:
            return None
    return n


def compile_certificate(n, word):
    endpoint, _ = replay(n, word, first_hit=True)
    require(endpoint == 1, "input is not a complete first-hit certificate")
    target, blocks, offset = [], [], 0
    while offset < len(word):
        for end in range(offset + 1, len(word) + 1):
            new = return_word(word[offset:end])
            if new is not None:
                blocks.append((offset, end))
                target.extend(new)
                offset = end
                break
        else:
            return {"status": "UNRESOLVED", "consumed": offset}
    target.append(4)
    result, _ = replay(5 * n, target, first_hit=True)
    require(result == 1, "compiler output failed")
    require(len(target) == len(word) + 1, "compiler odd count")
    require(sum(target) == sum(word) + 4, "compiler clock")
    return {"status": "CERTIFIED", "word": tuple(target), "blocks": blocks}


@lru_cache(None)
def inverse_s_upper(value):
    """Rational upper bound for value^(-21/25), verified by integer powers."""
    require(value >= 1, "upper-power domain")
    a, b = value.numerator, value.denominator
    aa, bb = a**S_NUM, SCALE**S_DEN * b**S_NUM
    lo, hi = 0, SCALE
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if mid**S_DEN * aa >= bb:
            hi = mid
        else:
            lo = mid
    require(hi**S_DEN * aa >= bb, "power upper bound")
    return Fraction(hi, SCALE)


@lru_cache(None)
def logarithms(depth):
    mod = 3**depth
    order = 2 * 3**(depth - 1)
    result, u = {}, 1
    for j in range(order):
        require(u not in result, "incorrect power-of-three order")
        result[u] = j
        u = (2 * u) % mod
    require(u == 1 and len(result) == 2 * 3**(depth - 1), "incomplete units")
    return result


def progression_min(q, p, prefix_clock, const, threshold, depth=DEPTH):
    d = min(p, depth)
    mod = 3**d
    order = 2 * 3**(d - 1)
    logs = logarithms(d)
    residue = (logs[const % mod] - prefix_clock - logs[q % mod]) % order
    first = threshold + (residue - threshold) % order
    require(pow(2, prefix_clock + first, mod) * (q % mod) % mod == const % mod,
            "inverse progression")
    return first, order


def family_charge(qmin, p, prefix_clock, const, threshold):
    first, order = progression_min(qmin, p, prefix_clock, const, threshold)
    kappa = ((1 << (prefix_clock + first)) - Fraction(const, qmin)) / 3**p
    require(kappa >= 1, "not a decreasing family")
    return inverse_s_upper(kappa) / (1 - inverse_s_upper(Fraction(1 << order))), first


def congestion_certificate():
    """A finite integer certificate uniformly bounds an infinite inverse sum."""
    modulus = 3**DEPTH
    t = inverse_s_upper(Fraction(4, 3))
    rows = []
    for residue in range(modulus):
        if residue % 3 == 0:
            continue
        qmin = residue if residue % 2 else residue + modulus
        if qmin < 5:
            qmin += 2 * modulus
        total = Fraction(0)
        firsts = []
        for r in range(1, DEPTH):
            p = r + 1
            charge, first = family_charge(qmin, p, 2 * r, 4**p - 3**p, 4)
            total += charge
            firsts.append(first)
        # For every r>=DEPTH, integrality implies 2^(b-2)q=1 mod3^DEPTH.
        period = 2 * 3**(DEPTH - 1)
        residue_b = (2 - logarithms(DEPTH)[qmin % modulus]) % period
        first = 4 + (residue_b - 4) % period
        c = Fraction(4, 3) * ((1 << (first - 2)) - Fraction(1, qmin))
        tail = inverse_s_upper(c) * t**DEPTH / (1 - t)
        tail /= 1 - inverse_s_upper(Fraction(1 << period))
        total += tail
        firsts.append(first)
        ones_firsts = []
        for r, threshold in ONES:
            p = r + 1
            charge, first = family_charge(qmin, p, r, 3**p - 2**p, threshold)
            total += charge
            ones_firsts.append(first)
        rows.append((total, residue, qmin, firsts, ones_firsts))
    rows.sort(reverse=True)
    worst = rows[0]
    upper = Fraction(903, 1000)
    require(all(x[0] < upper for x in rows), "not all endpoint classes covered")
    digest = hashlib.sha256(json.dumps([
        [str(z), r, q, a, b] for z, r, q, a, b in sorted(rows, key=lambda x:x[1])
    ], separators=(",", ":")).encode()).hexdigest()
    return {"classes": len(rows), "modulus": modulus, "s": "21/25",
            "coefficient_upper": str(upper), "worst_decimal": float(worst[0]),
            "worst_residue": worst[1], "worst_qmin": worst[2],
            "worst_ladder_first_exponents": worst[3],
            "worst_ones_first_exponents": worst[4], "rows_sha256": digest}


def checks():
    symbol_checks = accepted = source_checks = compiler_checks = 0
    for p in range(1, 7):
        for prefix in itertools.product(range(1, 6), repeat=p-1):
            word = prefix + (6,)
            const, clock = correction(word)
            answer = return_word(word)
            symbol_checks += 1
            if answer is not None:
                require(correction(answer) == (5 * const, clock), "correction identity")
                accepted += 1
    examples = []
    for r, threshold in ONES:
        word = (1,) * r + (threshold,)
        target = return_word(word)
        require(target is not None, "ones header missing")
        const, clock = correction(word)
        modulus = 1 << clock
        residue = (-const * pow(3**len(word), -1, modulus)) % modulus
        examples.append({"source_prefix": list(word), "target_prefix": list(target),
                         "residue": residue, "modulus": modulus})
        for k in range(40):
            n = residue + modulus * k
            source = n
            actual = []
            for _ in range(r + 1):
                source, a = odd_step(source)
                actual.append(a)
            require(tuple(actual[:-1]) == (1,) * r and actual[-1] >= threshold,
                    "source cylinder")
            new = return_word(actual)
            require(new is not None, "cylinder omitted by complete recognizer")
            out, _ = replay(5*n, new)
            require(out == 5 * source, "literal paired return")
            source_checks += 1
    for p in range(1, 6):
        for word in itertools.product(range(1, 9), repeat=p):
            n = inverse(word)
            if n is None:
                continue
            try:
                end, _ = replay(n, word, first_hit=True)
            except ArithmeticError:
                continue
            require(end == 1, "inverse reconstruction")
            out = compile_certificate(n, word)
            if out["status"] == "CERTIFIED":
                compiler_checks += 1
    require(compile_certificate(17, (2,3,4))["status"] == "UNRESOLVED",
            "17 must not be mislabeled")
    oracle_checks = 0
    for clock in range(1, 13):
        words = []
        for cuts in range(1 << (clock-1)):
            positions = [0] + [j for j in range(1, clock) if cuts & (1 << (j-1))] + [clock]
            words.append(tuple(b-a for a,b in zip(positions,positions[1:])))
        by_count = {}
        for word in words:
            by_count.setdefault(len(word), {})[correction(word)[0]] = word
        for word in words:
            const, _ = correction(word)
            expected = by_count[len(word)].get(5 * const)
            require(return_word(word) == expected, "exhaustive correction-language oracle")
            oracle_checks += 1
    require(return_word((2, 4)) == (5, 1), "inherited base block")
    for r in range(2, 30):
        require(return_word((2,)*r+(4,)) == (4,)+(2,)*(r-2)+(3,1),
                "inherited unbounded ladder specialization")
    overload_sum = Fraction(0)
    for r, lower in ((3,66),(5,130),(8,363),(9,510)):
        ratio = Fraction(3**(r+1), 2**(r+8))
        require(ratio.numerator**21 * 1000**25 > ratio.denominator**21 * lower**25,
                "overload lower bound")
        overload_sum += Fraction(lower,1000)
    require(overload_sum > 1, "full-column overload")
    # Genuine compiled examples from each new family, with a known endpoint 1.
    compiled_large = []
    for r, threshold in ONES:
        p = r + 1
        first, _ = progression_min(1, p, r, 3**p - 2**p, threshold, depth=p)
        word = (1,)*r+(first,)
        n = inverse(word)
        require(n is not None and n > 1, "new first-hit source")
        out = compile_certificate(n, word)
        require(out["status"] == "CERTIFIED", "new language compilation")
        compiled_large.append({"r":r,"b":first,"source_bits":n.bit_length(),
                               "target_word":list(out["word"])})
    density = Fraction(1,48) + sum((Fraction(1, 1 << (r+b)) for r,b in ONES), Fraction(0))
    return {"status":"PASS", "symbolic_words_checked": symbol_checks,
            "recognized_words": accepted, "ordinary_cylinder_checks":source_checks,
            "finite_first_hit_compiler_successes":compiler_checks,
            "exhaustive_same_clock_word_oracle_checks":oracle_checks,
            "families":examples,"compiled_unbounded_family_examples":compiled_large,
            "binary_cylinder_density":str(density),
            "actual_unit_domain_natural_density":str(Fraction(2,3)*density),
            "relative_unit_density":str(2*density),
            "omitted_r9_b8_column_lower_bound":str(overload_sum),
            "congestion":congestion_certificate(),
            "scope":"Exact bounded checks and an infinite-family congestion certificate; full five closure remains OPEN."}


if __name__ == "__main__":
    print(json.dumps(checks(), indent=2, sort_keys=True))
