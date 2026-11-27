"""Exact clock-unrestricted common-grade return counts for (Y, 3Y-1)."""

from functools import lru_cache


def events(lower_grade, upper_grade, carry):
    """All blocks of simultaneous halvings ending in at least one odd."""
    removed = min(lower_grade, upper_grade + 1)
    zeros = 0
    while True:
        parities = [(1, 0), (0, 1)] if carry % 2 else [(1, 1)]
        for lower_bit, upper_bit in parities:
            next_lower = lower_grade + lower_bit
            next_upper = upper_grade + upper_bit
            next_removed = min(next_lower, next_upper + 1)
            scale = 3 ** (lower_bit + upper_bit + removed - next_removed)
            c1 = 3 ** (next_lower - next_removed) * upper_bit
            c2 = 3 ** (next_upper + 1 - next_removed) * lower_bit
            doubled = scale * carry + c1 - c2
            if doubled % 2:
                raise ArithmeticError("nonintegral carry")
            if doubled:
                yield next_lower, next_upper, doubled // 2, zeros + 1
        if carry % 2:
            break
        carry //= 2
        zeros += 1


def count_returns(grade):
    """All contextual return words and their maximum clock, without a clock cutoff."""
    @lru_cache(maxsize=None)
    def visit(lower, upper, carry):
        if lower == upper == grade:
            magnitude = -carry
            if magnitude > 0 and magnitude & (magnitude-1) == 0:
                return 1, magnitude.bit_length()-1
            return 0, 0
        count, maximum = 0, 0
        for next_lower, next_upper, next_carry, clock in events(lower, upper, carry):
            if next_lower > grade or next_upper > grade:
                continue
            remaining, tail_clock = visit(next_lower, next_upper, next_carry)
            if remaining:
                count += remaining
                maximum = max(maximum, clock + tail_clock)
        return count, maximum

    answer = visit(0, 0, -1)
    visit.cache_clear()
    return answer


def census(limit):
    totals = [1]
    first = [0]
    rows = []
    for grade in range(1, limit+1):
        total, longest = count_returns(grade)
        decomposable = sum(first[p] * totals[grade-p] for p in range(1, grade))
        primitive = total - decomposable
        if primitive < 0:
            raise ArithmeticError("invalid first-return decomposition")
        totals.append(total)
        first.append(primitive)
        rows.append({"grade": grade, "all": total, "first": primitive, "max_clock": longest})
    return rows
