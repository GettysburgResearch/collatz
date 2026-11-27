"""Exact positive peak controls and complete earlier-Mersenne comparisons.

Run with Python 3 from any directory. The JSON report is written to stdout.
All assertion checks remain active under python -O.
"""
import json


def require(condition, description):
    if not condition:
        raise ValueError(description)


def step(x):
    return (3*x+1)//2 if x % 2 else x//2


def prefix(x, clock):
    odd = 0
    for _ in range(clock):
        odd += x % 2
        x = step(x)
    return x, odd


def until_one(x, budget):
    for h in range(budget + 1):
        yield x, h
        if x == 1:
            return
        x = step(x)
    raise ValueError("unverified first-hit budget")


def anchors():
    width = 1 << 64
    derivative = ((3**162-1)//8) % width
    for s in range(62):
        derivative = (derivative + (1 << (s+2))*derivative**2) % width
    require(derivative == 164232366001155405, "stabilized residue")
    first = [prefix(3**a-1, 89) for a in (11, 6)]
    require(first == [(1, 45), (2, 47)], "long initial phases")
    profiles = []
    for sign, h, endpoint, odds in [
        (1, 64, 2922489638071279607, (30, 33)),
        (-1, 62, 11724704031194517008, (27, 30)),
    ]:
        residue = sign*derivative % (1 << h)
        states = (1+3**13*residue, 2+3**10*residue)
        visits = [prefix(x, h) for x in states]
        require(visits == [(endpoint, odds[0]), (endpoint, odds[1])], "derivative trace")
        require(13+odds[0] == 10+odds[1], "derivative grades")
        profiles.append(dict(sign=sign, clock=h, residue=residue, sources=states,
                             endpoint=endpoint, odd=odds))
    endpoint = 206172918000360585496211725112706136396363302641
    odd = [prefix(3**a-1, 499) for a in (173, 164)]
    require(odd == [(endpoint, 241), (endpoint, 250)], "odd-base anchor")
    require(173+241 == 164+250, "odd-base grades")
    return dict(stable_derivative=derivative, clock_89=first, signs=profiles,
                odd_anchor=dict(exponents=[173, 164], clock=499, endpoint=endpoint,
                                odd=[241, 250]))


def record(j, expected):
    # A clock of -a means a native ascent site a steps before its peak.
    phases = {}
    y = (1 << j)-1
    for h in range(-j, 0):
        require(y % 2 == 1 and y not in phases, "native ascent")
        phases[y] = h
        y = step(y)
    require(y == 3**j-1, "native peak")
    floor = ((1 << (j+7))-271)//81
    odd = 0
    first_floor = None
    for y, h in until_one(y, 20000):
        require(y not in phases, "native simple trace through its first one")
        phases[y] = h
        if first_floor is None and 1024*y < 243*floor:
            first_floor = [h, odd]
        if y != 1:
            odd += y % 2
    native_charge = 2*(j+odd)-h
    max_charge = (-10**6, 0)
    best = None
    best_pair = None
    earliest_native = None
    for t in range(1, j):
        # Every site through the first 1 has an ordinary cutoff. The suffix
        # after 1 consists exactly of 1 and 2. Include the second explicitly.
        source = (1 << t)-1
        y = source
        first = None
        for l in range(-t, 0):
            if y in phases and first is None:
                first = (phases[y], l, y)
            y = step(y)
        require(y == 3**t-1, "earlier ascent")
        q = 0
        for y, l in until_one(y, 20000):
            if y in phases and first is None:
                first = (phases[y], l, y)
            if y != 1:
                q += y % 2
        require(first is not None, "earlier site at one")
        # Before its first repeated site the native trace is ordered. After
        # the first intersection any later native sites occur in that order,
        # except for the tail 1,2 cycle which is enumerated explicitly.
        candidates = (first, (phases[2], l+1, 2))
        for hn, hl, site in candidates:
            earliest_native = hn if earliest_native is None else min(earliest_native, hn)
            cost = max(0, hn, hl)
            if best is None or (cost, t, hn, hl) < (best, *best_pair[:3]):
                best = cost
                best_pair = (t, hn, hl, site)
        charge = 2*(t+q)-l
        require(charge != native_charge, "earlier equal compensated charge")
        max_charge = max(max_charge, (charge, t))
    data = dict(j=j, m=(j-11)//162, hit_one=[h, odd], charge=native_charge,
                earlier_max_charge=max_charge, first_subfloor=first_floor,
                first_native_clock=earliest_native, minimum_max_postpeak_clock=best,
                earliest_witness=best_pair)
    require((h, odd, native_charge, max_charge[0], *first_floor, earliest_native, best)
            == expected, "earlier census discrepancy at j=" + str(j))
    return data


def main():
    print(json.dumps(dict(anchors=anchors(), all_earlier=[
        record(11, (89, 45, 23, 16, 54, 29, 58, 58)),
        record(983, (7803, 3940, 2043, 1791, 2636, 1299, 7726, 7726)),
        record(2117, (16934, 8567, 4434, 4078, 5941, 2966, 16913, 16913)),
    ]), indent=2))


if __name__ == "__main__":
    main()
