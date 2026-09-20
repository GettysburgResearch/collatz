#!/usr/bin/env python3
"""Reproducible additional API/coverage controls, not independent peer review.

This test harness deliberately loads both implementations. verify.py itself
imports neither the generator nor this harness. No nonstandard packages.
"""
import hashlib
import importlib.util
import json
import random
import tempfile
from pathlib import Path


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    here = Path(__file__).resolve().parent
    run = load_module('acs_generator_contract', here/'run.py')
    verify = load_module('acs_verifier_contract', here/'verify.py')
    invalid = [([], None), ([[0,1],[1,0]], None), ([[True,1],[1,0]], None),
        ([[1,1.0],[1,0]], None), ([[1,1],[1,0]], [0,0]),
        ([[1,1],[1,0]], [3,3]), ([[1,1],[1,0]], [False,4]),
        ([[1,1],[1,0]], [-1,4])]
    count = 0
    for forms, ap in invalid:
        try:
            run.compile_family(forms, ap)
        except ValueError:
            count += 1
        else:
            raise ValueError('accepted invalid family')
    for d,b in [(-1,0),(True,0),(1,False),(1,1.0)]:
        try:
            run.compile_type(d,b)
        except ValueError:
            count += 1
        else:
            raise ValueError('accepted invalid chart')
    for gap in [0,-1,True,1.0]:
        try:
            run.gap_words(gap)
        except ValueError:
            count += 1
        else:
            raise ValueError('accepted invalid gap')
    with tempfile.TemporaryDirectory() as folder:
        path = Path(folder)/'duplicate.json'
        path.write_text('{"rows":[],"rows":[]}', encoding='utf-8')
        try:
            verify.load(path)
        except ValueError:
            count += 1
        else:
            raise ValueError('accepted duplicate JSON key')
    rng = random.Random(20260920)
    certificates = []
    for _ in range(256):
        core = rng.choice([1,5,7,11,35])
        size = rng.randrange(2,7)
        forms = [[core*2**rng.randrange(8)*3**rng.randrange(8),
                  rng.randrange(-10**6,10**6)] for _ in range(size)]
        modulus = rng.randrange(1,2000)
        residue = rng.randrange(modulus)
        result = run.compile_family(forms, [residue,modulus])
        verify.check_family(result)
        certificates.append(result)
    phase = run.compile_family([[1,2],[1,1]], [0,8])
    verify.check_family(phase)
    if (phase['base'], phase['modulus'], [len(w) for w in phase['words']]) != (48,128,[7,7]):
        raise ValueError('phase-neighborhood certificate changed')
    answer = dict(status='PASS', invalid_inputs_rejected=count,
        extra_family_seed=20260920, extra_family_count=len(certificates),
        extra_families_sha256=hashlib.sha256(run.canonical(certificates)).hexdigest(),
        phase_neighborhood=phase)
    print(json.dumps(answer, sort_keys=True))


if __name__ == '__main__':
    main()
