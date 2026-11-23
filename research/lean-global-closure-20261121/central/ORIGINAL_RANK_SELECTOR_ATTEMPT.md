# Direct attempt at the original-rank universal selector

Date: 2026-11-22. **Outcome: the universal successful selector was not
proved.** This is a record of an attempted closing argument, not a new
coverage theorem or a claim of Collatz progress from another equivalent
formulation. No finite source census is used as a mathematical premise.

The attempted proof combines the complete-word signed compiler, the new
global original-target floor, the larger-source tie at equal grade, and
the rational-shadow return interface. The exact obstruction is recorded
after the full source and target identities, rather than hidden behind
the existence of a total arithmetic transition.

## Frozen inputs actually used

| Source | Commit | Input |
|---|---|---|
| PR175 | `728389c2ad4796853948250a90188b0697483d92` | `SignedCarry.lean`, `SignedCarryReturns.lean`, complete literal-word transport and the existing funded absorbing guards. |
| PR177 | `8ef9bf0d828fc533721dee1f90c5d78fac80ad39` | `ROOTED_SOURCE_FLOOR.md`, `NEGATIVE_SHADOW_RETURN.md`, `STRICT_PREFIX_CONTRACTION.md`, and the actual `BoundedGapCofinal.lean` high-gap dispatcher. |
| PR180 | `ab3973099f0d285bbe88972382ad599bb02cd460` | `research/lean-joint-20261122/MIXED_COVER.md`: mixed source/target induction, finite reverse-source tie, literal interior surgery, and the variable two-run permutation. |
| PR185 | `53f01ca5b443ef57ef2160b4996dbb2cc87f7395` | `research/multiple-attacks-20261122/RATIONAL_SHADOW_DISPATCH.md`: a repeated physical source block can pay an explicitly certified rational-shadow contraction. |

The upstream inputs and their exact byte hashes are recorded in
`SOURCE_SNAPSHOT.json`. This pass did not rerun their old builds or count their
results as new theorems.

## 1. The all-word system with its complete source retained

Let the supplied actual complete odd certificate be

\[
q_0\xrightarrow{a_0}q_1\xrightarrow{a_1}\cdots
\xrightarrow{a_{m-1}}q_m=1,
\qquad 3q_j+1=2^{a_j}q_{j+1},\quad a_j\ge1.
\tag{1}
\]

In the low-alphabet problem, every `a_j<=4`; no bound on `m` is
assumed. The literal suffix at every `q_j` is part of the input.
Before the fixed terminal tail, the same discussion can stop at
`q_m=11` instead, retaining its proved `[1,2,3,4]` tail.

Write

\[
A_j=\sum_{i<j}a_i,\qquad
C_j=\sum_{i<j}3^{j-1-i}2^{A_i}.
\]

Then the exact source identities, including the complete-word
integrality condition, are

\[
2^{A_j}q_j=3^j q_0+C_j,
\qquad
3^m q_0+C_m=2^{A_m}.
\tag{2}
\]

In particular `C_m=2^A_m mod 3^m`. The positivity and oddness of the
intermediate states in (1) are retained; the word is not replaced by
an arbitrary sequence over four formal letters.

Let `N` be the original queried target. A known actual target prefix
may already have taken it to `y_0=T^kappa(N)`. Represent the current
target by

\[
y_j=3^{p_j}q_j-c_j>0.
\tag{3}
\]

The original positive-nine compiler starts at `(p_0,c_0)=(2,-2)` and
`y_0=9q_0+2`. Other initial pairs require their actual input identity;
they cannot be freely substituted for the original interval query.

Define the signed complement map on integers by

\[
S(z)=\begin{cases}z/2,&z\text{ even},\\(3z-1)/2,&z\text{ odd}.
\end{cases}
\]

While `p_j>0`, set

\[
z_j=3^{p_j-1}+c_j,
\quad o_j=\#\{\text{odd inputs in the first }a_j\text{ steps of }S(z_j)\}.
\]

Let `B_j>=0` be the exact correction of that finite parity word, so

\[
2^{a_j}S^{a_j}(z_j)=3^{o_j}z_j-B_j.
\]

The complete compiler gives the actual, not formal, recurrence

\[
\boxed{
p_{j+1}=p_j-1+o_j,\qquad
c_{j+1}=\frac{3^{o_j}(3^{p_j-1}+c_j)-B_j}{2^{a_j}},\qquad
y_{j+1}=T^{a_j}(y_j).}
\tag{4}
\]

The tail in (1) remains the same supplied tail. For the initial pair
`(2,-2)`, the first update is exactly `(a_0+1,1)`, and all later debts
are nonnegative. Reaching `p=0` therefore gives `y<=q` and a genuine
lower-grade query. Reaching another proved absorbing cone can also
close, with its stated rank and residue hypotheses.

### The normalized potential that was tested

Put `x_j=c_j/3^p_j`. Equation (4) gives

\[
\boxed{
x_{j+1}=\frac{1+3x_j}{2^{a_j}}
-\frac{B_j}{2^{a_j}3^{p_{j+1}}}.}
\tag{5}
\]

For the positive separation `delta_j=q_j-x_j=y_j/3^p_j`, it gives

\[
\delta_{j+1}=\frac{3\delta_j}{2^{a_j}}
+\frac{B_j}{2^{a_j}3^{p_{j+1}}}.
\tag{6}
\]

This explains why a decreasing relative source scale and an increasing
carry power can coexist. In particular `p` alone is not a decreasing
rank, and dropping the positive second term in (6) would reverse the
estimate needed to prove target descent.

If `O_j=sum_(i<j) o_i` and `H_j>=0` is the complete positive target
correction at ordinary clock `A_j`, the exact accumulated identities are

\[
\begin{gathered}
p_j+j=p_0+O_j,\\
2^{A_j}y_j=3^{O_j}y_0+H_j,\\
2^{A_j}c_j=3^{p_j}C_j+3^{O_j}c_0-H_j.
\end{gathered}
\tag{7}
\]

All three equalities use the same physical source and target clocks.
There is no independent resampling of target parities.

## 2. The original floor and the attempted universal inequality

For an original residual target `N>=177` with `N=3 mod 4`, PR177 supplies a complete
source `Q=2^e q_0`, `1<=e<=3`, with

\[
L=(N-1)/2<Q<N,
\qquad T^{j+1}(Q)\le L\quad(j\ge0).
\tag{8}
\]

Its literal low-alphabet prefix to eleven is nonempty. Every subsequent
odd source endpoint `q_j` and its next ordinary step remain below the
same original floor. Since `L` is odd, the safe future cannot equal
`L`. Hence

\[
3q_j+2<N.
\tag{9}
\]

A physical target return into `0<y<=3q_j+2` is consequently below the
original `N`, even if earlier target states exceeded it. A padding
`2^f q_(j+1)` with `f<a_j` is also an actual state in this same safe
source orbit; its proved interval cone is another valid original-floor
return. An old, already-consumed large gap does not make that padding
an actual state of the current suffix.

The attempted universal proof was to combine (2), (5), and (8) to force
one of these returns or another funded guard. Written without a hidden
change of target, the accumulated inequality needed at a source clock is

\[
\boxed{3^{O_j}y_0+H_j<2^{A_j}N.}
\tag{10 -- NOT PROVED UNIVERSALLY}
\]

For `y_0=N`, this is `H_j<(2^A_j-3^O_j)N`. For an already enlarged
carry `y_0>N`, proving descent merely below `y_0` is insufficient; the
right side of (10) still contains the original `N`.

The complete source equation controls `C_j` and the source odd count
`j`. It does not yet supply the required upper bound on the actual
target odd count `O_j` and its correction `H_j`. Equations (5)--(7)
preserve their dependence exactly, but do not create that upper bound.
The sign in (6) gives a lower bound on separation when its correction
is discarded, which is the wrong direction for (10).

At the terminal source one, (3) becomes `y_m=3^p_m-c_m>0`. That
equation by itself is not a successful exit: every positive integer
`Y` has such a representation by choosing a sufficiently large `p`
and `c=3^p-Y`. This does not assert that every such pair is reached by
the initial compiler. It identifies why the terminal equation cannot
replace an argument using the preceding complete-word constraints.

The new negative-shadow source rule does not fill this inference. It
gives an actual growing source prefix under its separated-negative-block
guard. The same latest source packet proves that complete bounded-four
sources whose every later odd state is smaller are cofinal. Therefore a
universal proof must also act on complete words outside that growth
guard; extending a source-growth search alone cannot be its totality
argument.

## 3. The all-word exchange and its exact grade debt

The second attempted route uses PR180's permitted larger source at the
same complete grade. Its published variable-length successful rewrite
has a direct extension as an ordinary certificate transformation.

Suppose the actual supplied source starts

\[
q\xrightarrow{3}u\xrightarrow{2}v_1\xrightarrow{2}\cdots
\xrightarrow{2}v_k\xrightarrow{4}a\xrightarrow{b}z,
\qquad k\ge1,
\tag{11}
\]

followed by its complete literal tail at `z`. Then the larger source
`q+4` has the actual segment

\[
q+4\xrightarrow{2}2u+3\xrightarrow{4}\frac{v_1+1}{2}
\xrightarrow{2}\cdots\xrightarrow{2}\frac{v_k+1}{2}
\xrightarrow{1}4a+1\xrightarrow{b+2}z.
\tag{12}
\]

Every shifted endpoint is odd: the interior old gaps two and the final
old gap four force `v_i=1 mod 4`. The final identity is
`3(4a+1)+1=4(3a+1)=2^(b+2)z`. Thus this is an all-length physical
transformation, retaining the old complete suffix. No arithmetic
exception or terminal search is suppressed.

Retain the initial powered-source exponent and cancel the common tail.
The old odd-gap multiset is `[3] ++ [2]^k ++ [4,b]`; the new one is
`[2,4] ++ [2]^(k-1) ++ [1,b+2]`. After cancelling common grades,
the comparison is exactly

\[
\boxed{\text{old remainder }\{6,2b\},\qquad
       \text{new remainder }\{2,2b+4\}.}
\tag{13}
\]

For `b=1` the grades agree, and the source increases. This is the
published successful rule. For every `b>=2`, the highest changed grade
increases. At `b=2`, an extra grade eight is created; at `b=3,4`, the
new gap is five or six. A recursive interval query at this larger
source is therefore not licensed by the original rank hypothesis.

The other structural exit changes the affine state. If the final old
gap in the two-run is followed by a gap three, so
`3v_k+1=8a`, then

\[
3\frac{v_k+1}{2}+1=2(2a+1).
\tag{14}
\]

The new path ends at `2a+1`, rather than `a`. The original complete
tail certifies `a`, not this new endpoint. Closing the transducer at
that point would require a further actual continuation and a paid
complete certificate. It cannot copy the old tail onto `2a+1`.

### Testing direct composition with the high-gap rule

For `b>=3`, (12) creates a high gap. I inspected the actual PR177
`high_gap_replacement` and `high_gap_powered_interval_rule` to test
whether immediate composition pays (13) against the original source.

The high-gap rule deletes the intermediate prefix through the created
gap and builds a cofinal ordinary prefix over `{1,2,3,4}` before the
same literal tail. Its proof controls each inserted grade by the
created grade `2b+4`. It places no bound on the number of inserted
gap-fours or on the entire inserted multiset relative to (11).

Consequently its conclusion is below the intermediate grade, not
automatically below the original grade. In the original alphabet-four
comparison, an uncontrolled number of new grade-eights can exceed the
original multiplicity. The missing composed claim is a construction
whose *final* complete grade is below the original one while its
source still covers the target. I did not prove that construction.
For `b=2`, the newly created gap is only four, so even the high-gap
premise is absent.

The equal-grade finite defect permits only an equality of the full
grade multiset. It cannot authorize these strict increases. Replacing
it with unrestricted reverse numerical order, or silently switching
to total-clock order, would remove the well-founded justification.

## 4. Rational shadows and the exact unresolved inference

The repeated-block compiler can supply (10) when an actual sufficiently
long repeated source block gives a binary pin for the **original**
target and a certified rational prefix pays its full affine offset.
This remains useful even when `p_j` grows. It is not valid to apply
its descent only to an enlarged current carry and then identify that
carry with the original target in (10).

For a target expressed after an arbitrary source prefix, one can pull
back the original affine expression to that later source endpoint.
Its offset may be negative and its denominator is an odd power of
three. The signed arithmetic can still be tracked exactly. What is
not supplied is a contracting rational prefix for every resulting
shadow, or the occurrence of its required repeated source block in
every complete word. At a terminal repeated gap-two loop, the actual
source is its exact fixed point one, so the compiler's fixed-source
exception retains the unknown target rather than eliminating it.

The attempted universal dispatcher therefore remains incomplete at
the following specific inference:

> For every supplied complete bounded-four source word in the
> original interval query, the actual all-word evolution must reach
> a guard funded by the original complete grade, or satisfy an
> original-target inequality such as (10); the complete-word
> integrality and the exchange rules must force this success.

I did not establish that inference. The failed proof does not license
it by prefix exhaustion, by source cofinality, by an intermediate
high-gap rank decrease, or by a finite dictionary of rational shadows.
The calculations above identify the exact target multiplier/offset
estimate and the exact exchange grade debt that a continuation must
resolve. No additional Lean module was added merely to formalize
this still-unproved totality premise.
