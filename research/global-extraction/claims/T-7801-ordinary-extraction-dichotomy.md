# T-7801 — Ordinary extraction is bounded least-root stabilization

**Claim ID:** `T-7801`  
**Title:** Finite compatibility yields an ordinary infinite object exactly when canonical representatives stay bounded  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-global-01`  
**Created:** 2026-07-25  
**Last updated:** 2026-07-27 — cross-model prior-art and typography correction  
**Dependencies:** `D-7801`  
**Prior branch-qualified equivalent:** Fable foundations `L-9918.1` at `2cb80b4629ebfde5c8aaa3433c38e1382ea956b7`  
**Scope:** every canonical nested cylinder chain and every prefix-closed deterministic integer architecture  
**Related counterexample candidates:** none

## Prior in-repository formulation and novelty boundary

A later cross-model audit located an earlier in-repository formulation of the architecture-wide least-root dichotomy in Fable `L-9918.1`. Therefore Statement B below must not be read as the first repository occurrence of that theorem.

The present packet retains distinct additions:

1. the signed single-chain canonical-representative formulation in Statement A;
2. the finite-union packaging for several architectures;
3. the separate expanding-affine countermodel `R-7801`, which proves that arbitrarily strong refund does not repair ordinary extraction.

The prior-art correction changes attribution, not the mathematical statement.

## Statement A — one nested cylinder chain

Let

\[
1=M_0\mid M_1\mid M_2\mid\cdots,
\qquad M_N\to\infty,
\]

and let

\[
0\le R_N<M_N,
\qquad
R_{N+1}\equiv R_N\pmod {M_N}.
\]

Put

\[
a_N=\frac{R_{N+1}-R_N}{M_N}.
\]

Then the following are equivalent.

1. There exists \(x\in\mathbb Z_{\ge0}\) such that
   \[
   x\equiv R_N\pmod {M_N}
   \qquad(N\ge0).
   \]
2. The sequence \((R_N)\) is eventually constant.
3. The sequence \((R_N)\) is bounded.
4. \(\liminf_{N\to\infty}R_N<\infty\).
5. The appended digits satisfy
   \[
   a_N=0
   \qquad\text{for every sufficiently large }N.
   \]

When these conditions hold, the realizing nonnegative integer is unique and equals the eventual value of \(R_N\).

For signed ordinary integers, the selected inverse-limit point lies in \(\mathbb Z\) if and only if one of the following mutually exclusive alternatives holds:

- \(R_N\) is eventually constant, giving a nonnegative integer;
- \(M_N-R_N\) is eventually a fixed positive integer, giving a negative integer.

## Proof of Statement A

Because \(R_{N+1}\) and \(R_N\) are canonical nonnegative representatives of compatible classes,

\[
R_{N+1}=R_N+a_NM_N
\]

with \(a_N\ge0\). Hence \((R_N)\) is nondecreasing.

Assume a nonnegative integer \(x\) realizes every cylinder. Once \(M_N>x\), the unique representative of \(x\bmod M_N\) in \([0,M_N)\) is \(x\) itself. Thus

\[
R_N=x
\]

for every sufficiently large \(N\). This proves \(1\Rightarrow2\).

The implications

\[
2\Longrightarrow3\Longrightarrow4
\]

are immediate. Since \((R_N)\) is nondecreasing, finite liminf implies boundedness of the whole sequence, and an integer-valued nondecreasing bounded sequence is eventually constant. Hence \(4\Rightarrow2\).

The identity

\[
R_{N+1}-R_N=a_NM_N
\]

shows that eventual constancy is equivalent to eventual vanishing of \(a_N\). Thus \(2\Longleftrightarrow5\).

If \(R_N=x\) eventually, compatibility gives \(x\equiv R_N\pmod{M_N}\) at every earlier depth as well, so \(x\) realizes the chain. This proves \(2\Rightarrow1\).

If two ordinary integers realize every cylinder, their difference is divisible by every \(M_N\); because \(M_N\to\infty\), the difference is zero. This proves uniqueness.

For a negative integer \(x=-c\), choose \(N\) with \(M_N>c\). Its canonical residue is \(M_N-c\), so \(M_N-R_N=c\) eventually. Conversely, that eventual identity realizes \(-c\) at every late depth and hence, by compatibility, at every depth. This proves the signed statement. ∎

## Statement B — a whole deterministic architecture

Let

\[
\mathcal S_0\supseteq\mathcal S_1\supseteq\mathcal S_2\supseteq\cdots
\]

be the positive-integer survivor tower of `D-7801`. Assume every \(\mathcal S_N\) is nonempty and put

\[
m_N=\min\mathcal S_N.
\]

Then the following are equivalent.

1. There exists a positive integer surviving every depth:
   \[
   \bigcap_{N\ge0}\mathcal S_N\ne\varnothing.
   \]
2. The least-root sequence \((m_N)\) is bounded.
3. The least-root sequence \((m_N)\) is eventually constant.

If these conditions fail, then

\[
m_N\longrightarrow\infty
\]

and the architecture is ordinarily empty.

## Proof of Statement B

The nesting of the survivor sets makes \((m_N)\) nondecreasing.

If \(x\) survives every depth, then

\[
m_N\le x
\]

for every \(N\), so \((m_N)\) is bounded.

Conversely, a nondecreasing bounded integer sequence is eventually constant, say

\[
m_N=m
\qquad(N\ge N_0).
\]

For every \(N\ge N_0\), the definition of the minimum gives \(m\in\mathcal S_N\). For an earlier depth \(j<N_0\), choose \(N\ge N_0\); nesting gives

\[
m\in\mathcal S_N\subseteq\mathcal S_j.
\]

Hence \(m\) belongs to every survivor set. This proves the equivalence.

If the equivalent conditions fail, a nondecreasing sequence of positive integers must tend to infinity. ∎

## Counterexample and exclusion corollary

Suppose a separately proved theorem makes the architecture counterexample-complete on survivors.

- If \((m_N)\) is bounded, its eventual value is an explicit ordinary infinite seed. After exact replay, it qualifies for a `K-####` candidate file.
- If \(m_N\to\infty\), no positive integer follows the architecture forever, so the entire prescribed architecture is eliminated.

This dichotomy is genuinely narrower than the Collatz conjecture. It decides one exact induced language or finite union of languages, not every positive Collatz orbit.

For finitely many architectures \(A_1,\ldots,A_r\), let

\[
m_N=\min_i m_N^{(i)}.
\]

Then boundedness of \(m_N\) produces a survivor in at least one architecture, while \(m_N\to\infty\) eliminates their complete finite union.

## Why compactness is insufficient

If every finite prefix is realizable, the corresponding finite residue tree may have an infinite path by compactness or König's lemma. That path supplies a compatible inverse-limit point. Statement A shows that ordinary extraction requires the additional archimedean assertion that the canonical representatives are bounded.

Neither nonemptiness of every level nor uniqueness of the inverse-limit point contains that assertion.

## Exact global blocker

For every positive architecture in the current repository, the extraction problem should be stated in one of these equivalent forms:

```text
prove sup_N m_N < infinity;
prove m_N eventually stabilizes;
write one finite integer that survives all N;
```

or, on the negative side,

```text
prove m_N -> infinity.
```

A theorem that proves only conditional growth of later states, abundance of finite lifts, positive-density refund, fresh-prime turnover, or small Haar measure does not decide any of these statements.

## Gap audit

- The theorem does not determine \((m_N)\) for any particular Collatz subsystem.
- A bounded subsequence of arbitrary noncanonical representatives is irrelevant; the theorem uses canonical least representatives or nested positive survivor sets.
- For signed extraction, eventual upper-end stabilization must be kept separate from positive extraction.
- Statement B has branch-qualified prior art in `L-9918.1`; novelty claims must retain the boundary stated above.
- The result is elementary, but it is load-bearing: it identifies exactly which repeatedly used compactness inference is invalid.
