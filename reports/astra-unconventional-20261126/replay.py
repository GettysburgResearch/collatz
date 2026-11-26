#!/usr/bin/env python3
"""Replay the unconventional packet from a clean complete checkout."""
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
NEW_PACKET = ROOT / 'research/astra-unconventional-20261126'
PACKETS = (NEW_PACKET,)
DEPENDENCIES = []
REVIEW_CONTROLS = []
REVIEW_SOURCES = []
CONTROL_NAMES = ['adelic/check.py', 'descent/check.py']
ALLOWED_AXIOMS = {'propext', 'Classical.choice', 'Quot.sound'}


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def demand(ok: bool, message: str) -> None:
    if not ok:
        raise RuntimeError(message)


def git(*args: str, root: Path = ROOT) -> str:
    return subprocess.run(['git', '-C', str(root), *args], check=True,
                          capture_output=True, text=True).stdout.strip()


def manifest() -> dict[str, str]:
    return {str(p.relative_to(ROOT)): digest(p.read_bytes())
            for p in sorted(set(DEPENDENCIES + REVIEW_CONTROLS + REVIEW_SOURCES + [q for packet in PACKETS
                for q in packet.rglob('*') if q.is_file()]))}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--lean', type=Path, required=True)
    parser.add_argument('--mathlib', type=Path, required=True)
    parser.add_argument('--cached-mathlib', type=Path, required=True)
    parser.add_argument('--leanpath-file', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    out = args.output.resolve()
    demand(not out.is_relative_to(ROOT), 'output must be outside the checkout')
    demand(not out.exists(), 'use a new output directory')
    demand(not git('status', '--porcelain'), 'source checkout must be clean')
    out.mkdir(parents=True)
    objects = out / 'objects'
    objects.mkdir()
    dependency_path = args.leanpath_file.read_text().strip()
    env = dict(os.environ, PYTHONUTF8='1', PYTHONDONTWRITEBYTECODE='1',
               PYTHONPYCACHEPREFIX=str(out / 'unused-python-cache'),
               LEAN_PATH=str(objects) + os.pathsep + dependency_path)
    receipt = {
        'schema': 'collatz-astra-unconventional-replay/v1',
        'started_utc': datetime.now(timezone.utc).isoformat(),
        'scope': 'All new public Lean declarations and specified finite controls; not the infinite written arguments or external range verification',
        'commit': git('rev-parse', 'HEAD'), 'tree': git('rev-parse', 'HEAD^{tree}'),
        'tracked_file_count': len(git('ls-files').splitlines()),
        'sources_before': manifest(), 'python': sys.version,
        'mathlib_commit': git('rev-parse', 'HEAD', root=args.mathlib),
        'dependency_objects': 'pinned Lean and Mathlib dependency objects reused; every project dependency and new module rebuilt in a new empty object directory',
        'lean_path': env['LEAN_PATH'],
        'commands': [], 'lean_audits': [], 'python_pairs': [], 'success': False,
    }

    def run(label: str, argv: list[str], timeout: int = 300) -> dict:
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
        source_names = [name for name in git('ls-files', root=args.mathlib).splitlines()
                        if name.endswith('.lean') or name in
                        {'lean-toolchain', 'lake-manifest.json', 'lakefile.lean', 'lakefile.toml'}]
        combined = hashlib.sha256()
        for name in source_names:
            fresh = (args.mathlib / name).read_bytes()
            cached = (args.cached_mathlib / name).read_bytes()
            demand(fresh == cached, 'cached Mathlib source mismatch: ' + name)
            combined.update(name.encode() + b'\0' + hashlib.sha256(fresh).digest())
        receipt['mathlib_source_comparison'] = {
            'files': len(source_names), 'mismatches': 0,
            'source_manifest_sha256': combined.hexdigest(),
            'fresh_checkout': str(args.mathlib.resolve()),
            'cached_source_tree': str(args.cached_mathlib.resolve()),
        }
        new_sources = sorted(NEW_PACKET.rglob('*.lean'))
        lean_sources = DEPENDENCIES + new_sources
        demand(bool(new_sources), 'no new Lean sources')
        receipt['new_module_count'] = len(new_sources)
        receipt['project_dependency_count'] = len(DEPENDENCIES)
        by_stem = {p.stem: p for p in lean_sources}
        ordered, visiting, done = [], set(), set()
        def visit(p):
            demand(p not in visiting, 'cyclic project imports')
            if p in done:
                return
            visiting.add(p)
            for name in re.findall(r'^import\s+(\S+)', p.read_text(), re.M):
                if name in by_stem:
                    visit(by_stem[name])
            visiting.remove(p)
            done.add(p)
            ordered.append(p)
        for p in lean_sources:
            visit(p)
        lean_sources = ordered
        demand(len({p.stem for p in lean_sources}) == len(lean_sources),
               'module basename collision')
        demand(receipt['mathlib_commit'] == 'd13f23b723b8a846827a245b89c10fc7d3f11612',
               'unexpected Mathlib revision')
        demand('version 4.34.1,' in receipt['lean_version'], 'unexpected Lean version')
        demand(bool(lean_sources), 'no Lean sources')
        for source in lean_sources:
            content = source.read_text()
            proof_text = re.sub(r'/-.*?-/', '', content, flags=re.S)
            demand(not re.search(r'\b(sorry|admit|axiom|native_decide)\b', proof_text),
                   'unchecked proof token in ' + source.name)
            names = re.findall(r'^#print axioms\s+(\S+)\s*$', content, re.M)
            demand(bool(names), 'missing named audits in ' + source.name)
            public_names = re.findall(r'^(?:@\[[^\n]*\]\s*)*(?:theorem|lemma)\s+(\w+)', content, re.M)
            demand(len(names) == len(set(names)) and {n.rsplit('.', 1)[-1] for n in names} == set(public_names),
                   'every public theorem must be audited exactly once: ' + source.name)
            label = source.parent.name + '-' + source.stem
            obj = objects / (source.stem + '.olean')
            result = run('lean-' + label, [str(args.lean.resolve()), '-j1',
                         '-DwarningAsError=true', '-DautoImplicit=false',
                         '-o', str(obj), str(source)])
            stdout = result['stdout'].decode()
            demand(not result['stderr'], 'unexpected Lean stderr')
            demand(not re.search(r'\b(warning|error):', stdout), 'Lean diagnostic')
            audits = re.findall(
                r"'([^']+)' (?:depends on axioms: \[([^\]]*)\]|does not depend on any axioms)",
                stdout)
            demand(len(audits) == len(names), 'missing or additional printed audits')
            for requested, (qualified, values) in zip(names, audits):
                demand(qualified == requested or qualified.endswith('.' + requested),
                       'audit name mismatch: ' + requested)
                axioms = {x.strip() for x in values.split(',') if x.strip()}
                demand(axioms <= ALLOWED_AXIOMS, 'unexpected transitive axiom')
                receipt['lean_audits'].append({'source': str(source.relative_to(ROOT)),
                    'declaration': qualified, 'axioms': sorted(axioms)})
            result['row']['object_sha256'] = digest(obj.read_bytes())

        controls = [NEW_PACKET / name for name in CONTROL_NAMES] + REVIEW_CONTROLS
        demand(bool(controls), 'no finite controls')
        for source in controls:
            tree = ast.parse(source.read_text())
            assertions = sum(isinstance(n, ast.Assert) for n in ast.walk(tree))
            demand(assertions == 0, 'assert disappears under optimization: ' + source.name)
            outputs = []
            for optimized in (False, True):
                label = ('python-opt-' if optimized else 'python-') + source.parent.name + '-' + source.stem
                argv = [sys.executable, '-X', 'utf8', '-B']
                if optimized:
                    argv.append('-O')
                outputs.append(run(label, argv + [str(source)]))
            demand(outputs[0]['stdout'] == outputs[1]['stdout'] and
                   outputs[0]['stderr'] == outputs[1]['stderr'],
                   'normal/optimized output differs: ' + source.name)
            receipt['python_pairs'].append({'source': str(source.relative_to(ROOT)),
                'identical_output': True, 'assert_nodes': assertions})

        run('repository-validation', [sys.executable, '-X', 'utf8', '-B',
            'tools/validate.py', '--regressions', '--receipt', str(out / 'repository-validation.json')])
        receipt['sources_after'] = manifest()
        demand(receipt['sources_before'] == receipt['sources_after'], 'sources changed during replay')
        demand(git('rev-parse', 'HEAD') == receipt['commit'] and
               git('rev-parse', 'HEAD^{tree}') == receipt['tree'], 'checkout changed during replay')
        demand(not git('status', '--porcelain'), 'replay changed checkout state')
        receipt['success'] = True
    finally:
        receipt['finished_utc'] = datetime.now(timezone.utc).isoformat()
        (out / 'receipt.json').write_text(json.dumps(receipt, indent=2) + '\n')
    print('PASS', len(receipt['lean_audits']), 'named Lean audits (new modules and dependencies);',
          len(receipt['python_pairs']), 'normal/optimized control pairs', flush=True)


if __name__ == '__main__':
    main()
