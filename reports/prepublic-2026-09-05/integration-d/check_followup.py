#!/usr/bin/env python3
"""Scoped D-edition checks only; NOT a full repository structural validator.

Authenticates seven active reading surfaces and their seven archived originals,
checks correction markers and small exact edge-case regressions. No source
checker is imported. No command writes data. Explicit failures survive -O.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from copy import deepcopy
from fractions import Fraction as F
from pathlib import Path

BASE = 'cd1b3689e8d37fc4232945072e2faf6bd5ee47bd'
REVIEW = '1c7744bcb9ded9336036919ffc7a19b5576ea58e'
MANIFEST = 'claims/followups/reviewer-d-2026-09-05.json'
ERRATA = 'research/integrated/ERRATA.md'


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def git_blob(data: bytes) -> str:
    return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()


def check_readings(manifest: dict, files: dict[str, bytes]) -> None:
    require(manifest['schema'] == 'collatz-review-followup/v1', 'schema')
    require(manifest['base_commit'] == BASE, 'baseline')
    require(manifest['review']['commit'] == REVIEW, 'review head')
    require(manifest['review']['tree'] == '7f6ea329c06af44e836e7e2d88ad694654bd0d55', 'review tree')
    require(len(manifest['review']['file_blobs']) == 9, 'review file inventory')
    rows = manifest['affected_reading_surfaces']
    require(len(rows) == 7 and len({r['path'] for r in rows}) == 7, 'seven distinct active paths')
    require(len({r['archive_path'] for r in rows}) == 7, 'seven distinct archive paths')
    require([r['id'] for r in manifest['findings']] == [f'E-D-{n:03d}' for n in range(1, 9)], 'finding coverage')
    require(all(r['replacement_status'] == 'proposed_pending_narrow_independent_review'
                for r in manifest['findings']), 'replacement status')
    for row in rows:
        require(git_blob(files[row['path']]) == row['active_blob'], 'active bytes: '+row['path'])
        require(git_blob(files[row['archive_path']]) == row['original_blob'], 'archive bytes: '+row['path'])
        require(row['original_blob'] != row['active_blob'], 'unapplied edit: '+row['path'])
    text = files[ERRATA].decode('utf-8')
    for n in range(1, 9):
        require(f'## E-D-{n:03d} ' in text, 'missing erratum')
    require('PROPOSED pending narrow independent review' in text, 'new-wording boundary')
    require('PENDING NARROW INDEPENDENT REVIEW' in files['research/integrated/periodic-tails/README.md'].decode(), 'periodic flag')
    require('#67, #68, and #69' in files['research/RESULTS_CATALOG.md'].decode(), 'old unreviewed boundary')


def regressions() -> dict:
    # Direct algebra of the signed counterfamily, not an infinite sample claim.
    signed = 0
    for J in range(33):
        for n in range(1, 49):
            r = (-2**J) % 2**n
            require(r == (0 if n <= J else 2**n-2**J), 'signed residue')
            signed += 1
    require(F(1, 4-3) == 1 and F(2, 4-3) == 2, 'positive trivial realizers')
    P, Q = 3**12, 2**19
    quotient_cases = 0
    for n in range(9):
        for h in range(1, 10):
            value_delta = P**n*Q*h
            require(value_delta//Q == P**n*h, 'quotient scale')
            require(P*(value_delta//Q) == P**(n+1)*h, 'output scale')
            quotient_cases += 1
    # Exact overlap-band boundary tests include a band touching U but not L.
    band_cases = 0
    for q in (2, 3, 5, Q):
        for k in range(1, 5):
            edge = q**k
            for lower, upper, expected in [
                (F(edge), F(edge), [k+1]),
                (F(edge)-F(1,2), F(edge), [k,k+1]),
                (F(edge)-F(1,2), F(edge)-F(1,4), [k]),
                (F(edge), F(edge)+F(1,2), [k+1]),
            ]:
                got = [ell for ell in range(1,k+3) if q**(ell-1) <= upper and q**ell > lower]
                require(got == expected, 'feasible overlap interval')
                band_cases += 1
    require(F(1,81) == (1-F(17,81))/64, 'positive strip endpoint')
    require(-F(1,81) == -F(64,81)/64, 'negative strip endpoint')
    require(all(F(2*k,2).denominator == 1 and F(2*k+1,2).denominator == 2
                for k in range(32)), 'syndetic versus full-tail integrality')
    return dict(signed_residues=signed, quotient_cases=quotient_cases,
                overlap_band_cases=band_cases, strict_strip_counterexamples=2,
                scope='finite edge cases only; not universal Collatz proof checking')


def self_test(manifest: dict, files: dict[str, bytes]) -> int:
    mutations = [
        lambda m, f: m.update(base_commit='0'*40),
        lambda m, f: m['review'].update(commit='0'*40),
        lambda m, f: m['affected_reading_surfaces'].pop(),
        lambda m, f: m['findings'].pop(),
        lambda m, f: m['findings'][0].update(replacement_status='verified'),
        lambda m, f: f.__setitem__(m['affected_reading_surfaces'][0]['path'], b'wrong active bytes'),
        lambda m, f: f.__setitem__(m['affected_reading_surfaces'][0]['archive_path'], b'wrong archive'),
        lambda m, f: f.__setitem__(ERRATA, f[ERRATA].replace(b'## E-D-008 ', b'## OMITTED ')),
    ]
    for mutate in mutations:
        m, f = deepcopy(manifest), dict(files)
        mutate(m, f)
        try:
            check_readings(m, f)
        except ValueError:
            continue
        raise ValueError('invalid scoped fixture accepted')
    return len(mutations)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[3])
    ap.add_argument('--self-test', action='store_true')
    args = ap.parse_args()
    manifest = json.loads((args.root/MANIFEST).read_text(encoding='utf-8'))
    paths = {ERRATA}
    for row in manifest['affected_reading_surfaces']:
        paths.update((row['path'], row['archive_path']))
    files = {p: (args.root/p).read_bytes() for p in paths}
    check_readings(manifest, files)
    result = regressions()
    print('PASS scoped D follow-up: 7 active files / 7 exact archived originals / 8 dispositions')
    print(json.dumps(result, sort_keys=True))
    if args.self_test:
        print('Invalid scoped fixtures rejected:', self_test(manifest, files))


if __name__ == '__main__':
    main()
