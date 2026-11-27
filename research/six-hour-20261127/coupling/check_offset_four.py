"""Replay the positive-source charts and all signed-seventeen end words."""
import json
from pathlib import Path


def check(condition, context):
    if not condition:
        raise ValueError(context)


def run(x, clocks):
    grade = 0
    for _ in range(clocks):
        bit = x % 2
        x = (3 * x + 1) // 2 if bit else x // 2
        grade += bit
    return x, grade


def hard(k):
    return 12 * 2 ** (18 * k) - 1


def row(k, shift, clocks, periodic):
    m = hard(k)
    d, rem = divmod(m - 5, 11)
    signed, turn_grade = run(-17, rem)
    n = 7 * d + 3 + turn_grade
    left, right = max(0, -shift), max(0, shift)
    residue = pow(3, n - left, 2**clocks)
    base1, base2 = 3**left * residue + signed, 3**right * residue - 1
    end1, grade1 = run(base1, clocks)
    end2, grade2 = run(base2, clocks)
    check(min(base1, base2) > 0, (k, 'physical end-word sources'))
    check(end1 == end2 and left + grade1 == right + grade2, (k, 'merger'))
    check(0 < n + shift < m - 40, (k, 'paid gap'))
    if periodic:
        check(clocks <= 18 * k, (k, 'binary precision'))
        for t in range(1, 4):
            inc, residue_m = divmod(hard(k + 5*t) - m, 11 * 2**clocks)
            check(inc > 0 and residue_m == 0, (k, t, 'period'))
    return dict(k=k, periodic=periodic, remainder=rem, turn_grade=turn_grade,
                signed=signed, left_power=left, right_power=right, clocks=clocks,
                unit_mod_2h=residue, word_grades=[grade1, grade2],
                common_residue_endpoint=end1)


def controls():
    check(run(-17, 11) == (-17, 7), 'negative cycle')
    check(pow(2, 90, 11) == 1, 'mod 11 period')
    check(pow(2, 18, 27) == 1 and pow(2, 162, 243) == 1, 'parent addresses')
    samples = []
    for j in (0, 1, 2, 5, 10):
        m = 11 + 162*j
        x = 2**(m-5)
        z, remainder = divmod(128*2**m - 271, 81)
        w = (z-31)//2
        check(remainder == 0 and x % 243 == 64, (j, 'source address'))
        check(0 < w < z and w % 48 == 17 and 2*w+31 == z, (j, 'canonical source'))
        check(run(w,10) == (2**(m-4)-1,4), (j, 'lower word'))
        check(run(3*w,11) == (27*x-17,6), (j, 'upper word'))
        samples.append(dict(j=j,m=m,w_mod_24576=w%24576))
    short = [(1,7,80),(2,2,31),(3,1,205),(4,-1,36),(5,1,64),(6,3,55)]
    periodic = [(7,2,31),(8,1,109),(9,-1,36),(10,1,64),(11,3,55)]
    rows = [row(k,g,h,False) for k,g,h in short] + [row(k,g,h,True) for k,g,h in periodic]
    check({r['k']%5 for r in rows if r['periodic']} == set(range(5)), 'coverage')
    return dict(source='27*2^(m-5)-17', turn_clocks=11, turn_grade=7,
                canonical_samples=samples, rows=rows)


if __name__ == '__main__':
    result = json.dumps(controls(), indent=2) + '\n'
    reference = Path(__file__).with_name('OFFSET_FOUR_CONTROLS.json')
    if reference.read_text() != result:
        raise SystemExit('OFFSET_FOUR_CONTROLS.json differs')
    print(result, end='')
