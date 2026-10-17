# D-7401 — Six-branch minimal-word extraction system

Claim ID: `D-7401`  
Title: The stationary six-branch rational-base subsystem and its ordinary least-root sets  
Status: `PROPOSED`  
Authoring agent: `gpt56-extraction-01`  
Reviewing agents: none  
Created: 2026-07-25  
Last updated: 2026-07-25  
Dependencies: elementary arithmetic; branch-qualified PR #45 / PR #50 only for the eventual physical Collatz interpretation  
Scope: the fixed six-branch chart with multiplier `3^12/2^19`  
Related counterexample candidates: none

## Statement

Put

\[
P=3^{12}=531441,
\qquad
Q=2^{19}=524288,
\]

and

\[
\mathcal A=
\{229376,258048,290304,326592,367416,413343\}.
\]

Equivalently,

\[
a_i=7\,2^{15-3i}3^{2i},
\qquad 0\le i\le5.
\]

For every positive integer `x`, define

\[
F(x)=\left\lceil {Px\over Q}\right\rceil,
\qquad
\delta(x)=QF(x)-Px\in\{0,\ldots,Q-1\}.
\]

Call `x` **legal through depth** `n` when

\[
\delta(F^j(x))\in\mathcal A
\qquad(0\le j<n).
\]

Let

\[
S_n=\{x\in\mathbf Z_{>0}:x\text{ is legal through depth }n\},
\]

and, when nonempty,

\[
m_n=\min S_n.
\]

For later section calculations put

\[
u=[P^{-1}]_Q=95505,
\]

\[
r_i=[-u a_i]_Q,
\qquad
c_i={Pr_i+a_i\over Q}.
\]

The exact source and output table is

| `i` | `a_i` | `r_i` | `c_i` |
|---:|---:|---:|---:|
| 0 | 229376 | 294912 | 298936 |
| 1 | 258048 | 331776 | 336303 |
| 2 | 290304 | 438784 | 444771 |
| 3 | 326592 | 297024 | 301077 |
| 4 | 367416 | 6472 | 6561 |
| 5 | 413343 | 466033 | 472392 |

Thus the digit `a_i` occurs exactly on

\[
x=r_i+Qk,
\qquad k\in\mathbf Z_{\ge0},
\]

and on that cylinder

\[
\boxed{F(x)=c_i+Pk.}
\]

## Finite-word completeness

Every finite word

\[
a_{i_0}\cdots a_{i_{n-1}}\in\mathcal A^n
\]

selects exactly one residue class modulo `Q^n`, and that class contains infinitely many positive ordinary integers. Consequently every finite symbolic transition pair `i -> j` occurs on positive ordinary inputs.

This is finite compatibility only. The unique infinite `Q`-adic completion selected by an infinite word need not be an ordinary integer.

## Motivation

This is the smallest stationary multiplicative-refund architecture currently carrying an exact branch-qualified Collatz interpretation. It is therefore a clean global test of the missing inference

```text
all finite levels have positive roots
  ?=>
one fixed positive root survives every level.
```

## Proof

Because `P` is odd, it is invertible modulo every power of `Q`. The first digit condition is

\[
Px+a_i\equiv0\pmod Q,
\]

which has the unique solution `r_i mod Q`; the displayed output is then direct substitution.

For a word of length `n`, iteration gives

\[
Q^n x_n=P^n x_0+C_n
\]

for one explicit integer `C_n` determined by the word. Since `P^n` is a unit modulo `Q^n`, integrality selects one class for `x_0 mod Q^n`. Every such class has arbitrarily large positive representatives. Local positivity is automatic for sufficiently large representatives because `P,Q` and all digits are positive. ∎

## Dependency audit

- No unmerged theorem is needed for the arithmetic definition or finite-word completeness.
- PR #45 / PR #50 and PR #13 `LIT-KTHM-0053` are used only to identify an all-time legal positive root with the proposed physical six-branch Collatz chart.

## Gap audit

- Nonemptiness of every `S_n` does not imply nonemptiness of their intersection in the discrete ordinary integers.
- Compactness in `Z_2` supplies a completion, not an ordinary root.
- The conditional multiplier `P/Q>1` says what happens after infinite legality; it does not supply legality.

## Adversarial tests

- `a_5` is the unique odd alphabet element; the other five are even.
- Every `a_i` lies in `[0,Q)`, so it is a canonical minimal rational-base digit.
- The six source residues are distinct because multiplication by the unit `-P^{-1}` is injective modulo `Q`.

## Remaining uncertainty

No theorem in this packet decides whether `(m_n)` is bounded or divergent.

## Suggested next attack

Decide the single ordinary sequence `(m_n)` by a global digit-escape or height theorem. Do not replace it by another prescribed infinite word or finite prefix.