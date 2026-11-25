"""Replay exact word offsets, shared ordinary endpoints, and weights."""
from fractions import Fraction
from itertools import product
from math import prod


def odd_step(n):
    m = 3 * n + 1
    a = (m & -m).bit_length() - 1
    return m >> a, a


def offset(word):
    clock = 0
    carry = 0
    for gap in word:
        carry = 3 * carry + (1 << clock)
        clock += gap
    return clock, carry


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def check(k, budgets, d=0, source_class=0, basin=False):
    r = len(budgets)
    require(2 * r <= k, "more pair positions than steps")
    choices = [range(1, b + 2, 2 * 3 ** (2 * j + d - 1))
               for j, b in enumerate(budgets, start=1)]
    words = []
    for selected in product(*choices):
        pairs = zip(selected, budgets)
        word = tuple(e for a, b in pairs for e in (a, b + 2 - a))
        words.append(word + (1,) * (k - 2 * r))
    modulus = 3 ** k
    lifted_modulus = modulus * 3 ** d
    clock = k + sum(budgets)
    residues = set()
    for word in words:
        s, carry = offset(word)
        require(s == clock, "inconsistent clock")
        numerator = carry + modulus * source_class
        residues.add((numerator * pow(1 << s, -1, lifted_modulus)) % lifted_modulus)
    require(len(residues) == 1, "different endpoint residues")
    residue = residues.pop()
    if basin:
        # Exhaust the order of 4 for this small fixture only.
        endpoint = next(y for n in range(1, 2 * lifted_modulus + 1)
                        if (y := (4 ** n - 1) // 3) >= modulus
                        and y % lifted_modulus == residue)
        require(odd_step(endpoint)[0] == 1, "endpoint missed the basin")
    else:
        endpoint = residue + (2 if residue % 2 else 1) * lifted_modulus
    sources = set()
    max_ratio = Fraction()
    for word in words:
        _, carry = offset(word)
        source, rem = divmod((endpoint << clock) - carry, modulus)
        require(not rem and source > 0 and source % 2, "illegal ordinary source")
        require(source % (3 ** d) == source_class, "wrong retained source class")
        current = source
        for gap in word:
            current, a = odd_step(current)
            require(a == gap, "incorrect deterministic gap")
        require(current == endpoint, "different ordinary terminal")
        sources.add(source)
        max_ratio = max(max_ratio, Fraction(carry, endpoint << clock))
    multiplicity = prod(map(len, choices))
    require(len(sources) == multiplicity, "non-injective word to source map")
    require(max_ratio < Fraction(1, 2 ** k), "relative-carry cut failed")
    print(f"k={k} S={clock} pairs={r} distinct_sources={multiplicity}"
          f" one_endpoint=true max_relative_offset<2^-{k}"
          f" odd_Haar_mass={multiplicity}*2^-{clock}"
          f" source_class={source_class}_mod_{3 ** d} basin_checked={basin}")


if __name__ == "__main__":
    check(2, [6], basin=True)
    check(12, [6])
    check(120, [60], d=1, source_class=2)
    check(240, [60, 60])
    check(120, [60, 60])  # Exact central clock 2k.
