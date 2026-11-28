"""A literal four-source clock rectangle, checked by complete native transcripts."""
from fractions import Fraction
import hashlib
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def first_hit(n, target):
    x, j, s = n, 0, 0
    history = []
    seen = set()
    while x != target:
        require(x not in seen, 'cycle before target')
        require(s < 10000, 'finite control exceeded its explicit step cap')
        seen.add(x)
        history.append(x)
        bit = x % 2
        x = (3*x+1)//2 if bit else x//2
        j += bit
        s += 1
    return j, s, Fraction(target*2**s, 3**j), history+[target]


def main():
    sources = (81, 135, 69, 115)
    expected = ((5, 12), (12, 24), (2, 7), (9, 19))
    rows = [first_hit(n, 5) for n in sources]
    require(tuple(r[:2] for r in rows) == expected, 'actual first-hit clocks')
    require(len(set(sources)) == len({r[2] for r in rows}) == 4,
            'four distinct starts and corrected values')
    require(sources[0]*sources[3] == sources[1]*sources[2] == 9315,
            'literal source product')
    for k in (0, 1):
        require(rows[0][k]+rows[3][k] == rows[1][k]+rows[2][k],
                'both native clock sums')
    require(rows[0][2]*rows[3][2] == rows[1][2]*rows[2][2],
            'corrected product')
    factors = [r[2]/n for n, r in zip(sources, rows)]
    require(factors[0]*factors[3] == factors[1]*factors[2],
            'exact correction-factor product, before logarithms')
    transcript = json.dumps([r[3] for r in rows], separators=(',', ':'))
    print(json.dumps({
        'scope': 'One literal ordinary rectangle, not an asymptotic count.',
        'target': 5, 'sources': sources, 'rows': expected,
        'corrected_values': [str(r[2]) for r in rows],
        'native_steps': sum(r[1] for r in rows),
        'transcript_sha256': hashlib.sha256(transcript.encode()).hexdigest(),
    }, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
