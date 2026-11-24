"""Replay both directed whole-progression certificates using the standard library."""

from fractions import Fraction
import json
from pathlib import Path


def require(condition, message):
    if not condition:
        raise ValueError(message)


def certificate(path, residue):
    lines = [line.strip() for line in path.read_text(encoding="ascii").splitlines()
             if line.strip() and not line.startswith("#")]
    label, count = lines.pop(0).split()
    require(label == "words", "missing dictionary")
    count = int(count)
    words = lines[:count]
    require(len(words) == len(set(words)) == count and all(words), "invalid dictionary")
    require(all(set(word) <= set("hDtiA") for word in words), "unknown path step")
    label, size = lines[count].split()
    nodes = [int(item) for line in lines[count + 1:] for item in line.split()]
    require(label == "tree" and len(nodes) == int(size), "invalid tree length")
    # For (i,j,k,l), i*x+j maps to k*x+l, for every integer x>=0.
    rules = {"h": (2, 0, 1, 0), "D": (1, 0, 2, 0), "t": (2, 1, 3, 2),
             "i": (3, 2, 2, 1), "A": (6, residue, 18, 3 * residue)}
    pending = [(2, 1)]
    leaves = steps = tests = max_modulus = 0
    tested_words = set()
    low = high = Fraction(1)
    shortest_substitution = None
    for action in nodes:
        require(pending, "orphan tree node")
        modulus, base = pending.pop()
        if action in (-2, -3):
            radix = -action
            for digit in reversed(range(radix)):
                pending.append((radix * modulus, base + digit * modulus))
            continue
        require(0 <= action < count, "index out of dictionary")
        word = words[action]
        tested_words.add(action)
        a, b = modulus, base
        for char in word:
            i, j, k, l = rules[char]
            quotient_slope, slope_remainder = divmod(a, i)
            quotient_base, base_remainder = divmod(b, i)
            require(slope_remainder == 0 and base_remainder == j,
                    f"illegal move {char} on {a}t+{b}, leaf {modulus}t+{base}")
            if char == "A":
                tests += 1
                low = min(low, Fraction(a, modulus), Fraction(b, base))
                high = max(high, Fraction(a, modulus), Fraction(b, base))
            a = k * quotient_slope
            b = k * quotient_base + l
            require(a > 0 and b > 0, "nonpositive image")
        require((a, b) == (3 * modulus, 3 * base), "wrong affine endpoint")
        steps += len(word)
        leaves += 1
        max_modulus = max(max_modulus, modulus)
        if base % 3 == 0 and word.count("A") >= 1:
            example = (len(word), modulus, base, word)
            if shortest_substitution is None or example < shortest_substitution:
                shortest_substitution = example
    require(not pending, "missing children")
    require(len(tested_words) == count, "unused dictionary entry")
    return {"residue_modulo_6": residue, "dictionary_words": count,
            "tree_nodes": len(nodes), "full_progression_leaves": leaves,
            "maximum_modulus": max_modulus, "longest_word": max(map(len, words)),
            "total_path_letters": steps, "forward_query_positions": tests,
            "minimum_query_to_input": str(low), "maximum_query_to_input": str(high),
            "shortest_example_from_multiple_of_three": shortest_substitution}


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    result = [certificate(here / f"cover{r}.txt", r) for r in (1, 5)]
    print(json.dumps(result, indent=2))
