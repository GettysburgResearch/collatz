"""Witnesses that all 36 ordered branch transitions (i,i') occur (T-6102 gap audit)."""
P = 3**12; Q = 2**19
A = [7*3**(2*i)*2**(15-3*i) for i in range(6)]
ASET = set(A); IDX = {a: i for i, a in enumerate(A)}
invP = pow(P, -1, Q)

# depth-2 lift: 36 classes mod 2^38, print least positive representative of each
found = {}
for i, a0 in enumerate(A):
    r = (-a0 * invP) % Q
    if r == 0:
        r = Q
    X1 = (P*r + a0) // Q
    for j, a1 in enumerate(A):
        t = (((-P*X1) % Q - a1) % Q) * pow(invP, 2, Q) % Q
        x = r + Q*t
        # verify by forward iteration
        d0 = (-P*x) % Q
        x1 = (P*x + d0) // Q
        d1 = (-P*x1) % Q
        assert d0 in ASET and d1 in ASET and IDX[d0] == i and IDX[d1] == j, (i, j)
        found[(i, j)] = x

print(f"all {len(found)} ordered transitions realised: {len(found) == 36}")
print("least witness for each (i -> i'):")
for i in range(6):
    print("  " + "  ".join(f"{i}{j}:{found[(i,j)]:>12}" for j in range(6)))
print("\nmin over all 36 =", min(found.values()), "= m_2")
