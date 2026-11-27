"""Exact binary-past residue, additive-energy and entropy witnesses."""
from collections import Counter, defaultdict
from functools import lru_cache
from itertools import combinations, product
import json


def require(test, label):
    if not test:
        raise ArithmeticError(label)


def ordinary_lift(word):
    power, numerator = 1, 0
    for a in word:
        numerator = 3*numerator+power
        power <<= a
    modulus = 2*power
    source = (power-numerator)*pow(3**len(word), -1, modulus) % modulus
    y = source+modulus
    for a in word:
        n = 3*y+1
        require(n & -n == 1 << a, "literal ordinary edge")
        y = n >> a
    return y


def differences(xs, modulus):
    return Counter((x-y) % modulus for x in xs for y in xs)


def energy(xs, modulus):
    return sum(c*c for c in differences(xs, modulus).values())


def split_energy(xs, modulus):
    if modulus == 1:
        return len(xs)**4
    fibers = defaultdict(list)
    for x in xs:
        fibers[x % 3].append(x//3)
    require(len(fibers) <= 2, "ternary branching")
    sub = list(fibers.values())
    e = sum(split_energy(a, modulus//3) for a in sub)
    if len(sub) == 2:
        da, db = (differences(a, modulus//3) for a in sub)
        mixed = sum(value*db[k] for k, value in da.items())
        require(mixed*mixed <= sum(t*t for t in da.values())*sum(t*t for t in db.values()),
                "integral mixed Cauchy")
        e += 4*mixed
    require(e == energy(xs, modulus), "raw versus recursive energy")
    return e


@lru_cache(None)
def interval_cap(length):
    if length <= 1:
        return length
    q, r = divmod(length, 3)
    sizes = [q+(i<r) for i in range(3)]
    return sum(sorted((interval_cap(v) for v in sizes), reverse=True)[:2])


def abstract_trees(depth):
    if depth == 0:
        return [(0,)]
    smaller = abstract_trees(depth-1)
    return [tuple(sorted([i+3*x for x in a]+[j+3*y for y in b]))
            for i, j in combinations(range(3), 2) for a, b in product(smaller, repeat=2)]


def check():
    row, residue_rows = {0}, []
    for depth in range(1, 9):
        mod = 3**depth
        row = {(3*v+1)*pow(1 << a, -1, mod) % mod for v in row for a in (1, 2)}
        actual = {ordinary_lift(word) % mod for word in product((1, 2), repeat=depth)}
        require(actual == row and len(row) == 2**depth, "actual endpoints and unique words")
        parents = Counter(v % (mod//3) for v in row)
        require(set(parents.values()) == {2}, "two children at every endpoint prefix")
        require(sum((2*y-x) % mod in row for x in row for y in row) == len(row),
                "no nonconstant modular progression")
        value = split_energy(row, mod)
        subset = sorted(row)[::3]
        sub_energy = split_energy(subset, mod)
        require(value <= 6**depth and sub_energy**5 <= len(subset)**13,
                "energy limits, with 13/5 rational control on an unequal split")
        residue_rows.append({"depth": depth, "endpoints": len(row), "energy": value,
                             "subset_size": len(subset), "subset_energy": sub_energy})

    trees = abstract_trees(3)
    attained = [max(sum(v < length for v in tree) for tree in trees) for length in range(28)]
    require(attained == [interval_cap(l) for l in range(28)], "sharp abstract interval bounds")
    energy_samples = [split_energy(tree, 27) for tree in trees]
    require(max(energy_samples) == 6**3 and min(energy_samples) < max(energy_samples),
            "sharp exponent with an adaptive example")

    tested = 0
    for size in range(16):
        population = Counter(word.count(1) for word in product((1, 2), repeat=size)
                             if all(word[i:i+3] != (2, 2, 2) for i in range(size-2)))
        for ones, count in population.items():
            require(count*2**(size-ones) <= 7**(ones+1), "no-222 weighted coding")
            tested += 1
    require(3**12 > 2**19 and 7**6 < 2**17 and 3**5 > 6**3, "strict entropy gap")
    canonical = [r for r in range(1, 384, 2) if r%3 == 2 and r%128 == 1]
    require(canonical == [257], "canonical 1222 source")
    return {"literal_depths": residue_rows, "abstract_depth_three_trees": len(trees),
            "abstract_mod27_energy_range": [min(energy_samples), max(energy_samples)],
            "sharp_cap_on_lengths_0_to_27": attained, "no222_composition_classes": tested,
            "canonical_residues_mod384": canonical}


if __name__ == "__main__":
    print(json.dumps(check(), indent=2))
