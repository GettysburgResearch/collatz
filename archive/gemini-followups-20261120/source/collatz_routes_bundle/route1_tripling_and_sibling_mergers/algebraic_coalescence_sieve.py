"""
Exact algebraic coalescence sieve for (n, 3n) [PR #146] and (2n, 2n+1) [PR #145],
plus the minimality stopping-time sieve for odd residue classes mod 2^M.
"""
import json
import math


def affine_collatz_orbit(r: int, M: int, max_steps: int = 100):
    """Track exact affine forms (2^p * 3^a) * m + b for n = 2^M * m + r."""
    p, a, b = M, 0, r
    states = {(p, a, b): 0}
    step = 0
    while p > 0 and step < max_steps:
        if b % 2 == 0:
            p -= 1
            b //= 2
        else:
            p -= 1
            a += 1
            b = (3 * b + 1) // 2
        step += 1
        states[(p, a, b)] = step
    return states


def run_sieve(max_M_3n: int = 13, max_M_sib: int = 12, max_M_drop: int = 14):
    tripling = {}
    for M in range(3, max_M_3n + 1):
        mod = 1 << M
        odd_count = mod // 2
        coalesced = 0
        witnesses = []
        for r in range(1, mod, 2):
            s1 = affine_collatz_orbit(r, M)
            p, a, b = M, 1, 3 * r
            hit = (p, a, b) in s1
            step = 0
            while not hit and p > 0 and step < 100:
                if b % 2 == 0:
                    p -= 1
                    b //= 2
                else:
                    p -= 1
                    a += 1
                    b = (3 * b + 1) // 2
                step += 1
                if (p, a, b) in s1:
                    hit = True
                    if M <= 6 and len(witnesses) < 5:
                        witnesses.append({
                            "r": r, "mod": mod,
                            "k_n": s1[(p, a, b)], "k_3n": step,
                            "common_form": f"(2^{p}*3^{a})*m + {b}"
                        })
            if hit:
                coalesced += 1
        surv = odd_count - coalesced
        tripling[M] = {
            "odd_classes": odd_count,
            "coalesced": coalesced,
            "survivors": surv,
            "coalesced_fraction": round(coalesced / odd_count, 6),
            "box_dim_est": round(math.log2(surv) / (M - 1), 5) if surv > 0 else 0.0,
            "witnesses": witnesses
        }

    sibling = {}
    for M in range(3, max_M_sib + 1):
        mod = 1 << M
        coalesced = 0
        for r in range(mod):
            s1 = affine_collatz_orbit(r, M)
            p, a, b = M, 1, 3 * r + 2
            hit = (p, a, b) in s1
            step = 0
            while not hit and p > 0 and step < 100:
                if b % 2 == 0:
                    p -= 1
                    b //= 2
                else:
                    p -= 1
                    a += 1
                    b = (3 * b + 1) // 2
                step += 1
                if (p, a, b) in s1:
                    hit = True
            if hit:
                coalesced += 1
        surv = mod - coalesced
        sibling[M] = {
            "total_classes": mod,
            "coalesced": coalesced,
            "survivors": surv,
            "coalesced_fraction": round(coalesced / mod, 6),
            "box_dim_est": round(math.log2(surv) / M, 5) if surv > 0 else 0.0
        }

    stopping_drop = {}
    for M in range(3, max_M_drop + 1):
        mod = 1 << M
        odd_count = mod // 2
        drops = 0
        for r in range(1, mod, 2):
            p, a, b = M, 0, r
            while p > 0:
                if b % 2 == 0:
                    p -= 1
                    b //= 2
                else:
                    p -= 1
                    a += 1
                    b = (3 * b + 1) // 2
                if (1 << p) * (3 ** a) < mod:
                    drops += 1
                    break
        surv = odd_count - drops
        stopping_drop[M] = {
            "odd_classes": odd_count,
            "excluded_by_drop": drops,
            "survivors": surv,
            "excluded_fraction": round(drops / odd_count, 6)
        }

    return {
        "tripling_pairs_n_3n": tripling,
        "sibling_pairs_2n_2n1": sibling,
        "stopping_time_drop_sieve": stopping_drop
    }


if __name__ == "__main__":
    print(json.dumps(run_sieve(), indent=2))
