#!/usr/bin/env python3
"""Check the frozen review integration's identities and structure, not mathematics."""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
import tempfile
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
SHA = re.compile(r'[0-9a-f]{40}\Z')
LINK = re.compile(r'(?<!!)\[[^\]]*\]\(([^)]+)\)')
OLD_IDS = set('IC-EXTRACT-001 IC-GHOST-001 IC-PERIODIC-001 IC-SC-001 IC-AUT-001 IC-RIG-001 IC-REF-001 IC-REP-001 RD-SC-001 RD-FC-001 RD-BRIDGE-001'.split())
NEW_IDS = {'IR-MASS-001', 'IR-RENEWAL-001', 'IR-MERGING-001', 'IR-ORBIT-001'}
CODE_PINS = {
    'experiments/X-ASTRA-003-run-renewal/verify.py': '4d330c3c59d468538e38f7ecbbecaf8697115b10',
    'experiments/X-ASTRA3-002-three-routes/verify.py': 'c9f2ee8ead22820938aaf9f7b7ab6b2671c67634',
    'research/external/mazur-2026/check_fixed_height_forward.py': '77e4494d703c9c70d66e2695b8fcf1cc2dff2292',
}
CURATED = [
    'README.md', 'research/README.md', 'claims/README.md', 'CONTRIBUTING.md',
    'docs/RESEARCH_MAP.md', 'docs/INTEGRATION_PRACTICE.md', 'docs/REPLAY_POLICY.md',
    'docs/PUBLIC_RELEASE_GATES.md', 'archive/README.md',
    'archive/research-2026-09-05/README.md', 'research/open-obligations/README.md',
    'research/astra-critical-mass/README.md', 'research/astra-three-routes/README.md',
    'research/external/mazur-2026/README.md',
    'experiments/X-ASTRA3-005-spectrum-switch/README.md',
    'reports/prepublic-2026-09-05/integration/README.md',
]


class CheckError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise CheckError(message)


def blob_sha(raw: bytes) -> str:
    return hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()


def tree_sha(directory: Path) -> str:
    # Git sorts directory names as if suffixed with '/'. Ignore generated caches.
    children = [p for p in directory.iterdir()
                if p.name != '__pycache__' and p.suffix not in ('.pyc', '.pyo')]
    children.sort(key=lambda p: os.fsencode(p.name) + (b'/' if p.is_dir() and not p.is_symlink() else b''))
    raw = bytearray()
    for child in children:
        if child.is_symlink():
            mode, sha = b'120000', blob_sha(os.fsencode(os.readlink(child)))
        elif child.is_dir():
            mode, sha = b'40000', tree_sha(child)
        else:
            mode = b'100755' if child.stat().st_mode & 0o100 else b'100644'
            sha = blob_sha(child.read_bytes())
        raw.extend(mode + b' ' + os.fsencode(child.name) + b'\0' + bytes.fromhex(sha))
    return hashlib.sha1(b'tree ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()


def safe_path(root: Path, relative: str) -> Path:
    p = PurePosixPath(relative)
    require(not p.is_absolute() and '..' not in p.parts, f'invalid repository path: {relative}')
    result = (root / relative).resolve()
    require(result.is_relative_to(root.resolve()), f'path escapes checkout: {relative}')
    return result


def namespaces_valid(namespaces: dict, heads: dict) -> None:
    seen = set()
    for name, item in namespaces.items():
        require(bool(SHA.fullmatch(item.get('commit', ''))), f'{name}: bad commit')
        require(heads.get(str(item.get('pr'))) == item['commit'], f'{name}: wrong review head')
        safe_path(Path('/checkout'), item['path'])
        identity = (item['pr'], item['commit'], item['path'])
        require(identity not in seen, f'{name}: collapsed source namespace')
        seen.add(identity)


def resolve_source(reference: str, namespaces: dict) -> tuple:
    name, separator, claim = reference.partition(':')
    require(bool(separator and claim and name in namespaces), 'unknown or ambiguous source namespace')
    item = namespaces[name]
    return item['pr'], item['commit'], item['path'], claim


def assemblies_valid(rows: list) -> None:
    require(len(rows) == 4 and {r['id'] for r in rows} == NEW_IDS, 'assembly identities changed')
    for row in rows:
        require(row.get('mathematical_status') == 'source-qualified', 'unreviewed assembly promoted')
        require(row.get('promotion_state') == 'accepted_reference_record', 'assembly promotion changed')
        require(row.get('integrated_statement_status') == 'pending_narrow_review', 'synthesis flag lost')


def local_link(root: Path, source: Path, target: str) -> bool:
    target = target.strip().split('#', 1)[0]
    if not target or re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', target):
        return False
    target = unquote(target)
    destination = (source.parent / target).resolve()
    require(destination.is_relative_to(root.resolve()), f'{source}: escaping link {target}')
    require(destination.exists(), f'{source}: missing link {target}')
    return True


def check(root: Path) -> None:
    manifest = json.loads((root / 'claims/reviewed-2026-09-05.json').read_text())
    aliases = json.loads((root / 'claims/aliases.json').read_text())
    heads = manifest['source_heads']
    require(set(heads) == {'87', '88', '90', '91', '92'}, 'source scope changed')
    require(all(SHA.fullmatch(s) for s in heads.values()), 'invalid source SHA')
    require(manifest.get('canonical_registry_changed') is False, 'canonical promotion requires new review')
    require(manifest.get('publication_gate') == 'not_cleared_by_integration', 'launch gate silently cleared')
    require(set(aliases['canonical_aliases']) == OLD_IDS, 'old aliases changed')
    assemblies_valid(manifest['assemblies'])
    namespaces = aliases['source_namespaces']
    require(len(namespaces) == 9, 'expected nine file-specific namespaces')
    namespaces_valid(namespaces, heads)
    for item in namespaces.values():
        require(safe_path(root, item['path']).is_file(), f'missing source {item["path"]}')
    require(resolve_source('CM-CLOCK:T-ASTRA-030', namespaces) != resolve_source('CM-FAN:T-ASTRA-030', namespaces), 'clock/fan collision')
    require(resolve_source('A3-BUDGET-MERGING:T-A3-1051', namespaces) != resolve_source('A3-SPECTRUM-PLATEAUS:T-A3-1051', namespaces), 'fifth-pass collision')
    for item in aliases['artifact_collisions']:
        require(len(set(item['paths'])) == 2, 'artifact paths collapsed')
        for path in item['paths']:
            require(safe_path(root, path).is_file(), f'missing artifact {path}')
    pins = dict(manifest['byte_pins'])
    trees = dict(manifest['untouched_source_subtrees'])
    reviewed_prs = [pr for review in manifest['reviews'] for pr in review['source_prs']]
    require(sorted(reviewed_prs) == sorted(map(int, heads)), 'source review assignments incomplete or overlapping')
    require({r['role'] for r in manifest['reviews']} == {'A', 'B'}, 'review coverage incomplete')
    for review in manifest['reviews']:
        require(bool(SHA.fullmatch(review['commit'])), 'invalid review SHA')
        pins[review['matrix']] = review['matrix_blob']
        trees[review['directory']] = review['directory_tree']
    pins.update(CODE_PINS)
    for path, expected in pins.items():
        require(bool(SHA.fullmatch(expected)), f'bad blob pin: {path}')
        require(blob_sha(safe_path(root, path).read_bytes()) == expected, f'blob changed: {path}')
    for path, expected in trees.items():
        require(tree_sha(safe_path(root, path)) == expected, f'preserved subtree changed: {path}')
    for path in list(CODE_PINS)[:2]:
        result = subprocess.run([sys.executable, '-O', '-B', str(root / path), '--help'],
                                capture_output=True, text=True, timeout=10)
        require(result.returncode != 0 and 'optimized Python is unsupported' in result.stderr,
                f'optimized legacy verifier did not fail closed: {path}')
    sibling = (root / 'experiments/X-ASTRA3-005-spectrum-switch/README.md').read_text()
    require('astra-three-routes/pass5-spectrum-switch/README.md' in sibling, 'wrong spectrum sibling link')
    require('astra-three-routes/pass5/README.md' not in sibling, 'budget sibling mislabeled as spectrum')
    paths = {root / p for p in CURATED}
    paths.update((root / 'research/integrated').rglob('*.md'))
    links = 0
    for path in sorted(paths):
        text = path.read_text(encoding='utf-8')
        require('reports-link-placeholder' not in text, f'unresolved link marker: {path}')
        for target in LINK.findall(text):
            links += local_link(root, path, target)
    print(f'OK: 4 qualified assemblies, 9 namespaces, {len(pins)} exact blob pins, {len(trees)} exact subtree pins, {links} local links, 2 optimized guards; no mathematical verification')


def self_test() -> None:
    cases = 0
    def rejected(action) -> None:
        nonlocal cases
        try:
            action()
        except CheckError:
            cases += 1
            return
        raise CheckError('invalid fixture was accepted')
    namespaces = {'left': {'pr': 90, 'commit': 'a' * 40, 'path': 'one.md'},
                  'right': {'pr': 90, 'commit': 'a' * 40, 'path': 'two.md'}}
    heads = {'90': 'a' * 40}
    namespaces_valid(namespaces, heads)
    require(resolve_source('left:T-001', namespaces) != resolve_source('right:T-001', namespaces), 'explicit identities collapsed')
    rejected(lambda: resolve_source('PR90:T-001', namespaces))
    changed = copy.deepcopy(namespaces); changed['right']['path'] = 'one.md'
    rejected(lambda: namespaces_valid(changed, heads))
    changed = copy.deepcopy(namespaces); changed['right']['commit'] = 'b' * 40
    rejected(lambda: namespaces_valid(changed, heads))
    rejected(lambda: safe_path(Path('/checkout'), '../outside'))
    rows = [{'id': name, 'mathematical_status': 'source-qualified', 'promotion_state': 'accepted_reference_record',
             'integrated_statement_status': 'pending_narrow_review'} for name in NEW_IDS]
    assemblies_valid(rows)
    changed_rows = copy.deepcopy(rows); changed_rows[0]['mathematical_status'] = 'verified'
    rejected(lambda: assemblies_valid(changed_rows))
    changed_rows = copy.deepcopy(rows); changed_rows[0]['integrated_statement_status'] = 'verified'
    rejected(lambda: assemblies_valid(changed_rows))
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory); source = root / 'doc.md'; source.write_text('test')
        require(local_link(root, source, 'doc.md'), 'valid local link rejected')
        before = tree_sha(root); source.write_text('changed')
        require(tree_sha(root) != before, 'tree pin missed changed proof bytes')
        rejected(lambda: local_link(root, source, 'missing.md'))
        rejected(lambda: local_link(root, source, '../outside.md'))
    require(blob_sha(b'hello\n') == 'ce013625030ba8dba906f756967f9e9ca394464a', 'Git blob hashing failed')
    print(f'SELF-TEST PASS: {cases} invalid fixtures rejected; no repository scan or mathematical verification performed')


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--self-test', action='store_true')
    args = parser.parse_args()
    try:
        if args.self_test:
            self_test()
        else:
            check(args.root.resolve())
    except (CheckError, OSError, ValueError, KeyError, TypeError, subprocess.SubprocessError) as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
