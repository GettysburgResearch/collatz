#!/usr/bin/env python3
"""Validate a complete clean checkout; integrity is not mathematical verification."""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]


def git(root: Path, *args: str) -> bytes:
    return subprocess.run(['git', '-C', str(root), *args], check=True,
                          capture_output=True, timeout=30).stdout


def checkout_state(root: Path) -> dict:
    actual_root = Path(os.fsdecode(git(root, 'rev-parse', '--show-toplevel').strip())).resolve()
    if actual_root != root.resolve():
        raise ValueError('run from a complete repository checkout, not a nested partial copy')
    head = git(root, 'rev-parse', 'HEAD').decode().strip()
    tree = git(root, 'rev-parse', 'HEAD^{tree}').decode().strip()
    if git(root, 'status', '--porcelain', '--untracked-files=no'):
        raise ValueError('tracked files or index are dirty; preserve your work and use a clean checkout')
    files = [os.fsdecode(p) for p in git(root, 'ls-tree', '-r', '--name-only', '-z', 'HEAD').split(b'\0') if p]
    missing = [p for p in files if not (root / p).exists() and not (root / p).is_symlink()]
    if missing:
        raise ValueError('incomplete checkout; missing tracked paths: ' + ', '.join(missing[:5]))
    if any(p.startswith(b'S ') for p in git(root, 'ls-files', '-t', '-z').split(b'\0')):
        raise ValueError('sparse/skip-worktree checkout is not a full-tree validation input')
    return dict(commit=head, tree=tree, tracked_files=len(files))


def commands(regressions: bool) -> list[list[str]]:
    cmds = [
        ['tools/check_integration_state.py'],
        ['tools/check_review_integration.py'],
        ['tools/check_review_integration.py', '--self-test'],
        ['tools/test_integrity_portability.py'],
        ['reports/prepublic-2026-09-05/integration-d/check_followup.py', '--self-test'],
    ]
    if regressions:
        for script, report in [('targeted_checks.py', 'checks.json'), ('final_checks.py', 'final_checks.json')]:
            folder = 'reports/prepublic-2026-09-05/reviewer-d/'
            for mode in ([], ['-O']):
                cmds.append(mode + [folder+script, '--check', folder+report, '--self-test'])
        for mode in ([], ['-O']):
            cmds.append(mode + ['research/external/mazur-2026/check_fixed_height_forward.py', '--self-test'])
    return [[sys.executable, '-X', 'utf8', '-B', *cmd] for cmd in cmds]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--regressions', action='store_true', help='include bounded D and fixed-height replays')
    parser.add_argument('--receipt', type=Path, help='write JSON outside the checkout, including failed commands')
    args = parser.parse_args()
    if sys.version_info < (3, 11):
        parser.error('Python 3.11+ is required by the retained replay programs')
    root = args.root.resolve()
    if args.receipt and args.receipt.resolve().is_relative_to(root):
        parser.error('--receipt must be outside the checkout; validation must not change its input')
    receipt = dict(schema='collatz-checkout-validation/v1',
                   started_utc=datetime.now(timezone.utc).isoformat(),
                   python=sys.version, platform=sys.platform, scope='structure, frozen identities and selected bounded regressions; not a proof of Collatz',
                   regressions=args.regressions, commands=[], success=False)
    try:
        receipt['checkout'] = checkout_state(root)
        print('CHECKOUT', json.dumps(receipt['checkout'], sort_keys=True), flush=True)
        env = dict(os.environ, PYTHONUTF8='1', PYTHONDONTWRITEBYTECODE='1')
        for command in commands(args.regressions):
            print('RUN', ' '.join(command[1:]), flush=True)
            start = time.monotonic()
            try:
                result = subprocess.run(command, cwd=root, env=env, capture_output=True,
                                        text=True, encoding='utf-8', errors='replace', timeout=180)
                row = dict(argv=command, exit_code=result.returncode,
                           stdout=result.stdout, stderr=result.stderr)
            except subprocess.TimeoutExpired:
                row = dict(argv=command, exit_code=124, stdout='', stderr='command timed out')
            row['seconds'] = round(time.monotonic()-start, 3)
            receipt['commands'].append(row)
            print(row['stdout'], end='', flush=True)
            if row['stderr']:
                print(row['stderr'], file=sys.stderr, end='', flush=True)
        receipt['checkout_after'] = checkout_state(root)
        if receipt['checkout_after'] != receipt['checkout']:
            raise ValueError('checkout identity changed during validation')
        receipt['success'] = all(row['exit_code'] == 0 for row in receipt['commands'])
    except (OSError, ValueError, subprocess.SubprocessError) as exc:
        receipt['error'] = str(exc)
        print('ERROR:', exc, file=sys.stderr)
    receipt['finished_utc'] = datetime.now(timezone.utc).isoformat()
    if args.receipt:
        args.receipt.parent.mkdir(parents=True, exist_ok=True)
        args.receipt.write_text(json.dumps(receipt, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
    print('PASS' if receipt['success'] else 'FAIL', 'checkout validation; not mathematical verification')
    return 0 if receipt['success'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
