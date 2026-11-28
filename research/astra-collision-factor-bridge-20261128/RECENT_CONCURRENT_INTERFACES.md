# Concurrent full-proof consumers and the stationary interface

Date: 2026-11-28. **Written integration of three concurrent Collatz
packets.** The source heads and complete files inspected by the coordinator
are recorded in the [intake](../../reports/astra-collision-factor-bridge-20261128/concurrent-source-intake.json).
No full Collatz proof is claimed in any of these inputs. Their external
analytic dependencies and local verification claims remain separate from
this pass's own kernel receipts.

## 1. The PR 218 signed first moment becomes one explicit stationary scalar

The complete [signed first-moment note in PR 218](https://github.com/GettysburgResearch/collatz/blob/aea80e35b6fc23cc909252a23e1ef5c945e1ca7e/research/astra-full-proof-20261128/descent/FIRST_MOMENT.md)
gives a source-qualified sufficient condition for full convergence. Put
\(N=2^k\), \(D=1-\tfrac12\log_2 3\), \(M=\lfloor k/D\rfloor\),
and choose an even \(g\) such that
\(\sqrt{k\log(k+2)}=o(g)\) and \(g=o(k)\). Define

\[
d(y)={\bf1}_{y\equiv3\ (4)}-{\bf1}_{y\equiv0\ (4)}.
\]

The native two-bit identity is
\(d(y)=b(y)+b(Ty)-1\), where \(b\) is parity. Thus the signed statistic

\[
F_k=\frac1g\sum_{0\le i<g/2}
\frac1N\sum_{n=1}^N d(T^{M+2i}n)
\tag{1}
\]

is the postcritical excess of odd departures divided by \(g\). PR 218
proves, with its named first-passage and positive-predecessor inputs,
that \(\liminf F_k\le0\) suffices for full Collatz. It does not prove
this signed upper bound. The following is an exact consumer of that
existing criterion using this pass's full-law stationary transfer.

For each clock \(h=M+2i\), take the fair jointly stationary real/ternary
path, retain its actual future grade \(A_h\), and set

\[
q=3^{A_h},\qquad r=Z_h\bmod q\in\{0,\ldots,q-1\},\qquad
L=q2^{-h}N.
\]

For \(j\in\{0,3\}\), choose the explicit simultaneous residue

\[
s_j=r+q\big((j-r)q^{-1}\bmod4\big)\in\{0,\ldots,4q-1\}.
\tag{2}
\]

The inverse exists because \(q\) is odd; in fact \(q^{-1}\equiv q\pmod4\).
Define the two interval counts and their signed difference by

\[
B_j=
\left\lfloor\frac{R_h+L-s_j}{4q}\right\rfloor
-\left\lfloor\frac{R_h-s_j}{4q}\right\rfloor,
\qquad \mathcal D_{h,N}=B_3-B_0.
\tag{3}
\]

These formulas count exactly the positive integers in the real interval
\((R_h,R_h+L]\) that satisfy the full ternary congruence and the indicated
residue modulo four. Positivity is automatic because \(R_h\ge0\).
They also cover grade zero. No sum over endpoint labels is left.

Let \(P_{h,N}\) be the true native endpoint law, and \(Q_{h,N}\) its
stationary-seeded version from
[the full-law theorem](factoring/STATIONARY_COLLISION_CONSUMER.md). The
exact fair word weight gives

\[
\sum_y d(y)Q_{h,N}(y)
=\frac{2^h}{N}\,\mathbb E\mathcal D_{h,N}.
\tag{4}
\]

Since \(d\) has range in \([-1,1]\), total variation gives

\[
\left|
\frac1N\sum_{n=1}^N d(T^h n)
-\frac{2^h}{N}\mathbb E\mathcal D_{h,N}
\right|\le 2\delta_N,
\qquad
\delta_N=\frac{\mathbb E\min(R_0,N)}N.
\tag{5}
\]

The bound is uniform in every clock, so averaging \(g/2\) terms and
dividing by \(g\) yields

\[
\boxed{
\left|F_k-
\frac1g\sum_{0\le i<g/2}
\frac{2^{M+2i}}N\,\mathbb E\mathcal D_{M+2i,N}
\right|\le\delta_N=O(\log N/N).}
\tag{6}
\]

Consequently the liminf-at-most-zero condition for the explicit signed
stationary expression in (6) is another exact consumer of PR 218's
full-convergence theorem. It is a transfer of that prior criterion, not
a new signed inequality.

At these clocks \(N\le2^h\). The full one-copy selector therefore
contains at most one endpoint. Hence \(\mathcal D\in\{-1,0,1\}\),
it vanishes when the selector rejects, and
\(\Pr(|\mathcal D|=1)\le N/2^h\). The necessary precision is on that
rare one-copy scale. Computing a few fixed Fourier coefficients, omitting
the same-path grade, or controlling a fixed ternary conductor would not
evaluate (6). A signed real/ternary trace estimate remains missing.

## 2. PR 220 already develops the sufficient semiprime family dynamically

The complete [factor-clock packet in PR 220](https://github.com/GettysburgResearch/collatz/blob/330dc8f7f1f7e970ad52b2835bf151cc71e44030/research/semiprime-factor-clocks-20261128/README.md)
is stacked on an earlier checkpoint of this pass. It studies exactly the
family in [SEMIPRIME_SUFFICIENCY.md](SEMIPRIME_SUFFICIENCY.md), with
\(n=pq\), \(p<q\), and \(\log n<p\le\log^2 n\).

Its larger-factor theorem has a clean arithmetic supply: for each eligible
small prime, the first \(O(\log\log X)\) parity word of prime multiples
is asymptotically fair after its forced first odd bit, by
Siegel--Walfisz on the relevant binary moduli. The additive correction
before crossing below \(q\) is at most the clock divided by \(3q\).
The resulting first-passage clock has Gaussian center
\(2\log p/\log(4/3)\) and width proportional to \(\sqrt{\log p}\).
This is a distributional theorem over the prime family, not a deadline
for every product.

That distinction is material. The same packet constructs long all-odd
prefixes within the family using primes in binary progressions, and
proves that every prescribed odd-start word occurs at the stated
exponential height. Its long ascending products refute a universal
\(O(\log p)\) larger-factor deadline. The finite witness and its prime
certification were reported by that packet; they were not rerun or
counted among this pass's Lean roots.

The smaller-factor passage result separately imports the actual
pair-fusion and minimum-clock laws, using a sparse upper transfer for
exceptional events. It shows high-probability descent below the slowly
growing factor near the global minimum clock. This is compatible with
a nonstandard component having a fixed minimum greater than one.

Thus this is genuine additional dynamical work on the sufficient family,
and it should be credited. Neither its early factor crossing nor our
existence of semiprime representatives proves convergence on that
family. The unresolved requirement remains a full dynamical closure,
or relative convergence density one in the sufficient family.

## 3. PR 219 keeps the native source in an affine rectangle estimate

The complete [native affine-rectangle note in PR 219](https://github.com/GettysburgResearch/collatz/blob/b1f2276c45218b0a05a6c4c0e413fec1e4e4dd46/research/astra-wild-nine-hour-20261128/outside/NATIVE_AFFINE_RECTANGLES.md)
combines a Subspace-Theorem lower bound and continued fractions. Its
discrepancy is subexponential in the clock, with a separate width/slope
term when the homogeneous multiplier is small. For actual sources, it
uses the exact identity

\[
2^hT^h(n)=3^{a_h(n)}n+A(n),\qquad
A(n)/2^h\equiv-3^{a_h(n)}n/2^h\pmod1.
\]

One can therefore bound concentration of the source's own fractional
carry by summing over only \(h+1\) grades, without summing over every
word or replacing the source by a newly chosen witness. This is a
useful protection against a severe counting loss beyond the binary
horizon.

The result has an explicit homogeneous floor on simple segments and
controls fractional carry arcs. The stationary selectors in (3) and in
the critical-grade theorem also retain the full ternary congruence and
the integer part of the real window. A lower bound for their diagonal
intersection does not follow from fractional-carry anti-concentration.
The PR itself states that missing consumer, including the cost of
unbounded target-dependent arc families. We do not supply it here.

## 4. What is connected and what remains open

The current concrete consumers are now compatible across the concurrent
packets: a one-copy negative critical grade tail, a one-copy signed
postcritical residue flux, and the original two-copy collision. Their
stationary formulas have no enumeration over endpoint labels. The
semiprime family has both unconditional sparse supply and independent
factor-passage analysis. The affine-rectangle estimate controls the
actual selected source, while the factoring evaluators supply specific
coefficient and Fourier operations.

The missing step is still an arithmetic estimate on the full growing
conductor and its joint real window, or a convergence theorem on the
sufficient semiprimes. This note supplies explicit interfaces and
priority, without replacing those estimates by generic stationarity,
finite experiments, or weak marginal laws.
