# A uniform finite occupation bound for ordinary Collatz prefixes

This attack strengthens the phase and temporal-frequency route for
ordinary Collatz orbits with an odd starting integer. It gives a finite
estimate whose constants and observation horizon do not depend on that
starting integer. It does not assume an escape rate, a distribution of
starting integers, or the analytic predecessor-density input of PR180.

The new observation is elementary but useful: a prefix of `N` distinct
positive integer states has reciprocal sum at most the harmonic number
`H_N`. Substituting this exact extremal bound into the actual Collatz
Fourier telescope changes its finite error budget from the square-root
bound available through a free cutoff to a logarithmic bound. Elementary
separation of the integer powers of two and three then makes the
frequency dependence explicit. The nonnegative character kernel from
PR178 transfers this to a uniform finite marked-visit estimate.

## Frozen inputs and provenance

The three vendored source files are copied byte for byte from PR178 at
commit `0bb13b800e4e97f9fd3091b1a3d2e98b49911b7c`:

| Module | SHA256 |
| --- | --- |
| `vendor-pr178/ReturnFourier.lean` | `a758b7b8c6b1827a5f96eb8ae32196c0145a0280229b6fa22bf899c3cd348ed3` |
| `vendor-pr178/MarkPhase.lean` | `bd4cc9ef10cbaa91b8d8a8ea83f1d9dfbbf644d0235ceff77452c18abdf199d9` |
| `vendor-pr178/MarkFrequency.lean` | `7786fd2c3eccecf8dedb931233c9ae1da059a8d883fb1e8250304b6c4df84921` |

Their dependency `ForwardSection` is the existing PR173 frozen source at
`fa0c9e2a2851e6324391e39c17afcb5913185aec`. The present packet already pins
and replays that source. These files are attributed inputs; their
theorems are not presented as new work here.

The occupation/source-mass analysis also inspected these exact revisions:

- [PR176](https://github.com/GettysburgResearch/collatz/pull/176),
  `3dbe5542fd6a5a1d63b354225d92391471c17002`: finite marked-ancestor fans,
  survivor certificates, and conservation of transported source weights.
- [PR178](https://github.com/GettysburgResearch/collatz/pull/178),
  `0bb13b800e4e97f9fd3091b1a3d2e98b49911b7c`: finite actual Fourier
  control, qualitative zero marked temporal density, and the obstruction
  to deriving low-bit independence from a uniform phase marginal.
- [PR180](https://github.com/GettysburgResearch/collatz/pull/180),
  `9010a8790535002b6d9ff92304f0ba289e2e98fe`: analytic marked-ancestor
  populations, the source-qualified predecessor-density input, and its
  conditional reciprocal-summability consequence.

## Definitions and scope

Write

\[
x_j=\operatorname{oddOrbit}(n,j),\qquad
\alpha=\log_2 3,\qquad h(x)=\log_2 x,
\]

and

\[
\chi_k(u)=e^{2\pi i k u}.
\]

The hypothesis in every new finite orbit estimate is

\[
n>0,\qquad x_i\ne x_j\quad(0\le i<j<N).
\]

The Lean algebraic statements allow any positive `n`, because the map
`oddStep x = oddPart(3*x+1)` is defined on every natural number. For even
`n` this first step is not the ordinary Collatz acceleration. To apply
the statements to an ordinary even source, first remove its powers of
two and use that odd starting state.

The endpoint `x_N` is not required to be different from the observed
states. The estimates therefore apply up to the first repeat, including
one whole nontrivial cycle if such a cycle exists. They also apply to
finite prefixes of convergent trajectories. For an ordinary odd source,
the orbit is the standard accelerated odd Collatz orbit; no 2-adic source
or changing-source limit enters the argument.

The marked set is the existing PR173 set `Marked`, with integer band
constant 70. In particular a marked state `x` satisfies

\[
0\le h(x)-\lfloor\log_2 x\rfloor
 \le\frac{140}{\lfloor\log_2 x\rfloor+1}.
\]

Let `V(n,N)` count marked states among `x_0,...,x_(N-1)`. This is the
vendored definition `MarkFrequency.markedVisits`.

## AC1. Exact finite harmonic budget

`reciprocal_set_harmonic` proves, for every finite set `S` of positive
integers,

\[
\sum_{x\in S}\frac1x\le H_{|S|}.
\]

The proof inducts by adjoining the largest element `a`. Positivity and
distinctness imply `|S|+1 <= a`, because the enlarged set lies in
`{1,...,a}`. Thus its new reciprocal contributes at most
`1/(|S|+1)`, precisely the increment of the harmonic number. There is no
asymptotic estimate or unspecified constant in this step.

Applying this to the image of the injective prefix gives

\[
\sum_{j<N}\frac1{x_j}\le H_N\le 1+\log N.
\tag{AC1}
\]

The Lean theorems are `odd_prefix_reciprocal_harmonic` and
`odd_prefix_reciprocal_log`. The logarithm on the right is natural.
The `N=0` case is included under Lean's standard convention `log 0=0`.

Before taking phases modulo one, `odd_prefix_log_cocycle_harmonic`
retains the full valuation identity:

\[
h(x_N)=h(n)+N\alpha-\sum_{j<N}v_2(3x_j+1)+E_N,
\qquad 0\le E_N\le H_N.
\]

Thus the logarithmic error bound also applies to the actual integer
halving cocycle. It does not replace that cocycle by its random-start
average.

The finite consequence `odd_prefix_valuation_bound` is especially useful
for a putative least counterexample: if `x_N>=n`, then

\[
\sum_{j<N}v_2(3x_j+1)\le N\alpha+H_N.
\]

The earlier checked inequality `lowBits(x)<=v_2(3*x+1)` therefore gives
the same upper bound for the truncated valuation sum on these prefixes.
Thus any claimed low-bit lower bound exceeding this explicit budget
would force descent; that lower bound is not supplied by phase occupation.

## AC2. Explicit Fourier budget, uniformly in the ordinary source

PR178 proves the actual-state telescope

\[
|1-\chi_k(\alpha)|
\left|\sum_{j<N}\chi_k(h(x_j))\right|
\le 2+4\pi k\sum_{j<N}\frac1{x_j}.
\]

`odd_prefix_fourier_harmonic` substitutes (AC1). To remove the implicit
small divisor, choose the nearest nonnegative integer

\[
a=\lfloor k\alpha+1/2\rfloor,\quad d=k\alpha-a,
\quad |d|\le1/2.
\]

The existing elementary `grid_barrier` gives

\[
|d|>\frac1{4^k+1}\qquad(k>0).
\]

The chord estimate

\[
|1-e^{2\pi i d}|=2|\sin(\pi d)|\ge4|d|
\]

therefore yields the deliberately weaker convenient bound

\[
1\le(4^k+1)|1-\chi_k(\alpha)|.
\tag{AC2a}
\]

This is `character_gap_budget`. It uses neither a numerical irrationality
certificate nor a transcendence theorem.

Define the explicit nonnegative budget

\[
F(K,N)=(4^K+1)(2+4\pi K H_N).
\]

`odd_prefix_fourier_explicit` proves simultaneously for every `0<k<=K`

\[
\left|\sum_{j<N}\chi_k(h(x_j))\right|\le F(K,N).
\tag{AC2b}
\]

In particular `odd_prefix_fourier_log` proves

\[
\left|\frac1N\sum_{j<N}\chi_k(h(x_j))\right|
\le\frac{(4^k+1)(2+4\pi k(1+\log N))}{N}
\qquad(N>0).
\tag{AC2c}
\]

For each fixed frequency this is an explicit `O_k(log N/N)` estimate
on every distinct finite ordinary prefix. Unlike a statement restricted
to a hypothetical infinite divergent orbit, the estimate can be applied
before one knows the future behavior of the source.

## AC3. Uniform finite marked-occupation inequality

PR178's nonnegative kernel is

\[
\mathcal K_K(u)=\left|\sum_{r=0}^{K-1}\chi_r(u)\right|^2.
\]

Its finite expansion and (AC2b) give

\[
\sum_{j<N}\mathcal K_K(h(x_j))
\le KN+K^2 F(K,N).
\tag{AC3a}
\]

For a marked state with `x>=2^B`, if

\[
1120\pi K\le B+1,
\tag{AC3b}
\]

every character in the kernel lies within distance `1/2` of 1, and
therefore

\[
K^2\le4\mathcal K_K(h(x)).
\]

There are at most `2^B` exceptional states with `x_j<2^B`, since the
observed values are distinct. This counts small *values*, wherever they
occur in the prefix. It does not assume the orbit increases, and does
not introduce a source-dependent time after which all states are large.

The Lean theorem `marked_visits_finite_bound` combines these estimates:

\[
\boxed{
K^2V(n,N)\le K^2 2^B+4KN+4K^2F(K,N)
}
\tag{AC3c}
\]

for every `B,K` satisfying (AC3b). The `K=0` case is a valid degenerate
inequality. For `K>0` one can divide by `K^2` and choose both parameters
from `N`, independently of `n`.

The companion `TemporalDensity.lean` selects explicit integer parameters
to obtain the all-horizon bound

\[
\boxed{(\lfloor\log_2N\rfloor+1)V(n,N)\le196608N.}
\tag{AC3d}
\]

The code uses `Nat.log2 N`, including its value zero at `N=0`. For the
nontrivial parameter branch it takes `K = Nat.log2 N / 16384` and
`B = 8192*K`. The small `K=0` branch follows from `V(n,N)<=N`.
The constants are deliberately loose. The companion theorem
`marked_visits_logarithmic_finite` explicitly requires an odd source and
distinctness of just the `N` observed states. Its verification receipt is
recorded with the packet's other final checks.

## A concrete obstruction at the first marked hit

The theorem `first_marked_offset_above_source` checks the following
diagnostic by exact natural-number reduction. Take the
ordinary odd source

\[
n=2^{601}-1.
\]

Its first eight odd states are

\[
x_j=3^j2^{601-j}-1\qquad(0\le j\le7).
\]

Every transition here is the actual shortcut step `(3*x+1)/2`, and the
states remain odd. The first marked state is `x_7`. Indeed,

\[
x_7=2^{605}+r,\qquad r=139\cdot2^{594}-1,
\]

and its mark test follows from

\[
606(139\cdot2^{594}-1)
 <84234\cdot2^{594}
 <143360\cdot2^{594}=70\cdot2^{605}.
\]

For completeness, the preceding failures can be checked without a
floating-point logarithm. Write `h_j=floor(log2(x_j))` and factor each
test margin as

\[
(h_j+1)(x_j-2^{h_j})-70\,2^{h_j}
=\Delta_j2^{b_j}-(h_j+1).
\]

| `j` | `b_j` | `h_j` | `Delta_j` |
| --- | --- | --- | --- |
| 0 | 600 | 600 | 531 |
| 1 | 600 | 601 | 462 |
| 2 | 599 | 602 | 43 |
| 3 | 598 | 602 | 5513 |
| 4 | 597 | 603 | 5788 |
| 5 | 596 | 603 | 60500 |
| 6 | 595 | 604 | 95445 |

All seven margins are strictly positive. Yet at the first marked hit,

\[
r-n=11\cdot2^{594}>0.
\]

Thus the offset of even the *first* forced marked state need not be a
smaller source than the original integer. Ordinary induction on `n`
cannot supply an offset certificate merely because that first mark has
been reached. This example concerns failure of that proposed induction
step; it asserts nothing about nonconvergence of its source.

## What this does and does not close

The bound is unconditional for each distinct finite positive prefix.
Combined with forced-band recurrence, it says that any hypothetical
infinite nonperiodic ordinary orbit has infinitely many marked visits
whose finite counts satisfy the same explicit uniform upper bound. This
quantifies the earlier qualitative zero-density conclusion; it does not
contradict recurrence.

It also constrains a hypothetical nontrivial ordinary cycle by applying
the finite bound to its distinct period. It does not exclude all such
cycles. Repeating that period many times would violate finite-prefix
injectivity, so this argument cannot silently apply the same harmonic
budget to arbitrarily long repetitions.

The remaining source-mass obstacle is precise. PR176's survivor
certificate needs an upper bound on the *number of starting states* in a
marked population that survive to a common ordinary deadline. Equations
(AC1)--(AC3) bound the *times* at which each fixed trajectory is marked.
They give no bound on how many independent sources survive. A fixed
positive source atom can retain all its transported mass while visiting
the section sparsely. Conservation of source weights remains compatible
with the new finite occupation inequality.

The target-dependent successful octaves in PR180 are also material.
One cannot promote them to a common octave for arbitrarily many targets
without another estimate. At one octave there are only the available
marked sources, and each source has only `O(d)` possible endpoints within
an `O(d)` clock. Summing a lower fan count over many targets must respect
that elementary incidence bound. The new temporal estimate does not
supply the missing synchronization of target-dependent successful scales.

Likewise, the phase equation removes the integer valuation cocycle
modulo 1. Its near-uniform phase occupation does not by itself force the
low-bit residue distribution required for negative average height drift.
PR178's circle-Haar times 2-adic `-1` model witnesses that these marginal
conditions can coexist abstractly. That model is not an ordinary positive
integer counterexample, and its finite ordinary shadows do not provide
one. Excluding the required fixed-source ordinary coupling is still an
unproved step.

The explicit frequency dependence also prevents a hidden exchange of
scales. Our useful common Fourier range grows only logarithmically with
the observation horizon. Within a fixed dyadic octave of height `d`, a
low-bit residue test oscillates in the leading logarithmic phase on a
scale of order `2^(-d)`. Fixed-frequency phase equidistribution therefore
does not resolve those residue tests as the state height increases. The
new quantitative bound supplies no estimate at the required changing
frequencies.

No global source-survivor bound, universal negative drift, or complete
Collatz proof is claimed by this packet.
