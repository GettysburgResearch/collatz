"""Literal all-smaller-source and all-clock test of the postpeak classification."""
import json


def run(x, count):
    result = [(x, 0)]
    grade = 0
    for _ in range(count):
        parity = x % 2
        x = (3 * x + 1) // 2 if parity else x // 2
        grade += parity
        result.append((x, grade))
    return result


def require(value, message):
    if not value:
        raise ValueError(message)


def evaluate(m):
    max_i = (m - 1) // 3
    original = run(3**m - 1, max_i)
    observed = predicted = 0
    starts = set()
    prepeak = postpeak = 0
    pure = {t: run(3**t - 1, max_i) for t in range(1, m)}
    witnesses = set()
    for t, path in pure.items():
        for i, ((a, p), (b, q)) in enumerate(zip(original, path)):
            if a == b:
                require(m + p == t + q, "grade compensation")
                witnesses.add((t, i))
                for d in range(t + 1):
                    if 2**(t - d) * 3**d < 2**m:
                        predicted += 1
    for x in range(1, 2**m - 1):
        shifted = x + 1
        n = (shifted & -shifted).bit_length() - 1
        b = shifted >> n
        path = run(x, n + m - 1)
        for i, (y, p) in enumerate(original):
            last_l = m - 2 * i - 1
            prepeak += n
            postpeak += last_l + 1
            for h, (z, g) in enumerate(path[: n + last_l + 1]):
                if y != z:
                    continue
                observed += 1
                starts.add(x)
                require(h == n + i, "lower clock")
                d = m + p - g
                require(d >= 0 and b == 3**d, "cofactor")
                require((n + d, i) in witnesses, "pure peak")
    require(predicted == observed, "completeness")
    return {
        "m": m,
        "smaller_starts": 2**m - 2,
        "prepeak_clock_pairs": prepeak,
        "postpeak_clock_pairs": postpeak,
        "meeting_tuples": observed,
        "distinct_visitors": len(starts),
        "earlier_peak_time_pairs": sorted(witnesses),
    }


def beyond_cone():
    # An unrestricted earlier merger need not have the stated height, clock or grade.
    for m in range(2, 16):
        for x in range(1, 2**m - 1):
            shifted = x + 1
            n = (shifted & -shifted).bit_length() - 1
            b = shifted >> n
            if b in (3**d for d in range(m + 2)):
                continue
            for i, (y, _) in enumerate(run(3**m - 1, 25)):
                for h, (v, _) in enumerate(run(x, n + 25)):
                    if h >= n and y == v and y > 2:
                        return dict(m=m, x=x, n=n, b=b, i=i, l=h-n, meeting=y)
    raise ValueError("missing counterexample")


if __name__ == "__main__":
    print(json.dumps({"checked": [evaluate(m) for m in range(1, 15)],
                      "unrestricted_control": beyond_cone()}, indent=2))
