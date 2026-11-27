"""Independent finite checks of the two-light chart and its scope boundary.

This is a bounded exact check, not a proof of an infinite reset language.
The companion TwoLight.lean supplies the universal three-tile theorem.
"""

import json


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def affine(bits):
    multiplier, carry = 1, 0
    for i, bit in enumerate(bits):
        if bit == "1":
            multiplier, carry = 3 * multiplier, 3 * carry + (1 << i)
    return 1 << len(bits), multiplier, carry


def source_cylinder(word, pad=2):
    # x=(q+7)/2; L:8*x'=9*x, P:32*x'=9*x+83.
    a, b, clocks = 1, 0, 0
    for letter in word:
        step = 3 if letter == "L" else 5
        a, b, clocks = (
            9 * a,
            9 * b + (0 if letter == "L" else 83) * (1 << clocks),
            clocks + step,
        )
    modulus = 1 << (clocks + 3 * pad)
    x = (-b * pow(a, -1, modulus)) % modulus or modulus
    return x, (a * x + b) // (1 << clocks), clocks, modulus


def run(n, clocks):
    bits = ""
    for _ in range(clocks):
        bits += str(n % 2)
        n = (3 * n + 1) // 2 if n % 2 else n // 2
    return n, bits


def check():
    rows = []
    controls = 0
    for word, target in [
        ("L", "011"),
        ("LLP", "10110011100"),
        ("LLPP", "1011011100001100"),
    ]:
        source = "".join("101" if letter == "L" else "11000" for letter in word)
        den, mult, carry = affine(source)
        target_den, target_mult, target_carry = affine(target)
        require((target_den, target_mult) == (den, mult), "wrong clocks or odd counts")
        require(183 * carry + den == mult + 128 * target_carry, "chart coefficient identity")
        base, _, clocks, modulus = source_cylinder(word)
        for lift in (0, 1, 7, 83):
            x = base + lift * modulus
            q = 2 * x - 7
            q_next, observed = run(q, clocks)
            require(observed == source, "source cylinder legality")
            require((183 * q + 1) % 128 == 0, "initial integrality")
            require((183 * q_next + 1) % 128 == 0, "terminal integrality")
            y = (183 * q + 1) // 128
            y_next, observed_target = run(y, clocks)
            require(observed_target == target, "target literal word")
            require(128 * y_next == 183 * q_next + 1, "literal return")
            controls += 1
        rows.append({"source_word": word, "source_bits": source, "target_bits": target,
                     "clocks": clocks, "odd_inputs": source.count("1"),
                     "source_carry": carry, "target_carry": target_carry})

    x, _, clocks, _ = source_cylinder("LLPPP")
    q = 2 * x - 7
    q_next, source_bits = run(q, clocks)
    y = (183 * q + 1) // 128
    y_next, target_bits = run(y, clocks)
    expected = (183 * q_next + 1) // 128
    require(source_bits == "101101110001100011000", "scope example literal source")
    require(y_next != expected, "triple-paid extension unexpectedly returned")
    return {
        "status": "PASS", "scope": "12 literal chart lifts and one finite failed extension",
        "ordinary_lifts": controls, "chart_rows": rows,
        "failed_unqualified_LLPPP_extension": {
            "source": q, "source_endpoint": q_next, "clocks": clocks,
            "shadow_start": y, "actual_shadow_endpoint": y_next,
            "putative_chart_endpoint": expected, "target_bits": target_bits,
            "meaning": "The simple LLPPP tile is not a return for this chart. This is not a Collatz counterexample."
        }
    }


if __name__ == "__main__":
    print(json.dumps(check(), indent=2))
