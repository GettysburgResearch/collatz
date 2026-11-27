"""Unnormalized four-copy transfers for the bounded physical phase mask."""
from collections import Counter
from functools import cache
from itertools import combinations_with_replacement, product
from math import log2
import json
import sys


def floor_alpha(n):
    if n < 0:
        return -(3 ** (-n)).bit_length()
    return (3 ** n).bit_length() - 1


def schedules(steps):
    return sorted({
        tuple(floor_alpha(i + 1 - j) - floor_alpha(i - j) for i in range(steps + 1))
        for j in range(steps + 2)
    })


@cache
def advance_pair(pair, beta, next_beta):
    choices = [
        tuple(k + beta - a for a in (1, 2) if 0 <= k + beta - a <= 3 - next_beta)
        for k in pair
    ]
    return Counter(tuple(sorted(t)) for t in product(*choices))


@cache
def transitions(plus, minus, beta, next_beta):
    return tuple(
        (u, v, a*b)
        for u, a in advance_pair(plus, beta, next_beta).items()
        for v, b in advance_pair(minus, beta, next_beta).items()
    )


@cache
def digit_sum(pair):
    return sum(1 << (2-k) for k in pair)


def energy(word, initial):
    pair = (initial, initial)
    dp = {(pair, pair, 0): 1}
    for beta, next_beta in zip(word, word[1:]):
        fresh = {}
        for (plus, minus, carry), count in dp.items():
            numerator = 3*carry + digit_sum(plus) - digit_sum(minus)
            if numerator % (1 << beta):
                continue
            next_carry = numerator >> beta
            for u, v, multiplicity in transitions(plus, minus, beta, next_beta):
                key = (u, v, next_carry)
                fresh[key] = fresh.get(key, 0) + multiplicity*count
        dp = fresh
    return sum(dp.values())


def brute(word, initial):
    paths = [(initial, 0)]
    clock = 0
    for beta, next_beta in zip(word, word[1:]):
        paths = [(k + beta - a, 3*c + (1 << (clock + 2 - k)))
                 for k, c in paths for a in (1, 2) if 0 <= k+beta-a <= 3-next_beta]
        clock += beta
    mod = 1 << clock
    pairs = Counter((a+b) % mod for _, a in paths for _, b in paths)
    return sum(v*v for v in pairs.values())


def check(steps):
    ws = schedules(steps)
    maxima = {}
    controls = 0
    for word in ws:
        clock = sum(word[:-1])
        for initial in range(4-word[0]):
            e = energy(word, initial)
            if steps <= 8:
                if e != brute(word, initial):
                    raise ArithmeticError((word, initial, e))
                controls += 1
            if e > maxima.get(clock, (0,))[0]:
                maxima[clock] = (e, initial, ''.join(map(str,word)))
    if steps == 64 and any(e**20 >= 2**(23*h) for h,(e,_,_) in maxima.items()):
        raise ArithmeticError('64-step modular fourth-energy rate')
    return {
        'odd_steps': steps, 'schedules': len(ws), 'independent_brute_checks': controls,
        'maxima_by_native_clock': {str(h): {'energy': e, 'initial_layer': k, 'schedule': w,
                                               'display_exponent': log2(e)/h}
                                   for h,(e,k,w) in sorted(maxima.items())}
    }


if __name__ == '__main__':
    print(json.dumps([check(int(v)) for v in sys.argv[1:]], indent=2))
