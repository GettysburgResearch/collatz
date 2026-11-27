"""Exact finite controls for negative rational witnesses at the binary gate."""

from math import gcd
import json


def check(condition, detail):
    if not condition:
        raise ArithmeticError(detail)


def prefix(z, q, steps):
    bits = []
    states = [z]
    for _ in range(steps):
        bit = z % 2
        bits.append(bit)
        z = (3 * z + q) // 2 if bit else z // 2
        states.append(z)
    return tuple(bits), states


def experiment(depth, height):
    dictionary = {}
    for p in range(1, height + 1):
        for q in range(1, height + 1, 2):
            if gcd(p, q) == 1:
                bits, states = prefix(-p, q, depth)
                for length in range(1, depth + 1):
                    dictionary.setdefault(bits[:length], (p, q, states[length]))
    groups = {}
    total = 0
    for m in range(1, 1 << depth, 2):
        bits, states = prefix(m, 1, depth)
        odd = 0
        for i, bit in enumerate(bits, start=1):
            odd += bit
            if 8 * odd < 5 * i:
                break
        else:
            total += 1
            # All words of length one occur. Shortest allowed partition.
            pieces = [None] * (depth + 1)
            pieces[0] = ()
            for end in range(1, depth + 1):
                best = None
                for start in range(end):
                    if bits[start:end] not in dictionary:
                        continue
                    candidate = pieces[start] + ((start, end),)
                    if best is None or len(candidate) < len(best):
                        best = candidate
                pieces[end] = best
            least = pieces[-1]
            for start, end in least:
                p, q, terminal = dictionary[bits[start:end]]
                a = end - start
                t = sum(bits[start:end])
                R = sum(bits[:start])
                x, y = states[start], states[end]
                check((1 << a) * (q * y - terminal) == 3**t * (q * x + p),
                      (m, start, end, "affine"))
                check((1 << a) <= q * x + p <= height * (x + 1),
                      (m, start, end, "height"))
                check((1 << (a + R)) <= height * 3**R * (m + 1),
                      (m, start, end, "transport"))
            k = len(least)
            group = groups.setdefault(k, [0, m, 0])
            group[0] += 1
            group[1] = min(group[1], m)
            group[2] += (1 << 60) // m
    return {"depth": depth, "height": height, "all_gated": total,
            "groups_by_shortest_piece_count": groups}


def main():
    # Floored sums in each group differ from 2^60 times its true harmonic
    # mass by less than the group size. Every operation above is integer.
    deltas = [experiment(n, h) for n, h in [(8, 3), (12, 7), (16, 11)]]
    print(json.dumps(deltas, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
