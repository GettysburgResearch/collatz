"""Exact simple-path reciprocal bound above 2^71, including the infinite tail."""
import json
from fractions import Fraction
from math import comb


FLOOR_BITS = 71
BARRIER_CUTOFF = 350
FINAL_CUTOFF = 1500


def require(test, message):
    if not test:
        raise ArithmeticError(message)


def count_bounds():
    # lengths[q] is ceil(log2(3^q)), including the equality at q=0.
    lengths = [(3**q - 1).bit_length() for q in range(FINAL_CUTOFF + 1)]
    caps = [0] * (FINAL_CUTOFF + 1)
    for k in range(FLOOR_BITS + 1, FINAL_CUTOFF + 1):
        best = 2**k
        if k <= BARRIER_CUTOFF:
            counts = [1]
            for h in range(1, k + 1):
                counts = [a + b for a, b in zip([0] + counts, counts + [0])]
                # Strict upper state bound 2^(k-h)3^p > 2^71 is necessary.
                for p in range(h + 1):
                    if lengths[p] + k - h > FLOOR_BITS:
                        break
                    counts[p] = 0
                d = k - h
                if d > 8:
                    continue
                lifts = 2**d - (2**d // 3)
                tail = 0
                for q in range(h, -1, -1):
                    target = lengths[q] + d
                    if target < k:
                        best = min(best, h + caps[target] + lifts * tail)
                    tail += counts[q]
        else:
            # One valid parity split suffices in the negligible far tail.
            q = 3 * k // 5
            target = lengths[q]
            if target < k:
                term = comb(k, q + 1)
                tail = term
                for p in range(q + 1, k):
                    term = term * (k - p) // (p + 1)
                    tail += term
                best = min(best, k + caps[target] + tail)
        caps[k] = best
    return caps


def kernel_budget():
    # Independent exact arithmetic for FloorCertificate's unpruned shell proof.
    cutoff = 325
    finite = Fraction()
    for j in range(FLOOR_BITS, cutoff):
        n = j + 1
        q = 41 * j // 65
        tail = sum(comb(n, p) for p in range(q + 1, n + 1))
        finite += Fraction(n + tail, 2**j)
    ratio = Fraction(31, 32)
    reserve = Fraction(2 * (cutoff + 2), 2**cutoff) + Fraction(256, 3) * ratio**cutoff
    require(3**41 < 2**65, "power cutoff")
    require(Fraction(4, 3)**65 * Fraction(3, 5)**41 <= ratio**65, "tilted power bound")
    require(finite <= Fraction(993, 1000), "finite unpruned sum")
    require(reserve < Fraction(3, 1000), "infinite unpruned reserve")
    # The sum of the pointwise inequalities has a single boundary difference.
    even_upper = (Fraction(249, 250) + Fraction(3, 10000)) / Fraction(3999, 1000)
    require(even_upper < Fraction(1, 4), "even telescoping")
    return {
        "cutoff": cutoff,
        "finite_eight_decimal_upper": ceil_scaled(finite),
        "reserve_eight_decimal_upper": ceil_scaled(reserve),
        "all_sites_strict_bound": "249/250",
        "even_departures_strict_bound": "1/4",
    }


def ceil_scaled(value):
    return (value.numerator * 10**8 + value.denominator - 1) // value.denominator


def main():
    caps = count_bounds()
    k = FINAL_CUTOFF
    finite = sum((Fraction(upper, 2**j) for j, upper in enumerate(caps)), Fraction())
    r = Fraction(99, 100)
    require(Fraction(5, 4)**5 * Fraction(2, 3)**3 < r**5, "Chernoff tail ratio")
    require(Fraction(3**3, 2**5) < r**5, "small endpoint ratio")
    tail = 2 * r**(k + 1) / (1-r) + Fraction(k+2, 2**k)
    # Each even departed state maps to a different site of half its size.
    total = (finite + tail) / 2
    require(total < Fraction(7, 25), "advertised correction")
    print(json.dumps({
        "floor_bits": FLOOR_BITS,
        "barrier_cutoff": BARRIER_CUTOFF,
        "tail_cutoff": k,
        "finite_eight_decimal_upper": ceil_scaled(finite),
        "tail_eight_decimal_upper": ceil_scaled(tail),
        "even_total_eight_decimal_upper": ceil_scaled(total),
        "strict_rational_bound": "7/25",
        "kernel_unrestricted_certificate": kernel_budget(),
    }, indent=2))


if __name__ == "__main__":
    main()
