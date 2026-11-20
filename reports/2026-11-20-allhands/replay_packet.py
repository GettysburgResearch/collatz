#!/usr/bin/env python3
"""Replay the six scoped programs normally and with -OO; no Collatz proof."""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[2]
REPORT = Path('reports/2026-11-20-allhands')
SCIENCE = Path('research/allhands-global-closure-20261120')


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path, required=True,
                        help='outside the checkout; contains reports and receipt')
    args = parser.parse_args()
    out = args.output_dir.resolve()
    if out.is_relative_to(ROOT):
        parser.error('output directory must be outside the checkout')
    out.mkdir(parents=True, exist_ok=True)
    cases = [
        ('circulation-author', SCIENCE/'check_directed_circulation.py', [],
         'directed-circulation-report.json'),
        ('prime-support-author', SCIENCE/'check_prime_support_peaks.py', [],
         'prime-support-report.json'),
        ('depth-author', SCIENCE/'check_directed_depth.py', [],
         'directed-depth-report.json'),
        ('circulation-review', REPORT/'review_circulation.py',
         ['--author-path', str(SCIENCE/'check_directed_circulation.py')],
         'circulation-review-report.json'),
        ('prime-support-review', REPORT/'review_prime_support_independent.py',
         ['--source-dir', str(SCIENCE)], 'prime-support-independent-report.json'),
        ('depth-review', REPORT/'review_directed_depth_independent.py', [],
         'directed-depth-independent-report.json'),
    ]
    started = datetime.now(timezone.utc).isoformat()

    def execute(case: tuple, optimized: bool) -> dict:
        name, script, extra, canonical = case
        mode = 'optimized' if optimized else 'normal'
        target = out/f'{name}-{mode}.json'
        command = [sys.executable, '-X', 'utf8', '-B']
        if optimized:
            command.append('-OO')
        command += [str(script), *extra, '--output', str(target)]
        before = time.monotonic()
        result = subprocess.run(command, cwd=ROOT, capture_output=True,
                                text=True, encoding='utf-8', timeout=180)
        row = dict(name=name, mode=mode, argv=command,
                   program_sha256=digest(ROOT/script),
                   exit_code=result.returncode,
                   seconds=round(time.monotonic()-before, 3),
                   canonical_report=str(REPORT/canonical))
        if target.exists():
            row['report_sha256'] = digest(target)
            row['matches_retained_report'] = (
                target.read_bytes() == (ROOT/REPORT/canonical).read_bytes())
        else:
            row['matches_retained_report'] = False
        if result.returncode:
            row['stdout'] = result.stdout
            row['stderr'] = result.stderr
        return row

    with ThreadPoolExecutor(max_workers=6) as pool:
        futures = [pool.submit(execute, case, optimized)
                   for case in cases for optimized in (False, True)]
        rows = [future.result() for future in futures]
    equal_modes = all(rows[i].get('report_sha256') ==
                      rows[i+1].get('report_sha256')
                      for i in range(0, len(rows), 2))
    success = equal_modes and all(row['exit_code'] == 0 and
                                  row['matches_retained_report'] for row in rows)
    receipt = dict(schema='collatz-allhands-replay/v1',
                   scope='bounded exact replays, output identity and optimization safety; not universal convergence',
                   started_utc=started,
                   finished_utc=datetime.now(timezone.utc).isoformat(),
                   python=sys.version, executions=rows,
                   normal_optimized_outputs_identical=equal_modes,
                   success=success)
    (out/'execution-receipt.json').write_text(
        json.dumps(receipt, indent=2, sort_keys=True)+'\n', encoding='utf-8')
    print(json.dumps({'success': success, 'executions': len(rows),
                      'identical_modes': equal_modes,
                      'receipt': str(out/'execution-receipt.json')}))
    return 0 if success else 1


if __name__ == '__main__':
    raise SystemExit(main())
