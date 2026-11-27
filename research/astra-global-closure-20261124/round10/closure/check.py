"""Independent ordinary path, backward-tree and coefficient checks. No dependencies."""
from collections import defaultdict
from itertools import product
from math import gcd


def require(condition, context):
    if not condition:
        raise RuntimeError(str(context))


def step(n):
    return (3 * n + 1) // 2 if n % 2 else n // 2


def run(n, t):
    for _ in range(t):
        n = step(n)
    return n


def coefficient(word):
    count = carry = 0
    for i, bit in enumerate(word):
        if bit:
            count += 1
            carry = 3 * carry + 2**i
    return count, carry


def in_cone(n, w, r, free_twos=False):
    if free_twos:
        while n % 2 == 0:
            n //= 2
    e = 0
    while n % 3 == 0:
        n //= 3
        e += 1
    return n < w or (n == w and e < r)


def inverse_meeting(x, w, r, H, free_twos=False):
    for _ in range(H + 1):
        layer = {x}
        for clock in range(H + 1):
            if any(in_cone(z, w, r, free_twos) for z in layer):
                return True
            if clock < H:
                layer = {2 * z for z in layer} | {
                    (2 * z - 1) // 3 for z in layer if z % 3 == 2
                }
        x = step(x)
    return False


def literal_class(H, shift):
    r, m, e = 2 * H, H + 1, 5 * H + 2
    u, v = 2 ** (e + 1), 3 ** (r + 1)
    lower = pow(3**m, -1, u) * (1 + 2**e) % u
    upper = pow(2**m, -1, v) * (1 + 3**r) % v
    a = lower + u * (((upper - lower) * pow(u, -1, v)) % v + v * shift)
    w, wr = divmod(2**m * a - 1, 3**r)
    b, br = divmod(3**m * a - 1, 2**e)
    x = 3**r * w
    require(wr == br == 0 and gcd(w, 6) == 1 and a % 2 and b % 2, (H, shift))
    require(run(x, m + e) == b and 0 < b < w, (H, shift, 'return'))
    require(not inverse_meeting(x, w, r, H, True), (H, shift, 'short clocks'))
    return w, a, b


def main():
    fibers = []
    for h in range(9):
        heaviest = defaultdict(int)
        for word in product((0, 1), repeat=h):
            k, c = coefficient(word)
            heaviest[c] = max(heaviest[c], k)
        fibers.append(heaviest)
    tested = positives = 0
    for H in range(1, 9):
        for r in (2 * H, 2 * H + 1):
            for w in range(1, 130):
                if gcd(w, 6) != 1:
                    continue
                x = 3**r * w
                u, word, detected = x, [], False
                for f in range(1, H + 1):
                    word.append(u % 2)
                    u = step(u)
                    k, c = coefficient(word)
                    detected |= fibers[f][c] > k
                direct = inverse_meeting(x, w, r, H)
                require(direct == detected, (H, r, w, detected))
                tested += 1
                positives += int(detected)
    require(coefficient((1, 0, 0, 0, 1)) == (2, 19), 'light word')
    require(coefficient((1, 1, 1, 0, 0)) == (3, 19), 'heavy word')
    require(run(87381, 1) == 2**17 and inverse_meeting(87381, 9709, 2, 1, True)
            and not inverse_meeting(87381, 9709, 2, 1), 'free two on an even endpoint')
    for u in range(16):
        require(run(96 * u + 69, 5) == run(32 * u + 23, 5) == 27 * u + 20,
                ('five-step collision', u))
    for h, shift in product(range(1, 11), range(3)):
        literal_class(h, shift)
    print(f'{tested} short-cone comparisons, {positives} physical returns; 30 delayed CRT controls')
    print('H=1, shift=0: (w,a,b) =', literal_class(1, 0))


if __name__ == '__main__':
    main()
