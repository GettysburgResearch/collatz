"""Check finite marked predecessors for a list of targets, with integer arithmetic."""

import json


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def step(value):
    return value // 2 if value % 2 == 0 else (3 * value + 1) // 2


def iterate(value, clocks):
    for _ in range(clocks):
        value = step(value)
    return value


def inv4(value):
    quotient, residue = divmod(value, 9)
    return 48 * quotient + {1: 4, 2: 8, 4: 20, 5: 26, 7: 37, 8: 40}[residue]


def row(target, numerator, denominator):
    # The exact bit length of 3^(Q^2) checks |Q log_2(3)-a|<=1/Q.
    q = denominator
    power = 3 ** (q * q)
    require(2 ** (numerator * q - 1) <= power <= 2 ** (numerator * q + 1), 'bad denominator')
    require((2 ** q) * target <= 3 ** q and target % 3 != 0, 'target or scale')
    initial = (2 ** q) * target
    lifted = initial
    hits = []
    for s in range(q + 1):
        e = q if ((2 ** q) * lifted) % 3 == 1 else q + 1
        n, remainder = divmod((2 ** e) * lifted - 1, 3)
        require(remainder == 0 and n % 2 == 1, 'source integrality')
        d = n.bit_length() - 1
        require(d + 1 <= 5 * e, 'valuation bound')
        if (d + 1) * (n - 2 ** d) <= 70 * (2 ** d):
            require(iterate(n, e) == lifted, 'long dropping prefix')
            require(iterate(lifted, 4 * s + q) == target, 'fixed target')
            require(lifted ** 5 <= 4 ** 5 * n ** 4, 'power descent')
            hits.append({'s': s, 'e': e, 'octave': d})
        lifted = inv4(lifted)
    require(bool(hits), 'missing marked source')
    return {'target': target, 'Q': q, 'row_marks': len(hits), 'example': hits[0]}


if __name__ == '__main__':
    receipts = [row(target, a, q) for a, q in [(84, 53), (485, 306), (1054, 665)]
                for target in [1, 5, 7, 31, 97, 127, 1024, 123457]]
    print(json.dumps(receipts, indent=2))
