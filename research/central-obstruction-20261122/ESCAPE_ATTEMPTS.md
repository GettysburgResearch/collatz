# Direct attempt to eliminate the last-contact escape measure

Date: 2026-11-22. **Outcome: no proof that eta is zero was obtained.**
This is an attempt record, not a new closing theorem. Its purpose is to
record the first missing arithmetic step in two direct attacks, so that
the proposed steps are not inadvertently promoted to established facts.

The target is the actual last-contact measure from PR176:

\[
\eta(x)=\nu(x)1_\Lambda(x),\qquad
\|\eta\|_1=\sum_{\mathcal C\text{ escaping}}C_{\mathcal C}\le A.
\]

The baseline PR185 is `53f01ca5b443ef57ef2160b4996dbb2cc87f7395`.
The newer source packets inspected here are PR175
`728389c2ad4796853948250a90188b0697483d92`, PR176
`31c4a880ea4acf6eec4783e68bfc75e2cf8e7fe6`, and PR180
`ab3973099f0d285bbe88972382ad599bb02cd460`, as exported in the
parent task's `central_sources` directory. The existing ordinary harmonic construction,
its source qualifications, and the exclusion of periodic states remain in
force. No new Lean axiom or asserted analytic premise is introduced.

## 1. Attempt: use the actual inverse height law to erase a retained atom

The recent Valbuena source advertises an actual-inverse-path law of large
numbers: from every fixed positive odd nonperiodic root prime to three,

\[
\frac{\log Y_k}{k}\longrightarrow a:=\log(4/3)
\quad\text{almost surely}.
\tag{1}
\]

The source describes a transfer of the source clock through fixed finite
prefixes, and explicitly distinguishes (1) from a uniform expected
occupation bound. This attempt gives (1) its full stated fixed-root
strength. It does not claim to reverify the source theorem or identify
its reference with the repository's `nu` merely from the overview.
For the proposed closure test below, grant the favorable version of (1)
for `K_nu`. If (1) is identified with the critical `K_G` law, the
repository's bounded mutual absolute continuity of the full inverse
path laws transfers its almost-sure assertion to `K_nu`. Even with this
favorable grant the attempted conclusion fails at (4).

Suppose an actual escaping source is `p`, and put `q_i=U^i(p)`.
The ordinary inverse kernel is

\[
K_\nu(q,n)=1_{U(n)=q}\nu(n)/\nu(q).
\]

The probability, starting at `q_i`, of taking the particular reversed
physical segment back to the **same original source** `p` is exactly

\[
\mathbb P^\nu_{q_i}(Y_j=q_{i-j}\text{ for }0\le j\le i)
=\prod_{j=1}^{i}\frac{\nu(q_{j-1})}{\nu(q_j)}
=\frac{\nu(p)}{\nu(q_i)}
\longrightarrow\frac{\nu(p)}{C_{\mathcal C}}>0.
\tag{2}
\]

Since `q_i` tends to infinity, `q_i>p` eventually. On the event in (2),

\[
\frac{\log Y_i-\log q_i}{i}
=\frac{\log p-\log q_i}{i}<0.
\tag{3}
\]

Thus an escape atom has a uniformly positive probability of a long
inverse segment with negative height displacement, when the root is
chosen to be the corresponding forward endpoint.

**The first unjustified line would be**

\[
\sup_{q\in N}
\mathbb P^\nu_q\!\left(
\log Y_k-\log q\le\tfrac12ak\right)\longrightarrow0.
\tag{4 — NOT PROVED}
\]

The fixed-root law (1) does not give (4). Equation (2) shows exactly the
original mass that a proof of (4), or an adequate restriction of it to
the moving roots, would have to eliminate. Neither the finite last-contact
mass nor its atomic limiting contact-source law supplies the required
uniformity: the time before that contact increases with `i`.

### An explicit countermodel to this LLN upgrade

This model is **not the Collatz map**. It isolates the precise invalid
probability-theory inference in (1) to (4), even in a countable ordinary
integer state space with a bounded positive harmonic reference.

Write `r=4/3` and label a two-sided path by distinct positive odd ternary units

\[
x_j=\begin{cases}
12\lceil10r^j\rceil+1,&j\ge0,\\
12\lceil10r^{-j}\rceil+5,&j<0.
\end{cases}
\]

Within either half, successive unrounded arguments differ by at least
`10/3`, so the labels are distinct. The halves have different residues
modulo twelve. Define `V(x_j)=x_(j+1)` on this countable state space and set
`nu(x_j)=1`. Ordinary inverse transport has one parent at every state and
preserves `nu`. Its inverse path from `x_j` is deterministic:
`Y_k=x_(j-k)`. For every fixed `j`,

\[
\lim_{k\to\infty}\frac{\log Y_k}{k}=\log r=a.
\]

Nevertheless, starting at `x_i` gives `Y_i=x_0`, with probability one,
so the event in (4) has probability one for that moving root and clock.
The finite original source `eta=delta_(x_0)` also has
`sum_(k>=0) L^k eta=1_{j>=0}` and escapes forward. If contacts are chosen
to be `{x_j:j<=0}`, every inverse path reaches contact, `x_0` is the
unique last contact, and the moving-root contact-source law is the same
fixed atom. The model is not asserted to satisfy the repository's
canonical-obstacle arithmetic bounds; none is needed to falsify the LLN
uniformization itself.

## 2. Attempt: force regularity of the canonical invariant label by adjacent coalescence

Let `J` be the canonical escape label, extended to every positive integer
as in PR182. Then `0<=J<1` and `J(Tn)=J(n)`. In particular

\[
J(2n)=J(n),\qquad J(3n+1)=J(n)\quad(n\text{ odd}).
\tag{5}
\]

Actual counted fusion of the trajectories from `n` and `n+1` implies
`J(n)=J(n+1)`. Therefore the adjacent-coalescence theorem supplies a real
arithmetic estimate for this very label, rather than for an unrelated
test function:

\[
\frac1X\sum_{n\le X}|J(n+1)-J(n)|\longrightarrow0.
\tag{6}
\]

When the published square-root fusion tail and its exact binary-cylinder
transport are retained, a finite clock `k` gives an upper bound of the
form

\[
\frac1X\sum_{n\le X}|J(n+1)-J(n)|
\le C(k+1)^{-1/2}+O(2^k/X).
\tag{7}
\]

Here the counting error follows because the counted-fusion predicate
through shortcut time `k` is periodic modulo `2^k`: on each binary
cylinder both affine branch coefficients and odd counts are fixed.
Taking `k=floor((log_2 X)/2)` yields the corresponding
`O((log X)^(-1/2))` mean bound. The rate retains the external coalescence
source as an input; the qualitative version (6) is enough to locate
the gap below.

For every fixed positive integer shift `d`, telescoping gives mean
`|J(n+d)-J(n)| -> 0`. Combining (5) with the mean shift estimate gives
approximate multiplication-by-three invariance on odd inputs. These are
actual consequences of the proposed route.

**The first unjustified line would be:** these local mean estimates give
ordinary Besicovitch approximation of `J` by finite polynomial-phase
sums, or a uniform modulus of continuity at a positive fraction of the
source height. No such implication has been obtained. The growing-block
synchronization estimate inspected in the literature has the form
`C(1+log D)^4/sqrt(k+1)`; with an ordinary source clock `k=O(log X)`,
it only controls a subpower block scale, not a macroscopic fraction of
`X`.

Two exact checks show what cannot be substituted for that missing step.

1. **An actual ordinary fixed-source exception to pointwise counted
   fusion.** The shortcut trajectories of `3` and `4` never synchronize:
   after `3 -> 5 -> 8 -> 4 -> 2 -> 1`, the two trajectories occupy the
   two states of the `1 <-> 2` cycle in opposite phases. Thus a
   density-one counted-fusion theorem cannot be applied to an arbitrarily
   selected fixed source. This is not a component mismatch: both sources
   reach one. It tests only the invalid pointwise upgrade of the fusion
   theorem.

2. **Local mean variation and exact doubling alone do not give the
   requested regularity.** Define
   `B(n)=1_{n/2^floor(log_2 n)<3/2}`. Then `B(2n)=B(n)` and its adjacent
   variation through `X` is `O(log X)`. But its ordinary means approach
   `1/2` along complete dyadic intervals and `2/3` at the half-interval
   endpoints. They do not converge. Hence `B` is not in the ordinary
   Besicovitch closure of finite polynomial-phase sums, whose ordinary
   means do converge. This example does not claim the extra Collatz
   invariance in (5); it prevents dropping that arithmetic condition from
   the attempted regularity transfer.

There is also no spectral-gap shortcut from irrational-rotation
ergodicity. For `alpha=log_2 3`, choose distinct integers `m_j` with
`||m_j alpha|| -> 0` and put
`f_j(x)=1_{{m_j x}<1/2}` on the circle. Then

\[
\|f_j(\cdot+\alpha)-f_j\|_1
\le2\|m_j\alpha\|\longrightarrow0,
\qquad\|f_j-1/2\|_1=1/2.
\]

Ergodicity forces an exactly invariant single function to be constant;
it gives no uniform compactness for these approximately invariant
functions. This is the uniformity the proposed mantissa-scale argument
would need, rather than a substitute proof of it.

## 3. What this attempt actually establishes

No estimate obtained here makes `eta` smaller, proves a strictly
subcritical bound for its atoms, or eliminates an escaping component.
Equations (2)--(3) locate the surviving fixed-source probability in the
inverse-clock attack. Equations (5)--(7) are the genuine arithmetic
information available in the coalescence attack, but they do not close
its scale-uniform regularity step. These are failed closure attempts,
not additional progress toward the theorem being counted as proved.

The newly inspected upstream notes already retain the same mass:
`SPARSE_BOUNDARY_MASS.md` exhibits a linear weighted contribution from
one original escaping source, and `LITERATURE_DIRICHLET_BOUNDARY.md`
identifies the positive coefficient `sum_C D_C^2/C_C` in the sharp
Cesaro-energy rate. Neither estimate was relabeled as a no-escape result.

## Literature consulted for the attempted extra inputs

- Lucas Valbuena, repository overview of *Collatz basin densities and
  canonical traces from first-passage stabilization*:
  https://github.com/x1xhlol/collatz-two-coordinate-obstruction/blob/main/README.md
  (fixed-root inverse height law and explicit open raw occupation upper
  bound).
- Omar Javier Said Duran, *Consecutive integers coalesce with density one
  under the Collatz map*, version 1, September 27, 2026:
  https://doi.org/10.5281/zenodo.23003524 . The actual theorem was inspected
  through the downstream primary-source exposition below, not independently
  rebuilt here.
- *Square-root coalescence tails: proof discussion and corrected
  attribution*, including its explicit source ledger:
  https://rstation.ai/r/collatz/posts/20 .
- *Synchronization of growing Collatz blocks and selected references*:
  https://rstation.ai/problems/collatz/papers/124 .
- *Microscopic occupation from smooth Syracuse passage laws*:
  https://rstation.ai/problems/collatz/papers/18 . Its occupation is before
  first entry below the specified band floor, and the source-density
  limit precedes the band limit. It does not bound post-minimum escape
  occupation or supply the uniformity in (4).
