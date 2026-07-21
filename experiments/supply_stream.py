"""Supply-stream statistics: do 3-smooth amplifier outputs show any bias
toward H-validity beyond the provable first-step enhancement?

THEOREM (first-step enhancement, exact).  A pure 3-smooth supply value
A0 = 81^N u (u odd) is odd, so its low base-64 digit is odd: the only
valid digit is 1, and 81^N u == 1 (mod 64) holds for N in exactly one
class mod 4 (ord(81 mod 64) = 4).  First-step validity density = 1/4 --
an 8x enhancement over the generic 2/64 = 1/32.

QUESTION.  Do the conditional continuation densities
    d_t = P(run > t | run >= t)
stay enhanced (structure!  a crack in the wall) or collapse to the
generic 1/32 (for odd values: 1/32; after step 1 values can be even, so
generic is 2/64 = 1/32 either way)?

METHOD (exact, no sampling).  Validity of the first t steps of
A0 = 81^N u depends only on N mod ord(81 mod 64^{t}) -- wait: depends on
A0 mod 64^{t+1}, i.e. on N mod ord(81 mod 64^{t+1}) = 2^{6(t+1)-4}.
Branch-and-prune: level-t valid classes of N, each extended by the 64
lifts to the next order.  Counts are EXACT densities.

Also: E2 empirical run distribution for actual amplifier outputs
81^{9m}(81x+1); E3 static digit frequencies of 81^k (middle digits);
E4 demand-agreement valuations along the Sturmian schedule.
"""

from collections import Counter
import math

def H(A):
    B, e = divmod(A, 64)
    return 81 * B + e if e in (0, 1) else None


def run_len(A, cap=64):
    r = 0
    while A % 64 in (0, 1) and r < cap:
        A = 81 * (A // 64) + A % 64
        r += 1
    return r


# ---------------------------------------------------------------- E1
def exact_tree(u=1, tmax=6):
    """Exact valid-N-class counts: level t uses modulus ord_t = 2^{6(t+1)-4}
    on N; a class N0 is level-t valid iff 81^{N0} u has H-run >= t
    (well-defined: run>=t depends on A0 mod 64^{t+1} <= 64^{t+1}, and
    ord(81 mod 64^{t+1}) = 2^{6(t+1)-4})."""
    print(f"== E1: exact validity tree for A0 = 81^N * {u} ==")
    # level 1: N mod ord(81, 64^2)=256 for safety, prune by run>=1
    ordt = 2 ** (6 * 2 - 4)  # covers A0 mod 64^2
    M = 64 ** 2
    p = pow(81, 0, M)
    valid = []
    powN = {  }
    x = u % M
    step = 81 % M
    cur = x
    for N in range(ordt):
        if run_len(cur, cap=1) >= 1:
            valid.append(N)
        cur = cur * 81 % M
    dens = len(valid) / ordt
    print(f"  t=1: {len(valid)}/{ordt} = {dens:.6f}   (theorem: 1/4 = 0.25)")
    prev, prev_ord = valid, ordt
    for t in range(2, tmax + 1):
        ordt = 2 ** (6 * (t + 1) - 4)
        M = 64 ** (t + 1)
        lift = ordt // prev_ord
        valid = []
        for N0 in prev:
            for j in range(lift):
                N = N0 + j * prev_ord
                A = pow(81, N, M) * u % M
                if run_len(A, cap=t) >= t:
                    valid.append(N)
        d = len(valid) / (len(prev) * lift) if prev else 0
        print(f"  t={t}: {len(valid)} classes mod 2^{int(math.log2(ordt))}; "
              f"conditional d_{t} = {d:.6f}  (generic 1/32 = 0.03125)")
        prev, prev_ord = valid, ordt
        if not prev:
            break
    return prev


# ---------------------------------------------------------------- E2
def amplifier_runs(mmax=3000):
    print("== E2: H-runs of actual amplifier outputs 81^{9m}(81x+1) ==")
    cnt = Counter()
    for x in (0, 1, 2, 3):
        for m in range(1, mmax + 1):
            A = 81 ** (9 * m) * (81 * x + 1)
            cnt[run_len(A)] += 1
    tot = sum(cnt.values())
    mean = sum(r * c for r, c in cnt.items()) / tot
    print(f"  {tot} outputs: run distribution {dict(sorted(cnt.items()))}")
    print(f"  mean run {mean:.5f}; first-step theorem predicts "
          f"P(run>=1) = 1/4 exactly for x=0 (odd outputs)")
    # split by x parity of output
    for x in (0, 1):
        c2 = Counter()
        for m in range(1, mmax + 1):
            A = 81 ** (9 * m) * (81 * x + 1)
            c2[run_len(A)] += 1
        ge1 = sum(v for r, v in c2.items() if r >= 1) / mmax
        print(f"  x={x}: P(run>=1) = {ge1:.5f}")


# ---------------------------------------------------------------- E3
def digit_stats(kmax=2500):
    print("== E3: static base-64 digit frequencies of 81^k (middle digits) ==")
    cnt = Counter()
    tot = 0
    for k in range(100, kmax):
        v = 81 ** k
        # strip 20 low and 20 high digits to isolate the middle
        ds = []
        while v:
            ds.append(v & 63)
            v >>= 6
        mid = ds[20:-20]
        cnt.update(mid)
        tot += len(mid)
    f01 = (cnt[0] + cnt[1]) / tot
    exp = 2 / 64
    sd = math.sqrt(exp * (1 - exp) / tot)
    print(f"  {tot} middle digits; freq(digit in {{0,1}}) = {f01:.6f}; "
          f"expected {exp:.6f} +- {sd:.6f} ({abs(f01-exp)/sd:.2f} sigma)")
    # full digit chi-square
    chi = sum((cnt[d] - tot / 64) ** 2 / (tot / 64) for d in range(64))
    print(f"  chi-square over 64 digits: {chi:.1f} (df=63, mean 63, "
          f"sd ~ {math.sqrt(126):.1f})")


# ---------------------------------------------------------------- E4
def demand_agreement(stages=4000):
    """Coset finding: demands are always == 0 mod 16 (r == 49(81^{-9m}-1),
    and 81-powers minus 1 are 0 mod 16); supply 81^{9m}(81x+1) is 0 mod 16
    iff x == 15 (mod 16) -- a DESIGNED condition on the context.  We
    therefore condition on the correct coset and measure the residual
    agreement valuation, which should be exactly generic (1/64 per
    additional digit): boundary = coset arithmetic, depth = generic."""
    print("== E4: demand-agreement (coset-conditioned) ==")
    sl = math.log(81) / math.log(64)
    alpha = 1 / (sl - 1) - 17
    m, xfrac = 20, 0.0
    cnt = Counter()
    j = 6
    Mj = 64 ** j
    i81 = pow(81, -1, Mj)
    x_base = 12345
    for t in range(stages):
        xfrac += alpha
        mp = m + (18 if xfrac >= 1 else 17)
        if xfrac >= 1:
            xfrac -= 1
        r = pow(i81, 9 * m + 1, Mj) * (17 * i81 - pow(81, 9 * m, Mj)) % Mj
        assert r % 16 == 0                     # coset lemma
        x = (x_base + t) - ((x_base + t) % 16) + 15   # x == 15 mod 16
        sup = pow(81, 9 * m, Mj) * (81 * x + 1) % Mj
        diff = (sup - r) % Mj
        v = 0
        while diff % 64 == 0 and v < j:
            diff //= 64
            v += 1
        cnt[v] += 1
        m = mp
    tot = sum(cnt.values())
    print(f"  {tot} stages, x == 15 mod 16: valuation distribution "
          f"{dict(sorted(cnt.items()))}")
    ge1 = sum(c for v, c in cnt.items() if v >= 1) / tot
    print(f"  P(v>=1) = {ge1:.5f}; conditioned null: agreement mod 64 needs"
          f" the remaining 2 bits of the digit -> 1/4 = 0.25;"
          f" then 1/64 per further digit")


if __name__ == '__main__':
    exact_tree(u=1, tmax=6)
    print()
    exact_tree(u=5, tmax=5)
    print()
    amplifier_runs()
    print()
    digit_stats()
    print()
    demand_agreement()
