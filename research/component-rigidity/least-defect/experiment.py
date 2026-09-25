#!/usr/bin/env python3
"""Generate all-height defect certificates and least-defect refinement traces.

The optimizer is the preserved dyadic-repair producer. Its original source is
hash checked; infinite numerical values remain rational enclosures, not exact
irrational optima. The new oracle never scans an ambient integer interval.
"""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
from fractions import Fraction as Q
import oracle as O

PARENT = Path(__file__).resolve().parents[1]/'dyadic-repair'/'run.py'
PARENT_SHA = '8b28607b5d58f6e9fc33be701c39f86210bde7ef88cdc740b16ceec7f0d6732a'
O.need(hashlib.sha256(PARENT.read_bytes()).hexdigest() == PARENT_SHA, 'changed parent solver')
spec = importlib.util.spec_from_file_location('preserved_dyadic_solver', PARENT)
DR = importlib.util.module_from_spec(spec)
spec.loader.exec_module(DR)


def refine(N: int, p: int = 3, cap: int = 128, cutoff_bits: int | None = None,
           ladder_depth: int = 0, precision_cap: int = 4096, batch_limit: int = 16) -> dict:
    O.integer(N, 1); O.integer(cap); O.integer(precision_cap, 64); O.integer(batch_limit, 1)
    O.need(type(p) is int and p in (3, 5), 'multiplier')
    if cutoff_bits is not None:
        O.integer(cutoff_bits, 1)
        O.need(N <= 1 << cutoff_bits, 'source outside cutoff')
    have = DR.initial_sources(N, p, ladder_depth)
    H = None if cutoff_bits is None else 1 << cutoff_bits
    if H is not None:
        O.need(all(max(n, (p*n+1)//2) <= H for n in have), 'initial path exits cutoff')
    common = {'schema': 'least-defect-refinement-v1', 'p': p, 'N': N,
              'cap': cap, 'cutoff_bits': cutoff_bits, 'initial_sources': have[:],
              'precision_cap': precision_cap, 'selection': 'LEAST_PREFIX_BATCH', 'batch_limit': batch_limit}
    records = []
    for j in range(cap+1):
        terms = 64
        while True:
            c = DR.solve({'p': p, 'N': N, 'odd_sources': have[:]},
                         horizon=None if H is None else cutoff_bits-1, tail_terms=terms)
            if c['status'] == 'PINS_INFEASIBLE' or Q(*c['upper'])-Q(*c['lower']) <= 1:
                break
            if terms >= precision_cap:
                return dict(common, records=records, final_cut=c,
                            status='UNRESOLVED_AT_PRECISION_CAP')
            terms = min(2*terms, precision_cap)
        if c['status'] == 'PINS_INFEASIBLE':
            return dict(common, records=records, final_cut=c, status='CONVERGENCE',
                        path=DR.original_path(N, p, have))
        m = O.model(O.from_cut(c), p)
        answer = O.least(m) if H is None else O.cutoff(m, H)
        n = answer['n'] if H is None else answer['least']
        if n is None:
            O.need(H is not None and answer['defects'] == 0, 'unexpected global separator')
            return dict(common, records=records, final_cut=c, model=m, oracle=answer,
                        status='FULL_FINITE_SEPARATOR')
        if j == cap:
            return dict(common, records=records, final_cut=c, model=m, oracle=answer,
                        status='UNRESOLVED_AT_ROUND_CAP')
        O.need(n not in have and n % 2 == 1, 'repeated or even repair')
        stop = 2*n if H is None else min(2*n, answer['last_eligible'])
        selected = O.first_defects(m['steps'], p, n, stop, batch_limit)
        O.need(selected and selected[0] == n and not set(selected) & set(have), 'repair batch')
        records.append({'cut': c, 'model': m, 'oracle': answer, 'selected': selected, 'batch_stop': stop})
        have = sorted(have+selected)
    raise RuntimeError('unreachable')


def compact(r: dict) -> dict:
    return {'p': r['p'], 'N': r['N'], 'cutoff_bits': r['cutoff_bits'],
            'status': r['status'], 'rounds': len(r['records']), 'inserted_edges': sum(len(z['selected']) for z in r['records']), 'batch_limit': r['batch_limit'],
            'largest_selected': max((n for z in r['records'] for n in z['selected']), default=None),
            'path_steps': len(r['path'])-1 if 'path' in r else None,
            'largest_completion_depth': max((z['model']['D'] for z in r['records']), default=0)}


def grid_steps(D: int, mask: int) -> list:
    size = 1 << D
    rows = []
    for i in range(size):
        c = 0 if i == 0 else (mask >> (i-1)) & 1
        if rows and rows[-1][2] == c:
            rows[-1][1] = O.encode(Q(size+i+1, size))
        else:
            rows.append([O.encode(Q(size+i, size)), O.encode(Q(size+i+1, size)), c])
    return rows


def suite() -> tuple[dict, dict]:
    models = []
    brute_sources = 0
    recurrence_checks = 0
    for p in (3, 5):
        for D in (1, 2, 3):
            for mask in range(1 << ((1 << D)-1)):
                steps = grid_steps(D, mask)
                m = O.model(steps, p)
                # Literal odd-source replay; use the unreduced depth-D grid.
                def col(n):
                    ix = ((n << D) >> (n.bit_length()-1))-(1 << D)
                    return 0 if ix == 0 else (mask >> (ix-1)) & 1
                small = []
                for h in range(10):
                    row = O.shell(steps, p, h)
                    bad = [n for n in range((1 << h) | 1, 1 << (h+1), 2)
                           if col(n) != col((p*n+1)//2)]
                    brute_sources += 1 if h == 0 else 1 << (h-1)
                    O.need(row['defects'] == len(bad) and row['least'] == (bad[0] if bad else None),
                           'literal shell comparison')
                    O.need(O.predicted_count(m, h) == len(bad), 'tail versus literal count')
                    small.append(row['defects'])
                comparisons = []
                for h in (m['start'], m['start']+m['period'], m['start']+7*m['period'], 64):
                    row = O.shell(steps, p, h)
                    O.need(row['defects'] == O.predicted_count(m, h), 'exact shell recurrence')
                    comparisons.append(row); recurrence_checks += 1
                heights = (1, 2, 7, 8, 23, 24, 127, 128, 513, 1 << 129)
                cuts = [O.cutoff(m, H) for H in heights]
                for c in cuts[:-1]:
                    H = c['H']
                    bad = [n for n in range(1, H+1, 2)
                           if (p*n+1)//2 <= H and col(n) != col((p*n+1)//2)]
                    O.need(c['defects'] == len(bad) and c['least'] == (bad[0] if bad else None),
                           'literal complete-cutoff comparison')
                models.append({'grid': [p, D, mask], 'model': m, 'small_counts': small,
                               'tail_comparisons': comparisons, 'cutoffs': cuts, 'least': O.least(m)})
    huge = []
    for p in (3, 5):
        for D, mask in ((1, 1), (3, 37)):
            m = O.model(grid_steps(D, mask), p)
            huge.append({'model': m, 'cutoff': O.cutoff(m, 1 << 4096)})
    configurations = [(1, 3, 0, None), (8, 3, 0, None), (3, 3, 32, None),
                      (7, 3, 64, None), (27, 3, 160, None), (97, 3, 96, None),
                      (871, 3, 16, None), (13, 5, 32, None),
                      (27, 3, 160, 13), (27, 3, 96, 8), (13, 5, 96, 10)]
    traces = [refine(n, p, cap, bits) for n, p, cap, bits in configurations]
    cycles = [[5, [1, 3, 8, 4, 2, 1]],
              [5, [13, 33, 83, 208, 104, 52, 26, 13]]]
    corpus = {'schema': 'least-defect-corpus-v1', 'models': models, 'huge': huge,
              'refinements': traces, 'cycles': cycles}
    summary = {'model_cases': len(models), 'literal_shell_source_checks': brute_sources,
               'recurrence_checks': recurrence_checks, 'huge_cutoffs': len(huge),
               'refinements': [compact(r) for r in traces],
               'huge_count_bits': [r['cutoff']['defects'].bit_length() for r in huge]}
    return corpus, summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--summary', type=Path)
    parser.add_argument('--source', type=int)
    parser.add_argument('--multiplier', type=int, choices=(3, 5), default=3)
    parser.add_argument('--rounds', type=int, default=128)
    parser.add_argument('--cutoff-bits', type=int)
    parser.add_argument('--batch-limit', type=int, default=16)
    args = parser.parse_args()
    if args.source is None:
        payload, summary = suite()
    else:
        payload = refine(args.source, args.multiplier, args.rounds, args.cutoff_bits, batch_limit=args.batch_limit)
        summary = compact(payload)
    text = json.dumps(payload, sort_keys=True, separators=(',', ':'))+'\n'
    args.output.write_text(text)
    summary['corpus_sha256'] = hashlib.sha256(text.encode()).hexdigest()
    if args.summary:
        args.summary.write_text(json.dumps(summary, sort_keys=True, indent=2)+'\n')
    print(json.dumps(summary, sort_keys=True))


if __name__ == '__main__':
    main()
