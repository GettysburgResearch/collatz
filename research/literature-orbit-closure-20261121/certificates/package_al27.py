"""Package exact ordinary mergers discovered on the AL 27 (mod 128) branch.

This is a bounded search and an infinite-family certificate, not a complete
cover. Applegate--Lagarias supply the branch as a design seed; no wild
semigroup multiplier is accepted as a physical Collatz step.
"""
from pathlib import Path
import json
from guided_cover import scan, step


def path(n, h):
    bits = []
    for _ in range(h):
        bits.append(str(n % 2))
        n = step(n)
    return ''.join(bits), n


def generate():
    data = scan(7, 27, 13, 2)
    rows = []
    for row in data['rows']:
        source_word, source_end = path(row['n'], row['h'])
        partner_word, partner_end = path(row['partner'], row['a'])
        if source_end != partner_end or row['min_t'] != 0:
            raise ValueError('This packet requires exact merger and no finite exceptions')
        rows.append(dict(source=row['n'], partner=row['partner'],
                         partner_increment=row['slope'],
                         source_word=source_word, partner_word=partner_word))
    rows.sort(key=lambda row: row['source'])
    return dict(
        schema='ordinary-merger-progressions-v1',
        map='T(n)=n/2 for even n, (3n+1)/2 for odd n',
        status='EXACT_FINITE_CERTIFICATE_WITH_UNRESOLVED_COMPLEMENT',
        target_residue=27, target_modulus=128, source_modulus=73728,
        source_clock=13, ternary_refinement=2,
        search_partner_clock_limit=21, search_node_cap=100000,
        source_classes=576, certified_classes=len(rows),
        unresolved=sorted(data['miss']), rows=rows,
        theorem='For each row and every t>=0: n=source+73728*t and x=partner+partner_increment*t obey 0<x<n and T^len(partner_word)(x)=T^13(n).',
        scope='No convergence assertion for unresolved classes; no universal selector. Coverage is relative to the one AL branch n=27 mod128.')


if __name__ == '__main__':
    out = Path(__file__).with_name('al27_certificate.json')
    out.write_text(json.dumps(generate(), indent=2) + '\n', encoding='utf-8')
    print(out)
