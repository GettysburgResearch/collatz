"""Replay the positive short-run construction at four ternary exponents."""


def run(n, clocks):
    for _ in range(clocks):
        n = (3*n+1)//2 if n % 2 else n//2
    return n


for r, k in ((2, 122), (3, 68), (4, 878), (5, 3308)):
    n0 = (2**(k+2)-7)//9
    v = n0//3**r
    if n0 != 3**r*v or v % 2 != 1 or v % 3 == 0 or run(n0, k+2) != 1:
        raise ValueError("reference source")
    for t in (1, 8, 17):
        w = v + 12*2**(k+2)*t
        lower = v + 9*2**(k+2)*t
        n = 3**r*w
        if not 0 < lower < w or n % 512 != 113 or w % 3 == 0:
            raise ValueError("lifted source")
        if run(n, k+4) != run(3**r*lower, k+2):
            raise ValueError("physical merger")
    print(f"r={r}, reference clocks={k+2}: three strictly smaller-base mergers")
