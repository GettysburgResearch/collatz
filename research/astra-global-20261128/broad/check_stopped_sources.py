"""Exact small stopped-cell regeneration and signed rational adversarial checks."""

from collections import Counter
from fractions import Fraction
from functools import cache

from check_gap_coding import numerator, require, step


def trit_repair(x, t):
    return next(e for e in range(1, 7) if (x * 2**e - 1) % 9 == 3 * t)


@cache
def corridor(x, n, credit):
    if n == 0:
        return ()
    for e in range(1, (credit + 5) // 3 + 1):
        z, rem = divmod(x * 2**e - 1, 3)
        if rem or z % 3 == 0:
            continue
        suffix = corridor(z % 3**n, n - 1, credit + 5 - 3 * e)
        if suffix is not None:
            return (e,) + suffix
    return None


def stopped_checks(N=3):
    width = N + 2
    m = 3**width
    phases = returns = cells = 0
    for trit in (1, 2):
        seen = set()
        departures, arrivals, first, last, actions = (Counter() for _ in range(5))
        tail_sum = length_sum = 0
        for r in range(trit, m, 3):
            w = ()
            for j in range(1, N + 1):
                candidate = corridor(r % 3 ** (j + 1), j, 3)
                if candidate is None:
                    break
                w = candidate
            j = len(w)
            d = 3 ** (j + 2)
            cell = r % d
            if (j, cell) in seen:
                continue
            seen.add((j, cell))
            cells += 1
            last_before_repair = cell
            for e in w:
                last_before_repair = step(last_before_repair, e)
            full = w + (trit_repair(last_before_repair, trit),)
            require(3 * sum(full) <= 5 * j + 3 + 18, 'stopped cost')
            weight = 3 ** (N - j)
            length_sum += weight * len(full)
            for lift in range(m // 3):
                x = cell + d * lift
                if x % 2 == 0:
                    x += d * (m // 3)
                first[x % m] += weight
                for e in full:
                    departures[x % m] += weight
                    actions[x % m, e] += weight
                    x = step(x, e)
                    require(x % 2 == 1 and x > 0, 'ordinary positive odd lift')
                    arrivals[x % m] += weight
                    phases += 1
                last[x % m] += weight
                returns += 1
        for j in range(N + 1):
            tail_sum += sum(corridor(r % 3 ** (j + 1), j, 3) is not None
                            for r in range(trit, m, 3))
        require(tail_sum == length_sum, 'finite stopping tail sum')
        require(first == last and arrivals == departures, 'variable-depth block flow')
        fresh = Counter()
        for (x, e), mass in actions.items():
            for t in range(3):
                fresh[step(x + t * m, e) % m] += mass
        require(fresh == Counter({x: 3 * v for x, v in departures.items()}), 'stationary rolling law')
    return cells, phases, returns


def residue(z, m):
    return z.numerator * pow(z.denominator, -1, m) % m


def smaller_legal(x, prefer_five=False):
    if prefer_five and x % 9 == 8:
        return 5
    return next(e for e in range(1, 5) if (2**e * x - 1) % 9 in (3, 6))


def labels(x, count):
    word = []
    for _ in range(count):
        e = smaller_legal(x)
        word.append(e)
        x = step(x, e)
    return word


def trap_checks():
    trajectories = phases = 0
    for W in (2, 3, 4):
        m = 3**W
        marker = [5] + labels(-11, W - 1)
        for s in range(1, m):
            if s % 3 == 0:
                continue
            w = labels(s, W) + marker + [1] * (30 * W)
            D = 3**len(w) - 2**sum(w)
            source = Fraction(-numerator(w), D)
            require(residue(source,m) == s and D > 0, 'row period')
            z = source
            cycle = {}
            for j, e in enumerate(w):
                if j in (W, 2 * W):
                    require(residue(z,m) == m - 1, 'indistinguishable marker')
                if z in cycle:
                    require(cycle[z] == e, 'inconsistent rational cycle')
                cycle[z] = e
                z = (2**e * z - 1) / 3
                phases += 1
            require(z == source, 'cycle did not return')
            for prefer_five in (False, True):
                seen = set()
                z = source
                exited = False
                for _ in range(2 * len(w)):
                    require(z not in seen and z < 0 and D % z.denominator == 0, 'baseline lattice or distinctness')
                    seen.add(z)
                    e = smaller_legal(residue(z,m), prefer_five)
                    next_z = (2**e * z - 1) / 3
                    if exited:
                        require(next_z not in cycle, 're-entry')
                    elif next_z not in cycle:
                        exited = True
                    z = next_z
                require(exited, 'selector completed incompatible lap')
                trajectories += 1
    return trajectories, phases


if __name__ == '__main__':
    print('stopping cells, executed gap phases, terminal lifts', *stopped_checks())
    print('strict-window baseline trajectories, signed periodic phases', *trap_checks())
