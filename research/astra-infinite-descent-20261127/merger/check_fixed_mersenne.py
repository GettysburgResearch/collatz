"""Independent scalar verification of the nine supplied PR206 parent comparisons."""
from pathlib import Path
import re


# The grades include the upper arm's d initial charge.
CASES = [
    (1, 27, 127896, 64108),
    (80, 720, 100726, 50666),
    (113, 1017, 70020, 35045),
    (130, 1170, 18284, 9151),
    (135, 1243, 14025, 7029),
    (138, 1243, 12359, 6213),
    (150, 1350, 19333, 9526),
    (159, 1431, 18823, 9354),
    (180, 1620, 20599, 10286),
]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def charges():
    text = (Path(__file__).resolve().parents[1] / "imports" / "pr206" / "ReturnDescentRows.lean").read_text()
    body = text.split("private def rows : Array Row := #[", 1)[1].split("]", 1)[0]
    pattern = r"⟨(\d+), (\d+), (\d+), (\d+), (\d+), (\d+)⟩"
    found = [[int(x) for x in match] for match in re.findall(pattern, body)]
    require(len(found) == 81, "the pinned 81-row price table")
    return [row[2] + row[3] for row in found]


def step(v):
    return (3 * v + 1) // 2 if v % 2 else v // 2


def main():
    table = charges()
    for k, d, h, grade in CASES:
        m = 12 * 2 ** (18 * k) - 1
        t = m - d
        charge = table[((t - 1) // 2) % 81]
        require(m % 162 == 11 and t > 0 and max(18, t + charge) <= m,
                f"smaller canonical source price k={k}")
        b = pow(3, t, 2**h)
        require(0 < b < 2**h and b % 2, "positive earlier representative")
        upper, lower = 3**d * b - 1, b - 1
        upper_grade, lower_grade = d, 0
        for _ in range(h):
            require((upper, upper_grade) != (lower, lower_grade), "first native compressed merger")
            upper_grade += upper % 2
            lower_grade += lower % 2
            upper, lower = step(upper), step(lower)
        require(upper == lower and upper_grade == lower_grade == grade, f"actual counted merger k={k}")
        print(f"PASS k={k} d={d} h={h} augmentedGrade={grade} rowCharge={charge}", flush=True)


if __name__ == "__main__":
    main()
