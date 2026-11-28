"""Exact tests for the tilted cylinder action and the sparse even carry."""
from fractions import Fraction as F
import json


def require(condition, label):
    if not condition:
        raise ValueError(label)


def unit_classes(modulus):
    return [a for a in range(1, modulus) if a % 3]


def kernel(s, depth, values):
    mod = 3**depth
    period = 2*mod
    z = 1-s
    weights = [3*s*z**j/(1-z**period) for j in range(period)]
    out = {}
    for y in unit_classes(3*mod):
        total = F(0)
        reached = []
        power = 1
        for weight in weights:
            power = 2*power % (3*mod)
            value = (power*y-1) % (3*mod)
            if value % 3 == 0 and value % 9:
                parent = value//3
                total += weight*values[parent]
                reached.append(parent)
        require(sorted(reached) == unit_classes(mod), "complete legal parent period")
        out[y] = total
    return out


def mean(f):
    return sum(f.values(), F(0))/len(f)


def norm(f):
    return max(map(abs, f.values()))


def cylinder_checks():
    rows = 0
    differences = 0
    for s in (F(1, 4), F(1, 16), F(1, 125)):
        current = {y: F(1) for y in unit_classes(3)}
        prior = None
        for j in range(1, 5):
            extended = kernel(s, j, current)
            require(mean(extended) == 1, "unit Haar preservation")
            next_diff = {y: w-current[y % (3**j)] for y, w in extended.items()}
            require(mean(next_diff) == 0, "martingale cylinder increment")
            if prior is not None:
                require(norm(next_diff) <= 2*3**j*s*norm(prior), "tilt supremum contraction")
                differences += 1
            rows += len(extended)
            current, prior = extended, next_diff
    return rows, differences


def carry_checks():
    prefixes = 0
    for n in range(1, 1025):
        state = n
        times = []
        q = 0
        for t in range(1, 18):
            if state % 2:
                state = (3*state+1)//2
                q += 1
            else:
                times.append((t-1, q))
                state //= 2
            x0 = 3**q*(n+1)
            carries = [2**b * 3**(q-before) for b, before in times]
            require(x0 + sum(carries) == 2**t*(state+1), "shifted sparse carry identity")
            for i, val in enumerate(carries):
                b, _ = times[i]
                require(val*(n+1)*3**b == x0*3**i*2**b, "marked coordinate ratio")
            prefixes += 1
    return prefixes


if __name__ == "__main__":
    rows, differences = cylinder_checks()
    print(json.dumps({"cylinder_rows": rows, "uniform_norm_comparisons": differences,
                      "actual_sparse_carry_prefixes": carry_checks()}, indent=2))
