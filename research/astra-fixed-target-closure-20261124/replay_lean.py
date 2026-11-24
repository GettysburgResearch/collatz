"""Compile the finite kernels in an existing pinned Lean/Mathlib environment.

No dependency is installed or downloaded. Generated oleans live in a temporary
directory, outside the checkout. JSON goes to stdout; redirect it outside the
checkout when replaying a clean publication. This is not an analytic proof.
"""

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile


def run(command, cwd, env):
    result = subprocess.run(command, cwd=cwd, env=env, capture_output=True,
                            text=True, timeout=180)
    return result.returncode, result.stdout + result.stderr


def git_text(root, *args):
    return subprocess.check_output(['git', *args], cwd=root, text=True).strip()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--mathlib-root', type=Path, required=True)
    parser.add_argument('--lean-bin', type=Path, required=True)
    args = parser.parse_args()
    mathlib = args.mathlib_root.resolve()
    lean_bin = args.lean_bin.resolve()
    here = Path(__file__).resolve().parent
    repo = here.parent.parent
    env = os.environ.copy()
    env['PATH'] = str(lean_bin) + os.pathsep + env.get('PATH', '')
    expected_lean = '5045d0056413266e57c625dcd7c365b10e377c52'
    expected_mathlib = 'd13f23b723b8a846827a245b89c10fc7d3f11612'
    code, version = run([str(lean_bin / 'lean'), '--version'], mathlib, env)
    if code or expected_lean not in version:
        raise RuntimeError('Unexpected Lean compiler: ' + version)
    if git_text(mathlib, 'rev-parse', 'HEAD') != expected_mathlib:
        raise RuntimeError('Unexpected Mathlib revision')
    if git_text(mathlib, 'status', '--porcelain', '--untracked-files=no'):
        raise RuntimeError('Mathlib has tracked changes')
    manifest = json.loads((mathlib / 'lake-manifest.json').read_text())
    dependencies = []
    for item in manifest['packages']:
        root = mathlib / manifest['packagesDir'] / item['name']
        revision = git_text(root, 'rev-parse', 'HEAD')
        dirty = git_text(root, 'status', '--porcelain', '--untracked-files=no')
        if revision != item['rev'] or dirty:
            raise RuntimeError('Dependency does not match manifest: ' + item['name'])
        dependencies.append({'name': item['name'], 'revision': revision,
                             'tracked_clean': True})
    code, path = run([str(lean_bin / 'lake'), 'env', 'printenv', 'LEAN_PATH'],
                     mathlib, env)
    if code:
        raise RuntimeError(path)
    paths = [str((mathlib / p).resolve()) if not Path(p).is_absolute() else p
             for p in path.strip().split(os.pathsep) if p]
    rows = []
    allowed = {'propext', 'Classical.choice', 'Quot.sound'}
    with tempfile.TemporaryDirectory(prefix='collatz-fixed-target-lean-') as temp:
        build = Path(temp)
        env['LEAN_PATH'] = os.pathsep.join([str(build), *paths])
        tasks = []
        for name in ['SourceDeletion', 'MinimumFailure', 'UpperRepresentative']:
            source = here / 'ordinary/dependencies' / (name + '.lean')
            copied = build / source.name
            shutil.copyfile(source, copied)
            tasks.append((source, copied, ['-o', str(build / (name + '.olean'))],
                          'byte-identical dependency'))
        tasks.extend((here / p, here / p, ['-DautoImplicit=false'], 'finite kernel')
                     for p in ['lean/ClockTransport.lean', 'lean/MixedTransport.lean',
                               'lean/CentralInverseBarrier.lean',
                               'arithmetic/CompanionPacking.lean',
                               'ordinary/OneEvenEscape.lean'])
        for source, compile_path, extra, kind in tasks:
            command = [str(lean_bin / 'lean'), '-j1', '-DwarningAsError=true',
                       *extra, str(compile_path)]
            code, output = run(command, compile_path.parent, env)
            declarations = []
            for match in re.finditer(
                    r"'([^']+)' (?:depends on axioms: \[([^\]]*)\]|does not depend on any axioms)",
                    output):
                axioms = [x.strip() for x in (match.group(2) or '').split(',') if x.strip()]
                if not set(axioms) <= allowed:
                    raise RuntimeError('Unexpected axiom dependency: ' + match.group(0))
                declarations.append({'name': match.group(1), 'axioms': axioms})
            rows.append({'path': str(source.relative_to(repo)), 'kind': kind,
                         'sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
                         'command': command, 'cwd': str(compile_path.parent),
                         'returncode': code, 'output': output,
                         'axiom_audit': declarations})
            if code:
                break
    result = {'scope': 'Finite Lean kernels and exact imported dependencies only; '
                       'no formalization of the analytic floor, entropy limits, '
                       'stationary probability, or full Collatz.',
              'compiler_version': version.strip(),
              'compiler_sha256': hashlib.sha256((lean_bin / 'lean').read_bytes()).hexdigest(),
              'mathlib_revision': expected_mathlib,
              'mathlib_tracked_clean': True, 'packages': dependencies,
              'passed': len(rows) == 8 and all(r['returncode'] == 0 for r in rows),
              'modules': rows,
              'audited_declaration_count': sum(len(r['axiom_audit']) for r in rows)}
    print(json.dumps(result, indent=2))
    if not result['passed']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
