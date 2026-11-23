#!/usr/bin/env python3
"""Exact finite diagnostics for the accompanying finite-insertion theorem."""
from fractions import Fraction
from itertools import combinations_with_replacement
import json


CHECKS_EXECUTED = 0


def require(condition, message):
    """Check a mathematical condition even when Python optimization is enabled."""
    global CHECKS_EXECUTED
    CHECKS_EXECUTED += 1
    if not condition:
        raise RuntimeError(message)


def gap_step(q):
    require(q > 0 and q % 2 == 1, 'gap_step requires a positive odd integer')
    v = 3 * q + 1
    a = (v & -v).bit_length() - 1
    return a, v >> a


def orbit(n, length):
    qs, gaps, sums, carries = [n], [], [0], [0]
    for i in range(length):
        a, q = gap_step(qs[-1])
        gaps.append(a)
        qs.append(q)
        carries.append(3 * carries[-1] + (1 << sums[-1]))
        sums.append(sums[-1] + a)
        require((1 << sums[-1]) * q == 3 ** (i + 1) * n + carries[-1],
                'original affine carry identity failed')
    return qs, gaps, sums, carries


def enlarged_word(gaps, cuts):
    out = []
    for i in range(len(gaps) + 1):
        out.extend([1] * cuts.count(i))
        if i < len(gaps):
            out.append(gaps[i])
    return out


def inverse_source(endpoint, word):
    z = Fraction(endpoint)
    for a in reversed(word):
        z = ((1 << a) * z - 1) / 3
    return z


def formula(n, qs, sums, cuts):
    return Fraction(n) - sum(
        (Fraction((1 << (sums[i] + ell - 1)) * (qs[i] + 1), 3 ** (i + ell))
         for ell, i in enumerate(cuts, 1)), Fraction(0))


def check_ordinary(n, m, qs, gaps, sums, cuts):
    t, N = len(cuts), n.bit_length()
    require(0 < m < n and m % 2 == 1, 'candidate is not a smaller positive odd source')
    require(3 ** t < (1 << t) * n, 'insertion-count bound failed')
    require((1 << t) < n * n, 'squared insertion-count bound failed')
    require(t < 2 * N, 'bitlength insertion-count bound failed')
    z, prev = m, 0
    for ell, cut in enumerate(cuts, 1):
        d_start = qs[prev] - z
        B = sums[cut] - sums[prev]
        require(d_start > 0 and d_start % (1 << (B + 1)) == 0,
                'common-block positive-difference divisibility failed')
        require(B <= sums[prev] + N - 2, 'common-block clock bound failed')
        for i in range(prev, cut):
            a, z = gap_step(z)
            require(a == gaps[i], 'candidate does not realize the prescribed original gap')
            require(qs[i + 1] - z > 0, 'aligned difference lost positivity in a common block')
        before = qs[cut] - z
        a, z_next = gap_step(z)
        require(a == 1, 'candidate does not realize an inserted gap one')
        after = qs[cut] - z_next
        require(2 * after == 3 * before - qs[cut] - 1, 'insertion difference identity failed')
        require(after < before, 'inserted gap did not decrease the aligned difference')
        require((after > 0) if ell < t else (after == 0),
                'alignment did not first merge at the last insertion')
        z, prev = z_next, cut
        require(sums[cut] <= (N - 2) * ((1 << ell) - 1), 'last-edit recurrence bound failed')
    require(z == qs[cuts[-1]], 'modified and original endpoints differ')
    require(sums[cuts[-1]] + t < N * (n * n + 2), 'modified merger clock bound failed')


def main():
    counts = dict(rational_candidates=0, positive_integer_candidates=0,
                  candidates_with_nonintegral_partial_source=0)
    examples, cancellation_example = [], None
    for n in range(3, 256, 2):
        qs, gaps, sums, carries = orbit(n, 10)
        for j in range(11):
            for t in range(1, 4):
                for prior in combinations_with_replacement(range(j + 1), t - 1):
                    cuts = prior + (j,)
                    word = enlarged_word(gaps[:j], cuts)
                    m = inverse_source(qs[j], word)
                    require(m == formula(n, qs, sums, cuts),
                            'inverse-word source disagrees with the insertion formula')
                    require(m < Fraction((1 << t) * n, 3 ** t),
                            'strict rational-source contraction failed')
                    counts['rational_candidates'] += 1
                    if m.denominator != 1 or m <= 0:
                        continue
                    m = int(m)
                    counts['positive_integer_candidates'] += 1
                    check_ordinary(n, m, qs, gaps, sums, cuts)
                    if t == 1:
                        require((qs[j] + 1) % (3 ** (j + 1)) == 0,
                                'single-insertion ternary divisibility failed')
                        require(3 * (1 << j) <= n + 1, 'single-insertion cut bound failed')
                    partials = [formula(n, qs, sums, cuts[:s]) for s in range(1, t)]
                    if any(x.denominator != 1 for x in partials):
                        counts['candidates_with_nonintegral_partial_source'] += 1
                        if cancellation_example is None:
                            cancellation_example = dict(n=n, m=m, cuts=cuts,
                                partial_sources=list(map(str, partials)),
                                last_original_clock=sums[j])
                    if len(examples) < 8 and (j > 0 or t > 1):
                        examples.append(dict(n=n, m=m, cuts=cuts,
                            original_gaps=gaps[:j], modified_gaps=word,
                            endpoint=qs[j], last_original_clock=sums[j],
                            modified_merger_clock=sums[j] + t))
    for u in range(1, 6):
        for t in range(1, 9):
            n, m = 2 * u * 3 ** t - 1, 2 * u * 2 ** t - 1
            z = m
            for _ in range(t):
                a, z = gap_step(z)
                require(a == 1, 'explicit family does not have the claimed gap-one word')
            require(z == n, 'explicit family does not attain its claimed endpoint')
            qs, gaps, sums, _ = orbit(n, 0)
            check_ordinary(n, m, qs, gaps, sums, (0,) * t)
    result = dict(status='all exact checks passed',
        scope=dict(odd_sources='3..255', last_cut='0..10', insertions='1..3',
                   all_cut_multisets=True, additional_family_cases=40),
        validation=dict(guards='explicit require/raise; active under python -O',
                        checks_executed=CHECKS_EXECUTED, output='stdout only'),
        counts=counts, cancellation_example=cancellation_example, examples=examples,
        claim_boundary='Finite diagnostics; the universal bound is proved in the note. No Collatz closure.')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
