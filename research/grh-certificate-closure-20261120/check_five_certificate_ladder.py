#!/usr/bin/env python3
"""Exact finite replay of the physical five certificate ladder."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def need(ok: bool, why: str) -> None:
    if not ok:
        raise ValueError(why)


def positive_odd(n: int) -> None:
    need(type(n) is int and n > 0 and n % 2 == 1, 'positive ordinary odd input')


def odd_step(n: int) -> tuple[int, int]:
    positive_odd(n)
    y, a = 3*n+1, 0
    while y % 2 == 0:
        y //= 2
        a += 1
    return y, a


def shortcut(n: int) -> int:
    need(type(n) is int and n > 0, 'positive ordinary input')
    return (3*n+1)//2 if n % 2 else n//2


def inverse_word(q: int, word: list[int]) -> int:
    positive_odd(q)
    for a in reversed(word):
        need(type(a) is int and a >= 1, 'positive division exponent')
        raw = (q << a)-1
        need(raw % 3 == 0, 'legal inverse division')
        q = raw//3
        positive_odd(q)
    return q


def run_word(x: int, word: list[int], first_hit: bool = False) -> int:
    positive_odd(x)
    for a in word:
        need(type(a) is int and a >= 1, 'positive integer division exponent')
        if first_hit:
            need(x != 1, 'premature first hit')
        x, actual = odd_step(x)
        need(actual == a, 'actual exponent differs')
    return x


def target_block(r: int, b: int) -> list[int]:
    need(type(r) is int and r >= 1 and type(b) is int and b >= 4, 'block domain')
    return [5, b-3] if r == 1 else [4]+[2]*(r-2)+[3, b-3]


def compile_five(x: int, source: list[int]) -> dict:
    need(run_word(x, source, True) == 1, 'supplied certificate does not end at one')
    out, i, blocks = [], 0, 0
    while i < len(source):
        start = i
        while i < len(source) and source[i] == 2:
            i += 1
        r = i-start
        if r == 0 or i == len(source) or source[i] < 4:
            return {'status': 'UNRESOLVED', 'consumed_letters': start}
        out += target_block(r, source[i])
        i += 1
        blocks += 1
    out.append(4)
    need(run_word(5*x, out, True) == 1, 'output certificate')
    need(len(out) == len(source)+1 and sum(out) == sum(source)+4,
         'exact output clocks')
    return {'status': 'CERTIFIED', 'word': out, 'blocks': blocks}


def pick_lift(q: int, r: int) -> tuple[int, int]:
    positive_odd(q)
    need(q % 3 != 0 and r >= 1, 'unit lift domain')
    modulus = 3**(r+1)
    for b in range(4, 4*3**r+4):
        if pow(2, b-2, modulus)*q % modulus != 1:
            continue
        x = inverse_word(q, [2]*r+[b])
        if x % 3:
            return x, b
    raise ValueError('proved unit lift bound failed')


def run() -> dict:
    counts = {'paired_blocks': 0, 'literal_shortcut_edges': 0,
              'odd_edges': 0, 'cylinder_inputs': 0,
              'first_hit_families': 0, 'compiled_certificates': 0,
              'rejected_controls': 0, 'unresolved_controls': 0}
    fixtures = []
    parameters = [(r,b) for r in range(1,13) for b in range(4,16)]
    parameters += [(r,b) for r in (24,64,128) for b in (4,7,19)]
    for r,b in parameters:
        modulus = 3**(r+1)
        q0 = pow(pow(2, b-2, modulus), -1, modulus)
        if q0 % 2 == 0:
            q0 += modulus
        for lift in range(3):
            q = q0+2*modulus*lift
            source = [2]*r+[b]
            target = target_block(r,b)
            x = inverse_word(q, source)
            need(inverse_word(5*q,target) == 5*x, 'inverse identity')
            need(run_word(x,source) == q and run_word(5*x,target) == 5*q,
                 'literal odd endpoints')
            need(len(source) == len(target) and sum(source) == sum(target),
                 'paired clocks')
            a,c = x,5*x
            for _ in range(sum(source)):
                a,c = shortcut(a),shortcut(c)
                counts['literal_shortcut_edges'] += 2
            need((a,c) == (q,5*q), 'literal shortcut endpoints')
            residue = 1+(1 if r%2==0 else 3)*2**(2*r+2)
            need(x % 2**(2*r+4) == residue, 'source cylinder')
            need(7*q <= x and q%3, 'smaller unit endpoint')
            counts['paired_blocks'] += 1
            counts['odd_edges'] += 2*len(source)
            fixtures.append((r,b,q,x))

    for x in range(1,100000,2):
        for r in range(1,7):
            residue = 1+(1 if r%2==0 else 3)*2**(2*r+2)
            if x % 2**(2*r+4) != residue:
                continue
            y = x
            for _ in range(r):
                y,a = odd_step(y)
                need(a == 2, 'converse initial exponent')
            q,b = odd_step(y)
            need(b >= 4 and 7*q <= x, 'converse terminal exponent and height')
            counts['cylinder_inputs'] += 1

    for r in range(1,7):
        for k in range(1,4):
            b = 2+2*3**r*k
            source = [2]*r+[b]
            x = inverse_word(1,source)
            expected = 1+4**(r+1)*(4**(3**r*k)-1)//3**(r+1)
            need(x == expected and x%3 == (1+k)%3, 'closed family and unit guard')
            result = compile_five(x,source)
            need(result['status'] == 'CERTIFIED', 'family compilation')
            counts['first_hit_families'] += 1
            counts['compiled_certificates'] += 1

    for pattern in ([1], [2], [3], [1,2], [2,1,3], [3,2,1,3,2,1], [1]*12):
        q, source = 1, []
        for r in reversed(pattern):
            q,b = pick_lift(q,r)
            source = [2]*r+[b]+source
        result = compile_five(q,source)
        need(result['status'] == 'CERTIFIED' and result['blocks'] == len(pattern),
             'composed compiler')
        counts['compiled_certificates'] += 1
    need(compile_five(1,[])['word'] == [4], 'empty source certificate')
    counts['compiled_certificates'] += 1

    # These are valid convergent antecedents outside the proved grammar.
    for x,word in [(5,[4]),(13,[3,4]),(3,[1,4])]:
        need(compile_five(x,word)['status'] == 'UNRESOLVED', 'unsupported word falsely accepted')
        counts['unresolved_controls'] += 1
    controls = [lambda: target_block(0,4), lambda: target_block(2,3),
                lambda: odd_step(True), lambda: odd_step(-1),
                lambda: compile_five(113,[2,7]),
                lambda: compile_five(113,[2.0,8]),
                lambda: compile_five(3,[True,4]),
                lambda: compile_five(1,[2]),
                lambda: inverse_word(3,[1])]
    for control in controls:
        try:
            control()
        except ValueError:
            counts['rejected_controls'] += 1
        else:
            raise ValueError('negative control accepted')
    return {'status':'PASS','counts':counts,
            'maximum_ladder_run':128,
            'fixture_sha256':hashlib.sha256(repr(fixtures).encode()).hexdigest(),
            'scope':'Exact finite ordinary replay of FL1-FL4 and the partial certificate compiler; universal claims rely on the proof. No full five closure or Collatz proof.',
            'grh_used':False}


if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    raw=json.dumps(run(),indent=2,sort_keys=True)+'\n'
    if args.output:
        args.output.write_text(raw,encoding='utf-8')
    print(raw,end='')
