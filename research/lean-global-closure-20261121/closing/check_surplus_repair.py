#!/usr/bin/env python3
"""Exact finite control for the target-word/safe-suffix repair attempt.

The all-word cut theorem is a written proof, not inferred from this control.
The source-record maximality is imported explicitly from the pinned PR185 note.
"""
from fractions import Fraction
import json

def step(n):
    return (3*n+1)//2 if n % 2 else n//2

def prefix(n, length):
    states = [n]
    bits = []
    correction = 0
    odd = 0
    for j in range(length):
        bit = n % 2
        bits.append(bit)
        if bit:
            odd += 1
            correction = 3*correction + 2**j
        n = step(n)
        states.append(n)
    assert 2**length * states[-1] == 3**odd * states[0] + correction
    return states, bits, odd, correction

q, e, t = 273, 2, 2047
word = [2, 3, 3, 3, 1, 2, 3, 4]
A, r, S = sum(word), len(word), 2**e*q
source_states, source_bits, source_odd, C = prefix(q, A)
target_states, target_bits, o, D = prefix(t, A)
assert source_states[-1] == 1 and source_odd == r
assert source_states[:-1].count(1) == 0
assert len(set(source_states)) == len(source_states)
assert all(n >= t for n in target_states)
assert 6*3**o > 5*2**A > 5*3**r*q
safe = sorted(set(prefix(S, e+A)[0][1:]))
assert max(safe) <= (t-1)//2

repairs = []
for b in range(A+1):
    _, bits, tail_odd, tail_correction = prefix(target_states[b], A-b)
    assert bits == target_bits[b:]
    for v in safe:
        z = Fraction(2**(A-b)*v-tail_correction, 3**tail_odd)
        if z.denominator == 1 and z > 0:
            z = int(z)
            changed_states, changed_bits, _, _ = prefix(z, A-b)
            assert changed_bits == bits and changed_states[-1] == v
            prefix_odd = sum(target_bits[:b])
            assert target_states[b] > 2**(A-b)
            assert 5*2**A < 6*3**prefix_odd*t
            assert prefix_odd >= r-2
            repairs.append({"cut_clock": b, "target_odd_events_before_cut": prefix_odd,
                            "copied_tail_clock": A-b, "copied_tail_odd_events": tail_odd,
                            "current_target": target_states[b], "new_tail_source": z,
                            "certified_endpoint": v})

first = [x for x in repairs if x["cut_clock"] == min(y["cut_clock"] for y in repairs)]
assert first == [{"cut_clock": 18, "target_odd_events_before_cut": 15,
                  "copied_tail_clock": 3, "copied_tail_odd_events": 3,
                  "current_target": 112103, "new_tail_source": 7,
                  "certified_endpoint": 26}]
assert prefix(7, 3)[0] == [7, 11, 17, 26]

result = {
    "source": {"S": S, "q": q, "initial_even_exponent": e, "word": word,
               "ordinary_clock_from_q": A, "odd_count": r, "correction": C},
    "target": {"t": t, "at_source_clock": target_states[-1], "odd_count": o,
               "correction": D, "no_descent_through_source_clock": True},
    "exact_surplus": [6*3**o, 5*2**A, 5*3**r*q],
    "all_positive_safe_endpoint_copied_tail_repairs": repairs,
    "first_repair": first,
    "first_repair_paid_source": 4*7,
    "first_repair_paid_interval_ceiling": 2*(4*7)+1,
    "scope": "Finite arithmetic control only. Does not establish all-certificate maximality, a universal repair selector, or Collatz.",
}
print(json.dumps(result, indent=2))
