# LIT-KTHM-0053 — The six-branch critical chart is a restricted minimal-word orbit in base `3^12/2^19`

**Status:** `KNOWN FRAMEWORK + NATIVE EXACT COROLLARY / PROPOSED MAPPING`  
**Created:** 2026-07-23  
**Native targets:** PR #45 `L-8407`; PR #50 `T-8305`, `L-8309`, `T-8307`  
**Primary sources inspected:** Akiyama–Frougny–Sakarovitch (2008); Dubickas (2009); Akiyama–Marsault–Sakarovitch (2018)  
**Conjectural neighboring source:** Andrieu–Eliahou–Vivion (2025/2026 revision)

## Statement

Put

\[
 P=3^{12}=531441,
 \qquad
 Q=2^{19}=524288,
\]

and let

\[
 \mathcal A=
 \{229376,258048,290304,326592,367416,413343\}.
\]

Equivalently,

\[
 \mathcal A=
 \left\{7\,2^{15-3i}3^{2i}:0\le i\le5\right\}.
\]

The six-branch boundary chart of PR #45/PR #50,

\[
 Qh_{n+1}=Ph_n+C_{i_n},
 \qquad C_i=3a_i,
\]

is exactly the following ordinary integer system after the intrinsic division

\[
 x_n=h_n/3:
\]

\[
 \boxed{Qx_{n+1}=Px_n+a_{i_n},\qquad a_{i_n}\in\mathcal A.}
\tag{1}
\]

Every digit in `A` lies in `[0,Q-1]`. Hence, whenever `(1)` is integral,

\[
 \boxed{x_{n+1}=\left\lceil {P x_n\over Q}\right\rceil,}
\tag{2}
\]

and `a_(i_n)` is the unique smallest outgoing digit from `x_n` in the rational-base representation tree for `P/Q`.

Consequently:

\[
 \boxed{
 \begin{minipage}{0.84\linewidth}
 A positive infinite six-branch chart path is exactly a positive integer root whose minimal (bottom) word in rational base `3^12/2^19` uses only the six digits in `A` forever.
 \end{minipage}}
\tag{3}
\]

The corresponding digit word is

\[
 a_n=Qx_{n+1}-Px_n.
\tag{4}
\]

Dubickas's complexity theorem therefore applies verbatim:

\[
 \boxed{
 \liminf_{L\to\infty}{p_a(L)\over L}
 \ge
 {\log Q\over\log(P/Q)}
 =971.866577472\ldots .}
\tag{5}
\]

In particular, no proposed controller whose output-word complexity has a smaller proved linear coefficient can generate such an ordinary path.

The recent normality conjecture for rational-base minimal words would exclude `(3)` immediately, because a normal word over `{0,...,Q-1}` cannot remain in a six-letter proper subset. This consequence is **conjectural** and is not used as a theorem.

## Proof of the exact native identification

PR #45 gives

\[
 Qh_{n+1}=Ph_n+C_i
\]

with

\[
 C_i=21\,2^{15-3i}3^{2i}=3a_i.
\]

Every chart boundary has positive `3`-adic valuation, so `x_n=h_n/3` is an ordinary positive integer. Division by three gives `(1)`.

For every integer `x`, an outgoing rational-base digit `a` is admissible exactly when

\[
 Px+a\equiv0\pmod Q.
\]

There is exactly one such residue in `[0,Q-1]`, namely

\[
 a=[-Px]_Q=Q\left\lceil{Px\over Q}\right\rceil-Px.
\]

All six native digits satisfy `0<=a_i<Q`, so an integral native edge is necessarily the unique minimal edge and `(2)` follows.

Conversely, the native constants have the exact form

\[
 C_i=Qe_i-Pd_i.
\]

If `(1)` holds with digit `a_i=C_i/3`, multiplication by three gives

\[
 Qh_{n+1}=Ph_n+C_i.
\]

Reducing modulo `Q` and `P` recovers respectively

\[
 h_n\equiv d_i\pmod Q,
 \qquad
 h_{n+1}\equiv e_i\pmod P.
\]

Thus the rational-base edge is not an over-approximation: it is exactly the physical chart branch.

Equation `(5)` is Dubickas's theorem for the ceiling map `(2)` and the digit sequence `(4)`.

## Literature consequences

1. Rational-base representation trees are highly nonregular, their integer-rooted subtrees are all distinct, and the successor map between bottom words requires an infinite sequential transducer. This supports the repository's conclusion that a bounded residue controller is not expected to preserve the exact ordinary root.
2. Every eventually periodic native type tail is excluded both by the elementary native sign argument and by the known non-eventual-periodicity of nonzero rational-base minimal words.
3. Marsault's nonrecognizability results for natural order and modulo-`Q` in rational base give an additional warning against replacing the ordinary root by a finite automaton.
4. Christoffel/Farey/Ostrowski literature remains useful for compiling finite critical words, but any infinite controller must also meet the very large complexity lower bound `(5)`.

## Exact positive target

Find one explicit positive integer `x_0` such that

\[
 a_n=Q\left\lceil{Px_n\over Q}\right\rceil-Px_n\in\mathcal A
 \quad\text{for every }n,
\]

where `x_(n+1)=ceil(Px_n/Q)`.

The PR #45/PR #50 physical conjugacy would then give an explicit positive unbounded shortcut-Collatz orbit. No completion-to-integer step would remain.

## Gap audit

- The normality statement is conjectural.
- The linear complexity lower bound does not exclude every six-letter word.
- Infinite rooted-tree/transducer complexity does not prove that no restricted ordinary root exists.
- No positive root satisfying `(3)` is supplied.
- Native claim statuses are not promoted by this literature note.
