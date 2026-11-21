"""Execute the frozen band packet and record actual clean-checkout evidence."""
import datetime
import hashlib
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

root = Path(sys.argv[1]).resolve()
receipt = Path(sys.argv[2]).resolve()
expected = sys.argv[3]
packet = root / 'research/band-return-20261121'
project = packet / 'lean'
runtime = Path('/workspace/scratch/957bb0caa6f2/lean-runtime/lean-4.34.1-linux/bin')
mathlib = Path('/workspace/scratch/957bb0caa6f2/lean-runtime/mathlib4')
pin = 'd13f23b723b8a846827a245b89c10fc7d3f11612'
modules = ['BandCertificates', 'BandDescent', 'BandSimulation', 'ReturnFourier',
           'MarkPhase', 'MarkFrequency', 'BandBridge', 'BandAudit']
env = dict(os.environ, PATH=str(runtime) + os.pathsep + os.environ['PATH'],
           MATHLIB_DIR=str(mathlib))


def stamp():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def git(*args, cwd=root):
    return subprocess.check_output(['git', *args], cwd=cwd, text=True).strip()


def state():
    tracked = git('ls-files').splitlines()
    if tracked != git('ls-tree', '-r', '--name-only', 'HEAD').splitlines():
        raise RuntimeError('Index is not the complete HEAD tree')
    if not all((root / path).is_file() for path in tracked):
        raise RuntimeError('A tracked file is absent')
    tree = git('rev-parse', 'HEAD^{tree}')
    if git('write-tree') != tree:
        raise RuntimeError('Index tree differs from HEAD')
    return {'head': git('rev-parse', 'HEAD'), 'tree': tree,
            'tracked_files': len(tracked),
            'status': git('status', '--porcelain', '--untracked-files=all')}


def sources():
    return {p: hashlib.sha256((root / p).read_bytes()).hexdigest()
            for p in git('ls-files', 'research/band-return-20261121',
                         'reports/2026-11-21-band-return').splitlines()}


def mathlib_state():
    head = git('rev-parse', 'HEAD', cwd=mathlib)
    clean = subprocess.run(['git', 'diff', '--quiet', 'HEAD', '--'],
                           cwd=mathlib).returncode == 0
    if head != pin or not clean:
        raise RuntimeError('Mathlib is not at the clean pinned revision')
    return {'head': head, 'tracked_changes': False}


record = {'started_utc': stamp(), 'commands': [], 'success': False,
          'scope': 'Actual complete band-packet Lean build and all-public-theorem axiom audit; full Collatz remains open.',
          'validator_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
try:
    record['before'] = state()
    if record['before']['head'] != expected or record['before']['status']:
        raise RuntimeError('Wrong head or dirty checkout')
    if (project / '.build').exists():
        raise RuntimeError('Fresh band output directory required')
    record['mathlib_before'] = mathlib_state()
    record['source_sha256'] = sources()
    public = []
    for source in sorted(project.glob('*.lean')):
        if source.name == 'BandAudit.lean':
            continue
        contents = source.read_text()
        namespaces = re.findall(r'^namespace\s+(\S+)\s*$', contents, re.M)
        if len(namespaces) != 1:
            raise RuntimeError('Unexpected namespace layout in ' + source.name)
        names = re.findall(r'^(?:theorem|lemma)\s+(\w+)', contents, re.M)
        public.extend(namespaces[0] + '.' + name for name in names)
    audited = re.findall(r'^#print axioms (\S+)',
                         (project / 'BandAudit.lean').read_text(), re.M)
    if len(public) != 81 or set(public) != set(audited) or len(audited) != 81:
        raise RuntimeError('Axiom-audit declaration coverage mismatch')
    record['public_theorems'] = sorted(public)
    commands = [[str(runtime / 'lean'), '--version'],
                ['bash', 'research/band-return-20261121/lean/build.sh', *modules]]
    for command in commands:
        print(json.dumps({'running': command}), flush=True)
        started = time.monotonic()
        result = subprocess.run(command, cwd=root, env=env,
                                capture_output=True, text=True)
        record['commands'].append({'argv': command, 'cwd': str(root),
                                   'exit_code': result.returncode,
                                   'stdout': result.stdout, 'stderr': result.stderr,
                                   'seconds': round(time.monotonic() - started, 3)})
        if result.returncode:
            raise RuntimeError('Command failed: ' + str(command))
    full_output = record['commands'][-1]['stdout']
    marker = 'Checking new BandAudit\n'
    if full_output.count(marker) != 1:
        raise RuntimeError('Cannot locate the standalone final axiom audit')
    # Individual research modules may also print focused audits. Only the
    # dedicated complete audit is used for exact declaration coverage here.
    output = full_output.split(marker, 1)[1]
    entries = re.findall(r"'([^']+)'\s+(?:depends on axioms:\s*\[([^\]]*)\]|does not depend on any axioms)",
                         output, re.S)
    dependencies = {}
    for name, body in entries:
        axioms = [a.strip() for a in body.split(',') if a.strip()]
        unexpected = set(axioms) - {'propext', 'Classical.choice', 'Quot.sound'}
        if unexpected:
            raise RuntimeError('Unexpected axioms for ' + name + ': ' + str(unexpected))
        if name in dependencies:
            raise RuntimeError('Duplicate axiom output for ' + name)
        dependencies[name] = axioms
    if set(dependencies) != set(audited):
        raise RuntimeError('Missing or unexpected axiom output: ' +
                           str(set(dependencies).symmetric_difference(audited)))
    record['axiom_dependencies'] = dependencies
    record['public_theorem_count'] = len(dependencies)
    record['after'] = state()
    record['mathlib_after'] = mathlib_state()
    if record['after'] != record['before'] or sources() != record['source_sha256']:
        raise RuntimeError('Checkout or source inputs changed during execution')
    if record['mathlib_after'] != record['mathlib_before']:
        raise RuntimeError('Mathlib inputs changed during execution')
    record['success'] = True
except Exception as error:
    record['error'] = str(error)
record['finished_utc'] = stamp()
receipt.parent.mkdir(parents=True, exist_ok=True)
receipt.write_text(json.dumps(record, indent=2, sort_keys=True) + '\n')
print(json.dumps({'success': record['success'], 'head': record.get('before', {}).get('head'),
                  'commands': len(record['commands']),
                  'public_theorems': record.get('public_theorem_count'),
                  'receipt': str(receipt), 'error': record.get('error')}), flush=True)
if not record['success']:
    raise SystemExit(1)
