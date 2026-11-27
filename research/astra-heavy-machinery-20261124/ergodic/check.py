"""Replay E2 using ordinary integer valuations, including at the exact rank threshold."""

from functools import cache
from itertools import product


def require(test, message):
    if not test:
        raise ArithmeticError(message)


def steps(source, count):
    x = source
    gaps = []
    for _ in range(count):
        require(x > 0 and x % 2 == 1, "invalid ordinary source")
        value = 3 * x + 1
        gap = (value & -value).bit_length() - 1
        x = value >> gap
        gaps.append(gap)
    return gaps, x


def carry(word):
    result = 0
    prefix_power = 1
    for gap in word:
        result = 3 * result + prefix_power
        prefix_power <<= gap
    return result


@cache
def inverse_four_logs(k):
    modulus = 3**k
    step = pow(4, -1, modulus)
    residue = 1
    logs = {}
    for exponent in range(modulus // 3):
        require(residue not in logs, "short principal-unit cycle")
        logs[residue] = exponent
        residue = residue * step % modulus
    require(residue == 1, "incomplete principal-unit cycle")
    return logs


def replay(x, word, b, u, rank):
    h = len(word) + 1
    gaps_x, t = steps(x, h)
    clock = sum(gaps_x)
    modulus = 3 ** (h + b + 1)
    chosen_carry = carry((*word, 1))
    unit = 1 + 3 * t - 3 * pow(2, -clock - rank, modulus) * (chosen_carry + 3**h * u)
    s = inverse_four_logs(h + b + 1)[unit % modulus]
    sibling = 4**s * t + (4**s - 1) // 3
    e = clock + rank - 2 * s - sum(word)
    require(e >= 2 * h + 1, "rank does not pay the terminal gap")
    z, remainder = divmod((sibling << (sum(word) + e)) - chosen_carry, 3**h)
    require(remainder == 0 and z > 0 and z % 2 == 1, "non-ordinary predecessor")
    require(z % 3**b == u, "wrong ternary digits")
    gaps_z, end_z = steps(z, h + 1)
    original, end_x = steps(x, h + 1)
    require(gaps_z[:h] == [*word, e], "physical gaps differ from the word")
    require(end_z == end_x, "wrong synchronized terminal value")
    require(sum(gaps_z) - sum(original) == rank, "wrong excess binary clock")
    shift = 1 << rank
    cubic_adjustment, remainder = divmod((1 << (clock + rank)) - (1 << (clock + rank - 2 * s)), 3)
    require(remainder == 0, "nonintegral additive adjustment")
    require(
        3**h * (z - shift * x) == shift * carry(gaps_x) - chosen_carry + cubic_adjustment,
        "ordinary additive distance identity failed",
    )
    return z.bit_length()


def main():
    words = [(), (1,), (2,), (17,), (1, 2), (3, 1), (2, 3, 1)]
    sources = [1, 3, 5, 7, 11, 19, 27, 31, 97, 483, (1 << 31) - 1]
    count = maximum = 0
    for x, word, b in product(sources, words, (1, 2, 3)):
        h = len(word) + 1
        base_rank = 2 * 3 ** (h + b) + sum(word) + 2 * h + 1
        for u, extra in product(range(3**b), (0, 1, 13)):
            bits = replay(x, word, b, u, base_rank + extra)
            maximum = max(maximum, bits)
            count += 1
    print(f"{count} physical E2 replays passed; largest witness has {maximum} bits")


if __name__ == "__main__":
    main()
