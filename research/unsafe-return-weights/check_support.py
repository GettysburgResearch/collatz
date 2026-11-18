"""Check the residue classification and unit-source/certified-basin constructions."""
from fractions import Fraction
from pathlib import Path
import runpy

directory = Path(__file__).resolve().parent
earlier = runpy.run_path(str(directory / "check.py"))
rank, module, require = (earlier[name] for name in ("rank", "module", "require"))


def source_after_prefix(t, q, constant, target, h, residue):
    k = 0
    modulus = 3
    rhs = constant + 3**q * residue
    if pow(2, t, 3) * target % 3 != rhs % 3:
        k = 1
    period = 2
    for _ in range(1, q + h):
        modulus *= 3
        candidates = [k + i * period for i in range(3)]
        k = next(e for e in candidates if pow(2, e + t, modulus) * target % modulus == rhs % modulus)
        period *= 3
    require((pow(2, k + t, modulus)*target-rhs) % modulus == 0, "wrong completion")
    return k


def main():
    even_count = 0
    for y in range(2, 50000, 2):
        if rank(module(y)[0]) <= rank(y):
            continue
        require(y % 9 in (1, 4), "unexpected even unsafe residue")
        z = (4 * y - 1) // 3
        require(z > y and z % 2 == 1 and z % 3 != 0, "wrong odd-unit predecessor")
        require(module(z) == (y, 1, 1, 2), "predecessor module is not exact")
        source_after_prefix(9, 7, 2363, z, 7, 0)
        even_count += 1

    require(earlier["coefficients"](Fraction(73, 16)) ==
            (4, [1, Fraction(1, 3), Fraction(1, 9), Fraction(2401, 243)]),
            "rank coefficients at the first unit phase")
    for b in (1, 2, 6, 21, 60):
        t, q = 11*b + 9, 7*(b+1)
        source_after_prefix(t, q, 17*3**q - 68*2**t, 1, max(7, b+3), 1)
    print(f"{even_count} even unsafe targets received odd-unit predecessors; "
          "5 certified-basin unit tower congruences.")


if __name__ == "__main__":
    main()
