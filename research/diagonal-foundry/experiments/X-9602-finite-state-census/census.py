#!/usr/bin/env python3
"""X-9602 — exhaustive finite-state feedback census.

Enumerates ALL strictly causal finite-state operators E_M with |S| <= 3
(machines M = (S, s0, delta, lambda); 2 + 128 + 17,496 = 17,626 machines),
builds each foundry solution alpha_E to K digits (T-9601 recursion), and
detects integral solutions (terminal constant digit runs).

T-9603 predicts: every integral hit has an eventually periodic parity
vector with period <= |S| <= 3, so its orbit enters one of the cycles
  {0}, {1,2}, {-1}, {-5,-7,-10}
(the only integer cycles with parity period <= 3), and every POSITIVE hit
has subcritical tail, hence reaches the trivial cycle. The census checks
this prediction against every machine.

Each hit is re-verified: rebuilt at 2K digits, closure equation replayed
directly from the integer by an independent code path, orbit cycle
classified by direct iteration.

Exact integer arithmetic throughout. Deterministic.

Usage: python3 census.py [K]     (default K = 256)
"""

import sys
from itertools import product

K = int(sys.argv[1]) if len(sys.argv) > 1 else 256
RUN_THRESHOLD = 48                # terminal constant run flagging a hit
KNOWN_CYCLES = {
    frozenset({0}): "0",
    frozenset({1, 2}): "1<->2 (trivial)",
    frozenset({-1}): "-1",
    frozenset({-5, -7, -10}): "-5 cycle",
}


def build_machine(s0, delta, lam, K):
    """Build alpha_E for machine (s0, delta, lam); delta[(q,b)] -> q'."""
    MOD = 1 << (K + 8)
    digits = []
    m = [0]
    a = [0]
    pow3 = [1]
    state = s0                     # state after consuming digits so far
    for k in range(K):
        e_k = lam[state]           # strictly causal output at position k
        if (m[k] & 1) != e_k:
            for i in range(k + 1):
                m[i] = (m[i] + pow3[a[i]] * (1 << (k - i))) % MOD
            d_k = 1
        else:
            d_k = 0
        digits.append(d_k)
        state = delta[(state, d_k)]
        p = m[k] & 1
        m.append((3 * m[k] + 1) // 2 % MOD if p else m[k] // 2)
        a.append(a[k] + p)
        while len(pow3) <= a[-1]:
            pow3.append(pow3[-1] * 3 % MOD)
    alpha = 0
    for d in reversed(digits):
        alpha = (alpha << 1) | d
    return alpha, digits


def terminal_run(digits):
    """(bit, length) of the terminal constant run."""
    last = digits[-1]
    n = 0
    for d in reversed(digits):
        if d != last:
            break
        n += 1
    return last, n


def machine_output(s0, delta, lam, digits, upto):
    """Independent replay of E on a digit prefix stream."""
    out = []
    state = s0
    for k in range(upto):
        out.append(lam[state])
        state = delta[(state, digits[k])]
    return out


def parity_prefix(n, upto):
    x, out = n, []
    for _ in range(upto):
        p = x & 1
        out.append(p)
        x = (3 * x + 1) // 2 if p else x // 2
    return out


def orbit_cycle(n, cap=10**6):
    seen = {}
    x = n
    for t in range(cap):
        if x in seen:
            cyc = frozenset(list(seen)[seen[x]:])
            return cyc
        seen[x] = t
        x = (3 * x + 1) // 2 if x & 1 else x // 2
    raise RuntimeError(f"no cycle within {cap} steps from {n}")


def verify_hit(s0, delta, lam, n):
    """Full verification of an integral hit n (may be negative)."""
    K2 = 2 * K
    alpha2, _ = build_machine(s0, delta, lam, K2)
    assert alpha2 == n % (1 << K2), "rebuild at 2K disagrees with integer"
    dig = [(n >> k) & 1 for k in range(K2)]        # two's-complement digits
    assert machine_output(s0, delta, lam, dig, K2) == parity_prefix(n, K2), \
        "closure equation replay failed"
    return orbit_cycle(n)


def enumerate_machines(nstates):
    states = range(nstates)
    for s0 in states:
        for lam in product((0, 1), repeat=nstates):
            for dv in product(states, repeat=2 * nstates):
                delta = {(q, b): dv[2 * q + b]
                         for q in states for b in (0, 1)}
                yield s0, delta, tuple(lam)


total = 0
hits = {}          # integer -> list of (nstates, s0, lam, delta-signature)
for nstates in (1, 2, 3):
    for s0, delta, lam in enumerate_machines(nstates):
        total += 1
        alpha, digits = build_machine(s0, delta, lam, K)
        bit, run = terminal_run(digits)
        if run >= RUN_THRESHOLD:
            n = alpha if bit == 0 else alpha - (1 << K)
            cyc = verify_hit(s0, delta, lam, n)
            assert cyc in KNOWN_CYCLES, f"UNEXPECTED CYCLE {sorted(cyc)}"
            sig = (nstates, s0, lam, tuple(sorted(delta.items())))
            hits.setdefault(n, []).append(sig)

print(f"X-9602 finite-state feedback census   K = {K}, "
      f"terminal-run threshold = {RUN_THRESHOLD}")
print(f"machines enumerated: {total} (all |S| <= 3, all initial states)")
print(f"integral hits: {sum(len(v) for v in hits.values())} machines, "
      f"{len(hits)} distinct integers")
print()
print(f"{'integer':>8}  {'machines':>8}   orbit cycle")
for n in sorted(hits, key=lambda v: (abs(v), v < 0)):
    cyc = orbit_cycle(n)
    print(f"{n:>8}  {len(hits[n]):>8}   {KNOWN_CYCLES[cyc]}")
print()
pos = [n for n in hits if n > 0]
print(f"positive hits: {sorted(pos)} — all reach the trivial cycle: "
      f"{all(orbit_cycle(n) == frozenset({1, 2}) for n in pos)}")
print("T-9603 consistency: every hit verified (rebuild at 2K, closure "
      "replay, cycle in the parity-period<=3 inventory).  PASS")
