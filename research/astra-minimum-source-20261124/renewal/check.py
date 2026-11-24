"""Exact ordinary replay of first-exit and dyadic representative identities."""
import json


def check(condition):
    if not condition:
        raise AssertionError("ordinary representative identity failed")


def step(value):
    return (3 * value + 1) // 2 if value % 2 else value // 2


def run(value, count):
    for _ in range(count):
        value = step(value)
    return value


def first_exits():
    counts = {"twelve_five": 0, "nine_zero": 0, "nine_three": 0, "complementary": 0}
    for a in range(2, 49):
        for b in range(1, 1024, 2):
            upper = (1 << a) * b - 1
            if upper % 3 or upper <= 3:
                continue
            q = upper // 3
            r = 3**a * b
            check(run(upper, a) == r - 1)
            y = (upper - 1) // 2
            if r % 4 == 1:
                check(run(upper, a + 2) == run(y, a + 1) == (r - 1) // 4)
                if q % 12 == 5:
                    small = 8 * (q // 12) + 3
                    check(small % 2 and 0 < small < q and run(3 * small, 2) == y)
                    counts["twelve_five"] += 1
                if q % 4 == 1 and q % 9 in (0, 3):
                    z = 4 * (q // 3) - 1
                    check(run(z, 3) == y)
                    if q % 9 == 0:
                        small = (2 * z - 1) // 3
                        check(0 < small < q and step(small) == z)
                        counts["nine_zero"] += 1
                    else:
                        small = z // 3
                        check(0 < small < q and small % 2 and 3 * small == z)
                        counts["nine_three"] += 1
            s = r // 9
            if s % 256 == 147:
                small = (upper - 3) // 4
                check(0 < small < q)
                check(run(upper, a + 8) == run(small, a + 6))
                counts["complementary"] += 1
    check(min(counts.values()) > 0)
    return counts


def main():
    for t in (*range(1, 2049), 10**30):
        q = 8192 * t - 21
        a = run(q, 5)
        check(0 < a < q and a % 6 == 1 and a == 6912 * t - 17)
        check(run(3 * q, 13) == run(3 * a, 8) == 2187 * t - 5)
        check(run(3 * (8 * t - 1), 3) == step(6 * t - 1) == 9 * t - 1)
    check(5**5 > 3 * 4**5)
    print(json.dumps({"dyadic_lifts_per_family": 2049, "first_exits": first_exits()}, indent=2))


if __name__ == "__main__":
    main()
