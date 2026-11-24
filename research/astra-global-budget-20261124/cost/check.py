"""Bounded exact controls for ordinary prefix toll and equal-grade gains."""

from fractions import Fraction as Q
from itertools import product


def require(condition, message):
    if not condition:
        raise ValueError(message)


def step(n):
    return (3 * n + 1) // 2 if n % 2 else n // 2


def carry(bits):
    value = 0
    for index, bit in enumerate(bits):
        if bit:
            value = 3 * value + 2**index
    return value


def balanced(bits):
    for length in range(1, len(bits) + 1):
        ones = [sum(bits[j:j + length]) for j in range(len(bits) - length + 1)]
        if max(ones) - min(ones) > 1:
            return False
    return True


def main():
    maxima = {}
    for t in range(12):
        for bits in product((0, 1), repeat=t):
            p = sum(bits)
            c = carry(bits)
            key = t, p, c % 3**p
            maxima[key] = max(c, maxima.get(key, c))

    states = list(range(161))
    counts = [0] * 161
    carries = [0] * 161
    gains = [0] * 161
    comparisons = 0
    for t in range(12):
        minimum = {}
        for x in range(1, 161):
            z, p, c = states[x], counts[x], carries[x]
            key = t, p, c % 3**p
            gain = (maxima[key] - c) // 3**p
            y = minimum.setdefault((z, p), x)
            require(2**t * z == 3**p * x + c, "affine equation")
            require(gain == x - y and gain >= gains[x], "ordinary minimum and monotonicity")
            gains[x] = gain
            comparisons += 1
        for x in range(1, 161):
            bit = states[x] % 2
            if bit:
                carries[x] = 3 * carries[x] + 2**t
                counts[x] += 1
            states[x] = step(states[x])

    blocks = ((1, 1, 0), (1, 0, 1))
    for m in range(1, 10):
        residues = {carry(sum(seq, ())) % 3**(2 * m)
                    for seq in product(blocks, repeat=m)}
        require(len(residues) == 2**m, "block carry collision")

    record = -1
    records = []
    max_score = 0
    prior = []
    total_blocks = 0
    for x in range(1, 351):
        path = [x]
        while path[-1] != 1:
            require(len(path) <= 1000, "bounded first-hit control")
            path.append(step(path[-1]))
        tau = len(path) - 1
        rawbits = [z % 2 for z in path[:-1]]
        p = 0
        past_max = max_score
        for t, z in enumerate(path):
            if z > 2 and t >= 8 * (x.bit_length() + past_max):
                require(2 * p > t + past_max, "grade cutoff")
            max_score = max(max_score, 2 * p - t)
            if t < tau:
                p += z % 2
        max_score = max(max_score, 2 * p - tau + 1)
        if tau > record:
            records.append(x)
            record = tau
            for t in range(max(0, tau - 1)):
                require(all(t >= len(old) or old[t] != path[t] for old in prior),
                        "strict record premature merge")
        prior.append(path)
        start = 0
        while start < tau:
            end = start + 1
            while end < tau and balanced(rawbits[start:end]):
                end += 1
            upper = Q(0)
            cost = Q(0)
            end_bits = path[end].bit_length()
            for j in range(start, end):
                b = path[j].bit_length()
                r = end - j
                require(r <= 12 * b, "suffix deadline")
                cost += Q(1, max(b, path[j + 1].bit_length()))
                upper += Q(25, end_bits + r)
            require(cost <= upper, "block toll")
            total_blocks += 1
            start = end
    print(f"carry comparisons={comparisons}, block residue depths=9, "
          f"stopping records={len(records)}, cost blocks={total_blocks}")


if __name__ == "__main__":
    main()
