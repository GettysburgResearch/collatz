"""Exact finite controls for affine posterior shells on words without two twos."""
from fractions import Fraction
from hashlib import sha256
from itertools import accumulate, product
from math import comb
import json


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def exponents(x, n):
    word = []
    states = [x]
    for _ in range(n):
        value = 3 * x + 1
        f = (value & -value).bit_length() - 1
        x = value >> f
        word.append(f)
        states.append(x)
    return word, states


def reference(word):
    q = 3 ** len(word)
    clocks = list(accumulate(word, initial=0))
    carry = sum(3 ** (len(word) - i - 1) * 2 ** clocks[i]
                for i in range(len(word)))
    endpoint = carry * pow(2, -clocks[-1], q) % q
    if endpoint % 2 == 0:
        endpoint += q
    source = (2 ** clocks[-1] * endpoint - carry) // q
    actual, states = exponents(source, len(word))
    require(tuple(actual) == word and states[-1] == endpoint, "exact source")
    return clocks, states


def inverse_words(target, length, budget):
    if length == 0:
        yield (), (target,)
        return
    if target % 3 == 0:
        return
    first = 1 if target % 3 == 2 else 2
    for last in range(first, budget - length + 2, 2):
        parent = ((target << last) - 1) // 3
        for word, states in inverse_words(parent, length - 1, budget - last):
            yield word + (last,), states + (target,)


def check_word(word, cap):
    n = len(word)
    clocks, states = reference(word)
    hs = [Fraction(2 ** clocks[i], 3 ** (i + 1)) for i in range(n)]
    # This infinite reference script continues with ones forever.
    remainder = Fraction(2 ** clocks[n], 3 ** n)
    center = sum(hs, remainder)
    shells = [set() for _ in range(cap + 1)]
    for alt, values in inverse_words(states[-1], n, clocks[-1] + cap):
        totals = list(accumulate(alt, initial=0))
        d = totals[-1] - clocks[-1]
        require(0 <= d <= cap, "terminal minimum")
        ds = [d + clocks[i] - totals[i] for i in range(n + 1)]
        require(min(ds) >= 0, "every suffix minimum")
        offsets = [values[i] - (states[i] << ds[i]) for i in range(n + 1)]
        normalized = [Fraction(offsets[i], 2 ** ds[i]) for i in range(n + 1)]
        for i, e in enumerate(word):
            require(2 ** e * normalized[i + 1]
                    == 3 * normalized[i] + Fraction(1, 2 ** ds[i]) - 1,
                    "one-step normalized affine recurrence")
        c = offsets[0]
        require(c not in shells[d], "fixed-shell injectivity")
        shells[d].add(c)
        error = center - normalized[0]
        require(error == remainder + sum(hs[i] / 2 ** ds[i] for i in range(n)),
                "exact center")
        if d >= 4:
            t, h = d // 4, (3 * d) // 4
            # Extend by reference ones if the competitor has already merged.
            first_t = totals[min(t, n)] + max(0, t - n)
            if first_t <= h:
                require(t <= n, "early meeting")
                require(error <= center * Fraction(1, 2 ** (d - h))
                        + sum(hs[t:], remainder), "localized good offset")

        high_source = states[0] + (2 << clocks[-1])
        high_alt = (high_source << d) + c
        alt_replay, high_states = exponents(high_alt, n)
        require(tuple(alt_replay) == alt and high_states[-1] ==
                states[-1] + 2 * 3 ** n, "same merger on a distinct lift")
    return shells


def main():
    cap = 12
    previous = {}
    rows = []
    for n in range(1, 9):
        digest = sha256()
        current = {}
        total = 0
        maximum = Fraction(0)
        for word in product((1, 2), repeat=n):
            if any(a == b == 2 for a, b in zip(word, word[1:])):
                continue
            shells = check_word(word, cap)
            current[word] = shells
            if n > 1:
                require(all(old <= new for old, new in
                            zip(previous[word[:-1]], shells)),
                        "all-shell persistence at a longer depth")
            for d, shell in enumerate(shells):
                for c in sorted(shell):
                    digest.update(f"{word},{d},{c}\n".encode())
                total += len(shell)
            mass = sum(Fraction(len(shell), 2 ** d) for d, shell in enumerate(shells))
            maximum = max(maximum, mass)
        rows.append({"depth": n, "scripts": len(current), "checked_competitors": total,
                     "maximum_truncated_relative_mass": str(maximum),
                     "affine_shells_sha256": digest.hexdigest()})
        previous = current

    cylinders = []
    for d in range(4, 18):
        t, h = d // 4, (3 * d) // 4
        observed = sum(sum(exponents(c, t)[0]) > h for c in range(1, 2 ** d, 2))
        count = Fraction(2 ** (d - 1), 2 ** h) * sum(comb(h, k) for k in range(t))
        require(observed == count, "exact dyadic complement")
        require(Fraction(observed, 2 ** (d - 1)) <= 2 ** t * Fraction(3, 4) ** h,
                "negative-binomial Chernoff")
        cylinders.append([d, observed, 2 ** (d - 1)])
    print(json.dumps({"scope": "finite affine and cylinder checks only",
                      "maximum_checked_excess": cap, "rows": rows,
                      "exceptional_odd_cylinder_counts": cylinders}, indent=2))


if __name__ == "__main__":
    main()
