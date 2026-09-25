#!/usr/bin/env python3
"""Regenerate both original payloads; verify their pinned SHA-256 identities."""
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import subprocess
import sys
from certify_budget import certify

HERE = Path(__file__).resolve().parent
OUT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else HERE / 'replayed'
OUT.mkdir(parents=True, exist_ok=True)
flags = ['-O'] if sys.flags.optimize else []
subprocess.run([sys.executable, *flags, '-S', '-B', str(HERE/'experiment.py'),
                '--output', str(OUT/'results.json')], check=True)
rows = [certify(27, Fraction(1)), certify(27, Fraction(10)),
        certify(13, Fraction(2), 5), certify(871, Fraction(10), 3, 4096),
        certify(1, Fraction(0))]
(OUT/'budget_certificates.json').write_text(json.dumps(rows, indent=2, sort_keys=True), encoding='utf-8')
expected = {'results.json': '8c8f2c92f6f31b755de75cbe1e590273549ba888e5017ce6d820ff74a7a35369',
            'budget_certificates.json': 'fa279c8a504777318ced0b1fd0025ee89024f0f1edd774dc34c90f21b4dbaa84'}
for name, digest in expected.items():
    if hashlib.sha256((OUT/name).read_bytes()).hexdigest() != digest:
        raise ValueError('original output identity changed: '+name)
for checker, payload in [('verify_certificates.py', 'results.json'),
                         ('verify_budget.py', 'budget_certificates.json')]:
    subprocess.run([sys.executable, *flags, '-S', '-B', str(HERE/checker), str(OUT/payload)], check=True)
print(json.dumps({'status':'PASS', 'original_payloads': expected}, sort_keys=True, indent=2))
