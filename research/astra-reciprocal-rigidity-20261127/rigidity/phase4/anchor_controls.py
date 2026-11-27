#!/usr/bin/env python3
"""Exact checks of physical branch words, anchors, and all chronological cut identities."""

import argparse
import json
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path


def require(condition, message):
    if not condition:
        raise ValueError(message)


def affine(word):
    intercept = 0
    odds = 0
    scale = 1
    for bit in word:
        if bit:
            intercept = 3 * intercept + scale
            odds += 1
        scale *= 2
    return scale, 3 ** odds, intercept


def anchor(word):
    denominator, multiplier, intercept = affine(word)
    return Fraction(intercept, denominator - multiplier)


def least_realizer(word):
    denominator, multiplier, intercept = affine(word)
    residue = (-intercept * pow(multiplier, -1, denominator)) % denominator
    return residue or denominator


def states(source, word):
    path = [source]
    for bit in word:
        value = path[-1]
        require(value % 2 == bit, "least realizer has the wrong physical parity")
        path.append((3 * value + 1) // 2 if bit else value // 2)
    return path


def audit_partitions(word, source, path):
    length = len(word)
    cumulative = [Fraction(1)]
    for bit in word:
        cumulative.append(cumulative[-1] * (Fraction(2, 3) if bit else 2))
    partitions = 0
    cuts = 0
    hits = 0
    for count in range(min(3, length)):
        for separators in combinations(range(1, length), count):
            boundaries = (0, *separators, length)
            ledger = Fraction(source)
            for left, right in zip(boundaries, boundaries[1:]):
                fixed = anchor(word[left:right])
                projected = ledger - fixed * cumulative[left]
                require(projected == cumulative[left] * (path[left] - fixed), "initial cut equality")
                contact = projected == 0
                require(contact == (path[right] == path[left]), "exact contact versus physical return")
                hits += contact
                cuts += 1
                increment = fixed * (cumulative[right] - cumulative[left])
                require(increment >= 0, "negative completed physical increment")
                ledger += increment
                require(ledger == cumulative[right] * path[right], "weighted piece transport")
            partitions += 1
    return partitions, cuts, hits


def one_run_summary(length):
    # Zero prefix, one nonempty odd run, zero suffix, together with all-even.
    # The formula includes all positions and run lengths without constructing 2^length words.
    modulus = 1 << length
    candidates = [(modulus, length, 0)]
    for odds in range(1, length + 1):
        multiplier = 3 ** odds
        native_intercept = multiplier - (1 << odds)
        inverse = pow(multiplier, -1, modulus)
        for start in range(length - odds + 1):
            least = (-((1 << start) * native_intercept) * inverse) % modulus
            candidates.append((least or modulus, start, odds))
    least, start, odds = min(candidates)
    selected = (0,) * start + (1,) * odds + (0,) * (length - start - odds)
    require(least_realizer(selected) == least, "one-run extremizer congruence")
    states(least, selected)
    return {"length": length, "least": least, "odd_start": start, "odd_length": odds,
            "words": len(candidates)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    ledger = {"words": 0, "partitions": 0, "piece_cuts": 0, "exact_contacts": 0}
    for length in range(1, 9):
        for word in product((0, 1), repeat=length):
            source = least_realizer(word)
            path = states(source, word)
            modulus, multiplier, intercept = affine(word)
            require(modulus * path[-1] == multiplier * source + intercept, "ordinary endpoint formula")
            counts = audit_partitions(word, source, path)
            ledger["words"] += 1
            for name, value in zip(("partitions", "piece_cuts", "exact_contacts"), counts):
                ledger[name] += value
    output = {"all_words_up_to_length_eight": ledger,
              "one_run_minima": [one_run_summary(length) for length in (8, 16, 32, 64, 128, 256)]}
    report = json.dumps(output, indent=2, sort_keys=True) + "\n"
    if args.check:
        expected = Path(__file__).with_name("ANCHOR_CONTROLS.json").read_text()
        require(report == expected, "recorded anchor report mismatch")
    print(report, end="")


if __name__ == "__main__":
    main()
