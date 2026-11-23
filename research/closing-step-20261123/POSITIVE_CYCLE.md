# Positive-cycle closure: a global denominator budget and exact return lattices

Date: 2026-11-23. Base: PR180
`7d4ad9f11d3d7a54c67b0c6cff4f13a2ab967161`.

**Status: source-qualified written theorem and an unconditional finite
return-lattice calculation. Complete positive integer cycle exclusion remains
OPEN.** The principal deduction below controls **all positive cycles
simultaneously**, rather than replacing their full denominators by selected
factors. It uses the earlier uniform ordinary predecessor-density statement
as an explicit input. A separate attempted amplification around a hypothetical
cycle is stopped by its exact ordinary integrality cost.

The direct goal was to turn original positive integer closure into an upper
bound on the full reduced complementary denominator, contradicting the lower
bounds already proved in PR180 and PR178. Neither that upper bound nor a new
all-word nonintegrality theorem was obtained. The global packing argument
does prove a finite total budget for the *original* complete cycle defects.
No literature-priority claim is made for the elementary identities used here.

## 1. Maps, inputs, and source boundaries

Use the ordinary shortcut map

\[
 T(n)=\begin{cases}n/2&n\text{ even},\\(3n+1)/2&n\text{ odd},\end{cases}
 \qquad
 U(q)=\frac{3q+1}{2^{v_2(3q+1)}}
\]

on positive integers, with `U` restricted to odd integers. Every positive
`T`-cycle contains an odd state and gives one `U`-cycle. Its distinct odd
states are ternary units: after any odd step, the next odd state is prime
to three, and periodicity then excludes a state divisible by three.

For a positive unit target `b`, let

\[
 \mathcal P(b)=\{n\ge1:T^j(n)=b\text{ for some }j\ge0\}.
\]

The sole analytic input in Sections 2--4 is the previously stated uniform
predecessor-density conclusion

\[
 \boxed{\quad
 \liminf_{X\to\infty}\frac1{\log X}
    \sum_{\substack{n\le X\\n\in\mathcal P(b)}}\frac1n
 \ge\frac{c_0}{b}
 \quad\text{for every positive ternary-unit }b,
 \qquad c_0>0.\quad}
 \tag{P}
\]

This is an inherited **source-qualified** input, not a theorem freshly
reproved in this pass. Its exact formulation and earlier single-divergent-
orbit application are in
[`DIVERGENT_ORBIT_PHASES.md`](../lean-forward-band-20261121/DIVERGENT_ORBIT_PHASES.md)
at the base commit above. The new use here is a simultaneous packing over
the periodic states of **every** positive component. The stronger natural-
density statements in the earlier packet are not needed.

The new peer inputs were inspected at these exact heads:

| Source | Exact head and path | Scope used |
|---|---|---|
| PR180 | `7d4ad9f11d3d7a54c67b0c6cff4f13a2ab967161`, `research/profound-step-20261123/ARITHMETIC_CLOSURE.md` | Full complementary denominator, primitive numerator budget, and the sign-sensitive control. |
| PR178 | `c91b80a3156e640ad471cf30c47721145ae21eb1`, `research/central-step-20261123/cycles/COMPLEMENTARY_DENOMINATOR_CAPACITY.md` | The full reduced companion denominator is greater than half the shortcut period for a nontrivial integer cycle. This is a lower bound. |
| PR177 | `f47a5ec51aa5853f104013a6d5046d6220ff7423`, `research/lean-exact-witness-global-20261121/literature-closure/cycles/POSITIVE_CARRY_CLOSURE_ATTEMPT.md` | The nearest-neighbor energy obstruction retains local positivity and actual quotient categories; it does not reject all nonlocal energies. |
| PR182 | `cb1ae1bb4af0c8d082e9ff466b9fe0c84932301c`, `research/literature-round4-20261123/CYCLE_RIGIDITY.md` | Full root-gap congruences recover the same numerical divisibility condition. Least-root selection supplies no independent rarity factor. |

## 2. Pack all positive periodic states into disjoint ordinary basins

Let `Q` be the set of **all positive odd periodic states**, with each state
listed once. No claim that `Q` is finite is made.

For each `q` in `Q`, exactly three exponents in `{1,...,6}` make

\[
 b=(2^e q-1)/3
\]

integral. Their values `2^e q mod 9` run through `1,4,7`; exactly one
therefore gives `3|b`. The other two are positive odd ternary-unit parents
of `q`, each satisfying

\[
                         b<22q.                         \tag{1}
\]

There is exactly one periodic `U`-predecessor of `q`. Indeed a periodic
predecessor must belong to the same cycle, and the action on that finite
cycle is a permutation. Choose one of the two small unit parents, denoted
`b_q`, that is **not periodic**.

**Disjointness lemma.** The sets `P(b_q)`, for all `q` in `Q`, are pairwise
disjoint.

To prove this, suppose one ordinary source reaches two different `b_q` and
`b_r`. At equal times the states are equal, and applying `U` gives `q=r`.
At unequal times, the later odd state would lie on the forward path from
the earlier one. But after the earlier parent, the intervening shortcut
states are even until the path reaches its periodic odd target. Every later
odd state is periodic. The chosen later parent is nonperiodic, a contradiction.
This argument also separates parents attached to different cycles.

For any finite subset `F` of `Q`, it follows that

\[
 \sum_{q\in F}\sum_{\substack{n\le X\\n\in\mathcal P(b_q)}}\frac1n
 \le\sum_{1\le n\le X}\frac1n.
\]

Divide by `log X`, take lower limits for the finite sum, and use (P).
The right side tends to one, so

\[
 c_0\sum_{q\in F}\frac1{b_q}\le1,
 \qquad
 \sum_{q\in F}\frac1q\le22/c_0.
\]

Taking the supremum over finite subsets proves the global theorem

\[
 \boxed{\qquad
       \sum_{\substack{q\ge1\\q\text{ odd and periodic}}}\frac1q
                  \le\frac{22}{c_0}.
       \qquad}                                           \tag{2}
\]

The sum does not count a state again on its next lap. Repeated cycle
traversals cannot be charged as new disjoint predecessor basins. There is
also no interchange of an infinite sum with the density limit.

## 3. A finite total budget for the complete cycle denominators

Let `C` be one positive `U`-cycle, with `p(C)` odd states and total division
count `A(C)`. The corresponding primitive shortcut period is `A(C)`.
Put

\[
 D_C=2^{A(C)}-3^{p(C)},\qquad
 \delta_C=A(C)\log2-p(C)\log3.
\]

Multiplication of the exact ordinary cycle equations gives

\[
 \delta_C
 =\sum_{q\in C}\log\left(1+\frac1{3q}\right)
 =\log\left(1+\frac{D_C}{3^{p(C)}}\right)>0.              \tag{3}
\]

In particular `D_C>0` is the **full numerical denominator** before the
ordinary cycle carry cancels it. Using `log(1+t)<=t` in (3) and summing
over distinct positive cycles, (2) proves

\[
 \boxed{\quad
 \sum_{C}\log\left(1+\frac{D_C}{3^{p(C)}}\right)
 =\sum_C\delta_C\le\frac{22}{3c_0}.
 \quad}                                                   \tag{4}
\]

The core `1 -> 2 -> 1` is included: its odd cycle is `{1}` and its defect
is `log(4/3)`. There is no exception hidden by a logarithm of zero.

The bound also has a basin interpretation. Let `B(C)` be the full ordinary
basin of `C`, and write `d_*(B(C))` for its lower logarithmic density.
All the selected parents attached to `C` lie in that basin, so

\[
 d_*(B(C))\ge\frac{c_0}{22}\sum_{q\in C}\frac1q
             \ge\frac{3c_0}{22}\delta_C.                  \tag{5}
\]

Thus each complete positive cycle defect consumes a specified amount of
ordinary basin mass. Distinct cycle basins are disjoint. Formula (4) is
simultaneous accounting, not a random-word estimate conditioned on closure.

### Consequences with their exact quantifiers

For every fixed `epsilon>0`,

\[
 \#\{C:\delta_C\ge\epsilon\}
                   \le\frac{22}{3c_0\epsilon}.           \tag{6}
\]

Consequently, if infinitely many distinct positive cycles existed, their
defects would tend to zero along every enumeration without repetition.
Taking `epsilon=log 2` shows that **all but finitely many** would satisfy

\[
             A(C)=\lceil p(C)\log_2 3\rceil.             \tag{7}
\]

Indeed `p(C) log_2 3` is irrational, and an additional integer division
above this ceiling makes `delta_C>log 2`. Statement (7) does not assert
that the pair of clocks is a continued-fraction convergent, and does not
give a period cutoff for the exceptional cycles.

Equivalently, for any fixed `0<epsilon<1`,

\[
 \#\{C:D_C/2^{A(C)}\ge\epsilon\}
 \le\frac{22}{3c_0[-\log(1-\epsilon)]}.                    \tag{8}
\]

These restrictions can coexist with a single nontrivial cycle, or with a
sufficiently sparse family of increasingly small positive defects. They
do not give the missing opposite bound on the complementary denominator.

## 4. The direct inverse-return attack and its exact arithmetic cost

A tempting amplification is to follow a cycle backward repeatedly. Its
real inverse multiplier is `exp(delta_C)`, which can be close to one.
One might hope to create many nearby ordinary inverse sources and consume
too much basin mass. The complete ordinary lattice prevents that inference.

The following calculation is unconditional given the supplied integer cycle.
Fix a phase `q`, let `w` be its complete shortcut word of length `A` and
weight `p`, and write

\[
 F_w(x)=\frac{3^p x+C_w}{2^A},\qquad
 C_w=(2^A-3^p)q.
\]

For `k>=1`, composition gives

\[
 F_{w^k}(x)
       =q+\frac{3^{kp}}{2^{kA}}(x-q).                    \tag{9}
\]

**Exact legal-return lattice.** The positive ordinary source `x` follows
the actual word `w^k` if and only if

\[
 x=q+2^{kA}t>0\quad(t\in\mathbb Z).
\]

Its endpoint is then

\[
             n=q+3^{kp}t>0.                             \tag{10}
\]

For necessity, same-word affine transport gives
`2^(kA) | 3^(kp)(x-q)`, hence `2^(kA) | x-q`. For sufficiency, after
`j<kA` steps the difference from the cycle phase is
`3^(p_j) 2^(kA-j) t`, which is even. Thus the literal next parity agrees
at every proper prefix, and the exact affine formula proves (9)--(10).
Ordinary positivity then persists under the actual map. This verifies all
branches, rather than inferring legality from a terminal rational equation.

Solving (9) backward from a fixed integer endpoint `n` gives

\[
 I_k(n)=q+\frac{2^{kA}}{3^{kp}}(n-q),\qquad
 \boxed{I_k(n)\in\mathbb Z\iff 3^{kp}\mid n-q.}          \tag{11}
\]

When the value in (11) is positive, (10) also proves its complete branch
legality. For `n!=q`, the number of allowed laps is at most
`floor(v_3(n-q)/p)`. A fixed off-cycle endpoint therefore cannot supply
arbitrarily many ordinary returns, however small the real defect is.

If `n>q` and (11) holds, then

\[
             n\ge q+3^{kp},\qquad I_k(n)\ge q+2^{kA}.
                                                               \tag{12}
\]

The tempting weak factor `exp(k delta_C)` is multiplied by the necessary
ternary source separation `3^(kp)`. The resulting ordinary starting height
is paid at the full binary scale `2^(kA)`. If instead `0<n<q`, positivity
of `I_k(n)` requires `2^(kA)<q`; only finitely many such laps are possible.

In particular, the ordinary sources realizing `w^k` form one residue class
modulo `2^(kA)`, of natural density exactly `2^(-kA)`. A real inverse orbit
without the condition in (11) has replaced the ordinary problem by a
rational one. Reusing the cycle point itself is the case `t=0`, and adds
no new source.

### Exact small control

For the core phase `q=1`, `w=10`, one has `A=2,p=1`. The fixed endpoint
`n=4` has one ordinary inverse return,

\[
 I_1(4)=5,\qquad 5\to8\to4,
\]

but

\[
 I_2(4)=19/3
\]

is nonintegral. It cannot be charged as a second ordinary inverse source.
For each `k`, the legal family is instead
`x=1+4^k t -> n=1+3^k t` with the actual repeated parity word.
The separate [exact checker](check_cycle_return.py) exercises this lattice,
both core phases, and damaged endpoint divisibility; its finite output is
not a cycle exclusion.

## 5. Why coupled products did not force complementary cancellation

For the actual original and complementary cycles, write the complementary
state as `y_i=w_i/b` with its complete reduced denominator `b`. Their
parities are opposite. The paired product has the exact updates

\[
 x_{i+1}w_{i+1}
 =\begin{cases}
 (3x_iw_i+w_i)/4&x_i\text{ odd},\\
 (3x_iw_i+b x_i)/4&x_i\text{ even}.
 \end{cases}                                             \tag{13}
\]

The product can grow only on the appropriate small-companion-numerator
steps; counting distinct such numerators gives the earlier denominator
capacity. Summing or multiplying (13) around the full word does not force
additional cancellation: the resulting identities follow from the two
complete affine closing equations.

A second exact identity keeps the shift by one. Multiplying the ratios of
`x_i+1` around the original cycle gives

\[
 2^A=3^p\prod_{x_i\text{ even}}\frac{x_i+2}{x_i+1},
 \qquad
 \prod_{x_i\text{ odd}}\left(1+\frac1{3x_i}\right)
 =\prod_{x_i\text{ even}}\left(1+\frac1{x_i+1}\right).
                                                               \tag{14}
\]

This retains original positivity and integrality, but it is also a
telescope on the same cycle. Counting its prime contributions as independent
of the ordinary product would be unjustified. No such independence is used
in (2)--(8).

For an exact scope control, the primitive positive rational word `11011010`
has original root `319/13`, complete denominator `13`, and original gcd one.
Its companion is `260/229`, with full reduced denominator `229`. Every
original state exceeds 21. The checker verifies (13) at all eight phases
and both products in (14), equal to `256/243`. Thus these real identities
alone do not detect ordinary integrality. The original word and rational
root are the retained PR182/PR177 control, not a new cycle example.

## 6. Literature examined and the next unsupported implication

Monks--Yazinski's [primary author paper](https://monks.scranton.edu/files/pubs/AutoConjV13.pdf),
Theorems 2.3--2.5, was read for the exact complementary-cycle symmetry and
self-conjugate-cycle restriction. It excludes the nontrivial self-conjugate
integer case. It does not force every positive integer cycle to be
self-conjugate or force its complementary denominator to be one.

Halbeisen--Hungerbuehler's [primary paper](https://people.math.ethz.ch/~halorenz/publications/pdf/collatz.pdf)
supplies the classical finite-word, rotation, and full-gcd framework. The
latest PR182 argument explains why rotating to the least state leaves the
integral proportion unchanged. The simultaneous packing proof above uses
ordinary predecessor basins instead of a new rotation-rarity factor.

The publisher's abstract of Knight's
[*Collatz high cycles do not exist*](https://doi.org/10.1016/j.disc.2025.114812)
was inspected; access to the HAL full text was denied. Its stated theorem
concerns the extremal high rational cycle at fixed clocks. No uninspected
proof or extension to all rational words is imported here.

The evolving [sparse block-sum paper, version 1](https://rstation.ai/problems/collatz/papers/22/v1)
and [mechanical-gap paper, version 1](https://rstation.ai/problems/collatz/papers/113/v1)
were inspected as literature leads. Their displayed results constrain
fixed defect complexity or separation from a mechanical extremizer. Their
global closing input remains absent; no unreviewed S-unit application from
those manuscripts is used in the proofs of this note.

For the direct cycle attack to close, one still needs either an arithmetic
contradiction for a single complete positive zero fibre, or a lower basin
mass/defect demand that cannot fit even one nontrivial cycle. The finite
total budget (4) supplies neither. In particular, summability of defects
does not imply that every defect vanishes. The inverse-return route cannot
amplify one small defect for free because of the all-lap lattice (10).

All statements in this note are written mathematics with the explicit (P)
qualification where used. No new Lean declaration or full Collatz theorem
is claimed.
