"""Exact finite examples for the physical forward-repayment clock bound."""
from pathlib import Path
import runpy

source = runpy.run_path(str(Path(__file__).resolve().parents[2] /
                            "experiments/X-ASTRA3-005-spectrum-switch/run.py"))
rank, step = (source[name] for name in ("rank", "step"))


def require(condition, context):
    if not condition:
        raise ValueError(context)


def main():
    endpoints = repayments = 0
    for height in range(1, 65):
        power = 3**height
        for unit in (1, 5, 7, 11, 17, 25, 31):
            n = unit * power
            require(rank(n) == n**2 // power, "wrong initial rank")
            y, odds, t = n, 0, 1
            while 15 * 4**t < power:
                odds += y % 2
                y = step(y)
                require(y > 1 and 20 * 8**t * rank(y) >= n**2 * 6**odds,
                        "physical clock inequality failed")
                endpoints += 1
                t += 1

        t = 1
        while 4**t <= 16 * power:
            t += 1
        modulus = 2**t
        residue = -pow(3, -1, modulus) % modulus
        lift = ((residue - power) * pow(3 * power, -1, modulus)) % modulus
        n = power + 3 * power * lift
        y = n
        for j in range(t):
            require(y % 2 == (j == 0), "wrong repayment word")
            y = step(y)
        require(y == (3*n + 1) // modulus and rank(y) < rank(n), "repayment failed")
        repayments += 1
    print(f"{endpoints} physical rank bounds; {repayments} exact ternary strata repaid.")


if __name__ == "__main__":
    main()
