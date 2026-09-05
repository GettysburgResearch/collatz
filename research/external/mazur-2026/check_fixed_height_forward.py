#!/usr/bin/env python3
"""Nonmutating replay of PR88's exact frozen finite checker (not a proof)."""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / 'archive/research-2026-09-05/pr88-source/check_fixed_height_attack.py'
SOURCE_BLOB = 'bc2c9874e1126756260d7ec6b79bc929609a34f2'
DEFAULT_REPORT = Path(__file__).with_name('fixed-height-forward-check-report.json')


def blob_sha(data: bytes) -> str:
    return hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()


def require_equal(actual: object, expected: object) -> None:
    if actual != expected:
        raise ValueError('frozen finite report differs from exact regeneration')


def reseal(report: dict) -> None:
    report.pop('semantic_sha256', None)
    raw = json.dumps(report, sort_keys=True, separators=(',', ':')).encode()
    report['semantic_sha256'] = hashlib.sha256(raw).hexdigest()


def self_test(expected: dict) -> int:
    cases = []
    row = copy.deepcopy(expected); row['scope']['does_not_prove'] = []; cases.append(row)
    row = copy.deepcopy(expected); row['exhaustive_rows'].pop(); cases.append(row)
    row = copy.deepcopy(expected); row['finite_bound_checks'][0]['no_descent_count'] += 1; cases.append(row)
    row = copy.deepcopy(expected); row['bootstrap_algebra']['warning'] = 'proved'; cases.append(row)
    for row in cases:
        reseal(row)
        try:
            require_equal(row, expected)
        except ValueError:
            continue
        raise RuntimeError('resealed tamper accepted')
    return len(cases)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', type=Path, default=DEFAULT_REPORT)
    parser.add_argument('--self-test', action='store_true')
    args = parser.parse_args()
    source = SOURCE.read_bytes()
    if blob_sha(source) != SOURCE_BLOB:
        raise ValueError('frozen checker source blob mismatch')
    before = args.check.read_bytes()
    expected = json.loads(before)
    with tempfile.TemporaryDirectory(prefix='collatz-fh-replay-') as tmp:
        script = Path(tmp) / 'check_fixed_height_attack.py'
        script.write_bytes(source)
        # -E ignores inherited PYTHONOPTIMIZE; no -O is passed to this legacy program.
        subprocess.run([sys.executable, '-E', '-B', str(script)], cwd=tmp, check=True,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        actual = json.loads(script.with_name('fixed-height-check-report.json').read_text())
    require_equal(actual, expected)
    if args.check.read_bytes() != before:
        raise RuntimeError('frozen report changed during replay')
    if args.self_test:
        print('RESEALED TAMPERING REJECTED', self_test(actual))
    print('NONMUTATING FINITE REPLAY PASS', actual['semantic_sha256'])
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
