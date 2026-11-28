"""Replay the finite phase entropy and mismatch bounds on genuine rational cycles."""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb, prod
import json


def require(test, message):
    if not test:
        raise AssertionError(message)


def primitive_rotation(word):
    return all(word < word[j:] + word[:j] for j in range(1, len(word)))


def realization(word):
    power = 1
    carry = 0
    for i, bit in enumerate(word):
        if bit:
            carry = 3 * carry + (1 << i)
            power *= 3
    determinant = (1 << len(word)) - power
    if determinant <= 0 or carry == 0:
        return None
    start = Fraction(carry, determinant)
    den = start.denominator
    x = start.numerator
    phases = []
    for bit in word:
        require(x % 2 == bit, "native numerator parity")
        phases.append(x)
        x = (3 * x + den) // 2 if bit else x // 2
    require(x == start.numerator and len(set(phases)) == len(word), "least period")
    return phases


def blocks(word, m):
    return [tuple(word[(i + j) % len(word)] for j in range(m))
            for i in range(len(word))]


def replay():
    cycles = entropy_rows = error_rows = collision_controls = 0
    for n in range(1, 12):
        for word in product((0, 1), repeat=n):
            if not primitive_rotation(word):
                continue
            phases = realization(word)
            if phases is None:
                continue
            cycles += 1
            references = [word, (0,) * n, tuple(i % 2 for i in range(n)),
                          tuple(word[i] ^ (i % 3 == 0) for i in range(n))]
            for m in range(1, min(n + 2, 8)):
                outgoing = blocks(word, m)
                counts = Counter(outgoing)
                residue_words = {}
                for x, w in zip(phases, outgoing):
                    residue = x % (1 << m)
                    require(residue_words.setdefault(residue, w) == w, "residue to word")
                require(len(residue_words) == len(counts), "word to residue")
                selections = [
                    list(range(n)),
                    [i for i in range(n) if phases[i] < min(phases) + (1 << m)],
                    [i for i in range(n) if phases[i] % 3 == phases[0] % 3
                     and phases[0] <= phases[i] < phases[0] + 3 * (1 << m)],
                    list(range(0, n, 2)),
                ]
                models = [(len(set(blocks(v, m))), sum(a != b for a, b in zip(word, v)))
                          for v in references]
                for sel_index, selection in enumerate(selections):
                    low = Counter(outgoing[i] for i in selection)
                    length, fiber = len(selection), max(low.values())
                    if sel_index in (1, 2):
                        require(fiber == 1, "odd-step progression injection")
                    if any(counts[w] > mult for w, mult in low.items()):
                        collision_controls += 1
                    require(n**n * fiber**length >=
                            length**length * prod(f**f for f in counts.values()),
                            "finite conditional entropy")
                    entropy_rows += 1
                    for model_count, edits in models:
                        volume = 0
                        for r in range(m):
                            volume += comb(m, r)
                            require((r + 1) * length <=
                                    (r + 1) * fiber * model_count * volume + m * edits,
                                    "Hamming ball and incidence")
                            error_rows += 1
    require(collision_controls > 0, "outsider collision exercised")
    # H_2(3/100) < 25/128 < 1/5.116201, both comparisons exact.
    require(100**12800 < 2**2500 * (3**3 * 97**97)**128, "entropy margin")
    require(2**128 * 101**(101*128) < 2**1250 * 100**(100*128), "edit margin")
    require(25 * 5116201 < 128 * 1000000, "logarithmic form margin")
    return {"cycles": cycles, "entropy_rows": entropy_rows, "hamming_rows": error_rows,
            "selections_with_outside_collisions": collision_controls}


if __name__ == "__main__":
    print(json.dumps(replay(), sort_keys=True))
