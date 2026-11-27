# Strict survivor exponents, sixfold occupation, and joint arrival clocks

**PROPOSED research; Collatz remains open.** This checkpoint strengthens
three ordinary-integer statements. It separates the written asymptotic
arguments from the finite arithmetic proved in Lean or replayed exactly.

## A fixed gain below two critical survivor entropies

Let `α=log₂3`, `p*=1/α`, and put

\[
 \beta_D=(2p_*-1)/(1-p_*),\quad
 h_D=H_2(\beta_D)/(2+\beta_D)=0.3208518\ldots,
 \qquad h_5=H_2(\alpha-1)/\alpha=0.6177244\ldots.
\]

For every interval `I` of length `X≥2`, the
[strict survivor bounds](cycles/phase6/README.md) give

\[
 \#(I\cap S_D)=O(X^{h_D-10^{-12}}),\qquad
 \#(I\cap S_5)=O(X^{h_5-10^{-12}}).
\]

Here `S_D` consists of odd integers whose entire forward odd orbit
avoids both `5,7 mod8`. The set `S_5` consists of odd states with a
bi-infinite positive ordinary history whose odd-step division exponents
are always one or two. The latter premise includes the relevant cycles;
it does not cover all one-sided avoid-five starts. The constants and
onsets are ineffective because the proofs use the fixed-place Subspace
Theorem. The numerical gain is specified independently of that onset.

The main step retains the canonical residue of the actual integer source.
A dimer word of physical length `T`, with `u` odd letters and affine
numerator `C`, has source residue `[-3^(-u)C] mod2^T`. At shallow linear
precision, the normalized canonical residue has an upper concentration
bound of any fixed dimension below one. Its counterpart for the backward
two-gap history is the canonical endpoint modulo `3^u`.

The proof first controls signed sums of independent finite-state word
numerators. A random block choice supplies fresh parity randomness at
the branching states. Taking enough independent copies ensures adequate
activity after a fixed mixing time. The argument bounds low activity
before conditioning on any prescribed sum bits. It then pays the exact
composition-conditioning cost. For a chunk of the actual word, the
exterior powers of two and three remain in its circle contribution.
The Subspace Theorem turns a sufficiently close signed sum into an exact
numerator equality, and Fourier Hölder combines the chunk laws.

Reading a slightly longer word than the logarithm of the interval width
makes the allowed source arc small. Near the critical composition this
improves the raw word entropy. Lower odd counts map the same survivor set
into shorter translated intervals; fixed-time injectivity closes the
induction. The backward argument uses actual positive predecessor
histories and deterministic forward recovery of their targets.

[MarkovCertificate.lean](cycles/phase6/MarkovCertificate.lean) proves
four finite declarations with no axioms in their printed inventories.
Its exact four-copy row potentials give contraction factors `37/50`
and `14/25`. The written [parameter calculation](cycles/phase6/EXPLICIT_GAIN.md)
uses these to justify the common gain `10^(-12)`. The finite certificates
do not formalize the analytic concentration theorem. Weaver 28 and 73
are credited for the source-residue, signed-moment, and arithmetic
separation architecture.

The improved exponent is positive. These counts therefore leave room
for an isolated nonconvergent trajectory or a nontrivial cycle.

## A smaller merger or positive occupation above a sixfold band

Use the shortcut map `T(2z)=z`, `T(2z+1)=3z+2`. A smaller merger through
clock `m` means that some state `T^i(X)`, `i≤m`, is visited by a positive
source below `X`, at any visitor clock. Set

\[
                         \theta=4999/15000<1/3.
\]

The [sixfold occupation theorem](descent/postpeak/sixfold/SIXFOLD.md)
states that, for every fixed `β>θ`, there is a positive `c_β` such that
every sufficiently large `X` and every `m≥X^β` have a smaller merger
through `m`, or at least `c_β m` of their first `m` departures above `6X`.
The same conclusion holds, with another positive fraction, above some
fixed radius `R_β X` with `R_β>6`.

When `θ<β<1/3`, a merger or first exit from `[X,6X]` occurs by
`ceil(X^β)`. If no strictly earlier merger occurs, the physical exit's
clock and direction agree with the homogeneous coefficient path
`3^(odd count)/2^(clock)`. An analogous comparison holds at a suitable
fixed radius `R_β=2^(k/l)>6`.

The finite calculation uses all 446 previously retained native merger
factors. [NativeFamily.lean](descent/postpeak/sixfold/NativeFamily.lean)
proves the generic ordinary affine-family consumer, and
[MotifBank.lean](descent/postpeak/sixfold/MotifBank.lean) checks all rows
inside the kernel. Every positive native lift supplies a positive lower
visitor `m` with `6m` strictly below its recorded reference state. Thus
an occurrence with reference state at most `6X` yields `m<X`.

For the global count, mechanical supports have length two or three.
At each support the unordered pair of zero slots is determined by a
four-copy numerator congruence. The exact verifier maintains the
last-even flags across cells and applies a second-order Bonferroni
upper bound to forbidden factors. Its three flag classes retain their
correct multiplicities. It checks all 61 phase types for a cell of
60 supports and all 1441 phase types for a block of 1440 supports.
For every block, its integer energy `E` and physical length `T` satisfy

\[
                  16E^5<2^{5T},\qquad T\le4000,
\]

which gives the uniform rate cap `4999/5000`.

Sparse excursions above the band are charged by recording their
containing blocks and neighbors. The remaining product families retain
the energy bound, with an error tending to zero as the exceptional
fraction shrinks. Weaver 181's located-window method and the cited
fixed-place Subspace Theorem give `O(X^(θ+ε))` eligible band sources.
An incidence count converts this to positive occupation. The separately
quoted estimate `μ(log2/log3)≤3` controls repeated cycles and the
physical-versus-homogeneous boundary comparison. Those external analytic
inputs are not part of the Lean replay.

This result allows upward escape. It supplies no mechanism that makes
an orbit return below its original source after such an escape.

## The joint clock scale in short ordinary intervals

Let `A⊂[1,M]` be any set of targets. Record the first landing site, the
shortcut time `τ`, and the odd count `p`; retain nonarrival as its own
mark. For an interval `I=[x,2^ρx)` inside `[X,2X)`, define

\[
 L=\min\{\log_2(X/M),\log_2(X\rho)\},\quad W=\sqrt L,
 \qquad 0<\rho\le1.
\]

The [short-window theorem](rigidity/phase7/SHORT_WINDOW_CLOCKS.md)
compares the actual distribution of `(landing,τ modm,p modm)` with
uniform residue pairs on each row, preserving the full landing marginal
and nonarrival. For every continued-fraction denominator `q` of `log₂3`,

\[
 d_{\rm TV}\ll mq/W+m/(\rho q).
\]

The constant is uniform in the target set, number of landing labels,
window position, and modulus. If consecutive convergent denominators
obey `Q≤sqrt(W/ρ)<Q'`, put

\[
                    H(W,\rho)=\max\{1,\rho Q,W/Q'\}.
\]

The upper bound is `O(min(1,m/H))`. For a matching ordinary first-passage
example, take the full target floor `M=floor(X^γ)` with
`log₂3/2<γ<1`, and windows no smaller than an inverse power of `log X`.
Then `m/H→∞` forces total variation to tend to one. This lower bound
uses the ordinary parity bijection and elementary concentration within
its genuine digit budget; it does not assume a local central limit
theorem. Continued-fraction gaps remain part of the all-scale answer.

The upper proof lifts the two edge comparisons to a rotation on a
circle of circumference `m`, together with a second residue coordinate.
Counted coalescence controls translation errors, and the nearly regular
convergent grid controls the averaging error. The sharpness proof
projects `(τ,p)` onto the primitive direction `Qτ−Pp`. The true pairs
lie in a short row-dependent window, while uniform pairs have equal
fibers. [ClockResidues.lean](rigidity/phase7/ClockResidues.lean) proves
that exact finite coordinate change and its fiber count.

With Weaver 124's growing-block coalescence and the separately sourced
positive lower density of predecessors of a fixed odd ternary-unit
target, the note also counts common blocks in short intervals at any
prescribed clock-residue pair. Its assumptions are
`m^3=o(H)` and `m^2(1+log D)^4=o(W)` for block length `D`.
The target's future and the nonarrival mass remain unresolved.

## Evidence and review boundary

The [sixth evidence archive](../../reports/astra-reciprocal-rigidity-20261127/checkpoint6/README.md)
records fresh Lean builds, exact Python and GMP runs, source manifests,
and clean repository checks. The root reconstructed the written
concentration, oversampling, sparse-window, and short-clock proofs.
The rigidity lane independently reviewed the cycle arguments and their
explicit exponent margins. Finite replays certify their declared finite
identities and inequalities, with no assertion of a full formal Collatz
proof.

This checkpoint also records a source-only attribution correction to
the fifth: Paper 186 already gives a much smaller aggregate avoid-seven
and dimer gap bound using its special `2^129` avoidance verification,
and Paper 217 already aggregates all additional cycle gaps. The earlier
four-language calculation at the general `2^71` floor remains valid,
with its numerical and historical scope now stated explicitly.
