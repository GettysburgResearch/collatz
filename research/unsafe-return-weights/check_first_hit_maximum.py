"""Compute exact initial terms of the cycle-independent finite escape test."""

from fractions import Fraction

from check_sinai_norm import advance_density


def first_return(source, horizon):
    state = source
    total_exponent = 0
    for depth in range(1, horizon + 1):
        expanded = 3 * state + 1
        exponent = (expanded & -expanded).bit_length() - 1
        state = expanded >> exponent
        total_exponent += exponent
        if state == source:
            return depth, Fraction(3**depth, 2**total_exponent)
    return None


def first_hit_mass(levels, depth, target, cycle):
    level = levels[depth]
    mass = level[target % len(level)]
    if cycle is not None:
        period, multiplier = cycle
        if period <= depth:
            previous = levels[depth - period]
            mass -= multiplier * previous[target % len(previous)]
    if mass < 0:
        raise AssertionError((depth, target, mass))
    return mass


def main():
    levels = [[Fraction(1)]]
    for depth in range(5):
        levels.append(advance_density(levels[-1]))
        maximum = Fraction(-1)
        maximizers = []
        for target in range(1, 3 ** (depth + 1) + 1, 2):
            if target % 3 == 0:
                continue
            cycle = first_return(target, depth + 1)
            lower = first_hit_mass(levels, depth, target, cycle)
            upper = first_hit_mass(levels, depth + 1, target, cycle)
            value = abs(upper - lower) / target
            if value > maximum:
                maximum = value
                maximizers = [target]
            elif value == maximum:
                maximizers.append(target)
        print(f"q={depth}, M={maximum}, maximizing targets={maximizers}")


if __name__ == "__main__":
    main()
