"""Bounded, exact controls for the moving-octave source count and cyclic gaps."""

from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import gcd


def require(test, message):
    if not test:
        raise ValueError(message)


def odd_step(x):
    raw = 3 * x + 1
    power = (raw & -raw).bit_length() - 1
    return raw >> power, power


def ceiling_ratio(n, d):
    return (n + d - 1) // d


def profile_check():
    total_groups = 0
    total_sources = 0
    max_words = 0
    for start_level in range(2, 12):
        lower = 2**start_level
        for length in range(1, 9):
            groups = defaultdict(lambda: defaultdict(list))
            for source in range(lower + 1, 2 * lower, 2):
                x = source
                levels = [start_level]
                clocks = []
                for _ in range(length):
                    x, valuation = odd_step(x)
                    clocks.append(valuation)
                    levels.append(x.bit_length() - 1)
                groups[tuple(levels)][tuple(clocks)].append(source)
            for levels, words in groups.items():
                final_lower = 2**levels[-1]
                require(len(words) <= length + 1, 'too many words')
                number = sum(map(len, words.values()))
                require(number <= (length + 1) * ceiling_ratio(final_lower, 3**length),
                        'source-count bound')
                for word, sources in words.items():
                    modulus = 2 ** (sum(word) + 1)
                    require(modulus * final_lower > 3**length * lower, 'clock lower bound')
                    require(all((source - sources[0]) % modulus == 0 for source in sources),
                            'shared-word terminal-parity cylinder')
                total_groups += 1
                total_sources += number
                max_words = max(max_words, len(words))
    return total_groups, total_sources, max_words


def affine_rank_check(actual, word):
    period = len(word)
    clock = sum(word)
    levels = []
    for x in actual:
        candidate = x.numerator.bit_length() - x.denominator.bit_length()
        levels.append(candidate if x >= Fraction(2)**candidate else candidate - 1)
    order = sorted(range(period), key=lambda i: actual[i] / Fraction(2)**levels[i])
    rank = {i: j for j, i in enumerate(order)}
    J = []
    for i in order:
        following = (i + 1) % period
        b = word[i] + levels[following] - levels[i]
        J.append(b * period + rank[following])
    require(sum(j - i for i, j in enumerate(J)) == period*clock, 'affine winding')
    displacement = max(abs(j-i) for i,j in enumerate(J))
    inversions = sum(J[j] > J[l % period] + (l // period)*period
                     for j in range(period) for l in range(j+1, j+2*displacement+1))
    bound = max(levels) - min(levels) + 1
    crossings = sum(0 < 3*(v - (2**s)*u) < 2**s - 1
                    for u in actual for v in actual for s in range(1, bound+1))
    require(crossings == inversions, 'geometric crossings')
    require(inversions >= gcd(clock, period)-1, 'cycle-count obstruction')
    if not crossings:
        require(J == [j+clock for j in range(period)], 'rank rotation')
    return inversions


def triadic_rank_check(odd, word):
    vertices, parity = [], []
    for i, a in enumerate(word):
        vertices.append(odd[i])
        parity.append(1)
        target = odd[(i+1) % len(odd)]
        for k in range(a-1, 0, -1):
            vertices.append(2**k * target)
            parity.append(0)
    period = len(vertices)
    levels = []
    normalized = []
    for vertex in vertices:
        t, x = 0, vertex
        while x < 1:
            x *= 3
            t -= 1
        while x >= 3:
            x /= 3
            t += 1
        normalized.append(x)
        levels.append(t)
    order = sorted(range(period), key=normalized.__getitem__)
    require(len(set(normalized)) == period, 'distinct triadic rays')
    rank = {i: j for j, i in enumerate(order)}
    J = []
    for i in order:
        prev = (i-1) % period
        correction = parity[prev]
        require(2*vertices[i] - correction == 3**correction * vertices[prev],
                'physical backward branch')
        J.append((correction + levels[prev] - levels[i])*period + rank[prev])
    require(sum(j-i for i,j in enumerate(J)) == period*len(odd), 'backward winding')
    displacement = max(abs(j-i) for i,j in enumerate(J))
    inversions = 0
    for j in range(period):
        for l in range(j+1, j+2*displacement+1):
            if J[l % period] + (l // period)*period >= J[j]:
                continue
            inversions += 1
            u, v = order[j], order[l % period]
            # Ratio of the later to earlier source lifting factors.
            ratio = Fraction(3) ** ((l // period) + levels[u] - levels[v])
            left, right = vertices[u], vertices[v]
            e_u, e_v = parity[(u-1) % period], parity[(v-1) % period]
            require(e_v == 1 and 0 < 2*(ratio*right-left) < ratio-e_u,
                    'backward physical crossing')
            if left.denominator == 1:
                require(ratio >= 3, 'ordinary triadic scale order')
    require(inversions >= gcd(period, len(odd))-1, 'backward cycle count')
    require((inversions-gcd(period, len(odd))+1) % 2 == 0, 'inversion parity')
    if inversions == 0:
        require(J == [j+len(odd) for j in range(period)], 'triadic rank rotation')
    return inversions


def cyclic_checks():
    checked = confined = 0
    nonintegral = inversions = triadic = gcd_obligations = 0
    defect_examples = []
    for length in range(1, 7):
        for word in product(range(1, 5), repeat=length):
            if min(word[i:] + word[:i] for i in range(length)) != word:
                continue
            if any(word == word[:h] * (length // h) for h in range(1, length) if length % h == 0):
                continue
            denominator = 2 ** sum(word) - 3**length
            if denominator <= 0:
                continue
            def carry(w):
                time, c = 0, 0
                for a in w:
                    c = 3*c + 2**time
                    time += a
                return c
            actual = [Fraction(carry(word[i:] + word[:i]), denominator) for i in range(length)]
            d = actual[0].denominator
            require(all(x.denominator == d for x in actual), 'phase denominators')
            checked += 1
            inversions += affine_rank_check(actual, word)
            triadic += triadic_rank_check(actual, word)
            gcd_obligations += gcd(sum(word), length) > 1
            if max(actual) >= 2*min(actual):
                if len(defect_examples) < 2 and d < denominator and min(actual) > 1:
                    defect_examples.append((word, denominator, d))
                continue
            confined += 1
            nonintegral += d > 1
            require(d == denominator, 'denominator saturation')
            ordered = sorted((int(d*x), i) for i, x in enumerate(actual))
            e = ordered[0][0]
            n = [value for value, _ in ordered]
            index = {i: j for j, (_, i) in enumerate(ordered)}
            image = [index[(i + 1) % length] for _, i in ordered]
            gap = [(n[j+1] if j+1 < length else 2*e) - value for j, value in enumerate(n)]
            require(all(image[(j+1) % length] == (image[j]+1) % length for j in range(length)),
                    'cyclic order')
            for j, (_, i) in enumerate(ordered):
                require(2**word[i] * gap[image[j]] == 3*gap[j] + (d if j+1 == length else 0),
                        'gap seam identity')
    require(defect_examples, 'missing wide-span partial cancellation control')
    return checked, confined, nonintegral, inversions, triadic, gcd_obligations, defect_examples


def residence_checks():
    checked = 0
    longest = (0, 0)
    for q in range(3, 100000, 2):
        k, power = 0, 1
        while power < q:
            k += 1
            power *= 3
        x = q
        length = 0
        visited = {x}
        while True:
            x, _ = odd_step(x)
            if x < q or x >= 2*q or x in visited:
                break
            visited.add(x)
            length += 1
        require(length <= 2*k, 'single-octave residence')
        longest = max(longest, (length, q))
        checked += 1
    return checked, longest


if __name__ == '__main__':
    print('moving profile groups, source occurrences, maximum word count:', profile_check())
    print('primitive rational cycles, octave confined, nonintegral confined, dyadic crossings, triadic crossings, noncoprime clocks, wide controls:', cyclic_checks())
    print('ordinary source checks, longest internal trajectory (edges, source):', residence_checks())
