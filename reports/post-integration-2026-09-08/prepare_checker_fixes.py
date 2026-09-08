#!/usr/bin/env python3
"""Prepare two exact-source typed-JSON guards. Only --apply modifies a checkout.

The self-test exercises isolated validation predicates and patch guards, not
any complete Collatz source verifier or its canonical corpus.
"""
from __future__ import annotations
import argparse
import ast
from hashlib import sha1, sha256
import json
from pathlib import Path

SOURCE = '912aec235fb2c5dbeac69a82454dd9c3d3a1e9fe'
TARGETS = (
 ('experiments/X-ATT-001-critical-tails/verify.py',
  '38588f83e8dd1a234e753bcd8fb8bd3f7d6e6902',
  "    require(report['payload'] == expected, 'semantic payload mismatch')",
  "    require(json.dumps(report['payload'], sort_keys=True, allow_nan=False) ==\n"
  "            json.dumps(expected, sort_keys=True, allow_nan=False),\n"
  "            'typed semantic payload mismatch')"),
 ('experiments/X-ATT-003-expanding-word-rank/verify.py',
  '760b5ade36c9927dfeea96cbbaafac08a99b07de',
  "    need(report['payload']==expected, 'complete reconstructed payload mismatch')",
  "    need(json.dumps(report['payload'], sort_keys=True, allow_nan=False) ==\n"
  "         json.dumps(expected, sort_keys=True, allow_nan=False),\n"
  "         'typed complete reconstructed payload mismatch')"),
)


def require(ok: bool, why: str) -> None:
    if not ok:
        raise ValueError(why)


def blob(raw: bytes) -> str:
    return sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()


def replace_exact(raw: bytes, expected: str, old: str, new: str) -> bytes:
    require(blob(raw) == expected, 'source fingerprint differs; re-review before changing it')
    require(raw.count(old.encode()) == 1, 'expected one exact validation predicate')
    changed = raw.replace(old.encode(), new.encode())
    ast.parse(changed.decode('utf-8'))
    require(changed != raw, 'no patch applied')
    return changed


def self_test() -> None:
    # Each mutation is resealed: the original predicates really accept it.
    original = {'count': 1, 'nested': [4096], 'open': False}
    mutations = [dict(count=True, nested=[4096], open=False),
                 dict(count=1.0, nested=[4096], open=False),
                 dict(count=1, nested=[4096.0], open=False),
                 dict(count=1, nested=[4096], open=0)]
    canonical = lambda p: json.dumps(p, sort_keys=True, allow_nan=False)
    seal = lambda p: sha256(canonical(p).encode()).hexdigest()
    for mutated in mutations:
        report = {'payload': mutated, 'sha256': seal(mutated)}
        require(report['sha256'] == seal(report['payload']) and mutated == original,
                'original predicate control')
        require(canonical(mutated) != canonical(original), 'typed guard missed mutation')
    # Execute the exact replacement expressions on isolated function fixtures.
    for _, _, old, new in TARGETS:
        helper = 'require' if 'require(' in old else 'need'
        raw = ("def validate(report, expected):\n"+old+'\n').encode()
        patched = replace_exact(raw, blob(raw), old, new)
        namespace = {'json': json, helper: require}
        exec(compile(patched, '<isolated-validation-fixture>', 'exec'), namespace)
        namespace['validate']({'payload': original}, original)
        for mutated in mutations:
            try:
                namespace['validate']({'payload': mutated}, original)
            except ValueError:
                pass
            else:
                raise ValueError('patched exact predicate accepted a typed mutation')
        try:
            replace_exact(raw, '0'*40, old, new)
        except ValueError:
            pass
        else:
            raise ValueError('wrong source accepted')
    print('PASS: 4 resealed type aliases; 8 exact-predicate rejections; 2 wrong-source refusals')
    print('Isolated fixtures only; no original corpus or source file was executed or patched.')


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path.cwd())
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--apply', action='store_true')
    group.add_argument('--self-test', action='store_true')
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return
    prepared = []
    for path, source_blob, old, new in TARGETS:
        source = args.root / path
        prepared.append((source, replace_exact(source.read_bytes(), source_blob, old, new)))
    # Check BOTH sources before any write. No canonical artifact is regenerated.
    for source, raw in prepared:
        if args.apply:
            source.write_bytes(raw)
        print(('APPLIED' if args.apply else 'CHECKED; NOT APPLIED'), source, 'new_blob='+blob(raw))
    print('Run both full source verifiers and their self-tests after application.')


if __name__ == '__main__':
    main()
