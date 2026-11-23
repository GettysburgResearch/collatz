#!/usr/bin/env python3
"""Freshly check this checkpoint and write an exact external receipt."""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(argv: list[str], cwd: Path, env=None) -> dict:
    result = subprocess.run(argv, cwd=cwd, env=env, capture_output=True, text=True)
    record = dict(argv=argv, cwd=str(cwd), exit_code=result.returncode,
                  stdout=result.stdout, stderr=result.stderr)
    if result.returncode:
        raise RuntimeError(json.dumps(record, indent=2))
    return record


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--lean', required=True, type=Path)
    parser.add_argument('--mathlib', required=True, type=Path)
    parser.add_argument('--receipt', required=True, type=Path)
    args = parser.parse_args()
    packet = Path(__file__).resolve().parent
    checkout = Path(subprocess.check_output(['git', 'rev-parse', '--show-toplevel'],
                                           cwd=packet, text=True).strip())
    receipt_path = args.receipt.resolve()
    if receipt_path.is_relative_to(checkout):
        raise ValueError('receipt must be outside the checkout')
    lean, mathlib = args.lean.resolve(), args.mathlib.resolve()
    dependency = packet/'lean/TriadicDualClosure.lean'
    source = packet/'lean/TriadicAmortizedBudget.lean'
    audit = packet/'lean/TriadicAmortizedAudit.lean'
    if digest(dependency) != '62a3d8a9541080864deb4887ba8c014a82222892869b14597c3b6385538913c7':
        raise ValueError('copied PR178 dependency differs from its pinned bytes')
    declarations = re.findall(r'^(def|theorem)\s+(\w+)', source.read_text(), re.MULTILINE)
    names = [name for _, name in declarations]
    audited = re.findall(r'^#print axioms CollatzTriadicBudget\.(\w+)',
                         audit.read_text(), re.MULTILINE)
    if len(names) != len(set(names)) or sorted(names) != sorted(audited):
        raise ValueError('audit must cover every new definition and theorem exactly once')
    inventory = json.loads((packet/'THEOREMS.json').read_text())
    expected = [{'kind': k, 'name': 'CollatzTriadicBudget.'+n} for k, n in declarations]
    if inventory['declarations'] != expected or inventory['new_source_sha256'] != digest(source):
        raise ValueError('theorem inventory does not bind the current source')
    for module in (dependency, source):
        code = re.sub(r'/-.*?-/', '', module.read_text(), flags=re.DOTALL)
        code = re.sub(r'--[^\n]*', '', code)
        if re.search(r'\b(sorry|admit|axiom|native_decide)\b', code):
            raise ValueError('admission, custom axiom or native shortcut found: '+module.name)
    receipt = {
        'schema': 'collatz-triadic-height-checks/v1',
        'started_utc': dt.datetime.now(dt.timezone.utc).isoformat(),
        'scope': ('New finite paired-certificate theorem and exact arithmetic controls; '
                  'no universal candidate construction or full Collatz proof. '
                  'The complete-carry congruence consumer remains written mathematics.'),
        'python': sys.version,
        'lean_version': run([str(lean), '--version'], packet)['stdout'].strip(),
        'mathlib_head': run(['git', 'rev-parse', 'HEAD'], mathlib)['stdout'].strip(),
        'mathlib_tracked_status': run(['git', 'status', '--short', '--untracked-files=no'], mathlib)['stdout'],
        'dependencies': ('Existing Mathlib/package objects reused; copied paired-state '
                         'dependency and new module freshly compiled; no historical corpus replay.'),
        'source_hashes': {str(p.relative_to(packet)): digest(p)
                          for p in (dependency, source, audit, Path(__file__), packet/'THEOREMS.json')},
        'declarations': expected,
        'finite_controls': [],
    }
    controls = [
        ('check_triadic_budget.py', []),
        ('check_triadic_review.py', ['--source', str(packet/'TRIADIC_AMORTIZED_BUDGET.md')]),
        ('check_optimal_ancestor.py', []),
    ]
    for name, extra in controls:
        path = packet/name
        normal = run([sys.executable, '-X', 'utf8', '-B', str(path), *extra], packet)
        optimized = run([sys.executable, '-X', 'utf8', '-B', '-O', str(path), *extra], packet)
        if normal['stdout'] != optimized['stdout']:
            raise ValueError('normal/optimized output mismatch: '+name)
        receipt['source_hashes'][name] = digest(path)
        receipt['finite_controls'].append({
            'file': name, 'normal_exit_code': 0, 'optimized_exit_code': 0,
            'identical_output': True,
            'output_sha256': hashlib.sha256(normal['stdout'].encode()).hexdigest(),
            'result': json.loads(normal['stdout']),
        })
    with tempfile.TemporaryDirectory(prefix='collatz-triadic-height-') as temporary:
        build = Path(temporary)
        for path in (dependency, source, audit):
            shutil.copy2(path, build/path.name)
        paths = [build, mathlib/'.lake/build/lib/lean']
        paths += sorted(p/'.lake/build/lib/lean' for p in (mathlib/'.lake/packages').iterdir())
        env = os.environ.copy()
        env['LEAN_PATH'] = os.pathsep.join(map(str, paths))
        receipt['lean_commands'] = []
        for path in (dependency, source):
            receipt['lean_commands'].append(run(
                [str(lean), '-DwarningAsError=true', '-o', path.stem+'.olean', path.name],
                build, env))
        result = run([str(lean), '-DwarningAsError=true', audit.name], build, env)
        receipt['lean_commands'].append(result)
    output = result['stdout']
    groups = re.findall(r'depends on axioms:\s*\[([^\]]*)\]', output)
    axioms = sorted({a.strip() for group in groups for a in group.split(',') if a.strip()})
    if set(axioms) - {'propext', 'Classical.choice', 'Quot.sound'} or 'sorryAx' in output:
        raise ValueError('unexpected axiom closure: '+repr(axioms))
    for name in names:
        if 'CollatzTriadicBudget.'+name not in output:
            raise ValueError('missing printed audit: '+name)
    receipt['axiom_union'] = axioms
    receipt['success'] = True
    receipt['finished_utc'] = dt.datetime.now(dt.timezone.utc).isoformat()
    receipt_path.parent.mkdir(parents=True, exist_ok=True)
    receipt_path.write_text(json.dumps(receipt, indent=2)+'\n')
    print(json.dumps({'success': True, 'declarations_audited': len(names),
                      'axioms': axioms, 'receipt': str(receipt_path)}, indent=2))


if __name__ == '__main__':
    main()
