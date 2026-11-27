"""Ordinary positive controls for the canonical upper-clock barrier."""
import json


def run(value, clocks):
    odds = []
    trail = [value]
    for j in range(clocks):
        if value % 2:
            odds.append(j)
            value = (3 * value + 1) // 2
        else:
            value //= 2
        trail.append(value)
    return trail, odds


def check(test, description):
    if not test:
        raise ValueError(description)


def controls():
    half_gap = (2**136 - 241) // 81
    rows = []
    for index in range(9):
        height = 18 + 162 * index
        z, remainder = divmod(2**height - 271, 81)
        check(remainder == 0 and z % 48 == 17, "hard source")
        arm, odds = run(3 * z, height)
        check(arm.index(1) == height and odds == [0, 1, 8], "upper first hit")
        lower, _ = run(z, height)
        for i in range(7, height + 1):
            check(lower[i] + 1 == 2**(height - i) * 3**(i - 7), "native ascent")
        entry = {"H": height, "native_upper_odds": odds}
        if index:
            y, remainder = divmod(2 ** (height - 1) - 15 - 2**135, 81)
            check(remainder == 0 and y % 48 == 17, "shorter source")
            alternate, odds = run(3 * y, height - 1)
            check(alternate.index(1) == height - 1 and odds == [0, 1, 135], "shorter first hit")
            check(z - 2 * y == half_gap, "asymptotic ratio")
            entry.update(shorter_upper_odds=odds, shorter_clock=height - 1)
        rows.append(entry)
    return {"half_gap": str(half_gap), "row_controls": rows}


if __name__ == "__main__":
    print(json.dumps(controls(), indent=2))
