"""Bounded rank-slice and actual module-clock synchronization checks."""
from collections import defaultdict
from pathlib import Path
import runpy

src = runpy.run_path(str(Path(__file__).resolve().parents[2] /
                         "experiments/X-ASTRA3-005-spectrum-switch/run.py"))
rank, step, module, vp = (src[k] for k in ("rank", "step", "module", "vp"))


def require(ok, message):
    if not ok:
        raise ValueError(message)


def slice_key(n):
    a = min({0, 1, 2, vp(2*n+1, 3)}, key=lambda i: (src["ra"](n, i), i))
    z = src["z"](n, a)
    return a, vp(z, 3), z > 0


def raw_clock(n, r):
    for _ in range(r):
        n = step(n)
    return n


def module_boundaries(n, limit):
    time = 0
    result = {0}
    while time < limit and n != 1:
        n, _, _, count = module(n)
        time += count
        result.add(time)
    return result


def main():
    r = 11
    fibers = defaultdict(list)
    for n in range(2, 30001):
        if rank(module(n)[0]) > rank(n) and n % 3:
            fibers[slice_key(n), raw_clock(n, r)].append(n)
    mergers = mid = 0
    for (_, y), inputs in fibers.items():
        best = min(inputs, key=rank)
        for n in inputs:
            if n == best:
                continue
            require(rank(best) < rank(n), "unresolved within-slice tie")
            mergers += 1
            if y <= 2:
                continue
            # Move both literal module clocks up to the first common full-run boundary.
            leading = vp(y+1, 2) if y % 2 else 0
            z = raw_clock(y, leading+1)
            if z == 1:
                continue
            endpoint, _, _, extra = module(z)
            joint_time = r+leading+1+extra
            left, right = (module_boundaries(origin, joint_time) for origin in (n, best))
            require(joint_time in left and joint_time in right, "missed common boundary")
            require(endpoint == raw_clock(n, joint_time), "wrong common state")
            mid += int(r not in left or r not in right)
    require(mid > 0, "no mid-module meetings checked")

    modulus = 2**11
    power = 3**7
    first = 1 + power*((-18*pow(power, -1, modulus)) % modulus)
    for j in range(1, 17):
        n = first + j*power*modulus
        require(n % 3 == 1 and rank(module(n)[0]) > rank(n), "unsafe progression failed")
    print(f"{mergers} strict equal-time lower-rank witnesses; "
          f"{mid} mid-module meetings resynchronized; 16 unsafe unit lifts.")


if __name__ == "__main__":
    main()
