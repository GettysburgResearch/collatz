# Sixth pass: boundary-only inverse minimization and genuinely asynchronous bridges

Agent: `astra-critical-mass-01` (GPT-6 Pro). Date: 2026-09-05.
Frozen parent: PR #90 at `908fdca1fe21456f8c6d476b31b74c8552670395`.

**All new theorem-level claims are PROPOSED pending independent review.**
No full Collatz proof, complete merging cover, basin-stability theorem, Green
bound, or discrepancy bound is claimed. This packet is an addition; it does not
change the earlier proofs or their separate review boundaries.

This continuation tests the preceding pass's proposed escape from synchronous
quotient stripping. It proves a two-return inverse minimization theorem that
retains only boundary exits, an exact further classification inside the earlier
five depth-two progressions, and a three-parameter family of physical two-sided
rank reductions. Its five-shortcut-step specialization **never** meets its
endpoint at equal clocks, yet provides a uniform rank reduction while any
prescribed finite forward rank horizon fails. Thus the phase obstruction is
avoided on a proved family, not dismissed or assumed absent globally.

**Publication boundary:** the current session had GitHub read access but no
exposed write action; direct git access failed at DNS resolution. This packet is
supplied as an addition-only patch for the frozen branch, not as a remotely
pushed commit. See the [session report](../../reports/astra-critical-mass-01/2026-09-05-boundary-fan.md).

## Claim map

| Claim | Result | Boundary |
|---|---|---|
| T-ASTRA-030 | Exact minimum in a complete inverse ball of radius two, using at most five candidates | Not a greedy algorithm for unbounded depth |
| T-ASTRA-031 | Exactly three subprogressions of the designated depth-two residual have a strict inverse reduction within two returns | Other classes and deeper diagrams remain open |
| T-ASTRA-032 | For all a>=2, H>=a+2, L>=1, two reverse section returns lower rank by more than four while L forward returns increase it | Ordinary sources vary with the parameters |
| L-ASTRA-033 | No positive fixed point of T^5; the a=2 bridge never synchronizes | Not a general positive-cycle theorem |
| R-ASTRA-034 | Greedy minimization fails; recursively discarding interior exits also fails at depth three | Exact counterexamples plus a third-return infinite progression |

## 0. Ordinary normalization and credited inputs

Use the one-division shortcut map

\[
T(n)=\begin{cases}n/2,&n\text{ even},\\(3n+1)/2,&n\text{ odd},\end{cases}
\quad n\in\mathbb N_{>0}.
\]

Put

\[
\mathcal H=\{n\ge1:n\equiv1\pmod3\},\quad
h(n)=\nu_3(2n+1),\quad u(n)=(2n+1)/3^{h(n)},\quad
P(n)=3^{h(n)}u(n)^2.
\]

The rank is defined on every positive integer, but the inverse return map below
is on the section H, with absorption at 1. On H, h>=1. Let R be the first
positive-time section return for n>1. This return is always finite: for an odd
source m=2^a v-1, the a odd shortcut steps give 3^a v-1, and one even step
returns to H. For an even section source, strip its first half and use this
formula unless two even steps already return. This is a finite calculation,
not an assumption of eventual convergence.

The section, rank, and complete inverse fan originate in PR #91 at
`b8c88843726ee7ac11cf91323c69bf911ca50706`. The least member of one inverse fan
and the five progressions used below are from [MINIMUM_RANK.md](MINIMUM_RANK.md),
frozen in PR #90 at `d4d8f8fb6feba3d508445b36417bc298ac50b79c`.
The global extension and synchronous obstruction are in
[REMAINDER_CANCELLATION.md](REMAINDER_CANCELLATION.md) at the parent above.
The necessary inverse formulas are rederived here; no imported analytic or
large-computation theorem is a dependency of the new arguments.

If a positive exceptional component exists, its section has a least P because
P is a positive integer. Any finite merging diagram to a smaller-rank ordinary
source contradicts that minimum. This is the motivation for the reductions,
not a proof that the reductions cover the whole section.

## 1. Complete inverse fan and one-generation minimum

Fix y>1 in H. Write h=h(y), u=u(y),

\[
B=2^{h+1}u-1,\quad k=\nu_3(B),\quad
s_j=2(2^j3^{h-j}u-1)\ (0\le j<h),
\]
\[
e=s_{h-1}=3\,2^h u-2,\qquad z=2^h u-1.
\]

The complete first-return predecessor fan is

\[
\mathcal F(y)=\{s_0,\ldots,s_{h-1}\}
\cup\bigl(\{z\}\text{ if }k\ge1\bigr).                 \tag{1.1}
\]

Starting backwards at 2y, a residue-2 state has an even predecessor in H and
an odd predecessor continuing the residue-2 chain. At the terminal odd node,
it either enters H or enters residue 0. A residue-0 branch has only even
predecessors, all in residue 0, so it supplies no further first-return source.
The odd inverse decreases its current positive value, proving termination of
this enumeration. All recorded sources are positive and at most 4y.

The least-rank member is

\[
I(y)=\begin{cases}e,&k=0,\\z,&k\ge1.\end{cases}       \tag{1.2}
\]

Indeed 2e+1=3B, so P(e)=3^{1-k}B^2. If z exists, 2z+1=B and
P(z)=P(e)/3. For j<h-1,

\[
P(s_j)=3(2^{j+2}3^{h-j-1}u-1)^2>P(e).
\]

This proves the exact minimum without counting a proper subset of the fan.
The rank is injective: nu_3(P(n)) recovers h(n), and then the positive square
root recovers u(n). There is no tie-breaking assumption below.

## 2. T-ASTRA-030 — only the boundary exits matter at radius two

Define the boundary set E(y)={e}, adding z when k>=1. Let B_2(y) contain y,
all first-return ancestors of y, and all ancestors of those ancestors. Then

\[
\boxed{
\min_{x\in B_2(y)} P(x)
=\min\left(\{P(y)\}\cup
\{P(b),P(I(b)):b\in E(y)\}\right).
}                                                        \tag{2.1}
\]

Thus at most five candidates suffice, independently of h. The root is included
in (2.1): the theorem concerns strict improvements inside the radius-two ball,
not necessarily the minimum at *exactly* distance two.

### Proof

The only omitted first-generation exits are s_j with j<=h-2. For them

\[
h(s_j)=1,\qquad u(s_j)=2^{j+2}3^{h-j-1}u-1=:v_j.
\]

Also

\[
\nu_3(4v_j-1)=\nu_3(2^{j+4}3^{h-j-1}u-5)=0,
\]

since the power of 3 in the first term is positive. Formula (1.2) therefore gives

\[
I(s_j)=6v_j-2,\quad P(s_j)=3v_j^2,\quad
P(I(s_j))=3(4v_j-1)^2>P(s_j).                           \tag{2.2}
\]

The smallest v_j occurs at j=h-2 and equals 3*2^h*u-1>2^h*u. Hence

\[
P(s_j)>3\,4^h u^2>3^h u^2=P(y).                         \tag{2.3}
\]

Every ancestor of s_j has rank at least P(I(s_j)), so neither that interior
exit nor any of its immediate ancestors beats the root. Only e and, when
present, z and their least-rank predecessors remain. For h=1 the omitted set
is empty. This proves (2.1) in every case. QED.

### A useful first-crossing corollary, with its scope kept separate

Suppose a backward path first attains rank below P(y) at a proper ancestor x.
If h(x)=1, its next forward section state has still smaller rank, contradicting
first crossing. This uses the elementary depth-one reduction in the prior
packet: all three return cases give P(R(x))<P(x).
If x is even with h(x)>=2, the odd source m=(x-1)/3 has P(m)=P(x)/3 and
T(m)=T(x), hence R(m)=R(x). It provides a lower-rank ancestor at the same
inverse distance. It cannot have h(m)=1, by the same first-crossing argument. The case m=1 cannot occur on
a first crossing toward a root y>1: its sibling x=4 already has parent 1.
Thus a first strict crossing can be sought at an odd terminal exit of depth
at least two. This does **not** license discarding every earlier large-rank
interior subtree at arbitrary depth. Equations (2.2)-(2.3) only justify the
complete two-generation pruning above.

## 3. T-ASTRA-031 — exact further inverse classification of the five progressions

Let D_0 be the designated earlier residual

\[
n>0,\quad n\equiv139,427,571,859,1003\pmod{1296}.         \tag{3.1}
\]

These integers are odd, have h(n)=2, and satisfy k(n) in {0,1}. They have no
strict immediate inverse reduction: its least inverse ratio is at least
49/27 when k=1 and at least 49/3 when k=0. The earlier packet shows that a
minimum-rank exceptional state at h=2 must lie here; the following theorem
can also be read simply as a statement about the explicitly defined set D_0.

For n in D_0, there is a strict lower-rank ancestor within two R returns
**if and only if** n belongs to one of these three disjoint progressions:

\[
\boxed{
\begin{array}{c|c|c|c}
 n & x & \text{physical word from }x\text{ to }n & P(x)/P(n)\text{ is below}\\\hline
30379+34992t &(32n-11)/9 &10010&1024/2187\\
3019+11664t &(32n-29)/27&10110&1024/2187\\
29371+34992t&(64n-31)/27&110010&4096/6561
\end{array}
\quad t\ge0.
}                                                        \tag{3.2}
\]

Each bound is less than one. All three words consist of two section returns.
The proof below establishes exact coverage at inverse radius two within D_0,
not merely sufficient tests. It says nothing about larger-radius or additional
forward merging diagrams on the complement.

### Proof by boundary valuations

Set u=(2n+1)/9. On D_0, u>=31; in particular all strict comparisons below
hold already at u>=7. The immediate boundary exits are e=12u-2 and,
when k=1, z=4u-1.

**Case k=0.** The only boundary exit is e, with h(e)=1 and unit 8u-1.
Put K=nu_3(32u-5). If K=0, its least predecessor is even and has rank larger
than P(n). If K>=1, its least predecessor is x=16u-3, and

\[
\frac{P(x)}{P(n)}=\frac{(32u-5)^2}{3^{K+2}u^2}.          \tag{3.3}
\]

Since 32-5/u>27, this is greater than one for K<=4. For K>=5 it is strictly
less than 1024/2187. Now K=nu_3(64n-13)-2, so the exact condition is
3^7 dividing 64n-13.

**Case k=1, through z.** Here h(z)=1 and v=(8u-1)/3 is its unit. Put
K=nu_3(4v-1). If K=0 the even minimum again has rank above P(n). Otherwise
its odd minimum is x=2v-1=(16u-5)/3 and

\[
\frac{P(x)}{P(n)}=\frac{(32u-7)^2}{3^{K+4}u^2}.          \tag{3.4}
\]

At u>=7, 32-7/u>=31>27. Thus K<=2 fails, while K>=3 gives the strict upper
bound 1024/2187. Since K=nu_3(64n-31)-3, the condition is 3^6 dividing 64n-31.

**Case k=1, through e.** Now h(e)=2 with the same unit v. Put
K=nu_3(8v-1). The even alternative when K=0 has rank above P(n). When K>=1
the odd minimum is x=4v-1=(32u-7)/3, and

\[
\frac{P(x)}{P(n)}=\frac{(64u-11)^2}{3^{K+4}u^2}.         \tag{3.5}
\]

For K<=3, this exceeds one because 64-11/u>62 and 62^2>3^7. For K>=4 it
is strictly less than 4096/6561. Here K=nu_3(128n-35)-3, giving the condition
3^7 dividing 128n-35.

By (2.1) these are all possible strict inverse improvements at this radius.
Combining the three ternary congruences with n=11 modulo 16 gives (3.2).
The resulting classes lie in 571, 427, and 859 modulo 1296 respectively;
the other two old classes do not meet these conditions. Direct affine
composition gives the three displayed words and sources. Alternatively,
(1.1) supplies the two physical section returns. Positive progressions start
at the listed least positive representatives, so no finite negative segment
has been silently admitted. QED.

The remaining depth-two set for this inverse test is exactly
D_0 minus these three progressions. At the prior finite cutoff 2^18, this
removes 37 of the 1,011 D_0 sources, leaving 974. This comparison is with D_0,
**not** a claim of 37 new sources beyond the union of every earlier merging
or shared-remainder rule on the branch. Overlap with those other families
has not been comprehensively audited.

## 4. T-ASTRA-032 — a three-parameter family of asynchronous backward bridges

For every integer a>=2, H>=a+2, and L>=1, there are infinitely many positive
odd ordinary n and x with

\[
\boxed{
R^2(x)=n,\quad h(x)=H,\quad h(n)=a,\quad k(n)=1,
\quad P(x)<P(n)/4,
}                                                        \tag{4.1}
\]

while

\[
\boxed{P(R^i(n))>P(n)\quad(1\le i\le L).}               \tag{4.2}
\]

The ancestor word is

\[
w_a=10\,1^a0,\qquad |w_a|=a+3.                          \tag{4.3}
\]

For a=2 the ancestor is numerically larger than n. For a>=3 the ancestor
is numerically smaller. No same-clock merger is required. In the a=2
specialization, Section 5 proves that no same-clock merger can ever occur.

### The exact arithmetic, before choosing ordinary sources

The first 10 maps x to (3x+1)/4. Following it by a odd steps and one even
step gives

\[
n=\frac{3^{a+1}x+5\,3^a-2^{a+2}}{2^{a+3}}.             \tag{4.4}
\]

In shifted coordinates this is

\[
2^{a+3}(2n+1)=3^a\bigl(3(2x+1)+7\bigr).                \tag{4.5}
\]

Thus the shifted remainder is exactly 7*3^a. For h(x)=H>=1,

\[
h(n)=a,\qquad
2^{a+1}u(n)-1=3(x+1)/2,\qquad k(n)=1.                  \tag{4.6}
\]

The last equality uses x=1 modulo 3. From the positive 7 in (4.5),

\[
\frac{P(x)}{P(n)}
<\frac{4^{a+3}}{3^{H+a+2}}.                              \tag{4.7}
\]

At H=a+2 the right side is 4^{a+3}/3^{2a+4}; for a=2 it is 1024/6561<1/4,
and increasing a multiplies it by 4/9. This proves the uniform quarter bound.
For a=2, (4.4) reads n=(27x+29)/32, and x>n when x>29/5; our sources have
H>=4, so that condition holds. For a>=3, both the slope and the positive
constant in (4.4) make n>x.

### CRT construction proving positive ordinary realizability

Put

\[
D_a=3^a-2^{a+1}>0,\quad b_a=3^a-2^a,\quad
\eta_a=-b_a/D_a.
\]

The odd denominator makes eta_a an ordinary rational with a defined residue
modulo every power of two. It is used **only to specify finite congruences**.
No orbit of that rational is asserted to be a positive ordinary trajectory.
Impose

\[
n\equiv\eta_a\pmod{2^{(a+1)L+1}},                        \tag{4.8}
\]
\[
2^{a+3}(2n+1)-7\,3^a
\equiv3^{a+H+1}\pmod{3^{a+H+2}}.                         \tag{4.9}
\]

Both define a single residue in their coprime moduli. CRT gives infinitely
many positive n. Taking the CRT representative plus at least one full modulus
makes the x from (4.4) positive. Equation (4.9) makes 2x+1 an odd positive
integer of exact ternary valuation H. Hence x is integral, and the final
integrality of the affine word (4.4) forces its physical parity class.

Here is a proof of that last standard guard. Each length-j parity word has
one residue class modulo 2^j: the two lifts of a length-i class have opposite
next parities because their i-step difference is the odd integer 3^{q_i}.
Its final affine integrality condition also has exactly one residue, because
3^q is odd. The physical class satisfies that condition, so the two classes
coincide. Positivity of an initial integer keeps every actual intermediate
value positive. The word 10 | 1^a0 therefore consists of two actual section
returns, with no unrecorded section entry.

### Forward resistance for the prescribed horizon

On an odd source with nu_2(n+1)=a, a complete section block 1^a0 acts as

\[
F_a(n)=\frac{3^a(n+1)-2^a}{2^{a+1}}
=\eta_a+C_a(n-\eta_a),\quad C_a=3^a/2^{a+1}>1.
\]

Since eta_a+1=-2^a/D_a has exact dyadic valuation a, (4.8) forces each of
the first L actual returns to use this block. More explicitly,

\[
n_i=\eta_a+C_a^i(n-\eta_a),\quad 0\le i\le L,            \tag{4.10}
\]

and n_i-eta_a remains divisible, in the dyadic rational sense, by
2^{(a+1)(L-i)+1}. At i<L this preserves the exact initial odd-run length a;
it also leaves every n_i odd through i=L. The displayed identities are
proved by finite induction on actual ordinary iterations.

All n_i are strictly increasing because C_a>1 and the additive term of F_a
is positive. Also h(n_i)=a throughout: every source is in H, its n_i+1 is a
3-unit, and the next shifted endpoint is 3^a(n_i+1)/2^a. Consequently
P(n_i)=(2n_i+1)^2/3^a>P(n). This proves (4.2). QED.

For a=2, (4.8) makes n=11 modulo 16 and (4.9) gives n=22 modulo 81 and nu_3(n+5)=3.
These sources lie specifically in 427 modulo 1296 and in the second
progression of (3.2). They pass the earlier immediate forward, inverse, and
sibling tests. The fixed five-step diagram bypasses any prescribed finite
forward rank horizon. The source varies with H and L; no infinite survivor
is extracted from those changing ordinary witnesses.

## 5. L-ASTRA-033 — the five-step bridge cannot synchronize at any later time

There is no positive integer y with T^5(y)=y.
For a word of length five and q odd steps, the affine equation is
(32-3^q)y=A. If q>=4 its denominator is negative and A>0. If q=0 it gives y=0.
The remaining complete possibilities for A are:

| q | 32-3^q | all possible A |
|---|---:|---|
| 1 | 29 | 1, 2, 4, 8, 16 |
| 2 | 23 | 5, 7, 10, 11, 14, 19, 20, 22, 28, 40 |
| 3 | 5 | 19, 23, 29, 31, 37, 38, 46, 49, 62, 76 |

None is a positive multiple of its denominator. The table follows from
A=sum 3^{q-1-r}2^{i_r} over increasing odd positions i_r in {0,...,4};
the two checkers reconstruct all 32 words differently. Thus this is a complete
finite-word exclusion at period five, not a large starting-integer census.

For any a=2 bridge, T^5(x)=n. Were T^j(x)=T^j(n) at any common j>=0, the
positive integer T^j(x) would be fixed by T^5. This is impossible. Therefore

\[
\boxed{T^j(x)\ne T^j(n)\text{ for every }j\ge0,
\qquad T^5(x)=n.}                                       \tag{5.1}
\]

Unlike the prior phase controls, this uses no stopping-time calculation or
assumption that the chosen family converges. It shows directly that a useful
lower-rank merging certificate can be intrinsically asynchronous. It does not
exclude all other positive cycles, or imply a similar no-synchronization
statement for every unbounded value of a.

## 6. R-ASTRA-034 — two false recursive shortcuts

### Greedy one-ancestor iteration is false

At the earlier residual n=29371,

\[
P(n)=383415561,\quad I(n)=26107,\quad I(I(n))=104428.
\]

Both greedy ancestors have larger rank than n. The other boundary exit is
78322, whose least ancestor is 69619. In fact

\[
R(69619)=78322,\quad R(78322)=29371,
\quad P(69619)=26594649<P(n).                             \tag{6.1}
\]

The actual shortcut word is 110010. Thus choosing the least-rank immediate
ancestor and repeating misses a strict two-return improvement. The larger
immediate boundary ancestor is essential. This is not a refutation of (2.1),
which retains both boundaries, or of deeper exact search.


### Discarding interiors at every depth is false too

Even retaining both boundaries at every step is not a complete deeper search.
At n=208363, which belongs to 1003 modulo 1296, the complete inverse ball of
radius three has lower-rank minimum x=4445077, while the boundary-only tree
through that radius has no rank below P(n). The actual path is

\[
4445077\xrightarrow{10}3333808\xrightarrow{00}833452
\xrightarrow{00}208363,                                \tag{6.2}
\]

and

\[
P(208363)=19295710281>12046160025=P(4445077).
\]

The first reverse step 208363 -> 833452 is the **interior** exit that the
radius-two proof allows us to discard only through one further generation.
The lower-rank ancestor is in the third generation. The exact complete and
pruned finite node sets are reconstructed by both checkers. This is an actual
counterexample to the naive all-depth extension, not just a warning that an
extension might fail.

The same six-shortcut-step word gives another positive infinite-family rule:

\[
\boxed{
 n=208363+314928t,\qquad x=(64n-1)/3,
 \qquad R^3(x)=n,\qquad P(x)/P(n)<4096/6561<1,
 \quad t\ge0.
}                                                       \tag{6.3}
\]

For this progression, h(n)=2 and 3^9 divides 128n+1. Since
2x+1=(128n+1)/3, h(x)>=8. Its word is 100000 with q=1, j=6, and
shifted remainder B=63. Thus

\[
64(2n+1)=3(2x+1)+63,
\quad P(x)/P(n)<4^6\,3^{2-h(x)-2}\le4096/6561.
\]

Integrality forces the physical word, or it may be checked directly from
3x+1=64n. The decomposition is 10 | 00 | 00. The positivity and congruence
conditions hold throughout the stated progression. Only the specific t=0
example is asserted to defeat the boundary-only tree at radius three; no
such additional comparison is claimed for every t.

## 7. Attempted completion and the precise unresolved part

The target was to turn the preceding shared-remainder rules into a complete
lower-rank merging construction without assuming synchronization. This pass
establishes a valid asynchronous family and an exact small inverse search
interface, including a proof that greedy iteration is insufficient.

The strong result (4.1)-(4.2) does not make the cover complete. In the old
five progressions, the new radius-two inverse classification still leaves
D_0 minus (3.2). The individual source 859 is not eliminated by these inverse
rules. Source 121 still has no strict ancestor-rank improvement within two
section returns. Neither is a counterexample to Collatz. A lower-rank source
found by a different forward/merging diagram can still handle them.

The first unsupported step in a proposed complete proof would be asserting
that repeatedly exploring the retained boundaries must reach a strict rank
crossing. The finite-radius pruning proof does not say that: large interior
subtrees do matter after more generations, as (6.2) demonstrates, and (6.1)
already defeats the simplest greedy iteration. No recursion on the residual complement with a
proved decreasing measure has been found here.

**Q-ASTRA-003 remains OPEN.** The next meaningful theorem is a complete,
physically guarded recursive treatment of the residual, with a termination
argument for the selector itself. Extending the radius or accumulating more
successful arithmetic progressions without such a theorem is finite evidence,
not full closure. The old 9x+4 basin implication is not supplied by these
alternative-source bridges.

## 8. Evidence and provenance

The [new experiment](../../experiments/X-ASTRA-006-boundary-fan/README.md) compares
the boundary shortcut against a separately reconstructed **complete** two-return
inverse ball at all 87,381 section sources through 2^18. It also includes 55
larger exact inputs, 216 CRT family cases, 2,268 subsequent forward returns,
24 very large progression substitutions, the complete T^5 word table, and
8 resealed tamper tests. The theorem's unbounded parameters are covered by
the mathematical proofs, not by those finite cases.

Both implementations passed locally. They have the same author: this is
implementation independence, not independent mathematical review or a formal
proof. Checks use explicit exceptions, so Python optimization does not remove
their assertions. No external computation, Lean build, or full-repository
validator is part of this continuation.

Primary repository sources, pinned rather than silently promoted:

- PR #91: `b8c88843726ee7ac11cf91323c69bf911ca50706`,
  `research/astra-three-routes/ROUTE_1_TRANSFER.md`: section, rank, inverse fan.
- PR #90 fourth pass: `d4d8f8fb6feba3d508445b36417bc298ac50b79c`,
  `research/astra-critical-mass/MINIMUM_RANK.md`: inverse minimum, generic
  backward-rank estimate, and the five designated depth-two progressions.
- PR #90 fifth pass: `908fdca1fe21456f8c6d476b31b74c8552670395`,
  `research/astra-critical-mass/REMAINDER_CANCELLATION.md`: global rank,
  shared remainders, and the fixed-quotient same-clock limitation.

External context consulted only at abstract level: A. Edgington,
*The autoconjugacy of a generalized Collatz map*, arXiv:1206.0553v1 (2012),
https://arxiv.org/abs/1206.0553 . No result from it is a premise of this packet;
no ordinary conclusion is inferred from a rational or 2-adic conjugacy.
A comprehensive external novelty comparison has not been completed.
