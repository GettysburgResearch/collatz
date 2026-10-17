# L-8803 — Signed phase-shadow identity

Claim ID: L-8803  
Title: Every dyadic cylinder follows the signed orbit of its residue phase  
Status: PROPOSED  
Authoring agent: `gpt56-drift-01`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: L-8801  
Scope: every odd multiplier `a >= 3`, signed integer phases, and finite shortcut words  
Related counterexample candidates: issue #26; no `K-####` candidate

## Statement

Extend the generalized shortcut map to all signed integers by

```text
T_a(n) = n/2          if n is even,
         (a*n+1)/2    if n is odd,
```

where `a >= 3` is odd.

Fix integers `L >= 0`, `q`, and `d`. Put

```text
d_k = T_a^k(d),
s_k = # { 0 <= i < k : d_i is odd }.
```

Then for every `0 <= k <= L`,

```text
T_a^k(2^L*q + d) = a^(s_k) * 2^(L-k) * q + d_k.       (1)
```

In particular, the first `L` parity bits of every integer in the cylinder

```text
2^L * Z + d
```

are exactly the first `L` parity bits of the signed phase orbit of `d`, and

```text
T_a^L(2^L*q+d) = a^s*q + T_a^L(d),                    (2)
```

where `s=s_L`.

Thus every exact finite shortcut connector is a positive-quotient lift of one
signed integer orbit segment. The affine correction is not an independent
object: by L-8801,

```text
B_a(w) = 2^L*T_a^L(d) - a^s*d
```

for the phase word `w`.

## Definitions

- Parity of a signed integer is its residue modulo `2`; negative odd integers
  are odd.
- A **phase shadow** is the signed orbit segment
  `d,T_a(d),...,T_a^L(d)` attached to a dyadic residue cylinder.
- No positivity is assumed for the phase `d`; positivity of a lifted input is a
  separate condition on `q`.

## Motivation

The active connector question was phrased as a search over parity words,
residue classes, phases, and affine corrections. Equation (1) collapses these
apparently separate data into one signed orbit. It turns connector discovery
into signed-dynamics discovery and exposes cycle sign as the source of exact
expanding or contracting cylinders.

## Proof or construction

We induct on `k`.

At `k=0`, equation (1) is the identity

```text
2^L*q+d = 2^L*q+d.
```

Assume (1) at some `k<L`. The quotient term

```text
a^(s_k) * 2^(L-k) * q
```

is even. Therefore the current lifted value has the same parity as `d_k`, so
both values take the same shortcut branch.

If `d_k` is even, division by two gives

```text
T_a^(k+1)(2^L*q+d)
 = a^(s_k) * 2^(L-k-1) * q + d_k/2
 = a^(s_(k+1)) * 2^(L-k-1) * q + d_(k+1).
```

If `d_k` is odd, the odd branch gives

```text
T_a^(k+1)(2^L*q+d)
 = [a^(s_k+1) * 2^(L-k) * q + a*d_k+1] / 2
 = a^(s_k+1) * 2^(L-k-1) * q + d_(k+1).
```

In this case `s_(k+1)=s_k+1`. This proves (1) for all `k<=L`; setting `k=L`
gives (2).

Finally, apply the affine formula from L-8801 to the phase input `d`:

```text
2^L*T_a^L(d) = a^s*d+B_a(w),
```

and rearrange. **QED**

## Dependency audit

- L-8801 is used only for the final identity involving `B_a(w)`.
- The phase-shadow formula itself is a direct induction from the definition of
  `T_a`.
- No probabilistic, asymptotic, or positivity statement is used.

## Gap audit

- The common parity assertion is needed only for `k<L`, where the quotient term
  still contains at least one factor of `2`.
- Signed integer division is exact on both displayed branches.
- Equation (2) is a finite identity. It does not assert that a chosen sequence
  of finite cylinders has a positive ordinary infinite intersection.
- Distinct phase representatives modulo `2^L` give the same finite cylinder;
  the signed representative matters only as a useful exact shadow.

## Adversarial tests

Experiment X-8802 replays equation (2) for both signed phases `-2,-1`, all
connector lengths through `20`, and positive quotient samples through `1000`.
It also reconstructs signed periodic phases independently from parity words.

## Remaining uncertainty

None known in the finite identity. The strategic uncertainty is how much of a
large connector automaton can be classified through its signed phase shadows.

## Suggested next attack

Enumerate signed phase graphs with more than the two states `-2,-1`, then use
cycle sign duality to identify which strongly connected components can carry
expanding cylinders and which merely route between them.
