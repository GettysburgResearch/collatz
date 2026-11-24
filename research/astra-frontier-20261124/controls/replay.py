#!/usr/bin/env python3
"""Replay the finite controls. These executions do not prove infinite theorems."""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
from pathlib import Path
import subprocess
import sys
from datetime import datetime, timezone


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--receipt', type=Path, required=True)
    args = parser.parse_args()
    directory = Path(__file__).resolve().parent
    records = []
    for name in ('reducible_checks.py', 'verify_gluing.py', 'check_first_crossing.py', 'check_farey_gate.py', 'check_global_barrier.py', 'check_even_input_refinement.py'):
        path = directory / name
        data = path.read_bytes()
        before = hashlib.sha256(data).hexdigest()
        assertions = sum(isinstance(node, ast.Assert) for node in ast.walk(ast.parse(data)))
        runs = []
        for optimize in (False, True):
            command = [sys.executable, '-X', 'utf8', '-B']
            if optimize:
                command.append('-O')
            command.append(str(path))
            result = subprocess.run(command, capture_output=True, timeout=180)
            runs.append({
                'argv': command, 'exit_code': result.returncode,
                'stdout': result.stdout.decode(), 'stderr': result.stderr.decode(),
                'stdout_sha256': hashlib.sha256(result.stdout).hexdigest(),
            })
            if result.returncode != 0:
                raise RuntimeError(f'{name} failed: {runs[-1]}')
        if runs[0]['stdout'] != runs[1]['stdout']:
            raise RuntimeError(f'optimized output differs for {name}')
        after = hashlib.sha256(path.read_bytes()).hexdigest()
        if before != after or assertions:
            raise RuntimeError(f'source changed or assert guards present: {name}')
        records.append({
            'file': name, 'sha256': before, 'source_unchanged': True,
            'ast_assert_nodes': assertions, 'normal_equals_optimized': True,
            'runs': runs,
        })
    receipt = {
        'schema': 'collatz-astra-finite-controls/v1',
        'finished_utc': datetime.now(timezone.utc).isoformat(),
        'python': sys.version,
        'scope': 'finite exact arithmetic controls; not a proof of the infinite claims or Collatz',
        'success': True, 'controls': records,
    }
    args.receipt.parent.mkdir(parents=True, exist_ok=True)
    args.receipt.write_text(json.dumps(receipt, indent=2) + '\n')
    for item in records:
        print(item['file'] + ': ' + item['runs'][0]['stdout'].strip())
    print('PASS: normal and optimized outputs agree; sources unchanged; no assert guards.')


if __name__ == '__main__':
    main()
