"""Exact parity carries and ordinary lifts for the two-gap merger theorems."""

from itertools import product


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def shortcut(x):
    return (3*x + 1)//2 if x % 2 else x//2


def orbit(x, time):
    bits = []
    for _ in range(time):
        bits.append(x % 2)
        x = shortcut(x)
    return x, bits


def source_data(word):
    clock, odds, carry = 0, 0, 0
    for letter in word:
        require(letter in "LP", "unknown source letter")
        block_clock, offset = (3, 7) if letter == "L" else (5, 5)
        carry = 9*carry + (offset << clock)
        clock += block_clock
        odds += 2
    return clock, odds, carry


def parity_word(clock, odds, carry):
    if not 0 <= odds <= clock:
        return None
    modulus = 1 << clock
    slope = 3**odds
    witness = -carry*pow(slope, -1, modulus) % modulus
    value, bits = orbit(witness, clock)
    if sum(bits) != odds or modulus*value != slope*witness + carry:
        return None
    return "".join(map(str, bits))


def half(word):
    clock, odds, carry = source_data(word)
    return parity_word(clock-1, odds, (carry + 7*3**odds)//2)


def ramp(word):
    clock, odds, carry = source_data(word)
    result = {}
    for target_odds in range(clock):
        target_carry = (carry - 7*3**odds)//2 + 3**target_odds
        bits = parity_word(clock-1, target_odds, target_carry)
        if bits is not None:
            result[odds-target_odds] = bits
    return result


def actual_start(word):
    # Solve with the final odd condition. The canonical representative may be zero.
    clock, odds, carry = source_data(word)
    modulus = 2 << clock
    q = ((1 << clock)-carry)*pow(3**odds, -1, modulus) % modulus
    return q or modulus


def check():
    accepted = {"PPP": ("half", 0), "PPLP": ("half", 0),
                "PLPP": ("ramp", 1), "PLPL": ("ramp", 1),
                "PLLL": ("ramp", 3), "PPLLP": ("ramp", 1)}
    for word, (family, exponent) in accepted.items():
        require(half(word) is not None if family == "half" else exponent in ramp(word), word)
    residual = {"P" + "".join(w) for w in product("LP", repeat=4)
                if not any(("P" + "".join(w)).startswith(p) for p in accepted)}
    require(residual == {"PPLLL", "PLLPP", "PLLPL"}, "residual prefix language")
    for w in residual:
        for j in range(1, len(w)+1):
            require(not half(w[:j]) and not ramp(w[:j]), "unexpected additional acceptance")

    # The signed 11-cycle makes s >= 66 impossible by a negative odd count
    # deficit too large to recover in the final five clocks.
    center, bits = orbit(-25, 33)
    require(center == -25 and sum(bits) == 21, "signed periodicity")
    require(max(1 + sum(orbit(-25, 3*s)[1])-2*s for s in range(11)) == 2,
            "signed exponent bound")
    require(all(half("P" + "L"*s + "P") is None for s in range(66)),
            "isolated half-pair boundary")
    require(ramp("PLLL") == {4: "0010001001100", 3: "0110001001100"}, "ramp endpoint")
    transitions = [
        ("L", (3, -4), (9, -19)), ("P", (9, -19), (3, -2)),
        ("L", (3, -2), (3, -4)), ("P", (3, -4), (3, -1)),
        ("P", (3, -1), (1, 0)), ("L", (3, -1), (1, -1)),
        ("P", (1, -1), (1, 0)),
    ]
    for letter, (ain, bin_), (aout, bout) in transitions:
        clock, odds, carry = source_data(letter)
        base = actual_start(letter)
        for q in (base, base + (2 << clock)):
            y = ain*q + bin_
            qnext = (3**odds*q + carry) >> clock
            require(orbit(y, clock)[0] == aout*qnext + bout, "loop identity")
    controls = 0
    for r in range(3, 32):
        for word, (family, exponent) in accepted.items():
            entire = "L"*r + word
            a, p, c = source_data(entire)
            start = actual_start(entire)
            for q in (start, start + (2 << a)):
                end = (3**p*q + c) >> a
                actual, _ = orbit(q, a)
                require(actual == end, "raw ordinary realization")
                if family == "half":
                    m = (q-7)//2
                    clocks = a-1
                else:
                    m = ((q+7) >> (r+1-exponent))-1
                    clocks = 2*r + exponent + source_data(word)[0]-1
                require(0 < m < min(q, (3*q+1)//4), "source-size inequality")
                require(orbit(m, clocks)[0] == end, "ordinary merger")
                controls += 1
    for s in (6, 7):
        for r in range(24):
            word = "L"*r + "PP" + "L"*s + "PLLL"
            a, p, c = source_data(word)
            q = actual_start(word)
            m = (q-7)//2
            end = (3**p*q+c) >> a
            require(orbit(m, a-1)[0] == end, "pair resonance")
            controls += 1
    print("Unresolved five-letter prefixes:", ", ".join(sorted(residual)))
    print("Signed-cycle isolated-pair base cases: 66")
    print("Ordinary endpoint controls:", controls)


if __name__ == "__main__":
    check()
