"""Exact checks of the Mersenne carry reconstruction and both sharp examples."""

from fractions import Fraction


def positions(value):
    while value:
        low = value & -value
        yield low.bit_length() - 1
        value -= low


def first_hit(source):
    time, odd_positions = 0, []
    while source != 1:
        if source % 2:
            odd_positions.append(time)
            source = 3 * source + 1
        gap = (source & -source).bit_length() - 1
        source >>= gap
        time += gap
    return time, odd_positions


def power_two(exponent):
    return Fraction(2) ** exponent


def amplitude(n):
    t, s = first_hit(n)
    return power_two(t - 2 * len(s)) / n


def reconstruct(source, anchor, period):
    base = 2**period
    assert (source - anchor) % (base - 1) == 0
    assert (2 * source - anchor) % (2 * base - 1) == 0
    time, odd = first_hit(source)
    grade = len(odd)
    tokens = list(positions(3**grade * anchor))
    for i, step in enumerate(odd):
        tokens.extend(step + bit for bit in positions(3 ** (grade - 1 - i)))
    capacity = len(tokens)
    buckets = [[] for _ in range(period)]
    for origin in tokens:
        buckets[origin % period].append([(origin, 0)])
    pending = [i for i, group in enumerate(buckets) if len(group) > 1]
    while pending:
        at = pending.pop()
        if len(buckets[at]) < 2:
            continue
        merged = buckets[at].pop() + buckets[at].pop()
        nxt = (at + 1) % period
        buckets[nxt].append([(origin, dist + 1) for origin, dist in merged])
        if len(buckets[nxt]) > 1:
            pending.append(nxt)
        if len(buckets[at]) > 1:
            pending.append(at)
    remaining = [group for bucket in buckets for group in bucket]
    assert len(remaining) == 1
    assert len(remaining[0]) == capacity
    for orig, dist in remaining[0]:
        assert 0 <= dist < capacity
        assert (orig + dist - time) % period == 0
    anchor_bit = next(positions(anchor))
    rt = anchor_bit + (time - anchor_bit) % period
    assert anchor_bit <= rt < anchor_bit + capacity
    degree = (time - rt) // period
    coeff = [Fraction() for _ in range(degree + 1)]
    coeff[degree] = power_two(rt)
    for i, step in enumerate(odd):
        ri = rt - (rt - step) % period
        assert rt - capacity < ri <= rt
        mi = (step - ri) // period
        assert 0 <= mi <= degree
        coeff[mi] -= 3 ** (grade - 1 - i) * power_two(ri)
    coeff = [v / 3**grade for v in coeff]
    assert sum(c * base**i for i, c in enumerate(coeff)) == source
    assert all(c <= 0 for c in coeff[:-1])
    assert sum(coeff) == 2 * sum(c / 2**i for i, c in enumerate(coeff)) == anchor
    assert coeff == [0, anchor]


def run():
    for k in (1801, 2026):
        for d in range(1, 101):
            reconstruct((2**k) * d, d, k)
    for k in range(3, 50, 6):
        e = 2 * k
        y = (340 * 2**e - 7) // 9
        assert (y - 37) % (2**k - 1) == 0
        assert first_hit(y) == (e + 10, [0, 2, e + 2])
        assert amplitude(y) > amplitude(37) == Fraction(8, 37)
    for k in range(8, 100, 18):
        e = k * (k + 1)
        y = (340 * 2**e - 7) // 9
        n = 2**k * y
        assert (n - 37) % (2**k - 1) == (2 * n - 37) % (2 ** (k + 1) - 1) == 0
        assert first_hit(n) == (k + e + 10, [k, k + 2, k + e + 2])
        assert amplitude(n) == Fraction(2 ** (e + 4), y) > Fraction(36, 85)
    print("PASS 200 ordinary carry reconstructions, 8 single-modulus and 6 paired-modulus sharp witnesses")


if __name__ == "__main__":
    run()
