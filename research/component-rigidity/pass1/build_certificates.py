#!/usr/bin/env python3
"""Build small exact, independently checkable all-height net certificates."""
from fractions import Fraction
import json
from pathlib import Path
from experiment import inverse_ladder, circular_ratio, hit_relative_window, verify_ladder

HERE = Path(__file__).resolve().parent

def pair(f):
    return [f.numerator, f.denominator]

rows = []
for n in (1, 27, 121, 303, 1311, 2**127 - 1):
    row = inverse_ladder(n, 512)
    verify_ladder(row)
    row['max_circular_ratio'] = pair(circular_ratio(row['nodes']))
    row['window_ratio'] = [101, 100]
    row['threshold'] = max(row['nodes'])
    row['windows'] = [hit_relative_window(row['nodes'], row['threshold'] * (17+j)//16+j*j, Fraction(101,100)) for j in range(16)]
    rows.append(row)

universal = []
for ratio, Q, M in [(Fraction(11,10), 11, 14), (Fraction(101,100), 146, 32)]:
    G = circular_ratio([3**j for j in range(Q+1)])
    c = Fraction(5,8) * Fraction(4,5)**M
    if not G / (1-c) < ratio:
        raise ValueError('universal net inequality failed')
    universal.append({'ratio':pair(ratio), 'Q':Q, 'M':M,
                      'ideal_gap':pair(G), 'product_loss_bound':pair(c),
                      'perturbed_gap_bound':pair(G/(1-c)),
                      'threshold_multiplier':5 * 16**(M+Q),
                      'threshold_formula':f'5 * 2^{4*(M+Q)} * ORIGINAL_N'})

payload = {'status':'EXACT FINITE CERTIFICATES; universal interpretation proved in PROOF.md',
           'universal_net_bounds':universal, 'source_nets':rows}
(HERE/'net_certificates.json').write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n')
print('Wrote',len(rows),'source nets and',len(universal),'universal bounds')
