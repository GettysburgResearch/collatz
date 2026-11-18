"""Construct and check modular certificates of completion by a final halving run."""
from pathlib import Path
import runpy

source = runpy.run_path(str(Path(__file__).resolve().parents[2] /
                            "experiments/X-ASTRA3-005-spectrum-switch/run.py"))
rank, module = (source[name] for name in ("rank", "module"))


def require(condition, context):
    if not condition:
        raise ValueError(context)


def halving_exponent(periods):
    bits = [int(bit) for bit in "11110111000" * periods + "111101110"]
    q = sum(bits)
    t = len(bits)
    constant = 0
    for i, bit in enumerate(bits):
        if bit:
            constant = 3 * constant + (1 << i)
    require(constant == 17 * 3**q - 68 * 2**t, "wrong signed-cycle offset")

    modulus = 3
    order = 2
    exponent = int(constant % 3 != 1)
    for _ in range(1, q + 7):
        modulus *= 3
        lifts = [exponent + j * order for j in range(3)
                 if pow(2, exponent + j * order, modulus) == constant % modulus]
        require(len(lifts) == 1, "nonunique ternary discrete-log lift")
        exponent = lifts[0]
        order *= 3

    k = (exponent - t) % order
    require(pow(2, k + t, modulus) == constant % modulus, "completion fails")
    return t, q, k, constant


def main():
    for b in (0, 1, 2, 5, 12, 32, 64):
        t, q, k, constant = halving_exponent(b)
        if b == 0:
            n = ((1 << (k + t)) - constant) // 3**q
            require(n > 0 and n % 3**7 == 0, "wrong positive ternary source")
            y, mode, repeats, clock = module(n)
            require((mode, repeats, clock) == (4, 1, 5), "first module")
            z, mode, repeats, clock = module(y)
            require((mode, repeats, clock) == (3, 1, 4), "last odd module")
            require(z == 1 << k and rank(n) < rank(y) < rank(z), "unsafe guards")
            require(rank(1) == 0, "last even module must be safe")
            print(f"Literal 2-state tower ends in 2^{k}, followed by k halvings.")
    print("Seven modular certificates through 130 unsafe states; "
          "large exponents checked symbolically.")


if __name__ == "__main__":
    main()
