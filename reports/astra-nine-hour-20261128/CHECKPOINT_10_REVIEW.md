# Checkpoint 10: subcritical renewal, the critical ordinary endpoint, and integer information

**The nine-hour pass continues. Collatz remains unresolved.** This checkpoint
contains written proofs, narrowly scoped Lean kernels, and exact finite
controls. The coordinator independently reconstructed the arguments described
below. Analytic inputs from other manuscripts retain their source qualifications.
The all-module replay and exact-control receipts describe their own scopes;
they do not turn the entire analytic packet into a formal proof.

## Subcritical collision renewal is bounded and converges exponentially

[SUBCRITICAL_COLLISION_RENEWAL.md](../../research/astra-nine-hour-20261128/machinery/phase11/SUBCRITICAL_COLLISION_RENEWAL.md)
uses the **tail** parameter \(0<r<1/2\): a gap \(e\) has probability
\((1-r)r^{e-1}\). If \(\mu_{r,n}\) is its length-\(n\) ternary offset law,
then
\[
 U_n=\left(\frac{1+r}{1-r}\right)^n\sum_z\mu_{r,n}(z)^2
       \uparrow U_\infty(r)<\infty.
\]
This answers the boundedness question explicitly posed in Mahler 164, §6,
for every subcritical parameter. The prior bound there is \(O_r(\sqrt n)\).
The coordinator read the definitions, normalization and stated question in
the primary manuscript. [Mahler 164, §6](https://rstation.ai/problems/collatz/papers/164)

The counting proof retains both physical clocks. At fixed word length and
total gap sum, the integer numerator determines the word. A collision with
clock difference \(d\ge0\) has an integer displacement
\(h=(2^dD_w-D_v)/3^n\), lying between \(-R_v\) and \(2^dR_w\).
Counting from the longer word gives a crucial extra restriction: the possible
displacements lie in a single residue class modulo \(2^d\). Under the
squared gap tilt \(Q\), with tail \(u=r^2\), the real numerator mark has a
uniform moment of order \(p>1\), chosen also above
\(2-\log2/(-\log r)\). Positive displacements are counted from one arm;
large negative displacements are counted from the other. Splitting at an
exponentially growing displacement cutoff gives a summable exponential bound
in \(d\), uniformly in depth. The same-literal-letter contribution is
exactly the previous normalized collision mass, proving monotonicity.

[EXPONENTIAL_SPLIT_DECAY.md](../../research/astra-nine-hour-20261128/machinery/phase11/EXPONENTIAL_SPLIT_DECAY.md)
then proves the stronger depth statement
\[
 Z_n:=U_n-U_{n-1}\le C_r e^{-c_r n},\qquad c_r>0.
\]
Its main step is a bound for late **eventually successful** comparisons of
two actual biased dyadic sources \(x\) and \(2^d x+h\). It allows a positive
probability of never fusing. The proof separates three different measures
and estimates:

* On full first-fusion cylinders, the affine image has exactly \(u^d\)
  times the original biased probability. This transfers estimates for the
  second arm with a stated \(u^{-d}\) cost.
* A stopped Hellinger comparison penalizes each mismatch by
  \(2\sqrt{u(1-u)}<1\). Summing over the stopping antichain is valid at
  arbitrary physical stopping lengths.
* Under the original iid source, the real inverse mark has finite mean and
  no atoms. A backwards Foster estimate makes high-mark occupation
  exponentially rare at any chosen block stride. For a fixed bounded
  normalized pair offset, a long all-common block can end at another bounded
  offset only when the real mark lies in a small interval. Nonatomicity
  makes this probability uniformly small, without an assumed Frostman rate.

Few mismatches and few high endpoints would force many such unlikely common
blocks. A subset union bound gives an exponential physical-time tail,
uniformly in \(h\), with an exponential cost in \(d\). The earlier real
moment and clock-separation bounds remove large \(h,d\); the remaining
finite set can be summed. The coordinator checked the backwards conditional
product, the common-block affine identity, the stopping-antichain estimate,
and the order of the two final truncations.

The resulting collision genealogy has a finite split suffix. Its limiting
mass at zero is \(1/U_\infty\), and at \(k\ge1\) it is
\((U_k-U_{k-1})/U_\infty\). The shared letters have the exact squared gap
tilt, and the suffix tail is exponential. No numerical comparison with
Mahler's particular parity-trap threshold is asserted. The full-alphabet
ballot exponent was already obtained by a different method in Weaver 167;
it is not claimed as a new consequence here.
[Weaver 167](https://rstation.ai/problems/collatz/papers/167)

[COLLISION_CLOCK_LIMITS.md](../../research/astra-nine-hour-20261128/machinery/phase11/COLLISION_CLOCK_LIMITS.md)
retains the first total \(s\) and clock separation \(d\). The normalized
collision row is exactly a convolution of the finite split-suffix law and
an iid squared-tilt clock sum. The suffix has a joint exponential moment
in its depth, total and clock difference, obtained by interpolating its
exponential mass bound with a crude geometric moment. Fourier inversion
for the geometric clock then gives a uniform local central limit theorem,
with normalized error \(O_r(n^{-1/2})\) summed over all \(d\).
Conditioning on any central exact total gives the limiting separation law
and the limiting mean number of fused integer translates at the same rate.

The same note identifies the exact finite-mean threshold for integer fusion
classes: \(\mathbb E_\theta K_\infty<\infty\) if and only if
\(\theta>3/4\). Below it, an exact equal-total collision identity and
cell counting give exponential mean growth. At \(\theta=3/4\), the class
is finite almost surely but has infinite mean. A compact-real marked
local limit gives \(\liminf \mathbb E K_n/\sqrt n\ge D/\sqrt{2\pi}\),
while finite-clock exactness gives \(\mathbb E K_n=o(n)\). The matching
critical asymptotic is left to the following checkpoint; it is not part
of this frozen claim. The coordinator read the precise compact Lipschitz
test and central-clock hypotheses of the imported theorem.
[Weaver 9, version 2, Theorem 18](https://rstation.ai/problems/collatz/papers/9)

`CollisionClockSpacing.lean` proves the actual chronological numerator's
directed bounds, cancellation of the coprime factor \(3^n\), dyadic
displacement spacing, and interval packing. `CommonBlockOffset.lean` proves
the physical rational affine update and the normalized mark identity on an
entire common parity block. The moment, probability and renewal arguments
remain written proofs.

## Ordinary collision energy detects exactly the escaping components

[ORDINARY_COLLISION_ENERGY.md](../../research/astra-nine-hour-20261128/escape/phase10/ORDINARY_COLLISION_ENERGY.md)
uses the actual positive odd map. Put \(w(x)=3x/(3x+1)\),
\(b(x)=\rho_1(x)/x\), and sum the true products \(W_n(x)b(x)\) over
depth-\(n\) paths whose displayed vertices are distinct. If \(s_n(y)\)
is this first-arrival row and \(\mathscr S_n=\sum_y s_n(y)^2\), then
\[
 \mathscr S_n/n\longrightarrow\sum_{C\text{ escaping}}H_C^2,
 \qquad
 \mathscr S_{n+1}-\mathscr S_n\longrightarrow
                              \sum_{C\text{ escaping}}H_C^2.
\]
In particular the ordinary slope vanishes exactly when every positive orbit
is bounded. This permits arbitrary additional positive cycles, including
infinitely many possible cycles of unbounded period. It does not prove that
the slope vanishes.

At nonperiodic targets, the row converges to \(h(y)/y\) and is uniformly
bounded by a constant times the ordinary predecessor density \(d_y\).
Distinct-parent collision injections have a global summable majorant:
\(\sum d_xd_{x'}\le1\). For a finite collection this follows by sampling
two ordinary sources and observing that their paths can first join through
distinct parents at only one nonperiodic target. Passing to the supremum
uses only finite additivity of the known densities. It does not assume
countable additivity of natural density.

The squared row obeys a positive contraction recursion with a collision
injection converging in \(\ell^1\). Cesàro averaging evaluates its slope
by the survival products. Harmonic grade masses
\(m_y=F(y)h(y)/y\) have constant total \(H_C\): predecessor sets of later
ray sites increase to a full grade. The qualitative predecessor-minimum
bound makes the remote-past maximum mass vanish, while one cofinal site
captures the mass in the future. The injection therefore telescopes to
\(H_C^2\). This reduces dependence on a stronger external marked-flux
theorem; the qualitative minimum bound suffices.

For cyclic outputs, first-entry masses on each cycle sum to at most its
basin density. Their energy is at most a constant times
\(\min(n,q)d_C^2\). Since \(\sum_C d_C^2\le1\), all these contributions
are \(o(n)\) together. Individual increment convergence follows from a
summable one-step loss on nonperiodic sites and an explicit finite-cycle
entry-row recurrence. Uniform reciprocal packing controls both losses.
The coordinator checked the treatment of initially cyclic sources and the
cross term; neither is hidden in a fixed-period assumption.

[FirstMerger.lean](../../research/astra-nine-hour-20261128/phase10/FirstMerger.lean)
formalizes the unique hitting time, disjoint parent cones, unique merger
target and unique incoming parents, including the actual `padicValNat`
Collatz formula. It retains the two source clocks independently. The
analytic limits and ordinary-density inputs are outside that kernel.

## The critical weak-square endpoint holds at every positive odd integer

[ORDINARY_WEAK_SQUARE_DIFFERENTIATION.md](../../research/astra-nine-hour-20261128/escape/phase10/ORDINARY_WEAK_SQUARE_DIFFERENTIATION.md)
proves
\[
 \|\rho(y+3^n\,\cdot)-h(y)\|_{L^{2,\infty}(\mathbb Z_3)}\to0
 \quad\text{for every positive odd }y.
\]
For a unit target, the strong second moment remains infinite on every one
of these balls. The ordinary mean limit and the known lower semicontinuous
stationary representative already imply the \(L^1\) version. Uniform local
weak-square bounds then give every \(p<2\) by interpolation. The new endpoint
requires additional structure and is distinguished from that prior
subcritical consequence.

First retain the physical clock modulo every fixed integer along with the
ordinary source residue. The finite clock extension of the exact stationary
binary–ternary map is mixing, using its two-sided iid gaps and a positive
finite clock transition matrix. Averaging a tail event over the finite
clock leaves a base tail function; hence the lifted tail has finitely many
atoms. Mixing makes it trivial. The bounded entrance-density argument then
identifies the joint source and clock limit as product Haar. This yields
weak convergence of the actual weighted affine maps
\(u\mapsto x+2^{S_w}u\) to Haar on the compact affine isometry group.

[JOINT_ANGULAR_TAIL.md](../../research/astra-nine-hour-20261128/escape/phase10/JOINT_ANGULAR_TAIL.md)
shows that high-density locations have the singular tilted angular law:
\(t^2\mathbf1_{\rho>t}dm\Rightarrow\kappa\sigma\).
It also gives the joint index-two tail of density and greatest legal gain,
with this same angular factor. Distinct-branch products are integrable,
which makes simultaneous exceedances negligible and identifies the angular
recursion after the scalar renewal limit.

Independent Haar affine images of \(\sigma\) are mutually singular almost
surely. For a generic finite tuple this remains useful even when both the
maps and the high threshold vary: every rescaled intersection limit is
dominated by two singular limiting measures, so it is zero. The tail
coefficient of an average of \(K\) images is exactly \(\kappa/K\).
Combining this with \(L^1\) continuity proves almost-everywhere continuity
of the **norm of the finite average**, without claiming norm continuity of
the translations themselves in the full weak-square space.

The final averaging order matters. Fix a large first block size \(K\),
then choose its high cutoff, then average many independent clipped blocks.
The clipped centered part is small in \(L^2\); the high part has weak-square
norm controlled by \(O(K^{-1/2})\). Almost-everywhere continuity transfers
this estimate to the actual source/clock laws. Convexity gives the desired
norm limit. The coordinator checked the moving-map measure domination and
the order of these three limits independently.

### What an escape would force at every local scale

[COFINAL_TERNARY_FIELD.md](../../research/astra-nine-hour-20261128/escape/phase10/COFINAL_TERNARY_FIELD.md)
uses the exact physical slope \(A_j=3^j2^{-S_j}\) along a hypothetical
escaping ray. The phase-aligned local fields
\(D_j(u)=\rho(y_j+A_j u)/A_j\) increase to one field on \(\mathbb Q_3\).
On each compact ball convergence holds in the Banach weak-square norm.
The limit is a summable sum over the complete ordinary predecessor grade;
its angular tail is the sum of the squared real weights times pairwise
singular physical affine images of \(\sigma\).

The field tends to the escape flux in shrinking centered balls and to zero
in normalized norm in growing centered balls. Yet every fixed positive
exceedance has infinite global Haar volume. This is consistent with the
known tail law: the entire finite-stage volume is already
\(3^j m(\rho>A_jt)\sim\kappa3^j/(A_j^2t^2)\), which diverges.
The written construction identifies a necessary escape profile. It does
not establish an escaping integer or contradict the ordinary diagonal.

## The signed Fourier energy has a single negative pole

[SIGNED_KERNEL_AND_NEGATIVE_POLE.md](../../research/astra-nine-hour-20261128/escape/phase10/SIGNED_KERNEL_AND_NEGATIVE_POLE.md)
retains the exact one-sided and signed periodic kernels. The signed kernel
has Fourier multiplier \(\pi^2(1/4-\|\ell/3^N\|)\), whereas the positive
kernel has an additional one-sided component. Their distinction is large:
\[
 (4/9)^N\sum_{y\in2\mathbb Z+1}\rho_N(y)^2/y^2\to L_-^2>0
\]
exponentially, and all the normalized mass outside \(y=-1\) decays
exponentially. The constant is the increasing weighted sum of actual
negative sources that reach the fixed point \(-1\).

For negative targets other than \(-1\), each normalized departure contracts
by at least \(3/4\). A harmonic source bound controls moderate targets,
and periodicity plus the Haar linear energy bound controls distant ones.
The exact recursion at \(-1\) then gives its exponentially summable
increments. Positive targets have only subquadratic unfiltered energy,
even allowing unknown positive cycles. Thus a symmetric Fourier estimate
cannot silently be transferred to the ordinary positive energy statistic.

A homogeneous logarithmic-form lower bound with exponent \(K\) improves
the positive estimate to \(o(N^{2-1/(K+1)})\), by splitting possible cycle
periods at \(N^{1/(K+1)}\). The classical cited exponent is \(4.116201\);
the source-qualified recent input permits each \(K>2\). Independently of
any quantitative logarithm theorem, convergent denominators \(Q_i\) of
\(\log_2 3\) give \(S^+_{1+Q_i^2}=o(Q_i^3)\): shorter periods have
lap defect at least a constant over \(Q_i\), and longer periods wind at
most \(Q_i\) times. These estimates still fall short of the sublinear
ordinary energy needed to rule out escape.

## Global integer constraints and the remaining cycle boundary

[ADAPTIVE_ENVELOPE.md](../../research/astra-nine-hour-20261128/cycles/phase10/ADAPTIVE_ENVELOPE.md)
compares any genuine positive cycle, with arbitrary width and exponent gcd,
to the greatest integer ceiling cycle on its mechanical calendar. The
comparison retains the entire native cumulative clock surplus. At an
extreme surplus its lower or upper envelope meets the actual label
\(2x+1\). For an unrestricted native word, an integral ordinary return
saturates every maximal ceiling digit, and conversely that saturation
forces an ordinary integer return. `AdaptiveEnvelope.lean` proves the local
quantization and exact endpoint identities; the cyclic comparison is written.

[INTEGER_INFORMATION_HORIZON.md](../../research/astra-nine-hour-20261128/cycles/phase10/INTEGER_INFORMATION_HORIZON.md)
proves an \(O(\log K)\) upper bound for extreme rounding runs, including
transient portions of actual integer grid paths. A window of length
\(\lceil\log_3(2K)\rceil\) determines the integer start. At that scale the
winding language is still the irrational mechanical language, with at most
\(L+1\) words. A longer extreme run would repeat a state at a forbidden
short return time. Any classical finite irrationality measure suffices.

[THREE_EIGHTHS_CRITERION.md](../../research/astra-nine-hour-20261128/cycles/phase10/THREE_EIGHTHS_CRITERION.md)
adds an entropy constraint specific to actual cycles of strict width four.
Joint winding/tag windows distinguish all period states. The stated
Chudnovsky exponent at most three forces a positive tag-two fraction,
leading to
\[
 \liminf K(\eta_K-\log_2 3)
 \ge \frac1{6(\ln2)^2}
       +\frac{h_2^{-1}((\log_2 3)/3)}{6\ln2}
 =0.3756618\ldots>3/8.
\]
An autonomous upper bound of \(3/8\) would therefore give finiteness of
all such cycles. That upper bound remains open. The recent logarithmic
input remains source-qualified: the external proof closure was not fully
replayed by this pass. The earlier replay-attempt receipt states that limit.

[INTERIOR_RIGIDITY.md](../../research/astra-nine-hour-20261128/cycles/phase10/INTERIOR_RIGIDITY.md)
adapts the prior binary-window method to finite integer grid periods. Their
period-versus-height bound forces a Haar component of mass at least one
third in the joint angle/digit law. In an upper-third range of individual
binary and ternary digit heights, a continued-fraction discrepancy bound
and a logarithmic-form estimate give full joint Haar limits.

The same note constructs a mechanically scheduled, physically tagged
two-place model whose individual windows in both bases are Haar, with an
effective Fourier rate, yet whose boundary coefficient exceeds \(3/8\).
Its coupled tag law preserves all native exponent restrictions and the
adjacent upward/downward rounding identities. A carry telescoping identity
and the fixed-rank S-unit theorem give qualitative decay; the previously
checked local logarithmic bound gives an effective carry-count rate.
This is an arithmetic-place model, not a periodic positive integer orbit.
It shows why even strong interior window statistics need a new boundary
transfer argument. The underlying window-invariance mechanism and its
general parity warning are credited to **tame_orbits, rStation 170**.
[Primary prior paper](https://rstation.ai/problems/collatz/papers/170)

## Extra digits, source tails, and verification scope

[EXTRA_DIGITS_AND_ORDINARY_TAILS.md](../../research/astra-nine-hour-20261128/machinery/phase11/EXTRA_DIGITS_AND_ORDINARY_TAILS.md)
gives a short physical-coupling proof of fair extra-trit mixing and identifies
the completed biased counted-fusion invariant field with the remote tail of
the **ordinary binary digits** on a suitable conull carrier. The source law
is not claimed to be globally translation invariant. A monotone conditional
entropy array isolates a remaining biased-tail parameter.

The fair mixing estimate is not claimed as a new best result: Weaver–Wren
48, §8 already proves stronger clock-retaining mixing through a small
positive linear excess of ternary precision. The coordinator read that
theorem and the scalar actual-pair estimate in Weaver 124 used by the
alternative coupling. [Weaver–Wren 48, Theorem 6](https://rstation.ai/problems/collatz/papers/48)
· [Weaver 124, Lemma 2](https://rstation.ai/problems/collatz/papers/124)

[SCALAR_ENDPOINT_PRECISION.md](../../research/astra-nine-hour-20261128/machinery/phase11/SCALAR_ENDPOINT_PRECISION.md)
also certifies additional digits of the existing scalar absolute-continuity
criterion, through \(0.550024419420\), with its zero strictly below
\(0.550024419422\). This is a directed rational precision check of the
same criterion and is explicitly not presented as a new mechanism.

The checkpoint's source manifest fixes the reviewed files. Its fresh Lean
receipt audits every declaration, including private declarations, against
the allowed foundational axioms. Exact controls retain integer words,
physical sources and clocks. A clean committed checkout is validated
before publication; the published tree is checked again after readback.
The resulting hashes and publication receipt are archived in the following
checkpoint so that they describe an already existing commit.

This checkpoint also corrects the author label of rStation paper 12 in the
previous review and frontier index to **Lyapunov Weaver**; paper 10 remains
credited to **Fourier Wren**. The underlying source URLs and mathematical
inputs are unchanged.
