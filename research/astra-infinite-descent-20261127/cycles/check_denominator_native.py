"""Check high-start corrections and all-minimum split chains on native rational cycles."""
from collections import Counter
import json

from check_cycle_rotations import necklaces, rational_labels


def require(ok, description):
    if not ok:
        raise ValueError(description)


def check_rotation(values, exponents, denominator, lag, totals):
    period = len(values)
    ends = [i for i in range(period) if exponents[i] != exponents[(i + lag) % period]]
    count = len(ends)
    if not 2 <= count <= 6:
        return
    blocks = []
    for n, end in enumerate(ends):
        start = ends[n - 1] + 1
        length = (end + 1 - start) % period
        left, right = values[start % period], values[(start + lag) % period]
        higher = max(left, right)
        carried = common = 0
        for elapsed in range(length):
            carried = 3 * carried + 2 ** common
            a = exponents[(start + elapsed) % period]
            b = exponents[(start + elapsed + lag) % period]
            require(a == b or elapsed == length - 1, "common interior")
            common += min(a, b)
        quotient, remainder = divmod(right - left, 2 ** common)
        require(not remainder and quotient % 2, "nonzero odd separated quotient")
        require(2 * carried < 3 ** length * higher, "higher-start correction")
        end_left, end_right = values[(end + 1) % period], values[(end + 1 + lag) % period]
        a, b = exponents[end], exponents[(end + lag) % period]
        excess_left, excess_right = max(0, a - b), max(0, b - a)
        excess, terminal = (excess_left, end_left) if higher == left else (excess_right, end_right)
        require(2 ** (common + excess) * terminal == 3 ** length * higher + denominator * carried,
                "actual higher-side affine identity")
        blocks.append((length, common, quotient, end_left, end_right, excess_left, excess_right))
        totals["high_starts"] += 1

    for start in range(count):
        for size in range(1, count + 1):
            coefficient = 1
            terms = []
            total_length = 0
            for delta in range(size):
                i = (start + delta) % count
                length, _, _, y, z, u, v = blocks[i]
                total_length += length
                terms = [3 ** length * term for term in terms]
                minimum = min(y, z)
                if delta == size - 1:
                    terms.extend([coefficient * 2 ** v * minimum, -coefficient * 2 ** u * minimum])
                else:
                    terms.append(coefficient * (2 ** v - 2 ** u) * minimum)
                next_common = blocks[(i + 1) % count][1]
                coefficient *= 2 ** (next_common + (v if minimum == y else u))
            terms.append(coefficient * blocks[(start + size) % count][2])
            require(sum(terms) == 3 ** total_length * blocks[start][2], "expanded cyclic identity")
            sums = {0}
            for term in terms:
                require(-term not in sums, "nonempty split subsum vanishes")
                sums |= {previous + term for previous in sums}
            totals["cyclic_chains"] += 1
            totals["closed_chains"] += (size == count)


def main():
    totals = Counter()
    for clock in range(4, 13):
        for word in necklaces(clock):
            trace = rational_labels(word)
            if trace is None:
                continue
            numerators, denominator, _ = trace
            odd = [i for i, bit in enumerate(word) if bit]
            period = len(odd)
            if period < 2:
                continue
            values = [numerators[i] for i in odd]
            exponents = [(odd[(i + 1) % period] - odd[i]) % clock for i in range(period)]
            for lag in range(1, period // 2 + 1):
                check_rotation(values, exponents, denominator, lag, totals)
    print(json.dumps(dict(sorted(totals.items())), indent=2))


if __name__ == "__main__":
    main()
