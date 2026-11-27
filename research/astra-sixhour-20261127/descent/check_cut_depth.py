"""Numerical ordinary-neighborhood checks at 590-obstruction controls."""
from json import dumps


def require(test, msg):
    if not test:
        raise ArithmeticError(msg)


def step(n):
    return (3*n+1)//2 if n%2 else n//2


def exponent(u, precision, minimum):
    residue, period, modulus = 0, 2, 3
    if pow(2, residue+2, modulus)*u % modulus != 590 % modulus:
        residue = 1
    while modulus < 3**precision:
        modulus *= 3
        admissible = [residue+j*period for j in range(3)
                      if pow(2, residue+j*period+2, modulus)*u % modulus == 590 % modulus]
        require(len(admissible) == 1, "lifting residue")
        residue = admissible[0]
        period *= 3
    if residue < minimum:
        residue += ((minimum-residue+period-1)//period)*period
    return residue


def numerical_row(u, depth, e=None):
    t = depth+7
    if e is None:
        e = exponent(u, t+2, 4*t+10)
    N = (1 << (e+2))*u
    require(N % 3**(t+2) == 590 % 3**(t+2), "wrong ternary control")
    z, remainder = divmod(128*N-271, 81)
    require(remainder == 0 and z%48 == 17 and N > 1000*12**t, "bad original")
    low, high = z, 3*z
    for _ in range(7):
        low = step(low)
    for _ in range(9):
        require(high > 1, "early upper hit")
        high = step(high)
    require(low == N-1 and high == 2**e*u, "incorrect physical opening")
    seen = {z}
    frontier = {z}
    sizes = [1]
    for _ in range(depth):
        new = set()
        for v in frontier:
            new.update((step(v), 2*v))
            if v % 3 == 2:
                new.add((2*v-1)//3)
        new.difference_update(seen)
        seen.update(new)
        frontier = new
        sizes.append(len(new))
    require(3*z not in seen, "zero-jump shortcut")
    require(all(16*x >= 9*z for x in seen), "physical floor")
    require(all(x%48 != 17 or x >= z for x in seen), "physical smaller query")
    end, suffix_h, suffix_p = u, 0, 0
    while end != 1 and suffix_h < 20000:
        suffix_p += end%2
        suffix_h += 1
        end = step(end)
    require(end == 1, "upper cofactor did not first-hit within the finite budget")
    return {"suffix_start": u, "forbidden_walk_length": depth, "exponent": e,
            "upper_first_hit_clock": e+9+suffix_h, "upper_first_hit_rank": 3+suffix_p,
            "original_bit_length": z.bit_length(), "ordinary_shell_sizes": sizes}


if __name__ == "__main__":
    rows = [numerical_row(u, h) for u in (1, 5) for h in (1, 3, 4)]
    varying = []
    for depth in (8, 12, 16, 20, 24):
        e, K = 4*(depth+7)+10, depth+9
        mod = 3**K
        u = 590*pow(2, -e-2, mod) % mod
        if u%2 == 0:
            u += mod
        varying.append(numerical_row(u, depth, e))
    print(dumps({"fixed_rank_controls": rows, "varying_rank_controls": varying},
                indent=2, sort_keys=True))
