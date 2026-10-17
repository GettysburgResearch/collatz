# L-8801 — Universal affine formula for an `ax+1` parity word

Claim ID: L-8801  
Title: Exact affine iterate formula for every odd multiplier  
Status: PROPOSED  
Authoring agent: `gpt56-drift-01`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: D-8801  
Scope: every odd `a >= 3`, every positive input, every finite admissible parity word  
Related counterexample candidates: issue #26; no `K-####` candidate

## Statement

Let `a >= 3` be odd. Suppose the first `L` iterates of a positive integer `n`
under `T_a` have parity word

```text
w=(eps_0,...,eps_(L-1))
```

and let `s=s(w)`. Then

```text
2^L * T_a^L(n) = a^s*n + B_a(w),
```

where `B_a(w)` is the correction from D-8801.

Equivalently, if `s_k=sum_(j<k) eps_j` and `B_k` is the correction of the first
`k` bits, then for every `0 <= k <= L`,

```text
2^k*T_a^k(n) = a^(s_k)*n + B_k.
```

If `w` contains at least one `1`, then `B_a(w)>0`.

## Definitions

All notation is from D-8801. The parity word is ordered in physical time: the
leftmost bit records the parity of the starting value.

## Motivation

This identity is the common arithmetic kernel of cycle reconstruction,
collision charts, fixed phases, residue cylinders, and parity-vector searches.
Proving it once for general odd `a` makes it possible to distinguish universal
format facts from constants special to `3x+1`.

## Proof or construction

Induct on the prefix length `k`.

For `k=0`,

```text
2^0*T_a^0(n)=n=a^0*n+0.
```

Assume

```text
2^k*T_a^k(n)=a^(s_k)*n+B_k.
```

If `eps_k=0`, the current value is even and

```text
2^(k+1)*T_a^(k+1)(n)
 = 2^k*T_a^k(n)
 = a^(s_k)*n+B_k.
```

Here `s_(k+1)=s_k` and the correction remains `B_k`, exactly the `w0`
recurrence.

If `eps_k=1`, the current value is odd and

```text
2^(k+1)*T_a^(k+1)(n)
 = 2^k*(a*T_a^k(n)+1)
 = a*(a^(s_k)*n+B_k)+2^k
 = a^(s_k+1)*n + a*B_k+2^k.
```

Here `s_(k+1)=s_k+1` and the correction is the `w1` recurrence. This proves the
formula for every prefix and hence for `k=L`.

The correction starts at zero, remains nonnegative, and at the first odd bit
becomes `2^k>0`; subsequent updates preserve positivity. Therefore any word
containing `1` has positive correction. **QED**

## Dependency audit

Only the definition of `T_a`, parity-word admissibility, and `B_a` in D-8801
are used.

## Gap audit

- The formula is conditional on the word being admissible at `n`. An arbitrary
  binary word cannot be substituted without an independent parity replay.
- The recurrence uses `2^k`, where `k` is the number of already processed bits.
- The multiplier `a` need not be prime. Oddness is not needed for this algebraic
  identity itself, but it is retained because later dyadic claims require it.
- Finite affine consistency does not establish an infinite ordinary orbit.

## Adversarial tests

X-8801 checks the identity for

```text
a in {3,5,7,9},
1 <= n <= 256,
1 <= L <= 12,
```

for 12,288 exact physical orbit prefixes.

## Remaining uncertainty

None known in the elementary induction. Independent reconstruction is pending.

## Suggested next attack

Use the correction as a symbolic polynomial in `a` and classify words for which
`a^s-2^L` divides the correction. This is the exact arithmetic gate for
same-phase expanding charts.
