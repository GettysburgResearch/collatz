#!/usr/bin/env python3
"""Replay the frozen adaptive-closure packet on a clean complete checkout."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time


def need(ok, message):
    if not ok:
        raise RuntimeError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def git(root, *args):
    return subprocess.check_output(['git', *args], cwd=root, text=True).strip()


def state(root):
    return {'head': git(root, 'rev-parse', 'HEAD'),
            'tree': git(root, 'rev-parse', 'HEAD^{tree}'),
            'status': git(root, 'status', '--porcelain'),
            'tracked_files': len(git(root, 'ls-files').splitlines())}


def utc():
    return datetime.now(timezone.utc).isoformat()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--receipt', type=Path, required=True)
    parser.add_argument('--manifest-only', action='store_true')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    receipt = args.receipt.resolve()
    need(not receipt.is_relative_to(root), 'receipt must be outside the checkout')
    report_dir = root / 'reports/2026-11-21-adaptive-closure'
    manifest_path = report_dir / 'manifest.json'
    raw_manifest = manifest_path.read_bytes()
    manifest = json.loads(raw_manifest)
    started = utc()
    before = state(root)
    need(before['status'] == '', 'complete checkout must start clean')
    need((root / 'tools/validate.py').is_file(), 'complete repository is required')
    for item in manifest['files']:
        path = root / item['path']
        need(path.is_file() and digest(path.read_bytes()) == item['sha256'],
             'manifest mismatch: ' + item['path'])
    runs = []
    if not args.manifest_only:
        for job in manifest['programs']:
            for optimized in (False, True):
                command = [sys.executable]
                if optimized:
                    command.append('-OO')
                command += ['-X', 'utf8', '-B', job['path']]
                tick = time.monotonic()
                result = subprocess.run(command, cwd=root, capture_output=True)
                expected_path = root / job['optimized_report' if optimized else 'report']
                expected = expected_path.read_bytes()
                entry = {'argv': command, 'exit_code': result.returncode,
                         'seconds': round(time.monotonic() - tick, 6),
                         'stdout_sha256': digest(result.stdout),
                         'expected_sha256': digest(expected),
                         'stderr': result.stderr.decode('utf-8', errors='replace'),
                         'output_matches': result.stdout == expected}
                runs.append(entry)
                need(result.returncode == 0 and not result.stderr and result.stdout == expected,
                     'frozen scientific replay failed: ' + job['path'])
    after = state(root)
    need(after == before, 'replay changed checkout identity or cleanliness')
    result = {'status': 'PASS', 'started_utc': started, 'finished_utc': utc(),
              'before': before, 'after': after, 'manifest_only': args.manifest_only,
              'manifest_sha256': digest(raw_manifest),
              'manifest_entries': len(manifest['files']), 'runs': runs,
              'scope': 'Frozen finite exact replay and identity checks; not a proof of Collatz.'}
    receipt.parent.mkdir(parents=True, exist_ok=True)
    receipt.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
