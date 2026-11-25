#!/usr/bin/env python3
"""Independent exact check of the finite inverse-cost experiment; not a cycle exclusion."""
from pathlib import Path
import json
import subprocess
import tempfile


def demand(ok, message):
    if not ok:
        raise RuntimeError(message)


def direct_table(k):
    """Enumerate forward exponent compositions, independently of the inverse DP."""
    modulus = 3**k
    result = [65535] * modulus
    limit = 4*k-2

    def visit(left, spent, carry):
        if left == 0:
            residue = carry * pow(pow(2, spent, modulus), -1, modulus) % modulus
            result[residue] = min(result[residue], spent)
            return
        for exponent in range(1, limit-spent-(left-1)+1):
            visit(left-1, spent+exponent, (3*carry+pow(2, spent, modulus)) % modulus)

    visit(k, 0, 0)
    return result


def main():
    source = Path(__file__).with_name('inverse_minimum.cpp')
    with tempfile.TemporaryDirectory(prefix='collatz-inverse-minimum-') as work:
        binary = str(Path(work) / 'inverse_minimum')
        compile_result = subprocess.run(['g++', '-O3', '-std=c++17', '-Wall', '-Wextra',
                                         '-Werror', str(source), '-o', binary],
                                        capture_output=True, text=True, check=True)
        demand(not compile_result.stdout and not compile_result.stderr, 'compiler diagnostic')
        small = subprocess.run([binary, '6'], capture_output=True, text=True, check=True)
        demand(not small.stderr, 'small census stderr')
        tables = [line.split() for line in small.stdout.splitlines() if line.startswith('table ')]
        demand(len(tables) == 6, 'missing small exact tables')
        for words in tables:
            k = int(words[1])
            demand(list(map(int, words[2:])) == direct_table(k), 'independent table differs at '+str(k))
        complete = subprocess.run([binary, '17'], capture_output=True, text=True,
                                  check=True, timeout=300)
        demand(not complete.stderr, 'complete census stderr')
        rows = []
        for line in complete.stdout.splitlines():
            words = line.split()
            demand(words[0] == 'k' and words[12] == 'savings', 'unrecognized census row')
            row = {words[i]: int(words[i+1]) for i in range(0,12,2)}
            row['savings'] = {int(a): int(b) for a,b in (w.split(':') for w in words[13:])}
            k = row['k']
            demand(row['residues'] == 3**k and row['allowed'] == row['total'] == 2**k,
                   'unexpected complete-word count')
            demand(row['direct_forbidden'] == 0, 'unexpected three-clock saving')
            expected = {0: 2**k} if k <= 15 else ({0:65532,1:4} if k == 16 else {0:131050,1:22})
            demand(row['savings'] == expected, 'unexpected saving census')
            rows.append(row)
        demand(len(rows) == 17, 'missing census depth')
    print(json.dumps({'status':'PASS', 'scope':'finite native {1,2} words through depth 17',
          'independent_composition_tables':6, 'rows':rows}, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
