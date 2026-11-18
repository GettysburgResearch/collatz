"""Check exact aligned clocks and explicit finite lower-diagram exclusions."""
from pathlib import Path
import runpy

helpers = runpy.run_path(str(Path(__file__).with_name("check_mergers.py")))
crt, rank, component, step, module, word_data, require = (
    helpers[name] for name in ("crt", "rank", "component", "step", "module", "word_data", "require")
)


def exclude_smaller(n, cap):
    """Enumerate every positive physical inverse path at each possible meeting time."""
    y = n
    nodes = 0
    for _ in range(cap+1):
        frontier = {y}
        for depth in range(cap+1):
            require(all(rank(m) >= rank(n) for m in frontier), "cheaper physical diagram")
            nodes += len(frontier)
            if depth == cap:
                break
            parents = {2*m for m in frontier}
            parents.update((2*m-1)//3 for m in frontier if m % 3 == 2)
            frontier = parents
        y = step(y)
    return nodes


def aligned(a):
    h = 6*a + 7
    power, d, c = 3**h, 3**a-2**(a+1), 3**a-2**a
    residue = ((power-c)*pow(d, -1, 3*power)) % (3*power)
    n = crt(2**a-1, 2**(a+1), residue, 3*power)
    require(rank(n) == component(n, a), "wrong moving minimum")
    y = helpers["replay"](n, "1"*a+"0")[-1]
    require(rank(y) < rank(n), "aligned ceiling failed")
    return exclude_smaller(n, a) if a <= 12 else 0


def unsafe(modes):
    h = 3*modes + 7
    k = h+modes+2
    power = 3**h
    word = "1"*modes + "0"*k
    _, _, residue = word_data(word)
    n = crt(residue, 2**len(word), 1+power, 3*power)
    require(1+power <= n < 2**len(word)*3*power, "wrong least CRT range")
    require(rank(n) == (n-1)**2//power and rank(module(n)[0]) > rank(n), "wrong unsafe stratum")
    require(rank(helpers["replay"](n, word)[-1]) < rank(n), "rank failed to repay")
    return exclude_smaller(n, modes) if modes <= 14 else 0


def main():
    nodes = sum(aligned(a) for a in (5, 6, 8, 12, 32, 64))
    nodes += sum(unsafe(m) for m in (2, 4, 7, 11, 14, 24, 48))
    print(f"6 exact aligned and 7 unsafe clock constructions; "
          f"{nodes} physical inverse-frontier entries checked under finite clock caps.")


if __name__ == "__main__":
    main()
