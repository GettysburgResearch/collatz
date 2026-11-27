"""Evaluate every charged rotation certificate directly at the origin and unit vectors."""
from fractions import Fraction
from itertools import product
from pathlib import Path
import json


DIRECTORY = Path(__file__).resolve().parent
REPORT = DIRECTORY.parents[2] / "reports/astra-infinite-descent-20261127/cycles/ROTATION_DENOMINATORS.json"
SCALE = 10000


def values(count, wrapped, slope, orientation, point):
    times = point[:count]
    lag = point[count]
    start = count + 1
    heights, translated, excess, shifted_excess, low, extra, arc = (
        point[start + j * count:start + (j + 1) * count] for j in range(7)
    )
    slopes = slope - SCALE
    lengths = [times[i] - times[i - 1] + (i == 0) for i in range(count)]
    rows = {"half_lag": SCALE // 2 - SCALE * lag}
    first_list = list(zip(times, heights, excess))
    indices = [*range(count - wrapped, count), *range(count - wrapped)]
    second_list = [
        (times[i] + lag - (i >= count - wrapped), translated[i], shifted_excess[i])
        for i in indices
    ]
    for track, ordered in enumerate((first_list, second_list)):
        prior_time = prior_height = paid = 0
        for j, (time, height, cost) in enumerate(ordered):
            interval = time - prior_time
            paid += cost
            rows[f"time_{track}_{j}"] = interval * SCALE
            rows[f"prefix_{track}_{j}"] = slopes * time - (paid + height) * SCALE
            if j:
                rows[f"step_{track}_{j}"] = slopes * interval + (prior_height - height - cost) * SCALE
            prior_time, prior_height = time, height
        rows[f"end_{track}"] = (1 - prior_time) * SCALE

    for i in range(count):
        bounds = {
            "low_left": heights[i] - low[i],
            "low_right": translated[i] - low[i],
            "extra_left": heights[i] - extra[i],
            "extra_right": translated[i] - extra[i],
            "extra_excess": excess[i] + shifted_excess[i] - extra[i],
            "duration": arc[i] - lengths[i],
            "start_cap": heights[i - 1] + translated[i - 1] - low[i - 1] - arc[i],
        }
        rows.update({f"{label}_{i}": SCALE * bound for label, bound in bounds.items()})
        left = slope * lengths[i] + SCALE * (heights[i - 1] - heights[i] - excess[i])
        right = slope * lengths[i] + SCALE * (translated[i - 1] - translated[i] - shifted_excess[i])
        rows[f"left_clock_{i}"] = arc[i] * SCALE - left
        rows[f"right_clock_{i}"] = arc[i] * SCALE - right
        if orientation[i] in ("L", "R"):
            if orientation[i] == "L":
                higher, lower, clock = heights, translated, left
            else:
                higher, lower, clock = translated, heights, right
            rows[f"orient_{i}"] = SCALE * (higher[i - 1] - lower[i - 1])
            rows[f"upper_clock_{i}"] = clock - SCALE * arc[i]
            rows[f"separation_{i}"] = SCALE * (higher[i - 1] - arc[i])
        for size in range(1, count + 1):
            chain = [j % count for j in range(i - size + 1, i + 1)]
            cost = sum(excess[j] + shifted_excess[j] + low[j] for j in chain[:-1])
            terminal = heights[i] + translated[i] + extra[i] - arc[(i + 1) % count]
            rows[f"chain_{i}_{size}"] = SCALE * (terminal + cost) - slope * sum(lengths[j] for j in chain)
    return rows


def error_charge(label):
    if label.startswith("prefix_"):
        return int(label.split("_")[-1]) + 2
    if label.startswith("step_"):
        return 2
    return int(label.startswith("upper_clock_"))


def charged_maximum(count, wrapped, signs, weights):
    dimension = 8 * count + 1
    if not weights or any(type(w) is not int or w <= 0 for w in weights.values()):
        raise ValueError("nonpositive or nonintegral weight")

    def evaluate(point, slope):
        row = values(count, wrapped, slope, signs, point)
        return sum(row[name] * weight for name, weight in weights.items())

    maxima = []
    for slope in (15849, 15850):
        point = [0] * dimension
        origin = evaluate(point, slope)
        maximum = origin
        for i in range(dimension):
            point[i] = 1
            maximum += max(0, evaluate(point, slope) - origin)
            point[i] = 0
        maxima.append(Fraction(maximum, SCALE * sum(weights.values())))
    tax = sum(error_charge(key) * weight for key, weight in weights.items())
    return max(maxima) + Fraction(tax, 4096 * sum(weights.values()))


def main():
    trees = json.loads((DIRECTORY / "rotation_denominator_duals.json").read_text())
    records = json.loads(REPORT.read_text())
    if not 2 ** 15849 < 3 ** SCALE < 2 ** 15850:
        raise ValueError("logarithm slope bracket")
    order_types = [(s, w) for s in range(2, 7) for w in range(s + 1)]
    if set(trees) != {f"{s},{w}" for s, w in order_types} or len(records) != len(order_types):
        raise ValueError("incomplete order types")
    maxima = []
    for count, wrapped in order_types:
        record = next(row for row in records if (row["mismatches"], row["wrapped"]) == (count, wrapped))
        leaves = {row["higher_sides"]: Fraction(row["charged_upper"]) for row in record["leaves"]}
        seen = set()
        for sides in product("LR", repeat=count):
            node = trees[f"{count},{wrapped}"]
            chosen = ["*"] * count
            while "weights" not in node:
                i = node["branch"]
                if not 0 <= i < count or chosen[i] != "*":
                    raise ValueError("invalid branch")
                chosen[i] = sides[i]
                node = node[sides[i]]
            name = "".join(chosen)
            if name not in seen:
                maximum = charged_maximum(count, wrapped, name, node["weights"])
                if maximum != leaves[name] or maximum >= 0:
                    raise ValueError((count, wrapped, name, maximum, leaves[name]))
                maxima.append(maximum)
                seen.add(name)
        if seen != set(leaves) or len(seen) != len(record["leaves"]):
            raise ValueError("invalid reported leaf coverage")
    print(json.dumps({"order_types": len(order_types), "leaves": len(maxima),
                      "largest_charged_upper": str(max(maxima))}, indent=2))


if __name__ == "__main__":
    main()
