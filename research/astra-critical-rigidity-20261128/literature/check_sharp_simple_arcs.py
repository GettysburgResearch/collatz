"""Independent integer replay of the simple rational sharpness constructions."""
from math import gcd
import json


def check(condition, message):
    if not condition:
        raise ValueError(message)


def successors(start, denominator, steps):
    numerators, bits = [start], []
    for _ in range(steps):
        n = numerators[-1]
        bit = n % 2
        bits.append(bit)
        numerators.append((3 * n + denominator) // 2 if bit else n // 2)
    return numerators, bits


def routed_witness(first, count, length, grade, periods, charged):
    base_two = 2**length
    base_three = 3**grade
    delta = base_two - base_three
    check(0 < charged < count and delta > 0, "bad parameter bounds")
    Q = base_two**periods - base_three**periods
    q = delta * Q
    words, carries = [], []
    for i in range(count):
        n = first + i
        y, bits = successors(n, 1, length)
        check(y[-1] == 1 and sum(bits) == grade, "router witness")
        carry = base_two - base_three * n
        carry_direct = sum(2**j * 3**sum(bits[j + 1:])
                           for j, bit in enumerate(bits) if bit)
        check(carry == carry_direct and carry > 0, "carry from actual word")
        words.append(bits)
        carries.append(carry)
    check(all(carries[i] - carries[i + 1] == base_three
              for i in range(count - 1)), "center progression")
    start = carries[0] * Q + base_three * base_two**periods
    check(gcd(start, q) == 1 and gcd(q, 6) == 1, "complete rational denominator")
    steps = charged * length * periods
    y, bits = successors(start, q, (charged + 1) * length * periods)
    for i in range(charged + 1):
        left = i * length * periods
        check(y[left] == carries[i] * Q + base_three * base_two**periods,
              "prescribed positive rational at each boundary")
        check(bits[left:left + length * periods] == words[i] * periods,
              "actual powered word at every step")
    check(len(set(y[:steps + 1])) == steps + 1, "simple charged prefix")
    check(all(gcd(n, q) == 1 for n in y), "denominator at every time")
    return steps + 1, q.bit_length()


def two_runs():
    total = 0
    for m in range(3, 82, 2):
        q = 2**m - 1
        a = 2**m
        y, bits = successors(a, q, 2 * m)
        check(bits == [0] * m + [1] * m, "two-run itinerary")
        check(len(set(y)) == len(y), "two-run simplicity")
        check(y[m:] == [3**j * 2**(m - j) - q for j in range(m + 1)],
              "two-run closed formula")
        total += len(y)
    return total


def main():
    repetitions = (6, 9, 12, 18)
    families = vertices = max_bits = 0
    for first, count, length, grade in ((98, 5, 18, 7), (2987, 14, 34, 14)):
        for k in range(1, count):
            for r in repetitions:
                size, den_bits = routed_witness(first, count, length, grade, r, k)
                families += 1
                vertices += size
                max_bits = max(max_bits, den_bits)
    print(json.dumps({
        "charged_simple_prefixes": families,
        "charged_vertices_replayed": vertices,
        "largest_exact_denominator_bit_length": max_bits,
        "largest_piece_count": 13,
        "simple_two_run_vertices": two_runs(),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
