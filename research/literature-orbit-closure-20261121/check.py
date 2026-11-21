#!/usr/bin/env python3
"""Reproduce the pinned literature/orbit-closure packet without downloads.

Supply Lean 4.34.1, a built mathlib checkout at the pinned commit, and an
external build directory. Sources remain unchanged. The receipt records exact
inputs, every invocation, compiler logs, axiom audits and repository validation.
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

PACKET = Path('research/literature-orbit-closure-20261121')
BASE_PACKET = Path('research/lean-band-coupling-20261121')
BASE_HEAD = '366dab89ee9548084ab9b5e4e90ff82abf287a20'
LEAN_VERSION = '4.34.1'
LEAN_COMMIT = '5045d0056413266e57c625dcd7c365b10e377c52'
MATHLIB_COMMIT = 'd13f23b723b8a846827a245b89c10fc7d3f11612'
BASE_PORT_SHA256 = '2d0a4df167bd6f5c920283584ae9c12370ea3621bc75fcfcf4bebbf5ebcbb785'
OFFSET_SHA256 = '6524d349cdb69cd86c3f8cbf54c6fb94b10c70f0f3e040d816e5fc6a5f00c9de'
FROZEN_HASHES = {
    'ShellCover': '76477e195c733e8b8c9fdf523d954d85375b3ac244ee0590127192743bffc88c',
    'ForwardSection': 'f134020b95f79c3b90cfe104c7d4234ee8d162c97acaa02c6aefc6ec86d19ae4',
    'SectionDynamics': '94c05e9cfc738b319acb52e9c6f07b0344dc87cb31ed4ed49cb2540fde51c9ac',
}
MODULES = [
    'ShellCover', 'ForwardSection', 'SectionDynamics', 'OffsetDescent',
    'HarmonicTransport', 'ClockAbsorption', 'BandAbsorption', 'FiniteResolvent',
    'ExplicitSeed', 'ActualSurvivorMass', 'ExplicitClosure',
    'PullbackArithmetic', 'WildLift', 'HalfSourceMerge', 'LongDiamondErasure',
    'MarkedErasure', 'NewBandFamily', 'RayCertificates', 'AL27Certificates', 'Audit',
]
ALLOWED_AXIOMS = {'propext', 'Classical.choice', 'Quot.sound'}


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def locate_repo(explicit: Path | None) -> Path:
    if explicit is not None:
        candidates = [explicit.resolve()]
    else:
        here, cwd = Path(__file__).resolve(), Path.cwd().resolve()
        candidates = [here.parent, *here.parents, cwd, *cwd.parents]
    for root in candidates:
        if (root / BASE_PACKET / 'check.py').is_file() and (root / PACKET).is_dir():
            return root
    raise ValueError('Cannot locate both repository packets; supply --repo ROOT')


def audits_from(text: str) -> list[dict]:
    audits = []
    for theorem, body in re.findall(r"'([^']+)' depends on axioms: \[([^\]]*)\]", text):
        names = {a.strip() for a in body.split(',') if a.strip()}
        if not names <= ALLOWED_AXIOMS:
            raise ValueError(f'Unexpected axioms in {theorem}: {sorted(names - ALLOWED_AXIOMS)}')
        audits.append({'theorem': theorem, 'axioms': sorted(names)})
    for theorem in re.findall(r"'([^']+)' does not depend on any axioms", text):
        audits.append({'theorem': theorem, 'axioms': []})
    if re.search(r'\b(sorryAx|Lean\.ofReduceBool)\b', text):
        raise ValueError('Unfinished or native-evaluation axiom in compiler output')
    return audits


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--lean', required=True, type=Path)
    parser.add_argument('--mathlib', required=True, type=Path)
    parser.add_argument('--build-dir', required=True, type=Path)
    parser.add_argument('--repo', type=Path)
    parser.add_argument('--prepare-only', action='store_true',
                        help='Check inputs and prepare external sources; claim no compilation')
    args = parser.parse_args()
    repo = locate_repo(args.repo)
    packet, base = repo / PACKET, repo / BASE_PACKET
    mathlib, lean, build = args.mathlib.resolve(), args.lean.resolve(), args.build_dir.resolve()
    if build.is_relative_to(repo) or build.is_relative_to(mathlib):
        parser.error('--build-dir must be outside the repository and mathlib checkout')
    generated, output, logs = build / 'source', build / 'lib', build / 'logs'
    for directory in (generated, output, logs):
        directory.mkdir(parents=True, exist_ok=True)
    unexpected = {p.stem for p in output.glob('*.olean')} - set(MODULES)
    if unexpected:
        raise ValueError(f'Build directory has unlisted Lean modules: {sorted(unexpected)}')
    receipt = {
        'schema': 'literature-orbit-closure-check-v1', 'complete': False,
        'prepared_only': args.prepare_only, 'repository': str(repo),
        'packet': str(PACKET), 'base_head': BASE_HEAD, 'build_directory': str(build),
        'started_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
        'inputs': [], 'modules': [], 'invocations': [],
        'axiom_allowlist': sorted(ALLOWED_AXIOMS),
    }

    def save() -> None:
        (build / 'receipt.json').write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')

    def input_record(path: Path, expected: str | None = None) -> bytes:
        raw = path.read_bytes()
        actual = sha(raw)
        receipt['inputs'].append({'path': str(path.relative_to(repo)), 'sha256': actual})
        if expected is not None and actual != expected:
            raise ValueError(f'Pinned input hash mismatch: {path}')
        return raw

    env = dict(os.environ)
    env['PYTHONDONTWRITEBYTECODE'] = '1'

    def run(label: str, command: list[str], cwd: Path, echo: bool = False) -> str:
        record = {'label': label, 'command': command, 'cwd': str(cwd)}
        receipt['invocations'].append(record)
        save()
        start = time.monotonic()
        result = subprocess.run(command, cwd=cwd, env=env, text=True, encoding='utf-8',
                                errors='replace', stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        log = logs / f'{len(receipt["invocations"]):02d}-{label}.log'
        log.write_text(result.stdout, encoding='utf-8')
        record.update(exit_code=result.returncode,
                      elapsed_seconds=round(time.monotonic() - start, 3),
                      output_sha256=sha(result.stdout.encode()), log=str(log))
        save()
        if echo or result.returncode:
            print(result.stdout, end='', flush=True)
        if result.returncode:
            raise RuntimeError(f'{label} failed with exit code {result.returncode}; see {log}')
        return result.stdout

    try:
        version = run('lean-version', [str(lean), '--version'], repo).strip()
        if not re.search(r'\bversion ' + re.escape(LEAN_VERSION) + r'\b', version) or LEAN_COMMIT not in version:
            raise ValueError(f'Wrong Lean version/commit: {version}')
        receipt['lean_version'] = version
        mathlib_head = run('mathlib-head', ['git', 'rev-parse', 'HEAD'], mathlib).strip()
        if mathlib_head != MATHLIB_COMMIT:
            raise ValueError(f'Wrong mathlib commit: {mathlib_head}')
        receipt['mathlib_commit'] = mathlib_head
        receipt['repository_head'] = run('repository-head', ['git', 'rev-parse', 'HEAD'], repo).strip()
        receipt['repository_tree'] = run('repository-tree', ['git', 'rev-parse', 'HEAD^{tree}'], repo).strip()
        tracked = run('tracked-files', ['git', 'ls-files', '-z'], repo).split('\0')
        tracked = [path for path in tracked if path]
        missing = [path for path in tracked if not (repo / path).exists() and
                   not (repo / path).is_symlink()]
        receipt['tracked_file_count'] = len(tracked)
        if missing:
            raise ValueError(f'Checkout is incomplete; missing tracked files: {missing[:8]}')
        initial_status = run('status-before', ['git', 'status', '--porcelain=v1'], repo)
        receipt['checkout_clean_before'] = not initial_status.strip()
        if initial_status.strip() and not args.prepare_only:
            raise ValueError('Full verification requires a clean complete checkout')

        pins = json.loads(input_record(packet / 'source-pins.json'))
        if pins.get('mathlib_commit') != MATHLIB_COMMIT or pins.get('base_head') != BASE_HEAD:
            raise ValueError('Packet source pins disagree with the checker')
        input_record(base / 'source-pins.json')
        input_record(base / 'check.py', BASE_PORT_SHA256)
        spec = importlib.util.spec_from_file_location('_pinned_pr184_check', base / 'check.py')
        if spec is None or spec.loader is None:
            raise ValueError('Cannot load the pinned module-format port')
        port_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(port_module)

        deps = [mathlib / '.lake/build/lib/lean']
        deps += sorted((mathlib / '.lake/packages').glob('*/.lake/build/lib/lean'))
        required_olean = deps[0] / 'Mathlib/Analysis/SpecialFunctions/Log/Base.olean'
        if not required_olean.is_file():
            raise ValueError('The supplied pinned mathlib cache is not built')
        env['LEAN_PATH'] = os.pathsep.join(str(p) for p in [output, *deps])
        receipt['lean_path'] = env['LEAN_PATH']
        patch = []
        for name in MODULES:
            inherited = name in FROZEN_HASHES or name == 'OffsetDescent'
            path = (base if inherited else packet) / 'lean' / f'{name}.lean'
            expected = FROZEN_HASHES.get(name, OFFSET_SHA256 if name == 'OffsetDescent' else None)
            raw = input_record(path, expected).decode('utf-8')
            prepared = port_module.module_port(name, raw) if name in FROZEN_HASHES else raw
            (generated / f'{name}.lean').write_text(prepared, encoding='utf-8')
            patch.extend(difflib.unified_diff(raw.splitlines(True), prepared.splitlines(True),
                         fromfile=str(path.relative_to(repo)), tofile=f'generated/{name}.lean', n=0))
            receipt['modules'].append({'module': name, 'source': str(path.relative_to(repo)),
                                       'source_sha256': sha(raw.encode()),
                                       'compiled_source_sha256': sha(prepared.encode())})
        (build / 'module-port.patch').write_text(''.join(patch), encoding='utf-8')
        receipt['module_port_sha256'] = sha(''.join(patch).encode())

        certificates = packet / 'certificates'
        for name in ('al27_certificate.json', 'guided_cover.py', 'package_al27.py',
                     'verify_al27.py', 'generate_al27_lean.py'):
            input_record(certificates / name)
        input_record(repo / 'tools/validate.py')
        if args.prepare_only:
            receipt['prepared_inputs'] = True
            save()
            print(f'Prepared {len(MODULES)} modules. No compilation or validation claimed.')
            return

        for record in receipt['modules']:
            name = record['module']
            print(f'Checking {name} ...', flush=True)
            command = [str(lean), '-j1', '-DwarningAsError=true', '-o',
                       str(output / f'{name}.olean'), f'{name}.lean']
            text = run(name, command, generated, echo=True)
            record['axiom_audits'] = audits_from(text)
            record['exit_code'] = 0
            if name == 'Audit':
                expected = re.findall(r'^#print axioms (\S+)', (generated / 'Audit.lean').read_text(), re.M)
                actual = [a['theorem'] for a in record['axiom_audits']]
                if sorted(actual) != sorted(expected) or len(set(actual)) != len(actual):
                    raise ValueError('Final Audit did not report each requested theorem exactly once')
                receipt['final_public_theorem_audit_count'] = len(actual)
            save()

        python = [sys.executable, '-X', 'utf8', '-B']
        run('verify-al27', python + [str(certificates / 'verify_al27.py')], repo, echo=True)
        run('regenerate-al27', python + [str(certificates / 'generate_al27_lean.py'),
            '--check', '--output', str(packet / 'lean/AL27Certificates.lean')], repo, echo=True)
        run('repository-validation', python + ['tools/validate.py'], repo, echo=True)
        final_status = run('status-after', ['git', 'status', '--porcelain=v1'], repo)
        receipt['checkout_clean_after'] = not final_status.strip()
        if final_status != initial_status:
            raise ValueError('Checkout status changed during verification')
        receipt['axiom_audit_count'] = sum(len(m['axiom_audits']) for m in receipt['modules'])
        receipt['complete'] = True
        receipt['completed_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
        save()
        print(f'All {len(MODULES)} modules, both certificate checks, and repository validation passed.')
        print(f'Receipt: {build / "receipt.json"}')
    except BaseException as error:
        receipt['error'] = str(error)
        receipt['error_type'] = type(error).__name__
        receipt['complete'] = False
        save()
        raise


if __name__ == '__main__':
    main()
