# A linear-height rational certificate by global excursion accounting

23 November 2026. Parent checkpoint:
`cb1ae1bb4af0c8d082e9ff466b9fe0c84932301c`.

**Status: a stronger finite rational certificate is proved below; the
universal successful-candidate construction remains OPEN.** The direct
triadic approximation attack did not construct a witness for every
ordinary source. The useful positive result comes from pursuing the
broader rational route in the newest PR178: its finite certificate can
be reduced from a cubic denominator-scale budget to a budget linear in
the odd denominator and logarithmic in the initial numerator/source
height. A mixed-denominator version removes the power-of-three part
before paying for the residual denominator.

The improvement is global. A nearly neutral large-numerator step must
be followed by a uniformly contracting step. Before a numerator repeats,
each small signed value is charged only once. Summing the contractions
over all excursions avoids multiplying a worst excursion length by the
number of possible returns.

The eight public declarations in `TriadicConstruction.lean` formalize
the new local contraction, exact distinct-value charge and final
geometric contradiction. The complete visit/repetition certificate,
parity decoding and mixed-denominator consumer remain written proofs.

## 1. Frozen source and literature boundary

PR178 was refreshed at
`c91b80a3156e640ad471cf30c47721145ae21eb1`. These exact files were read:

| Path | Blob | Role |
|---|---|---|
| `research/central-step-20261123/rational/FINITE_RATIONAL_CERTIFICATE.md` | `598fbfcb64545247d355c5ca7aee4e40f63e0e1e` | The finite rational-candidate interface, small-visit repetition, and parity-tail argument being improved |
| `research/central-step-20261123/rational/lean/RationalExcursions.lean` | `e08a06f2c011699f5fde3a33223f0f93350a56f6` | Earlier finite numerical estimates; read, not imported as a new compile here |
| `research/central-step-20261123/triadic/OPTIMAL_SELECTOR_AND_HEIGHT.md` | `d5fc4e7a3b5cd8b27cac696ef6561b8b12aa8dfd` | The full numerator/exponent optimization and its remaining ordinary-source approximation gap |

The qualitative rational-autoconjugacy/nondivergence equivalence is
already [Monks–Yazinski, *The autoconjugacy of the 3x+1 function*](https://monks.scranton.edu/files/pubs/AutoConjV13.pdf),
Theorem 2.1. Its exact definition of the complementary map and the
theorem were read in the primary paper. The complete finite certificate
is the newer pinned repository input above. No historical priority is
claimed for elementary excursion methods or the rationality reduction.

The preceding local
[`TRIADIC_RIGIDITY.md`](../literature-round4-20261123/TRIADIC_RIGIDITY.md)
proves that a reduced triadic dual exponent counts original-even inputs
before the first 2. It gives a better specialized candidate decision
than the general-denominator test here. The present result does not
replace that specialization or assert existence of a dual.

## 2. Literal finite certificate

Fix a positive ordinary integer `n`, a signed integer `a`, and a positive
odd integer `q`. Use the shortcut Collatz map `T` and signed numerator
map

\[
T(x)=\begin{cases}x/2&x\text{ even},\\(3x+1)/2&x\text{ odd},\end{cases}
\qquad
S_q(w)=\begin{cases}w/2&w\text{ even},\\(3w+q)/2&w\text{ odd}.\end{cases}
\tag{1}
\]

Let `x_k=T^k(n)` and `w_k=S_q^k(a)`. A compatible test at clock `k`
means `x_k mod 2 + w_k mod 2 = 1`. The candidate is `a/q`; reduction
is not needed for this base certificate. Signed numerators and zero are
included.

Put

\[
\begin{split}
B&=n\max(1,|a|),& M&=2B\,16^q,\\
L&=\operatorname{bl}(M),& t_*&=14L+4q+4,\\
H(n,a,q)&=t_*+L=\boxed{15L+4q+4}.
\end{split}
\tag{2}
\]

Here `bl(M)` is the least positive integer with `M<2^L`.

**Finite rational certificate.** If the first `H(n,a,q)` paired tests
pass, then either the original orbit reaches 1 before `H`, or there are
`0<=i<j<t_*` with

\[
                         (x_i,w_i)=(x_j,w_j).
\tag{3}
\]

In particular, the original positive integer is eventually periodic.
The conclusion is not a statement that every candidate or every source
passes the test. If the original coordinate reaches 1, the certificate
has succeeded in proving its convergence; this branch alone does not
identify the tested rational as the exact all-time dual.

Since `16^q=2^(4q)`, the exact bit length is

\[
L=\operatorname{bl}(B)+4q+1,
\qquad
\boxed{H(n,a,q)=15\operatorname{bl}(B)+64q+19.}
\tag{4}
\]

Thus the new horizon is `O(log(n max(1,|a|))+q)`. The preceding
PR178 horizon was
`O(q^2(log(n max(1,|a|))+q log(2q)))`. The improvement is in the
proved candidate budget, not in universal witness existence.

## 3. Uniform contraction over two large clocks

Work until the original orbit reaches 1, so all original states under
consideration satisfy `x>=2`. Define the positive integer potential

\[
                      V(x,w)=x\max(1,|w|).
\tag{5}
\]

A clock is *small* when `|w|<=q`, and *large* otherwise.
At a large clock, `|w|>=q+1>=2`, and the next numerator is nonzero.
Thus the maximum in (5) is the absolute value at both ends of a large
update.

If the original input is odd, it is at least 3. Exact complementary
equations give

\[
\frac{V'}V=\frac{3x+1}{4x}\le\frac56.
\tag{6}
\]

If the original input is even, then

\[
\frac{V'}V=\frac{|3w+q|}{4|w|}\le\frac{3|w|+q}{4|w|}<1.
\tag{7}
\]

For negative `w<-q`, the sharper ratio in (7) is at most `3/4`.
For positive `w>q`, the next numerator is
`w'=(3w+q)/2>2q`. At that next clock, if it too is large, an
original-odd step has ratio at most `5/6`, while an original-even step
has ratio at most

\[
                  \frac{3w'+q}{4w'}\le\frac78.
\]

Every individual large update is nonincreasing. These cases prove

\[
\boxed{V_{k+2}\le\frac78 V_k
       \quad\text{when clocks }k,k+1\text{ are both large}.}
\tag{8}
\]

The constant is independent of `q`. The assumption that the original
has not hit 1 is necessary. For example, with odd `q>=3`, the two
compatible updates from `(x,w)=(1,2q+4)` have product ratio
`(4q+6)/(4q+8)`, which tends to one. The certificate terminates at
original 1 instead of applying (8) there.

## 4. Each small signed value is charged once

For a nonzero small numerator, the exact equations imply

\[
            V'\le\left(1+\frac{q}{|w|}\right)V.
\tag{9}
\]

For an original-odd input, `w` is even and nonzero, and (6) applies.
For an original-even input, `w` is odd and

\[
2\max(1,|w'|)\le3|w|+q,
\]

which yields (9), including an update to zero. A zero numerator is
even, so its compatible original input is odd, its next numerator is
zero, and the elementary bound `x'<=2x` gives `V'<=2V`.

Consider a prefix before the first repetition of a small signed
numerator. Each member of `{-q,...,q}` occurs at most once as a
small input. The total multiplicative charge from nonzero small
inputs is therefore at most

\[
\begin{split}
 \prod_{k=1}^{q}\left(1+\frac qk\right)^2
 &=\binom{2q}{q}^{\!2}
 \le 16^q.
\end{split}
\tag{10}
\]

All factors are at least one, so completing a subset of visited values
to this full product is valid. The two signs are separately charged.
The value zero costs at most a further factor two and appears at most
once before repetition. Thus every such prefix obeys

\[
                           V_k\le M=2B16^q.
\tag{11}
\]

This is the first saving over multiplying a worst small-state cost by
the number of visits. The exact one-sign product and its squared bound
are formalized in Lean.

## 5. Count all large pairs together

Assume for contradiction that no small numerator repeats among the
`t_*` input clocks `0,...,t_*-1`, and that the original has not reached
1 before `H`. Let `s` be the number of small clocks. Then
`s<=2q+1`.

The remaining large clocks form at most `s+1` runs. Pair consecutive
large clocks within each run; leave at most one unpaired clock per run.
If `P` is the number of pairs, then

\[
2P\ge (t_*-s)-(s+1)=t_*-2s-1\ge14L+1.
\tag{12}
\]

In particular `P>=7L`. Interleaving does not change the product
estimate: each pair contributes (8), leftover large steps do not
increase the potential, and all small steps together cost (10) plus
the possible zero factor. Therefore

\[
 1\le V_{t_*}
 \le M\left(\frac78\right)^P
 \le M\left(\left(\frac78\right)^7\right)^L
 \le M2^{-L}<1,
\tag{13}
\]

a contradiction. The inequality `(7/8)^7<=1/2` is an exact rational
inequality. This is the second saving: large clocks from every
excursion are amortized against one initial potential and one total
small-value charge. There is no extra factor of `q` multiplying the
logarithmic initial-height cost.

Hence a repeated small numerator occurs at some first return time
`j<t_*`. Choose its earlier occurrence `i<j`. All small inputs before
`j` are distinct, so (11) gives

\[
                        0<x_i,x_j\le M<2^L.
\tag{14}
\]

## 6. The retained parity tail makes the original state repeat

The map `S_q` is deterministic. Thus `w_i=w_j` implies
`w_(i+t)=w_(j+t)` for every nonnegative `t`. The extra `L` paired
tests in `H=t_*+L` imply that the original windows starting at `i`
and `j` have the same first `L` parities.

For a common length-`L` original word with `p` odd letters and full
carry `C`, the two complete affine equations give

\[
2^L\bigl(T^L(x_i)-T^L(x_j)\bigr)=3^p(x_i-x_j).
\]

Coprimality of two and three yields `2^L | x_i-x_j`. Bounds (14)
force `x_i=x_j`. This proves (3), and determinism repeats the full
paired block forever.

The extra parity tail cannot be omitted: a repeated numerator does
not itself say the original states coincide. All source bounds and
the complete parity word are retained in this argument.

The initial finite test is also the exact endpoint congruence from
the pinned PR178 interface. For original parity `e_k`, even-input
count `b_K`, and complete complementary carry

\[
D_0=0,\qquad D_{k+1}=3^{1-e_k}D_k+(1-e_k)2^k,
\]

it is equivalent to

\[
                     2^H\mid 3^{b_H}a+qD_H.
\tag{15}
\]

A first prescribed parity failure creates a negative 2-adic valuation;
subsequent affine branches cannot restore integrality. Thus (15) tests
the entire actual prefix rather than just an unrelated final equation.

### A complete exact decision for a supplied rational candidate

The same accounting also gives a total decision procedure for the
specific proposition `a/q=Omega(n)`, with every odd denominator allowed.
This procedure uses the literal pair states rather than only a fixed
prefix-congruence acceptance rule. Its state-clock budget is

\[
\boxed{K_{\rm decision}=t_*=14\operatorname{bl}(B)+60q+18.}
\tag{15a}
\]

At each state, reject the candidate if its parity is not opposite to
the original parity. Otherwise:

1. If the original state is 1, accept exactly when the numerator is
   `2q`; reject the candidate otherwise. The original source's
   convergence has of course already been witnessed in either case.
2. If a small numerator `w_j` repeats an earlier small value `w_i`,
   accept exactly when `x_j=x_i`; reject the candidate otherwise.
3. Record a new small value, if any, and take the two literal next steps.

An equal pair repeats a compatible block forever, so acceptance in
step 2 is sound. Conversely, an all-time candidate cannot have
`w_i=w_j` and `x_i!=x_j`: determinism would give the same full original
parity vector from both clocks, and finite parity coding would make
`2^k | x_i-x_j` for every `k`, forcing equality. At original 1,
the unique complementary all-time rational is 2; the same parity-coding
uniqueness proves step 1. Signed and unreduced inputs are allowed.

The global positive-potential contradiction proves that one of these
events or a parity failure occurs at a clock strictly below `t_*`.
Thus at most `t_*-1` ordinary transitions are needed. There is no need
to wait for the extra `L` bits in this exact decision procedure: a
repeated numerator with a different original state already refutes
all-time compatibility. The extra tail is needed in the sufficient
prefix-congruence theorem, where one wants to derive an original repeat
from finite matching alone.

This is a decision for a supplied rational, not a decision procedure
for whether `Omega(n)` is rational. Searching without a proved successful
candidate bound still does not settle arbitrary original sources.

## 7. Remove powers of three before paying for the residual denominator

Suppose the candidate is reduced and

\[
q=3^r q_0,\qquad q_0>0\text{ odd},\qquad 3\nmid q_0.
\tag{16}
\]

Put `B_0=max(1,|a|,3^r q_0)`, `L_0=bl(B_0)`, and `N=bl(n)`.
While the denominator level is positive, the numerator transitions are

\[
\begin{array}{c|cc}
\text{original input}&\text{new numerator}&\text{new level}\\\hline
\text{odd}&w/2&j\\
\text{even}&(w+3^{j-1}q_0)/2&j-1.
\end{array}
\tag{17}
\]

At positive levels the numerator stays a unit at three and has
absolute value at most `B_0`. Consequently `L_0` consecutive
original-odd inputs would divide a nonzero integer of absolute value
less than `2^L_0` by `2^L_0`. This is impossible. Under a compatible
prefix, the `r`th original-even input therefore occurs by a clock

\[
                              J\le rL_0.
\tag{18}
\]

Take `J=0` if `r=0`. One may stop immediately if original 1 has
already been found. At the exhaustion clock, the actual candidate is
`w_J/q_0`, with the same original source state `x_J`. Apply (2) to
that tail. This gives the adaptive total horizon

\[
\boxed{
 J+15\operatorname{bl}\!\left(2x_J\max(1,|w_J|)16^{q_0}\right)
      +4q_0+4.
}
\tag{19}
\]

There is also an explicit sufficient initial budget. Since
`x_J<=n2^J<2^(N+J)` and `max(1,|w_J|)<2^L_0`, the bit length in
(19) is at most `1+N+J+L_0+4q_0`. Equations (18)--(19) imply that

\[
\boxed{
H_{\rm mixed}=15N+(16r+15)L_0+64q_0+19
}
\tag{20}
\]

paired tests suffice for eventual periodicity. The residual denominator
is charged linearly; the full factor `3^r` is not paid as an excursion
state count. This does not claim a general linear bound on `J` in `r`.

For exact recognition, instead apply (15a) at the actual exhaustion
state, stopping earlier at a parity failure or at original 1 with the
exact current rational comparison to 2. Since the tail's `bl(B)` is
at most `N+J+L_0`, the resulting initial state-clock budget is

\[
\boxed{
K_{{\rm mixed},\,\rm decision}
 =14N+(15r+14)L_0+60q_0+18.
}
\tag{20a}
\]

This recognizes the supplied rational itself; rejection makes no
assertion about convergence of the original orbit.

For `q_0=1`, eventual integral paired dynamics force the standard pair
cycle, using the round-four classification. The already published
triadic exact-equality verifier remains substantially better in that
special case. For `q_0>1`, nontrivial positive cycles still need a
separate exclusion. The new rational certificate alone proves no such
exclusion or denominator bound.

## 8. What the direct construction attempt still lacks

For every actual prefix, admissible numerators still lie in the single
translated congruence class

\[
                     a\equiv q\omega_K\pmod{2^K},
\qquad \omega_K\equiv-3^{-b_K}D_K\pmod{2^K}.
\tag{21}
\]

The new target is to find an odd `q` and signed `a` whose match length
funds (4), or whose normalized denominator funds (19) or (20).
No bound accomplishing this for every fixed ordinary source was found.

The broader rational class removes the obstruction to approximating a
fixed nontriadic rational with powers of three only. However, generic
pigeonhole approximation still gives a numerator scale about `2^K/Q`
with denominator at most `Q`, and the denominator may be even. Removing
its two-part loses prefix bits. Even granting oddness, polynomial `Q`
leaves a guaranteed numerator with about `K` bits, which does not fund
the coefficient 15 in (4). The new linear cost in `q` improves the
available search region, but does not turn that generic guarantee into
the required source-specific estimate. A fortunate actual approximation
is not excluded; a theorem guaranteeing it is missing.

The decisive missing inference remains arithmetic information about
the particular translated class (21) attached to one unchanged positive
ordinary source. Real contraction, a candidate at each changing finite
depth, and rational density in the 2-adics do not establish that
source-specific assertion.

## Formal scope and verification boundary

`TriadicConstruction.lean` contains eight public statements:

| Statement | Formal scope |
|---|---|
| `large_step_nonincrease` | Nonzero output and nonincrease on an exact large step |
| `odd_step_five_sixths` | Uniform original-odd contraction before original 1 |
| `very_large_step_seven_eighths` | Uniform one-step bound above twice the numerator threshold |
| `large_two_step_seven_eighths` | The new two-step contraction, uniform in the denominator |
| `nonzero_step_charge` | Magnitude-dependent cost for each nonzero signed numerator |
| `distinct_charge_product` | Exact central-binomial product for one sign |
| `signed_distinct_charge_bound` | The `16^q` upper bound for the two full sign lists |
| `global_charge_contradiction` | The accumulated contraction contradicts a positive final value |

The module retains literal integer branch equations. It does not
formalize the signed visited-value injection, the run pairing,
first-repeat selection, parity-tail reconstruction or mixed-denominator
consumer. Those steps are written in full above. Development compilation
and any independent replay are reported separately by the executing
agent/root, not inferred from the presence of a `.lean` file.
