# Endpoint pressure test: harmonic defects and the remaining logarithm

**Status: proved conditional endpoint consequences; no global closure.**
This companion uses the homogeneous ordinary variation lemma and the
logarithmic-profile comparison from `ORDINARY_DIRICHLET_COERCIVITY.md`.
It records what survives at exponent one and what the argument still lacks.

The reviewed main note is frozen at SHA-256
`d5229d794b97ba4c7663f105388ed597251d34fd678cc2189c39ebf0c7b43c74`.
Its ordinary source is PR146 at
`7d04c4dd756cfe495eb3eee78eba35a99085cd2a`, particularly
`research/upper-bit-mergers/TRIPLING_VARIATION.md` and
`THREE_RAY_VARIATION.md`. No new distribution assumption is introduced.

## 1. A conditional endpoint limit still holds

Let \(f\) be a bounded real or complex labeling with \(f(Tn)=f(n)\).
Put

\[
d(n)=|f(3n)-f(n)|,\qquad
D(X)=\sum_{\substack{n\le X\\n\ {\rm odd}}}d(n),\qquad Q=2C',
\]

where \(C,C'\ge1\) are the main note's variation constants. Assume

\[
\sum_{n\ge1}\frac{d(n)}n<\infty.                         \tag{E1}
\]

Then the dyadic logarithmic profiles

\[
g_k(t)=f(\lfloor2^{k+t}\rfloor),\qquad0\le t<1,
\]

converge in \(L^1\) to a constant \(c\). In particular, for Boolean
\(f\), one has \(c\in\{0,1\}\), and

\[
2^{-k}\sum_{2^k\le n<2^{k+1}}|f(n)-c|\longrightarrow0.    \tag{E2}
\]

**Proof.** The main note proves

\[
\|g_{k+1}-g_k\|_1
\le \frac{C}{2^k\ln2}D(Q2^k).
\]

At exponent one, replace its power estimate by Tonelli's exact geometric
bound:

\[
\sum_{k\ge0}2^{-k}D(Q2^k)
\le2Q\sum_{m\ {\rm odd}}\frac{d(m)}m<\infty.              \tag{E3}
\]

Thus the profiles form an \(L^1\)-Cauchy sequence. Also \(D(X)/X\to0\):
split the sum at a fixed \(M\), bound the finite initial contribution by
\(D(M)/X\), and bound the remaining contribution divided by \(X\)
by \(\sum_{m>M}d(m)/m\).

The ordinary rotation comparison in the main note is bounded by a
constant times \(D(AX)/X\), for a fixed \(A\). It therefore tends to
zero. The \(L^1\) limit is invariant under rotation by the irrational
\(\log_2 3\), so its nonconstant Fourier coefficients vanish and it
equals a constant almost everywhere. For Boolean labels, an almost
everywhere convergent subsequence forces that constant to be 0 or 1.
The lower logarithmic measure \(1/(2^{k+1}\ln2)\) of each integer cell
then gives (E2). QED.

## 2. Harmonic mass introduces a logarithmic defect kernel

Set \(h(n)=|f(n)-c|\). It is invariant, nonnegative, and satisfies (E2).
Its tripling defect is bounded by \(d(n)\). The same dyadic telescoping
argument at \(s=1\) gives the extended inequality

\[
N_1(h)=\sum_{n\ge1}\frac{h(n)}n
\le\frac C2\sum_{j\ge0}(j+1)2^{-j}D(Q2^j).               \tag{E4}
\]

For an odd integer \(m\), let
\(J_m=\max(0,\lceil\log_2(m/Q)\rceil)\). The exact kernel is

\[
\sum_{j\ge J_m}(j+1)2^{-j}
 =2^{1-J_m}(J_m+2).
\]

Consequently

\[
N_1(f-c)
\le C\sum_{m\ {\rm odd}}d(m)2^{-J_m}(J_m+2)
\le CQ\sum_{m\ {\rm odd}}
       \frac{(3+\log_2m)d(m)}m.                          \tag{E5}
\]

Thus a finite logarithmically weighted harmonic defect moment does give
finite centered harmonic mass. The weaker assumption (E1) proves the
profile limit, but (E4)–(E5) alone do not prove that centered harmonic
mass is finite. The factor \(j+1\) arises because there are \(j+1\)
earlier shells in the endpoint summation. Removing the resulting
logarithm requires additional information. This is a boundary of this
argument, not an impossibility theorem for another endpoint estimate.

## 3. Why the component complement does not close the argument

For a Boolean component indicator, boundedness gives only
\(0\le d(n)\le1\) and \(D(X)\le(X+1)/2\). These bounds imply
neither (E1) nor the stronger finite moment in (E5). No unconditional
upper bound of either kind has been proved for a hypothetical ordinary
separating component.

Replacing \(f\) by its complement \(1-f\) preserves the absolute
tripling defect at every integer. It therefore preserves every defect
moment in this note. When (E1) holds, it replaces the limiting constant
\(c\) by \(1-c\), while

\[
|(1-f)-(1-c)|=|f-c|.
\]

Taking the complement supplies no improvement to (E3) or (E5). A Boolean
limit of zero can describe a sparse exceptional component; a limit of
one can describe its complement. Neither statement says the sparse
component is empty.

The subcritical coercivity theorem leaves a hypothetical ordinary
component and its boundary with abscissa one unexcluded. Neither this
endpoint limit nor Booleanity supplies the missing arithmetic upper
estimate. Collatz remains unresolved by these arguments.
