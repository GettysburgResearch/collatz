"""Ternary control at 590 with an independently unbounded initial offset."""
import json
from fractions import Fraction
from functools import cache


def require(condition, message):
    if not condition:
        raise ValueError(message)


@cache
def reflected(y, budget):
    while y != 1:
        if budget < 0 or y > 1 << budget:
            return False
        if y % 2:
            y = (3*y-1)//2
        else:
            y //= 2
            budget -= 1
    return budget == 0


def main():
    N, cap = 590, Fraction(128, 81)
    forms, max_time, max_site, max_U = {}, 0, 0, 0
    for x in range(1, int(N*cap)+1):
        point, h, p = x, 0, 0
        while True:
            max_site, max_time = max(max_site, point), max(max_time, h)
            U = 0
            # The lower integration bound exhausts all U beyond a data-dependent cutoff.
            while (N << U)-1 <= point:
                max_U = max(max_U, U)
                remaining = 0
                while ((N << U)-1) << remaining <= point:
                    y = (N << (U+remaining))-point
                    if 1 <= y <= 1 << remaining and reflected(y, remaining):
                        slope = Fraction(1 << (U+remaining+h), 3**p)
                        center = slope*N-x
                        if slope <= cap and 1 <= center <= 1 << (h-p+remaining):
                            forms.setdefault(U, set()).add((slope, center))
                    remaining += 1
                U += 1
            if point == 1:
                break
            odd = point % 2
            point = (3*point+1)//2 if odd else point//2
            h += 1
            p += odd
            require(h <= 113, "ordinary first hit bound")
    expected = {tuple(map(Fraction, row)) for row in [
        ("8/9", "13/9"), ("1", "1"), ("256/243", "623/243"), ("32/27", "61/27"),
        ("4/3", "5/3"), ("1024/729", "2735/729"), ("128/81", "271/81")
    ]}
    require(forms == {0: expected}, "all-offset center enumeration")
    require((max_site, max_time, max_U) == (125252, 113, 7), "ordinary range")
    bound = 1-Fraction(1180, 10000)*cap**2
    print(json.dumps(dict(center=N, sources=int(N*cap), max_site=max_site,
                          max_time=max_time, max_initial_offset=max_U,
                          positive_depth_candidates={u: sorted((str(a),str(b)) for a,b in R)
                                                     for u,R in forms.items()},
                          haar_lower_bound=str(bound)), indent=2))


if __name__ == "__main__":
    main()
