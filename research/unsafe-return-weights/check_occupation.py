"""Finite interface checks for raw occupation and sparse module prefixes."""
from pathlib import Path
import runpy

prev = runpy.run_path(str(Path(__file__).with_name("check_mergers.py")))
step, module, word_data, require = (prev[k] for k in ("step", "module", "word_data", "require"))


def iterate(n, t):
    for _ in range(t):
        n = step(n)
    return n


def main():
    word_count = source_count = 0
    for ell in range(1, 14):
        words = {("1"*a + "0")*(ell+1) for a in range(ell)}
        prefixes = {word[:ell] for word in words} | {"1"*ell}
        require(len(prefixes) == ell+1, "wrong prefix count")
        for word in prefixes:
            q, _, residue = word_data(word)
            for d in (1, 3, 9, 81):
                first_index = ((residue-1)*pow(d, -1, 2**ell)) % 2**ell
                n = 1 + d*(first_index+2**ell)
                next_n = n+d*2**ell
                first = prev["replay"](n, word)[-1]
                second = prev["replay"](next_n, word)[-1]
                require(second-first == d*3**q, "wrong transported progression")
                word_count += 1
        for n in range(2, 4097):
            if module(n)[3] >= ell:
                x, bits = n, ""
                for _ in range(ell):
                    bits += str(x % 2)
                    x = step(x)
                require(bits in prefixes, "missing long module")
                source_count += 1
    full = {1, 2, 4, 8, 16}
    require(len(full)-len({iterate(x, 2) for x in full}) == 2, "preperiod control")
    print(f"{word_count} odd-stride transfers; {source_count} legal long-module prefixes; "
          "sharp finite-preperiod correction.")


if __name__ == "__main__":
    main()
