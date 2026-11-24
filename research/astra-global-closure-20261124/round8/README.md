# Ordinary descent and the arithmetic cost of positive witnesses

**Collatz remains OPEN.** Round eight constructs a whole strictly contracting
subprogression inside every prescribed ternary unit class, proves a stronger
arithmetic restriction on positive witnesses of a fixed source, and obtains
large actual paired families on the two components of their supplied source.
The first two results are independent of the recent analytic manuscripts.
The stronger paired abundance statements retain those manuscripts as named
inputs.

Three GPT-6.2 Astra streams developed the work, with cross-reviews and an
independent coordinator reconstruction. The baseline is the published
round-seven commit 0e8a7f9f965416189b30b57b8aa818fbcb7757c7.
[Repository intake](../../../reports/astra-global-closure-20261124/round8/INTAKE.md)
and the [source ledger](SOURCES.json) distinguish new results, prior work,
late concurrent improvements, and external hypotheses.

Throughout, \(T(2n)=n\), \(T(2n+1)=3n+2\), and \(C\) is the positive
ordinary basin of 1. A unit is a positive odd integer prime to three.
A forward failure has \(u\in C,\ 3u\notin C\); a reverse failure has the
opposite labels. Round seven proves that excluding either kind on all
units would settle Collatz.

## 1. A full contracting progression in every ternary cell

For every positive \(q\) prime to three and every \(p\ge0\), there are
\[
 0\le t<3^{5p+13},\qquad A\le4p
\]
such that **every** member
\[
              Q=q+3^p(t+3^{5p+13}l),\qquad l\ge0,
\]
has a positive ordinary predecessor \(z\) satisfying
\[
                    T^{5p+13+A}z=Q,\qquad 171z<Q.
\]
The theorem includes the existence of the subprogression and physical
legality for all its ordinary members. It is proved in Lean as
RayGrade.every_cell.

Applied to the bad arm of a directed unit failure on the selected
subprogression, the construction and round seven's bounded directed paths
yield a failure of the same orientation
below \(u/5\) in the forward case, and below \(u/8\) in the reverse case.
Successive selection gives a subprogression with both implications, and
any prescribed odd binary class can be retained. Applegate and Lagarias's
published inverse-path certificate gives a sufficient ternary precision of
at most \(p+\lceil5p/6\rceil+65\) for \(p\ge1\), improving the asymptotic
coefficient. That sharpening uses their external computer
certificate; the elementary precision \(6p+13\) is independent of it.

The lane also proves a uniform cost for all smaller representatives meeting
an initial all-odd excursion. If \(q+1\) is divisible by \(2^i\),
\(0<z<q\), and \(T^h z=T^i q\), then
\[
             h>i,\qquad P_h(z)>i+v_3(q-1)\quad(q>1).
\]
The lower clock \(h\) is unrestricted. Explicit Mersenne exponent
progressions pay this growing odd-step cost. For every exact ternary grade
\(s\ge2\), they give a progression on which a forward failure at \(u\)
forces another below \(u/18\).

The coverage quantifier is essential: every coarse cell has a contracting
subcell, but a specified failing integer can miss that subcell. In this
construction \(z\ge2^r-1\), so a fixed target satisfying \(171z<Q\) permits
only finitely much final all-odd precision. No indefinitely repeated
contraction for every original input has been proved.

[Proof and exact quantifiers](unit/README.md) ·
[Lean](unit/RayGrade.lean) ·
[Ordinary replay](unit/check.py)

## 2. Long repeated suffixes force a large part outside every fixed prime set

Fix one positive ordinary \(n\). Let \(x_k=T^k n\), and let \(p_k\) count
the odd inputs of this actual prefix. A positive lift
\[
                  m_k=n+2^k t_k
\]
follows the same \(k\) branches to \(x_k+3^{p_k}t_k\).
Suppose its subsequent physical word ends at 1 and is a concatenation
of a bounded number of powers of words whose root lengths sum to \(o(k)\).
The roots may change, and their repetition counts and the total suffix
duration may be arbitrarily large.

For every fixed finite prime set \(S\supseteq\{2,3\}\), every sequence of
lifts \(m_k\ne n\) at depths tending to infinity must satisfy
\[
                  \frac{\log (t_k)_{S'}}{k}\longrightarrow\infty.
\]
Here \((t_k)_{S'}\) removes all prime powers supported in \(S\) and
retains every multiplicity at the other primes. Thus even arbitrarily
large displacement supported in a fixed set of primes cannot pay for
these suffixes at deep prefixes of a fixed ordinary source.

The general theorem allows a bounded signed \(2,3\)-power presentation of
the entire suffix carry, with atoms \(d_j2^{u_j}3^{v_j}\), nonnegative
integer exponents, coefficients of height \(\exp(o(k))\), and
\(v_j\le h_k+o(k)\), where \(h_k\) is the suffix odd count. It also allows
a moving target \(r_k\), provided
\(x_k r_k/3^{p_k}\le e^{-\delta k}\) for a fixed \(\delta>0\).
The proof uses Evertse's published theorem on primitive nondegenerate
integer zero sums. After pruning zero subsums on the right-hand side and
dividing by the complete common content, it proves the opposing estimate
\[
       \frac{\text{product of all outside-}S\text{ parts}}
            {\text{maximum primitive coordinate}}
                   \le e^{-\delta k/2}.
\]
No squarefree replacement, algebraicity hypothesis on an unknown companion,
or bounded-duration assumption is used. The exact full-divisor step,
physical affine identities, repeated-word identity, and signed pruning are
proved in Lean. Evertse's theorem and the asymptotic conclusion remain
written mathematics.

This suffix language is actually realizable: for every prescribed positive
source, depth \(k\), and \(d\ge1\), an explicit positive lift has a
first-hit suffix \(1^d0^j\). Taking \(d=k\) gives unbounded odd count
with two fixed roots. The theorem proves that every such construction
pays the large displacement cost. It does not construct a small witness
for an unresolved original integer.

The latest PR192 already proves the full-displacement bound for bounded
odd tails, including its power-of-two consequence and a moving-target
extension. Those statements are credited as prior work.

[Full proof and comparison](arithmetic/README.md) ·
[Lean](arithmetic/SparseTerminal.lean) ·
[Independent review](../../../reports/astra-global-closure-20261124/round8/unit/ARITHMETIC_REVIEW.md)

## 3. Actual paired families with smaller and larger ordinary members

There are two different clock regimes.

At the native clock \(h\), on any aligned block of \(N=2^h\) ordinary
sources, set
\[
   J=\max(P_h(x),1+P_h(3x)),\qquad G_J=N/3^J.
\]
Apart from \(O_w(N/h^w)\) sources, each odd unit \(x\) has at least
\(\lfloor G_J/h^{3w+8}\rfloor\) units on each strict side, sharing its
ternary residue and all four entries
\[
                  (P_h(x),T^h x,P_h(3x),T^h(3x)).
\]
Every partner lies within \(G_Jh^{3w+8}\). This estimate is unconditional.
It uses the shared real source coordinate to count joint endpoints; it
does not assume independence of the two arms.

Under the named trajectory input H, a later pair of actual landing clocks
gives a stronger local statement. With \(O_w(X/(\log X)^w)\) exceptions
on each octave, one record of two small endpoints, clocks, and odd counts
serves each retained source simultaneously at every aligned dyadic
subinterval scale. On an interval of length \(L\), it has
\(\lfloor L/(\log X)^{B(w)}\rfloor\) partners on each strict side.
At the octave scale this is \(X/(\log X)^{O_w(1)}\); at a suitable
polylogarithmic interval scale it gives a strictly smaller nearby unit.
All partners remain in the same two ordered ordinary components as
the supplied pair.

Under F as well, every fixed component has positive lower ordinary
density by PR203's fixed-target depth bank. For any cut separating two
distinct ordinary components, the ordinary cut reductions then force
infinite reciprocal mass of retained discordant edges.
The late PR201 directed covers improve this statement: either chosen
unit residue modulo six, in either direction, supports arbitrarily large
finite flows between any two specified distinct components, with capacities
\(1/x\), on every tail. The graph is defined by actual all-time components;
this is an existence statement, not an algorithm deciding those components.
No opposing bound on that flow is known.

An independent exact identity gives a further guarded descent. If both
\(r,3r\) reach the \(1,2\) cycle by clock \(h\), then for \(t>0\),
\[
 r+2^{h+2}t\longmapsto r+3\cdot2^h t
\]
strictly decreases the source while preserving both ordered components.
The two arms may have different phases and odd counts. Its finite
iteration eventually leaves this anchor's congruence; no cover of every
exceptional source by suitable anchors has been obtained.

[Paired landing and cut proof](paired/README.md) ·
[Native profiles and anchor descent](paired/PAIRED_PREFIX.md) ·
[Late directed-cover improvement](paired/LATE_PR201.md) ·
[Lean](paired/PairedProfiles.lean)

## 4. Abundant short completions have a necessary description cost

The two main streams can be joined at the same fixed ordinary source.
Under F, for every fixed \(n>0\) and every sufficiently large \(k\),
there are exponentially many distinct
\[
 m\equiv n\pmod{2^k},\qquad m\equiv n\pmod3,\qquad
                    2^{Dk}\le m<2^{Dk+1},
\]
for an absolute constant \(D\), such that both \(m\) and \(3m\)
reach 1 in \(O(k)\) steps. They preserve the first \(k\) actual
parities of \(n\) and \(3n\) respectively, and their two arms merge
by clock \(40(k+1)\).

For every fixed number of repeated blocks, the arithmetic theorem forces
a positive linear lower bound on the sum of their root lengths on both
stopping continuations. The bound is uniform over all these sufficiently
late witnesses, with a constant depending on the fixed source and block
budget. Its proof is ineffective through Evertse's theorem.

This supplies actual short positive completions of each finite prefix
and identifies a necessary cost of describing them. Those completions
are other integers. For a hypothetical failing source, they have changed
its nonconvergent component.

[Construction and proof](paired/CROSS_ROUTE.md)

## 5. Why the least ordinary failure is still unserved

A least directed failure forces the odd fraction on its bad arm to be
at least
\[
          \log_3 2-O(1/h+1/u).
\]
This is above the half-odd regime used for native typical profiles.
At the critical grade \(p=\lceil h\log_3 2\rceil\), an elementary
rotation and carry argument gives at least
\[
                         \frac{\binom hp}{h(1+h/2)}
\]
distinct exact endpoint profiles even among words whose designated arm
never falls below its start during the entire prefix. Their exponential
rate is \(H_2(\log_3 2)\), about \(0.949955527\).
This is a finite-horizon count, not evidence for an infinite counterexample.
It prevents an unjustified extrapolation of the near-half profile estimate.

The late PR193, conditional on PR146's symbolic absorption estimate, gives
repeated smaller ordered representatives for most ordinary sources, with
prescribed low bits and ternary residue choices. It composes with the
ternary contracting subcells. A sufficiently large least failure, however,
violates the required odd-count gate at every native first-stage checkpoint,
so this construction does not start at that prescribed source.
The late PR201 gives an exact-clock finite-row criterion covering escape
and nontrivial cycles. Its required upper bound is unproved, and its
explicit two-gap amplified sources do not approach a fixed positive
source to increasing binary precision. These are precise remaining
interfaces, not missing formalization of a complete proof.

[Critical profiles](unit/CRITICAL_PROFILES.md) ·
[Late PR193 review](../../../reports/astra-global-closure-20261124/round8/unit/LATE_PR193_REVIEW.md) ·
[Late PR201 review](../../../reports/astra-global-closure-20261124/round8/arithmetic/LATE_PR201_REVIEW.md)

## 6. Executed evidence

| Module | Selected axiom reports | Formal scope |
|---|---:|---|
| RayGrade | 11 | All-clock grade barriers, legal inverse lifting, and the every-cell ordinary descent theorem |
| SparseTerminal | 12 | Physical prefix and suffix rows, signed pruning, repeated blocks, and complete-divisor identities |
| PairedProfiles | 8 | Ordinary binary lifts, simultaneous anchor contraction, and the joint real-profile estimate |

All three were rebuilt from source into an empty project output cache,
with Lean 4.34.1 and warnings as errors. The 31 selected inventories
contain only propext, Classical.choice, and Quot.sound. Existing Mathlib
and package objects were reused at the recorded revision.

Four finite scripts passed in normal and optimized Python, giving eight
canonical-output matches with active explicit guards. Separately, the
late PR201 affine covers were replayed in both Python modes: all
2,211 whole-progression leaves and 84,642 path letters passed. That
isolated upstream replay is not a complete upstream checkout or Lean
rebuild.

[Lean receipt](../../../reports/astra-global-closure-20261124/round8/lean/receipt.json) ·
[Finite replay](../../../reports/astra-global-closure-20261124/round8/CONTROL_REPLAY.json) ·
[Upstream cover replay](../../../reports/astra-global-closure-20261124/round8/UPSTREAM_COVERS.json) ·
[Coordinator review](../../../reports/astra-global-closure-20261124/round8/ROOT_REVIEW.md)

The closing obligation is to serve every supplied ordinary failure, or
to contradict the remaining directed cut mass or exact-row statistic.
The subprogressions, exceptional-set estimates, and arithmetic cost
theorem do not yet supply that implication.
