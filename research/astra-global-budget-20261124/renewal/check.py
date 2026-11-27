"""Exact finite controls for completed-word rows and transfer to ordinary pairs."""
from collections import defaultdict
from fractions import Fraction
import json


def require(condition):
    if not condition:
        raise RuntimeError("finite paired-pressure check failed")


def advance(value):
    return (3 * value + 1) // 2 if value % 2 else value // 2


def run(value, steps):
    word = []
    for _ in range(steps):
        word.append(value % 2)
        value = advance(value)
    return tuple(word), value


def complete_pair(word, first, second):
    """Replay successive first returns and common padding to the odd sentinel."""
    index = blocks = 0
    while index < len(word):
        a = b = 0
        while index < len(word):
            require(first % 2 == word[index])
            a += first % 2
            b += second % 2
            first, second = advance(first), advance(second)
            index += 1
            if a == b and 5 * first == second:
                break
        else:
            return None
        while first % 2 == 0 and index < len(word):
            require(word[index] == 0 and second % 2 == 0)
            first, second = first // 2, second // 2
            index += 1
        if first % 2 == 0:
            return None
        blocks += 1
    return blocks, first, second


def select_rows(max_clock):
    rows = defaultdict(list)
    for e in range(1, max_clock + 1):
        seen = set()
        for n in range(1, 2 ** (e + 1), 2):
            word, y = run(n, e)
            if y % 2 == 0:
                continue
            parsed = complete_pair(word, n, 5 * n)
            if parsed is None:
                continue
            require(word not in seen and parsed[1:] == (y, 5 * y))
            seen.add(word)
            p = sum(word)
            carry = 2 ** e * y - 3 ** p * n
            require(carry > 0 and carry % 3)
            if carry <= 4 * 2 ** e:
                rows[p, e].append((carry, word))
    return rows


def check_coarse_prefix(r, p, s):
    """Replay the correcting word on all unit prefixes at precision s."""
    modulus = 3 ** (p + 1)
    checked = 0
    for v in range(1, 3 ** s):
        if v % 3 == 0:
            continue
        target = v if v % 2 else v + 3 ** s
        exponents = []
        for _ in range((s + 1) // 2):
            h = next(h for h in range(6, 24)
                     if (2 ** h * target - 7) % 9 == 0
                     and (2 ** h * target - 7) % 27 != 0)
            target = (2 ** h * target - 7) // 9
            exponents.append(h)
        carry = 0
        total = 0
        for h in reversed(exponents):
            carry = 9 * carry + 7 * 2 ** total
            total += h
        multiplier = 9 ** len(exponents)
        output_modulus = multiplier * modulus
        z = (multiplier * r + carry) * pow(2 ** total, -1, output_modulus) % output_modulus
        require(z % (3 ** s) == v)
        for odd_output in (z + (z % 2 == 0) * output_modulus,
                           z + (2 + (z % 2 == 0)) * output_modulus):
            x, rem = divmod(2 ** total * odd_output - carry, multiplier)
            require(rem == 0 and x > 0 and x % modulus == r and x % 2)
            left_word, left = run(x, total)
            right_word, right = run(5 * x, total)
            require(left == odd_output and right == 5 * odd_output)
            require(sum(left_word) == sum(right_word) == 2 * len(exponents))
            checked += 1
    return checked


def main():
    max_clock = 16
    rows = select_rows(max_clock)
    memberships = imports = sources = nontrivial = coarse = 0
    largest = (0, 0, 0)
    for (p, e), entries in sorted(rows.items()):
        scale = Fraction(2 ** e, 3 ** p)
        modulus = 3 ** (p + 1)
        inverse = pow(2 ** e, -1, modulus)
        groups = defaultdict(list)
        for carry, word in entries:
            excluded = carry * inverse % modulus
            for digit in (1, 2):
                r = (excluded + digit * 3 ** p) % modulus
                require(r % 3 and (2 ** e * r - carry) % modulus != 0)
                groups[r].append((carry, word))
        require(sum(map(len, groups.values())) == 2 * len(entries))
        memberships += 2 * len(entries)
        cap = 4 * scale + 1
        top = max(map(len, groups.values()))
        require(top <= cap)
        largest = max(largest, (top, p, e))
        mean = Fraction(len(entries), 3 ** p)
        good = [r for r in groups if len(groups[r]) >= mean / 2]
        require(Fraction(len(good), 2 * 3 ** p) * cap >= mean / 2)
        if p > 5 or scale < 1:
            continue
        coarse += sum(check_coarse_prefix(good[0], p, s) for s in (1, 2, 3))
        for q in (1, 5, 7, 25):
            r = max(good, key=lambda s: len(groups[s]))
            period = 2 * 3 ** (p + 2)
            h = next(h for h in range(period, 2 * period)
                     if pow(2, h, 9 * modulus) * q % (9 * modulus) == 9 * r + 7)
            middle = (2 ** h * q - 7) // 9
            require(middle % 64 == 49 and middle % modulus == r)
            # The one transfer block has six literal steps and h-6 exact halvings.
            a, y = run(middle, 6)
            b, z = run(5 * middle, 6)
            require(sum(a) == sum(b) == 2 and y == q * 2 ** (h-6) and z == 5 * y)
            distinct = set()
            for carry, word in groups[r]:
                x, rem = divmod(2 ** e * middle - carry, 3 ** p)
                require(rem == 0 and x > 0 and x % 2 and x % 3)
                require(scale * (middle - 4) <= x < scale * middle)
                result = complete_pair(word, x, 5 * x)
                require(result is not None and result[1:] == (middle, 5 * middle))
                distinct.add(x)
            require(len(distinct) == len(groups[r]))
            imports += 1
            sources += len(distinct)
            nontrivial += len(distinct) > 1
    print(json.dumps(dict(max_clock=max_clock, bounded_offset=4, nonempty_rows=len(rows),
                          complete_words=sum(map(len, rows.values())),
                          unit_cell_memberships=memberships, ordinary_fixed_pair_imports=imports,
                          imported_sources=sources, multiple_source_imports=nontrivial,
                          coarse_prefix_ordinary_two_arm_lifts=coarse,
                          maximum_cell_and_row=list(largest)), sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
