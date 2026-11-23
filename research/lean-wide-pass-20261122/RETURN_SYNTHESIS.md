# Actual return occupation: a uniform logarithmic gain

**Full Collatz closure remains open.** This attack obtains a source-uniform
upper bound for the actual marked occupation before the first repeated odd
state. It also constructs an actual clock-weighted marked reference measure
with finite fourth logarithmic moment, **retaining the full periodic tails**.
Neither result replaces a source
weight by an endpoint weight. The remaining return-transport and cycle
terms are retained explicitly.

The finite Fourier separation, finite prefix bound, and finite weighted
source accounting are Lean checked in
[`lean/ReturnSynthesis.lean`](lean/ReturnSynthesis.lean). The optimized
logarithmic rate, infinite measure sums, discounted resolvent, and moment
construction below are written deductions, with proofs. They are not
reported as separately kernel-checked declarations.

## 1. What was combined

The starting checkpoint is PR180 at
`d0349de2108abb7c8fb8393c086610e3372df116`. The new source snapshot is
[`SOURCE_SNAPSHOT.json`](SOURCE_SNAPSHOT.json). The relevant sources read in
this lane are:

| Exact source | Interface retained |
|---|---|
| PR178, `75f2f9aad4d3f80aaa1f8718e229faa04ee5770e`, `research/band-return-20261121/lean/ReturnFourier.lean`, `MarkPhase.lean`, `MarkFrequency.lean` | Actual Fourier coboundary, finite reciprocal cutoff, marked phase width, nonnegative Fejér kernel. The older temporal-density conclusion had an orbit-dependent eventual horizon. |
| Same PR178, `research/reframe-20261121/GLOBAL_MASS.md`, `GREEN_FRACTIONAL_MOMENTS.md`, `GREEN_TOPOLOGY.md` | Exact fixed-target Green bounds and the failure of continuous ternary renormalization. A compact almost-everywhere conclusion does not control every positive ordinary target. |
| PR183, `907a540943090968bc683b1b9246208e9053c1f8`, `research/literature-closing-20261121/transport/RETURN_TRANSPORT.md` | The exact entrance residual, unchanged original atoms, fourth-log-moment recurrence budget, and the unresolved regularity of a manufactured return reference. |
| PR175, `2055b8a311ab87d07bffc730154a7f8546fe382c`, `research/lean-global-closure-20261121/WIDE_CLOSURE_ATTEMPT.md` | The non-exhausted pressure tail is exponentially small, while the actual exhausted-source moment remains open. It supplies no return-packet replacement law. |
| Resident `research/integrated/renewal-transport/README.md` and its scoped source packets | A fresh rank-moment estimate cannot be restarted on an arbitrary transported packet. The unsafe-return counterexample retains that domain issue. |

The new estimates below do **not** assume the written predecessor-density
or joint-clock results of the earlier PR180 pass. They use the actual
integer map and the pinned PR173/PR178 Fourier interfaces only.

Use the shortcut map `T` and the odd accelerated map

\[
U(x)=(3x+1)/2^{v_2(3x+1)}.
\]

For a positive odd source `n`, put `x_j=U^j(n)`. A state is marked when

\[
x\text{ is odd},\qquad
(d+1)(x-2^d)\le70\,2^d,
\quad d=\lfloor\log_2x\rfloor.
\]

Write `M(n,N)` for the number of marked states among `x_0,...,x_(N-1)`.
The principal hypothesis for a finite prefix is just that these `N`
ordinary states are distinct. The orbit need not be known to remain
injective after that prefix.

## 2. A finite bound with no source-dependent horizon

Put `alpha=log_2 3` and

\[
S_k(n,N)=\sum_{j<N}e^{2\pi i k\log_2 x_j}.
\]

PR178's checked finite coboundary and reciprocal cutoff give, for every
nonnegative integer `B`,

\[
\left|1-e^{2\pi i k\alpha}\right|\,|S_k(n,N)|
\le2+4\pi k\left(B+\frac{N}{B+1}\right).       \tag{R1}
\]

This is an actual-path estimate. No independence, random starting residue,
predecessor-density input, or limiting equidistribution is used.

### Elementary frequency separation

For `0<k<=K`, the new Lean theorem proves

\[
\boxed{\frac1{4^K+1}\le
\left|1-e^{2\pi i k\alpha}\right|.}              \tag{R2}
\]

Here is the argument represented in `explicit_frequency_separation`.
Choose the nonnegative integer `a=floor(k alpha+1/2)` and put
`u=k alpha-a`, so `|u|<=1/2`. The previously checked integer-power
separation theorem `grid_barrier`, applied with `N=4^k`, rules out
`|u|<=1/(4^k+1)`. The elementary chord inequality

\[
|1-e^{2\pi iu}|=2|\sin(\pi u)|\ge4|u|
\quad(|u|\le1/2)
\]

then gives R2. The chord estimate is also checked, using Mathlib's sine
bound. In particular R2 is not an unproved irrationality-measure premise.

### Count exceptional states inside the finite prefix

Let `K,D` be nonnegative integers satisfying

\[
1120\pi K\le D+1.                                \tag{R3}
\]

The Fejér kernel used here is the nonnegative function

\[
F_K(u)=\left|\sum_{r<K}e^{2\pi iru}\right|^2.
\]

For a marked state of height at least `D`, the checked phase bound is

\[
0\le\log_2x-\lfloor\log_2x\rfloor
\le\frac{140}{\lfloor\log_2x\rfloor+1}.
\]

Condition R3 makes every one of the `K` summands lie within `1/2` of one.
Consequently `K^2<=4F_K(log_2x)`. This is the new theorem
`marked_kernel_of_height`.

There are at most `2^D` small states in the given injective prefix. This
counts values directly; it does not wait for an orbit-dependent final visit
below `2^D`. The finite kernel expansion therefore gives

\[
K^2 M(n,N)\le K^2 2^D+4KN+4K^2 A,                \tag{R4}
\]

whenever every nonzero Fourier coefficient with `k<K` is at most `A`.
Combining R1 and R2 supplies the completely explicit choice

\[
A=(4^K+1)\left[2+4\pi K
                  \left(B+\frac N{B+1}\right)\right]. \tag{R5}
\]

`marked_kernel_finite_cutoff`, `kernel_sum_absolute`, and
`marked_visits_finite_bound` check these steps. The last theorem retains
a free positive frequency gap; `marked_visits_explicit_bound` composes it
with R2 and discharges that premise uniformly in the ordinary source.

### Quantitative specialization

There is an absolute constant `C` such that every positive odd source
and every injective prefix of length `N` satisfy

\[
\boxed{M(n,N)\le C\frac{N}{\log(N+2)}.}           \tag{R6}
\]

All logarithms in rate estimates may be taken natural; changing the base
changes only `C`. For completeness, one deliberately generous explicit
specialization of R4--R5 is as follows. Take `K>=1`, `D=8192K`, and
`B=ceil(sqrt N)`, and assume `N>=2^(16384K)`. Then

\[
2^D\le\sqrt N,\qquad
B+N/(B+1)\le2\sqrt N+1.
\]

Since `pi<4` and `sqrt N>=1`, R5 gives

\[
A\le64K(4^K+1)\sqrt N.
\]

Moreover

\[
256K^2(4^K+1)\le2^{4K+9}\le2^{8192K}\le\sqrt N.
\]

The first inequality uses `K<=2^K` and `4^K+1<=2*4^K`.
Thus `4A<=N/K`, and also `sqrt N<=N/K`. Dividing R4 by `K^2`
proves the convenient finite form

\[
N\ge2^{16384K},\quad K\ge1
\quad\Longrightarrow\quad K M(n,N)\le6N.         \tag{R7}
\]

For sufficiently large `N`, choose
`K=floor(log_2 N/16384)>=log_2 N/32768`; for the remaining finite
range use `M(n,N)<=N`. This proves R6 with an absolute constant, uniformly
over every source and every permitted prefix.

Consequently, along an injective odd orbit, if `i_j` is the odd-clock
index of its `j`th marked visit, then for all sufficiently large `j`

\[
i_j\ge c\,j\log(j+1)                             \tag{R8}
\]

for an absolute `c>0`. Apply R6 with `N=i_j+1`, use `j<=N`, and
absorb the endpoint convention into the constant. The same lower bound
holds in ordinary shortcut time, since each odd step uses at least one
shortcut clock. This controls the accumulated actual return clocks;
it asserts neither that individual return gaps grow nor that returned
heights decrease.

## 3. Actual original-source occupation and its discounted resolvent

Let `mu` be any finite nonnegative measure on positive odd starting
states. For an original source `s`, let `tau(s)` be the first odd-clock
index at which a state repeats, with `tau(s)=infinity` for an injective
orbit. Define the actual nonrepeating marked occupation packet

\[
\nu_j(m)=\mathbf1_{m\text{ marked}}
 \sum_{\substack{s:\ j<\tau(s)\\U^j(s)=m}}\mu(s).
                                                               \tag{R9}
\]

Every collision is summed and every source keeps its original mass.
One may delete visits to one as well; doing so only reduces these bounds.
For a nonperiodic failed source, neither the repetition cutoff nor deletion
of one ever removes its atom.

Apply R6 to the prefix of length `min(N,tau(s))`. The function
`t/log(t+2)` is increasing for `t>=0`, so Tonelli gives

\[
\boxed{\sum_{j<N}\|\nu_j\|_1
\le C\|\mu\|_1\frac{N}{\log(N+2)}.}              \tag{R10}
\]

The finite source identity and weighted inequality behind this step are
Lean checked as `marked_source_occupation_identity` and
`weighted_marked_occupation_bound`. In particular this is not a statement
about the natural density of the set of marked endpoints.

For `0<r<1`, define the actual clock-discounted marked potential

\[
\mathcal Z_r(\mu)=\sum_{j\ge0}r^j\|\nu_j\|_1.
\]

Writing `epsilon=1-r`, summation by parts in the nonnegative sums yields

\[
\mathcal Z_r(\mu)
=\epsilon\sum_{N\ge1}r^{N-1}\sum_{j<N}\|\nu_j\|_1.
\]

Split at `N=epsilon^(-1/2)`. For smaller `N`, use the trivial bound
`sum_(j<N)||nu_j||<=N||mu||`. That part is `O(||mu||)`. For larger
`N`, `log(N+2)>=1/2 log(1/epsilon)` and
`sum_(N>=1)N r^(N-1)=epsilon^(-2)`. Equation R10 gives

\[
\boxed{\mathcal Z_r(\mu)
\le\frac{C'\|\mu\|_1}
 {(1-r)\log(1/(1-r))}}
\qquad(r\text{ sufficiently close to }1).          \tag{R11}
\]

Thus the nonrepeating marked occupation has a uniform logarithmic gain
over the full geometric clock pole. Equivalently,
`(1-r) Z_r(mu)=O(||mu||/log(1/(1-r)))`. No finite-atom exception is
discarded to obtain this rate.

### The cycle term is separate and remains present

The cutoff at first repetition is material. In the actual map killed
only at one, a nontrivial cycle retains every source atom which enters it.
If a cycle `C` has `p_C` distinct odd states and `m_C` marked states,
its long-run marked frequency is `m_C/p_C`. The forced section theorem
gives `m_C>=1`, if such a cycle exists. Its first period also obeys R6,
so `m_C/p_C<=C/log(p_C+2)`, but this is positive rather than zero.

For an arbitrary finite original-source measure, the actual marked
time-average, without the repetition cutoff, is exactly

\[
\lim_{N\to\infty}\frac1N
 \sum_s\mu(s)\sum_{j<N}\mathbf1_D(U^j(s))
=\sum_{\text{positive odd cycles }C}
 \mu\{s:s\text{ enters }C\}\frac{m_C}{p_C}.        \tag{R12}
\]

Each source is either eventually periodic or injective, and R6 handles
the latter. The per-source average is bounded by one, so dominated
convergence proves R12. For the map killed only at one, remove the trivial
cycle's contribution; all hypothetical nontrivial-cycle contributions
remain. Equation R11 alone cannot establish R12's vanishing.

## 4. A finite fourth-log-moment reference that is actually constructed

Suppose the original measure also satisfies

\[
K_\mu=\sum_s\mu(s)L(s)^4<\infty,
\qquad L(s)=1+\lfloor\log_2s\rfloor.
\]

PR183 supplies such a measure by first entrance: with
`mu=E_*(sum_(n>=1)n^(-4) delta_n)`,
`K_mu<=4096 zeta(2)`. Original atoms can still be kept under their
pre-entrance labels, since all estimates are nonnegative and sum complete
fibers.

Define the **full** marked packet, without the repetition cutoff, by

\[
\widetilde\nu_j(m)=\mathbf1_{m\text{ marked}}
 \sum_{s:U^j(s)=m}\mu(s).
\]

For **any** fixed `eta>0`, form the actual full marked reference

\[
\alpha_\eta=
\sum_{j\ge0}
 \frac{\widetilde\nu_j}{(j+1)^5[\log(j+2)]^\eta}.  \tag{R13}
\]

Then

\[
\boxed{\sum_m\alpha_\eta(m)L(m)^4<\infty.}        \tag{R14}
\]

First consider the part before the first repeated state,
`alpha_eta^nr=sum_j c_j nu_j`. Since `U(x)<=2x` for every positive odd integer,
`L(U^j(s))<=L(s)+j`. The inequality
`(a+b)^4<=8(a^4+b^4)` gives

\[
\sum_m\alpha_\eta^{\rm nr}(m)L(m)^4
\le8K_\mu\sum_{j\ge0}c_j
 +8\sum_{j\ge0}j^4c_j\|\nu_j\|_1,
\quad
c_j=((j+1)^5[\log(j+2)]^\eta)^{-1}.               \tag{R15}
\]

The first sum converges. Handle `j=0,1` separately. On
`2^k<=j<2^(k+1)`, for `k>=1`, the second coefficient
is at most `C_eta 2^(-k) k^(-eta)`, while R10 bounds the packet sum
over that block by `C||mu|| 2^k/k`. Hence the block contributes at most
`C_eta||mu||/k^(1+eta)`. Summing bounds the entire nonrepeating part.

Now retain the periodic tails. For a source with finite first repetition
time `tau>=1`, every state at or after `tau` equals one of the states
before `tau`. In particular,

\[
L(U^j(s))\le L(s)+\tau\qquad(j\ge\tau).
\]

The actual finite-orbit containment and ordinary height bound are also
proved in the supporting `lean/RepeatedTail.lean`; the following infinite
coefficient sum is a written calculation. The decreasing-series integral
estimate gives

\[
\sum_{j\ge\tau}c_j
\le\frac54(\log2)^{-\eta}(\tau+1)^{-4}.
\]

Consequently this source's whole post-repetition fourth-log-moment is at
most

\[
\frac54(\log2)^{-\eta}\mu(s)
 \frac{(L(s)+\tau)^4}{(\tau+1)^4}
\le10(\log2)^{-\eta}\mu(s)(L(s)^4+1).
\]

Summing over all eventually periodic sources is finite. Sources with
infinite `tau` have no post-repetition contribution. Together with R15,
this proves R14 for the **full** reference R13, including every hypothetical
nontrivial-cycle atom. The occupation estimates R10 and R11 continue to
require their stated nonrepetition cutoff.

This is an actual regularity result, not an assumed moment estimate for
a manufactured reference. When the initial measure is supported on the
marked section, `alpha_eta>=c_0 mu` before deletion of the state one,
where `c_0=(log2)^(-eta)>0`. Every nonrepeating later occurrence also has
its original atom represented with its positive, explicit clock weight.
Periodic occurrences are retained as well; the construction does not kill
a hypothetical cycle.

## 5. The remaining global comparison

The latest PR183 recurrence argument would exclude an injective surviving
source if one finite-fourth-log-moment reference `lambda` dominated the
actual return packets with coefficients

\[
Q^k\rho\le A(k+1)[1+\log(k+2)]^5\lambda.
                                                               \tag{R16}
\]

R14 supplies a genuine finite-moment measure, but does not supply R16.
One attempted sufficient route is to compare each occurrence's coefficient
with the coefficient at its actual later return. If one original atom's marked
occurrence at odd clock `t` is followed by its `k`th further marked return
at clock `u`, the coefficients in R13 have ratio

\[
\frac{c_t}{c_u}
=\left(\frac{u+1}{t+1}\right)^5
 \left(\frac{\log(u+2)}{\log(t+2)}\right)^\eta.    \tag{R17}
\]

This termwise comparison does not supply the critical scale. Already at
`t=0` on an injective surviving source, R8 gives
`u>=c k log(k+1)`, so R17 grows at least as a positive constant times
`k^5 (log k)^(5+eta)`. The desired coefficient in R16 has only a linear
factor in `k`. Moreover the pinned first-return theorem allows arbitrarily
large `R(n)/n` on marked ordinary sources. Since one odd step increases
height by at most a factor of two, their first odd return clocks are
unbounded. Thus a source-uniform, finite, **one-return termwise** bound
on `c_0/c_u` is unavailable for this reference.

This is a limitation of the proposed termwise proof, not a disproof of
aggregate domination in R16. Other original sources and other occurrences
may supply additional reference mass at the same endpoint. Any successful
use of R13 at the critical scale must control those complete endpoint
fibers, rather than merely compare two times of the same occurrence.

The universal section-access estimate bounds a return's clocks by a
multiple of the square root of its current height, and the initial fourth
logarithmic moment does not control that transported square-root height.
The known unsafe-return moment failure makes the same domain distinction
essential in the rank formulation.

Nor can the discount in R11 be removed while retaining its conclusion:
its right side still tends to infinity as `r` tends to one. A fixed
nonperiodic source may have infinitely many marked returns with counting
function `O(N/log N)`. Its unchanged atom then contributes infinite
undiscounted marked occupation and remains compatible with R10--R11.

This pass therefore advances the actual upper side: a uniform finite
prefix estimate, an original-source occupation bound, a logarithmic
clock-resolvent gain, and a proved full finite-moment construction.
An aggregate endpoint-fiber comparison sufficient for R16, or a
positive-cost source-packet drift with summable errors that also kills
cycles, is still missing. No such bound is inserted into the Lean theorem
statements.

## 6. Exact formal provenance and replay scope

The following files are byte-identical copies from PR178 at
`75f2f9aad4d3f80aaa1f8718e229faa04ee5770e`:

| Vendor file | SHA-256 |
|---|---|
| `lean/vendor/ReturnFourier.lean` | `a758b7b8c6b1827a5f96eb8ae32196c0145a0280229b6fa22bf899c3cd348ed3` |
| `lean/vendor/MarkPhase.lean` | `bd4cc9ef10cbaa91b8d8a8ea83f1d9dfbbf644d0235ceff77452c18abdf199d9` |
| `lean/vendor/MarkFrequency.lean` | `7786fd2c3eccecf8dedb931233c9ae1da059a8d883fb1e8250304b6c4df84921` |

They reuse the existing pinned `ForwardSection.lean` and its source
dependencies. The added Mathlib import is
`Mathlib.Analysis.SpecialFunctions.Trigonometric.Bounds`, at the unchanged
Mathlib revision `d13f23b723b8a846827a245b89c10fc7d3f11612` and Lean
`4.34.1`. No new analytic axiom is declared.

The public declarations audited in the new module are the explicit
frequency separation, marked-state kernel lower bound, finite-prefix
kernel cutoff, absolute kernel sum, finite visit bound, its explicit-gap
specialization, exact weighted source identity, and weighted occupation
bound. The build receipt records
the final declarations, exact compiler exit, and axiom output. Standard
Lean axioms are `propext`, `Classical.choice`, and `Quot.sound`; none is
a Collatz assertion.
