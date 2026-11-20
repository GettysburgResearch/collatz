#!/usr/bin/env python3
"""Replay this research packet against frozen reports; not a Collatz proof."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import gzip
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
REPORTS = ROOT/'reports/2026-11-20-grh-closure'
PROGRAMS = [
    ('check_five_certificate_ladder.py', 'five-ladder-report.json', []),
    ('check_five_ladder_review.py', 'five-ladder-independent-report.json', []),
    ('check_ladder_renewal.py', 'ladder-renewal-report.json', []),
    ('check_grh_interfaces.py', 'grh-interface-report.json', []),
    ('review_grh_interfaces_independent.py', 'grh-interface-independent-report.json',
     ['--source-dir', str(HERE)]),
    ('check_rigidity_interfaces.py', 'rigidity-interfaces-report.json', []),
]


def need(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git(*args: str) -> str:
    return subprocess.run(['git', '-C', str(ROOT), *args], check=True,
                          capture_output=True, text=True).stdout.strip()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--receipt', type=Path, required=True)
    parser.add_argument('--require-clean', action='store_true')
    args = parser.parse_args()
    need(not args.receipt.resolve().is_relative_to(ROOT), 'receipt must be outside checkout')
    receipt = {'schema': 'collatz-grh-certificate-replay/v1', 'success': False,
               'started_utc': datetime.now(timezone.utc).isoformat(),
               'scope': 'frozen contents, exact finite arithmetic, raw search integrity; universal statements rely on written proofs; no full Collatz proof',
               'executions': []}
    try:
        before = {'commit': git('rev-parse', 'HEAD'), 'tree': git('rev-parse', 'HEAD^{tree}'),
                  'tracked_dirty': bool(git('status', '--porcelain', '--untracked-files=no')),
                  'untracked_or_dirty': bool(git('status', '--porcelain'))}
        receipt['checkout'] = before
        if args.require_clean:
            need(not before['untracked_or_dirty'], 'complete replay needs a clean checkout')
        manifest_path = REPORTS/'content-manifest.json'
        manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
        for row in manifest['files']:
            path = ROOT/row['path']
            need(path.is_file(), 'missing manifest file: '+row['path'])
            raw = path.read_bytes()
            need(len(raw) == row['bytes'] and sha(raw) == row['sha256'],
                 'manifest mismatch: '+row['path'])
        receipt['manifest_files_checked'] = len(manifest['files'])
        receipt['manifest_sha256'] = sha(manifest_path.read_bytes())
        searches = json.loads((REPORTS/'bounded-level-search-summary.json').read_text(encoding='utf-8'))
        for row in searches:
            raw = gzip.decompress((REPORTS/f"level-{row['J']}.json.gz").read_bytes())
            need(sha(raw) == row['raw_report_sha256'], 'raw search archive mismatch')
            data = json.loads(raw)
            for key in ('J', 'pops', 'certified_cells', 'uncovered_leaves', 'unsearched_cells'):
                need(data[key] == row[key], 'raw search summary mismatch: '+key)
            need(data['unsearched_cells'] == 0, 'retained searches completed within their bounds')
        receipt['raw_search_archives_checked'] = len(searches)
        env = dict(os.environ, PYTHONUTF8='1', PYTHONDONTWRITEBYTECODE='1')
        for script, report, extra in PROGRAMS:
            expected = (REPORTS/report).read_bytes()
            for optimized in (False, True):
                command = [sys.executable, '-X', 'utf8', '-B']
                if optimized:
                    command.append('-OO')
                command.extend([str(HERE/script), *extra])
                start = time.monotonic()
                result = subprocess.run(command, cwd=ROOT, env=env,
                                        capture_output=True, timeout=90)
                row = {'script': script, 'optimized': optimized,
                       'exit_code': result.returncode,
                       'seconds': round(time.monotonic()-start, 3),
                       'stdout_sha256': sha(result.stdout),
                       'reference_report': str((REPORTS/report).relative_to(ROOT)),
                       'reference_sha256': sha(expected),
                       'reference_bytes_match': result.stdout == expected,
                       'stderr': result.stderr.decode('utf-8', errors='replace')}
                receipt['executions'].append(row)
                need(result.returncode == 0, 'failed execution: '+script)
                need(result.stdout == expected, 'report differs: '+script)
                need(json.loads(result.stdout)['status'] == 'PASS', 'nonpass report: '+script)
                print('PASS', script, '-OO' if optimized else 'normal', flush=True)
        after = {'commit': git('rev-parse', 'HEAD'), 'tree': git('rev-parse', 'HEAD^{tree}'),
                 'tracked_dirty': bool(git('status', '--porcelain', '--untracked-files=no')),
                 'untracked_or_dirty': bool(git('status', '--porcelain'))}
        need(before == after, 'checkout changed during replay')
        receipt['checkout_after'] = after
        receipt['success'] = True
    except (OSError, ValueError, subprocess.SubprocessError, KeyError) as exc:
        receipt['error'] = str(exc)
        print('FAIL', str(exc), flush=True)
    receipt['finished_utc'] = datetime.now(timezone.utc).isoformat()
    args.receipt.parent.mkdir(parents=True, exist_ok=True)
    args.receipt.write_text(json.dumps(receipt, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
    print('PASS' if receipt['success'] else 'FAIL', 'packet replay; not full Collatz closure')
    return 0 if receipt['success'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
