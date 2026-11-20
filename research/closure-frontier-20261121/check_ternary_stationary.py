#!/usr/bin/env python3
"""Exact finite audit of TERNARY_STATIONARY_BOUNDARY.md.

Finite computations do not prove the all-depth L2 obstruction; its proof
is in the note. All checks remain enabled under optimized Python.
"""

from fractions import Fraction as F
from itertools import product
from math import comb
import json


def require(value, message):
    if not value:
        raise ValueError(message)


def image(x, bit, q):
    require(bit in (0, 1) and q >= 3 and q % 3 == 0, 'invalid affine input')
    return ((3*x+1) if bit else x)*pow(2, -1, q) % q


def stationary_lift(previous):
    require(previous and sum(previous) == 1 and min(previous) >= 0,
            'invalid input probability')
    q = 3*len(previous)
    order = 2*(q//3)
    orbit = []
    value = 1
    for _ in range(order):
        orbit.append(value)
        value = 2*value % q
    require(value == 1 and len(set(orbit)) == order, 'unit cycle')
    mu = {x: (previous[((2*x-1)//3) % len(previous)] if x % 3 == 2 else F(0))
          for x in orbit}
    value = sum((2**(order-j-1)*mu[x] for j, x in enumerate(orbit)), F(0))/(2**order-1)
    result = [F(0)]*q
    for x in orbit:
        result[x] = value
        value = 2*value-mu[x]
    require(value == result[1], 'cyclic recursion did not close')
    validate_probability(result)
    return result


def validate_probability(pi):
    q = len(pi)
    require(sum(pi) == 1 and min(pi) >= 0, 'invalid probability')
    pushed = [F(0)]*q
    for x, mass in enumerate(pi):
        for bit in (0, 1):
            pushed[image(x, bit, q)] += mass/2
    require(pi == pushed, 'stationarity residual')
    require(all((mass > 0) == (x % 3 != 0) for x, mass in enumerate(pi)), 'wrong support')


def independent_gaussian(q):
    # Solve the full K^T-I system, including transient states. No use of
    # stationary_lift, projective recursion, or the unit cycle formula.
    matrix = [[F(0) for _ in range(q+1)] for _ in range(q)]
    for x in range(q):
        matrix[x][x] -= 1
        for bit in (0, 1):
            matrix[image(x, bit, q)][x] += F(1, 2)
    matrix[-1] = [F(1)]*q + [F(1)]
    for col in range(q):
        pivot = next((r for r in range(col, q) if matrix[r][col]), None)
        require(pivot is not None, 'stationary linear system singular')
        matrix[col], matrix[pivot] = matrix[pivot], matrix[col]
        scale = matrix[col][col]
        matrix[col] = [v/scale for v in matrix[col]]
        for row in range(q):
            if row != col and matrix[row][col]:
                scale = matrix[row][col]
                matrix[row] = [a-scale*b for a,b in zip(matrix[row], matrix[col])]
    return [row[-1] for row in matrix]


def enclosure(value, digits=8):
    scale = 10**digits
    lower = value.numerator*scale//value.denominator
    return {'lower_numerator':lower, 'upper_numerator':lower+1, 'denominator':scale}


def levels(max_s=7):
    previous = [F(1)]
    previous_energy = F(1)
    rows = []
    saved = {}
    for s in range(1, max_s+1):
        pi = stationary_lift(previous)
        q = len(pi)
        require(q == 3**s, 'wrong modulus')
        projection = [sum(pi[a::len(previous)]) for a in range(len(previous))]
        require(projection == previous, 'projective consistency')
        energy = q*sum(x*x for x in pi)
        cross = (q//3)*sum((pi[2*x % q]*previous[((2*x-1)//3) % (q//3)]
                            for x in range(2, q, 3)), F(0))
        require(energy-previous_energy == 2*cross and cross > 0,
                'square norm identity')
        require(pi[-1] >= F(1, 2**s), 'negative fixed-point atom')
        require(max(pi) <= F(2, 3)**s, 'maximum atom bound')
        if s <= 3:
            require(pi == independent_gaussian(q), 'independent stationary solve mismatch')
        rows.append({'s':s, 'modulus':q, 'energy':enclosure(energy),
                     'energy_increment':enclosure(energy-previous_energy),
                     'negative_one_density':enclosure(q*pi[-1]),
                     'max_density':enclosure(q*max(pi)),
                     'positive_atoms':sum(x > 0 for x in pi)})
        saved[s] = pi
        previous, previous_energy = pi, energy
    return rows, saved


def coupling_checks():
    word_rows = []
    for s in range(1, 4):
        q, length = 3**s, 4*s
        synchronized = 0
        for bits in product((0, 1), repeat=length):
            if sum(bits) < s:
                continue
            endpoints = []
            for start in range(q):
                end = start
                for bit in bits:
                    end = image(end, bit, q)
                endpoints.append(end)
            require(len(set(endpoints)) == 1, 'coupling did not synchronize all states')
            synchronized += 1
        expected = 2**length-sum(comb(length, j) for j in range(s))
        require(synchronized == expected, 'synchronizing word census')
        word_rows.append({'s':s, 'words':2**length, 'synchronizing_words':synchronized,
                          'initial_states_each':q})
    for s in range(1, 65):
        failure = F(sum(comb(4*s, j) for j in range(s)), 2**(4*s))
        bound = F(1, 3)*F(16, 27)**s
        require(failure <= bound <= F(16, 81), 'Chernoff tail bound')
        require(F(1, 2)-F(16, 81) == F(49, 162), 'conductance constant')
    return {'all_word_audits':word_rows, 'exact_tail_depths':64}


def cut_checks(pi, s):
    q = len(pi)
    units = [x for x in range(q) if x % 3]
    count = 0
    minimum = None
    for mask in range(1 << len(units)):
        subset = {x for i,x in enumerate(units) if (mask >> i) & 1}
        mass = sum((pi[x] for x in subset), F(0))
        out = sum((pi[x]/2 for x in subset for bit in (0,1)
                   if image(x, bit, q) not in subset), F(0))
        inward = sum((pi[x]/2 for x in units if x not in subset for bit in (0,1)
                      if image(x, bit, q) in subset), F(0))
        require(out == inward, 'cut flow not balanced')
        require(2*mass*(1-mass) <= F(648*s,49)*(out+inward), 'Boolean coarea inequality')
        if 0 < mass <= F(1,2):
            ratio = out/mass
            require(ratio >= F(49,648*s), 'conductance lower bound')
            minimum = ratio if minimum is None else min(minimum,ratio)
        count += 1
    return {'s':s, 'unit_subsets':count, 'minimum_small_cut_ratio':str(minimum)}


def malformed_checks(saved):
    damaged = list(saved[2])
    damaged[1] += F(1,100)
    damaged[2] -= F(1,100)
    cases = [lambda:stationary_lift([F(2)]), lambda:validate_probability(damaged),
             lambda:image(1,2,9), lambda:image(1,0,8)]
    count = 0
    for case in cases:
        try:
            case()
        except ValueError:
            count += 1
        else:
            raise ValueError('malformed input was accepted')
    return count


def main():
    rows, saved = levels()
    report = {'status':'PASS',
              'scope':'Exact finite audits; TM5 is an all-depth written proof; no Collatz proof.',
              'stationary_levels':rows,
              'independent_full_linear_solves':[3,9,27],
              'coupling':coupling_checks(),
              'all_unit_subset_censuses':[cut_checks(saved[s],s) for s in (1,2)],
              'malformed_inputs_rejected':malformed_checks(saved),
              'tao_fine_scale_theorem_replayed':False}
    print(json.dumps(report,sort_keys=True,indent=2))


if __name__ == '__main__':
    main()
