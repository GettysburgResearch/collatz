# L-6916 — Transported two-sided phase floor for odd-affine dyadic paths

**Claim ID:** `L-6916`  
**Status:** **PROPOSED pending independent review**  
**Authoring agent:** `gpt56-positive-tangent-01` (`GPT-5.6 Pro`)  
**Created:** 2026-08-01  
**Issue:** #75  
**Dependencies:** elementary odd-affine composition; conceptual inputs PR #47 `L-9611` and PR #48 `L-8210`  
**Scope:** finite exact past/future blocks meeting at one positive ordinary boundary

## 1. Setup

Let an exact finite past block carry a positive ordinary source `x_-` to a
boundary `x` through

\[
Q_- x=P_-x_-+C_-,
\tag{1}
\]

and let an exact finite future block carry that boundary to `x_+` through

\[
Q_+x_+=P_+x+C_+.
\tag{2}
\]

Assume

\[
Q_-,Q_+\text{ are powers of two},
\qquad
P_-,P_+\text{ are odd positive integers}.
\tag{3}
\]

All local physical divisibility and branch conditions are part of the phrase
“exact block.”

## 2. Output phase from the past

Reducing `(1)` modulo `P_-` gives

\[
Q_-x\equiv C_-\pmod {P_-}.
\]

Since `Q_-` is a unit modulo the odd number `P_-`, every exact realization of
the past block satisfies

\[
\boxed{
 x\equiv
 \Sigma_-:=[Q_-^{-1}C_-]_{P_-}
 \pmod {P_-}.}
\tag{4}
\]

This is the transported output phase supplied by the past.

## 3. Source phase from the future

Integrality of `(2)` gives

\[
P_+x+C_+\equiv0\pmod {Q_+}.
\]

Oddness of `P_+` therefore gives the unique future source phase

\[
\boxed{
 x\equiv
 \Theta_+:=[-P_+^{-1}C_+]_{Q_+}
 \pmod {Q_+}.}
\tag{5}

This is exactly the finite transported-cylinder residue of PR #48 `L-8210`.
For a changing-modulus quotient chain, composing the future maps produces
`Q_+=K_s`, `P_+=P_s`, and `C_+=B_s` in that claim's notation.

## 4. Two-sided CRT floor

The moduli in `(4)` and `(5)` are coprime. Let

\[
\eta(B_-,B_+)
\]

be the least positive representative of the unique CRT class

\[
 x\equiv\Sigma_-\pmod {P_-},
 \qquad
 x\equiv\Theta_+\pmod {Q_+}.
\tag{6}
\]

If the least nonnegative representative is zero, define the least positive
representative to be `P_-Q_+`.

Then every positive ordinary boundary realizing both exact blocks satisfies

\[
\boxed{x\ge\eta(B_-,B_+).}
\tag{7}
\]

### Proof

Equations `(4)` and `(5)` are necessary for any exact realization. CRT gives
one residue class modulo `P_-Q_+`. Every positive member of that class is at
least its least positive representative. ∎

## 5. Finite-library phase floor

For finite exact libraries `\mathcal P_u` of past blocks and `\mathcal F_v`
of future blocks, define

\[
\boxed{
H_{u,v}
=\min_{B_-\in\mathcal P_u,\ B_+\in\mathcal F_v}
 \eta(B_-,B_+).}
\tag{8}
\]

Every positive boundary having an admissible past block from
`\mathcal P_u` and future block from `\mathcal F_v` obeys

\[
\boxed{x\ge H_{u,v}.}
\tag{9}
\]

The finite computation of one exact `H_(u,v)` is therefore capable of proving
an all-depth theorem whenever a separate argument gives an upper bound below
that floor for every proposed trajectory in the declared architecture.

## 6. Existing results as special cases

### PR #47 two-sided pulse phase

For the negative-three pulse letters, a past word has odd multiplier
`P_-=9^u`, and a future word has dyadic source modulus `Q_+`. Equations
`(4)--(9)` reproduce PR #47 `L-9611`. Its cycle-minimum upper bound supplies
the independent upper estimate needed to turn a finite phase table into an
all-repetition cycle exclusion.

### PR #48 transported stack

For a nonstationary quotient chain, PR #48 `L-8210` gives the exact future
residue `Theta_+` after all intervening odd affine transports. The present
lemma adds the matching output phase from a finite exact past and combines the
two by CRT. Plain Euclidean radix digits cannot replace either phase.

### PR #45 six-branch chart

The stationary six-branch chart is the constant-radix instance. Its future
source residue is the stationary specialization

\[
\Theta_s=[-P^{-s}C_s]_{Q^s}.
\]

A fixed-modulus projection sees only the de Bruijn completion ghosts of PR #44.
A successful ordinary exclusion must instead prove that transported two-sided
floors, or the corresponding pulled-back least representatives, escape in the
Archimedean place.

## 7. Exact research consequence

The review of PRs #44, #45, #47, and #48 identifies the following reusable
architecture:

```text
finite exact past
    -> odd output phase;
finite exact future
    -> inverse-affine dyadic source phase;
CRT
    -> one ordinary boundary floor;
separate real/cycle/no-descent ceiling
    -> possible all-depth contradiction.
```

This explains why:

- fixed-modulus PDR cannot solve ordinary extraction;
- raw radix capacity is not future legality;
- the phase-floor method can nevertheless prove unbounded-repetition negative
  theorems when paired with a genuine ordinary upper bound.

## 8. Gap audit

- The lemma is a lower-bound compiler, not a proof that `H_(u,v)` grows.
- In a divergent architecture, large internal boundaries are compatible with
  a growing phase floor; a pullback to the same initial ordinary source is
  still required.
- A finite phase table is load-bearing only after the exact past/future
  libraries and an architecture-wide upper bound have been proved.
- This new lemma does not retroactively verify or strengthen any source claim
  in PR #44, #45, #47, or #48.
- No proof of SC*, FC*, or Collatz is claimed.
