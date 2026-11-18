"""An exact finite lattice search, independent of the asymptotic S-unit input."""
from pathlib import Path
import runpy

prior = runpy.run_path(str(Path(__file__).with_name("check_mergers.py")))
require = prior["require"]


def least_independent(a, cap):
    modulus = 3**a - 2**(a+1)
    twos = {}
    for j in range(-cap, cap+1):
        twos.setdefault(pow(2, j, modulus), []).append(j)
    best = None
    for k in range(-cap, cap+1):
        for j in twos.get(pow(3, -k, modulus), ()):
            if a*j + (a+1)*k:
                value = max(abs(j), abs(k))
                best = value if best is None else min(best, value)
            else:
                require(k % a == 0 and j == -(a+1)*(k//a), "nonprimitive aligned claim")
    return best


def main():
    expected = {3: 2, 4: 6, 5: 18, 6: 9, 7: 131, 8: 89, 11: 374}
    for a in range(3, 35):
        value = least_independent(a, 50*a)
        require(value == expected.get(a), f"unexpected second direction at {a}")
    q, c, _ = prior["word_data"]("100")
    require(q == 1 and c == 1, "incorrect terminating-prefix data")
    supporting = runpy.run_path(str(Path(__file__).with_name("check_support.py")))
    for a in (5, 12, 24, 48):
        h = a*a+10
        d, offset = 3**a-2**(a+1), 3**a-2**a
        residue = (3**h-offset)*pow(d, -1, 3**(h+1)) % 3**(h+1)
        supporting["source_after_prefix"](3, 1, 1, 1, h+1, residue)
    print("Exact signed exponent boxes |j|,|k|<=50a through a=34; "
          "7 independent exceptions detected; 4 terminating congruences.")


if __name__ == "__main__":
    main()
