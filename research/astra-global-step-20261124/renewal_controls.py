"""Exact controls for two persistent ordinary shadows, including shifted cylinders."""

from itertools import product


def require(condition, description):
    if not condition:
        raise ArithmeticError(description)


def shortcut(x):
    return (3*x + 1)//2 if x % 2 else x//2


def trajectory(x, length):
    bits = []
    for _ in range(length):
        bits.append(x % 2)
        x = shortcut(x)
    return x, bits


def normalized_word(word):
    width, scale, carry = 0, 1, 0
    for letter in word:
        require(letter in 'LP', 'letter')
        extra, injection = (3, 0) if letter == 'L' else (5, 83)
        carry = 9*carry + (injection << width)
        scale *= 9
        width += extra
    return width, scale, carry


# x=(q+7)/2. Modes give x−anchor.
TRANSITIONS = [
    ('PPLLLP' + 'L'*5, 10, 7),
    ('PPLLLLP' + 'L'*4, 10, 7),
    ('PLLPPLPP' + 'L'*9, 7, 10),
    ('PLLPLPP' + 'L'*6, 7, 7),
    ('PLLPLLPLLPP' + 'L'*9, 10, 10),
]


def replay(word, divisor, multiplier, initial_anchor, terminal_anchor):
    clocks, scale, carry = normalized_word(word)
    modulus = 1 << clocks
    require(carry % divisor == 0, 'integral coarse carry')
    carry //= divisor
    base = -carry*pow(scale, -1, modulus) % modulus
    sample = base if multiplier*base >= initial_anchor else base + 2*modulus
    checks = 0
    for t in (0, 1, 2, 33, 1000):
        source = sample + t*modulus
        endpoint, remainder = divmod(scale*source+carry, modulus)
        require(not remainder, 'ordinary endpoint')
        q = 2*divisor*source - 7
        original = q
        for letter in word:
            for gap in ((2, 1) if letter == 'L' else (1, 4)):
                n = 3*original+1
                require((n & -n) == (1 << gap), 'literal odd gap')
                original = n >> gap
        require(original == 2*divisor*endpoint-7, 'original endpoint')
        target = multiplier*source-initial_anchor
        output, bits = trajectory(target, clocks)
        require(3**sum(bits) == scale, 'target odd count')
        require(output == multiplier*endpoint-terminal_anchor, 'target endpoint')
        require(0 < target < min(q, (3*q+1)//4), 'both source floors')
        checks += 1
    return checks


def main():
    total = sum(replay(w, 1, 1, a, b) for w, a, b in TRANSITIONS)
    total += sum(replay('L', 1, 1, a, a) for a in (7, 10))
    for w in ('L', 'LLLPL', 'LLLPPLL'):
        total += replay(w, 128, 157, 5, 5)
    for first, second in product(('LLLPL', 'LLLPPLL'), repeat=2):
        total += replay(first+'L'*(2+len(first))+second, 128, 157, 5, 5)
    print('Exact ordinary cylinder comparisons:', total)
    print('Two-state core transitions:', len(TRANSITIONS))
    print('Singleton/doublet ordered-pair controls:', 4)


if __name__ == '__main__':
    main()
