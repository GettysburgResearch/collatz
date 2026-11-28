"""Finite exact checks for the single-defect profinite simulation."""

from collections import Counter, deque
from fractions import Fraction
from itertools import product


def require(condition, info):
    if not condition:
        raise ArithmeticError(info)


def advance(value, letter, modulus=None):
    numerator = (3 * value + 1) if letter else value
    if modulus is not None:
        return numerator * pow(2, -1, modulus) % modulus
    return numerator / 2


def steer(start, end, modulus):
    parent = {start: None}
    queue = deque([start])
    while end not in parent:
        require(queue, (start, end, modulus))
        u = queue.popleft()
        for bit in range(2):
            v = advance(u, bit, modulus)
            if v not in parent:
                parent[v] = (u, bit)
                queue.append(v)
    tail = []
    v = end
    while parent[v] is not None:
        v, bit = parent[v]
        tail.append(bit)
    require(len(tail) < modulus, (start, end, modulus, len(tail)))
    return list(reversed(tail))


def steer_mixed(start, end, trits, prime_to_six):
    three_power = 3**trits
    inverse_two = pow(2, -1, three_power)
    value = three_power - 1
    for even_count in range(2*three_power//3):
        if value == end % three_power:
            break
        value = value * inverse_two % three_power
    else:
        raise ArithmeticError(("nonunit target", end, three_power))
    suffix = [1]*trits + [0]*even_count
    pullback = end % prime_to_six
    for bit in reversed(suffix):
        pullback = (2*pullback-bit) * (
            pow(3, -1, prime_to_six) if bit else 1) % prime_to_six
    return steer(start % prime_to_six,pullback,prime_to_six) + suffix


def check_mixed_moduli():
    cases = 0
    for trits, m in ((1,1),(2,5),(3,7)):
        whole = 3**trits*m
        starts = range(whole) if whole <= 50 else range(0,whole,7)
        for first, last in product(starts,range(whole)):
            if last % 3 == 0:
                continue
            word = steer_mixed(first,last,trits,m)
            state = first
            for bit in word:
                state = advance(state,bit,whole)
            require(state == last,(first,last,whole))
            require(len(word) <= m-1+trits+2*3**(trits-1), len(word))
            cases += 1
    return cases


def cycle(anchor):
    states = []
    x = anchor
    while x not in states:
        states.append(x)
        x = (3*x + 1 if x % 2 else x) // 2
    require(x == anchor, anchor)
    return states


def script_for_law(modulus, three_digits, binary_digits, runs):
    bits, predictions = [], {}
    state = 0
    for anchor, copies in runs:
        route = steer(state, anchor % modulus, modulus)
        bits.extend(route)
        phases = cycle(anchor)
        offset = len(bits)
        length = copies*len(phases)
        for j in range(three_digits*len(phases), length-binary_digits):
            predictions[offset+j] = phases[j % len(phases)]
        bits.extend([y % 2 for y in phases]*copies)
        state = anchor % modulus
    bits.extend(steer(state, 0, modulus))
    return bits, predictions


def parity_residue(bits):
    # Each prefix solution is r mod 2^j; flipping the next source bit
    # adds the current odd affine slope to the current endpoint.
    r, slope, x = 0, 1, 0
    for j, bit in enumerate(bits):
        if x % 2 != bit:
            r += 2**j
            x += slope
        if bit:
            x, slope = (3*x+1)//2, 3*slope
        else:
            x = x // 2
    return r


def check_stage(modulus, runs):
    k2, k3 = 5, 3
    word, expected = script_for_law(modulus, k3, k2, runs)
    s = sum(word)
    require(3**s > 2**len(word), "finite stage lacks its growth reserve")
    source = 7
    true_prefix = []
    y = source
    for _ in range(6):
        true_prefix.append(y % 2)
        y = (3*y+1 if y % 2 else y)//2
    wrong = 1 - y % 2
    z = advance(Fraction(y), wrong)
    require(z.denominator == 2, z)
    initial = true_prefix+[wrong]+steer(
        z.numerator*pow(z.denominator,-1,modulus)%modulus, 0, modulus)
    script = initial + word*2 + [0]*k2
    sample_length = len(script) - k2
    initial_2 = parity_residue(script)
    odd_modulus = modulus*3**k3
    binary_modulus = 2**len(script)
    n = initial_2 + binary_modulus * (
        (source-initial_2)*pow(binary_modulus,-1,odd_modulus)%odd_modulus)
    n += binary_modulus*odd_modulus

    q = Fraction(source)
    seen = set()
    for i, bit in enumerate(script):
        require(n % 2 == bit, (i,n,bit))
        if i < sample_length:
            require(n not in seen, (i,n))
            seen.add(n)
        if i >= len(true_prefix)+1:
            require(q.denominator == 2**(i-len(true_prefix)), (i,q))
        require((q.numerator-n*q.denominator) % odd_modulus == 0, i)
        j = i - len(initial)
        if 0 <= j < 2*len(word) and j%len(word) in expected:
            anchor = expected[j%len(word)]
            require((n-anchor) % (2**k2*odd_modulus) == 0, (i,anchor))
        n = (3*n+1 if bit else n)//2
        q = advance(q,bit)
    return Counter({"stage words":1, "guarded joint phase checks":2*len(expected),
                    "whole simple ordinary prefix dates":sample_length,
                    "single-defect rational steps":len(script)-len(true_prefix)-1})


if __name__ == "__main__":
    receipt = Counter()
    for q in (5,7,25,35,49):
        for a,b in product(range(q),repeat=2):
            current = a
            for bit in steer(a,b,q):
                current = advance(current,bit,q)
            require(current==b,(a,b,q))
            receipt["all-pair residue routes"] += 1
    for q in (5,35,175):
        for runs in (((-1,127),), ((1,123),(-1,135),(-5,33))):
            receipt.update(check_stage(q,runs))
    receipt["mixed-modulus unit transports"] = check_mixed_moduli()
    for name, count in sorted(receipt.items()):
        print(f"{name}: {count}")
