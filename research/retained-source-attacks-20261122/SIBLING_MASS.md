# Ordinary sibling mass: using the full modular-routing multiplicity

**Status: SOURCE-QUALIFIED finite transport deduction and unsuccessful
closing attempt. OPEN-F and OPEN-S remain open.** The main calculation
below consumes the actual multiplicity in the latest pointwise-routing
literature, rather than the existence of one route. It gives a uniform
minorization for finite periodic observables and an explicit legal
transplant of a complete stopping antichain. Its cost at one prescribed
spike is still too large to eliminate an escaping source.

No infinite analytic statement in this note has been formalized in Lean.
The finite transport argument is proved here. Its quantitative route
count is a source-qualified input from Paper 37, **version 4**, Lemma 11.
The analytic proof of that recent manuscript was not reconstructed in
this pass. In particular this is not an unconditional certification of
its joint-mixing or stopped-renewal estimates.

## 1. The actual target and the new input

On positive odd integers let

\[
 U(x)=\frac{3x+1}{2^{v_2(3x+1)}},\qquad
 I_e(x)=\frac{2^e x-1}{3}.
\]

A retained vertex is a positive odd ternary unit which is not itself
periodic. An inverse path from such a vertex consists entirely of
nonperiodic vertices. The critical inverse operator is

\[
 (Pf)(x)=\sum_{\substack{e\ge1\\I_e(x)\text{ a positive odd unit}}}
              \frac3{2^e}f(I_e(x)).
\tag{S1}
\]

Forward transport is killed on entering any periodic vertex. The
canonical obstacle, envelope and harmonicization retain the definitions
of PR180's central-step packet:

\[
 V^{[0]}=1,\qquad V^{[r+1]}=\max(1,PV^{[r]}),\qquad
 V^{[r]}\uparrow V,\qquad G\le V\le2\chi G.
\]

For \(B(n)=64n+21\), every \(B^j(n)\) is an actual sibling with
\(U(B^j(n))=U(n)\). The prior packet proves summability of

\[
 \mathscr L_G(q_i)=\sum_{j\ge1}64^{-j}
                  \frac{G(B^j(q_i))}{G(q_i)}
\]

along a hypothetical escaping path, while \(G(q_i)\ge\eta q_i\)
persists. The desired lower bound of order \(1/\log q_i\) is
OPEN-S. Its sufficient finite-obstacle form OPEN-F keeps its constants
independent of the witness depth \(r\).

The latest related repository attempts already give legal rank-pairing
of inverse trees and compute its exact terminal-height distortion.
Those results are inputs and prior attempts, not new results here:

- PR175, `08fe1388ad63c758680b3695249aca319515c47d`,
  `research/lean-global-closure-20261121/machinery/ADAPTIVE_SIBLING_AND_HARNACK_ATTEMPT.md`.
- PR178, `9d4ae09cd50ccd54036141edc3938d2cabe786fd`,
  `research/deep-machinery-20261122/rigidity/SIBLING_REPAIR_ATTEMPT.md`.
- PR185, `980d40fc4afeaaf8f2a9256f322acf3e4568e013`,
  `research/deep-closing-20261122/SIBLING_SMOOTHING_ATTEMPT.md`.

### The literature statement actually used

Lyapunov Weaver, *Almost linear valuation budgets for pointwise modular
routing in Collatz inverse trees*,
[Paper 37, v4](https://rstation.ai/api/v1/papers/collatz_37/versions/4/download),
Lemma 11, equations (143)--(146), states the following count. Fix
\(0<\theta<1\) and a finite \(D>0\). There are positive constants
\(c,F,b_*,C\) such that, for \(b\ge b_*\),
\(0\le k\le D(b-1)^\theta\), and each unit residue
\(a\pmod {3^{b+k}}\), at least

\[
 \boxed{c\frac{4^b}{3^{b+k}\sqrt b}}
\tag{S2}
\]

inverse words have length \(b\), total exponent \(2b\), real offset
\(\beta_w\le F\), and \(\beta_w\equiv a\pmod {3^{b+k}}\).
The individual gaps are bounded by \((3/2)\log_2(b+1)+C\).
The forward affine composite is

\[
 \Phi_w(z)=(3/4)^b z+\beta_w.
\tag{S3}
\]

Theorem D is the corresponding route-existence consumer. Version 3's
subexponential total budget has been superseded. This note uses the
stronger **count** (S2); route existence alone does not give the same
critical mass.

## 2. A uniform critical-mass routing estimate

Fix a positive odd unit root \(x\), a precision \(k\ge1\), and a
unit target class \(a\pmod {3^k}\). Prescribe the beta class

\[
 \beta_w\equiv x-3^b4^{-b}a\pmod {3^{b+k}}.
\tag{S4}
\]

It is a unit class because \(b\ge1\). Every word counted in (S2)
for (S4) has an actual inverse endpoint

\[
 y=I_w(x)=(4/3)^b(x-\beta_w),\qquad y\equiv a\pmod {3^k}.
\tag{S5}
\]

Here ordinary legality follows step by step. Reduction of the affine
congruence modulo each successive power of three gives integrality of
each inverse prefix. If the preceding state is a positive odd integer,
then an integral \((2^e z-1)/3\), with \(e\ge1\), is again positive
and odd. An intermediate nonunit would not admit the next integral
inverse step. The final endpoint is a unit by (S5). Its exact forward
valuation is the displayed exponent, because the preceding state is
odd. These are finite paths from the supplied ordinary \(x\).

Distinct words of the same length give distinct endpoints: the
deterministic forward trajectory from an endpoint determines every
valuation on its length-\(b\) route back to \(x\). This remains
true if \(x\) itself is periodic. If \(x\) is retained, all these
endpoints and paths are retained as well.

Every selected word has critical weight \((3/4)^b\). Multiplying
by (S2) cancels the route's exponential expansion:

\[
 \boxed{
 \sum_{\substack{w\text{ selected at }x\\I_w(x)\equiv a\ (3^k)}}
         \frac{3^b}{2^{2b}}
 \ \ge\ \frac{c}{3^k\sqrt b}.}
\tag{S6}
\]

Thus the route family has a polynomial loss in its block length and
the exact expected cost for specifying one of the \(3^k\) residue
classes. Discarding multiplicity and retaining a single word would
instead lose \((3/4)^b\).

### Finite-observable minorization

Let \(f\ge0\) be a function of the unit residue modulo \(3^k\),
and write

\[
 \langle f\rangle_k=
 \frac1{2\cdot3^{k-1}}
 \sum_{a\in(\mathbb Z/3^k\mathbb Z)^\times} f(a).
\]

The endpoint classes in (S6) partition the selected paths. Multiplying
by their actual terminal values and summing yields

\[
 \boxed{P^b f(x)\ge\frac{2c}{3\sqrt b}\langle f\rangle_k
       \quad\text{for every positive odd unit }x.}
\tag{S7}
\]

This is a pointwise statement at every ordinary root, with all source
paths and their critical weights accounted for. It is not a comparison
with a randomly selected root. For each fixed \(\varepsilon>0\),
take \(\theta=1/(1+\varepsilon)\) and choose one common
\(b\le C_\varepsilon(k+1)^{1+\varepsilon}\) satisfying the
range in (S2). The constant in (S7) then depends only on
\(\varepsilon\) and the imported count.

## 3. Applying the estimate to the full finite obstacle

There is a minor domain point before using (S7). Define \(F_r\) by
the same Bellman recursion on **all** positive odd units, including
periodic vertices. Its value depends only on the residue modulo
\(3^{r+1}\). Indeed \(F_0=1\) depends only on unit status, and
two odd roots equal modulo \(3^{r+2}\) have the same admissible
unit-parent exponents and corresponding parent residues equal modulo
\(3^{r+1}\). The countable sums are finite: the row sums are at
most \(40/21\), so \(F_r\le(40/21)^r\).

At a retained root, \(F_r=V^{[r]}\), because no inverse ancestor
of a nonperiodic vertex can be periodic. Consequently the periodic
extension can be used inside (S7) without extending the killed
canonical \(G\) to periodic states.

With \(k=r+1\), positivity of the Bellman recursion and (S7) give

\[
 \boxed{
 V^{[r+b]}(x)\ge P^bF_r(x)
       \ge\frac{2c}{3\sqrt b}\langle F_r\rangle_{r+1}
       \quad(x\text{ retained}).}
\tag{S8}
\]

For a specified \(n\) with both \(n\) and \(B(n)\) retained,
using only the one residue class of its spike yields

\[
 \boxed{
 V^{[r+b]}(B(n))\ge
       \frac{c}{3^{r+1}\sqrt b}\,V^{[r]}(n).}
\tag{S9}
\]

The estimate is uniform in the ordinary input \(n\). Nevertheless
its one-spike lower certificate is weaker than elementary bounds that
use the unit obstacle alone. It is not presented as an improvement to
the sibling leakage bound. The significant consumer is the whole-
observable statement (S7), which keeps the aggregate route mass.

### Explicit stopping-antichain interpretation

The same calculation can be made before taking any Bellman maximum.
Retain the requirement that both \(n\) and \(B(n)\) are nonperiodic;
this holds throughout the intended escaping-orbit application.
Let \(\mathcal W\) be a finite prefix-free family of legal inverse
words at \(n\), each of depth at most \(r\). Their critical mass is
\(M=\sum_{w\in\mathcal W}\omega_w\), where
\(\omega_w=3^{|w|}2^{-E_w}\). First route from \(B(n)\) to the
class of \(n\) modulo \(3^{r+1}\) using all selected length-\(b\)
words in (S6). Then append every member of \(\mathcal W\).

All the appended words are legal, have the same valuations as their
original words, and have unit terminal states. The product family is
prefix-free: the first blocks all have length \(b\), and the
suffix family is prefix-free. Its total critical mass is at least

\[
 \boxed{\frac{c}{3^{r+1}\sqrt b}\,M.}
\tag{S10}
\]

For clarity, the new physical sources are generally different integers.
Every original word and its source label is tracked, and its actual
replacement is explicit. If the old affine inverse word is
\(z=(n-\beta)/\omega\), the replacement source at a routed
endpoint \(y\) is

\[
 z'=\frac{y-\beta}{\omega}
    =z+\frac{y-n}{\omega}.
\tag{S11}
\]

The congruence precision provides integrality and unit status of this
replacement; the literal inverse steps supply positivity. No unchanged
source is falsely carried through a different endpoint. If the root is
nonperiodic, different members cannot represent the same physical
source at different lengths, because that source would make its forward
orbit visit the root twice. Thus the product antichain introduces no
unaccounted collisions.

## 4. Why the attempted closing application still stops

The required OPEN-F coefficient is \(c_\eta/\log(2+n)\), independent
of the depth witnessing \(V^{[r]}(n)\ge\eta n\). Formula (S10)
still pays \(3^{-r}\). Summing over the actual sibling indices does
not cancel that payment: \(\sum_{j\ge1}64^{-j}=1/63\).

The full average in (S8) would avoid this payment if a comparable
fraction of residue classes carried a value comparable to the specified
spike. Such a conclusion is not supplied by a lower bound at that one
ordinary integer. For example, if

\[
 \vartheta=\frac{\#\{a\in(\mathbb Z/3^{r+1}\mathbb Z)^\times:
                    F_r(a)\ge\alpha F_r(n)\}}
                   {2\cdot3^r},
\]

then (S8) supplies coefficient \(2c\alpha\vartheta/(3\sqrt b)\).
Nothing in the routing theorem bounds \(\vartheta\) from below at
a specified high-linear spike.

There is a useful elementary check on any attempted replacement of
that missing fraction. The unrestricted critical operator preserves
unit-Haar mean: each affine branch has ternary Jacobian \(1/3\),
so its integrated coefficient is \(2^{-e}\), and
\(\sum_{e\ge1}2^{-e}=1\). Therefore the Bellman recursion gives

\[
 \langle F_r\rangle\le r+1,
 \qquad
 \vartheta\le\frac{r+1}{\alpha F_r(n)}.
\tag{S12}
\]

These averages can be read on any sufficiently fine finite quotient;
no limiting density at an ordinary point is assumed. In particular,
when the supplied spike has height \(\eta n\), a general argument
declaring a fixed positive residue fraction would conflict with (S12)
whenever \(n\) is much larger than the clock \(r\). The estimate
does not bound the true sibling ratio from above; it diagnoses the
information that the proposed averaging proof discards.

### The existing density inputs give a stronger mean bound

Under the same source-qualified mixing and atom-floor inputs already
used to construct the canonical envelope, the means in fact stay
bounded uniformly in \(r\). This is a short consequence of those
inputs, rather than a new regularity claim about specified integers.

Write \(D_s\), for \(s\ge1\), for the usual full-Haar Syracuse
densities, and regard them as finite-cylinder functions on
\(\mathbb Z_3\). They vanish on nonunits and satisfy
\(D_{s+1}=PD_s\). Their initial construction allows a nonunit
oldest source, whereas the operator in (S1) omits nonunit terminal
values; the displayed recursion agrees because \(D_s=0\) there
for \(s\ge1\). We do not identify \(D_1\) with \(P1\) for
the unit-restricted operator (S1).
Summing out the clock in the existing `JOINT_CLOCK_MIXING.md` estimate
(JF) makes \(D_s\) Cauchy in \(L^1\). Its limit \(\rho\) has
full-Haar mean one and vanishes on nonunits. The same branch change
of variables makes \(P\) a positive \(L^1\) contraction, so
\(D_{s+1}=PD_s\) implies \(P\rho=\rho\) in \(L^1\), hence
almost everywhere. The earlier uniform floor \(D_s\ge c_0>0\)
on units for all sufficiently large \(s\) implies
\(\rho\ge c_0\) almost everywhere on units.

Induction in the Bellman recursion now gives
\(F_r\le\rho/c_0\) almost everywhere for each \(r\). Positivity
of \(P\) preserves an almost-everywhere inequality: its branch
maps are nonsingular and there are only countably many branches.
Because normalized unit Haar has total mass one while the units have
full-Haar mass \(2/3\), it follows that

\[
 \boxed{\langle F_r\rangle\le\frac{3}{2c_0},\qquad
 \vartheta\le\frac{3}{2c_0\alpha F_r(n)}.}
\tag{S13}
\]

The value of \(\rho\) at the ordinary point \(n\) has never been
used. Each \(F_r\) is a genuine finite-cylinder observable, so its
Haar integral and its level-set fraction are well defined independently
of which null-set representative is chosen for \(\rho\).

Thus even an arbitrarily deep Bellman witness does not force a broad
Haar fraction at the height \(\eta n\): the fraction is at most
\(3/(2c_0\alpha\eta n)\). The lower-bound certificate in (S8)
only depends on the bounded mean and the block normalization. It does
not retain the exceptional high value needed by OPEN-F. Neither (S13)
nor this observation is an upper bound for the actual sibling mass.

The second attempted route was height-feedback repair: at each paired
inverse node choose an admissible new exponent near
\(e+\log_2(x/y)\) to keep the new predecessor comparable to the
old one. This can repair one step when such a positive exponent is
available. When \(y/x\) is large and the old exponent is small, the
new exponent cannot be lowered below the least legal unit exponent.
That least exponent depends on the actual residue modulo nine, and
its repeated real growth is not bounded by the old contracting path.
Allowing extra inverse steps has the same issue. No weighted terminal-
height bound under the original stopping policy was established. The
existing rank-pairing formula already identifies this uncontrolled
quantity exactly; it must not be replaced by iid gaps.

## 5. Outcome and handoff

The new use of the literature is a genuine all-root finite transport
estimate (S7), with a legal complete-antichain implementation (S10).
It improves the use of the routing theorem from one existential word
to its full critical mass and makes its cost explicit. Its one-spike
consumer does not improve OPEN-F's quantitative lower bound.

A successful continuation would have to preserve the exceptional
ordinary spike through the repair, or control the replaced physical
source heights under its actual stopping mass. Modular accessibility,
even with the almost linear valuation budget in v4, does not itself
do either. No positive nonsummable sibling-current bound or escape
exclusion has been obtained in this lane.

### Frozen dependencies and evidence

- PR180, `a66a44c9bf058cd7efe1018827ddda9a13297a21`,
  `research/central-step-20261122/CRITICAL_BOUNDARY.md`, Section 6:
  original OPEN-S/OPEN-F and actual sibling summability.
- Same head, `research/lean-forward-band-20261121/MINIMAL_ENVELOPE_ATOM_REMOVAL.md`:
  all-positive obstacle recursion and retained-domain restriction.
- Same head, `research/lean-forward-band-20261121/JOINT_CLOCK_MIXING.md`,
  (JF), and `research/lean-forward-band-20261121/GLOBAL_RENEWAL_ATTACK.md`,
  Section 8: the existing full-Haar mixing and uniform unit-density floor
  used only for (S13). Their source qualification is retained.
- PR175/178/185 at the exact heads and paths in Section 1:
  earlier legal repairs, terminal distortion, and the sibling entropy cost.
- Paper 37 **v4**, Lemma 11 and Theorem D:
  https://rstation.ai/api/v1/papers/collatz_37/versions/4/download . The page's current
  version was checked after an initial v3 read; only v4 supplies (S2).
  The versioned Markdown download was opened successfully from the
  current paper page; the guessed `/37/v4` HTML route was inaccessible.
  The finite consumer is proved above; the imported analytic count remains
  source-qualified. No full external proof audit or formal replay is claimed.

No large numerical search was needed for the deduction. No historical
priority claim is made for this consumer or its operator formulation.
