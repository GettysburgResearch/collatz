# T-0021 — Bounded-tail affine counter lanes cannot close at all heights

Claim ID: `T-0021`  
Title: Nondegenerate power-sum obstruction for affine padding updates with finite high-tail libraries  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-21  
Dependencies: `L-0016`, `L-0017`  
External infrastructure: PR #13 `LIT-KTHM-0008` — nondegenerate power sums have finitely many zeros  
Scope: finite families of cycle-padded tower types with affine counter updates and bounded ordinary high tails  
Related counterexample candidates: none

## Statement

Consider one source tower type \(E\) and one target tower type \(F\), each in the notation of `L-0016`.

For the source write

\[
k_t=k_0+\ell t,
\qquad
g_t=g_0+at,
\]

with recovery data \(r,b\), periodic core \(\mu_t\), and quotient output

\[
q'_E(t,h)
=
\frac{3^b\bigl(3^{g_t}(\mu_t+2^{r+1}h)+1\bigr)}{2^{r+1}}.
\tag{1}
\]

For the target write

\[
\bar k_u=\bar k_0+\bar\ell u,
\]

with recovery depth \(\bar r\), periodic core \(\bar\mu_u\), and binary input quotient

\[
q_F(u,h')
=
2^{\bar k_u}igl(\bar\mu_u+2^{\bar r+1}h'\bigr).
\tag{2}
\]

Fix:

- one source high tail \(h\ge0\);
- one target high tail \(h'\ge0\);
- integers \(c\ge1\) and \(d\), with
  \[
  u=ct+d\ge0
  \]
  on the heights considered.

Then the exact connector equality

\[
\boxed{
q'_E(t,h)=q_F(ct+d,h')
}
\tag{3}
\]

holds for only finitely many integers \(t\ge0\).

### Finite-library consequence

Let there be finitely many source and target tower types, finitely many high tails attached to each type, and finitely many affine counter rules

\[
t'=c_et+d_e.
\]

Then only finitely many tower heights realize any exact transition in that whole library.

Consequently no all-height counter-stack Collatz certificate can be built from all three of the following restrictions simultaneously:

1. finitely many tower types;
2. a finite bounded high-tail library;
3. finitely many affine counter-update rules.

At least one genuinely unbounded resource is necessary. In the present framework the natural resource is the ordinary high tail \(h\), carried as a growing stack word or unbounded cofactor.

## Proof

By `L-0016`, the core residues \(\mu_t\) and \(\bar\mu_u\) are periodic. Let their periods be \(P\) and \(\bar P\).

Suppose (3) held for infinitely many \(t\). Partition those heights into finitely many residue classes modulo a common multiple of

\[
P
\quad\text{and}
\quad
\bar P
\]

pulled back through the affine map \(u=ct+d\). One class contains infinitely many solutions. Write its heights as

\[
t=t_0+Qn,
\qquad n\ge0,
\tag{4}
\]

so that both periodic cores are constant on the class:

\[
\mu_t=\mu_*,
\qquad
\bar\mu_{ct+d}=\bar\mu_*.
\tag{5}
\]

On this progression, the source output (1) is

\[
q'_E(t,h)
=C\alpha^n+D,
\tag{6}
\]

where

\[
\alpha=3^{aQ}>1,
\]

\[
C=
\frac{3^{b+g_0+at_0}}{2^{r+1}}
\bigl(\mu_*+2^{r+1}h\bigr)>0,
\]

and

\[
D=\frac{3^b}{2^{r+1}}>0.
\]

The target input (2) is

\[
q_F(ct+d,h')=E\beta^n,
\tag{7}
\]

where

\[
\beta=2^{\bar\ell cQ}>1
\]

and

\[
E=
2^{\bar k_0+\bar\ell(ct_0+d)}
\bigl(\bar\mu_*+2^{\bar r+1}h'\bigr)>0.
\]

Thus (3) becomes the three-term power-sum equation

\[
\boxed{
C\alpha^n-E\beta^n+D=0.
}
\tag{8}
\]

All three coefficients are nonzero. The pairwise quotients of the bases

\[
\alpha,
\qquad
\beta,
\qquad
1
\]

are not roots of unity:

- \(\alpha\) is a positive power of three;
- \(\beta\) is a positive power of two;
- \(\alpha/\beta\ne1\) by unique prime factorization.

Therefore (8) is a nondegenerate power sum. PR #13's imported theorem `LIT-KTHM-0008` implies that it has only finitely many zeros \(n\ge0\), contradicting the assumed infinite set. This proves the first statement.

The finite-library consequence follows by taking a finite union of finite exceptional sets. ∎

## Stronger geometric reading

For fixed \(h\), the source input quotients themselves split into finitely many exact dyadic rays. Indeed, on one core residue class \(t=s+Pj\),

\[
q_E(t,h)
=2^{k_0+\ell s}
\bigl(\mu_s+2^{r+1}h\bigr)
\left(2^{\ell P}\right)^j.
\tag{9}
\]

The theorem says that an affine-height connector cannot repeatedly match the corresponding ternary exponential output ray to another dyadic input ray. The obstruction is not lack of finite examples; it is multiplicative independence of two and three.

## Interpretation

The proposed state

\[
(i,t,\rho,n)
\]

cannot use \(t\) as its only unbounded storage while letting \(n\) be selected from a fixed finite library at each control state. A valid construction must let the ordinary high tail vary without bound and transport actual data between levels.

This sharply narrows `Q-0019`:

> the next object is not merely a one-counter automaton; it is a counter-controlled stack or cofactor transducer.

The connector lemma `L-0017` supplies exactly the required data channel:

\[
\eta+2^Kz
\longmapsto
\theta+3^Gz.
\]

## Dependency audit

- `L-0016` supplies the periodic core and exact source/target formulas.
- `LIT-KTHM-0008` is used only after all coefficients and bases are displayed and the nondegeneracy hypotheses are checked.
- The theorem concerns exact equality, not merely congruence or high valuation.

## Gap audit

- The theorem does not exclude nonlinear counter updates.
- It does not exclude an unbounded high tail \(h_t\), a branching tail language, or a pushdown stack.
- Skolem–Mahler–Lech is ineffective here; the proof supplies no computable final exceptional height.
- A finite-height experiment cannot verify the qualitative finiteness conclusion by exhaustion.

## Adversarial tests

`X-0012` verifies the exact periodic cores and connector formulas used before the power-sum reduction. The finiteness step is a literature-backed theorem, not an empirical claim.

## Suggested next attack

Promote the free high tail \(z\) in `L-0017` to the principal stack object. Search for a finite transducer on its LSD-first digits whose control is the tower type and padding height, and whose output tail contains a larger copy of the same stack schema.