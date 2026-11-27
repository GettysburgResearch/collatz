"""Independent replay of both arms of 66 ordinary carry chains."""

import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def follow(start, clocks):
    value = start
    odds = 0
    for _ in range(clocks):
        parity = value % 2
        odds += parity
        value = (value * (1 + 2 * parity) + parity) // 2
    return value, odds


def main():
    depths = list(range(1, 12))
    entry_clocks = [2, 3, 13, 19, 23, 29]
    cases = 0
    for depth in depths:
        modulus = 3 ** (8 * depth + 3)
        for k in entry_clocks:
            x = 17 * modulus + (203816 * pow(517727 * 2**k, -1, modulus)) % modulus
            source, remainder = divmod(16 * 2**k * x - 7, 9)
            require(remainder == 0, "nonintegral terminal")
            for _ in range(depth):
                index, remainder = divmod(source - 1121, 48 * 3**8)
                require(index >= 0 and remainder == 0, "invalid inverse row")
                source = 89585 + 48 * 2**19 * index

            horizon = 19 * depth + 4 + k
            require(follow(source, horizon) == (x, 8 * depth + 2), "lower arm mismatch")
            upper = (3 ** (k + 1) * x - 1, 8 * depth + 2 + k)
            require(follow(3 * source, horizon) == upper, "upper arm mismatch")
            cases += 1

    require(cases == 66, "incomplete case schedule")
    print(json.dumps({"depths": depths, "entry_clocks": entry_clocks,
                      "verified_double_arm_cases": cases}, sort_keys=True))


if __name__ == "__main__":
    main()
