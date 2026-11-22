#!/usr/bin/env python3
"""Replay only the deep-closing packet in a clean complete checkout.

Requires existing Lean4.34.1 and the pinned built Mathlib checkout.
No downloads, inherited Lean modules, source ports or repository writes.
All generated sources, compiler artifacts, logs and the receipt are external.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import time

sys.dont_write_bytecode = True
PACKET = Path('research/deep-closing-20261122')
LEAN_VERSION = '4.34.1'
LEAN_COMMIT = '5045d0056413266e57c625dcd7c365b10e377c52'
MATHLIB_COMMIT = 'd13f23b723b8a846827a245b89c10fc7d3f11612'
ALLOW = {'propext', 'Classical.choice', 'Quot.sound'}
EXPECTED = {
    'OriginalSourceEntropy': ('CollatzOriginalEntropy', (
        'entropy_le_crossEntropy', 'push_nonneg', 'le_push', 'push_sum',
        'sum_push_mul', 'push_comp', 'entropy_push_le', 'geometric_mass',
        'codeProb_pos', 'codeProb_sum_le', 'log_codeProb',
        'finite_word_entropy_bound', 'gapPath_affine',
        'same_word_same_ternary_endpoint', 'endpoint_eq_code',
        'physical_endpoint_code', 'finite_original_source_entropy',
        'finite_original_source_entropy_of_mean', 'sliding_window_cost_le',
        'single_gap_log_identity', 'finite_gap_log_budget',
    )),
    'CycleWordEntropy': ('CollatzCycleWordEntropy', (
        'weighted_binomial_bound', 'cone_weight_bound', 'cycle_word_count_bound',
    )),
}


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def require(ok, message):
    if not ok:
        raise ValueError(message)


def uncomment(text):
    """Remove nested Lean comments while preserving line boundaries."""
    out, i, depth = [], 0, 0
    while i < len(text):
        if text.startswith('/-', i):
            depth += 1
            out.append('  ')
            i += 2
        elif depth and text.startswith('-/', i):
            depth -= 1
            out.append('  ')
            i += 2
        elif depth:
            out.append('\n' if text[i] == '\n' else ' ')
            i += 1
        elif text.startswith('--', i):
            end = text.find('\n', i)
            if end < 0:
                out.append(' ' * (len(text) - i))
                i = len(text)
            else:
                out.append(' ' * (end - i))
                i = end
        else:
            out.append(text[i])
            i += 1
    require(depth == 0, 'unterminated Lean comment')
    return ''.join(out)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--lean', type=Path, required=True)
    parser.add_argument('--mathlib', type=Path, required=True)
    parser.add_argument('--build-dir', type=Path, required=True)
    parser.add_argument('--repo', type=Path)
    args = parser.parse_args()
    repo = args.repo.resolve() if args.repo else Path(__file__).resolve().parents[2]
    lean = args.lean.resolve()
    mathlib = args.mathlib.resolve()
    build = args.build_dir.resolve()
    require((repo / PACKET / 'README.md').is_file(), 'complete packet missing')
    require(not build.is_relative_to(repo) and not build.is_relative_to(mathlib),
            'external build directory required')
    require(not build.exists() or (build.is_dir() and not any(build.iterdir())),
            'use an empty external build directory')
    source, library, logs = build / 'source', build / 'lib', build / 'logs'
    for path in (source, library, logs):
        path.mkdir(parents=True, exist_ok=True)
    receipt = {
        'schema': 'collatz-deep-closing-replay/v1', 'complete': False,
        'started_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
        'repository': str(repo), 'packet': str(PACKET),
        'inputs': [], 'commands': [], 'modules': [], 'review_bindings': [],
        'source_ports': False,
    }
    env = dict(os.environ)
    env['PYTHONDONTWRITEBYTECODE'] = '1'

    def save():
        (build / 'receipt.json').write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')

    def safe_repo_path(relative):
        path = repo / relative
        require(path.resolve().is_relative_to(repo), 'input escapes repository: ' + str(relative))
        require(path.is_file() and not path.is_symlink(), 'regular input file required: ' + str(relative))
        return path

    def record(path, expected=None):
        raw = path.read_bytes()
        item = {'path': str(path.relative_to(repo)), 'sha256': digest(raw)}
        if not any(x['path'] == item['path'] for x in receipt['inputs']):
            receipt['inputs'].append(item)
        require(expected is None or item['sha256'] == expected,
                'pinned input mismatch: ' + str(path))
        return raw

    def run(label, argv, cwd=repo, echo=False):
        item = {'label': label, 'argv': [str(x) for x in argv], 'cwd': str(cwd)}
        receipt['commands'].append(item)
        save()
        start = time.monotonic()
        process = subprocess.run(item['argv'], cwd=cwd, env=env,
                                 stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        log = logs / f'{len(receipt["commands"]):02d}-{label}.log'
        log.write_bytes(process.stdout)
        item.update(exit_code=process.returncode,
                    seconds=round(time.monotonic() - start, 3),
                    log=str(log), log_sha256=digest(process.stdout))
        save()
        output = process.stdout.decode('utf-8', errors='replace')
        if echo or process.returncode:
            print(output, end='', flush=True)
        require(process.returncode == 0, f'{label} failed; see {log}')
        return output

    try:
        receipt['head'] = run('head', ['git', 'rev-parse', 'HEAD']).strip()
        receipt['tree'] = run('tree', ['git', 'rev-parse', 'HEAD^{tree}']).strip()
        before = run('status-before', ['git', 'status', '--porcelain=v1'])
        require(not before.strip(), 'clean checkout required')
        tracked = [x for x in run('tracked-files', ['git', 'ls-files', '-z']).split('\0') if x]
        require(all((repo / x).exists() or (repo / x).is_symlink() for x in tracked),
                'incomplete checkout: tracked paths missing')
        receipt['tracked_files'] = len(tracked)
        tracked_set = set(tracked)
        version = run('lean-version', [lean, '--version']).strip()
        require('version ' + LEAN_VERSION in version and LEAN_COMMIT in version,
                'wrong Lean revision')
        receipt['lean_version'] = version
        mathlib_head = run('mathlib-head', ['git', 'rev-parse', 'HEAD'], mathlib).strip()
        require(mathlib_head == MATHLIB_COMMIT, 'wrong Mathlib revision')
        receipt['mathlib_commit'] = mathlib_head

        manifest = json.loads(record(safe_repo_path(PACKET / 'DEPENDENCIES.json')))
        require(manifest['lean_version'] == LEAN_VERSION and
                manifest['lean_commit'] == LEAN_COMMIT and
                manifest['mathlib_commit'] == MATHLIB_COMMIT,
                'runtime manifest mismatch')
        rows = manifest['new_modules']
        declared = {row['module']: row for row in rows}
        require(len(declared) == len(rows) and set(declared) == set(EXPECTED),
                'new module manifest set mismatch')
        supplied = {str(x.relative_to(repo)) for x in (repo / PACKET / 'lean').rglob('*.lean')}
        expected_paths = {str(PACKET / 'lean' / (name + '.lean')) for name in EXPECTED}
        require(supplied == expected_paths, 'unexpected Lean source set')
        prepared = {}
        for name, (namespace, expected_short) in EXPECTED.items():
            row = declared[name]
            relative = PACKET / 'lean' / (name + '.lean')
            require(row['path'] == str(relative), 'unexpected module path: ' + name)
            require(re.fullmatch(r'[0-9a-f]{64}', row['sha256']) is not None,
                    'invalid source digest: ' + name)
            raw = record(safe_repo_path(relative), row['sha256'])
            text = raw.decode('utf-8')
            clean = uncomment(text)
            require(not re.search(r'\b(?:sorry|admit|axiom|native_decide)\b', clean),
                    'admission, custom axiom or native proof in ' + name)
            imports = re.findall(r'^\s*(?:public\s+)?import\s+([^\n]+)', clean, re.M)
            require(imports, 'no explicit imports in ' + name)
            for line in imports:
                for imported in line.split():
                    require(imported.split('.')[0] in
                            {'Mathlib', 'Std', 'Init', 'Lean', 'Batteries', 'Aesop', 'Qq'},
                            'local/inherited import forbidden: ' + imported)
            commands = re.findall(r'^#print axioms (\S+)\s*$', clean, re.M)
            public = [decl for modifiers, decl in re.findall(
                r'^((?:(?:public|private|protected)\s+)*)(?:theorem|lemma)\s+(\w+)',
                clean, re.M) if 'private' not in modifiers.split()]
            require(len(public) == len(expected_short) and set(public) == set(expected_short),
                    'unexpected public theorem set in ' + name)
            require(len(commands) == len(expected_short) and
                    {x.rsplit('.', 1)[-1] for x in commands} == set(expected_short),
                    'incomplete or duplicate #print audit commands in ' + name)
            target = source / (name + '.lean')
            target.write_bytes(raw)
            require(digest(target.read_bytes()) == row['sha256'], 'source copy changed bytes')
            prepared[name] = raw

        reviews = json.loads(record(safe_repo_path(PACKET / 'REVIEW_BINDING.json')))
        require(isinstance(reviews.get('scope'), str) and bool(reviews['scope']),
                'review scope missing')
        require(isinstance(reviews.get('bindings'), list) and bool(reviews['bindings']),
                'review bindings missing')
        seen_bindings = set()
        for row in reviews['bindings']:
            pair = (row['review'], row['path'])
            require(pair not in seen_bindings, 'duplicate review binding')
            seen_bindings.add(pair)
            require(re.fullmatch(r'[0-9a-f]{64}', row['sha256']) is not None,
                    'invalid review target digest')
            review_raw = record(safe_repo_path(row['review']))
            record(safe_repo_path(row['path']), row['sha256'])
            require(row['review'] in tracked_set and row['path'] in tracked_set,
                    'review binding points to untracked content')
            receipt['review_bindings'].append(dict(row, review_sha256=digest(review_raw)))
        receipt['review_scope'] = reviews['scope']
        for path in sorted((repo / PACKET).rglob('*')):
            if path.is_file():
                relative = str(path.relative_to(repo))
                require(relative in tracked_set, 'untracked packet input: ' + relative)
                record(path)
        record(safe_repo_path(Path('tools/validate.py')))

        dependencies = [mathlib / '.lake/build/lib/lean']
        dependencies += sorted((mathlib / '.lake/packages').glob('*/.lake/build/lib/lean'))
        require((dependencies[0] / 'Mathlib/Data/Nat/Choose/Sum.olean').is_file() and
                (dependencies[0] / 'Mathlib/Analysis/SpecialFunctions/Log/Basic.olean').is_file(),
                'required Mathlib cache unavailable')
        env['LEAN_PATH'] = os.pathsep.join(str(x) for x in [library, *dependencies])
        receipt['lean_path'] = env['LEAN_PATH']
        total = 0
        for name, (namespace, expected_short) in EXPECTED.items():
            print('Checking ' + name + ' ...', flush=True)
            artifact = library / (name + '.olean')
            output = run(name, [lean, '-j1', '-DwarningAsError=true', '-o', artifact,
                                name + '.lean'], source, True)
            require(not re.search(r'\b(?:sorryAx|Lean\.ofReduceBool)\b', output),
                    'unfinished/native proof mechanism')
            audits = []
            for declaration, body in re.findall(r"'([^']+)' depends on axioms: \[([^\]]*)\]", output):
                axioms = {x.strip() for x in body.split(',') if x.strip()}
                require(axioms <= ALLOW, f'unexpected axioms for {declaration}: {axioms - ALLOW}')
                audits.append({'declaration': declaration, 'axioms': sorted(axioms)})
            for declaration in re.findall(r"'([^']+)' does not depend on any axioms", output):
                audits.append({'declaration': declaration, 'axioms': []})
            actual = [x['declaration'] for x in audits]
            expected_full = {namespace + '.' + x for x in expected_short}
            require(len(actual) == len(expected_full) and set(actual) == expected_full,
                    'compiled public axiom audit set differs in ' + name)
            total += len(audits)
            raw = prepared[name]
            receipt['modules'].append({
                'module': name, 'source': declared[name]['path'], 'new': True,
                'source_sha256': digest(raw), 'compiled_source_sha256': digest(raw),
                'axioms': audits, 'artifact_sha256': digest(artifact.read_bytes()),
            })
            save()
        require(total == 24, 'expected exactly 24 new public theorem audits')
        receipt['new_theorem_audits'] = total
        py = [sys.executable, '-X', 'utf8', '-B']
        certs = repo / PACKET / 'certificates'
        for mode, executable in [('normal', py), ('optimized', [sys.executable, '-O', '-X', 'utf8', '-B'])]:
            run(mode + '-arithmetic', executable + [certs / 'check_arithmetic.py'], echo=True)
            run(mode + '-cycle-law', executable + [certs / 'cycle_law_controls.py'], echo=True)
        run('repository-validation', py + ['tools/validate.py'], echo=True)
        after = run('status-after', ['git', 'status', '--porcelain=v1'])
        require(after == before, 'checkout changed during replay')
        require(run('head-after', ['git', 'rev-parse', 'HEAD']).strip() == receipt['head'],
                'repository HEAD changed during replay')
        require(run('tree-after', ['git', 'rev-parse', 'HEAD^{tree}']).strip() == receipt['tree'],
                'repository tree changed during replay')
        require(all(digest((repo / item['path']).read_bytes()) == item['sha256']
                    for item in receipt['inputs']), 'input changed during replay')
        require(all((source / (name + '.lean')).read_bytes() == raw
                    for name, raw in prepared.items()), 'external compiler source changed')
        receipt.update(complete=True, checkout_clean_after=True,
                       finished_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()))
        save()
        print('PASS: two independent modules, 24 public axiom audits, '
              'two exact controls in both Python modes, and repository gate.', flush=True)
    except BaseException as error:
        receipt.update(complete=False, error=str(error), error_type=type(error).__name__)
        save()
        raise


if __name__ == '__main__':
    main()
