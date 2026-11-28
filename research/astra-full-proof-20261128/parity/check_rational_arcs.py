"""Exact finite certificate in the positive-parameter rational-arc obstruction."""


PARAMETER = 191
CUTOFF = 80 * PARAMETER


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def step(x, b):
    return (3 * x + b) // 2 if x % 2 else x // 2


def follow(x, b, t):
    q = 0
    for _ in range(t):
        q += x % 2
        x = step(x, b)
    return x, q


def check_certificate():
    require(241**501 < 80**501 * 2**800 and 3**135 < 2**214,
            "strict upper-tail thresholds")
    b = PARAMETER
    subgroup = {pow(2, j, b) for j in range(95)}
    require(len(subgroup) == 95 and pow(2, 95, b) == 1 and 3 in subgroup,
            "wrong subgroup")
    require(all(2 * x % b in subgroup and 3 * x % b in subgroup for x in subgroup),
            "subgroup closure")
    cycle = []
    x = 961
    for _ in range(40):
        cycle.append(x)
        x = step(x, b)
    require(x == 961 and len(set(cycle)) == 40 and sum(x % 2 for x in cycle) == 25,
            "wrong positive control cycle")

    distance = {x: 0 for x in cycle}
    inputs = [x for x in range(1, CUTOFF + 1) if x % b in subgroup]
    for x in inputs:
        path = []
        y = x
        while y not in distance:
            require(len(path) <= 252, "failure to reach the specified cycle in bound")
            path.append(y)
            y = step(y, b)
        for z in reversed(path):
            distance[z] = 1 + distance[y]
            y = z
    require(len(inputs) == 7600 and max(distance[x] for x in inputs) == 252,
            "wrong coverage or maximal distance")
    require(all(d == 0 or distance[step(x, b)] + 1 == d for x, d in distance.items()),
            "invalid finite descent certificate")
    print("191 control: 95 unit residues, 7,600 sources through 15,280,"
          " maximal cycle distance 252, 25 odd departures per 40-step lap")


def check_binary_conjugacy():
    for depth in range(1, 12):
        modulus = 2**depth
        for n in range(1, modulus + 1):
            r = n * pow(PARAMETER, -1, modulus) % modulus
            require(follow(n, PARAMETER, depth)[1] == follow(r, 1, depth)[1],
                    "binary conjugacy")
    print("Positive-parameter/standard binary count conjugacy through depth 11: pass")


if __name__ == "__main__":
    check_certificate()
    check_binary_conjugacy()
