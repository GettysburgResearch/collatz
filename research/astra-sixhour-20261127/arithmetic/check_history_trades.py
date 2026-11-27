"""Replay two-place history cycles on genuine ordinary and rational controls."""
from collections import defaultdict, deque
import json
from check_small_filter import extend, lowbit, rank_array, require


def forest_path(adjacency, start, end):
    previous = {start: None}
    queue = deque([start])
    while queue:
        u = queue.popleft()
        if u == end:
            path = []
            while previous[u] is not None:
                u, edge = previous[u]
                path.append(edge)
            return list(reversed(path))
        for v, edge in adjacency[u]:
            if v not in previous:
                previous[v] = (u, edge)
                queue.append(v)
    return None


def audit(word, length):
    values = rank_array(word)
    p, h = len(word), sum(word)
    q = values[0].denominator
    require(all(x.denominator == q for x in values), 'full odd denominator')
    digits = list(map(lowbit, values))
    shift = {j: j*h % p for j in range(-length, length+1)}
    two, three = 1 << (length*h//p), 3**length
    modulus = two*three
    span = q*(max(values)-min(values))
    forest = defaultdict(list)
    vertices = set()
    nonzero = balanced = tested = 0
    witness = None
    for r in range(p):
        past = ('P', tuple(extend(digits, r+shift[j]) for j in range(-length, 0)))
        future = ('F', tuple(extend(digits, r+shift[j]) for j in range(length)))
        vertices.update((past, future))
        path = forest_path(forest, past, future)
        if path is None:
            forest[past].append((future, r))
            forest[future].append((past, r))
            continue
        ranks = [r, *path]
        require(len(ranks) % 2 == 0 and len(set(ranks)) == len(ranks), 'alternating edges')
        signs = [1 if j % 2 == 0 else -1 for j in range(len(ranks))]
        signed = lambda array, j: sum(s*extend(array, i+shift[j]) for s, i in zip(signs, ranks))
        numerator = q*signed(values, 0)
        require(numerator.denominator == 1 and numerator % modulus == 0, 'complete two-place divisor')
        require(not (len(ranks)*span < 2*modulus) or numerator == 0, 'interval lift')
        for j in range(-length, length):
            require(signed(digits, j) == 0, 'actual multiset balance')
            beta = (j+1)*h//p - j*h//p
            require((1 << beta)*signed(values, j+1) == 3*signed(values, j), 'exact bilateral transport')
        if numerator:
            nonzero += 1
            if witness is None:
                witness = {'ranks': ranks, 'signed_source_sum': str(signed(values, 0)),
                           'cleared_quotient': int(numerator/modulus)}
        else:
            balanced += 1
        tested += 1
    components = len(vertices)-(p-tested)
    return {'period': p, 'clock': h, 'denominator': q, 'odd_steps_each_side': length,
            'moduli': [two, three], 'vertices': len(vertices), 'components': components,
            'independent_forest_cycles': tested, 'zero_sum': balanced, 'nonzero_sum': nonzero,
            'first_nonzero': witness}


if __name__ == '__main__':
    controls = [[2], [1, 1, 2, 2, 2], [1,1,1,2,2,2,2,2],
                list(map(int, '12112121212211222212212121221122212211222'))]
    outcomes = [audit(word, length) for word in controls for length in (1, 2, 3, 4)]
    require(any(row['nonzero_sum'] for row in outcomes), 'rational obstruction fixture must be active')
    require(all(row['independent_forest_cycles'] == 0 for row in outcomes if row['period'] == 1),
            'ordinary fixed-point control')
    print(json.dumps(outcomes, indent=2))
