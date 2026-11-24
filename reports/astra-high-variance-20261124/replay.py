#!/usr/bin/env python3
"""Fresh, source-hashed replay of this packet; no mathematical claims by census."""
from __future__ import annotations

import argparse
import ast
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[2]
PACKET = ROOT / 'research/astra-high-variance-20261124'
ALLOWED_AXIOMS = {'propext', 'Classical.choice', 'Quot.sound'}


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def demand(ok: bool, message: str) -> None:
    if not ok:
        raise RuntimeError(message)


def git(*args: str) -> str:
    return subprocess.run(['git', '-C', str(ROOT), *args], check=True,
                          capture_output=True, text=True).stdout.strip()


def manifest() -> dict[str, str]:
    return {str(p.relative_to(ROOT)): digest(p.read_bytes())
            for p in sorted(PACKET.iterdir()) if p.is_file()}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--lean', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    out = args.output.resolve()
    demand(not out.is_relative_to(ROOT), 'replay output must be outside the checkout')
    demand(not out.exists(), 'use a new empty output directory')
    demand(not git('status', '--porcelain'), 'source checkpoint must be fully clean')
    out.mkdir(parents=True)
    objects = out / 'objects'
    objects.mkdir()
    env = dict(os.environ, PYTHONUTF8='1', PYTHONDONTWRITEBYTECODE='1',
               PYTHONPYCACHEPREFIX=str(out / 'unused-python-cache'))
    env.pop('LEAN_PATH', None)  # Every module in this packet imports only Std.
    receipt = {
        'schema': 'collatz-astra-high-variance-replay/v1',
        'started_utc': datetime.now(timezone.utc).isoformat(),
        'scope': 'exact new sources, fresh Lean objects, finite controls, repository integrity',
        'commit': git('rev-parse', 'HEAD'), 'tree': git('rev-parse', 'HEAD^{tree}'),
        'sources_before': manifest(), 'python': sys.version,
        'commands': [], 'lean_audits': [], 'python_pairs': [], 'success': False,
    }

    def run(label: str, argv: list[str], timeout: int = 180) -> dict:
        start = time.monotonic()
        proc = subprocess.run(argv, cwd=ROOT, env=env, capture_output=True, timeout=timeout)
        (out / (label + '.stdout.log')).write_bytes(proc.stdout)
        (out / (label + '.stderr.log')).write_bytes(proc.stderr)
        row = {'label': label, 'argv': argv, 'exit_code': proc.returncode,
               'seconds': round(time.monotonic() - start, 3),
               'stdout_sha256': digest(proc.stdout), 'stderr_sha256': digest(proc.stderr)}
        receipt['commands'].append(row)
        print(label, 'exit', proc.returncode, 'seconds', row['seconds'], flush=True)
        demand(proc.returncode == 0, label + ' failed; inspect logs')
        return {'row': row, 'stdout': proc.stdout, 'stderr': proc.stderr}

    try:
        version = run('lean-version', [str(args.lean.resolve()), '--version'])
        receipt['lean_version'] = version['stdout'].decode().strip()
        for source in sorted(PACKET.glob('*.lean')):
            text = source.read_text()
            imports = re.findall(r'^import\s+(.+)$', text, re.M)
            demand(imports == ['Std'], 'unexpected imports in ' + source.name)
            demand(not re.search(r'\b(sorry|admit|axiom)\b', text),
                   'unchecked proof token in ' + source.name)
            names = re.findall(r'^#print axioms\s+(\S+)\s*$', text, re.M)
            demand(bool(names), 'missing named axiom audits in ' + source.name)
            obj = objects / (source.stem + '.olean')
            result = run('lean-' + source.stem, [str(args.lean.resolve()), '-j1',
                         '-DwarningAsError=true', '-o', str(obj), str(source)])
            stdout = result['stdout'].decode()
            demand(not result['stderr'], 'unexpected Lean stderr')
            demand(not re.search(r'\b(warning|error):', stdout), 'Lean diagnostic')
            audits = re.findall(r"'([^']+)' depends on axioms: \[([^\]]*)\]", stdout)
            demand(len(audits) == len(names), 'missing or additional printed audits')
            for requested, (qualified, values) in zip(names, audits):
                demand(qualified == requested or qualified.endswith('.' + requested),
                       'audit name mismatch: ' + requested)
                axioms = {x.strip() for x in values.split(',') if x.strip()}
                demand(axioms <= ALLOWED_AXIOMS, 'unexpected transitive axiom')
                receipt['lean_audits'].append({'source': source.name,
                    'declaration': qualified, 'axioms': sorted(axioms)})
            result['row']['object_sha256'] = digest(obj.read_bytes())

        for source in sorted(PACKET.glob('*.py')):
            tree = ast.parse(source.read_text())
            assertions = sum(isinstance(n, ast.Assert) for n in ast.walk(tree))
            demand(assertions == 0, 'assert disappears under optimization: ' + source.name)
            outputs = []
            for optimized in (False, True):
                label = ('python-opt-' if optimized else 'python-') + source.stem
                argv = [sys.executable, '-X', 'utf8', '-B']
                if optimized:
                    argv.append('-O')
                outputs.append(run(label, argv + [str(source)]))
            demand(outputs[0]['stdout'] == outputs[1]['stdout'] and
                   outputs[0]['stderr'] == outputs[1]['stderr'],
                   'normal/optimized output differs: ' + source.name)
            receipt['python_pairs'].append({'source': source.name,
                'identical_output': True, 'assert_nodes': assertions})

        run('repository-validation', [sys.executable, '-X', 'utf8', '-B',
            'tools/validate.py', '--receipt', str(out / 'repository-validation.json')])
        receipt['sources_after'] = manifest()
        demand(receipt['sources_before'] == receipt['sources_after'], 'sources changed during replay')
        demand(git('rev-parse', 'HEAD') == receipt['commit'] and
               git('rev-parse', 'HEAD^{tree}') == receipt['tree'], 'checkout changed during replay')
        demand(not git('status', '--porcelain'), 'replay changed checkout state')
        receipt['success'] = True
    finally:
        receipt['finished_utc'] = datetime.now(timezone.utc).isoformat()
        (out / 'receipt.json').write_text(json.dumps(receipt, indent=2) + '\n')
    print('PASS', len(receipt['lean_audits']), 'named Lean audits;',
          len(receipt['python_pairs']), 'normal/optimized control pairs', flush=True)


if __name__ == '__main__':
    main()
