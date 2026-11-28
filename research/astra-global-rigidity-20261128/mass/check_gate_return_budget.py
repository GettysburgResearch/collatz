"""Exact completed true-gate budgets on finite verified terminating paths.

This control tests the declared native interface and the actual gate cocycle.
It makes no assertion about the limiting return law or arbitrary termination.
"""

import json


def require(condition, label):
    if not condition:
        raise ValueError(label)


def step(n):
    return (3 * n + 1) // 2 if n % 2 else n // 2


def main():
    deficit = {1: 0, 2: 1}

    def obtain(n):
        path, seen = [], set()
        x = n
        while x not in deficit:
            require(x not in seen and len(path) < 100_000,
                    "finite control did not reach a verified suffix")
            seen.add(x)
            path.append(x)
            x = step(x)
        for x in reversed(path):
            d = deficit[step(x)]
            deficit[x] = max(0, d - 1) if x % 2 else d + 1
        return deficit[n]

    def gate(n):
        return bool(n % 2 and obtain(step(n)) == 0)

    gates = completed = killed = 0
    largest_clock = 0
    for n in range(3, 16_384, 2):
        obtain(n)
        if not gate(n):
            continue
        gates += 1
        x, q, t, a = n, 0, 0, 0
        while x != 1 and a < 8:
            require(x >= 3 and x % 2, "native departure floor")
            raw = 3 * x + 1
            e = (raw & -raw).bit_length() - 1
            x = raw >> e
            q += 1
            t += e
            if gate(x):
                a += 1
                require(t + a == 2 * q, "strict gate grade balance")
                require(6**q <= n * 2**a * 5**q,
                        "completed native height budget")
                completed += 1
                largest_clock = max(largest_clock, t)
        killed += x == 1
    require(gates > 500 and completed > 1000 and killed > 100,
            "insufficient completed and killed actual paths")
    print(json.dumps({"true_gate_starts": gates,
                      "completed_return_prefixes": completed,
                      "killed_before_eight_returns": killed,
                      "largest_shortcut_clock": largest_clock,
                      "actual_suffix_states": len(deficit)}, sort_keys=True))


if __name__ == "__main__":
    main()
