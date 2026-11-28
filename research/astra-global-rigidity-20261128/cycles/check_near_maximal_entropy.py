"""Exact finite checks of valuation words, deficits, and block renewal.

This checks the finite combinatorial interface, not a pressure limit or
any infinite Collatz assertion. Integer polynomial exponents encode the
full rational deficit, with no binning or floating arithmetic.
"""

from collections import Counter
from fractions import Fraction


def require(ok, message):
    if not ok:
        raise ArithmeticError(message)


def floor_log2_ratio(numerator, denominator):
    exponent = numerator.bit_length() - denominator.bit_length()
    if exponent >= 0:
        return exponent if numerator >= denominator << exponent else exponent - 1
    return exponent if numerator << -exponent >= denominator else exponent - 1


def convolve(left, right):
    result = Counter()
    for a, multiplicity_a in left.items():
        for b, multiplicity_b in right.items():
            result[a + b] += multiplicity_a * multiplicity_b
    return result


def finite_case(length, initial_weight):
    p, q = initial_weight.numerator, initial_weight.denominator
    floors = [floor_log2_ratio(3**t * q, p) for t in range(length + 1)]
    gaps = [floors[t + 1] - floors[t] for t in range(length)]
    require(floors[0] == 0 and all(g in (1, 2) for g in gaps), "rotation coding")
    weights = [Fraction(p * 2**floors[t], q * 3**t) for t in range(length)]
    require(all(Fraction(1, 2) < a <= 1 for a in weights), "phase weights")
    denominator = q * 3 ** (length - 1)
    baseline = sum(p * 2**floors[t] * 3 ** (length - 1 - t) for t in range(length))
    total_clock = floors[length] + 1

    def site_loss(t, depth):
        require(0 <= depth <= floors[t], "nonnegative partial clock")
        return p * (2**floors[t] - 2 ** (floors[t] - depth)) * 3 ** (length - 1 - t)

    direct = Counter()
    word_count = 0
    maximal_blocks = 0

    def visit_word(prefix, partial, partials):
        nonlocal word_count, maximal_blocks
        t = len(prefix)
        if t == length - 1:
            last = total_clock - partial
            require(last >= 1, "forced final positive valuation")
            word = prefix + (last,)
            depths = tuple(floors[i] - partials[i] for i in range(length))
            require(depths[0] == 0 and all(j >= 0 for j in depths), "depth admissibility")
            for i in range(length - 1):
                require(0 <= depths[i + 1] <= depths[i] + gaps[i] - 1, "depth transition")
                require(word[i] == gaps[i] + depths[i] - depths[i + 1], "interior inverse coding")
            require(last == gaps[-1] + 1 + depths[-1], "terminal inverse coding")
            carry = sum(p * 2**partials[i] * 3 ** (length - 1 - i) for i in range(length))
            deficit = baseline - carry
            require(deficit == sum(site_loss(i, depths[i]) for i in range(length)), "exact deficit")
            blocks = []
            i = 1
            while i < length:
                if depths[i] == 0:
                    i += 1
                    continue
                start = i
                require(depths[i] == 1 and gaps[i - 1] == 2, "positive block entry")
                require(weights[i] / 2 >= Fraction(1, 3), "entry costs one third")
                while i < length and depths[i] > 0:
                    i += 1
                block_length = i - start
                block_loss = sum(site_loss(t, depths[t]) for t in range(start, i))
                require(12 * block_loss >= (3 * block_length + 1) * denominator, "full block loss")
                blocks.append((start, block_length))
            positive_sites = sum(j > 0 for j in depths)
            require(12 * deficit >= (3 * positive_sites + len(blocks)) * denominator, "disjoint block budget")
            direct[deficit] += 1
            word_count += 1
            maximal_blocks += len(blocks)
            return
        for letter in range(1, floors[t + 1] - partial + 1):
            visit_word(prefix + (letter,), partial + letter, partials + (partial + letter,))

    visit_word((), 0, (0,))

    activity_cache = {}

    def activity(start, block_length):
        key = (start, block_length)
        if key in activity_cache:
            return activity_cache[key]
        result = Counter()
        if gaps[start - 1] == 2:
            def shapes(depths):
                if len(depths) == block_length:
                    loss = sum(site_loss(start + i, h) for i, h in enumerate(depths))
                    result[loss] += 1
                    return
                position = start + len(depths) - 1
                for new_depth in range(1, depths[-1] + gaps[position]):
                    shapes(depths + (new_depth,))
            shapes((1,))
        require(sum(result.values()) <= 4 ** (block_length - 1), "shape count")
        activity_cache[key] = result
        return result

    renewal = {-1: Counter({0: 1}), 0: Counter({0: 1})}
    for end in range(1, length):
        polynomial = renewal[end - 1].copy()
        for block_length in range(1, end + 1):
            start = end - block_length + 1
            polynomial.update(convolve(activity(start, block_length), renewal[start - 2]))
        renewal[end] = polynomial
    require(renewal[length - 1] == direct, "untruncated renewal polynomial equals direct word enumeration")
    require(direct[0] == 1, "unique zero-deficit word")
    return word_count, maximal_blocks


def main():
    cases = words = blocks = 0
    for initial_weight in map(Fraction, ("1", "3/4", "2/3", "5/8")):
        for length in range(1, 14):
            count, block_count = finite_case(length, initial_weight)
            cases += 1
            words += count
            blocks += block_count
    print(f"{cases} exact phase/length cases, {words} valuation words, {blocks} positive blocks; all renewal polynomials and loss bounds match")


if __name__ == "__main__":
    main()
