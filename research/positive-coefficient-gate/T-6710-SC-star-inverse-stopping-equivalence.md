# T-6710 — SC* inverse stopping equivalence and finite source escape

**Claim ID:** `T-6710`  
**Status:** **PROPOSED**  
**Authoring agent:** `gpt56-positive-review-01` (`GPT-5.6 Pro`)  
**Issue:** #75  
**Dependencies:** finite parity-cylinder bijection; elementary shortcut affine identity  
**Scope:** exact reformulation and quantitative finite transfer for the all-supercritical source problem

## 1. Definitions

For the shortcut Collatz map let

\[
q_k(n)=\#\{0\le i<k:T^i(n)\text{ odd}\},
\qquad
C_k(n)=\frac{3^{q_k(n)}}{2^k},
\]

and define the coefficient stopping time

\[
\tau_c(n)=\min\{k\ge1:C_k(n)<1\},
\]

with `tau_c(n)=infinity` if no such `k` exists.

For `N>=0`, define the positive all-supercritical survivor set

\[
S_N=\{n\ge1:C_k(n)\ge1\text{ for every }1\le k\le N\},
\]

and its least element

\[
m_N=\min S_N.
\]

The set is nonempty at every finite depth because every binary parity word of length `N` has one positive residue class modulo `2^N`, and all-supercritical words exist at every finite depth.

Equivalently, if `W_N^sup` is the family of length-`N` all-supercritical parity words and `r_w in {1,...,2^N}` is the canonical positive source of `w`, then

\[
m_N=\min_{w\in W_N^{\rm sup}}r_w.
\]

## 2. Exact inverse theorem

For every integer `B>=1`, put

\[
H(B)=\max_{1\le n\le B}\tau_c(n),
\]

provided all displayed stopping times are finite.

Then for every `N>=0`,

\[
\boxed{
m_N>B
\iff
\tau_c(n)\le N\text{ for every }1\le n\le B.
}
\]

Consequently, whenever `H(B)<infinity`,

\[
\boxed{m_N>B\qquad(N\ge H(B)).}
\]

### Proof

By definition, `n in S_N` iff `tau_c(n)>N`. Therefore `m_N>B` iff no integer `1<=n<=B` belongs to `S_N`, iff `tau_c(n)<=N` for every such `n`. Taking `N>=H(B)` gives the stated source-escape bound. ∎

## 3. SC* is exactly coefficient stopping

The sets `S_N` are nested decreasing, hence `m_N` is nondecreasing. Moreover,

\[
\bigcap_{N\ge0}S_N
=
\{n\ge1:\tau_c(n)=\infty\}.
\]

Therefore

\[
\boxed{
m_N\longrightarrow\infty
\iff
\tau_c(n)<\infty\text{ for every positive integer }n.
}
\]

Thus repository target `SC*` is exactly the coefficient-stopping-time conjecture in canonical-source language. It is not merely analogous to that conjecture.

### Proof

If some fixed `n` has `tau_c(n)=infinity`, then `n in S_N` for every `N`, so `m_N<=n` for every `N` and source escape fails.

Conversely, if `m_N` does not tend to infinity, monotonicity makes it bounded. Since it is integer-valued, it eventually stabilizes at some `n`. Then `n in S_N` for every depth, so `tau_c(n)=infinity`. ∎

## 4. Transfer from ordinary convergence certificates

Let `sigma_1(n)` be any certified time at which the orbit reaches `1`.
For `n>1`, the exact affine identity

\[
1=T^{\sigma_1(n)}(n)=C_{\sigma_1(n)}(n)n+E_{\sigma_1(n)},
\qquad E_{\sigma_1(n)}\ge0,
\]

implies

\[
C_{\sigma_1(n)}(n)\le\frac1n<1.
\]

Hence

\[
\tau_c(n)\le\sigma_1(n).
\]

For `n=1`, the shortcut word `10` gives `C_2=3/4<1`.

Therefore, if a finite verification certifies that every `1<=n<=B` reaches `1` within at most `R(B)` shortcut steps, then

\[
\boxed{m_N>B\qquad(N\ge\max\{2,R(B)\}).}
\]

This is a proof-grade conversion from a finite convergence certificate into a canonical SC* source lower bound. It requires the actual maximal certified hitting-time bound, not merely the statement that all starts below `B` converge.

## 5. Fixed-source valuation form

For a length-`N` parity word `w`, let `q=q(w)` and let `A_w` be the affine numerator:

\[
T_w(x)=\frac{3^q x+A_w}{2^N}.
\]

A fixed positive integer `n` realizes `w` through depth `N` exactly when

\[
v_2(3^q n+A_w)\ge N
\]

and the induced parity prefix is `w`. Thus SC* is also equivalent to the fixed-source statement:

> For every fixed positive integer `n`, there is a finite bound on the length of an all-supercritical word `w` satisfying `v_2(3^{q(w)}n+A_w)>=|w|`.

This is the exact source-level `2`-adic inequality still missing from the present repository estimates.

## 6. Relation to T-6709 and the newer stack

`T-6709` classifies any hypothetical element of the intersection `cap_N S_N`: its ordinary orbit tends to `+infinity`. PR #80 proves that the known scalar bank, density, and correction-product estimates do not by themselves empty this intersection. PR #81 names the same source escape as `SC*`; PR #83 shows that thinness or zero family entropy is still not emptiness.

The present theorem therefore gives the exact logical status:

```text
T-6709:
  any fixed ordinary survivor is divergent;

T-6710:
  SC* emptiness is exactly universal finite coefficient stopping;

missing:
  one fixed-source valuation/canonical-boundary inequality proving that emptiness.
```

## 7. Gap audit

- This theorem does not prove `SC*`; it proves an exact equivalence and finite transfer.
- A finite convergence range gives only a finite lower bound on `m_N` unless a cofinal family of verified ranges with explicit maximal hitting times is supplied.
- The low-band remainder estimates control endpoints and growth after ordinary realization. They do not by themselves bound the canonical source residue.
- Any claimed proof of SC* must use the fixed source in the divisibility relation, not merely an abstract compatible parity path or scalar surplus profile.

## 8. Exact next inequality

A sufficient closing theorem is any function `Phi(n)<infinity` such that for every all-supercritical finite word `w` realized from source `n`,

\[
|w|\le\Phi(n).
\]

Equivalently, it suffices to prove

\[
v_2(3^{q(w)}n+A_w)<|w|
\]

for all all-supercritical `w` beyond a source-dependent finite threshold. A uniform effective `Phi` would immediately yield the quantitative inverse lower bound

\[
m_N>\max\{B:\Phi(B)\le N\}.
\]
