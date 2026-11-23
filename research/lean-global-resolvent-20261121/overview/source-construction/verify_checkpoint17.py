#!/usr/bin/env python3
"""Replay only the new certificate module and checkpoint-17 exact controls."""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(argv: list[str], cwd: Path) -> dict:
    result = subprocess.run(argv, cwd=cwd, capture_output=True, text=True)
    record = dict(argv=argv, cwd=str(cwd), exit_code=result.returncode,
                  stdout=result.stdout, stderr=result.stderr)
    if result.returncode:
        raise RuntimeError(json.dumps(record, indent=2))
    return record


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--lean', type=Path, required=True)
    parser.add_argument('--mathlib', type=Path, required=True)
    parser.add_argument('--receipt', type=Path, required=True)
    args = parser.parse_args()
    packet = Path(__file__).resolve().parent
    repo = Path(run(['git', 'rev-parse', '--show-toplevel'], packet)['stdout'].strip())
    report = repo / 'reports/2026-11-23-source-construction'
    receipt_path = args.receipt.resolve()
    if receipt_path.is_relative_to(repo):
        raise ValueError('execution receipt must be outside the checkout')

    started = dt.datetime.now(dt.timezone.utc).isoformat()
    manifest_path = report / 'manifest.json'
    manifest = json.loads(manifest_path.read_text())
    for item in manifest['files']:
        path = repo / item['path']
        if digest(path) != item['sha256'] or path.stat().st_size != item['bytes']:
            raise ValueError('manifest mismatch: ' + item['path'])

    # Source pins are metadata rather than an invitation to rebuild old code.
    # When the frozen objects are present, also compare their actual bytes.
    source_checks = []
    sources = json.loads((packet / 'SOURCES.json').read_text())
    for lane in sources['lanes']:
        for item in lane['repository_sources']:
            spec = item['commit'] + ':' + item['path']
            exists = subprocess.run(['git', 'cat-file', '-e', spec], cwd=repo,
                                    capture_output=True).returncode == 0
            if exists:
                raw = subprocess.check_output(['git', 'show', spec], cwd=repo)
                blob = run(['git', 'rev-parse', spec], repo)['stdout'].strip()
                if hashlib.sha256(raw).hexdigest() != item['sha256'] or blob != item['git_blob']:
                    raise ValueError('upstream source mismatch: ' + spec)
            source_checks.append(dict(lane=lane['lane'], commit=item['commit'],
                                      path=item['path'], object_present=exists,
                                      verified=exists))

    with tempfile.TemporaryDirectory(prefix='collatz-checkpoint17-') as directory:
        nested_receipt = Path(directory) / 'rigidity.json'
        nested_command = run([
            sys.executable, '-X', 'utf8', '-B', str(packet / 'verify_candidate_rigidity.py'),
            '--lean', str(args.lean.resolve()), '--mathlib', str(args.mathlib.resolve()),
            '--receipt', str(nested_receipt)], packet)
        rigidity = json.loads(nested_receipt.read_text())

    controls = []
    for name, expected_file in [
        ('check_optimal_ray.py', 'optimizer-controls.json'),
        ('check_cycle_product_control.py', 'cycle-controls.json'),
    ]:
        normal = run([sys.executable, '-X', 'utf8', '-B', str(packet / name)], packet)
        optimized = run([sys.executable, '-X', 'utf8', '-B', '-O', str(packet / name)], packet)
        if normal['stdout'] != optimized['stdout']:
            raise ValueError('optimized replay mismatch: ' + name)
        expected = json.loads((report / expected_file).read_text())
        if json.loads(normal['stdout']) != expected:
            raise ValueError('frozen control mismatch: ' + name)
        controls.append(dict(file=name, source_sha256=digest(packet / name),
                             normal=normal, optimized=optimized, identical_output=True))

    frozen_controls = {
        'check_exact_rigidity.py': 'rigidity-controls.json',
        'check_carry_construction.py': 'construction-controls.json',
    }
    for item in rigidity['controls']:
        frozen = json.loads((report / frozen_controls[item['file']]).read_text())
        if item['result'] != frozen:
            raise ValueError('frozen rigidity/construction control mismatch: ' + item['file'])

    # The independent carry-review checker is deliberately small and unrelated
    # to the author implementation. It is also preserved and replayed exactly.
    review_checker = report / 'check_carry_written_review.py'
    review_source = ['--source', str(packet / 'CARRY_CONSTRUCTION_ATTACK.md')]
    review_normal = run([sys.executable, '-X', 'utf8', '-B', str(review_checker)] + review_source, report)
    review_optimized = run([sys.executable, '-X', 'utf8', '-B', '-O', str(review_checker)] + review_source, report)
    if review_normal['stdout'] != review_optimized['stdout']:
        raise ValueError('independent written-control optimization mismatch')
    if json.loads(review_normal['stdout']) != json.loads((report / 'carry-written-review-controls.json').read_text()):
        raise ValueError('independent written-control receipt mismatch')

    result = dict(
        schema='collatz-checkpoint17-scoped-replay/v1',
        started_utc=started, finished_utc=dt.datetime.now(dt.timezone.utc).isoformat(),
        success=True, python=sys.version,
        scope='Fresh build of the new exact-candidate module and its two unchanged dependencies; complete new-declaration audit; four new exact checkers and independent carry-review controls. No historical research corpus replay.',
        git_head_at_execution=run(['git', 'rev-parse', 'HEAD'], repo)['stdout'].strip(),
        git_status_at_execution=run(['git', 'status', '--short'], repo)['stdout'],
        manifest_sha256=digest(manifest_path), manifest_entries=len(manifest['files']),
        source_checks=source_checks, rigidity_command=nested_command, rigidity=rigidity,
        other_controls=controls,
        independent_written_controls=dict(normal=review_normal, optimized=review_optimized,
                                          identical_output=True),
    )
    receipt_path.parent.mkdir(parents=True, exist_ok=True)
    receipt_path.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(dict(success=True, declarations=len(rigidity['declarations']),
                          axiom_union=rigidity['axiom_union'], new_checkers=4,
                          independent_written_checker=True,
                          upstream_entries=len(source_checks), receipt=str(receipt_path)), indent=2))


if __name__ == '__main__':
    main()
