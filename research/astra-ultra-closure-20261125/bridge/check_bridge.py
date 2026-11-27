"""Exact finite controls for the conditional cost comparison and literal return words."""

import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def orbit(x, h):
    odd = 0
    for _ in range(h):
        parity = x % 2
        odd += parity
        x = (3 * x + 1) // 2 if parity else x // 2
    return x, odd


def main():
    threshold = 1600
    constant = 9 * (2**40 + 1)
    require(constant**3 * 243**threshold < 16**3 * 256**threshold, "height budget")
    rows = []
    for exponent, base in ((1878, 14417), (3159, 13451)):
        require(pow(3, 3 * exponent + 2, 16384) == base, "power residue")
        earlier, o1 = orbit(base + 1, 14)
        later, o2 = orbit(27 * base + 1, 14)
        require(earlier == later and o1 == o2 + 3, "physical prefix")
        rows.append([exponent, base, earlier, o1, o2])
    require(pow(3, 12288, 16384) == 1, "exponent period")
    require(orbit(17, 9)[0] == 1 and orbit(51, 17) == (1, 7), "canonical anchors")
    print(json.dumps({"height_threshold": threshold, "neighbor_rows": rows}, sort_keys=True))


if __name__ == "__main__":
    main()
