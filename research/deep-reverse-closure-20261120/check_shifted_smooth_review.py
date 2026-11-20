#!/usr/bin/env python3
"""Independent reconstruction; no imports from the author or repository."""
import hashlib
import json
from pathlib import Path


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def extract(n, p):
    require(n > 0, "valuation requires a positive input")
    a = 0
    while n % p == 0:
        n //= p
        a += 1
    return a, n


def odd_step(n):
    require(n > 0 and n % 2 == 1, "ordinary odd input required")
    a, u = extract(3*n+1, 2)
    return u, a


def shifted(n):
    s, v = extract(n+1, 2)
    t, q = extract(v, 3)
    return s, t, q


def finite_table():
    records = []
    transitions = []
    for k in range(1, 128):
        N = 2*3**(k-1)-1
        u, a = odd_step(N)
        b, raw = extract(3**k-1, 2)
        require(a == b+1 and raw == u, "boundary valuation off by one")
        require(b == (1 if k % 2 else 2+extract(k, 2)[0]), "valuation formula")
        s, t, q = shifted(u)
        records.append([k, a, s, t, q])
        if q == 1:
            transitions.append([k, N, u, b, s, t])
    require(transitions == [[1, 1, 1, 1, 1, 0],
                            [2, 5, 1, 3, 1, 0],
                            [4, 53, 5, 4, 1, 1]], "wrong smooth complement")
    require(3**128 > 4800*2**14*128**15, "large-index cutoff")
    require(129**15 < 3*128**15, "cutoff induction multiplier")
    return records


def exits_and_basin():
    checks = 0
    within = set()
    for k in range(1, 128):
        for s in range(1, k+1):
            t = k-s
            n = 2**s*3**t-1
            initial = n
            for i in range(s-1):
                require(shifted(n)[2] == 1, "premature class exit")
                n, a = odd_step(n)
                require(a == 1, "forced run exponent")
                require(n == 2**(s-i-1)*3**(t+i+1)-1, "forced run state")
            require(n == 2*3**(k-1)-1, "wrong boundary state")
            n, a = odd_step(n)
            require(a >= 2, "boundary is not a defect")
            if k not in (1, 2, 4):
                require(shifted(n)[2] != 1, "missing exact exit")
            else:
                within.add(initial)
                seen = set()
                while n != 1:
                    require(n not in seen and shifted(n)[2] == 1, "within-class tail")
                    seen.add(n)
                    n, _ = odd_step(n)
            checks += 1
    require(within == {1, 3, 5, 15, 23, 35, 53}, "wrong within-class basin")
    return checks


def finite_prefixes():
    history_checks = clock_checks = 0
    for start in range(1, 2000, 2):
        n = start
        seen = set()
        outside = int(shifted(n)[2] != 1)
        defects = 0
        last_defect_finish = 0
        for j in range(600):
            if n in seen:
                break
            seen.add(n)
            require(2**j*(n+1) <= 3**j*(start+1), "shifted height envelope")
            following, a = odd_step(n)
            if a >= 2:
                r = last_defect_finish
                # The exact form of R_(i+1) <= (log_2 3) R_i + log_2(n_0+1).
                require(2**(j+1) <= 3**r*(start+1), "defect clock recurrence")
                last_defect_finish = j+1
                defects += 1
                clock_checks += 1
            outside += int(shifted(following)[2] != 1)
            if following not in seen:
                require(defects <= 2*outside+2, "simple-prefix incidence count")
                history_checks += 1
            n = following
    return history_checks, clock_checks


def main():
    records = finite_table()
    cases = exits_and_basin()
    histories, clocks = finite_prefixes()
    canonical = json.dumps(records, separators=(",", ":")).encode()
    print(json.dumps({
        "scope": "independent finite complement and arithmetic controls; universal proof conditional on quoted Lagarias Lemma 2.2(1)",
        "finite_boundary_indices": len(records),
        "table_sha256": hashlib.sha256(canonical).hexdigest(),
        "exact_first_exit_examples": cases,
        "simple_prefix_incidence_checks": histories,
        "exact_defect_clock_checks": clocks,
        "author_implementation_imported": False,
    }, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
