"""Compare exact inverse arrays with a forward scan of complete rational grids."""
from fractions import Fraction
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def prefix(x, grade):
    bits = []
    state = x
    odds = 0
    while odds < grade:
        bit = state % 2
        bits.append(bit)
        odds += bit
        state = (3 * state + 1) // 2 if bit else state // 2
    return state, bits


def rational_step(numerator, height):
    if numerator % 2:
        require(height > 0, "should stop at first integer")
        return (numerator + 3 ** (height - 1)) // 2, height - 1
    return numerator // 2, height


def main():
    marks = (1, 3, 4, 7, 9, 10, 19, 31)
    checked = source_count = physical_count = without_hits = 0
    cases = []
    for x in (1, 7, 27, 97, 871, 6171):
        for n in range(1, 8):
            z, bits = prefix(x, n)
            clock = len(bits)
            multiplier = Fraction(3 ** n, 2 ** clock)
            correction = z / multiplier - x
            denominator = 3 ** (n + 1)
            for lo, hi in ((0, 3), (x, x + 3)):
                predicted = {}
                for mark in marks:
                    q = Fraction(2 * mark - 1, 3)
                    h = 0
                    while True:
                        r = (2 ** h * q) / multiplier - correction
                        if r >= hi:
                            break
                        if r > lo:
                            m = r * denominator
                            require(m.denominator == 1 and m.numerator % 3, "full reduced grade")
                            date = clock + h + 1
                            require(Fraction(3 ** n, 2 ** date) == q / (2 * (r + correction)),
                                    "rescaled time identity")
                            require((m.numerator - denominator * x) % (2 ** clock) == 0,
                                    "native cylinder")
                            predicted[m.numerator] = (mark, date)
                        h += 1
                actual = {}
                for m in range(lo * denominator + 1, hi * denominator):
                    if m % 3 == 0:
                        continue
                    source_count += 1
                    d, h = m, n + 1
                    for bit in bits:
                        if d % 2 != bit:
                            break
                        d, h = rational_step(d, h)
                    else:
                        require(h == 1, "prefix left exactly one grade")
                        date = clock
                        while h:
                            d, h = rational_step(d, h)
                            date += 1
                        if d in marks:
                            actual[m] = (d, date)
                require(predicted == actual, "complete physical and inverse arrays disagree")
                checked += 1
                physical_count += len(actual)
                without_hits += not actual
                cases.append([x, n, lo, hi, len(actual)])
    print(json.dumps({"complete_grids": checked, "reduced_sources_scanned": source_count,
                      "matched_sources": physical_count, "empty_grids_for_selected_marks": without_hits,
                      "eligible_marks": marks, "cases": cases}, indent=2))


if __name__ == "__main__":
    main()
