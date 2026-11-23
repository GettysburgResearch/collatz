# Critical iid statistics do not determine one infinite ray

Date: 23 November 2026. **Status: written construction and proof, independently
reviewed; finite arithmetic controls accompany it. No new Lean theorem is
claimed. The resulting sources are irrational 2-adic integers almost surely,
not positive ordinary integer counterexamples.**

This construction tests a possible closing step in the actual stationary-law
route: can critical iid empirical gap statistics, even together with a strict
forward pressure minimum and sublinear bridge oscillation, force recurrence
of the particular ray being studied? The answer to that general implication
is no. Sparse insertions produce a single consistent infinite ray with all
those properties and a finite normalized inverse tail. A second construction
reverses the pressure sign and tests the separate stationary real-series
conclusion. The two series and the two origin conditions are kept distinct.

The construction is elementary. Its purpose is the precise application
boundary in this repository, not a claim of a new general theorem about
generic points. The accompanying ordinary-source insertion theorem identifies
an arithmetic condition that this symbolic construction does not satisfy.

## 1. Two real series, and the exact claim

Let

\[
 \ell=\log_2 3,\qquad p=1/\ell,\qquad
 \gamma(k)=p(1-p)^{k-1}\quad(k=1,2,\ldots).
\]

For an infinite positive gap word \(b=(b_1,b_2,\ldots)\), put

\[
 B_0=0,\quad B_j=\sum_{i=1}^j b_i,\quad
 T_j=j\log3-B_j\log2,\quad \chi_j=e^{T_j}=3^j2^{-B_j}.
 \tag{1}
\]

The two real series relevant here have opposite multipliers:

\[
 S(b)=\frac13\sum_{j\ge0}\chi_j^{-1}
      =\sum_{j\ge0}\frac{2^{B_j}}{3^{j+1}},\qquad
 R(b)=\frac13\sum_{j\ge1}\chi_j
      =\sum_{j\ge1}\frac{3^{j-1}}{2^{B_j}}.
 \tag{2}
\]

The first is the normalized **forward inverse tail**. If a real trajectory
follows the gaps, its affine formula is

\[
 q_j=\chi_j\left(q_0+\frac13\sum_{i=0}^{j-1}\chi_i^{-1}\right).
 \tag{3}
\]

The second is the **reversed-gap real series** used in PR180's stationary
lift. Neither (2) nor (3) identifies their different real values.

**Theorem GR+.** There is a nonatomic law on infinite gap words such that,
almost surely, all of the following hold:

1. Every finite contiguous word has its iid \(\gamma\)-product frequency.
2. \(B_j/j\to\ell\), including the unbounded first moment, and \(T_j/j\to0\).
3. \(T_j>0\) for every \(j>0\), and
   \(\chi_j\ge(j/2)^3\) for every sufficiently large \(j\).
4. \(S(b)<\infty\), whereas \(R(b)=\infty\).
5. The bridge oscillation
   \[
   V_N=\max_{0\le j\le N}(T_j-jT_N/N)
       -\min_{0\le j\le N}(T_j-jT_N/N)
   \tag{4}
   \]
   is \(o(N)\).
6. The exact 2-adic source coded by the word is irrational almost surely.

**Theorem GR-.** A second nonatomic law has properties 1, 2, 5, and 6,
but satisfies \(T_j<0\) for all \(j>0\), eventually
\(\chi_j\le8j^{-3}\), and consequently \(R(b)<\infty\),
\(S(b)=\infty\).

GR+ retains a strict forward pressure minimum and finite inverse tail. GR-
shows why empirical iid genericity cannot by itself transfer stationary
critical divergence of \(R\) to a selected ray. GR- does **not** retain the
minimum condition: its origin is a strict maximum. Neither theorem supplies
the canonical harmonic path law of an escaping component or an ordinary
integer source.

## 2. An iid input and a sublinear regulator

Take raw iid gaps \(G_1,G_2,\ldots\) with law \(\gamma\). Write

\[
 A_n=\sum_{i=1}^nG_i,\qquad
 Z_n=n\log3-A_n\log2,\qquad h(n)=3\log(n+1).
 \tag{5}
\]

Work on the probability-one event on which

\[
 A_n/n\to\ell,\qquad Z_n/n\to0,
 \tag{6}
\]

and every finite raw gap word has its iid frequency. The last assertion
holds simultaneously because the finite words form a countable set. For
each fixed word of length \(r\), split its possible starting positions
into residue classes modulo \(r\); the indicators within each class are
independent, so the strong law gives the required frequency. Intersect
these events with (6).

A deterministic consequence used repeatedly is

\[
 \max_{0\le k\le n}|Z_k|=o(n).
 \tag{7}
\]

Indeed, for any \(\varepsilon>0\), the late terms obey
\(|Z_k|\le\varepsilon k\le\varepsilon n\); the maximum over a fixed
initial segment divided by \(n\) tends to zero.

For GR+, let \(c=\log(3/2)>0\) and set

\[
 I_n=\max_{0\le k\le n}
 \max\left(0,\left\lceil\frac{h(k)-Z_k}{c}\right\rceil\right),
 \qquad I_0=0.
 \tag{8}
\]

Immediately before raw gap \(G_n\), insert \(I_n-I_{n-1}\) copies of
the gap 1. Then append \(G_n\) itself. This constructs one infinite
output, not separately chosen finite completions. The rule can inspect
\(G_n\) before inserting; no adaptedness claim is required.

Since \(h\) is increasing, (7) gives

\[
 0\le I_n\le1+\frac{h(n)+\max_{k\le n}|Z_k|}{c}=o(n).
 \tag{9}
\]

Thus the inserted symbols have zero asymptotic density.

## 3. All output clocks obey the pressure bound

After raw gap \(G_n\) has been appended, the output clock is
\(j_n=n+I_n\), its total gap is \(A_n+I_n\), and therefore

\[
 T_{j_n}=Z_n+cI_n\ge h(n)=3\log(n+1).
 \tag{10}
\]

Between the preceding raw endpoint and this one, inserted gap-1 symbols
only increase pressure. Before raw gap \(G_n\), their pressure is at least
the preceding endpoint value \(3\log n\). By (9), every output clock in
this block obeys \(j\le n+I_n\le2n\) eventually. Hence every late
output clock, including an interstitial insertion clock, satisfies

\[
 \chi_j\ge n^3\ge(j/2)^3.
 \tag{11}
\]

The first insertion, if present, increases pressure strictly. The first
raw endpoint has pressure at least \(3\log2>0\). Since raw gap 1 alone
does not reach that first barrier, there is at least one insertion in
the first block. Thus \(T_j>0\) for every \(j>0\). Equations (2) and
(11) now give \(S<\infty\) and \(R=\infty\).

## 4. All finite statistics and the critical first moment survive

For an arbitrary output prefix of length \(j\), let \(n=n(j)\) be the
number of raw gaps already completed, and let \(J=J(j)\) be the number
of inserted symbols already used. Then

\[
 j=n+J,\qquad 0\le J\le I_{n+1}=o(n).
 \tag{12}
\]

The number \(n(j)\) tends to infinity. Thus \(n/j\to1\) and \(J/j\to0\).
Deleting one inserted symbol affects at most \(r\) old and \(r-1\)
new contiguous occurrences of a fixed length-\(r\) word. Consequently
the absolute difference between its occurrence count in this output
prefix and its count in the first \(n\) raw symbols is at most
\((2r-1)J\). This is \(o(j)\). The simultaneous raw frequency statements
therefore prove property 1. Reversing the fixed finite word preserves
its iid product probability, so the corresponding reversed-block
empirical statistics have the same limit.

Finite-cylinder convergence does not by itself control an unbounded
coordinate. Here the mean follows instead from the exact identity

\[
 B_j=A_n+J.
 \tag{13}
\]

Equations (6) and (12) imply \(B_j/j\to\ell\), hence \(T_j/j\to0\).
As in (7), \(\max_{j\le N}|T_j|=o(N)\). For the bridge in (4),

\[
 V_N\le2\max_{j\le N}|T_j|+2|T_N|=o(N).
 \tag{14}
\]

This is the oscillation of the centered bridge. It is **not** a claim
of sublinear total variation.

## 5. The negative regulator

For GR-, put \(d=\log(4/3)>0\) and define

\[
 J_n=\max_{0\le k\le n}
 \max\left(0,\left\lceil\frac{h(k)+Z_k}{d}\right\rceil\right),
 \qquad J_0=0.
 \tag{15}
\]

Insert \(J_n-J_{n-1}\) copies of gap 2 immediately before \(G_n\).
Exactly as in (9), \(J_n=o(n)\). The output pressure at raw endpoints is

\[
 T_{n+J_n}=Z_n-dJ_n\le-3\log(n+1).
 \tag{16}
\]

Inserted twos decrease pressure. At every late clock in raw block \(n\),
it follows that \(\chi_j\le n^{-3}\le8j^{-3}\). If there are no
insertions in the first block, its raw endpoint is already strictly
negative by (16); otherwise the inserted twos start by decreasing it.
Thus every positive clock has negative pressure.

The frequency argument is unchanged. Its separate first-moment identity
is now \(B_j=A_n+2J\), so the critical mean and (14) still hold.
The two conclusions about (2) follow from the displayed cubic bound.

## 6. Nonatomic output, without assuming rational periodicity

The insertion map need not be invertible; its output is nevertheless
nonatomic. Each output coordinate depends on finitely many raw gaps, so
the output is a measurable random word. The same argument applies to either
sign. Fix one deterministic
output word \(b\), fix \(\delta>0\), and let
\(m_n=\lceil(1+\delta)n\rceil\). On the event that the output is \(b\)
and the insertion count after the first \(n\) raw symbols is at most
\(\delta n\), the raw \(n\)-prefix is a
subsequence of \(b_1,\ldots,b_{m_n}\). There are at most
\(\binom{m_n}{n}\) possible raw prefixes of this form, and each has
probability at most \(p^n\). Therefore

\[
 \Pr\{\text{output}=b\}
 \le \Pr\{I_n>\delta n\}+\binom{m_n}{n}p^n
 \tag{17}
\]

for GR+, with \(J_n\) in place of \(I_n\) for GR-.
The first term tends to zero by (9). The exponential rate of the second is

\[
 (1+\delta)\log(1+\delta)-\delta\log\delta+\log p.
 \tag{18}
\]

It is negative for sufficiently small \(\delta\). Explicitly, take
\(\delta=1/10\). Since \(\ell>3/2\), we have \(p<2/3\), and

\[
 e^{10((11/10)\log(11/10)-(1/10)\log(1/10))}(2/3)^{10}
 =\frac{11^{11}}{15^{10}}<1.
 \tag{19}
\]

Thus every individual output has probability zero.

Every positive gap word has the well-defined odd 2-adic code

\[
 X(b)=-\sum_{j\ge0}\frac{2^{B_j}}{3^{j+1}}\in\mathbb Z_2^\times.
 \tag{20}
\]

The series converges because \(B_j\ge j\). Its first summand is odd
and every later summand is even. Directly separating that first term gives

\[
 3X(b)+1=2^{b_1}X(\operatorname{shift}b).
 \tag{21}
\]

The tail code is odd, so the exact valuation in (21) is \(b_1\).
Decoding repeatedly recovers every gap; the map \(b\mapsto X(b)\) is
injective. Since \(\mathbb Q\cap\mathbb Z_2\) is countable and the
output law has no atoms, \(X(b)\) is irrational almost surely.
This argument does not assume that rational parity words are eventually
periodic.

For GR+, the same formal series (20) also converges over the reals to
the negative value \(-S(b)\). Its 2-adic value is irrational almost
surely. Convergence in both completions does not identify either value
with a positive ordinary integer. No real convergence of (20) is
claimed for GR-.

## 7. Exact finite ordinary realization, with its changing source

Every finite prefix \(b_1,\ldots,b_L\) still has positive ordinary
realizers. Let

\[
 C_L=\sum_{i=0}^{L-1}3^{L-1-i}2^{B_i},\qquad
 M=2^{B_L+1}.
\]

The unique odd residue class

\[
 n\equiv(2^{B_L}-C_L)(3^L)^{-1}\pmod M
 \tag{22}
\]

gives an odd final quotient \((3^Ln+C_L)/2^{B_L}\). The usual split
carry identity then shows that every intermediate quotient is odd and
each prescribed gap is its exact valuation. Positive representatives
give positive intermediate states. Each intermediate state is an affine
function of \(n\) with positive slope, so sufficiently large lifts put
all of them above any fixed floor. Distinct clocks have different slopes
(otherwise a nonzero power of two would equal a nonzero power of three),
so only finitely many lifts have a repeated state. Choose a larger lift
avoiding those finitely many exceptions if distinctness is required.

The sources in (22) can change with \(L\). For an irrational code in
(20), no single ordinary source realizes all prefixes. This is exactly
the distinction between the earlier finite controls in PR182 and the
new consistent infinite **nonordinary** control here.

## 8. What the literature can and cannot close here

Atkinson's 1976 recurrence theorem applies to an integrable cocycle over
an ergodic probability-preserving automorphism. Its recurrence conclusion
is almost everywhere for that invariant probability law. It is not a
recurrence theorem for every deterministic point having the law's finite
empirical block frequencies. The primary statement was inspected in the
article reproduced in Appendix A of the author's Warwick thesis.

PR180's stationary real-series theorem is respected. Its conditionally
critical stationary law has \(R=\infty\) almost surely. GR- is a different
output law, despite sharing every finite empirical frequency and the
critical mean. GR+ has \(R=\infty\) as well; its convergence assertion
concerns the reciprocal series \(S\). Applying a stationary theorem to
either selected output requires a new measure or orbit-specific argument.

Conditioned random-walk literature was considered as a possible way of
retaining a selected pressure minimum. No conditioned-walk theorem is
needed or imported in this proof. The new construction itself shows why
one must keep source arithmetic when trying that route.

The ordinary-source insertion note in this packet is the direct next
test: under a fixed integer source, making these symbolic edits into an
ordinary aligned trajectory incurs exact divisibility and a finite edit
budget. Neither that restriction nor the present countermodel proves
that every critical ordinary gap word is recurrent. **The missing step
is an ordinary-source rigidity statement for the actual infinite law.**

## 9. Reproduction and evidence level

`check_generic_ray_controls.py` uses integer comparisons to implement
(8) and (15) for supplied finite raw words. It checks every intermediate
pressure bound, minimal insertion at each new record, exact block-count
changes, both series orientations, and the ordinary realization (22).
It also contains deliberately damaged controls. The raw finite fixtures
are not claimed to be iid generic or to certify an asymptotic rate.

The all-time assertions, nonatomicity, and irrationality follow from
the written arguments above. They were independently reviewed at the
file hash recorded in the checkpoint review. `SOURCES.json` records
the frozen repository inputs and the primary literature access scope.
