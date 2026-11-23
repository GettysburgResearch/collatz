"""Check arithmetic ranges and exact minimum bounds of the recorded runs."""

from math import comb, gcd

full_runs = [(32, 20, 808182895, 225792840), (35, 22, 2978678759, 1476337800)]
for A, p, D, count in full_runs:
    assert D == 2**A - 3**p > 0
    assert count == comb(A, p)
    assert 2 ** (A - p) * (3**p - 2**p) < 2**64
    assert A < 256

slice_runs = [
    (46, 29, 39409, 15407792),
    (65, 41, 551, 660519),
    (149, 94, 343, 1151678),
    (233, 147, 5, 33744),
]
for A, p, d, bound in slice_runs:
    D = 2**A - 3**p
    assert D > 0 and D % d == 0
    assert gcd(A, p) == 1 and gcd(d, 6) == 1
    assert bound == d * (p * 2**A - D) // (3 * D)
    # Deleting even branches increases the state. The executable evaluates one
    # extra odd branch before pruning an excess odd count, so use q=p+1 here.
    q = p + 1
    assert 3**q * (bound + d) < 2**q * 2**128
    print(f"Validated slice A={A}, p={p}, d={d}, bound={bound}, 128-bit range.")

print("Validated both full-word counts and their 64-bit numerator ranges.")
