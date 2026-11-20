# Full-measure paired returns, ordinary density, and the critical pressure

**PROPOSED, with an explicitly source-qualified control input.**
The results below prove almost-sure paired returns and a density-one
ordinary paired-descent statement. They do not prove forward-five
closure or the Collatz conjecture. They also identify precisely why
the full return dictionary cannot have a bounded label-blind
subcritical inverse-fiber kernel.

## 1. Sources and normalization

Use the shortcut map, affine-section lattice, state recurrence, and
finite core of `AFFINE_SECTION_RECURRENCE.md`, Theorem S. Thus

\[
y=5\,3^k x+c,\qquad
c\in3^{-\max(0,-k)}\mathbb Z.
\]

Put \(D=3^{\max(0,-k)}c\in\mathbb Z\), so

\[
3^{k_-}y=5\,3^{k_+}x+D,
\qquad k_+=\max(k,0),\quad k_-=\max(-k,0).
\tag{R1}
\]

The imported deterministic control is PR146 at the exact head
`66970775e4bdc945a68308e37a8eb028ebde42d2`,
`research/upper-bit-mergers/FIVE_RETURN_IN_EVERY_CLASS.md`, Section 1.
It routes every integer state \((k,D)\) to \((0,0)\) by a finite
choice of source parity bits. Its qualitative termination argument
is reconstructed below; the source's additional uniform clock bound
and modular localization theorem are not needed here.

The inverse-fiber averaging input is PR167 at the exact head
`e83cc8b35ad614c616df7c00318cc9645a174c34`,
`research/least-failure-closure-20261121/DENSITY_CONGESTION.md`,
DC1--DC3. Section 5 states the precise normalization used from it.

## 2. Reconstructed communication to the root

For source bit \(i\), let \(j=i+D\pmod2\), taking \(j\in\{0,1\}\),
and put \(t=k+j-i\). Direct substitution in (R1) gives

\[
k'=t,\qquad
2D'=3^{t_-+j-k_-}D+3^{t_-}j-5\,3^{t_+}i.
\tag{R2}
\]

Every exponent displayed here is nonnegative. Parity guarantees
that the integer numerator is even. This is precisely (S1) after
normalizing the denominator.

For nonzero \(k\), an even \(D\) has the two same-level updates

\[
D\longmapsto D/2,\qquad
D\longmapsto(3D+c_k)/2,
\quad c_k=3^{k_-}-5\,3^{k_+}.
\]

Its binary valuation is \(v_2(c_k)=1\) for odd \(k\), and two for
even nonzero \(k\). If \(0<v_2(D)\le v_2(c_k)\), use zero bits
until \(D\) is odd. If \(D=0\) or its valuation is larger, first
use one bit and then strip the remaining factors two with zero bits.
At most two bits are needed to make \(D\) odd. With odd \(D\),
choose \(i=1\) for \(k>0\) and \(i=0\) for \(k<0\). This lowers
\(|k|\) by one. Therefore level zero is reached in at most
\(3|k|\) bits.

At level zero, halve an even nonzero \(D\). For odd \(D\), choose
one bit, giving level \(-1\) and offset \(F=(3D-5)/2\ne0\).
Choose \(v_2(F)\) zero bits to reach its signed odd part \(f\),
then one further zero bit. The resulting state is

\[
k'=0,\qquad D'=(f+1)/2.
\tag{R3}
\]

If \(D\ge3\), then \(0<D'\le(3D-3)/4\). If \(D<0\), then
\(|D'|\le(3|D|+3)/4\). Thus absolute value strictly decreases
for \(|D|>3\). The cases \(D=1,-1,3\) respectively give
\(0,0,1\). For \(D=-3\), the source bit word `1101000` gives

\[
(-1,-7),\ (-2,-13),\ (-1,-5),\ (-2,-10),\
(-2,-5),\ (-1,-1),\ (0,0).
\]

This proves finite root accessibility from every lattice state. It
chooses a finite continuation in a binary cylinder; it does not
change the already fixed higher bits of a supplied ordinary integer.

## 3. Almost-sure root recurrence

**Theorem R.** Under Haar binary input, the section chain visits
\((0,0)\) infinitely often, almost surely. The conclusion also holds
after any specified finite source prefix.

**Proof.** Theorem S gives almost-sure returns to a finite core
\(\mathcal F\) from every state. For each state in \(\mathcal F\),
choose one finite root-control word from Section 2. Let \(L\ge1\)
be the maximum of their lengths. At the root, a zero source bit
leaves the section at the root. Pad each selected word with such
bits to length \(L\). Conditional on a core visit, there is then
probability at least \(2^{-L}>0\) of a root visit in the next
\(L\) steps.

After an unsuccessful trial, wait until the next core visit and
try again. Each wait is almost surely finite, by Theorem S and the
Markov property. The conditional probability of failing the first
\(m\) trials is at most \((1-2^{-L})^m\), which tends to zero.
Thus the root is hit almost surely from every state. Applying the
same argument after each deterministic time proves infinitely many
root visits. No independence of successive trials is assumed; the
uniform conditional lower bound is enough. The finite-prefix claim
uses the exact fresh-bit realization in Section 2 of the companion
proof. \(\square\)

At a root visit at clock \(h\),

\[
T^h(5x)=5T^h(x),\qquad p_Y(h)=p_X(h).
\tag{R4}
\]

The first positive root-return words form a prefix-free binary
dictionary of total Haar measure one. The statement concerns
finite parity cylinders; it does not assert that every ordinary
integer belongs to the dictionary.

There are also infinitely many root visits at which the current
source is odd. At a root visit, a zero bit keeps the state at the
root. A run of zero bits ends in a one bit with probability one;
at its starting clock the section is still at the root and the
current source is odd. Repeated root visits give the assertion.
The next bit used to specify odd endpoint parity is independent of
the already consumed finite prefix.

## 4. A strict ordinary paired descent outside a uniformly sparse set

Fix \(0<\theta<1\) and a nonnegative delay \(H\). Under Haar input,
the strong law for the independent fair source bits gives
\(p_h/h\to1/2\). Hence

\[
\frac{3^{p_h}}{2^h}\longrightarrow0.
\]

By Theorem R and its odd-endpoint refinement, almost every parity
sequence has a clock \(h\ge H\) at which the section is the root,
the current source is odd, and the common affine slope is less
than \(\theta/2\). On its corresponding finite cylinder,

\[
q=T^h(x)=\frac{3^{p_h}x+B}{2^h},\qquad
T^h(5x)=5q,
\quad B\ge0.
\tag{R5}
\]

Every sufficiently large positive ordinary lift in that cylinder
satisfies \(q<\theta x\). The necessary lower bound on \(x\)
may depend on the finite word. When the starting source is odd,
the endpoint is a ternary unit, since after its first odd step
the ordinary shortcut orbit cannot enter zero modulo three.

**Ordinary density conclusion.** Among positive odd ternary units,
the inputs admitting an exact paired descent (R5), with odd endpoint
and clock at least \(H\), have relative natural density one. More
strongly, their complement has **zero upper Banach density** relative
to that domain. Without the odd-unit restriction the analogous
statement holds in the positive integers, omitting any unnecessary
endpoint restriction.

Here zero upper Banach density means that the largest proportion of
failures in an interval of length \(N\) tends to zero as \(N\to\infty\),
uniformly in the position of the interval. To prove the statement,
choose any \(\varepsilon>0\). A finite union of successful parity
cylinders has relative measure at least \(1-\varepsilon\), because
the full countable union has measure one. Refine them to a common
finite binary period, and impose the odd-unit restriction using
the additional modulus three. Every such periodic set has its
stated density uniformly over intervals, with counting error bounded
by a constant depending only on the period. The ordinary height
thresholds remove only finitely many points from this finite union;
their counting contribution divided by \(N\) tends uniformly to
zero. Thus the failure set has upper Banach density at most
\(\varepsilon\). Let \(\varepsilon\downarrow0\).

Within one prescribed finite prefix the same proof gives the
relative version; its absolute density is the prefix's density.
No quantitative rate in the interval length or in the delay is
obtained by this argument.

The delay \(H\) is fixed before this density assertion. Taking a
countable intersection over delays does not prove a pointwise
ordinary theorem. In fact **every positive integer whose source
has a supplied terminating certificate has only finitely many root
returns**, regardless of whether its multiplied companion converges.
If the companion does not converge, a root return after the source
has entered \(\{1,2\}\) would put the companion at five or ten,
forcing convergence and contradicting the premise. If the companion
does converge, then after both trajectories reach \(\{1,2\}\),
their ratio can never be five. Thus all certified ordinary sources
lie in the null exceptional set of infinitely many root returns.
This is a domain limitation, not evidence of nonconvergence.

## 5. Null recurrence and infinite subcritical average pressure

The stronger probabilistic return theorem does not improve the
full positive inverse-fiber kernel in the direction needed for
an energy contraction. The following establishes a sharp limitation
for this full return dictionary.

### R5.1. The expected positive root-return time is infinite

Condition on an odd initial source. The first source bit is one,
so after one step the section is \((k,c)=(0,-2)\). Let \(\tau\)
be the first subsequent time of hitting the root. It is almost
surely finite by Theorem R, but

\[
\mathbb E\tau=\infty.
\tag{R6}
\]

Indeed the martingale \(k_t\) starts at zero and has quadratic
variation increment \(\mathbf1_{\{c_t\text{ odd}\}}\). From
\((0,-2)\) the next carry is either \(-1\) or \(-5\), so an
active step occurs before any root hit. If \(\mathbb E\tau\)
were finite, the stopped martingale would converge in \(L^2\):
the second moment of its tail increments is bounded by
\(\mathbb E(\tau-n)_+\to0\). Its terminal value is zero. The
martingale second-moment identity would then give

\[
0=\mathbb E k_\tau^2
=\mathbb E\sum_{t<\tau}\mathbf1_{\{c_t\text{ odd}\}}\ge1,
\]

a contradiction. Including the one initial step leaves the
infinite expectation unchanged. The unconditioned first positive
root-return time also has infinite expectation, because its odd
initial branch has probability one half. This is null recurrence
of the reachable root class, not a finite mean renewal process.

### R5.2. Any full odd-source return selection has infinite pressure

Choose any almost-surely finite rule selecting a **positive**
root-return clock \(\sigma\) with odd endpoint, based on a finite
parity prefix. The first odd-endpoint return, or the first return
meeting the strict slope condition of Section 4, is such a rule.
It is at least the first positive root-return time, so
\(\mathbb E\sigma=\infty\) under odd initial input. The endpoint
oddness may require looking at the bit at clock \(\sigma\); no
stopping-time identity for \(\sigma\) is used below.

Let \(p_t\) count odd source bits at clocks \(0,\ldots,t-1\).
Conditionally on the initial bit being one,

\[
\mathbb E2^{p_t}=2(3/2)^{t-1}
=\frac43(3/2)^t.
\]

Markov's inequality gives the explicit exponential bound

\[
\Pr(p_t\ge3t/5)\le\frac43\alpha^t,
\qquad \alpha=\frac{3/2}{2^{3/5}}<1,
\quad\alpha^5=\frac{243}{256}.
\tag{R7}
\]

Therefore

\[
\mathbb E\big[\sigma\mathbf1_{\{p_\sigma\ge3\sigma/5\}}\big]
\le\frac43\sum_{t\ge1}t\alpha^t<\infty.
\]

On the complementary event,

\[
\log\frac{2^\sigma}{3^{p_\sigma}}
>\sigma\left(\log2-\frac35\log3\right)
=\frac\sigma5\log(32/27)>0.
\]

It follows from \(\mathbb E\sigma=\infty\) that

\[
\mathbb E\left[\left(\log\frac{2^\sigma}{3^{p_\sigma}}
\right)_+\right]=\infty,
\qquad
\boxed{\mathbb E\left[\left(\frac{2^\sigma}{3^{p_\sigma}}
\right)^{1-s}\right]=\infty\quad(0<s<1).}
\tag{R8}
\]

The last implication uses \(e^{a u}\ge a u\) for \(a,u>0\).
It needs no independence between the return rule and the bits.

### R5.3. Application of the pinned finite-fiber averaging identity

For the dictionary statement, choose either the first positive
odd-endpoint root return or the first return meeting Section 4's
fixed delay and slope conditions. Acceptance at clock L is then
decided by exactly the consumed L bits and the endpoint parity bit
at clock L; no later lookahead is used. This makes the first
successful selection a prefix-free dictionary. The expectation
argument in R5.2 allowed more general selections, but the following
cylinder normalization is asserted only under this guard.

A selected word with clock \(L\) and \(p\ge1\) odd
inputs specifies its endpoint's next parity as well. Its relative
binary cylinder measure among odd starting inputs is \(2^{-L}\).
Restricting sources to ternary units does not change this relative
measure. For each word,

\[
x_w(q)=\frac{2^{L_w}q-B_w}{3^{p_w}},\quad B_w>0,
\qquad 3\nmid B_w.
\]

Odd ternary-unit endpoint legality has relative residue fraction
\(3^{-p_w}\), including exclusion of source multiples of three.
For any **finite** subdictionary \(F\), DC2 gives

\[
\lim_{Q\to\infty}\operatorname{mean}_{\substack{q\le Q\\
q\text{ odd},\;3\nmid q}}
\sum_{\substack{w\in F\\q\text{ legal}}}
\left(\frac{q}{x_w(q)}\right)^s
=\sum_{w\in F}2^{-L_w}
\left(\frac{2^{L_w}}{3^{p_w}}\right)^{1-s}.
\tag{R9}
\]

At \(s=1\), increasing finite subdictionaries have limiting mean
approaching one. At every \(0<s<1\), their limiting means are
unbounded by (R8). Consequently a label-blind bound on the complete
positive inverse-fiber kernel, valid at every endpoint outside a
fixed finite set, must satisfy

\[
C\ge1\quad(s=1),\qquad C=\infty\quad(0<s<1).
\tag{R10}
\]

No exchange of an infinite family with an endpoint average occurs:
apply the proposed uniform bound to each finite subdictionary and
then increase that finite family. Removing the finitely many small
ordinary sources required for a strict height decrease does not
change any of the finite-family limits in (R9).

This conclusion is specific to controlling every possible positive
endpoint charge separately. It does not establish divergence of
the energy of an actual invariant label. Such labels may have many
zero defects, and their supports are not arbitrary delta masses.
A support-sensitive argument, a signed identity, or a separately
certified zero-defect family is not ruled out by (R10).

## 6. Remaining ordinary implication

The new combination gives both an almost-sure root return theorem
and an ordinary density-one supply of finite paired descents. The
preserved identity is still \(d_5(x)=d_5(q)\), where
\(d_5(x)=d(f(5x),f(x))\) for an actual ordinary invariant label.
It does not force that common value to vanish. An ordinary source
can lie in the exceptional set for a selected future return, and
the full positive subcritical kernel has the obstruction (R10).

The first missing closing statement is therefore a pointwise or
support-sensitive ordinary assertion: every actual failed
five-comparison must reach a strictly smaller failed comparison,
or its total weighted defect must be finite by an estimate that
uses actual invariant-label constraints. Neither is proved here.
GRH has no role in the theorems above and supplies no such ordinary
transfer merely by being assumed.
