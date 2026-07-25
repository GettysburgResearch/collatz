"""End-to-end physical replay: chart legality <-> real shortcut-Collatz orbit (T-6101).

For a chart-legal x, checks that the real Collatz trajectory of n = 6x-5 executes exactly
19N steps with 12N odd steps, realises the predicted parity word, and lands on 6*x_N-5.
"""
P = 3**12
Q = 2**19
A = [7 * 3**(2*i) * 2**(15-3*i) for i in range(6)]
ASET = set(A)
IDX = {a: i for i, a in enumerate(A)}


def chart_word(x, N):
    """Digit word and endpoint of the chart orbit, stopping early if a step is illegal."""
    w = []
    for _ in range(N):
        d = (-P * x) % Q
        if d not in ASET:
            break
        w.append(IDX[d])
        x = (P * x + d) // Q
    return w, x


def T(n):
    return (3*n + 1)//2 if n % 2 else n//2


def block_word(i):
    """W_i = (110)^(5-i) . 1010 . (110)^i"""
    return "110"*(5-i) + "1010" + "110"*i


def replay(label, m, N):
    w, xN = chart_word(m, N)
    assert len(w) == N, f"{label} is not legal for {N} steps"
    n = 6*m - 5
    cur, parity, odd = n, [], 0
    for _ in range(19*N):
        parity.append(cur % 2)
        odd += cur % 2
        cur = T(cur)
    predicted = "".join(block_word(i) for i in w)
    # T-6102: v_2(x_k) = 15 - 3*i_k along the whole orbit
    xs, val_ok = m, True
    for i in w:
        val_ok &= (xs & -xs).bit_length() - 1 == 15 - 3*i
        xs = (P*xs + A[i]) // Q
    print(f"{label}  (N={N}, digit word {''.join(map(str, w))})")
    print(f"   T^{19*N}(6x-5) == 6*x_{N}-5      : {cur == 6*xN - 5}")
    print(f"   odd steps {odd} == 12*N = {12*N}   : {odd == 12*N}")
    print(f"   realised parity word == predicted: {''.join(map(str, parity)) == predicted}")
    print(f"   v_2(x_k) == 15-3*i_k for all k   : {val_ok}")
    print(f"   growth {cur/n:.6f} vs (P/Q)^N = {(P/Q)**N:.6f}")


if __name__ == "__main__":
    replay("m_6", 49927377479016341945330731072, 6)
    replay("m_9", 274731072270742333628800865325991165013963264, 9)
    replay("m_12", 83301137368103499460139839972641009013711852735287572369408, 12)
