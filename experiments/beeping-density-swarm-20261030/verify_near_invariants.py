#!/usr/bin/env python3
"""Exact bounded checks of the parity-majority obstruction; no Collatz claim."""
from __future__ import annotations
import argparse
from fractions import Fraction
import hashlib
import json
from math import comb
from pathlib import Path


def need(ok, message):
    if not ok:
        raise RuntimeError(message)


def shortcut(n):
    return n // 2 if n % 2 == 0 else (3*n+1) // 2


def parity_word(n, length):
    out = 0
    for i in range(length):
        out |= (n & 1) << i
        n = shortcut(n)
    return out


def majority(n, k):
    return int(parity_word(n, k).bit_count() > k//2)


def pair(x):
    x = Fraction(x)
    return [x.numerator, x.denominator]


def run():
    rows = []
    all_sources = 0
    for k in (1, 3, 5, 7, 9, 11, 13, 15, 17):
        q = 1 << k
        words = [parity_word(n, k) for n in range(q)]
        need(len(set(words)) == q, 'parity bijection')
        values = [int(word.bit_count() > k//2) for word in words]
        need(sum(values) == q//2, 'balanced majority')
        target_multiplicities = [0]*q
        mismatch = 0
        for n in range(2*q):
            target = shortcut(n)
            target_multiplicities[target % q] += 1
            need(majority(n, k) == values[n % q], 'periodicity on next period')
            mismatch += abs(values[target % q]-values[n % q])
        need(set(target_multiplicities) == {2}, 'dyadic Haar invariance')
        expected = 2*comb(k-1, (k-1)//2)
        need(mismatch == expected, 'exact majority defect')
        rows.append({'k': k, 'period': q, 'literal_source_residues': 2*q,
                     'mismatches': mismatch, 'defect': pair(Fraction(mismatch,2*q))})
        all_sources += 2*q

    # Fixed anchors including a whole actual finite orbit and separate values.
    # The arbitrary separate values do not assert global Collatz consistency.
    zero_chain = {1, 2, 4, 5, 8, 10, 16, 20}
    anchors = {n: 0 for n in zero_chain}
    anchors.update({27: 1, 41: 1, 62: 1})
    checked_edges = [(n, shortcut(n)) for n in anchors if shortcut(n) in anchors
                     and anchors[n] == anchors[shortcut(n)]]
    patches = []
    for k in (7, 9, 11, 13, 15):
        q = 1 << k
        original = [majority(n,k) for n in range(q)]
        modified = original.copy()
        need(len({n % q for n in anchors}) == len(anchors), 'distinct anchors')
        for n, value in anchors.items():
            modified[n % q] = value
        changed = sum(x != y for x,y in zip(original,modified))
        mismatch = sum(abs(modified[shortcut(n) % q]-modified[n % q]) for n in range(2*q))
        old_defect = Fraction(comb(k-1,(k-1)//2), 1 << k)
        new_defect = Fraction(mismatch,2*q)
        mean = Fraction(sum(modified), q)
        need(new_defect <= old_defect+Fraction(2*len(anchors),q), 'patch defect bound')
        need(abs(mean-Fraction(1,2)) <= Fraction(len(anchors),q), 'patch mean bound')
        need(min(mean,1-mean) >= Fraction(1,2)-Fraction(len(anchors),q), 'constant distance')
        for n,target in checked_edges:
            need(modified[n%q] == modified[target%q], 'finite prescribed edge')
        patches.append({'k':k, 'anchor_count':len(anchors), 'changed_classes':changed,
                        'checked_edges':len(checked_edges), 'mean':pair(mean),
                        'defect':pair(new_defect), 'distance_to_constants':pair(min(mean,1-mean))})

    # Closed formulas at larger k are algebraic evaluations, not literal replay.
    formula_rows = [{'k':k,'defect':pair(Fraction(comb(k-1,(k-1)//2),1 << k))}
                    for k in (33,65,129,257,513,1025)]
    payload = {'schema':'collatz-parity-majority/v1',
               'status':'finite checks of separate proved formulas, not Collatz verification',
               'literal_source_residues':all_sources, 'majorities':rows,
               'patched_anchors':patches, 'formula_only':formula_rows,
               'slow_height_example':'proved analytically in companion note; no numerical evidence claimed'}
    canonical = json.dumps(payload,sort_keys=True,separators=(',',':')).encode()
    return {'payload':payload,'sha256':hashlib.sha256(canonical).hexdigest()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    args = parser.parse_args()
    report=run()
    encoded=json.dumps(report,indent=2,sort_keys=True)+'\n'
    if args.output:
        args.output.write_text(encoded,encoding='utf-8')
    print(json.dumps({'status':'PASS','sha256':report['sha256'],
                      'literal_source_residues':report['payload']['literal_source_residues'],
                      'majority_lengths':len(report['payload']['majorities']),
                      'anchor_lengths':len(report['payload']['patched_anchors'])},sort_keys=True))


if __name__ == '__main__':
    main()
