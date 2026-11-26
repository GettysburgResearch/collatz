"""Exact replay of the bounded-branch rank-three prefix and first-cycle tests."""

import json


def require(condition, reason):
    if not condition:
        raise ValueError(reason)


def step(x):
    return (3*x+1)//2 if x%2 else x//2


def run(h, x):
    p = 0
    for _ in range(h):
        p += x%2
        x = step(x)
    return x, p


def check():
    grid = 2**18
    missed = {2: {6}, 3: {6, 8}, 4: {6, 8, 10}, 5: {6, 7, 8, 10}}
    queries = []
    for e, H, h, a, w, v in ((8, 13, 8, 6561, 5537, 584),
                              (10, 19, 14, 109985, 92801, 12388)):
        for k in range(e+3, H):
            z, rem = divmod(2**k-15-2**(e+2), 81)
            require(rem or z < 1 or z%48 != 17, "unexpected low-clock query site")
        D = 2**H
        require(0 < a < D and (81*a+15+2**(e+2))%D == 0, "parent query class")
        y, p = run(5, a)
        b, q = run(h, 3*w)
        require(y == w and b == v, "query path constants")
        dw = 3**p*2**(H-5)
        k, rem = divmod(3*dw, 2**h)
        require(rem == 0, "upper lift parity budget")
        dv = 3**q*k
        require(w%48 == 17 and dw%48 == 0, "canonical query")
        require(w < a and dw < D, "query below parent")
        require(0 < v and 1024*v < 243*a and 1024*dv < 243*D, "query triple floor")
        queries.append({"e": e, "parent": [a, D], "lower_at_5": [w, dw],
                        "upper_clock": h, "upper_site": [v, dv]})
    rows = []
    bases = []
    for e in range(6, 49):
        a = (-(15+2**(e+2))*pow(81, -1, grid)) % grid
        require((81*a+15+2**(e+2))%grid == 0, "wrong lower binary class")
        windows = {}
        for r in range(2, 6):
            for h in range(19):
                b, p = run(h, a)
                if 4**r*b < 3**r*a and 4**r*3**p < 3**r*2**h:
                    windows[r] = [h, p]
                    break
            require((r not in windows) == (e in missed[r]), "prefix classification")
        rows.append({"e": e, "binary_residue": a, "clock_and_odds_by_r": windows})
        for H in range(e+3, 50):
            z, rem = divmod(2**H-15-2**(e+2), 81)
            if rem or z < 1 or z%48 != 17:
                continue
            require(H >= 18 and z % grid == a, "small upper clock or wrong lift")
            if z >= 2**40:
                continue
            x, h = z, 0
            while x != 1 and h <= 1000:
                x, h = step(x), h+1
            require(x == 1, "small ordinary source")
            bases.append([e, H, z, h])
    require(run(10, 929) == (221, 5) and step(147) == 221, "gap-seven merger")
    require(4**5*147 < 3**5*929 and 4**5*162 < 3**5*1024, "gap-seven floor")
    require(run(7, 33) == (22, 4) and run(5, 31) == (242, 5), "on-cycle gap six")
    require(16*31+7 < 3*242 and 16*32 < 3*243, "cycle ceiling violation")
    require(len(bases) == 5, "unexpected small-source population")
    return {"binary_modulus": grid, "finite_prefixes": rows, "small_sources_e_H_z_hit": bases,
            "smaller_canonical_queries": queries,
            "remaining_e_by_r": {"2": [], "3": [6], "4": [6], "5": [6]}}


if __name__ == "__main__":
    print(json.dumps(check(), indent=2))
