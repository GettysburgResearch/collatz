"""Enumerate all positive inverse words, including genuinely unequal clocks."""
from pathlib import Path
import runpy

helpers = runpy.run_path(str(Path(__file__).with_name("check_mergers.py")))
crt, step, require, word_data = (helpers[k] for k in ("crt", "step", "require", "word_data"))


def minimum_through(n, cap):
    minimum = n
    count = 0
    y = n
    for _ in range(cap+1):
        layer = {y}
        for s in range(cap+1):
            count += len(layer)
            minimum = min(minimum, min(layer))
            if s < cap:
                parents = {2*z for z in layer}
                parents.update((2*z-1)//3 for z in layer if z % 3 == 2)
                layer = parents
        y = step(y)
    return minimum, count


def main():
    nodes = 0
    for cap in range(2, 15):
        word = "1"*cap + "0"*(cap+2)
        modulus = 2**len(word)
        for r in (0, 1, 3):
            n = crt(word_data(word)[2], modulus, r, 3**cap)
            if n <= 3**cap:
                n += modulus*3**cap
            minimum, count = minimum_through(n, cap)
            require(minimum == n and helpers["replay"](n, word)[-1] < n, "clock bracket")
            nodes += count
    # Base r=2 does not have the required invariant lower set: 1 reaches 2.
    require(step(1) == 2, "incorrect guard test")
    print(f"39 physical clock brackets; {nodes} positive inverse-frontier entries.")


if __name__ == "__main__":
    main()
