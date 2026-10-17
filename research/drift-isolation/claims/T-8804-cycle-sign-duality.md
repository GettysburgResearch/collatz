# T-8804 — Cycle sign duality

Claim ID: T-8804  
Title: Positive shortcut cycles are subcritical and negative shortcut cycles are supercritical  
Status: PROPOSED  
Authoring agent: `gpt56-drift-01`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: L-8801, L-8803  
Scope: every nonzero signed periodic orbit of `T_a` for odd `a >= 3`  
Related counterexample candidates: issue #26; no `K-####` candidate

## Statement

Let `d != 0` be periodic under the signed shortcut map `T_a`. Suppose its
primitive period has length `L>=1`, parity word `w`, and odd-step count `s`.
Then

```text
(2^L-a^s)*d = B_a(w),                                  (1)
```

and `B_a(w)>0`. Consequently,

```text
d > 0   iff   2^L > a^s,
d < 0   iff   2^L < a^s.                                (2)
```

Equivalently:

- every positive nonzero shortcut cycle is multiplicatively subcritical;
- every negative shortcut cycle is multiplicatively supercritical;
- the signed phase of an exact same-phase cylinder determines the sign of its
  quotient multiplier.

More precisely, L-8803 lifts the cycle to

```text
T_a^L(2^L*q+d)=a^s*q+d.
```

This cylinder expands its quotient exactly when the underlying signed cycle is
negative.

For `a=5`, the signed cycle

```text
-2 -> -1 -> -2
```

has `L=2`, `s=1`, and generates the exact `4 -> 5` chart of T-8802. The known
positive control cycles have `2^L>5^s` and therefore generate contracting
same-phase cylinders.

## Definitions

- **Subcritical** means `a^s/2^L<1`.
- **Supercritical** means `a^s/2^L>1`.
- The zero fixed point is excluded because its all-even word has `B=0` and does
  not obey the strict sign alternatives.

## Motivation

This theorem connects three objects that were previously treated separately:
signed cycles, parity-word denominators, and exact expanding charts. It explains
why the simplest positive-drift amplifier arises from a negative orbit and gives
an exact search principle: look for negative periodic phase shadows to obtain
full-cylinder expansion.

## Proof or construction

Apply the affine parity-word formula L-8801 to the periodic phase `d`:

```text
2^L*T_a^L(d)=a^s*d+B_a(w).
```

Since `T_a^L(d)=d`, rearranging gives (1).

The word must contain an odd step. If it were all even, then

```text
T_a^L(d)=d/2^L=d,
```

forcing `d=0`, contrary to the hypothesis. The recursive definition of
`B_a(w)` starts at zero and adds a positive power of two whenever an odd bit is
read, multiplying earlier contributions by positive `a`. Hence `B_a(w)>0`.

Equation (1) now says that `d` and `2^L-a^s` have the same sign. Equality
`2^L=a^s` is impossible because its product with nonzero `d` would be zero while
`B_a(w)>0`. This proves (2).

The lifted same-phase identity is L-8803 with `T_a^L(d)=d`. **QED**

## Dependency audit

- L-8801 supplies the finite affine formula and positivity of the correction.
- L-8803 supplies the interpretation as a full dyadic-cylinder identity.
- No cycle census or unproved uniqueness claim is used.

## Gap audit

- The theorem classifies the sign of a cycle that already exists; it does not
  prove existence or uniqueness of signed cycles.
- Supercriticality of a negative phase cylinder does not imply a positive
  ordinary infinite orbit. The compatible infinite completion may remain
  negative, as in the constant directives of T-8802.
- A connector graph can contain nonperiodic signed phase paths; this theorem
  applies directly only to closed phase shadows.

## Adversarial tests

X-8802 exhausts parity words through length `18` for `a=5`, reconstructing one
negative cycle `[-2,-1]` and the positive cycles containing `1`, `13`, and `17`.
Every reconstructed cycle satisfies the sign rule. The finite census is not a
proof that no other cycles exist.

## Remaining uncertainty

None known in the sign theorem. Its usefulness for larger connector systems
depends on finding and classifying their signed strongly connected components.

## Suggested next attack

Search negative signed cycles for other odd multipliers and compare the
complexity of their low-digit rational-base subtrees. This may produce a family
of calibrated expanding control universes rather than a single `5x+1` example.
