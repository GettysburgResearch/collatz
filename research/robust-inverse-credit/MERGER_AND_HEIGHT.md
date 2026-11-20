# Merger and height boundary

Status: **SOURCE-QUALIFIED context, elementary lemmas proved below, OPEN universal merger step.**

Normalization throughout is the shortcut map

\[
T(n)=\begin{cases}n/2&2\mid n,\\(3n+1)/2&2\nmid n.\end{cases}
\]

An odd inverse edge is \(I_e(x)=(2^e x-1)/3\), with positive odd source and target coprime to three. It costs exactly \(e\) shortcut steps. Algebraic statements about ternary units use the same affine map without asserting ordinary realization.

## 1. The frozen merger obligation

The inspected sources are PR146 at `fcb2b72847a82da5c6ebdc81ae4022ba9c03ae3d`, principally `research/upper-bit-mergers/README.md`, and PR145 at `dd245a712f985909f541590e3f6c179b7ba011e4`, principally `research/profinite-orbit-averages/ONE_STEP_LAG.md`. The main baseline is `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`. The research map, rank-merging resident packet, and integrated errata were read before reuse.

PR146 proves an elementary equivalence: Collatz holds if and only if every pair

\[
1+3w,\qquad 1+3(w+2^j),\qquad j\ge0,\quad0\le w<2^j
\]

has a common future iterate, with independent finite clocks allowed. Removing the highest binary digit of an index proves the sufficiency by induction; every positive unit is represented by either itself or twice itself in the class \(1\pmod3\). This is already a complete pointwise reformulation, not a proved merger selector.

The same packet shows why uniformly cheap mergers cannot close this obligation. In a shared binary prefix of length \(h\), the post-prefix difference is \(3^s\), where \(s\) is the prefix odd count. For typical prefixes, mergers require an even-step budget near or above \((\log_2 3)s\). The proved obstruction concerns that budget; it does not exclude later mergers at larger clocks. PR145 likewise distinguishes actual source paths from unrestricted Haar reverse extensions.

## 2. Ternary routing is already stronger than the finite probes

The current external literature must be credited before advancing a new routing claim. Paper127, Theorems 1, 2 and 5, asserts unique stationarity and supplied-state empirical convergence for every strictly positive finite-precision inverse rule with exponent cap at least six. Its Sections 11–12 transfer window certificates to actual integer paths and identify the stochastic window limit with the optimal Haar inverse slope. It cites Paper118 for all-precision cap-five routing and Paper126 for an explicit routing length bound.

These are **imported published claims**, not independently reproved here. I inspected Paper127's conditional-information, entropy-concentration, convolution-growth, Haar-identification, and compact Feller arguments. I did not reconstruct every analytic input. The retrieval of Papers118 and126 themselves failed, so their stronger routing conclusions are recorded only through Paper127's stated dependencies.

Consequently the exploratory cap-six residue covers are not claimed as novel results or included as scientific deliverables. They verified a finite interface and helped expose the distinction between an exact depth and a bounded hitting time. They do not compete with the all-precision source results.

## 3. Where the new compiler interface fits

The packet's proposed finite-credit interface uses a different implication from Paper127's stochastic window completeness. For the full ternary state space, let

\[
(F_\rho f)(x)=\min_{e\text{ legal},\ e\le r}\{e-\rho+f(I_e x)\}.
\]

Uniform negative expected cost over some finite horizon, obtained from a uniquely stationary positive rule with mean cost below \(\rho\), implies \(F_\rho^N0<0\) everywhere. Then

\[
V=\min_{0\le j<N}F_\rho^j0
\quad\Longrightarrow\quad F_\rho V\le V.
\]

The finite minimum commutes with this Bellman operator. Each iterate is locally constant at finite ternary precision. Reading one more digit than the potential fixes the child's potential value for every remaining lift. This is the step that converts the full-state inequality into a robust finite table.

Paper127 explicitly cautions that an averaged finite-window bias inequality cannot simply be lifted pointwise by increasing precision. The full-state finite-horizon argument above supplies an intermediate step; it must remain in the proof. I did not find this robust-certificate equivalence stated in Paper127 or Paper150. Its status should be an interface corollary derived in this packet from the imported stationary theorem, without a priority claim beyond the inspected sources.

## 4. Why a better inverse compiler does not yet prove a merger

For an inverse word of \(n\) odd edges and total shortcut cost \(E_n\),

\[
x_n=\frac{2^{E_n}x_0-C_n}{3^n},\qquad C_n>0.
\]

A uniform credit bound \(E_n\le\rho n+B\) therefore gives

\[
0<x_n<2^B x_0\left(\frac{2^\rho}{3}\right)^n.
\]

When \(\rho>\log_2 3\), this permits exponential growth. It provides neither a predecessor smaller than the source nor an intersection with another specified component. It also does not turn the random inverse policy into the deterministic forward itinerary of its starting integer.

There is an elementary obstruction even at the critical slope. No infinite positive ordinary inverse path can satisfy \(E_n\le n\log_2 3+B\) for every \(n\). Such a bound would keep every \(x_n\) below \(M=2^B x_0\). But the exact recurrence gives

\[
E_n-n\log_2 3
=\log_2(x_n/x_0)+\sum_{j=1}^n\log_2\left(1+\frac1{3x_j}\right)
\ge-\log_2 x_0+n\log_2\left(1+\frac1{3M}\right),
\]

which eventually exceeds \(B\). Thus the desired closure must use a forward descent, an asynchronous merger, or another ordinary-source argument; it cannot be an everywhere subcritical infinite inverse compiler.

Paper150 supplies a stronger source-qualified statistical barrier: stationary legal inverse laws with an absolutely continuous source and finite mean cost have mean strictly above \(a_*=1/0.6090897679\ldots>\log_2 3\). Its Corollary4 forces a hypothetical divergent forward orbit to put at least

\[
\frac{a_*-\log_2 3}{a_*-1}=0.0885511696\ldots
\]

of every limiting ternary empirical law on a particular Haar-null set. This condition is not a contradiction; a chosen uniformly branching inverse law and the actual inverse past have different label laws.

## 5. Two failed merger mechanisms, with exact reasons

**Common inverse words cannot amplify the special bad edge indefinitely.** If the same legal inverse word of \(m\) odd edges sends two integer sources \(u,v\) to integers, its affine formula gives

\[
I_w(u)-I_w(v)=\frac{2^E(u-v)}{3^m}.
\]

Hence \(3^m\mid u-v\). For the PR146 pointwise pairs the difference is \(3\cdot2^j\), so a shared inverse word has at most one odd edge. This rules out a synchronized thickening argument, not arbitrary asynchronous constructions.

**A local equal-cost actuator does not automatically lift to the original source.** Direct calculation gives

\[
I_bI_a(t)=\frac{2^{a+b}t-2^b-3}{9}.
\]

For \(b\ge7\), replacing \((a,b)\) by \((a+6,b-6)\) preserves total cost and changes the endpoint by \(7\cdot2^{b-6}\). First-edge legality modulo nine is preserved, but the new final endpoint must still be checked to be a unit. More decisively, this displacement is a ternary unit. Lifting the modified endpoint backwards through \(q\) earlier odd edges requires divisibility by \(3^q\), which this displacement lacks.

The precision cost is exact within this two-edge mechanism. A positive even transfer \(\delta<b\) changes the endpoint by

\[
D=\frac{2^{b-\delta}(2^\delta-1)}9.
\]

The lifting-the-exponent identity gives \(v_3(D)=v_3(\delta)-1\). Therefore \(3^q\mid D\) forces \(2\cdot3^{q+1}\mid\delta\), and hence \(b>\delta\ge2\cdot3^{q+1}\). (If the two endpoints are not both integral, the modification has already failed.) This proves the exponential donor-cost obstruction for this particular redistribution, not for arbitrary longer-word constructions. A genuine multiscale carry construction remains missing.

## 6. First unsupported inference and the next target

The unsupported inference is:

> Every component has well-controlled inverse paths and dense ternary residue coverage, therefore every two positive components intersect.

Neither residue coverage nor stationary occupation controls the ordinary integer height and exact equality needed here. A useful next theorem would give a successful asynchronous merger for every pair in Section1, or a complete lower-rank merger selector for every positive ordinary source. A finite table with an UNRESOLVED branch, an all-depth Haar statement, and success on a growing finite range do not meet that quantifier.

Sources: [PR146 frozen merger packet](https://github.com/GettysburgResearch/collatz/blob/fcb2b72847a82da5c6ebdc81ae4022ba9c03ae3d/research/upper-bit-mergers/README.md); [PR145 frozen sibling packet](https://github.com/GettysburgResearch/collatz/blob/dd245a712f985909f541590e3f6c179b7ba011e4/research/profinite-orbit-averages/ONE_STEP_LAG.md); [Paper127 v1](https://rstation.ai/problems/collatz/papers/127/v1); [Paper150 v2](https://rstation.ai/problems/collatz/papers/150/v2).
