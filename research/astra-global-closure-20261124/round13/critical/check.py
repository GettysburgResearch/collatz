"""Exact finite controls for the explicit mechanical critical script.

No floating logarithms, probable-prime tests or disabled Python assertions.
These finite checks do not establish transcendence or a fixed infinite orbit.
"""

from fractions import Fraction
import json


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    length = 4096
    clocks = [0]
    gaps = []
    power = 1
    for j in range(1, length + 1):
        power *= 3
        clock = power.bit_length() - 1
        require((1 << clock) < power < (1 << (clock + 1)), "strict clock bracket")
        gaps.append(clock - clocks[-1])
        clocks.append(clock)
        require(gaps[-1] in (1, 2), "mechanical alphabet")
    complexities = []
    for n in range(1, 65):
        observed = len({tuple(gaps[j:j + n]) for j in range(length - n + 1)})
        require(observed <= n + 1, "finite factor complexity")
        complexities.append({"length": n, "observed_factors": observed})

    realizations = []
    for n in (1, 2, 3, 4, 8, 16, 32, 64, 128, 256):
        modulus = 3 ** n
        residue = sum(3 ** (j - 1) * pow(2, -clocks[j], modulus)
                      for j in range(1, n + 1)) % modulus
        q = residue if residue % 2 else residue + modulus
        while q <= 2 * n + 1:
            q += 2 * modulus
        require(q > 0 and q % 2 == 1 and q % 3 != 0, "positive unit endpoint")
        y = q
        beta = Fraction(0)
        for j in range(1, n + 1):
            numerator = (1 << gaps[j - 1]) * y - 1
            require(numerator % 3 == 0, "ordinary predecessor divisibility")
            predecessor = numerator // 3
            require(0 < predecessor < q and predecessor % 2 == 1, "ordinary prefix heights")
            require(3 * predecessor + 1 == (1 << gaps[j - 1]) * y, "physical odd edge")
            beta += Fraction(3 ** (j - 1), 1 << clocks[j])
            require(Fraction(1 << clocks[j], 3 ** j) * (q - beta) == predecessor,
                    "complete affine carry")
            y = predecessor
        # Literal forward odd map, including exact valuations.
        forward = y
        for expected in reversed(gaps[:n]):
            value = 3 * forward + 1
            exponent = (value & -value).bit_length() - 1
            require(exponent == expected, "exact physical valuation")
            forward = value >> exponent
        require(forward == q, "literal forward endpoint")
        realizations.append({"depth": n, "clock": clocks[n],
                             "endpoint": str(q), "source": str(y)})

    print(json.dumps({
        "status": "PASS",
        "scope": "Finite mechanical prefixes and changing positive ordinary realizations; no infinite ordinary orbit or transcendence inferred by this program.",
        "mechanical_prefix_length": length,
        "factor_counts": complexities,
        "ordinary_realizations": realizations,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
