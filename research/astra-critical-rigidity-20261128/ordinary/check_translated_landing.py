"""Exact native controls for a common real translation and first integer landing."""
from collections import Counter, defaultdict
from fractions import Fraction
import json

from check_line_shadow_structure import require


def run(n, numerator):
    require(n > 0 and numerator > 0 and numerator % 3, "invalid reduced input")
    h, d = n, numerator
    path = [(h, d)]
    while h:
        odd = d % 2
        h -= odd
        d, remainder = divmod(d + odd * 3**h, 2)
        require(remainder == 0 and d > 0, "inexact or nonpositive departure")
        require(h == 0 or d % 3, "premature integral landing")
        path.append((h, d))
    return path


def joint_control(n, raw, translate, counts):
    scale = 3**n
    start = raw + scale * translate
    trace = run(n, start)
    residual = Fraction(raw, scale)
    carry = 0
    for t, (h, d) in enumerate(trace):
        value = Fraction(d, 3**h)
        phase = Fraction(translate * 3**(n-h), 2**t)
        require(value == phase + residual and 0 < residual, "wrong translated residual")
        require((2**t) * d == start + 3**h * carry, "native prefix carry")
        counts["residual_dates"] += 1
        if t == len(trace) - 1:
            require((2**t) * d >= start, "lost terminal binary height")
            counts["large_terminal"] += d.bit_length() >= 30
            counts["late_landing"] += t >= 4*n
            break
        bit = d % 2
        residual = (3**bit * residual + bit) / 2
        carry = (3**bit)*carry + bit * 2**t
    # Test the time-plus-height inequality for every maximal above-one tail.
    i = 0
    while i < len(trace) - 1:
        h, d = trace[i]
        if d <= 3**h:
            i += 1
            continue
        j = i + 1
        while j < len(trace)-1 and trace[j][1] > 3**trace[j][0]:
            j += 1
        end_h, end_d = trace[j]
        require(2**(j-i) * end_d * 3**h <= d * 3**end_h * 4**(h-end_h),
                "joint excursion time and terminal height")
        if end_h:
            require(2 * end_d > 3**end_h, "crossing below one missed lower endpoint")
        counts["above_one_segments"] += 1
        i = j
    counts["translated_sources"] += 1


def cohort(n, coast, counts):
    scale = 3**n
    groups = defaultdict(list)
    for m in range(1, scale):
        if m % 3:
            trace = run(n, m)
            t = next(i for i, (h, _) in enumerate(trace) if h == 1)
            groups[(t, trace[t][1])].append((m, trace))
    (t, d), members = max(groups.items(), key=lambda item: (len(item[1]), item[0]))
    modulus = 2**coast
    z = modulus + (-d * pow(scale, -1, modulus)) % modulus
    shift = 2**t * z
    require(modulus <= z < 2*modulus and (d+scale*z) % modulus == 0, "bad coast class")
    for m, original in members:
        lifted = run(n, m + scale * shift)
        for i, (h, old_d) in enumerate(original[:t+1]):
            require(lifted[i] == (h, old_d + scale * z * 2**(t-i)), "physical prefix shift")
        for delta in range(coast+1):
            require(lifted[t+delta] == (1, (d+scale*z) // 2**delta), "lost shared coast")
        require(len(lifted)-1 > t+coast, "coast reached positive integer")
    counts["lifted_cohort_sources"] += len(members)
    counts["coast_source_dates"] += coast * len(members)
    return dict(grade=n, shared_date=t, shared_numerator=d, cohort=len(members),
                grid_units=2*3**(n-1), coast=coast, shift_bits=shift.bit_length())


def main():
    counts = Counter()
    for n in (2, 4, 6, 8):
        scale = 3**n
        for shift in (0, 1, 2**9-1, 2**40, 2**80+87):
            for m in range(1, min(400,scale), 7):
                if m % 3:
                    joint_control(n, m, shift, counts)
    cohorts = [cohort(n, d, counts) for n,d in ((3,17), (5,64), (7,121), (9,257))]
    require(counts["large_terminal"] and counts["late_landing"], "missing both regimes")
    require(cohorts[-1]["cohort"] > 1, "no actual many-source control")
    print(json.dumps(dict(scope="Finite exact native controls; no asymptotic tail tested",
                          counts=dict(counts), cohorts=cohorts), sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
