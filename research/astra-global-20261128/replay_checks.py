#!/usr/bin/env python3
"""Replay every bounded control in this packet with and without optimization.

The receipt describes finite computations only. None establishes a universal
cycle, trace, or Collatz theorem. No dependency is downloaded or mutated.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time

PACKET = Path(__file__).resolve().parent


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--receipt', type=Path, required=True)
    args = parser.parse_args()
    scripts = sorted(PACKET.rglob('check_*.py'))
    before = {str(p.relative_to(PACKET)): sha(p) for p in scripts}
    receipt = {
        'schema': 'collatz-global-bounded-controls/v1',
        'scope': 'bounded exact controls only; no universal Collatz proof',
        'started_utc': datetime.now(timezone.utc).isoformat(),
        'python': sys.version,
        'source_hashes': before,
        'runs': [],
        'passed': False,
    }
    try:
        if not scripts:
            raise RuntimeError('No bounded control scripts found')
        for script in scripts:
            outputs = []
            for optimize in (False, True):
                cmd = [sys.executable, '-X', 'utf8', '-B']
                if optimize:
                    cmd.append('-O')
                cmd.append(str(script))
                started = time.monotonic()
                result = subprocess.run(cmd, cwd=PACKET, text=True,
                    capture_output=True, env=dict(os.environ, PYTHONHASHSEED='0'))
                row = {
                    'source': str(script.relative_to(PACKET)),
                    'optimized': optimize,
                    'exit_code': result.returncode,
                    'seconds': round(time.monotonic()-started, 4),
                    'stdout': result.stdout,
                    'stderr': result.stderr,
                }
                receipt['runs'].append(row)
                if result.returncode:
                    raise RuntimeError(f'{script.name} failed: {result.stderr}')
                outputs.append(result.stdout)
            if outputs[0] != outputs[1]:
                raise RuntimeError(f'Optimization changed output: {script.name}')
            print(f'PASS {script.relative_to(PACKET)} (normal and -O)', flush=True)
        after = {str(p.relative_to(PACKET)): sha(p)
                 for p in sorted(PACKET.rglob('check_*.py'))}
        if after != before:
            raise RuntimeError('Control sources changed during replay')
        receipt['paired_control_count'] = len(scripts)
        receipt['passed'] = True
    except Exception as exc:
        receipt['error'] = str(exc)
        print(f'FAIL: {exc}', flush=True)
    finally:
        receipt['finished_utc'] = datetime.now(timezone.utc).isoformat()
        args.receipt.parent.mkdir(parents=True, exist_ok=True)
        args.receipt.write_text(json.dumps(receipt, indent=2)+'\n')
    return 0 if receipt['passed'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
