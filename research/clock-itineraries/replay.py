"""Construct and independently replay ordinary marked Collatz paths."""

from functools import cache
from itertools import product
from math import prod
import json


def check(condition, message):
    if not condition:
        raise ValueError(message)


@cache
def logarithms(modulus):
    """Positive representatives of the discrete logarithms, including log(1)."""
    order = 2 * (modulus // 3)
    table = {pow(2, e, modulus): e for e in range(1, order + 1)}
    check(len(table) == order, "two did not generate the unit group")
    return table


def compatible(q, marks, clock, modulus):
    left = pow(2, clock, modulus) * q * prod(marks[1:])
    right = prod(3*r + 1 for r in marks)
    return (left - right) % modulus == 0


def construct(q, marks, clock, precision):
    """Return forward gaps for a compatible clock in the proved range."""
    modulus = 3**precision
    check(precision >= 1 and len(marks) >= 2, "need at least two marks and positive precision")
    check(q > 0 and q % 2 == 1 and q % 3 != 0, "target must be a positive odd unit")
    check(all(0 <= r < modulus and r % 3 for r in marks), "invalid unit residue")
    order = 2 * (modulus // 3)
    check(clock >= 3*order*(len(marks)+1) + 1, "clock below the uniform bound")
    if not compatible(q, marks, clock, modulus):
        return None

    remaining = clock
    endpoint = q
    reverse_tail = []
    for r in reversed(marks[2:]):
        residue = (3*r+1)*pow(endpoint, -1, 3*modulus) % (3*modulus)
        gap = logarithms(3*modulus)[residue]
        reverse_tail.append(gap)
        endpoint = ((1 << gap)*endpoint - 1) // 3
        remaining -= gap

    period_modulus = 9*modulus
    residue = (pow(2, remaining, period_modulus)*endpoint - 3 - 9*marks[0]) % period_modulus
    first = logarithms(period_modulus)[residue]
    return (first, remaining-first, *reversed(reverse_tail))


def replay(q, gaps, marks, clock, modulus):
    """Use exact inverse division, then read every shortcut step forward."""
    x = q
    for gap in reversed(gaps):
        check(gap > 0, "nonpositive gap")
        x, rem = divmod((1 << gap)*x - 1, 3)
        check(rem == 0 and x > 0 and x % 2 == 1 and x % 3 != 0, "invalid odd unit")
    source = x
    seen_marks = []
    seen_clocks = []
    for t in range(clock):
        if x % 2:
            seen_marks.append(x % modulus)
            seen_clocks.append(t)
            x = (3*x+1)//2
        else:
            x //= 2
    check(x == q, "wrong terminal")
    check(tuple(seen_marks) == tuple(marks), "wrong chronological marks")
    check(tuple(b-a for a,b in zip(seen_clocks, seen_clocks[1:] + [clock])) == gaps,
          "wrong forward gaps")
    return source


def enumerate_row(q, depth, clock, modulus):
    """All positive gap compositions with this clock, pruned by literal divisibility."""
    if depth == 0:
        return {()} if clock == 0 else set()
    words = set()
    for last in range(1, clock-depth+2):
        y, rem = divmod((1 << last)*q-1, 3)
        if rem == 0 and y > 0 and y % 3:
            words.update(w+(y % modulus,) for w in enumerate_row(y, depth-1, clock-last, modulus))
    return words


def check_sparse_paths():
    """Expand the shifted identity independently on ordinary forward trajectories."""
    segments = balanced = 0
    for source in range(3, 4000, 2):
        q = source
        clock = ones = terms = 0
        valuations = []
        for depth in range(1, 26):
            value = 3*q+1
            gap = (value & -value).bit_length()-1
            q = value >> gap
            if q == 1:
                break
            defect = (1 << gap)-4
            terms = 3*terms + (defect << clock)
            if defect:
                valuations.append(clock + min(2, gap))
            clock += gap
            ones += gap == 1
            check(3**depth*(source-1) == ((q-1) << clock) + terms, "shifted identity")
            terminal_valuation = clock + (((q-1) & -(q-1)).bit_length()-1)
            extended = valuations + [terminal_valuation]
            check(all(a < b for a, b in zip(extended, extended[1:])), "subsum valuations")
            segments += 1
            if clock == 2*depth:
                terminal = q << clock
                carry = terminal - 3**depth*source
                check(carry > 0, "nonpositive affine carry")
                j = ((terminal-1)//carry).bit_length()
                check(terminal <= carry << j, "relative carry exponent")
                check(depth <= (j+5*ones+1)*(1 << (2*ones+1))+2*ones, "sparse bound")
                balanced += 1
    return segments, balanced


def main():
    rows = scripts = compatible_cases = incompatible_cases = free_words = 0
    for depth in (2, 3):
        for q in range(1, 2*3**(depth+1), 2):
            if q % 3 == 0:
                continue
            for clock in range(1, 6*(depth+1)+15):
                actual = enumerate_row(q, depth, clock, 3)
                words = set(product((1, 2), repeat=depth))
                predicted = {w for w in words if compatible(q, w, clock, 3)}
                check(actual <= predicted, "signature failed its necessity test")
                if clock >= 6*(depth+1)+1:
                    check(actual == predicted, "missing compatible word above cutoff")
                rows += 1
                scripts += len(words)
    check((1, 1) not in enumerate_row(13, 2, 18, 3)
          and compatible(13, (1, 1), 18, 3), "sharp two-gap witness failed")

    for k in range(1, 5):
        modulus = 3**k
        units = [r for r in range(modulus) if r % 3]
        order = len(units)
        for depth in (2, 3, 5, 9):
            floor = 3*order*(depth+1)+1
            for i in range(12):
                q = (2*modulus*(1+i*i) + (1 if i%2 else 5))
                w = tuple(units[(3*i+j*j+7*j) % order] for j in range(depth))
                for clock in range(floor, floor+2*order):
                    gaps = construct(q, w, clock, k)
                    if gaps is None:
                        incompatible_cases += 1
                    else:
                        replay(q, gaps, w, clock, modulus)
                        compatible_cases += 1
                # At fixed clock each of the internal slots can absorb the signature.
                for slot in range(1, depth):
                    clock = floor+i
                    matches = []
                    for r in units:
                        v = w[:slot]+(r,)+w[slot+1:]
                        if compatible(q, v, clock, modulus):
                            matches.append(v)
                    check(len(matches) == 1, "missing or ambiguous compensation trit")
                    gaps = construct(q, matches[0], clock, k)
                    replay(q, gaps, matches[0], clock, modulus)
                    free_words += 1

    # Construct an entire Boolean cube at one exact row, with the same genuine suffix.
    gate = (1 << 63)-1
    m, b = 10, 70
    q = gate
    suffix = []
    for _ in range(b-m):
        n = 3*q+1
        e = (n & -n).bit_length()-1
        suffix.append((q % 3, e))
        q = n >> e
    remaining = 2*b - sum(e for _,e in suffix)
    sources = set()
    for free in product((1,2), repeat=m-1):
        variants = [free+(r,) for r in (1,2)]
        compatible_words = [w for w in variants if compatible(gate, w, remaining, 3)]
        check(len(compatible_words)==1, "clock phase did not single out one mark")
        w = compatible_words[0]
        gaps = construct(gate, w, remaining, 1)
        x = replay(q, gaps+tuple(e for _,e in suffix), w+tuple(r for r,_ in suffix), 2*b, 3)
        check((3*gate+1)*3**b*x <= 3*gate*4**b*q, "carry bound failed")
        sources.add(x)
    check(len(sources)==2**(m-1), "distinct mark words collided")
    segments, balanced = check_sparse_paths()
    print(json.dumps(dict(direct_rows=rows, direct_word_tests=scripts,
                          higher_precision_constructed=compatible_cases,
                          incompatible_signatures=incompatible_cases,
                          compensated_words=free_words, cube_sources=len(sources),
                          cube_odd_steps=b, cube_shortcut_steps=2*b,
                          shifted_segments=segments, balanced_sparse_rows=balanced), indent=2))


if __name__ == "__main__":
    main()
