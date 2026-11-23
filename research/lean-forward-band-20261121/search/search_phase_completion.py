#!/usr/bin/env python3
"""Target the entire saved parity-rank frontier with the unbounded phase rule.

All accepted query edges are either strictly smaller in the unchanged rank
R(n)=2n (even), n (odd), or justified by solved_phase_odd_psi on the entire
affine cell. Search results remain search certificates pending Lean export.
"""
from collections import deque, Counter
from functools import lru_cache
import argparse, hashlib, json, time


def phase_terminal(a, b):
    if b <= 0 or b % 4 != 3:
        return None
    h = ((b + 1) & -(b + 1)).bit_length() - 1
    if h < 2 or a % (1 << (h + 2)):
        return None
    if pow(3, h - 1, 4) * ((b + 1) >> h) % 4 == 3:
        return h
    return None


def search(M, r, cap=100000, height=100, phase=True, even_macro=True):
    root_weight = 2 if r % 2 == 0 else 1
    starts = ((M, r), (2 * M, 2 * r - 1))
    bounds = (height * M, height * r)
    reached = [{starts[0]: (None, None)}, {starts[1]: (None, None)}]
    queues = [deque([starts[0]]), deque([starts[1]])]
    phase_edges = 0

    def smaller(a, b):
        weight = (2 if b % 2 == 0 else 1) if a % 2 == 0 else 2
        return b > 0 and weight * a <= root_weight * M and weight * b < root_weight * r

    @lru_cache(None)
    def known(a, b):
        if b <= 0:
            return None
        if smaller(a, b):
            return 'rank'
        h = phase_terminal(a, b) if phase else None
        if h is not None:
            return 'phase:' + str(h)
        if even_macro and a % 2 == 0 and b % 2 == 0:
            half = known(a // 2, b // 2)
            # This source is odd. It cannot recurse through the even macro.
            odd = known(2 * a, 2 * b - 1)
            if half is not None and odd is not None:
                return ['even', half, odd]
        return None

    direct = phase_terminal(M, r) if phase else None
    if direct is not None:
        return {'cell': [M, r], 'terminal_phase': direct, 'nodes': 0}

    def neighbors(a, b):
        yield 'D', (2 * a, 2 * b)
        if a % 2 == 0:
            if b % 2 == 0:
                yield 'E', (a // 2, b // 2)
            else:
                yield 'O', (3 * a // 2, (3 * b + 1) // 2)
        if a % 3 == 0 and (2 * b - 1) % 3 == 0 and 2 * b - 1 > 0:
            yield 'I', (2 * a // 3, (2 * b - 1) // 3)
        forward = known(a, b)
        if forward is not None:
            yield ['+psi', forward], (2 * a, 2 * b - 1)
        if a % 2 == 0 and (b + 1) % 2 == 0:
            backward = known(a // 2, (b + 1) // 2)
            if backward is not None:
                yield ['-psi', backward], (a // 2, (b + 1) // 2)

    def path(side, z):
        result = []
        while reached[side][z][0] is not None:
            previous, move = reached[side][z]
            result.append(move)
            z = previous
        return result[::-1]

    while queues[0] and queues[1] and sum(map(len, reached)) < cap:
        side = 0 if len(queues[0]) <= len(queues[1]) else 1
        z = queues[side].popleft()
        for move, new in neighbors(*z):
            if min(new) <= 0 or new[0] > bounds[0] or new[1] > bounds[1]:
                continue
            if isinstance(move, list) and move[1] != 'rank':
                phase_edges += 1
            if new not in reached[side]:
                reached[side][new] = (z, move)
                queues[side].append(new)
                if new in reached[1 - side]:
                    return {'cell': [M, r], 'left': path(0, new), 'right': path(1, new),
                            'endpoint': list(new), 'nodes': sum(map(len, reached)),
                            'extra_edges_seen': phase_edges}
    return {'cell': [M, r], 'unresolved': True, 'nodes': sum(map(len, reached)),
            'queue_exhausted': not queues[0] or not queues[1],
            'extra_edges_seen': phase_edges}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True)
    parser.add_argument('--output', required=True)
    parser.add_argument('--levels', type=int, default=6)
    parser.add_argument('--height', type=int, default=100)
    parser.add_argument('--cap', type=int, default=100000)
    parser.add_argument('--compare-baseline', action='store_true',
                        help='Replay the matched search without either added rule.')
    parser.add_argument('--compact', action='store_true',
                        help='Save counts, hashes, and one final frontier instead of path traces.')
    args = parser.parse_args()
    start = time.monotonic()
    original = json.load(open(args.input))
    if 'rows' in original:
        frontier = [tuple(row['cell']) for row in original['rows'] if row.get('unresolved')]
        prior_summary = original['summary']
        source_hash = hashlib.sha256(open(args.input, 'rb').read()).hexdigest()
    elif 'initial_frontier' in original:
        frontier = [tuple(cell) for cell in original['initial_frontier']]
        prior_summary = original['prior_summary']
        source_hash = original['source_sha256']
    else:
        # The compact publication receipt carries exactly the saved frontier,
        # so replay does not require a staging path or the full older trace.
        frontier = [(original['initial_modulus'], r)
                    for r in original['initial_unresolved_residues']]
        prior_summary = original['prior_summary']
        source_hash = original['input_sha256']
    baseline_frontier = frontier[:]
    report = {
        'status': 'SEARCH ONLY; NOT A LEAN-CHECKED COVER',
        'source_sha256': source_hash,
        'rank': '2*n when even, n when odd',
        'terminal_rule': 'solved_phase_odd_psi; whole affine cells only',
        'initial_frontier': [list(c) for c in frontier],
        'prior_summary': prior_summary,
        'height': args.height, 'cap': args.cap, 'levels': [], 'new_certificates': []}

    def frontier_hash(cells):
        data = json.dumps(sorted(cells), separators=(',', ':')).encode()
        return hashlib.sha256(data).hexdigest()

    for level in range(args.levels + 1):
        cells = frontier if level == 0 else [(2 * M, r + j * M) for M, r in frontier for j in range(2)]
        rows = [search(M, r, cap=args.cap, height=args.height) for M, r in cells]
        frontier = [tuple(row['cell']) for row in rows if row.get('unresolved')]
        report['new_certificates'].extend(row for row in rows if not row.get('unresolved'))
        summary = {'level': level, 'tested': len(cells),
                   'solved': len(cells) - len(frontier), 'remaining': len(frontier),
                   'remaining_mod32': dict(sorted(Counter(r % 32 for M, r in frontier).items())),
                   'max_nodes': max((row['nodes'] for row in rows), default=0),
                   'seconds': time.monotonic() - start}
        if args.compare_baseline:
            baseline_cells = baseline_frontier if level == 0 else [
                (2 * M, r + j * M) for M, r in baseline_frontier for j in range(2)]
            baseline_rows = [search(M, r, cap=args.cap, height=args.height,
                                    phase=False, even_macro=False)
                             for M, r in baseline_cells]
            baseline_frontier = [tuple(row['cell']) for row in baseline_rows if row.get('unresolved')]
            summary['baseline_tested'] = len(baseline_cells)
            summary['baseline_remaining'] = len(baseline_frontier)
            summary['frontiers_exactly_equal'] = set(frontier) == set(baseline_frontier)
            summary['enriched_frontier_sha256'] = frontier_hash(frontier)
            summary['baseline_frontier_sha256'] = frontier_hash(baseline_frontier)
        report['levels'].append(summary)
        report['unresolved'] = [list(c) for c in frontier]
        report['last_unresolved_details'] = [row for row in rows if row.get('unresolved')]
        print(json.dumps(summary), flush=True)
        with open(args.output, 'w') as out:
            if args.compact:
                modulus = report['initial_frontier'][0][0] * 2**level
                compact = {key: value for key, value in report.items()
                           if key not in ('new_certificates', 'unresolved', 'last_unresolved_details')}
                compact['final_modulus'] = modulus
                compact['final_unresolved_residues'] = sorted(r for M, r in frontier)
                compact['final_enriched_frontier_sha256'] = frontier_hash(frontier)
                if args.compare_baseline:
                    compact['final_baseline_frontier_sha256'] = frontier_hash(baseline_frontier)
                compact['all_final_unresolved_exhausted_bounded_queues'] = all(
                    row['queue_exhausted'] for row in rows if row.get('unresolved'))
                json.dump(compact, out, indent=2)
            else:
                json.dump(report, out, indent=2)
        if not frontier:
            break


if __name__ == '__main__':
    main()
