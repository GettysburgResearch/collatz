"""Exact finite controls for FBR's polynomial compiler, not a cycle search."""
from fractions import Fraction as Q
import json


def word_data(word):
    length = odds = correction = 0
    for bit in word:
        if bit == "1":
            correction = 3 * correction + 2**length
            odds += 1
        elif bit != "0":
            raise ValueError("nonbinary word")
        length += 1
    return length, odds, correction


def add_monomial(poly, exponents, coefficient):
    poly[exponents] = poly.get(exponents, Q(0)) + coefficient
    if not poly[exponents]:
        del poly[exponents]


def compiler(schema):
    schema = [item for item in schema if item[0]]
    if not schema:
        return {}, {}
    data = [(word_data(word), a, b) for word, a, b in schema]
    f = {}
    corners = []
    for j in range(len(data) + 1):
        coefficient = Q(1)
        ax = ay = 0
        for i, ((length, odds, _), a, b) in enumerate(data):
            if i < j:
                coefficient *= Q(2) ** (length * b)
                ax += length * a
            else:
                coefficient *= Q(3) ** (odds * b)
                ay += odds * a
        corners.append(((ax, ay), coefficient))
    for i, ((length, odds, correction), _, _) in enumerate(data):
        fixed = Q(correction, 2**length - 3**odds)
        add_monomial(f, corners[i + 1][0], fixed * corners[i + 1][1])
        add_monomial(f, corners[i][0], -fixed * corners[i][1])
    d = {}
    add_monomial(d, corners[-1][0], corners[-1][1])
    add_monomial(d, corners[0][0], -corners[0][1])
    return f, d


def evaluate(poly, k):
    return sum(c * Q(2) ** (a * k) * Q(3) ** (b * k)
               for (a, b), c in poly.items())


CASES = [
    ("single trivial loop", [("10", 1, 0)], Q(1)),
    ("common fixed blocks", [("10", 1, 0), ("1010", 2, 1)], Q(1)),
    ("fixed phase connectors", [("10", 1, 0), ("1", 0, 1),
                                ("01", 1, 0), ("0", 0, 1)], Q(1)),
    ("negative fixed point", [("1", 1, 1), ("11", 2, 0)], Q(-1)),
    ("zero fixed point", [("0", 1, 0), ("00", 1, 1)], Q(0)),
    ("rational noninteger", [("100", 1, 0), ("100100", 1, 1)], Q(1, 5)),
    ("different fixed blocks", [("1", 1, 0), ("0", 1, 0)], None),
    ("mixed block data", [("100", 1, 0), ("1100", 2, 1)], None),
    ("all slopes zero", [("10", 0, 1)], Q(1)),
    ("empty block deletion", [("", 1, 5), ("10", 1, 0)], Q(1)),
    ("zero repetition deletion", [("10", 0, 0), ("01", 1, 0)], Q(2)),
]


def main():
    results = []
    for label, schema, constant in CASES:
        f, d = compiler(schema)
        actual_samples = 0
        quotients = set()
        for k in range(6):
            word = "".join(w * (a * k + b) for w, a, b in schema)
            length, odds, correction = word_data(word)
            if evaluate(f, k) != correction:
                raise RuntimeError((label, k, "numerator"))
            if evaluate(d, k) != 2**length - 3**odds:
                raise RuntimeError((label, k, "full denominator"))
            if not word:
                continue
            actual_samples += 1
            q = Q(correction, 2**length - 3**odds)
            quotients.add(q)
            if constant is not None and q != constant:
                raise RuntimeError((label, k, "constant classification"))
            if q.denominator == 1:
                x = q.numerator
                for bit in word:
                    if x % 2 != int(bit):
                        raise RuntimeError((label, k, "physical parity"))
                    x = (3 * x + 1) // 2 if x % 2 else x // 2
                if x != q:
                    raise RuntimeError((label, k, "physical loop"))
        if constant is not None:
            if any(f.get(m, 0) != constant * d.get(m, 0) for m in f.keys() | d.keys()):
                raise RuntimeError((label, "polynomial identity"))
        elif len(quotients) < 2:
            raise RuntimeError((label, "nonconstant control"))
        results.append({"case": label, "retained_parameters": actual_samples,
                        "constant": None if constant is None else str(constant),
                        "passed": True})
    print(json.dumps({"scope": "11 exact compiler and parity controls; no global cycle search",
                      "results": results}, indent=2))


if __name__ == "__main__":
    main()
