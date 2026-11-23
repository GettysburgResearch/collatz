#!/usr/bin/env python3
"""Replay checkpoint 18's new exact controls; no global theorem certification."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import sys


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--receipt', type=Path, required=True)
    args = parser.parse_args()
    packet = Path(__file__).resolve().parent
    root = packet.parents[3]
    report = root / 'reports/2026-11-23-global-closing'
    require(not args.receipt.resolve().is_relative_to(root),
            'Write the execution receipt outside the checkout.')
    result = {
        'schema': 'collatz-checkpoint18-scoped-execution/v1',
        'started_utc': datetime.now(timezone.utc).isoformat(),
        'python': sys.version,
        'scope': 'Frozen-file integrity and four new finite exact checkers; '
                 'not a Lean replay, proof of asymptotic statements, or Collatz proof.',
        'success': False,
        'checks': [],
        'sources': [],
    }
    try:
        manifest_path = report / 'manifest.json'
        manifest_bytes = manifest_path.read_bytes()
        manifest = json.loads(manifest_bytes)
        result['manifest_sha256'] = sha(manifest_bytes)
        for relative, expected in manifest['files'].items():
            require(sha((root / relative).read_bytes()) == expected,
                    'Frozen file mismatch: ' + relative)
        result['frozen_files_checked'] = len(manifest['files'])
        jobs = [
            ('check_generic_ray_controls.py', 'GENERIC_RAY_CONTROLS.json'),
            ('check_finite_gap_one_insertions.py', 'CHECK_RESULT.json'),
            ('check_all_gap_collisions.py', 'all-gap-collision-controls.json'),
            ('check_paired_tensor_controls.py', 'PAIRED_TENSOR_CONTROLS.json'),
        ]
        for script, record in jobs:
            outputs = []
            for optimized in (False, True):
                command = [sys.executable, '-X', 'utf8', '-B']
                if optimized:
                    command.append('-O')
                command.append(str(packet / script))
                run = subprocess.run(command, cwd=root, capture_output=True, timeout=180)
                row = {'script': script, 'optimized': optimized,
                       'exit_code': run.returncode, 'stdout_sha256': sha(run.stdout),
                       'stderr_sha256': sha(run.stderr)}
                result['checks'].append(row)
                require(run.returncode == 0, script + ' failed: ' + run.stderr.decode(errors='replace'))
                require(not run.stderr, script + ' emitted unexpected stderr')
                require(json.loads(run.stdout) == json.loads((report / record).read_bytes()),
                        script + ' does not match the frozen finite result')
                outputs.append(run.stdout)
            require(outputs[0] == outputs[1], script + ' normal/optimized outputs differ')
            print('PASS', script, 'normal and optimized; frozen result matches', flush=True)
        source_union = json.loads((packet / 'SOURCES.json').read_bytes())
        for source in source_union['repository_sources']:
            key = source['commit'] + ':' + source['path']
            run = subprocess.run(['git', 'show', key], cwd=root, capture_output=True, timeout=30)
            if source['source_available_in_integration_checkout']:
                require(run.returncode == 0, 'Required frozen source unavailable: ' + key)
                require(sha(run.stdout) == source['sha256'], 'Frozen source mismatch: ' + key)
                status = 'content hash matched; mathematical read scope is separately recorded'
            else:
                status = 'not verified: original ledger was metadata-only and had no content hash'
            result['sources'].append({'commit': source['commit'], 'path': source['path'], 'status': status})
        # Check that no control changed a frozen file while running.
        for relative, expected in manifest['files'].items():
            require(sha((root / relative).read_bytes()) == expected,
                    'A control modified frozen input: ' + relative)
        result['success'] = True
    except (OSError, ValueError, subprocess.SubprocessError) as exc:
        result['error'] = str(exc)
        print('FAIL', str(exc), flush=True)
    result['finished_utc'] = datetime.now(timezone.utc).isoformat()
    args.receipt.parent.mkdir(parents=True, exist_ok=True)
    args.receipt.write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n')
    print('PASS' if result['success'] else 'FAIL', 'checkpoint18 scoped replay; not mathematical certification')
    return 0 if result['success'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
