"""Exact directed flows, triangular digit projections and heavy signed cylinders."""

from collections import deque
from fractions import Fraction


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def order(width):
    modulus = 3 ** width
    period = 2 * modulus // 3
    result = []
    state = 1
    for _ in range(period):
        result.append(state)
        state = (2 * state) % modulus
    require(state == 1 and len(set(result)) == period, "doubling-log order")
    return result


def log_data(parent, circle):
    lower_modulus = len(parent)
    supply = [parent[s % lower_modulus] / 3 for s in circle]
    demand = [parent[(s - 1) // 3] if s % 3 == 1 else Fraction(0) for s in circle]
    require(sum(supply) == sum(demand) == 1, "law normalization")
    return supply, demand


def directed_route(supply, demand):
    period = len(supply)
    total = Fraction(0)
    primitive = []
    for born, used in zip(supply, demand):
        total += born - used
        primitive.append(total)
    require(total == 0, "cyclic balance")
    shift = max(s - f for s, f in zip(supply, primitive))
    flux = [f + shift for f in primitive]
    cut = next(d for d in range(period) if flux[d] == supply[d])
    queue = deque([(cut, supply[cut])]) if supply[cut] else deque()
    arrivals = [Fraction(0)] * period
    departures = [Fraction(0)] * period
    cost = Fraction(0)
    packets = 0
    for distance in range(1, period + 1):
        absolute = cut + distance
        point = absolute % period
        need = demand[point]
        while need:
            require(bool(queue), "unsatisfied target demand")
            start, amount = queue.popleft()
            paid = min(amount, need)
            gap = absolute - start
            require(1 <= gap <= period, "strictly positive routed gap")
            cost += paid * gap
            departures[start % period] += paid
            arrivals[point] += paid
            packets += 1
            need -= paid
            if paid < amount:
                queue.appendleft((start, amount - paid))
        if distance < period and supply[point]:
            queue.append((absolute, supply[point]))
    require(not queue and arrivals == demand and departures == supply, "exact coupling marginals")
    require(sum(flux) == cost, "optimal routed cost equals forced total flux")
    return cost, packets


def refine_geometric(parent, circle, theta):
    _, demand = log_data(parent, circle)
    q = 1 - theta
    period = len(circle)
    # The affine backward recurrence makes one complete cyclic turn.
    current = Fraction(0)
    for i in reversed(range(period)):
        current = theta * demand[(i + 1) % period] + q * current
    current /= 1 - q ** period
    log_law = [Fraction(0)] * period
    for i in reversed(range(period)):
        current = theta * demand[(i + 1) % period] + q * current
        log_law[i] = current
    law = [Fraction(0)] * (3 * len(parent))
    for i, s in enumerate(circle):
        law[s] = log_law[i]
        require(log_law[i - 1] == theta * demand[i] + q * log_law[i], "geometric circle recurrence")
    require(all(sum(law[t::len(parent)]) == mass for t, mass in enumerate(parent)), "projective geometric law")
    return law, log_law


def tent(m, length, d):
    return sum((d + u + length) // m - (d + u) // m for u in range(length))


def check_tents():
    checks = 0
    for m in (2, 6, 18, 54, 162):
        for length in range(1, 25):
            for d in range(m):
                value = tent(m, length, d)
                require(0 <= value and abs(tent(m, length, d + 1) - value) <= 1, "adjacent tent increment")
                require(value == sum(tent(3 * m, length, d + k * m) for k in range(3)), "three-axis projection")
                if (d + length) % m == 0:
                    require(value >= length, "targeted tent peak")
                if m == 2:
                    require(2 * value <= length ** 2 + 1, "width-one tent bound")
                checks += 1
    return checks


def main():
    levels = 0
    packets = 0
    atom_bounds = 0
    tent_checks = check_tents()
    for theta in (Fraction(4, 7), Fraction(3, 5), Fraction(5, 8), Fraction(2, 3)):
        q = 1 - theta
        parent = [Fraction(0), q / (1 + q), 1 / (1 + q)]
        largest_cost = Fraction(0)
        for width in range(2, 6):
            circle = order(width)
            supply, demand = log_data(parent, circle)
            cost, emitted = directed_route(supply, demand)
            law, unflattened = refine_geometric(parent, circle, theta)
            primitive = []
            total = Fraction(0)
            for flat, old in zip(supply, unflattened):
                total += flat - old
                primitive.append(total)
            mean = sum(primitive) / len(circle)
            analytic_cost = 1 / theta + len(circle) * max(s - m / theta - h + mean for s, m, h in zip(supply, unflattened, primitive))
            require(analytic_cost == cost, "independent geometric scalar formula")
            require(parent[-1] >= theta ** (width - 1), "signed fixed-cylinder mass")
            largest_cost = max(largest_cost, cost)
            peak = max(demand)
            for length in range(1, len(circle) + 1):
                require(len(circle) * length * peak <= length ** 2 + 1 + 2 * (len(circle) - 2) * largest_cost, "heavy-atom bound")
                atom_bounds += 1
            parent = law
            levels += 1
            packets += emitted
    # Exact signs independent of the approximated critical parameter.
    require(5 ** 5 > 4 * 3 ** 6 and 3 * Fraction(3, 5) ** 2 > 1, "critical heavy-atom threshold")
    print(f"stationary transports={levels}, positive routed packets={packets}, tent checks={tent_checks}, atom bounds={atom_bounds}")


if __name__ == "__main__":
    main()
