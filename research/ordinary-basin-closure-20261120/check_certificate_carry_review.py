#!/usr/bin/env python3
"""Independent direct-map regression of the sibling certificate-carry note."""
import json


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def oddpart(value):
    require(value > 0, "positive odd-part argument")
    while value % 2 == 0:
        value //= 2
    return value


def step(n):
    return oddpart(3 * n + 1)


def iterate(n, q):
    for _ in range(q):
        n = step(n)
    return n


def gap(n):
    x, a = 3 * n + 1, 0
    while x % 2 == 0:
        x //= 2
        a += 1
    return a


def inverse(a, z):
    n, remainder = divmod(2**a * z - 1, 3)
    return n if remainder == 0 and n > 0 and n % 2 else None


def ray(k, x):
    return 2**k * x - 1


def main():
    counts = {"one_letter_carries": 0, "two_letter_rules": 0,
              "ternary_carry_transports": 0, "terminal_divisibility": 0,
              "depth_two_family": 0}
    suffixes = (1, 5, 7, 11, 13, 17, 29, 31, 49, 53, 113)
    for z in suffixes:
        for a in range(1, 10):
            x = inverse(a, z)
            if x is None:
                continue
            require(gap(x) == a and step(x) == z, "source inverse letter")
            for k in range(1, 9):
                target = ray(k, x)
                for j in range(k):
                    require(iterate(target, j) == 3**j * 2 ** (k - j) * x - 1,
                            "universal initial run")
                require(iterate(target, k) == oddpart(3**k * x - 1),
                        "universal terminal carry")
                require(iterate(target, k) == oddpart(
                    2**a * 3 ** (k - 1) * z - (3 ** (k - 1) + 1)),
                    "source-letter carry")
                counts["one_letter_carries"] += 1
            if a >= 2:
                common = oddpart(9 * x - 1)
                require(iterate(ray(1, x), 2) == common, "A two-step merger")
                require(iterate(ray(2, x), 2) == common, "B two-step merger")
                require(step(ray(1, x)) == ray(a - 1, z), "A actual new state")
                require(iterate(ray(2, x), a) == iterate(ray(a - 1, z), a - 1),
                        "B stated merger clocks")

    for w in suffixes:
        for b in range(1, 10):
            z = inverse(b, w)
            if z is None:
                continue
            x = inverse(1, z)
            if x is None:
                continue
            require(gap(x) == 1 and gap(z) == b, "two-letter source word")
            if b == 1:
                require(step(ray(1, x)) == (w - 2) // 3, "A (1,1) first step")
                require(iterate(ray(1, x), 2) == step(ray(1, z)) == oddpart(w - 1),
                        "A (1,1) merger")
            elif b == 2:
                require((w - 1) % 3 == 0, "A (1,2) denominator")
                require(step(ray(1, x)) == oddpart((w - 1) // 3),
                        "A (1,2) carry")
            else:
                require(step(ray(1, x)) == inverse(b - 2, w), "A (1,b) inverse")
                require(iterate(ray(1, x), 2) == w, "A (1,b) absorption")
                require(iterate(ray(2, x), 2) == 2**b * w - 3,
                        "B (1,b) initial carry")
                require(iterate(ray(2, x), b) == iterate(ray(b - 2, w), b - 2),
                        "B (1,b) merger clocks")
            counts["two_letter_rules"] += 1

    for d in range(6):
        for e in (1, 2, 7, 13):
            w = 1 + 2 * 3 ** (d + 1) * e
            x = inverse(2, w)
            require(x is not None and (x - 1) % 3**d == 0, "carry domain")
            require(oddpart((x - 1) // 3**d) == oddpart((w - 1) // 3 ** (d + 1)),
                    "gap-two denominator growth")
            counts["ternary_carry_transports"] += 1
        for b in range(3, 121):
            integral = (2 ** (b - 2) - 1) % 3 ** (d + 1) == 0
            require(integral == ((b - 2) % (2 * 3**d) == 0),
                    "exact terminal denominator condition")
            counts["terminal_divisibility"] += 1

    family = []
    for r in range(1, 13):
        h = 6 * r + 1
        x = (2 ** (h + 3) - 7) // 9
        require(x % 16 == 1 and x > 1, "depth-two source class")
        require(gap(x) == 2 and gap(step(x)) == h + 1, "complete source gaps")
        require(step(x) > 1 and iterate(x, 2) == 1, "exact source hitting depth")
        target = ray(1, x)
        require(gap(target) == gap(step(target)) == 2, "target first gaps")
        require(iterate(target, 2) == 2**h - 1, "terminal Mersenne")
        trajectory = [target]
        for _ in range(h + 2):
            trajectory.append(step(trajectory[-1]))
        require(all(n > 1 for n in trajectory), "target clock lower bound")
        require(trajectory[h + 1] == 2 * 3 ** (h - 1) - 1, "growth-debt peak")
        require(trajectory[h + 2] == (3**h - 1) // 2, "growth-debt endpoint")
        require(9 * x + 7 == 2 ** (h + 3), "peak parameter identity")
        family.append({"r": r, "source_odd_depth": 2,
                       "source_total_valuation": h + 3,
                       "target_odd_depth_lower_bound": h + 3})
        counts["depth_two_family"] += 1

    report = {"status": "No substantive mathematical issue found in the reviewed identities.",
              "counts": counts, "depth_two_family": family,
              "scope": "Finite direct-map regression plus separate universal algebra review; no proof that the residual Mersennes converge."}
    output = json.dumps(report, sort_keys=True, indent=2) + "\n"
    print(output, end="")


if __name__ == "__main__":
    main()
