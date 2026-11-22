#!/usr/bin/env python3
"""Replay this continuation and only its required Lean source dependencies.

Requires an existing Lean 4.34.1 and the pinned built Mathlib checkout.
No downloads; all generated sources, compiler artifacts, and logs are external.
The required repository gate runs in the same clean complete checkout.
"""
from __future__ import annotations

import argparse
import difflib
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import time

sys.dont_write_bytecode = True
PACKET = Path('research/whole-repo-closure-20261122')
PREVIOUS = Path('research/literature-orbit-closure-20261121')
BASE = Path('research/lean-band-coupling-20261121')
LEAN_COMMIT = '5045d0056413266e57c625dcd7c365b10e377c52'
MATHLIB_COMMIT = 'd13f23b723b8a846827a245b89c10fc7d3f11612'
PORT_HASH = '2d0a4df167bd6f5c920283584ae9c12370ea3621bc75fcfcf4bebbf5ebcbb785'
PORT_SOURCES = {
    'ShellCover': '76477e195c733e8b8c9fdf523d954d85375b3ac244ee0590127192743bffc88c',
    'ForwardSection': 'f134020b95f79c3b90cfe104c7d4234ee8d162c97acaa02c6aefc6ec86d19ae4',
    'SectionDynamics': '94c05e9cfc738b319acb52e9c6f07b0344dc87cb31ed4ed49cb2540fde51c9ac',
}
ALLOW = {'propext', 'Classical.choice', 'Quot.sound'}


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def require(ok, message):
    if not ok:
        raise ValueError(message)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--lean', type=Path, required=True)
    parser.add_argument('--mathlib', type=Path, required=True)
    parser.add_argument('--build-dir', type=Path, required=True)
    parser.add_argument('--repo', type=Path)
    args = parser.parse_args()
    repo = args.repo.resolve() if args.repo else Path(__file__).resolve().parents[2]
    lean, mathlib, build = args.lean.resolve(), args.mathlib.resolve(), args.build_dir.resolve()
    require((repo/PACKET/'README.md').is_file(), 'complete packet missing')
    require(not build.is_relative_to(repo) and not build.is_relative_to(mathlib), 'external build directory required')
    require(not (build/'receipt.json').exists(), 'use a fresh build directory')
    source, library, logs = build/'source', build/'lib', build/'logs'
    for path in (source, library, logs):
        path.mkdir(parents=True, exist_ok=True)
    receipt = {'schema': 'collatz-whole-repo-continuation-replay/v1', 'complete': False,
               'started_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
               'repository': str(repo), 'inputs': [], 'commands': [], 'modules': []}
    env = dict(os.environ)
    env['PYTHONDONTWRITEBYTECODE'] = '1'

    def save():
        (build/'receipt.json').write_text(json.dumps(receipt, indent=2)+'\n')

    def record(path, expected=None):
        raw = path.read_bytes()
        item = {'path': str(path.relative_to(repo)), 'sha256': digest(raw)}
        if not any(x['path'] == item['path'] for x in receipt['inputs']):
            receipt['inputs'].append(item)
        require(expected is None or item['sha256'] == expected, f'pinned input mismatch: {path}')
        return raw

    def run(label, argv, cwd=repo, echo=False):
        item = {'label': label, 'argv': [str(x) for x in argv], 'cwd': str(cwd)}
        receipt['commands'].append(item)
        save()
        start = time.monotonic()
        p = subprocess.run(item['argv'], cwd=cwd, env=env, text=True,
                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        log = logs/f'{len(receipt["commands"]):02d}-{label}.log'
        log.write_text(p.stdout)
        item.update(exit_code=p.returncode, seconds=round(time.monotonic()-start, 3),
                    log=str(log), log_sha256=digest(p.stdout.encode()))
        save()
        if echo or p.returncode:
            print(p.stdout, end='', flush=True)
        require(p.returncode == 0, f'{label} failed; see {log}')
        return p.stdout

    try:
        receipt['head'] = run('head', ['git', 'rev-parse', 'HEAD']).strip()
        receipt['tree'] = run('tree', ['git', 'rev-parse', 'HEAD^{tree}']).strip()
        before = run('status-before', ['git', 'status', '--porcelain=v1'])
        require(not before.strip(), 'clean checkout required')
        tracked = run('tracked-files', ['git', 'ls-files', '-z']).split('\0')
        tracked = [x for x in tracked if x]
        require(all((repo/x).exists() or (repo/x).is_symlink() for x in tracked), 'incomplete checkout')
        receipt['tracked_files'] = len(tracked)
        version = run('lean-version', [lean, '--version']).strip()
        require('version 4.34.1' in version and LEAN_COMMIT in version, 'wrong Lean revision')
        receipt['lean_version'] = version
        mhead = run('mathlib-head', ['git', 'rev-parse', 'HEAD'], mathlib).strip()
        require(mhead == MATHLIB_COMMIT, 'wrong Mathlib revision')
        receipt['mathlib_commit'] = mhead
        record(repo/BASE/'check.py', PORT_HASH)
        spec = importlib.util.spec_from_file_location('_frozen_pr184_port', repo/BASE/'check.py')
        require(spec is not None and spec.loader is not None, 'missing source port')
        port = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(port)
        manifest = json.loads(record(repo/PACKET/'DEPENDENCIES.json'))
        require(manifest['lean_commit'] == LEAN_COMMIT and manifest['mathlib_commit'] == MATHLIB_COMMIT, 'runtime manifest mismatch')
        vendors = {row['module']: row for row in manifest['vendor_sources']}
        targets = sorted(x.stem for x in (repo/PACKET/'lean').glob('*.lean'))
        require(bool(targets), 'no new Lean sources')
        pending, ordered, prepared, paths = set(), [], {}, {}

        def visit(name):
            if name in prepared:
                return
            require(name not in pending, 'cyclic local imports')
            options = [repo/base/'lean'/f'{name}.lean' for base in (PACKET, PREVIOUS, BASE)]
            options.append(repo/PACKET/'lean/vendor'/f'{name}.lean')
            found = [path for path in options if path.is_file()]
            require(len(found) == 1, f'ambiguous or missing local module {name}')
            path = found[0]
            expected = vendors[name]['sha256'] if name in vendors else PORT_SOURCES.get(name)
            raw = record(path, expected).decode()
            text = port.module_port(name, raw) if name in PORT_SOURCES else raw
            if name in vendors:
                require(path == repo/vendors[name]['path'], 'vendor location mismatch')
                header = re.match(r'(?:import [^\n]+\n)+', raw)
                require(header is not None, 'unexpected vendor import header')
                imports = '\n'.join('public '+line for line in header.group(0).splitlines())
                text = 'module\n\n'+imports+'\n\n@[expose] public section\n'+raw[header.end():]
            pending.add(name)
            # Only the actual initial Lean header is syntax. Inherited module
            # documentation contains a prose line beginning with "import".
            for line in text.splitlines():
                clean = line.strip()
                if not clean or clean in {'module', 'prelude'} or clean.startswith('--'):
                    continue
                imported_line = re.fullmatch(r'(?:public\s+)?import\s+(.+)', clean)
                if imported_line is None:
                    break
                for imported in imported_line.group(1).split('--', 1)[0].split():
                    if imported.split('.')[0] not in {'Mathlib', 'Std', 'Init', 'Lean', 'Batteries', 'Aesop', 'Qq'}:
                        visit(imported)
            pending.remove(name)
            prepared[name], paths[name] = text, path
            (source/f'{name}.lean').write_text(text)
            ordered.append(name)

        for target in targets:
            visit(target)
        deps = [mathlib/'.lake/build/lib/lean']
        deps += sorted((mathlib/'.lake/packages').glob('*/.lake/build/lib/lean'))
        require((deps[0]/'Mathlib/Tactic/IntervalCases.olean').is_file(), 'required Mathlib cache unavailable')
        env['LEAN_PATH'] = os.pathsep.join(str(x) for x in [library, *deps])
        receipt['lean_path'] = env['LEAN_PATH']
        patches = []
        for name in ordered:
            original = paths[name].read_text()
            patches.extend(difflib.unified_diff(original.splitlines(True), prepared[name].splitlines(True),
                fromfile=str(paths[name].relative_to(repo)), tofile=f'generated/{name}.lean', n=0))
        patch = ''.join(patches)
        (build/'module-port.patch').write_text(patch)
        receipt['module_port_sha256'] = digest(patch.encode())
        for path in sorted((repo/PACKET).rglob('*')):
            if path.is_file():
                record(path)
        record(repo/'tools/validate.py')
        total = 0
        for name in ordered:
            print(f'Checking {name} ...', flush=True)
            output = run(name, [lean, '-j1', '-DwarningAsError=true', '-o', library/f'{name}.olean', f'{name}.lean'], source, True)
            audits = []
            for declaration, body in re.findall(r"'([^']+)' depends on axioms: \[([^\]]*)\]", output):
                axioms = {x.strip() for x in body.split(',') if x.strip()}
                require(axioms <= ALLOW, f'unexpected axioms for {declaration}: {axioms-ALLOW}')
                audits.append({'declaration': declaration, 'axioms': sorted(axioms)})
            for declaration in re.findall(r"'([^']+)' does not depend on any axioms", output):
                audits.append({'declaration': declaration, 'axioms': []})
            require(not re.search(r'\b(sorryAx|Lean\.ofReduceBool)\b', output), 'unfinished/native proof mechanism')
            if name in targets:
                commands = re.findall(r'^#print axioms (\S+)', prepared[name], re.M)
                declarations = [decl for modifiers, decl in re.findall(
                    r'^((?:(?:public|private|protected)\s+)*)(?:theorem|lemma)\s+(\w+)',
                    prepared[name], re.M) if 'private' not in modifiers.split()]
                actual = [x['declaration'] for x in audits]
                require(len(audits) == len(commands) == len(declarations), f'incomplete theorem audit in {name}')
                require(len(set(actual)) == len(actual), f'duplicate audit in {name}')
                require(sorted(x.rsplit('.', 1)[-1] for x in actual) == sorted(declarations), f'audited declarations differ in {name}')
                total += len(audits)
            receipt['modules'].append({'module': name, 'new': name in targets,
                'source': str(paths[name].relative_to(repo)), 'source_sha256': digest(paths[name].read_bytes()),
                'compiled_source_sha256': digest(prepared[name].encode()), 'axioms': audits,
                'artifact_sha256': digest((library/f'{name}.olean').read_bytes())})
            save()
        receipt['new_theorem_audits'] = total
        certs = repo/PACKET/'certificates'
        py = [sys.executable, '-X', 'utf8', '-B']
        run('exact-certificate', py+[certs/'block_schema_verify.py', certs/'block_schema_certificates.json', '--self-test'], echo=True)
        run('optimized-certificate', [sys.executable, '-O', '-X', 'utf8', '-B', certs/'block_schema_verify.py', certs/'block_schema_certificates.json', '--self-test'], echo=True)
        generated = build/'regenerated-block-certificates.json'
        run('regenerate-certificate', py+[certs/'block_schema_certify.py', '--output', generated], echo=True)
        require(generated.read_bytes() == (certs/'block_schema_certificates.json').read_bytes(), 'certificate regeneration mismatch')
        run('repository-validation', py+['tools/validate.py'], echo=True)
        after = run('status-after', ['git', 'status', '--porcelain=v1'])
        require(after == before, 'checkout changed during replay')
        require(all(digest((repo/item['path']).read_bytes()) == item['sha256'] for item in receipt['inputs']), 'source changed during replay')
        receipt.update(complete=True, checkout_clean_after=True,
                       finished_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()))
        save()
        print(f'PASS: {len(ordered)} modules, {total} new theorem audits, exact certificate and repository gate.', flush=True)
    except BaseException as error:
        receipt.update(complete=False, error=str(error), error_type=type(error).__name__)
        save()
        raise


if __name__ == '__main__':
    main()
