# Uniform translated packing on the actual moving inverse law

**Status: PROPOSED written theorems. Escape remains OPEN.** The estimates are
uniform in the height of an interval and in the inverse clock. The moving-law
application uses the previously source-qualified ordinary harmonic kernel.
The counting theorem uses integer dynamics, binomial estimates and real inequalities. The origin-centered
sparsity and reciprocal summability of a single orbit have prior art, including
the Garcia–Tal work discussed in
[ORBIT_MELLIN](../astra-three-routes/pass2/ORBIT_MELLIN.md).
Here we count all translated intervals and allow arbitrary transversals of
the exact inverse fibers. No priority claim is made for the origin bound.

## 1. Uniform local packing for arbitrary synchronously distinct odd cores

Let T(n)=n/2 for even n and (3n+1)/2 for odd n. Let u(n) be the odd
part of n and U(n)=u(3n+1) on positive odd integers. Call a set S of
positive integers admissible here if, for each t≥0, the map
n ↦ U^t(u(n)) is injective on S. There is no invariance or common
height assumption on S. Put

    a = log(2)/log(3),    θ = H₂(a) = 0.949955527188... ,

where H₂ is binary entropy. For every d with θ<d<1 there is a constant
C_d, independent of the set and of the translation, such that

    |S ∩ [M,M+L)| ≤ C_d L^d       (all integers M≥0, L≥1).        (1)

In particular this applies to the odd values of any injective ordinary
trajectory. The full shortcut trajectory can contain two points with the
same odd part. For that separate case, the proof below instead takes the
supremum over subsets of injective full shortcut trajectories; the
fixed-time images remain in such a trajectory and are distinct.

**Proof.** Write k=floor(log₂ L). For each n let p count odd states in
its first k shortcut steps. Unrolling these steps gives

    2^k T^k(n) = 3^p n + b,          0 ≤ b ≤ 3^k − 2^k.           (2)

Indeed the next numerator correction is b for an even step and 3b+2^k
for an odd step. The first k parities biject the residue classes modulo
2^k with binary words of length k. To see this by induction, the two
lifts differing by 2^k share the first k parities and their k-th images
differ by the odd integer 3^p, so they have opposite next parities.

Choose 1/2<t<a so close to a that H₂(t)<d. At most
2·2^{k H₂(t)} sources in the interval have p>tk. Each parity cylinder
has at most two representatives because L<2^{k+1}, and the binomial
tail count is bounded by 2^{kH₂(t)} (assign Bernoulli-t weights to
the words: each with p>tk has weight at least 2^{-kH₂(t)}).

For each remaining p, (2) places all images in one translated interval,
with real left endpoint 3^p M/2^k and real width at most

    3^p L/2^k + (3/2)^k ≤ 2L^{t log₂3} + L^{log₂(3/2)}.

The translation contributes no error proportional to M. The image map
on this p-class is injective and its image is admissible, because

    u(T^k(n)) = U^p(u(n)).

This identity follows at each even step by stripping a two, and at each
odd step by taking the odd core of 3n+1. Consequently for any s≥0 the
image odd cores after s further odd steps are the original cores after
p+s steps.

Let B(L) be the supremum of the left side of (1) over all admissible
sets and all nonnegative integer translations. For k≥1 and
g=max(t log₂3, log₂(3/2))<1, taking integer endpoints and using the k+1
possible weights gives

    B(L) ≤ 2L^{H₂(t)} + (k+1) B(ceil(3L^g)+2).                   (3)

For large L the new length is less than L. Choose L₀ so that for all
L>L₀ the first term is ≤L^d/2 and
(k+1)(ceil(3L^g)+2)^d ≤ L^d/2. These conditions hold because
H₂(t)<d and gd<d. Choose C_d≥1 to cover L≤L₀ by the trivial count L.
Strong induction gives (1). This proves the strict-exponent statement;
it does not assert the endpoint exponent with a constant. ∎

### 1a. Finite synchronized merging, uniformly in the starting height

For d>θ there are constants K_d and C_d such that for *every* translated
integer interval I of length L≥1,

    |{U^R(u(n)): n∈I, n≥1}| ≤ C_d L^d,
    R = ceil(K_d log₂(2L)).                                        (1a)

The same estimate holds at every later common odd clock. In particular
there are at least L^{1−d}/C_d members of any interval of L positive
integers whose odd parts reach one common odd state by this clock.

To prove this, in (3) choose g' with g<g'<1. For sufficiently large L,
L'=ceil(3L^g)+2 satisfies log₂(2L')≤g' log₂(2L). Choose
K_d≥1/(1−g'). A set on which the terminal map U^R∘u is injective
remains injective at every earlier odd clock. Inside a class with p
odd steps its image under T^k has distinct outputs at the residual
clock R−p, because u(T^k n)=U^p(u(n)). Moreover
R−p≥ceil(K_d log₂(2L')). Thus the induction proving (3) and (1)
works for this finite-clock property, using the trivial base bound.
Select one representative per distinct terminal output to prove (1a).

### 1b. The critical exponent and its square-root logarithmic gain

For an absolute constant C, including all admissible sets, there is a
stronger uniform estimate

    |S ∩ [M,M+L)| ≤ C G(L),     G(L)=L^θ/sqrt(log(2L)).           (1b)

It counts total visits even when huge excursions separate successive
visits. Prior PR185, Theorem 4 in the collision note cited below,
gives the same power and logarithmic factor for a segment entirely
below a height bound. Its last paragraph distinguishes that conclusion
from counting total visits. The translation and arbitrary admissible
sets here are essential to the following induction. The sharp total
origin-centered bound for one actual orbit was already proved in PR182
at `a7fd3ac9e5bff7412858df23d776bb847e9c1371`,
`research/whole-repo-round3-20261123/GLOBAL_ORBIT_COUNT.md`, equation (1).
Our strengthening covers all translations and arbitrary transversals and
has a common finite synchronization clock independent of the translation.

Put b=log₂(3/2)<1. Choose an integer D>0, fixed independently of L,
and restrict typical weights to p≤p₀=floor(ak)−D. The exceptional
parity words number at most C_D 2^{kθ}/sqrt(k) for large k. Indeed the
first binomial coefficient at p₀+1 is bounded by this expression by
Stirling, since (p₀+1)/k=a+O_D(1/k) and H₂ is differentiable at a.
The ratio of successive coefficients is (k−p)/(p+1), uniformly
bounded below 1 on this upper tail since a>1/2. Each word contains
at most two sources in an interval of length L. This contributes at
most A_D G(L).

Use the upper interval lengths L_p=ceil(2·3^p+(3/2)^k)+2, separately
for every p≤p₀. The real image width in (2) is less than L_p.
All log(2L_p)≥c log(2L) with absolute c>0 for large L, because
L_p≥(3/2)^k. Concavity of x^θ and summing a geometric series give

    Σ_{p≤p₀} L_p^θ ≤ C₁ 3^{−θD} L^θ + C₂(k+1)(L^b+3)^θ.

Here the sum only uses nonnegative p, and C₁,C₂ do not depend on D.
Choose D large enough that c^{-1/2}C₁ 3^{−θD}<1/4. Increasing D if
needed, every L_p≤L/2 for sufficiently large L. The second term is
o(L^θ), so eventually Σ_p G(L_p)≤G(L)/2. The exact recursion is

    B(L) ≤ A_D G(L) + Σ_{p≤p₀} B(L_p).

Strong induction gives (1b) with C≥2A_D covering the finitely many
smaller L. This logarithmic gain is an upper bound; we do not assert
that any orbit attains it.

There is a finite-clock version of (1b). The estimate on the number of
distinct U^R(u(n)) in (1a) holds with right side C G(L) and
R=ceil(K (log₂(2L))²) for an absolute K. For each L_p≤L/2 the loss
in squared logarithms is at least 2 log₂(2L)−1, while the class
spends only p≤k odd steps. The residual-clock induction above applies
verbatim, enlarging the finite base range. This proves a height-independent
ordinary synchronization bound at the critical exponent.

**Smaller partners and the induction boundary.** Keep the smallest source
in each terminal fiber of the interval. Every other positive source in
that interval has a strictly smaller positive partner in the same interval
whose odd core reaches the same endpoint at the displayed common odd
clock. Thus at most C G(L) fail this finite certificate. The corresponding
shortcut clocks exist and can differ, because stripping twos and individual
odd returns consume differing numbers of shortcut steps.

The exact checker supplies height-uniform numerical versions, with no
unknown asymptotic constant. For k shortcut steps use signatures
(p,T^k(n)). For any source lift by 2^k h the signature becomes
(p,T^k(n)+3^p h), by (2) and parity periodicity. Thus equal signatures
remain equal for all translations with that residue, and imply equal
ordinary odd-core outputs at common odd clock k. A sliding window
enumerates all start residues from 1 through 2^k.

| Common odd clock k | Positive interval length | Upper bound on distinct outputs | Guaranteed sources with smaller partners |
|---:|---:|---:|---:|
| 8 | 256 | 130 | 126 |
| 12 | 4,096 | 1,540 | 2,556 |
| 16 | 65,536 | 19,283 | 46,253 |

These are finite-computation certificates uniform in starting height.
The output column is the maximum number of distinct signatures; further
mergers can occur. Reproduce with `python -B escape_check.py`.

Sliding or enlarging intervals need not remove their fiber minima.
For a direct logical check, consider the separate positive-integer map
f(n)=1 on odds and f(n)=2^{1+v₂(n)} on evens. Its one-step image of
*any* interval of L consecutive positive integers has at most
floor(log₂ L)+3 points: at most one input is a multiple of the first
power of two greater than L. Nevertheless 1 is fixed and 2 escapes
through the powers of two, with no smaller merging partner.
This map tests only the inference from the interval-count bound.
The open Collatz step is a physical certificate for every possible
least nonconvergent source among the surviving fiber minima.

## 2. All-modulus inverse-distance estimate at the ordinary source

For Q≥2, z an integer and S admissible, define

    W_Q(S,z) = Σ_{x∈S, x≠z, x≡z mod Q} |x−z|^{-1}.

For an absolute constant C (one can fix any d in (θ,1)),

    sup_{S,z} W_Q(S,z) ≤ C log(2Q)/Q.                             (4)

Indeed the number at distance at most R is zero below Q and otherwise
at most min(2R/Q, C'_d R^d), by spacing and (1). Integrate this count
against dR/R². Up to R₀=Q^{1/(1−d)} the first bound contributes at
most 2 log(R₀/Q)/Q, and above R₀ the second contributes at most
C'_d/((1−d)Q). The proof includes unbounded S by nonnegative summation.
It also handles centers outside S. This is discrete counting dimension
at unit resolution. No box-covering estimate after rescaling is used.

## 3. The same original law, uniformly in every inverse clock

Fix one injective positive odd orbit q_j=U^j(q₀). Let N=M+1. At depth r,
take any probability measures μ_j supported on the ordinary fibers
U^{-r}(q_{j+r}), 0≤j≤M, and put ζ=N^{-1}Σ_j μ_j.
This includes the exact inverse laws of PR185, with any killing and
unit-domain restriction of that source. Their supporting fibers are
disjoint. No weight regularity or comparison constant is assumed.

Choose independently one x_j from each μ_j. Every resulting transversal
is admissible: a merger after t≤r would merge its distinct depth-r
targets. At t>r, its images are q_{j+t}, again distinct. Consequently,
by averaging (1) and (4),

    ζ([M',M'+L)) ≤ C_d L^d/N,
    sup_z Σ_{x≠z, Q|(x−z)} ζ(x)/|x−z| ≤ C log(2Q)/(NQ).           (5)

In fact (4) controls the sum over j of the *largest* kernel value
available in its fiber, still by C log(2Q)/Q, since one can select a
maximizer in each nonempty congruent subset. The same selection works
in entire synchronous equivalence classes, where x and y are equivalent
if their odd cores merge after the same finite number of odd steps.
Representatives from different classes are automatically admissible.
Thus (1b) also bounds the number of distinct such classes represented
in any translated interval. Equation (1a) gives a finite merger clock.

Here averaging is an integration device for the *given* μ_j. The
result concerns their exact mixture, regardless of how far r exceeds
M. Equation (5) even applies to all admissible inverse selectors
individually. It is not a total-variation approximation.

For X,Y independent with law ζ let B be the event X≠Y and Q|(X−Y).
Writing C_off=Pr(B), define H_Q by

    H_Q = 1 / E[1/|X−Y| given B]      when C_off>0.

The exact unweighted-to-weighted interface obtained by integrating (5)
over Y is

    C_off / H_Q ≤ C log(2Q)/(NQ).                                  (6)

The diagonal mass is at most 1/N since the fibers are disjoint and
each contributes mass 1/N. In the notation of the previous packet,
the critical lower bound on the *same* law is, for large fixed m and
Q=3^m, liminf_{M→∞} inf_r Col_m(ζ_{M,r}) ≥ c sqrt(m) Q^{-θ}
for the specified canonical harmonic kernel. Together these give

    liminf_{M→∞} inf_r H_{3^m}(ζ_{M,r})/N
        ≥ c' 3^{(1−θ)m}/sqrt(m).                                  (7)

The order here is first M→∞, then m→∞. Equations (1)–(6) are written
deductions independent of this imported critical lower bound.
For (7) use PR185's source-qualified harmonic construction and
its fixed-precision, all-clock lower bound in
`research/central-closure-20261123/COLLISION_LOGARITHMIC_GAIN.md`.
The frozen head used here is `2ac1f63b5f8d51ab4b472307b52cc89c9ef6df9d`,
Theorem 3, equation (16). For r=0 the lower bound on the actual
empirical law uses no harmonic-flow hypothesis.

There is also a simultaneous finite range. For any fixed T>0 and the
source-dependent c,M₀ in that theorem, require M≥M₀, m²≤TM, and
1/N≤(c/2)sqrt(m)Q^{-θ}. Then (7) holds as a finite inequality, with
the corresponding constant, before taking either limit. Moreover every
atom has mass ≤1/N, so the conditional probability of separation ≤R
given B is at most 2R/(NQ C_off) by lattice spacing alone. In this
range at least half of the distinct colliding pairs have separation
≥(c/8)N sqrt(m)Q^{1−θ}. This median bound needs no translated packing;
the harmonic mean additionally controls the influence of rare near pairs.

**First unsupported step in an escape contradiction.** One would need an
upper estimate for H_Q/N on those same laws along suitable precisions,
clocks and averaging windows, improving the right-hand scale in (7).
The canonical retracing probability ν(q_j)/ν(q_{j+r}) controls mass at
q_j and carries no factor 1/|q_i−q_j|. Its ordinary total-variation
comparison therefore does not supply the missing estimate. A large
unweighted congruence collision probability can be carried by widely
separated distinct ordinary integers. Equations (5)–(7) quantify exactly
how much separation an escaping orbit would require.

## Formal scope

[EscapeCore.lean](EscapeCore.lean) formalizes the shortcut iteration,
its integral affine remainder bound (2), the translated-interval
inequality before dividing by 2^k, residual-clock distinctness on a
fixed-weight class under the displayed transport identity, and the all-time synchronous distinctness
of a transversal of inverse fibers with synchronously distinct targets. The counting, entropy and harmonic
arguments above are mathematical proofs in prose.
