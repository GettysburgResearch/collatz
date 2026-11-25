#!/usr/bin/env python3
"""Independent ordinary-orbit check of the supplied 81 binary cylinders."""
import json
from pathlib import Path
import re


def demand(ok, message):
    if not ok:
        raise RuntimeError(message)


def orbit(n, h):
    odd = 0
    for _ in range(h):
        odd += n % 2
        n = n//2 if n%2 == 0 else (3*n+1)//2
    return n, odd


root = Path(__file__).resolve().parents[3]
source = root / 'research/astra-diagonal-closure-20261125/joint/TritChain.lean'
match = re.search(r'\(\[([\d,\s]+)\]\s*:\s*List Nat\)', source.read_text())
demand(match is not None, 'witness table missing')
residues = list(map(int, re.findall(r'\d+', match.group(1))))
demand(len(residues) == 81 and max(residues) < 2**14, 'invalid witness table')
checks = 0
for suffix, residue in enumerate(residues):
    for lift in (0, 1, 17, 2**128+37):
        n = residue+2**14*lift
        for h in (14,17,31):
            x,p = orbit(n,h)
            y,q = orbit(81*n+suffix,h)
            demand(x == y and p == q+4, 'ordinary cylinder mismatch')
            checks += 1
print(json.dumps({'status':'PASS','suffixes':81,'checks':checks,
                  'clock':14,'maximum_residue':max(residues),
                  'scope':'finite independent controls; Lean supplies all-lifts theorem'},
                 indent=2, sort_keys=True))
