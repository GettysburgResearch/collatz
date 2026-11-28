"""Exact finite controls for repetition trees, previous factors and shared rules."""

from collections import Counter
from functools import cache
from itertools import combinations, product


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def twos(nonzero):
    require(nonzero != 0, "valuation of zero")
    absolute = abs(nonzero)
    return (absolute & -absolute).bit_length() - 1


def shortcut(value):
    return (3 * value + 1) // 2 if value % 2 else value // 2


@cache
def optimal_rule(word):
    if len(word) == 1:
        return 1, ("bit", word)
    options = []
    for offset in range(1, len(word)):
        left, right = word[:offset], word[offset:]
        options.append((1 + optimal_rule(left)[0] + optimal_rule(right)[0], ("cat", left, right)))
    for period in range(1, len(word) // 2 + 1):
        base, exponent = word[:period], len(word) // period
        if word == base * exponent:
            options.append((1 + optimal_rule(base)[0], ("pow", base, exponent)))
    return min(options)


def check_exhaustive_tree_sizes(limit):
    # Independent bottom-up enumeration by syntax size, with bounded expansion.
    words = [set(), {"0", "1"}]
    best = {"0": 1, "1": 1}
    for size in range(2, 2 * limit):
        group = set()
        for base in words[size - 1]:
            group.update(base * q for q in range(2, limit // len(base) + 1))
        for left_size in range(1, size - 1):
            for left in words[left_size]:
                group.update(left + right for right in words[size - left_size - 1] if len(left) + len(right) <= limit)
        words.append(group)
        for word in group:
            best.setdefault(word, size)
    for length in range(1, limit + 1):
        for bits in product("01", repeat=length):
            word = "".join(bits)
            require(best[word] == optimal_rule(word)[0], "minimum syntax size")
    return len(best)


def longest_parse(word, states, admitted):
    result = []
    start = 0
    while start < len(word):
        choices = []
        for previous in range(start):
            if not admitted(start, previous):
                continue
            length = 0
            while start + length < len(word) and word[previous + length] == word[start + length]:
                length += 1
            exact = twos(states[start] - states[previous])
            require(length == min(exact, len(word) - start), "pair cylinder length")
            if length:
                choices.append((length, -previous, exact))
        if choices:
            length, negative_address, exact = max(choices)
            result.append((start, -negative_address, exact))
            start += length
        else:
            start += 1
    return result


def check_transport(states, copies, counters):
    for start, address, length in copies:
        while len(states) <= start + length:
            states.append(shortcut(states[-1]))
        require((states[start] - states[address]) % (2 ** length) == 0, "copy root valuation")
        require((states[start + length] - states[address + length]) % 2 == 1, "first mismatch")
    for arity in range(2, min(len(copies), 4) + 1):
        for selected in combinations(copies, arity):
            first, last = selected[0][0], selected[-1][0]
            odds = sum(value % 2 for value in states[first:last])
            terms = [3 ** odds * (states[first] - states[selected[0][1]])]
            for (start, previous, length), (next_start, next_previous, _) in zip(selected, selected[1:]):
                end = start + length
                require(end <= next_start, "selected copy overlap")
                word = [value % 2 for value in states[end:next_start]]
                affine = 0
                for index, bit in enumerate(word):
                    affine = (3 if bit else 1) * affine + bit * (2 ** index)
                odd, gap = sum(word), len(word)
                terminal = states[previous + length]
                root = states[next_previous]
                carry = 3 ** odd * terminal + affine - 2 ** gap * root
                require(carry % 2 == 1, "boundary carry valuation")
                require(abs(carry) <= 3 ** odd * 2 ** (gap - odd) * (1 + max(terminal, root)), "integer reference carry height")
                later_odds = sum(x % 2 for x in states[next_start:last])
                terms.append(2 ** (end - first) * 3 ** later_odds * carry)
            rhs = 2 ** (last - first) * (states[last] - states[selected[-1][1]])
            require(sum(terms) == rhs, "composed exact transport")
            for size in range(1, arity + 1):
                require(all(sum(subset) != 0 for subset in combinations(terms, size)), "zero subsum")
            counters["transports"] += 1


def check_shared_grammar(word, states, counters):
    rules = {}
    earliest_boundary = {}
    packets = []
    completed = {}

    def visit(phrase, offset):
        if phrase in completed:
            packets.append((offset, completed[phrase], len(phrase)))
            return
        rule = optimal_rule(phrase)[1]
        rules[phrase] = rule
        if rule[0] == "bit":
            packets.append((offset, None, 1))
        else:
            child = rule[1]
            earliest_boundary[phrase] = offset + len(child)
            visit(child, offset)
            if rule[0] == "cat":
                visit(rule[2], offset + len(child))
            else:
                packets.append((offset + len(child), offset, len(phrase) - len(child)))
        completed[phrase] = offset

    visit(word, 0)
    require(len(packets) <= 2 * len(rules) + 1, "shared grammar packet count")
    require(sum(length for _, _, length in packets) == len(word), "packet coverage")
    for start, address, length in packets:
        if address is None:
            require(length == 1, "literal length")
        else:
            require(address < start and word[start:start + length] == word[address:address + length], "shared packet expansion")
            require(2 ** length <= max(states[:start + 1]) + 1, "packet height bound")
            counters["shared copies"] += 1
    for horizon in (1, 2, 3, 5):
        for size in range(1, len(word) // horizon + 1):
            end = horizon * size
            factors = {word[pos:pos + size] for pos in range(end - size + 1)}
            bound = (2 if size == 1 else 0) + sum(min(size, pos) for pos in earliest_boundary.values() if pos <= end)
            require(len(factors) <= bound, "first-boundary factor count")
            counters["factor bounds"] += 1


def main():
    counts = Counter()
    counts["enumerated words"] = check_exhaustive_tree_sizes(7)
    for source in list(range(1, 91)) + [127, 171, 231, 255, 327, 639, 703, 871, 6171, 2 ** 18 - 1]:
        states = []
        visited = set()
        value = source
        while value not in visited and len(states) < 60:
            states.append(value)
            visited.add(value)
            value = shortcut(value)
        word = "".join(str(state % 2) for state in states)
        counts["simple sources"] += 1
        check_shared_grammar(word, states, counts)
        for begin in range(len(word)):
            first = states[begin]
            for period in range(1, (len(word) - begin) // 2 + 1):
                base = word[begin:begin + period]
                for exponent in range(2, (len(word) - begin) // period + 1):
                    if word[begin:begin + exponent * period] != base * exponent:
                        break
                    difference = states[begin + period] - first
                    require(difference % 2 ** ((exponent - 1) * period) == 0, "literal power divisibility")
                    require(2 ** (exponent * period) <= 3 ** period * (first + 1), "power height")
                    require(2 ** (exponent * period) <= (first + 1) ** 5, "power window")
                    counts["literal powers"] += 1
        for admitted in (lambda _a, _b: True, lambda a, b: 3 * b <= a):
            copies = longest_parse(word, states, admitted)
            check_transport(states, copies, counts)
    print(", ".join(f"{key}={counts[key]}" for key in sorted(counts)))


if __name__ == "__main__":
    main()
