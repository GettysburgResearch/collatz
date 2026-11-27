"""Exact controls for the signed cycle and denominator-uniform charge proofs."""

from fractions import Fraction
from itertools import product


def require(truth, message):
    if not truth:
        raise ValueError(message)


def primitive_necklaces(length):
    for word in product((0, 1), repeat=length):
        rotations = {word[i:] + word[:i] for i in range(length)}
        if len(rotations) == length and min(rotations) == word and any(word):
            yield word


def trace(word):
    numerator = 0
    for i, odd in enumerate(word):
        if odd:
            numerator = 3 * numerator + (1 << i)
    root = Fraction(numerator, (1 << len(word)) - 3**sum(word))
    value = root
    states = []
    for odd in word:
        require(value.numerator % 2 == odd and value.denominator == root.denominator,
                "native signed parity or denominator mismatch")
        states.append(abs(value))
        value = (3 * value + 1) / 2 if odd else value / 2
    require(value == root and len(set(states)) == len(word), "least-period failure")
    if root < 0:
        require(min(states) >= 1, "reflected real minimum below one")
    return states, root.denominator


def rational_charges(word, states, coefficient):
    length = len(word)
    reciprocals = [1 / state for state in states]
    majorants = [odd * r / 2 for odd, r in zip(word, reciprocals)]
    increments = [majorants[i] + coefficient * (reciprocals[i] - reciprocals[(i + 1) % length])
                  for i in range(length)]
    relative_minima = []
    for i in range(length):
        total = minimum = Fraction(0)
        for j in range(length):
            total += increments[(i + j) % length]
            minimum = min(minimum, total)
        relative_minima.append(minimum)
    active = []
    total_charge = Fraction(0)
    for i in range(length):
        charge = increments[i] + relative_minima[(i + 1) % length] - relative_minima[i]
        require(charge >= 0, "negative future-minimum charge")
        total_charge += charge
        if charge > 0:
            require(charge <= increments[i] <= (coefficient + Fraction(1, 2)) * reciprocals[i],
                    "pointwise charge upper bound")
            active.append(i)
    require(total_charge == sum(majorants), "lost cyclic charge")
    return active


def audit_charged_prefixes(word, states, floor, coefficient):
    active = rational_charges(word, states, coefficient)
    growth_denom = 1 + Fraction(1, 2 * coefficient)
    growth_upper = 3 + 1 / floor
    length = len(word)
    tests = 0
    for i in active:
        reciprocal_factor = Fraction(1)
        odd_factor = Fraction(1)
        for j in range(1, 2 * length + 1):
            reciprocal_factor *= growth_denom
            if word[(i + j - 1) % length]:
                odd_factor *= growth_upper
            ratio = states[(i + j) % length] / states[i]
            require(1 <= ratio * reciprocal_factor, "Gronwall prefix loss too large")
            require((1 << j) * ratio <= odd_factor, "prefix odd ratio upper")
            require((1 << j) <= odd_factor * reciprocal_factor, "odd prefix cutoff")
            tests += 1
    return len(active), tests


def audit_ascent(word, states, denominator, level):
    if min(states) >= level or max(states) < 2 * level:
        return 0
    maximum = max(states)
    length = len(word)
    peak_index = states.index(maximum)
    before = peak_index
    steps = 0
    while states[(before - 1) % length] >= level:
        before = (before - 1) % length
        steps += 1
    require(level <= states[before] <= 2 * level and maximum >= Fraction(length, denominator),
            "missing last crossing or denominator packing")
    sigma = 3 + 1 / level
    require(maximum <= 2 * level * (sigma / 2)**steps, "crossing horizon")
    odd_factor = Fraction(1)
    for j in range(1, steps + 1):
        if word[(before + j - 1) % length]:
            odd_factor *= sigma
        require(states[(before + j) % length] >= level and (1 << (j-1)) <= odd_factor,
                "rare ascent prefix test")
    return 1


def scalar_controls():
    require(31**24 * 2 < 32**24, "24-step contraction")
    # (1+sqrt(3))/(2sqrt(2)) < 31/32 follows by squaring twice.
    require((8 * 31**2 - 4 * 32**2)**2 > 12 * 32**4, "square-root drift")
    require(Fraction(2**23, 6) >= 192**2, "explicit large-state cutoff")
    rate = Fraction(1, 2**30)
    tiny = Fraction(1, 10**12)
    require((Fraction(1, 2) + tiny) * (2 - rate / 50) + tiny < 1,
            "explicit critical exponent margin")
    require(3**6309 < 2**10000, "critical odd proportion > 6309/10000")
    require(10000**10000 < 2**9500 * 6309**6309 * 3691**3691, "entropy below 19/20")
    require(5**250 < 2**245 * 3**150 * 2**100, "elementary state-count slack")


if __name__ == "__main__":
    scalar_controls()
    necklaces = positive = negative = active = prefixes = crossings = 0
    observed = set()
    for length in range(1, 12):
        for word in primitive_necklaces(length):
            states, denominator = trace(word)
            require((denominator, word) not in observed, "duplicate cycle")
            observed.add((denominator, word))
            necklaces += 1
            if 2**length > 3**sum(word):
                positive += 1
            else:
                negative += 1
            minimum = min(states)
            if minimum >= 1:
                count, scans = audit_charged_prefixes(word, states, minimum, 16)
                active += count
                prefixes += scans
            for level in (Fraction(1), Fraction(2), Fraction(4)):
                crossings += audit_ascent(word, states, denominator, level)
    print(f"PASS: {necklaces} least-period signed necklaces ({positive} positive, {negative} negative), "
          f"{active} rational charged phases, {prefixes} exact prefix inequalities, "
          f"{crossings} last-ascent witnesses, 7 scalar comparisons")
