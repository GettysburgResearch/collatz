# LIT-KTHM-0026 — Finite-state tilted transfer bound

**Verdict:** `FOLKLORE / STANDARD`; complete proof supplied.  
**Maps to:** issue #8's conditioned rare-event operator.  
**Literature context:** Chernoff bounds for Markov additive processes and Perron–Frobenius analysis of tilted transfer matrices.

Let \(P=(P_{ij})\) be a stochastic matrix on a finite state set, let \(g(i,j)\in\mathbb R\), and let

\[
G_n=\sum_{t=0}^{n-1}g(X_t,X_{t+1}).
\]

For \(s\in\mathbb R\), define the tilted matrix

\[
P_s(i,j)=P_{ij}e^{s g(i,j)}.
\]

## Theorem

For initial row distribution \(\mu\),

\[
\boxed{\mathbb E_\mu e^{sG_n}=\mu P_s^n\mathbf1.}
\tag{1}
\]

For \(s>0\),

\[
\boxed{
\Pr_\mu(G_n\ge an)
\le e^{-san}\mu P_s^n\mathbf1.
}
\tag{2}
\]

In particular, for any submultiplicative matrix norm,

\[
\Pr(G_n\ge an)
\le C_\mu e^{-san}\lVert P_s^n\rVert.
\]

If \(P_s\) is irreducible, Perron–Frobenius theory gives the exponential rate

\[
\limsup_{n\to\infty}\frac1n\log\Pr(G_n\ge an)
\le -sa+\log\rho(P_s).
\tag{3}
\]

Optimizing over \(s>0\) gives the usual finite-state Chernoff rate bound.

## Proof

Expand the expectation over state paths. Every transition contributes \(P_{ij}e^{s g(i,j)}=P_s(i,j)\); summing intermediate states is exactly matrix multiplication, proving (1). Markov's inequality applied to \(e^{sG_n}\) gives (2). The norm bound is immediate, and the Perron–Frobenius growth rate of powers of a finite irreducible nonnegative matrix gives (3). ∎

## Boundary

This theorem applies only after a finite truncation and its transition weights are frozen exactly. A spectral gap for one truncation does not automatically persist as modulus and depth grow. Conditioning must use the correct tilted/normalized operator; shuffled controls are diagnostic, not proofs.