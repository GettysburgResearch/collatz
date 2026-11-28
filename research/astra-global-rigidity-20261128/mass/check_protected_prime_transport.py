"""Finite exact checks for the protected outside-prime transport examples."""

from math import gcd, lcm, prod


def check(condition, message):
    if not condition:
        raise RuntimeError(message)


def shortcut(n):
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def verify(t, n, outside, all_coprime=False):
    cores = []
    start = 8**t * n - 5
    state = start
    for i in range(t + 1):
        expected = 9**i * 8**(t - i) * n - 5
        check(state == expected and (state + 1) % 8 == 4, 'ramp start')
        core = (state + 1) // 4
        check(gcd(core, outside) == 1, 'prime support')
        if cores:
            check(8 * core == 9 * cores[-1] + 1, 'adjacent recurrence')
        if all_coprime:
            check(all(gcd(z, core) == 1 for z in cores), 'pairwise gcd')
        cores.append(core)
        if i < t:
            for parity in (1, 1, 0):
                check(state % 2 == parity and state >= start, 'protected word')
                state = shortcut(state)
    repeated = prod(cores) // lcm(*cores)
    differences = prod(9**k - 8**k for k in range(1, t + 1))
    check(differences % repeated == 0, 'least-common-multiple certificate')


def main():
    outside = 2 * 3 * 5 * 17
    step = 24 * 5 * 17
    for t in range(1, 27):
        for k in (1, 2, 3, 11, 37):
            verify(t, step * k, outside)
    for t in range(1, 13):
        differences = prod(9**k - 8**k for k in range(1, t + 1))
        verify(t, step * differences, outside, all_coprime=True)
    print('130 ordinary blocks and 12 mutually coprime constructions passed')


if __name__ == '__main__':
    main()
