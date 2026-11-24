"""Replay the finite ordinary-source controls in LINEAR_HORIZON.md."""
import json


def check(condition, t, description):
    if not condition:
        raise ValueError(f"T={t}: {description}")


def trajectory(source, clocks):
    values = [source]
    for _ in range(clocks):
        q = values[-1]
        values.append((3 * q + 1) // 2 if q % 2 else q // 2)
    return values


def verify(t):
    k = 2 * t
    modulus = 2**t
    r = pow(3, -k, modulus)
    u = 2 ** (2 * t - 1) + r
    n = 2 ** (k + 1) * u - 1
    x = (n - 1) // 2
    b = 3**k * u - 1
    octave = n.bit_length() - 1
    check((n + 1) & -(n + 1) == 2 ** (k + 1), t, "canonical valuation")
    check(n % 2 == 1 and octave == 4 * t, t, "odd source in target octave")
    check((octave + 1) * (n - 2**octave) <= 70 * 2**octave, t, "marked band")
    check(b % modulus == 0, t, "post-rise congruence")
    check(b % 4 != 2 and b % 2 != 1 and b % 64 != 56, t, "grammar rejection")
    source_values = trajectory(n, 3 * t + 1)
    partner_values = trajectory(x, 3 * t)
    check(source_values[k + 1] == 3 * b + 2, t, "source rising endpoint")
    check(partner_values[k] == b, t, "partner rising endpoint")
    check(min(source_values[1:]) > n, t, "strict growth above start")
    check(set(source_values).isdisjoint(partner_values), t, "independent-clock disjointness")


if __name__ == "__main__":
    first, last = 6, 350
    for t in range(first, last + 1):
        verify(t)
    print(json.dumps({"T_min": first, "T_max": last, "cases": last - first + 1,
                      "status": "pass"}, separators=(",", ":")))
