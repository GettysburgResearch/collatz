"""Exact path-population bound for every mechanical rank phase at length 256."""
from collections import Counter
from itertools import product
import json

from check_strip_energy import schedules


def population(word, initial):
    counts = {initial: 1}
    for beta, next_beta in zip(word, word[1:]):
        next_counts = Counter()
        for k, count in counts.items():
            for gap in (1, 2):
                successor = k + beta - gap
                if 0 <= successor <= 3 - next_beta:
                    next_counts[successor] += count
        counts = next_counts
    return sum(counts.values())


def direct_population(word, initial):
    total = 0
    for gaps in product((1, 2), repeat=len(word) - 1):
        layer = initial
        for i, gap in enumerate(gaps):
            layer += word[i] - gap
            if not 0 <= layer <= 3 - word[i + 1]:
                break
        else:
            total += 1
    return total


def run():
    controls = 0
    for word in schedules(8):
        for k in range(4 - word[0]):
            if population(word, k) != direct_population(word, k):
                raise ArithmeticError(('independent eight-step control', word, k))
            controls += 1
    maxima = {}
    words = schedules(256)
    for word in words:
        clock = sum(word[:-1])
        count = max(population(word, k) for k in range(4 - word[0]))
        maxima[clock] = max(maxima.get(clock, 0), count)
    if len(words) != 258 or set(maxima) != {405, 406}:
        raise ArithmeticError(('phase coverage', len(words), sorted(maxima)))
    if any(count**25 >= 2**(12*clock) for clock, count in maxima.items()):
        raise ArithmeticError(('12/25 support exponent', maxima))
    return {'odd_steps': 256, 'phase_schedules': len(words), 'direct_checks_at_eight': controls,
            'max_histories_by_native_clock': maxima, 'certified_rate': '12/25'}


if __name__ == '__main__':
    print(json.dumps(run(), indent=2))
