"""Compare streaming odd and even edge tests with the actual shortcut identities."""

from itertools import product


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def end_state(transitions, state, digits):
    for digit in digits:
        state = transitions[state][digit]
    return state


def bits(n, lsb):
    word = [int(bit) for bit in bin(n)[2:]]
    return word[::-1] if lsb else word


def output(transitions, mask, n, lsb):
    return (mask >> end_state(transitions, 0, bits(n, lsb))) & 1


def msb_small(transitions, mask, n):
    state = end_state(transitions, 0, bits(n, False))
    return ((mask >> state) ^ (mask >> transitions[state][0])) & 1


def msb_large(transitions, mask, m):
    state, quotient_state, rem = 0, None, 0
    for bit in bits(m, False):
        state = transitions[state][bit]
        quotient_bit, rem = divmod(2 * rem + bit, 3)
        if quotient_state is not None or quotient_bit:
            if quotient_state is None:
                quotient_state = 0
            quotient_state = transitions[quotient_state][quotient_bit]
    if rem != 2:
        return 0
    quotient_state = transitions[0 if quotient_state is None else quotient_state][1]
    return ((mask >> state) ^ (mask >> quotient_state)) & 1


def lsb_small(transitions, mask, n):
    digits = bits(n, True)
    a = end_state(transitions, 0, digits)
    b = end_state(transitions, transitions[0][0], digits)
    return ((mask >> a) ^ (mask >> b)) & 1


def lsb_large(transitions, mask, n):
    a, b, carry = transitions[0][1], 0, 2
    for bit in bits(n, True):
        a = transitions[a][bit]
        carry, digit = divmod(3 * bit + carry, 2)
        b = transitions[b][digit]
    require(carry > 0, "canonical positive input ended with a zero carry")
    b = end_state(transitions, b, bits(carry, True))
    return ((mask >> a) ^ (mask >> b)) & 1


def run():
    machines = comparisons = 0
    for size in (1, 2):
        for entries in product(range(size), repeat=2 * size):
            transitions = [entries[2*i:2*i+2] for i in range(size)]
            for mask in range(1 << size):
                machines += 1
                for n in range(1, 257):
                    a = output(transitions, mask, n, False)
                    small = output(transitions, mask, 2*n, False)
                    large = output(transitions, mask, 2*n+1, False)
                    end = output(transitions, mask, 3*n+2, False)
                    require(msb_small(transitions, mask, n) == (a ^ small), "MSB even")
                    require(msb_large(transitions, mask, 3*n+2) == (large ^ end), "MSB odd")
                    require(msb_large(transitions, mask, 3*n+1) == 0, "MSB guard")
                    require(msb_large(transitions, mask, 3*n) == 0, "MSB guard")
                    x = output(transitions, mask, n, True)
                    y = output(transitions, mask, 2*n, True)
                    u = output(transitions, mask, 2*n+1, True)
                    v = output(transitions, mask, 3*n+2, True)
                    require(lsb_small(transitions, mask, n) == (x ^ y), "LSB even")
                    require(lsb_large(transitions, mask, n) == (u ^ v), "LSB odd")
                    comparisons += 6
    return machines, comparisons


if __name__ == "__main__":
    print("canonical DFAs and exact edge-test comparisons:", *run())
