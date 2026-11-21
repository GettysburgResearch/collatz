# Positive ordinary targets have finite inverse Jacobian Green functions

**Status: unconditional paper theorem and an open continuation toward closure.**
The proof below treats every positive ordinary target and every inverse depth.
It permits hypothetical divergent orbits and nontrivial positive cycles. It
therefore does not prove Collatz. No assertion below has been imported as a
Lean axiom, and this packet contains no new Lean declaration for the analytic
series argument.

The new object retains the actual ordinary predecessors. It produces a finite
positive Poisson solution and, at a critical geometric gap law, a summable
trace at every positive integer of the corresponding ternary cylinder
densities. The distinction between this result and absorption of fixed source
mass is made explicit in section 6.

## 1. Map, paths, and the inverse Green function

Use the ordinary shortcut map

\[
 T(n)=\begin{cases}n/2,&n\text{ even},\\(3n+1)/2,&n\text{ odd}.
 \end{cases}
\]

For an actual path of length `t` from `b`, let `p_t(b)` be its number of
odd input clocks and put

\[
 D_t(b)=\frac{3^{p_t(b)}}{2^t}.
\]

This is the linear coefficient in the exact affine formula for the path;
no differentiability of the integer map is assumed. That formula gives

\[
 2^tT^t(b)=3^{p_t(b)}b+C_t(b),\qquad C_t(b)\ge0.\tag{G1}
\]

If the path contains an odd input, the first such input contributes at
least `3^(p_t(b)-1)` to `C_t(b)`. In particular,

\[
 T^t(b)=n>0\quad\Longrightarrow\quad
 D_t(b)^s\le\frac{n^s}{b^s}\qquad(s>0).\tag{G2}
\]

For any real `s>1`, define the nonnegative extended series

\[
 \mathscr R_s(n)=
 \sum_{t\ge0}\ \sum_{\substack{b\ge1\\T^t(b)=n}}D_t(b)^s.
 \tag{G3}
\]

The zero-clock term is one. Different visits from the same source are kept
as separate terms. The following theorem proves that this series is finite;
its finiteness is not assumed in the definition.

### Theorem G: all positive target values are finite

For every integer `n>=1` and every real `s>1`,

\[
 \boxed{
 \mathscr R_s(n)\le
 \frac{n^s\zeta(s)}{1-(3n/(3n+1))^s}<\infty.
 }\tag{G4}
\]

If `n` is not periodic under `T`, the stronger bound is

\[
 \boxed{\mathscr R_s(n)\le n^s\zeta(s).}\tag{G5}
\]

Here `zeta(s)` denotes the elementary convergent sum
`sum_{b>=1} b^(-s)`. No analytic continuation or zeta-function hypothesis is
used.

**Proof.** If `n` is nonperiodic, a fixed source `b` can visit it at most
once. Two visits at clocks `t<u` would give `T^(u-t)(n)=n`. Therefore G2,
summed over the distinct positive sources, proves G5.

If `n` is periodic, let `L>0` be its least ordinary period and let `p` be
the number of odd inputs in that period. Necessarily `p>=1`, since a
positive cycle cannot consist entirely of halvings. Applying G1 to the
cycle gives

\[
 2^L n=3^p n+C,\qquad C\ge3^{p-1},
\]

and hence

\[
 0<\frac{3^p}{2^L}\le\frac{3n}{3n+1}<1.\tag{G6}
\]

For a fixed source that reaches `n`, all subsequent visits occur after
successive complete periods. Their `s`-th coefficient powers form a
geometric series with ratio `(3^p/2^L)^s`. The first-visit contribution is
at most `n^s/b^s` by G2. Summing the geometric series and then summing over
`b>=1` proves G4. The bound G4 also follows from G5 in the nonperiodic case,
because its denominator is less than one. This exhausts both cases without
classifying the positive cycles. □

At `s=2`, the elementary bound `zeta(2)<=2` gives, for example,

\[
 \mathscr R_2(n)\le
 \frac{2n^2(3n+1)^2}{6n+1}\le\frac{16}{3}n^3.
 \tag{G7}
\]

The last inequality uses `3n+1<=4n` and `6n+1>=6n`.

## 2. An exact finite positive Poisson solution

The two possible immediate predecessors of `n` are `2n` and, only when
`n mod3=2`, `(2n-1)/3`. Regroup G3 according to the last edge. Nonnegative
summation and theorem G justify the regrouping, giving

\[
 \boxed{
 \mathscr R_s(n)=1+2^{-s}\mathscr R_s(2n)
 +\left(\frac32\right)^s
    \mathbf1_{n\equiv2\ (3)}
       \mathscr R_s\!\left(\frac{2n-1}{3}\right).
 }\tag{G8}
\]

This is an unconditional equation on the actual positive integers. It is
not a stationary law postulated after a marked return. In particular,
`R_s(n)=1/(1-2^(-s))` for `3|n`: its only predecessors are its repeated
even doubles.

The correction in G1 is essential. It makes every positive cycle's
coefficient strictly less than one, and is what makes G3 finite even on
such a cycle. Dropping that correction would discard the denominator
control in G6.

## 3. Complete odd words and a ternary cylinder trace

Let `a_1,...,a_k>=1`, define `A_j=a_1+...+a_j`, and set

\[
 S_k=\sum_{j=1}^{k}3^{j-1}2^{-A_j}\quad\text{in }
 \mathbb Z/(3^k),\qquad S_0=0\quad\text{in }\mathbb Z/(1).
 \tag{G9}
\]

The congruence `S_k=n mod3^k` is exactly the condition that all of the
successive inverse operations

\[
 m_0=n,\qquad m_j=\frac{2^{a_j}m_{j-1}-1}{3}
 \quad(1\le j\le k)\tag{G10}
\]

are integral. To see this, reduce G9 modulo three for the first operation,
then remove its first summand and divide the residual congruence by three.
Induction gives every later operation. Because `m_0>=1` and each gap is
positive, every integral `m_j` is a positive odd integer. This proves
ordinary positivity and legality; no completed-integer trajectory is
substituted for an ordinary one.

Thus the word corresponds to the actual path from `b=m_k` to `n`, with
`k` odd inputs and `A_k` shortcut clocks. Its chronological source gap word
is `(a_k,...,a_1)`. The final endpoint `n` may be even: the last leg may stop
inside its final halving run. A fixed source and an actual hitting clock
specify a unique such word.

Define the unnormalized complete-word trace

\[
 G_{s,k}(n)=
 \sum_{\substack{a_1,...,a_k\ge1\\S_k\equiv n\ (3^k)}}
         \frac{3^{sk}}{2^{sA_k}},
 \qquad G_{s,0}(n)=1.
 \tag{G11}
\]

Prepending any number of initial even halvings to an odd-source path
multiplies its weight by `2^(-s e)`. The zero-odd paths contribute the same
geometric sum. Therefore exact nonnegative grouping gives

\[
 H_s(n):=\sum_{k\ge0}G_{s,k}(n)
       =(1-2^{-s})\mathscr R_s(n).\tag{G12}
\]

Consequently every positive target has a finite complete-word trace for
**every** real `s>1`, with the bounds obtained by multiplying G4/G5 by
`1-2^(-s)`. Its equation is

\[
 \boxed{
 2^sH_s(n)=H_s(2n)+3^s\mathbf1_{n\equiv2\ (3)}
     H_s\!\left(\frac{2n-1}{3}\right)+(2^s-1).
 }\tag{G13}
\]

For `s=2`, this gives the particularly simple bound and equation

\[
 1\le H_2(n)\le4n^3,
 \qquad
 4H_2(n)=H_2(2n)+9\mathbf1_{n\equiv2\ (3)}
 H_2\!\left(\frac{2n-1}{3}\right)+3.\tag{G14}
\]

### Normalized probabilities: the discount must remain visible

Give the independent gaps the normalized distribution

\[
 \mathbb P_s(a)=(2^s-1)2^{-sa}\qquad(a\ge1),
\]

and write

\[
 F_{s,k}(n)=3^k\mathbb P_s(S_k\equiv n\pmod{3^k}).
\]

The exact relation to G11 is

\[
 \boxed{
 G_{s,k}(n)=
 \left(\frac{3^{s-1}}{2^s-1}\right)^kF_{s,k}(n).
 }\tag{G15}
\]

For `1<s<2`, the factor inside parentheses is **less than one**. Indeed,
strict concavity of `x^(s-1)` gives
`1+3^(s-1)<2^s`. Finite discounted trace in G12 does not imply finite
undiscounted trace or a uniform bound for `F_{s,k}` in this interval.

At the critical value `s=2`, the factor equals one, and the law becomes
`P(a)=3/4^a`. There is then an unconditional conclusion about the
**undiscounted** ternary cylinder densities at every fixed positive integer:

\[
 \boxed{\sum_{k\ge1}F_{2,k}(n)=H_2(n)-1<\infty,
 \qquad F_{2,k}(n)\longrightarrow0.}\tag{G16}
\]

This does not assert uniformity in a moving target. For contrast, the word
with all gaps one has `S_k=(3/2)^k-1`, hence `S_k=-1 mod3^k`. It gives

\[
 F_{2,k}(-1)\ge(9/4)^k.\tag{G17}
\]

Thus the positive ordinary integer trace and the negative fixed point of the
completed map behave differently. The positive representatives `3^k-1` in
G17 change with `k`; they are not a fixed positive counterexample to G16.

## 4. Why the apparent averaged contraction is not yet absorption

For the homogeneous inverse operator in G8, its mean coefficient over a
complete ternary residue period is

\[
 \lambda(s)=2^{-s}(1+3^{s-1})<1\qquad(1<s<2).\tag{G18}
\]

The new trace theorem proves finite positive solutions on actual inputs,
including this whole interval. It does not make G18 a pointwise contraction
of original source packets. In particular, the ordinary incoming operator
on a weight `W` is

\[
 (\mathcal LW)(n)=W(2n)+\mathbf1_{n\equiv2\ (3)}
 W((2n-1)/3),
\]

with no coefficient averaging. For the natural candidate
`W_s(n)=R_s(n)/(n+1)^s`, G8 gives the exact residual

\[
 W_s(n)-(\mathcal LW_s)(n)
 =\frac{1-\varepsilon_s(n)\mathscr R_s(2n)}{(n+1)^s},
 \quad
 \varepsilon_s(n)=
 \left(\frac{n+1}{2n+1}\right)^s-2^{-s}>0.
 \tag{G19}
\]

The positive finite affine correction has not vanished. At `s=2`, a strict
positive residual requires

\[
 \mathscr R_2(2n)<\frac{4(2n+1)^2}{4n+3}.\tag{G20}
\]

The raw all-state inequality actually fails on a concrete positive input.
The exact ordinary path from `27` reaches `4616` after `45` shortcut clocks,
with `33` odd inputs. Consequently

\[
 \mathscr R_2(4616)\ge\frac{3^{66}}{2^{90}}
 >\frac{85266756}{9235}
 =\frac{4(2\cdot2308+1)^2}{4\cdot2308+3}.
 \tag{G22}
\]

The middle inequality is the exact integer comparison
`9235*3^66 > 85266756*2^90`. Thus G19 is negative at `n=2308`.
The accompanying replay records all 46 states of the 45-clock path and
checks this integer inequality. This rules out the unguarded all-state
claim for this particular weight. It does not rule out a finite-core repair
or a different weight.

### Surplus Green mass supplies a smaller ordinary merger or a cycle

There is a useful positive connection to the companion merger attack:

\[
 \boxed{
 \mathscr R_2(2n)>4n
 \ \Longrightarrow
 \bigl[n\text{ is periodic}\bigr]\ \text{or}
 \bigl[\exists\,0<b<n,\ t:\ T^t(b)=2n\bigr].
 }\tag{G23}
\]

To prove it, suppose that `n` is nonperiodic and that no `0<b<n` reaches
`2n`. Then `2n` is also nonperiodic, since `T(2n)=n`. Moreover, `b=n`
cannot reach `2n`: that would produce a positive return to `n`. Every
predecessor counted by `R_2(2n)` is therefore at least `n+1`, and each
appears at only one clock. G2 gives

\[
 \mathscr R_2(2n)
 \le4n^2\sum_{b\ge n+1}b^{-2}
 \le4n^2\sum_{b\ge n+1}\frac1{b(b-1)}=4n,
\]

contradicting the assumed surplus. Since the G20 threshold is exactly
`4n+1+1/(4n+3)`, every nonpositive residual in G19 at `s=2` lies inside
this dichotomy. The smaller-source conclusion gives
`Basin(b) iff Basin(2n) iff Basin(n)` through actual ordinary paths.

The surplus can be witnessed by a finite packet: nonnegative summation
means some finite collection of actual path contributions already has sum
greater than `4n`. If that packet contains a source below `n`, it supplies
the smaller partner directly. A source equal to `n` gives a cycle; two
distinct visits from the same source give a cycle through `2n`. Otherwise
its distinct sources are all at least `n+1`, and the displayed bound
prevents its sum from exceeding `4n`. Thus this is a finite, ordinary
certificate mechanism, not a fresh parity law or an unexamined limiting
witness.

A decreasing reference common to the good-drift moves and these smaller
mergers is still needed. In particular, a partner below a later, larger
orbit value need not be below the original source. Periodicity in G23
also does not identify the cycle as the one through `1`.

The theorem's cubic upper bound does not imply this essentially linear
bound. Nor does pointwise finiteness show that `W_s(n)` tends to zero as
`n` tends to infinity. A positive weight tending to zero with `n`, with a strict incoming
inequality outside a certified finite core, would force every ordinary
orbit to enter that core, but G19 has not supplied it.

One can see the fixed-source issue directly. Along an actual orbit `n_t`
from `b`,

\[
 n_t=D_t(b)b
   \prod_{\substack{j<t\\n_j\text{ odd}}}
       \left(1+\frac1{3n_j}\right).
\]

The single original source `b` contributes its coefficient power to
`R_s(n_t)`. If the reciprocal sum over its odd orbit is finite, then

\[
 \frac{\mathscr R_s(n_t)}{n_t^s}
 \ge b^{-s}\exp\!\left(-\frac{s}{3}
             \sum_{n_j\text{ odd}}\frac1{n_j}\right)>0.
 \tag{G21}
\]

PR180's reciprocal-summability argument, conditional on its stated
predecessor-density input, is compatible with exactly this persistent
trace on a hypothetical escaping orbit. The new endpointwise finite bound
has not erased a source atom.

The proof of theorem G uses positivity and the affine `+1`, not a
multiplier-three absorption theorem. The same reasoning applies to the
positive `5x+1` cycle with accelerated gaps `(1,1,5)`:
`13 -> 33 -> 83 -> 13`. Its full-cycle coefficient is `125/128<1`, so its
Green function is finite although it never reaches one. This is a direct
scope check on the proposed Green-function route.

## 5. Exact finite replay

[`mass-search/critical_inverse_trace.py`](mass-search/critical_inverse_trace.py)
computes the complete rational density vector on `Z/(3^k)` at `s=2`. The
exponent `a` has period `2*3^(k-1)` modulo `3^k`; grouping its infinite
geometric tail makes every vector entry an exact `Fraction`. For every
residue it checks

\[
 4F_{2,k}(n)=F_{2,k}(2n)+
 9\mathbf1_{n\equiv2\ (3)}F_{2,k-1}((2n-1)/3),
\]

along with normalization, nonnegativity, vanishing on multiples of three,
and G17. It also checks selected positive-target partial sums against the
proved all-depth bound. The actual run covered depths one through four,
with all `3,9,27,81` residues, and normal and optimized Python produced
identical output. These finite executions validate the separate generator;
the all-depth conclusions G4--G16 are the paper argument above.

The receipt is
[`critical-inverse-trace.json`](../../reports/lean-exact-witness-global-20261121/section-mass/critical-inverse-trace.json).
No floating-point experiment is used as theorem evidence.

## 6. Latest source refresh and the remaining inference

The source-specific mass and phase inputs inspected for this attack are:

| Frozen source | Used conclusion and boundary |
|---|---|
| PR176, `3dbe5542fd6a5a1d63b354225d92391471c17002`, `research/lean-global-resolvent-20261121/section/UPPER_COUNT_ATTEMPT.md` | Actual marked predecessor populations give a lower footprint for fixed-floor survivors. Their required upper estimate is not supplied by the section count. |
| PR178, `0bb13b800e4e97f9fd3091b1a3d2e98b49911b7c`, `research/band-return-20261121/{GLOBAL_CLOSURE_ATTEMPT,WEIGHTED_RANK_OBSTRUCTION}.md` | The update from `a8a0736...` adds receipts and paper deductions, with no changed Lean proof input. Its weighted-rank obstruction concerns fixed `(n+1)lambda^clock mu^oddcount` on its specified unrestricted move union, not the exponent-multiset order used in PR177. |
| PR180, `9010a8790535002b6d9ff92304f0ba289e2e98fe`, `research/lean-forward-band-20261121/DIVERGENT_ORBIT_PHASES.md` | Disjoint incoming branches imply reciprocal summability on an injective orbit under the explicit uniform predecessor-density premise. That analytic premise is source-qualified here. |
| PR183, `8659cf62ac685540cadeef320e596c852fbb0959`, `research/band-completion-20261121/mass/RENEWAL_ATTEMPT.md` | First-entrance moments and primitive-to-section remainder bounds retain original source weights. They do not assert renewal absorption. |

An arbitrarily slowly growing floor does not repair the missing fixed-floor
estimate. A fixed failed root `m` may be reached by all its ancestors. Once
a growing floor exceeds `m`, those same sources pass an almost-boundedness
test while still failing convergence to one. Choosing cofinal marked fan
scales cannot keep that floor below `m` forever while letting it diverge.

The present attack supplies a finite all-depth inverse Green function, its
exact positive-integer Poisson equation, the critical unweighted
cylinder-trace decay, and a finite mechanism turning surplus Green mass
into a smaller ordinary merger or a cycle. The unresolved step is the
stronger control needed
in G19, or another actual source-sensitive absorption argument. No complete
selector or full Collatz theorem is claimed.
