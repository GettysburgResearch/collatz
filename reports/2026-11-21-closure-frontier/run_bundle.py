#!/usr/bin/env python3
"""Replay the frozen closure-frontier packet in a clean complete checkout."""
from pathlib import Path
import argparse
import datetime
import hashlib
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
REPORTS = 'reports/2026-11-21-closure-frontier'
SCIENCE = 'research/closure-frontier-20261121'
PROGRAMS = [
    (SCIENCE+'/five_return_compiler.py', REPORTS+'/five_return_report.json'),
    (REPORTS+'/five_independent_check.py', REPORTS+'/five_independent_report.json'),
    (SCIENCE+'/negative_template_compiler.py', REPORTS+'/negative_template_report.json'),
    (REPORTS+'/review_negative_templates.py', REPORTS+'/review_negative_templates_report.json'),
    (SCIENCE+'/check_finite_conductor.py', REPORTS+'/finite-conductor-report.json'),
    (REPORTS+'/independent_quotient_review.py', REPORTS+'/independent-quotient-report.json'),
    (SCIENCE+'/check_ternary_stationary.py', REPORTS+'/ternary-stationary-report.json'),
    (REPORTS+'/review_ternary_independent.py', REPORTS+'/ternary-independent-report.json'),
]


def require(value, message):
    if not value:
        raise RuntimeError(message)


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT, text=True).strip()


def state():
    tracked = subprocess.check_output(['git','ls-files','-z'],cwd=ROOT).split(b'\0')
    tracked = [p.decode() for p in tracked if p]
    tree_paths = subprocess.check_output(['git','ls-tree','-r','--name-only','-z','HEAD'],cwd=ROOT).split(b'\0')
    tree_paths = [p.decode() for p in tree_paths if p]
    require(sorted(tracked) == sorted(tree_paths), 'index differs from complete commit tree')
    require(all((ROOT/p).exists() for p in tracked), 'tracked file missing from checkout')
    return {'head':git('rev-parse','HEAD'), 'tree':git('rev-parse','HEAD^{tree}'),
            'status':git('status','--porcelain','--untracked-files=all'),
            'tracked_files':len(tracked)}


def stamp():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--receipt', required=True)
    parser.add_argument('--manifest-only',action='store_true')
    parser.add_argument('--expect-head')
    args = parser.parse_args()
    destination = Path(args.receipt).resolve()
    require(not destination.is_relative_to(ROOT), 'receipt must be outside checkout')
    record = {'started_utc':stamp(),'manifest_only':args.manifest_only,'runs':[],'status':'FAIL'}
    try:
        before = state()
        record['before'] = before
        require(before['status'] == '', 'checkout is dirty')
        if args.expect_head:
            require(before['head'] == args.expect_head, 'unexpected commit')
        manifest_bytes = (ROOT/REPORTS/'CONTENT_SHA256.json').read_bytes()
        manifest = json.loads(manifest_bytes)
        for path, expected in manifest['files'].items():
            require(sha((ROOT/path).read_bytes()) == expected, 'manifest mismatch: '+path)
        record['manifest_sha256'] = sha(manifest_bytes)
        record['manifest_entries'] = len(manifest['files'])
        if not args.manifest_only:
            for program, reference in PROGRAMS:
                expected = (ROOT/reference).read_bytes()
                for optimized in (False, True):
                    command = [sys.executable,'-X','utf8','-B']
                    if optimized:
                        command.append('-O')
                    command.append(program)
                    started = stamp()
                    run = subprocess.run(command,cwd=ROOT,capture_output=True)
                    entry = {'command':command,'started_utc':started,'finished_utc':stamp(),
                             'exit_code':run.returncode,'stdout_sha256':sha(run.stdout),
                             'reference':reference,'matches_frozen_report':run.stdout == expected,
                             'stderr':run.stderr.decode('utf-8',errors='replace')}
                    record['runs'].append(entry)
                    require(run.returncode == 0, 'program failed: '+program)
                    require(run.stdout == expected, 'frozen report differs: '+program)
        after = state()
        record['after'] = after
        require(after == before, 'checkout changed during execution')
        record['status'] = 'PASS'
    except Exception as error:
        record['error'] = str(error)
    finally:
        record['finished_utc'] = stamp()
        destination.parent.mkdir(parents=True,exist_ok=True)
        destination.write_text(json.dumps(record,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps({'status':record['status'],'head':record.get('before',{}).get('head'),
                      'manifest_entries':record.get('manifest_entries'),
                      'executions':len(record['runs']),'receipt':str(destination)},sort_keys=True))
    if record['status'] != 'PASS':
        raise SystemExit(record.get('error','bundle failed'))


if __name__ == '__main__':
    main()
