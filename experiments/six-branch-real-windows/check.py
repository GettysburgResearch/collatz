"""Check the real-window constants and all four-edge type words, exactly."""
from fractions import Fraction
from itertools import product

P, Q = 3**12, 2**19
R = (294912, 331776, 438784, 297024, 6472, 466033)
C = (298936, 336303, 444771, 301077, 6561, 472392)
A = tuple(Q*c-P*r for r, c in zip(R, C))
LOW, HIGH = (Fraction(a, P-Q) for a in (min(A), max(A)))
RATIO = Fraction(P, Q)


def separation(residues, modulus):
    values = sorted(residues)
    return min((v-u) % modulus for u, v in zip(values, values[1:] + values[:1]))


def check_word(word, windows):
    root, endpoint, modulus, slope = 0, 0, 1, 1
    for i in word:
        lift = (R[i] - endpoint) * pow(slope, -1, Q) % Q
        root += modulus * lift
        endpoint = C[i] + P * ((endpoint + slope * lift - R[i]) // Q)
        modulus *= Q
        slope *= P
    error = (LOW + HIGH) / 2
    for i in reversed(word):
        error = (Q*error + A[i]) / P
    x, y = root, root + error
    for j, i in enumerate(word):
        assert x % Q == R[i] and LOW <= y-x <= HIGH
        assert x // Q == y // Q
        if j:
            assert x % (P*Q) in windows
        x = (P*x + A[i]) // Q
        y *= RATIO
    assert x == endpoint and y-x == (LOW + HIGH) / 2


def main():
    assert A == (229376, 258048, 290304, 326592, 367416, 413343)
    windows = {r + Q*((c-r)*pow(Q, -1, P) % P) for r, c in product(R, C)}
    assert len(windows) == 36 and separation(windows, P*Q) == 516358953
    assert (separation(R, Q), separation(C, P)) == (2112, 2141)
    assert HIGH-LOW + Fraction(max(A)-min(A), Q) < 27
    assert 36 * (HIGH-LOW)/(P*Q) < Fraction(333, 10**11)
    for word in product(range(6), repeat=4):
        check_word(word, windows)
    x, fake = 5523840113, 5599203328
    assert x % Q in R and fake % Q in R
    assert (P*x + A[R.index(x % Q)]) // Q == fake-1
    assert LOW < (x+45)*RATIO - fake < HIGH
    assert fake % P not in C
    print("36 CRT windows, 1296 four-edge words, one spurious one-sided edge checked")


if __name__ == "__main__":
    main()
