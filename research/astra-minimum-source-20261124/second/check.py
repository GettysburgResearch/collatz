"""Replay the two actual odd runs and their meeting with a smaller multiple."""
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def step(n):
    return (3 * n + 1) // 2 if n % 2 else n // 2


def run(n, clocks):
    for _ in range(clocks):
        n = step(n)
    return n


def strip(n, prime):
    exponent = 0
    while n % prime == 0:
        n //= prime
        exponent += 1
    return exponent, n


def check_source(n):
    m, a = strip(n + 1, 2)
    q = n // 3
    require(n == 3 * q and 1 <= m <= 3, "first run hypotheses")
    r = 3**m * a
    require(r % 4 == 3, "first exit residue")
    u = (3**(m - 1) * a - 1) // 4
    require(0 < u < q and r == 12 * u + 3, "smaller triple")
    y = run(n, m + 1)
    require(run(n, m) == r - 1 and y == 6 * u + 1, "first exit path")
    length, b = strip(y + 1, 2)
    last = 3**length * b
    require(run(y, length) == last - 1, "second run")
    if last % 4 != 1:
        return length, False
    target = (last - 1) // 4
    require(run(3 * u, length + 1) == target, "smaller triple path")
    require(run(n, m + length + 3) == target, "bad triple path")
    return length, True


def crt_source(h, length):
    binary = 2**(length + 3)
    ternary = 3**(h + 1)
    low2 = (2**(length + 1) * (-1)**length - 1) * pow(27, -1, binary) % binary
    low3 = (1 + 3**h) * pow(8, -1, ternary) % ternary
    a = low2 + binary * ((low3 - low2) * pow(binary, -1, ternary) % ternary)
    n = 8 * a - 1
    require(strip(n, 3)[0] == h and strip(n + 1, 2)[0] == 3, "CRT valuations")
    require(3 * a % 256 == 199, "separation from first-exit residue 147")
    return n


def main():
    results = {}
    for m in range(1, 4):
        counts = [0, 0]
        for a in range(1, 8192, 2):
            n = 2**m * a - 1
            if n % 3 == 0 and 3**m * a % 4 == 3:
                _, excluded = check_source(n)
                counts[excluded] += 1
        require(min(counts) > 0, "both second exits must occur")
        results[str(m)] = {"other_second_exit": counts[0], "merger": counts[1]}
    require(check_source(4455) == (5, True), "worked example")
    pairs = 0
    for h in range(3, 12):
        for length in range(7, 26):
            require(check_source(crt_source(h, length)) == (length, True), "CRT run")
            pairs += 1
    print(json.dumps({"first_run_lengths": results, "CRT_pairs": pairs}, sort_keys=True))


if __name__ == "__main__":
    main()
