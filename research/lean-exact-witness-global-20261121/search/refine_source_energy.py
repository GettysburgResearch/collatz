#!/usr/bin/env python3
"""Bounded adaptive work checkpoint for the exact one-query energy grammar.

Both children of every unresolved binary cell are retained.  Resolved rows
apply only on their explicitly checked tail; finite entrance exceptions remain
listed, not silently discharged.  A nonempty queue is not a theorem obstruction.
"""
import argparse
from collections import Counter, deque
import hashlib
import json
from pathlib import Path
import time

import source_energy_frontier as energy


def coarse_dependencies(record, base):
    if record['classification'] == 'ordinary_merger':
        return []
    query = record['query']
    residues = energy.frontier.dependency.oddpart_residues(*query['form'], base)
    return [(query['kind'], r) for r in residues]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--budget', type=int, default=2000)
    parser.add_argument('--seconds', type=float, default=30)
    parser.add_argument('--out', required=True)
    args = parser.parse_args()
    if args.budget < 1 or args.seconds <= 0:
        raise ValueError('positive work limits required')
    base = 1440
    active = {('R3', r) for r in range(9, base, 18)}
    queue = deque((kind, base, r) for kind, r in sorted(active))
    leaves = []
    stats = []
    processed = splits = 0
    started = time.monotonic()
    while queue and processed < args.budget and time.monotonic() - started < args.seconds:
        kind, modulus, residue = queue.popleft()
        records, cell_stats = energy.search(kind, modulus, residue)
        processed += 1
        stats.append(cell_stats | {'M': modulus})
        if records:
            choices = []
            for record in records:
                deps = coarse_dependencies(record, base)
                score = (sum(dep not in active for dep in deps), len(deps),
                         len(record.get('rank_inserted', ())),
                         len(record['row']['left']) + len(record['row']['right']))
                choices.append((score, record, deps))
            choices.sort(key=lambda choice: choice[0])
            _, record, deps = choices[0]
            record['dependencies_coarse'] = [list(dep) for dep in deps]
            record['finite_entrance_parameters'] = list(range(record['tail_parameter']))
            leaves.append(record)
            for dep in deps:
                if dep not in active:
                    active.add(dep)
                    queue.append((dep[0], base, dep[1]))
        else:
            splits += 1
            queue.append((kind, 2 * modulus, residue))
            queue.append((kind, 2 * modulus, residue + modulus))
    elapsed = time.monotonic() - started
    max_inserted = max((len(row.get('rank_inserted', ())) for row in leaves), default=0)
    summary = {
        'processed': processed,
        'resolved_leaves': len(leaves),
        'unresolved_cells': len(queue),
        'activated_coarse_states': len(active),
        'binary_splits': splits,
        'resolved_by_bits': dict(Counter(energy.frontier.v2(row['row']['M']) for row in leaves)),
        'unresolved_by_bits': dict(Counter(energy.frontier.v2(modulus) for _, modulus, _ in queue)),
        'finite_entrance_exceptions': sum(len(row['finite_entrance_parameters']) for row in leaves),
        'max_inserted_length': max_inserted,
        'uniform_energy_base': max(2, max_inserted + 1),
        'inverse_nodes_examined': sum(row['inverse_nodes'] for row in stats),
        'maximum_inverse_depth_bound': max((row['inverse_depth_bound'] for row in stats), default=0),
        'seconds': elapsed,
    }
    files = [Path(__file__), Path(energy.__file__),
             Path(energy.frontier.__file__),
             Path(energy.frontier.dependency.__file__)]
    data = {
        'status': 'UNRESOLVED: exact adaptive energy frontier; no global theorem asserted',
        'base_modulus': base,
        'limits': {'processed_cells': args.budget, 'wall_seconds_between_cells': args.seconds},
        'input_code_sha256': {str(path): hashlib.sha256(path.read_bytes()).hexdigest() for path in files},
        'summary': summary,
        'active_coarse_states': [list(state) for state in sorted(active)],
        'resolved_leaves': leaves,
        'unresolved_frontier': [list(cell) for cell in queue],
        'processed_cell_statistics': stats,
    }
    Path(args.out).write_text(json.dumps(data, separators=(',', ':')) + '\n')
    print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    main()
