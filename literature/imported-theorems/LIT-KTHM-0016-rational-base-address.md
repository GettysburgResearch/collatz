# LIT-KTHM-0016 — Rational-base address identity and bounded real tail

**Verdict:** `FOLKLORE / STANDARD`; complete proof supplied.  
**Maps to:** `PR3/T-0010` and signed negative-return systems.  
**Nearby literature:** Akiyama–Frougny–Sakarovitch on rational-base numeration. Their canonical languages are nearby objects, not an exact identification with the repository's cylinder-selected signed system.

Let integers \(1<M<N\) be given, let \(A\subset\mathbb Z\) be finite, and suppose

\[
Nq_t=Mq_{t+1}+a_t,
\qquad a_t\in A.
\tag{1}
\]

Put \(eta=N/M\) and \(ho=M/N\).

## Theorem

For every \(k\ge1\),

\[
\boxed{N^kq_0-M^kq_k=
\sum_{t=0}^{k-1}a_tN^{k-1-t}M^t.}
\]

For an infinite chain define

\[
x_t=\frac1N\sum_{j\ge0}a_{t+j}\rho^j.
\]

There is a real \(C\) such that

\[
\boxed{q_t=C\beta^t+x_t},
\]

and

\[
\frac{\min A}{N-M}\le x_t\le\frac{\max A}{N-M}.
\]

If every \(q_t\) is integral, then the fractional parts of \(C\beta^t\) remain in an arc of length at most

\[
\boxed{\operatorname{diam}(A)/(N-M).}
\]

## Proof

Multiply (1) at time \(t\) by \(N^{k-1-t}M^t\) and sum; the quotient terms telescope. Equation (1) is also \(q_{t+1}=\beta q_t-a_t/M\). Direct calculation gives the identical recurrence for \(x_t\), so \(q_t-x_t=C\beta^t\). The coefficients in \(x_t\) are nonnegative and sum to \(1/(N-M)\), giving the bounds. Finally \(C\beta^t=q_t-x_t\); reduce modulo one and use integrality of \(q_t\). ∎

## Boundary

A narrow real window is necessary, not sufficient. It neither proves dyadic cylinder admissibility nor turns a `p`-adic compatible path into an ordinary integer.