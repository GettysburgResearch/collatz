# A finite critical spike forces a small ordinary ancestor

**Date:** 2026-11-22 UTC.  
**Status:** complete written corollary of
`POLYLOGARITHMIC_INVERSE_HORIZONS.md`, SHA256
`d4c5b9758f0e8ee1cb8f73d40f63ce8d5da642b48612b47842fd5b049bbd3824`.
It retains that note's source-qualified analytic dependencies. No new
infinite-depth or almost-everywhere-to-ordinary inference is used.

The useful conclusion here is an actual smaller ancestor, at a bounded
ordinary odd-step depth. Its hypothesis is a *finite* large density or
canonical-obstacle certificate. An arbitrarily late infinite-depth spike
does not meet that hypothesis automatically.

## 1. Only a finite predecessor floor is needed

For an integer horizon \(K\ge0\), replace condition (F) in the cited note by

\[
 \forall j\le K\ \forall n>0\text{ odd},\quad
 [3\nmid n\ \land\ U^j(n)=q]\ \Longrightarrow\ n\ge b.
 \tag{F_K}
\]

Theorem 1, equation (9), remains valid with this weaker hypothesis:

\[
 \max_{s\le K}D_s(q)/q
       \le b^{-1/2}+C_AK(K+2)m^{-A-1},
 \qquad 3^{4m}\le b,\quad m\ge1.
 \tag{1}
\]

Indeed every application of the counting estimate in its proof has prefix
depth \(d=s-jm-2m\), with \(1\le d\le K\). Its nonzero sources are
unit predecessors at that depth, so \(\omega\le q/b\) follows from
\((F_K)\). The base estimate uses only \(q\ge b\), the depth-zero part
of the floor, and no positive-depth predecessor assumption. Thus no
ancestor at a depth larger than \(K\) is used in this deduction.

## 2. Density certificate to ordinary ancestor

### Theorem

Fix \(B>0\), \(0<\gamma<1\), and \(\eta>0\). There is
\(Q=Q(B,\gamma,\eta)\) such that every positive odd unit \(q\ge Q\)
has the following property. If some integer \(s\le(\log q)^B\) satisfies

\[
                   D_s(q)\ge\eta q/\log(q+2),
 \tag{2}
\]

then there are a positive odd unit \(n\) and an integer \(j\) such that

\[
 \boxed{
 1\le j\le s,\qquad
 U^j(n)=q,\qquad
 n<\exp((\log q)^\gamma)<q.
 }
 \tag{3}
\]

**Proof.** Put \(b=\exp((\log q)^\gamma)\). For sufficiently large
\(q\), \(1<b<q\). Suppose that no unit predecessor of \(q\) within
depth \(s\) is smaller than \(b\). Then \((F_s)\) holds. Choose

\[
 m=\left\lfloor\frac{\log b}{4\log3}\right\rfloor
   =\left\lfloor\frac{(\log q)^\gamma}{4\log3}\right\rfloor.
\]

For sufficiently large \(q\), \(m\ge c(\log q)^\gamma\), with an
absolute \(c>0\), and \(3^{4m}\le b\). Choose a *fixed* exponent
\(A>0\) such that

\[
                    \gamma(A+1)>2B+2.
 \tag{4}
\]

Using (1) with \(K=s\),

\[
 \begin{aligned}
 D_s(q)/q
 &\le \exp\!\left(-\tfrac12(\log q)^\gamma\right)
       +C_A s(s+2)m^{-A-1}\\
 &=O_{A,B,\gamma}((\log q)^{-2})
   =o(1/\log(q+2)).
 \end{aligned}
 \tag{5}
\]

This contradicts (2) once \(q\) is large enough. Hence an actual unit
predecessor \(n<b\) exists at some depth \(j\le s\). It cannot be at
depth 0 because \(q>b\), so \(j\ge1\). This proves (3).
\(\square\)

The proof keeps \(A\) fixed before \(q\) varies. Its unknown source
constant \(C_A\) is absorbed into the stated threshold \(Q\), not treated
as 1 or as a uniform constant in \(A\).

## 3. Canonical obstacle certificate to ordinary ancestor

Using the source-proved finite comparison \(V_k(q)\le\kappa D_{k+1}(q)\),
the preceding theorem gives the following version.

For every fixed \(B>0\), \(0<\gamma<1\), and \(\eta>0\), all
sufficiently large positive odd units \(q\) satisfying

\[
 \exists k\le(\log q)^B:\qquad
                    V_k(q)\ge\eta q/\log(q+2)
 \tag{6}
\]

have a positive odd unit ancestor. For any witnessing \(k\) in (6), that
ancestor can be chosen to obey

\[
 \boxed{
 1\le j\le k+1,\qquad U^j(n)=q,\qquad
 n<\exp((\log q)^\gamma)<q.
 }
 \tag{7}
\]

To apply the theorem literally, use \(\eta/\kappa\) and any fixed
horizon exponent larger than \(B\); for sufficiently large \(q\), this
absorbs the additive 1 in \(k+1\). Alternatively the proof (5) works
directly with \(s=k+1\le2(\log q)^B\).

This is a smaller-source merger statement in the physical positive
integers: the forward orbit of \(n\) reaches \(q\) in at most \(k+1\)
ordinary odd steps. If convergence of every positive source below \(q\)
is separately established, that smaller source supplies convergence of
\(q\). No convergence hypothesis is needed to prove the ancestor itself.

## 4. What remains unresolved

A lower bound on \(V(q)=\sup_kV_k(q)\) guarantees some finite large
certificate, with a little slack in the threshold. It does **not** give a
certificate with \(k\le(\log q)^B\) for any fixed \(B\). The preceding
result therefore proves a concrete small-ancestor conclusion whenever
such a bounded-depth certificate exists. It does not prove that every
marked target has one, or that all ordinary sources are covered.

For a fixed escaping orbit, a small ancestor produced by (7) could also
belong to that same escaping component. One may not infer absorption merely
from the existence of a smaller member unless the required induction or
independent convergence premise has actually been supplied.
