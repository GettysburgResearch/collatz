"""Replay the ordinary upper orbit and the certified lower power-of-two hit."""


def require(condition, message):
    if not condition:
        raise ValueError(message)


def step(n):
    return (3 * n + 1) // 2 if n % 2 else n // 2


def construct(blocks, height):
    depth = 5 * (blocks + 1)
    period = 2**depth
    residue = -65 * pow(147, -1, period) % period
    endpoint = residue
    ones = 0
    for _ in range(depth):
        ones += endpoint % 2
        endpoint = step(endpoint)

    ternary = 3**height
    t0 = (3 ** (height - 1) - residue) * pow(period, -1, ternary) % ternary
    unit = endpoint + 3**ones * t0
    modulus = 3 ** (ones + height)

    # Lift the discrete logarithm from modulus 3 by one ternary digit.
    exponent = 0 if unit % 3 == 1 else 1
    order = 2
    power = 3
    while power < modulus:
        power *= 3
        exponent = next(
            e for e in (exponent, exponent + order, exponent + 2 * order)
            if pow(2, e, power) == unit % power
        )
        order *= 3
    while exponent < unit.bit_length():
        exponent += order

    q = residue + period * ((2**exponent - endpoint) // 3**ones)
    require(q % ternary == 3 ** (height - 1), "source ternary valuation")
    require((147 * q + 65) % period == 0, "source binary class")

    lower = q
    early_lower = {lower}
    for clock in range(1, depth + 1):
        lower = step(lower)
        if clock <= 5 * blocks:
            early_lower.add(lower)
    require(lower == 2**exponent, "lower arm missed certified power of two")

    upper = 3 * q
    require(upper not in early_lower, "early meeting at upper source")
    for _ in range(blocks):
        start = upper
        for parity in (1, 1, 1, 1, 0):
            require(upper % 2 == parity, "wrong physical upper-arm branch")
            upper = step(upper)
            require(upper not in early_lower, "early direct arm meeting")
            require(upper >= start, "upper arm dropped below its run entry")
        require(upper % 2 == 1, "upper arm missed the singleton exit")
    return q.bit_length(), exponent


if __name__ == "__main__":
    for k, h in [(1, 1), (1, 3), (2, 3), (3, 1), (4, 3)]:
        bits, exponent = construct(k, h)
        print(f"K={k} h={h} source_bits={bits} lower_power_exponent={exponent}")
