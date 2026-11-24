# Ordinary cycle occupation and a full-statement Lean proposal

**Collatz remains OPEN.** This pass attempted a universal proof using the latest minimum-source, exact-clock, paired-ancestor and companion results. It establishes a further restriction on every sufficiently long hypothetical ordinary cycle, synchronizes that restriction with the companion at the same physical phases, and gives a compiled end-to-end certificate theorem. The universal certificate coverage needed to instantiate that theorem is not proved.

The map throughout is the shortcut map

$$T(n)=\begin{cases}n/2&n\text{ even},\\(3n+1)/2&n\text{ odd}.\end{cases}$$

On odd inputs, $U(n)=(3n+1)/2^{v_2(3n+1)}$. A positive ordinary integer is **good** if some finite iterate of $T$ equals 1. All counting statements below retain their actual ordinary paths. Rational cycles are used only as expressly identified controls.

## A complete-cycle restriction from the literature

**PROPOSED written theorem, independently reconstructed.** There is an absolute $p_0$ such that every primitive positive ordinary cycle of odd period $p\ge p_0$, with minimum $m$, has

$$\#\{i:x_i>2m\}>p/21.$$

There is also an absolute positive fraction valid for every nontrivial ordinary cycle. No numerical onset or unconditional cycle exclusion is asserted.

The new connection uses Wu and Wang's actual three-coefficient logarithmic-form theorem, with its constant coefficient set to zero. The full-period identity gives

$$0<A\log2-p\log3\le p/(3m),\qquad
  \log m\le(5.1163051+\varepsilon)\log p+O_\varepsilon(1).$$

For $k=\max(1,\lceil\log_3m\rceil)$, a path with a prescribed sequence of height intervals $[2^{h_i}m,2^{h_i+1}m)$ and terminal height in $[m,2m)$ has at most $k+1$ ordinary sources. A new integer proof of this complete capacity bound is Lean checked. It orders the lifted values $2^{A_i}x_i$, then uses terminal spacing modulo $3^k$ to separate words.

If at most $p/21$ odd phases were above $2m$, at least $p/84$ circular length-$k$ windows would have both endpoints in the lowest interval and at most $4k/75$ positive interior levels. The levels rise by at most one at each odd step. Their reverse difference code is injective, has length $k$, and has total mass equal to the number of positive levels. Weak-composition counting and the source capacity give

$$p/84\le(k+1)^2\exp\!\big(kf(4/75)\big),\qquad
 f(t)=(1+t)\log(1+t)-t\log t.$$

The strict inequality $5.12f(4/75)<\log3$ makes the right side $o(p)$. Lean checks both the code and an exact integer form of that numerical inequality.

[Full proof and source](critical/CYCLE_OCCUPATION.md) · [Independent reconstruction](minimum/CYCLE_REVIEW.md) · [Ordinary capacity kernel](minimum/MovingOctaveOrder.lean) · [Profile code kernel](critical/OctaveOccupation.lean)

## The physical and companion conditions occur at the same phases

**PROPOSED written theorem, independently reconstructed.** The high physical states above can be synchronized with the all-pasts companion records of PR205. This is an overlap theorem on one supplied periodic orbit, not an inference from two marginal counts.

Put $\rho=3/5$, $d=\log2-\rho\log3$, $c=d/2$ and $V=(1-\rho)\log3$. For every sufficiently long primitive ordinary cycle, and every real height threshold $H$, its strict record set $R$ satisfies

$$\#\{a\in R:x_a>e^H\}
 \ge\frac{c}{c+V}\#\{i:x_i>e^H\}.$$

Between successive records, physical logarithmic height loses at least $c$ per clock, apart from a bounded overshoot at the next record. Charging high clocks against the potential $(\log x-H)_+$ and summing over a lap proves the inequality. At these same high records, the companion has a uniformly bounded positive value and distinct sufficiently long preceding parity words.

The physical cycle denominator and the reduced companion denominator remain different integers. Rotating the physical word gives equivalent divisibility tests modulo the physical denominator; the synchronized past count does not turn those rotations into independent congruences. The written proof identifies this remaining arithmetic step.

[Synchronization proof](critical/COMPANION_SYNCHRONIZATION.md)

## The final Lean proposal and its exact missing input

[UniversalProposal.lean](UniversalProposal.lean) proves

$$
(\forall n>0,\ \exists k,\ T^k n=1)
\quad\Longleftrightarrow\quad
(\forall q>1,\ \exists\,0<v<q,\ \exists i,j,\ T^i(3q)=T^j(3v)).
$$

This elementary integration criterion is not claimed as a new equivalent formulation. The module's purpose is to expose the complete statement and make every proposed certificate checkable against it.

The backward direction first uses strong induction on $q$ to prove convergence of every positive multiple of three. Six explicit ordinary inverse paths then cover every positive integer: every such integer is the endpoint of a positive multiple of three after at most six shortcut steps. The forward direction uses the verified path from 3 to 1.

A certificate contains a smaller positive index and two independent finite clocks. Its checker evaluates both literal paths. The final theorem is:

~~~lean
theorem certified_collatz (selector : Nat → Certificate)
    (coverage : ∀ q, 1 < q → check q (selector q) = true) :
    ∀ n, 0 < n → ∃ k, run k n = 1
~~~

**The coverage proof is OPEN.** There is no total successful selector in this packet. No finite census, almost-everywhere estimate, supplied analytic axiom or admitted proof is used to discharge that hypothesis. The cycle theorems above do not establish it.

## Other full-closure routes examined

The [minimum-source construction](minimum/README.md) gives infinitely many actual good lower arms $q$ with fixed $v_3(3q)=3$ and arbitrarily many expanding 11110 blocks on the upper arm. Both arms can avoid every meeting with each clock at most the prescribed horizon. At a fixed source, however, Lean proves that precisely the prefixes with $32^K\mid49x+65$ are legal, so infinite repetition of this word is impossible. These are different quantifiers. The construction does not satisfy the least-failure hypothesis.

The [exact ordinary coboundary](interior/ORDINARY_STATIONARY_BOUNDARY.md) shows why stationarizing a trajectory loses the root $3q$: an odd multiple of three leaves divisibility by three immediately and never returns. Lean proves the finite counting identity and the full exit statement. Assani's power-bounded finite-measure criterion would need a separate law that actually charges the supplied root. An [ordinary high-record family](interior/HIGH_RECORD_ROOT_TEST.md) also keeps the companion bounded through arbitrarily long growing prefixes with a good lower arm.

The [exact-clock comparison](critical/CLOCK_MASS.md) retains the relative real carry. Conditional on the named floor F, the entire balanced row at every ordinary unit target already has mass of order at least $b^{-1/2}$, while PR201's required large-carry count corresponds to an exponentially small mass. An upper bound on the entire row cannot provide the opposing estimate through positivity alone.

The [variation construction](interior/VARIATION_BOUNDARY.md) saturates PR197's shattering lower bound at its actual query locations if invariant basin labels and replayed query legality are omitted. It does not construct invariant labels or refute that source theorem.

## Evidence, dependencies and replay

The new five-module replay passes Lean 4.34.1, compiler commit 5045d0056413266e57c625dcd7c365b10e377c52, with warnings as errors and automatic implicit variables disabled. All **31 public theorem declarations** are axiom-audited. Their dependencies are contained in the standard axioms propext, Classical.choice and Quot.sound, or empty. The modules import only Std.

The complete asymptotic cycle argument, Wu–Wang's theorem, the companion synchronization and the ordinary interpolation construction remain written mathematics. The source-qualified floor F appears only in its separate clock-mass deduction. Neither F nor any other analytic hypothesis is inserted into the Lean proof.

Run only the new kernels and construction controls:

~~~bash
python -B research/astra-universal-proof-20261124/replay.py \
  --lean /absolute/path/to/lean \
  --report-dir /absolute/path/to/receipts
~~~

[Compiler receipt](../../reports/astra-universal-proof-20261124/kernel/LEAN_REPLAY.json) · [Coordinator review](../../reports/astra-universal-proof-20261124/ROOT_REVIEW.md) · [Frozen source files](../../reports/astra-universal-proof-20261124/SOURCE_BINDINGS.json) · [Latest-work intake](../../reports/astra-universal-proof-20261124/PR_INTAKE.json) · [Literature scope](LITERATURE.md)
