"""Verify literal paths and the integer affine identities of every certificate.

The verifier imports neither the search nor its inverse-word implementation.
All-parameter validity follows from parity-cylinder lifting, as proved in the
accompanying note; these checks authenticate each input to that theorem.
"""
from pathlib import Path
import hashlib
import json


def require(test, message):
    if not test:
        raise ValueError(message)


def replay(n, word):
    start = n
    odd = 0
    additive = 0
    denominator = 1
    coefficient = 1
    for bit in word:
        require(bit in '01', 'invalid bit')
        require(n % 2 == int(bit), 'incorrect physical parity')
        if bit == '0':
            n //= 2
        else:
            n = (3 * n + 1) // 2
            additive = 3 * additive + denominator
            coefficient *= 3
            odd += 1
        denominator *= 2
    require(denominator * n == coefficient * start + additive,
            'affine numerator identity failed')
    return n, odd


def verify(path):
    raw = path.read_bytes()
    data = json.loads(raw)
    require(data['schema'] == 'ordinary-merger-progressions-v1', 'schema')
    M = data['source_modulus']
    require(M == 73728 and data['source_clock'] == 13, 'packet parameters')
    covered = set()
    max_clock = 0
    for row in data['rows']:
        n, x, S = row['source'], row['partner'], row['partner_increment']
        w, v = row['source_word'], row['partner_word']
        require(0 < x < n < M, 'strict source reduction failed')
        require(0 < S < M, 'strict slope reduction failed')
        require(n % 128 == 27 and n not in covered, 'invalid source partition')
        require(len(w) == 13 and len(v) <= data['search_partner_clock_limit'], 'clocks')
        require(M % 2**len(w) == 0 and S % 2**len(v) == 0,
                'increments do not preserve the physical words')
        y, p = replay(n, w)
        z, q = replay(x, v)
        require(y == z, 'base endpoints differ')
        require(3**p * (M // 2**len(w)) ==
                3**q * (S // 2**len(v)), 'endpoint slopes differ')
        # Separate literal check at t=1; the theorem covers every t>=0.
        y1, p1 = replay(n + M, w)
        z1, q1 = replay(x + S, v)
        require(y1 == z1 and p1 == p and q1 == q, 'second physical ray point')
        covered.add(n)
        max_clock = max(max_clock, len(v))
    unresolved = set(data['unresolved'])
    require(len(unresolved) == len(data['unresolved']), 'duplicate unresolved class')
    require(not covered.intersection(unresolved), 'overlapping statuses')
    require(covered | unresolved == set(range(27, M, 128)), 'partition incomplete')
    require(len(covered) == data['certified_classes'] == 446, 'certified count')
    require(len(covered | unresolved) == data['source_classes'] == 576, 'total count')
    all_sources = covered | unresolved
    trivial = {n for n in all_sources if n % 3 == 2}
    direct = set()
    for n in all_sources:
        y = n
        for _ in range(13):
            y = y // 2 if y % 2 == 0 else (3 * y + 1) // 2
            if y < n:
                direct.add(n)
                break
    baseline = trivial | direct
    require(baseline <= covered, 'certificate missed an identified baseline')
    require((len(trivial), len(direct), len(baseline), len(covered - baseline))
            == (192, 207, 330, 116), 'baseline comparison')
    return dict(status='PASS', certified_classes=len(covered),
                unresolved_classes=len(unresolved), source_modulus=M,
                source_clock=13, maximum_partner_clock=max_clock,
                ray_samples_replayed=2 * len(covered),
                trivial_smaller_predecessor_classes=len(trivial),
                direct_descent_by_clock_13_classes=len(direct),
                baseline_union_classes=len(baseline),
                certified_beyond_baseline_classes=len(covered - baseline),
                file_sha256=hashlib.sha256(raw).hexdigest(),
                scope='Exact infinite arithmetic-progression mergers; incomplete branch cover.')


if __name__ == '__main__':
    print(json.dumps(verify(Path(__file__).with_name('al27_certificate.json')), indent=2))
