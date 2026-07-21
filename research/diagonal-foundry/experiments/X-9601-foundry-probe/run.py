#!/usr/bin/env python3
"""X-9601 — foundry probe.

Builds the unique 2-adic solution alpha_E of the closure equation
    parity(alpha) = E(digits(alpha))
for a battery of strictly causal operators E (T-9601 construction), checks
the four constant-operator validation gates against closed-form answers,
replays every result through an independent verifier that shares no orbit
code with the builder, spot-checks stage uniqueness, and records digit /
parity statistics for the feedback probes.

Exact integer arithmetic throughout; no floats on any critical path
(floats appear only in printed density summaries).

Usage:  python3 run.py [K]      (default K = 1024 digits)
"""

import hashlib
import sys

K = int(sys.argv[1]) if len(sys.argv) > 1 else 1024
GUARD = 8                       # extra bits so parity stays valid at step K
BITS = K + GUARD
MOD = 1 << BITS


# ----------------------------------------------------------------------
# Builder (T-9601 recursion, incremental form).
#
# State after stage k: digits d_0..d_{k-1} of the prefix a^(k),
#   m[i] = T^i(a^(k)) represented mod 2^BITS  (valid mod 2^(BITS-i)),
#   a[i] = number of odd steps among the first i steps.
# Flip update (L-9601 (F)): adding 2^k to the prefix adds
#   3^{a[i]} * 2^{k-i} to T^i, for every i <= k.
# ----------------------------------------------------------------------

def build(E, K):
    digits = []
    m = [0]
    a = [0]
    pow3 = [1]
    for k in range(K):
        e_k = E(digits)                       # strictly causal: prefix only
        if (m[k] & 1) != e_k:
            d_k = 1
            for i in range(k + 1):
                m[i] = (m[i] + pow3[a[i]] * (1 << (k - i))) % MOD
        else:
            d_k = 0
        digits.append(d_k)
        p = m[k] & 1
        assert p == e_k, "stage condition failed - builder bug"
        m.append((3 * m[k] + 1) // 2 % MOD if p else m[k] // 2)
        a.append(a[k] + p)
        while len(pow3) <= a[-1]:
            pow3.append(pow3[-1] * 3 % MOD)
    alpha = 0
    for d in reversed(digits):
        alpha = (alpha << 1) | d
    return alpha, digits


# ----------------------------------------------------------------------
# Independent verifier: direct orbit iteration, no shared orbit code.
# parity_i of alpha depends only on alpha mod 2^(i+1), so a K-digit
# representative certifies parity bits 0..K-1.
# ----------------------------------------------------------------------

def verify(E, alpha, K):
    x = alpha
    parities = []
    for _ in range(K):
        p = x & 1
        parities.append(p)
        x = (3 * x + 1) // 2 if p else x // 2
    digits = [(alpha >> k) & 1 for k in range(K)]
    for k in range(K):
        if parities[k] != E(digits[:k]):
            return False, k
    return True, None


def parity_prefix(alpha, n):
    x, out = alpha, []
    for _ in range(n):
        p = x & 1
        out.append(p)
        x = (3 * x + 1) // 2 if p else x // 2
    return out


def uniqueness_spot_check(E, alpha, digits, stages):
    """Confirm the rejected digit violates its stage condition."""
    for k in stages:
        flipped = alpha ^ (1 << k)
        p_k = parity_prefix(flipped, k + 1)[k]
        e_k = E(digits[:k])
        assert p_k != e_k, f"uniqueness violated at stage {k}"
    return True


# ----------------------------------------------------------------------
# Operator battery.
# ----------------------------------------------------------------------

def const_word(w):
    return lambda d: w[len(d) % len(w)]

def quine(e0):
    """Shifted quine: parity bit k := digit k-1 (Q-9603)."""
    return lambda d: d[-1] if d else e0

def antizero(d):
    """Reward zero digits with odd steps: e_k = 1 iff previous digit is 0."""
    return (1 - d[-1]) if d else 1

def prefix_parity(d):
    return sum(d) & 1

def thermostat(num, den):
    """Digit-driven supercritical thermostat: emit 1 while the digit
    ones-count is below (num/den) * k, else 0.  Exact comparison."""
    return lambda d: 1 if den * sum(d) < num * len(d) or not d else 0

def window_xor(d):
    x1 = d[-1] if len(d) >= 1 else 1
    x3 = d[-3] if len(d) >= 3 else 0
    return x1 ^ x3

def random_causal(seed):
    """Deterministic 'random' strictly causal operator: bit k is a hash of
    (seed, digit prefix)."""
    def E(d):
        h = hashlib.sha256()
        h.update(seed.encode())
        h.update(bytes(d))
        return h.digest()[0] & 1
    return E


def zero_runs(digits):
    best = cur = 0
    best_end = -1
    for i, d in enumerate(digits):
        cur = cur + 1 if d == 0 else 0
        if cur > best:
            best, best_end = cur, i
    tail = 0
    for d in reversed(digits):
        if d:
            break
        tail += 1
    return best, best_end, tail


def report(name, E, expect=None):
    alpha, digits = build(E, K)
    ok, bad = verify(E, alpha, K)
    assert ok, f"{name}: replay verifier failed at bit {bad}"
    uniqueness_spot_check(E, alpha, digits, SPOT_STAGES)
    par = parity_prefix(alpha, K)
    dd = sum(digits)
    pd = sum(par)
    zbest, zend, ztail = zero_runs(digits)
    line = (f"{name:>14}: digit-density {dd}/{K} = {dd/K:.4f}   "
            f"parity-density {pd}/{K} = {pd/K:.4f}   "
            f"max-0-run {zbest} (end {zend})   terminal-0-run {ztail}")
    checks = []
    if expect is not None:
        gate = (alpha == expect % (1 << K))
        checks.append("GATE-EXACT-MATCH" if gate else "GATE-FAIL")
        assert gate, f"{name}: validation gate failed"
    print(line + ("   [" + " ".join(checks) + "]" if checks else ""))
    print(f"{'':>14}  first 48 digits : {''.join(map(str, digits[:48]))}")
    print(f"{'':>14}  first 48 parity : {''.join(map(str, par[:48]))}")
    return alpha, digits


SPOT_STAGES = [1, 2, 3, 5, 13, 64, 100, K // 2, K - 2]

print(f"X-9601 foundry probe    K = {K} digits, working precision {BITS} bits")
print(f"uniqueness spot-check stages: {SPOT_STAGES}")
print()
print("--- constant-operator validation gates (open-loop corner, known answers) ---")
report("const (100)^w", const_word([1, 0, 0]), expect=pow(5, -1, 1 << K))
report("const (1)^w", const_word([1]), expect=-1)
report("const (10)^w", const_word([1, 0]), expect=1)
report("const (110)^w", const_word([1, 1, 0]), expect=-5)
print()
print("--- feedback probes (closed loop) ---")
# The expects below were DISCOVERED empirically on the first run of this
# probe, then identified in closed form and pinned as exact congruence
# gates; proofs (via T-9601 uniqueness): O-9601 for the quines and
# prefix-parity, L-9602 for the thermostats (alpha = -5/3).
report("quine e0=1", quine(1), expect=-1)
report("quine e0=0", quine(0), expect=0)
report("antizero", antizero)
report("prefix-parity", prefix_parity, expect=0)
report("thermo 7/10", thermostat(7, 10), expect=-5 * pow(3, -1, 1 << K))
report("thermo 9/10", thermostat(9, 10), expect=-5 * pow(3, -1, 1 << K))
report("window-xor", window_xor)
report("rand 'x9601a'", random_causal("x9601a"))
report("rand 'x9601b'", random_causal("x9601b"))
print()
print("All gates exact, all replays verified, all spot-checks passed.")
