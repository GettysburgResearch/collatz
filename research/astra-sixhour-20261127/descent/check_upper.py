"""Independent integer/rational replays for the supplied upper-word theorems."""
from json import dumps
from math import prod


def require(value, why):
    if not value:
        raise ValueError(why)


def step(n):
    return (3*n+1)//2 if n % 2 else n//2


def first(n, limit=20000):
    x, p = n, 0
    for h in range(limit + 1):
        if x == 1:
            return h, p
        p += x % 2
        x = step(x)
    raise ValueError(("upper first hit exceeded finite replay budget", n, limit))


def physical(n, h):
    p = 0
    for _ in range(h):
        p += n % 2
        n = step(n)
    return n, p


def reduce_center(a, k):
    initial = a
    require(k == 0 or a % 3 != 0, "initial fraction not reduced")
    t = 0
    while k:
        require(a % 3 != 0, ("nonunit", t, k, a))
        if a % 2:
            k -= 1
            a += 3**k
        require(a % 2 == 0, "inexact signed step")
        a //= 2
        t += 1
    if a < 0:
        require((1 << t)*(-a) <= -initial, "negative exit budget")
    return t, a


def full_center(z, H, r):
    a = 3**(r+1)*z-(1 << H)
    t, c = reduce_center(a, r+1)
    require((1 << t)*max(1, abs(c)) <= max(1, abs(a))*prod(1+3**j for j in range(r+1)),
            "time-height budget")
    if t <= H:
        require(physical(z, t) == ((1 << (H-t))+c, r+1), "ordinary lower lifting")
    return t, c


def ordinary_controls():
    cases = {}
    for z in range(17, 17+48*480, 48):
        H, r = first(3*z)
        t, c = full_center(z, H, r)
        padded_H, padded_r = H+2*r, 2*r
        require(physical(3*z, padded_H) == (1, padded_r), "upper padding")
        low_H, _ = first(z)
        t2, c2 = full_center(z, padded_H, padded_r)
        if low_H >= padded_H:
            require(t2 <= padded_H, "padded signed time")
            require(physical(z, padded_H)[1] >= 2*r+1, "paid grade")
        key = ("negative" if c < 0 else "zero" if c == 0 else "positive",
               "within" if t <= H else "beyond",
               "earlier lower hit" if low_H < padded_H else "forced paid grade")
        name = " / ".join(key)
        cases[name] = cases.get(name, 0)+1
    return cases


def suffix_samples():
    u = 5
    results = []
    require(pow(2, 162, 243) == 1 and pow(2, 81, 243) != 1 and pow(2, 54, 243) != 1,
            "order modulo 243")
    for s in range(1, 10):
        h, count = first(u)
        require(count == s and u % 2 and u % 3, "bad supplied suffix")
        A = (1 << h)-3**s*u
        require(A > 0 and A % 3 != 0, "bad suffix carry")
        row = []
        for lift in range(3):
            e0 = next(e for e in range(162) if (pow(2, e+5, 243)*u) % 243 == 103)
            e = e0+(lift+2)*162
            numerator = (1 << (e+9))*u-271
            z, rem = divmod(numerator, 81)
            require(rem == 0 and z % 48 == 17, "canonical positive source")
            H, r = first(3*z)
            require((H, r) == (e+9+h, 3+s), "supplied true first hit")
            t, c = full_center(z, H, r)
            require((t, c) == (7+s, -1-(1 << (e+2-s))*A), "full exit")
            require(physical(z, 7) == ((1 << (e+2))*u-1, 4), "opening")
            require(physical(z, e+9)[0] == 3**(e+2)*u-1, "peak")
            extra = (3**e//(1 << e)).bit_length()-1
            require((1 << (extra+e)) <= 3**e < (1 << (extra+e+1)),
                    "integer surplus deadline")
            stop = e+9+extra
            x = z
            for i in range(stop+1):
                require(16*x >= 9*z, ("premature contraction", s, e, i))
                x = step(x)
            row.append({"e": e, "original_bits": z.bit_length(), "exit_clock": t,
                        "negative_exit_bits": (-c).bit_length(), "height_floor_clock": stop,
                        "upper_first_hit": H})
        results.append({"suffix_odd_count": s, "u": str(u), "suffix_clocks": h, "rows": row})
        j = next(j for j in range(4, 11) if ((1 << j)*u) % 9 in (4, 7))
        u = ((1 << j)*u-1)//3
    return results


if __name__ == "__main__":
    print(dumps({"ordinary_parents": ordinary_controls(), "supplied_suffixes": suffix_samples()},
                indent=2, sort_keys=True))
