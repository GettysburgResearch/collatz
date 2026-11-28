"""Exact rational controls for prefix transporters and physical fusion fixtures."""

from collections import defaultdict
from fractions import Fraction as F
from functools import cache
from itertools import product


def require(condition, message):
    if not condition:
        raise ValueError(message)


@cache
def words_of_total(total):
    if total < 0:
        return ()
    if total == 0:
        return ((),)
    return tuple((first,) + rest for first in range(1, total + 1)
                 for rest in words_of_total(total - first))


@cache
def words_up_to(limit):
    return tuple(w for total in range(limit + 1) for w in words_of_total(total))


@cache
def affine(word):
    slope, offset = F(1), F(0)
    for e in reversed(word):
        slope, offset = 3 * slope / 2**e, (1 + 3 * offset) / 2**e
    return slope, offset


def parameters(u, v):
    su, bu = affine(u)
    sv, bv = affine(v)
    return sum(v) - sum(u), len(u) - len(v), bu - su * bv / sv


def v2(value):
    def order(integer):
        return (integer & -integer).bit_length() - 1
    return order(abs(value.numerator)) - order(value.denominator)


def weight(word, theta):
    return theta**len(word) * (1 - theta)**(sum(word) - len(word))


def prefix_sources(a, b, c):
    """Return target words or target prefix/gap-tail addresses; no theta input."""
    c = F(c)
    if c == 0:
        if b != 0:
            return ()
        return (((), 0),) if a == 0 else (((), max(1, 1 - a)),)

    pure = []
    # If v is empty, a=-S_u; if u is empty, a=S_v.
    for left_empty in (False, True):
        total = a if left_empty else -a
        for w in words_of_total(total):
            u, v = ((), w) if left_empty else (w, ())
            if parameters(u, v) == (a, b, c):
                pure.append((u, 0))
    if pure:
        require(len(pure) == 1, 'reduced pure transporter must be unique')
        return tuple(pure)

    r = -v2(c)
    slope = F(2)**a * F(3)**b
    targets = []
    for u in words_up_to(max(0, r)):
        for v in words_up_to(max(0, r + a)):
            d = a + sum(u) - sum(v)
            if d == 0 or len(u) - len(v) != b:
                continue
            if affine(u)[1] - slope * affine(v)[1] != c:
                continue
            first = max(1, 1 - d)
            require(parameters(u + (first,), v + (first + d,)) == (a, b, c),
                    'reported first positive-gap representative is wrong')
            targets.append((u, first))
    return tuple(targets)


def exact_common(a, b, c, theta):
    q = 1 - theta
    target = sum((weight(u, theta) * q**max(0, first - 1)
                  for u, first in prefix_sources(a, b, c)), F(0))
    factor = q**a * (q / theta)**b
    require(0 <= target <= 1 and factor * target <= 1,
            'shared probability exceeds one')
    return min(F(1), factor) * target


def reduced_pair(u, v):
    while u and v and u[-1] == v[-1]:
        u, v = u[:-1], v[:-1]
    return u, v


def in_carrier(word, families):
    for prefix, first in families:
        n = len(prefix)
        if word[:n] == prefix and (first == 0 or (len(word) > n and word[n] >= first)):
            return True
    return False


def check_bounded_catalogue():
    words = words_up_to(6)
    tables = defaultdict(set)
    for u, v in product(words, repeat=2):
        key = parameters(u, v)
        tables[key].add(reduced_pair(u, v))
    theta = F(2, 3)
    for (a, b, c), pairs in tables.items():
        specs = prefix_sources(a, b, c)
        for u, _ in pairs:
            require(in_carrier(u, specs), 'independently enumerated word pair was lost')
        reverse = parameters_reverse(a, b, c)
        require(exact_common(a, b, c, theta) == exact_common(*reverse, theta),
                'direct and inverse common-part masses disagree')

    # Exhaust the independent small search for all a,b in {-1,0,1}, c!=0,
    # -v2(c)<=2. Both normalized last letters can be taken with minimum 1.
    # The two pre-last totals are at most 2,3. Every resulting normalized
    # word has total <=4: if its final letter exceeds 1 the OTHER word ends
    # in 1, and its total differs by at most one.
    negatives = 0
    for a, b, numerator, denominator in product(range(-1, 2), range(-1, 2),
                                                range(-7, 8), (1, 2, 3, 4, 6, 9)):
        c = F(numerator, denominator)
        if not c:
            continue
        key = (a, b, c)
        value = bool(prefix_sources(*key))
        require(value == (key in tables), 'decoder disagrees with complete small census')
        negatives += not value
    require(negatives > 300, 'negative control census unexpectedly small')
    return len(words)**2, len(tables), negatives


def parameters_reverse(a, b, c):
    return -a, -b, -c / (F(2)**a * F(3)**b)


def reverse_gap_word(x, clock):
    word, gap = [], 0
    for _ in range(clock):
        if x % 2:
            if gap:
                word.append(gap)
            gap = 1
            x = (3*x + 1) // 2
        else:
            gap += 1
            x //= 2
    require(x % 2 and gap, 'fusion fixture did not end at an odd state')
    word.append(gap)
    return tuple(reversed(word)), x


def check_fusion():
    fixtures = ((1, 1, 1, 4), (1, -1, 3, 5), (1, 3, 5, 6),
                (2, 1, 1, 2), (3, -7, 39, 13), (0, 2, 7, 13),
                (2, -3, 39, 13), (4, 3, 59, 8))
    for m, offset, x, clock in fixtures:
        y = (1 << m) * x + offset
        u, z = reverse_gap_word(x, clock)
        v, t = reverse_gap_word(y, clock + m)
        require(z == t and len(u) == len(v) and u != v, 'false counted fusion')
        su, bu = affine(u)
        sv, bv = affine(v)
        require(su == (1 << m) * sv and bu == bv + sv * offset,
                'normalized physical affine identity failed')
        require(not prefix_sources(m, 0, F(offset)), 'odd-preserving physical map overlapped')
    return len(fixtures)


def main():
    theta = F(2, 3)
    q = 1 - theta
    for sign in (-1, 1):
        require(exact_common(0, 0, F(sign, 4), theta) == theta * q,
                'quarter-shift or inverse overlap')
        require(exact_common(sign, 0, 0, theta) == q, 'dyadic dilation or inverse')
    for e in range(1, 6):
        pure = parameters((e,), ())
        require(exact_common(*pure, theta) == weight((e,), theta), 'one word image')
        require(exact_common(*parameters_reverse(*pure), theta) == weight((e,), theta),
                'inverse one-word image')
    require(exact_common(0, 0, F(1, 2), theta) == 0, 'half-shift singularity')
    for d in range(-26, 27):
        require(exact_common(0, 0, F(d), theta) == int(d == 0), 'integer translation')
    count, distinct, negatives = check_bounded_catalogue()
    print(f'{count} word pairs, {distinct} affine maps, {negatives} rejected controls, '
          f'{check_fusion()} ordinary unequal-clock/translated fusions passed')


if __name__ == '__main__':
    main()
