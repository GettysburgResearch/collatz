"""Exact small example for the mechanical-word physical-piece construction."""

from fractions import Fraction
from math import ceil, gcd, lcm


def shortcut(value):
    return (3 * value + 1) // 2 if value % 2 else value // 2


def adjust(starts, indices, number, modulus):
    assert abs(number) <= len(indices)
    step = modulus if number >= 0 else -modulus
    for i in indices[:abs(number)]:
        starts[i] += step


def check():
    length, odd_count, h, test_modulus = 485, 306, 3, 5
    word = [((i + 1) * odd_count) // length - (i * odd_count) // length
            for i in range(length)]
    denominator = 2**length - 3**odd_count
    q_unit = lcm(test_modulus, 3)
    modulus = 2**h * q_unit
    assert denominator > 1 and gcd(denominator, modulus) == 1
    numerator = 0
    for i, odd in enumerate(word):
        if odd:
            numerator = 3 * numerator + 2**i
    numerators = [numerator]
    for odd in word:
        current = numerators[-1]
        numerators.append(((3 * current + denominator) if odd else current) // 2)
    assert numerators.pop() == numerator

    starts, errors, blocks = [], [], []
    for i in range(0, length, h):
        value = Fraction(numerators[i], denominator)
        residue = numerators[i] * pow(denominator, -1, modulus) % modulus
        source = residue + modulus * round((value - residue) / modulus)
        starts.append(source)
        errors.append((source - value) / modulus)
        blocks.append(word[i:i + h])

    low_weight = h * odd_count // length
    groups = [[i for i, block in enumerate(blocks)
               if len(block) == h and sum(block) == weight]
              for weight in (low_weight, low_weight + 1)]
    for indices in groups:
        adjust(starts, indices, -round(sum(errors[i] for i in indices)), modulus)

    def replay():
        states, outputs = [], []
        for start, block in zip(starts, blocks):
            value = start
            for parity in block:
                assert value % 2 == parity
                states.append(value)
                value = shortcut(value)
                outputs.append(value)
        return states, outputs

    states, outputs = replay()
    imbalance = sum(states) - sum(outputs)
    assert imbalance % q_unit == 0
    target = imbalance // q_unit
    low = 3**low_weight - 2**h
    high = 3**(low_weight + 1) - 2**h
    total_low = (target * pow(low, -1, abs(high))) % abs(high)
    if 2 * total_low > abs(high):
        total_low -= abs(high)
    total_high = (target - low * total_low) // high
    assert low * total_low + high * total_high == target
    adjust(starts, groups[0], total_low, modulus)
    adjust(starts, groups[1], total_high, modulus)

    states, outputs = replay()
    successors = states[1:] + states[:1]
    defects = [out - expected for out, expected in zip(outputs, successors)]
    assert len(set(states)) == length and min(states) > 0
    assert all(n % 3 for n in states)
    assert sum(defects) == 0 and all(d % q_unit == 0 for d in defects)
    assert 0 < sum(d != 0 for d in defects) <= ceil(length / h)
    assert set(states) != set(outputs)
    print(f"PASS {length} distinct ordinary states, {sum(d != 0 for d in defects)} "
          f"nonzero joins, all multiples of {q_unit}, exact first moment.")


if __name__ == "__main__":
    check()
