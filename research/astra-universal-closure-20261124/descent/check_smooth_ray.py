"""Complete integer checks for the bounded candidate sets in SMOOTH_RAY.md."""


def defect(seed):
    z = seed
    odds = 0
    for clock in range(5000):
        if z == 1:
            return clock - 2*odds
        odds += z % 2
        z = (3*z+1)//2 if z % 2 else z//2
    raise ValueError(f"clock limit reached for {seed}")


for m, a, r, w, e, candidates in (
    (4, 1, 1, 5, 4, 5),
    (2, 1081, 1, 1441, 9, 8),
    (5, 20153, 3, 23885, 1, 76),
    (5, 149051, 3, 176653, 9, 37),
):
    b = 3**m*a - 1
    if not (2**m*a-1 == 3**r*w and w % 3 and a < w and b % (2**(e+1)) == 2**e):
        raise ValueError("source shape")
    target = defect(b) - 2*m
    for k in range(candidates+1):
        eligible = 4**k * 2**max(0, target) <= a*3**k * 2**max(0, -target)
        if eligible != (k < candidates):
            raise ValueError("power cutoff")
        if eligible and defect(3**k*a)-2*k == target:
            raise ValueError("unexpected affine meeting")
    print(f"m={m} a={a} e={e} verified all {candidates} eligible powers; target={target}")
