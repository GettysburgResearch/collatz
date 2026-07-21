"""P2 deep-dive II (issue #4): the room recursion, its unconditional
count bound, and the mod-81 interval-equidistribution mask.

Facts under test (EQ-INTERCHANGE.md §§7-8):

  (identity)  For 0 < Y < 64^{K-1}:
     {A in R_K : 0 < A <= Y}  <-->  {(A', eps): A' in R_{K-1},
        eps in {0,1}, A' == eps (mod 81), 0 < A' <= 81(Y-eps)/64 + eps}
     via A = 64(A'-eps)/81 + eps ... i.e. A' = 81(A-eps)/64 + eps.
     (The congruence is FREE: A' = 81B + eps forces A' == eps mod 81.)

  (bound)     count(K, 64^{(1-e)K}) <= 2^{K-j},  j = floor(eK/log64(81))
              -- iterate the identity j times, drop congruences, stop
              when the window fills the range.

  (mask)      The conditional sharpening needs: R_n restricted to an
              interval [0,Z] equidistributes mod 81 (classes {0,1}
              jointly own ~2/81).  Measure the deviation profile.
"""
import math
from eq_ladder import coded

M, N = 64, 81
LOG64_81 = math.log(81) / math.log(64)


def enumerate_RK(K):
    words = [[0], [1]]
    for _ in range(K - 1):
        words = [w + [d] for w in words for d in (0, 1)]
    return sorted(coded(w, M, N, K) for w in words)


def count_upto(RK, Y, cls=None):
    if cls is None:
        return sum(1 for A in RK if 0 < A <= Y)
    return sum(1 for A in RK if 0 < A <= Y and A % 81 in cls)


if __name__ == "__main__":
    R = {K: enumerate_RK(K) for K in range(2, 15)}

    print("== identity check (one-room regime Y < 64^K/81, and general) ==")
    bad1 = bad2 = n1 = n2 = 0
    for K in range(3, 15):
        Q1 = 64 ** (K - 1)
        for Y in [10, 10**3, 64**(K // 2), 64**K // 100, 64**K // 82,
                  64 ** (K - 1) - 1, 64**K // 2]:
            if Y >= 64 ** K:
                continue
            lhs = count_upto(R[K], Y)
            # one-room form (valid when Z_eps < 64^{K-1}, i.e. Y < ~64^K/81)
            one_room_valid = 81 * Y // 64 + 1 < Q1
            rhs1 = 0
            rhs2 = 0
            for eps in (0, 1):
                Zt = 81 * (Y - eps) // 64 + eps
                rhs1 += sum(1 for A in R[K - 1]
                            if 0 < A <= min(Zt, Q1 - 1) and A % 81 == eps)
                # general: rooms r = 0..80; child A' = 81B+eps - r*Q1
                for r in range(0, 81):
                    lo = r * Q1
                    hi = min(Zt, (r + 1) * Q1 - 1)
                    if hi < lo:
                        break
                    cls = (eps - r * Q1) % 81
                    rhs2 += sum(1 for A in R[K - 1]
                                if lo <= A + r * Q1 and 0 <= A <= hi - lo
                                and A % 81 == cls and (A + r*Q1) > 0
                                and 0 < 64 * ((A + r*Q1 - eps) // 81) + eps <= Y)
            if one_room_valid:
                n1 += 1
                if lhs != rhs1:
                    bad1 += 1
                    print(f"  ONE-ROOM MISMATCH K={K} Y={Y}: {lhs} vs {rhs1}")
            n2 += 1
            if lhs != rhs2:
                bad2 += 1
                print(f"  GENERAL MISMATCH K={K} Y={Y}: {lhs} vs {rhs2}")
    print(f"  [{'PASS' if bad1 == 0 else 'FAIL'}] one-room identity in its "
          f"regime ({n1} cells)")
    print(f"  [{'PASS' if bad2 == 0 else 'FAIL'}] general multi-room "
          f"identity ({n2} cells)")

    print("\n== unconditional bound check: count <= 2^(K-j) ==")
    ok = True
    for K in (10, 12, 14):
        for e10 in range(1, 10):
            e = e10 / 10
            Y = int(64 ** ((1 - e) * K))
            j = int(e * K / LOG64_81)
            c = count_upto(R[K], Y)
            b = 2 ** (K - j)
            if c > b:
                ok = False
                print(f"  VIOLATION K={K} e={e}: {c} > {b}")
    print(f"  [{'PASS' if ok else 'FAIL'}] bound holds at K=10,12,14, "
          f"e=0.1..0.9")

    print("\n== mask: mod-81 equidistribution of R_n ∩ [0,Z] ==")
    print("  n   Z=64^(bn)  |set|   share cls{0,1} (uniform 2/81=0.0247)"
          "   max class dev")
    for n in (12, 14):
        for b10 in (5, 7, 9, 10):
            b = b10 / 10
            Z = int(64 ** (b * n))
            sel = [A for A in R[n] if 0 < A <= Z]
            if len(sel) < 30:
                print(f" {n:3d}  b={b:.1f}  {len(sel):6d}   (too few)")
                continue
            cnt = [0] * 81
            for A in sel:
                cnt[A % 81] += 1
            share01 = (cnt[0] + cnt[1]) / len(sel)
            dev = max(abs(c / len(sel) - 1 / 81) for c in cnt)
            print(f" {n:3d}  b={b:.1f}  {len(sel):6d}   {share01:.4f}"
                  f"                              {dev:.4f}")
    print("MEASUREMENT COMPLETE")
