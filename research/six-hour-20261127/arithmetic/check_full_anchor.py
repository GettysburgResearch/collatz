"""Full physical ceiling, exact integer fourth moments at mechanical returns."""
from collections import Counter
from functools import cache
from hashlib import sha256
from itertools import product
import json

from check_anchor_carries import require, schedules


def earlier_grades(later, increment):
    return range(max(0, 1-increment+later), min(3-increment, 2-increment+later)+1)


@cache
def routes(terminal, increment):
    values = []
    for earlier in product(*(earlier_grades(k, increment) for k in terminal)):
        digits = [4 >> k for k in earlier]
        difference = digits[0]+digits[1]-digits[2]-digits[3]
        values.append((tuple(sorted(earlier[:2])), tuple(sorted(earlier[2:])), difference))
    return values


@cache
def transitions(terminal, carry, increment):
    result = Counter()
    for positive, negative, difference in routes(terminal, increment):
        next_carry, remainder = divmod((1 << increment)*carry+difference, 3)
        if remainder:
            continue
        if positive > negative or (positive == negative and next_carry < 0):
            target = negative+positive, -next_carry
        else:
            target = positive+negative, next_carry
        result[target] += 1
    return list(result.items())


def modular_energy(word, grade):
    counts = {((grade,)*4, 0): 1}
    for increment in map(int, word):
        previous = {}
        for (terminal, carry), count in counts.items():
            for target, multiplicity in transitions(terminal, carry, increment):
                previous[target] = previous.get(target, 0)+multiplicity*count
        counts = previous
    return sum(counts.values())


def literal(word, grade):
    modulus = 3**len(word)
    paths = [(grade, 0)]
    power_two = 1
    for step, increment in enumerate(map(int, word)):
        power_two *= 1 << increment
        factor = 3**step*pow(power_two, -1, modulus)
        paths = [(x, (residue+factor*(4 >> x)) % modulus)
                 for later, residue in paths for x in range(3)
                 if x+increment <= 3 and 1 <= increment+x-later <= 2]
    pairs = Counter((a+b) % modulus for _, a in paths for _, b in paths)
    return sum(count*count for count in pairs.values())


def check():
    fixtures = []
    for word in ("1", "2", "112", "2121", "21121", "22121121"):
        exact = [literal(word, k) for k in range(3)]
        require(exact == [modular_energy(word, k) for k in range(3)], "literal quartet residue")
        fixtures.append({"reverse": word, "energies": exact})
    records = []
    for word in schedules():
        energies = [modular_energy(word, k) for k in range(3)]
        require(max(energies)**100 < 3**(111*len(word)), "full physical energy")
        records.append({"length": len(word), "reverse_sha256": sha256(word.encode()).hexdigest(),
                        "energies": energies})
    return {"per_edge_exponent": "111/100", "source_exponent": "37/100",
            "fixtures": fixtures, "returns": records}


if __name__ == "__main__":
    print(json.dumps(check(), indent=2))
