# A whole-word attempt at the actual joint counterquery

**22 November 2026. Status: universal completion not obtained.**

This pass retains the actual least-target, minimum-grade, maximum-source
hypotheses. It tries to change an entire physical word and permits an
arbitrary target horizon and an arbitrary clock on the alternative source.
It does not restrict the construction to a bounded block language or a
bounded list of local source surgeries.

The attempt produced an exact description of the required correction
reservoir and a useful size implication of the new survivor bound. It did
not prove that the reservoir contains the required legal word. A concise
control below shows that even allowing **all** alternative words and
alternative clocks does not restore a source-clock deadline.

## Frozen inputs

* [PR177, joint counterquery](https://github.com/GettysburgResearch/collatz/blob/e4ca639326bac73da8c2a698dec8a749e5efbe68/research/lean-exact-witness-global-20261121/JOINT_MINIMAL_COUNTEREXAMPLE.md)
  supplies the simultaneous original-target and complete-source induction
  resources.
* [PR180, actual arithmetic rigidity](https://github.com/GettysburgResearch/collatz/blob/a66a44c9bf058cd7efe1018827ddda9a13297a21/research/deep-machinery-20261122/ARITHMETIC_RIGIDITY.md)
  supplies the actual first-hit bound `2A<t`, the strict target multiplier
  bound, and the impossibility of copying the unaltered target prefix onto
  a smaller supplied source endpoint.
* [PR175, bounded languages](https://github.com/GettysburgResearch/collatz/blob/08fe1388ad63c758680b3695249aca319515c47d/research/lean-global-closure-20261121/machinery/BOUNDED_LANGUAGE_SOURCE_RIGIDITY.md)
  and [PR176, context-free certificates](https://github.com/GettysburgResearch/collatz/blob/00018ce11fa657b5f3fae072e5567a1d93184c2b/research/lean-global-resolvent-20261121/overview/machinery/CONTEXT_FREE_CERTIFICATE_OBSTRUCTION.md)
  rule out treating a sound fixed grammar of bounded-gap complete words as
  a cofinal source selector. Arithmetic guards are retained here.
* [PR185, tail-aware arithmetic](https://github.com/GettysburgResearch/collatz/blob/980d40fc4afeaaf8f2a9256f322acf3e4568e013/research/deep-closing-20261122/ARITHMETIC_ATTACK.md)
  corrects the earlier long alphabet-four example with a genuinely cheaper
  complete source. The control here therefore includes an all-certificate
  grade argument, not only a finite record census.

The new S-unit sparse-endpoint theorem in PR177 was also inspected. It
constrains returns between actual sparse endpoints; it supplies neither a
target-word correction nor a uniformly bounded target-word complexity.

## 1. The attempted universal construction

Write the shortcut map as `T`, and let `t` be the least bad positive
integer in a putative `JointBadQuery`. For any `k>=0`, set

\[
 N=T^k(t),\qquad 2^kN=3^o t+C.
 \tag{1}
\]

Instead of attaching the actual target prefix to a new endpoint, try to
find a **different complete finite prefix ending at this same actual N**.
Its starting point `u<t` would already converge by the original-target
hypothesis. The common endpoint would then prove convergence of `t`.
Neither prefix is required to have the source word's length or odd count.

For an alternative ordinary clock `m` and odd count `h`, the complete legal
correction set is

\[
 \mathcal C_{m,h}=
 \left\{\sum_{i=0}^{h-1}3^{h-1-i}2^{d_i}:
       0\le d_0<\cdots<d_{h-1}<m\right\}.
 \tag{2}
\]

For `h=0` the only correction is zero. The positions `d_i` are the odd
inputs of the entire shortcut word. A member of (2) is not replaced by an
arbitrary rational-base digit.

The required reservoir condition is exactly

\[
 \boxed{\begin{gathered}
 C'\in\mathcal C_{m,h},\qquad
 C'\equiv2^mN\pmod{3^h},\\
 0<2^mN-C'<3^h t.
 \end{gathered}}
 \tag{3}
\]

It yields the positive integer `u=(2^mN-C')/3^h<t`.
The affine equality also certifies the actual parity word. Reduced modulo
two, it forces the first prescribed parity of `u`; taking that branch
and dividing its contribution reduces to the shorter word. Induction
establishes every branch and gives `T^m(u)=N`.

Thus (3) would close the full counterquery, including cycles, if its
existence were proved for some `k,m,h` on every joint witness. Formula (3)
is the exact arithmetic goal of this attempt, **not an existence theorem**.

## 2. What the actual source surplus does buy

Let the complete odd source have `r` odd steps, ordinary clock `A`, and
source `q`. The pinned PR180 theorem retains the original target floor and
proves

\[
 2A<t,\qquad
 6\,3^o>5\,2^A>5\,3^r q,
 \tag{4}
\]

where `o` is the target's actual odd count through the same clock `A`.
Its stronger pre-specialization invariant gives, for `N=T^A(t)`,

\[
 (3t+1-A)2^A N\le(3t+1)3^o t,
 \qquad
 \boxed{2^A N<\frac65\,3^o t.}
 \tag{5}
\]

Consequently, **any positive integral A-clock inverse word for N with
more than o odd events already starts below `2t/5`**. Indeed its correction
is nonnegative, and

\[
 u=\frac{2^AN-C'}{3^h}
 <\frac65\,3^{o-h}t\le\frac25t\qquad(h\ge o+1).
 \tag{6}
\]

For an equal-odd-count alternative, the size and congruence test is
instead

\[
 C'\equiv C\pmod{3^o},\qquad
 0<C'-C<3^o t.
 \tag{7}
\]

These deductions make the size comparison easy once the alternative
exists. The supplied complete source has **fewer** odd events than the
actual target by (4); its correction is not the larger-odd-count word
required in (6). Its endpoint is also one rather than `N`. No source
minimality hypothesis licenses either change without a new legal word.

For a different inverse clock `m`, the same comparison reads

\[
 u<\frac65\,2^{m-A}3^{o-h}t.
 \tag{8}
\]

Thus allowing more inverse clocks introduces a compensating odd-event
cost. It does not by itself supply an unbounded reservoir of smaller
sources.

## 3. A quantitative check on the proposed reservoir

For one fixed `m,h` and one word, integrality of its inverse selects
exactly one endpoint residue modulo `3^h`, because `2^m` is invertible
there. There are `binomial(m,h)` words. In a common modulus `3^m`, the
fraction of endpoint residues admitting any inverse word with
`h>=ceil(5m/8)` is therefore at most

\[
 \sum_{h\ge\lceil5m/8\rceil}\binom mh3^{-h}
 \le 5^{-5m/8}(1+5/3)^m
 =\left(\frac{16777216}{20503125}\right)^{m/8}.
 \tag{9}
\]

The middle inequality multiplies the terms by `5^h` and uses
`5^h>=5^(5m/8)`. The final rational base is strictly less than one.
This bound includes all words and all possible collisions of their
endpoint classes; it does not assume independent parity bits.

This is an **unconditional residue counting bound**, not a statement about
the endpoint distribution of an actual orbit. In particular, an actual
high-odd-count prefix already places its endpoint in one of these sparse
classes. The estimate cannot decide whether that same selected endpoint
has another, better inverse word. Conditioning on the actual supplied
source and target history is precisely the arithmetic information still
missing from the proposed reservoir argument.

## 4. One control with the full extremal grade scope

Take

\[
 t=1263,\qquad S=820=4\cdot205,\qquad
 W=[3,3,3,1,2,3,4].
\]

The literal prefix `[3,3,3]` ends at eleven; `W` is a complete certificate
to one. Its odd-source clock is 19, and the powered-source clock is 21.
The source floor holds since every positive-clock source value is at most
410, below `floor((t-1)/2)=631`. Every nonempty source prefix contracts.

This source is genuinely extremal. Let `G` be its complete grade. The
existing one-four language classification, also used in
[PR185's extremal-clock proof](https://github.com/GettysburgResearch/collatz/blob/980d40fc4afeaaf8f2a9256f322acf3e4568e013/research/central-obstruction-20261122/EXTREMAL_SOURCE_CLOCK_FAILURE.md),
has odd sources

\[
 \{3,5,7,9,11,13,17,19,25,29,33,45,51,77,205,273\}.
\]

Any grade at most `G` has gaps at most four and at most one four. With
no four, the odd source is one and the powered source is at most eight.
With one four, its initial exponent is at most two and its odd source
belongs to the displayed set. The complete word of 273 is `[2]++W`,
followed possibly by terminal gap-two padding. Thus its exponent-two
certificate is already above `G`. The word of 205 is `W` followed by
padding; exponent two and no padding gives exactly `G`, and padding
raises it. It follows that

\[
 \max_{\text{grade}\le G}S'=820,
 \qquad \max_{\text{grade}<G}S'=546=2\cdot273.
 \tag{10}
\]

All other displayed odd sources are at most 77, except 205 and 273;
the latter two with exponent at most one give at most 546. The `546`
certificate is below `G` at grade five, so the second bound is attained.
This covers every initial exponent and every terminal padding, not just
sampled certificates. Since `1093<1263<=1641`, `G` is the minimum grade
capturing this target and 820 is the maximum source at that grade.

Nevertheless, **for every positive u<1263, every clock m>=0, and every
target clock 0<=k<=24, one has `T^m(u) != T^k(1263)`**.
The control verifies this unbounded-clock statement with a finite closed
set: the completed orbits of all 1262 smaller positive starts form a
2008-element set `F`, closed under `T`, containing every such start.
Every displayed target state through clock 24 lies outside `F`.
Closure and induction exclude every alternative clock, not merely the
clocks searched during its construction.

The first smaller merger is

\[
 T^{25}(1263)=1622=T(1081),
\]

and the first descent is `T^26(1263)=811`.
This target converges. The control excludes a strategy demanding a
smaller merger by the supplied source horizon; it does not refute
`FloorIntervalStep`, later mergers, or fully adaptive rewrites.

## 5. Exact stopping point of the universal attempt

For arbitrary `k`, (3) retains all alternative words and both clocks.
The minimum positive ancestor of `T^k(t)` is nonincreasing with `k`:
any old ancestor also reaches the next endpoint. That observation gives
no strict drop. Under a least-counterexample assumption the minimum
would remain exactly `t` at every clock.

I did not prove that the complete extremal source forces a strict drop
of this minimum, a member of (3), or a descending complexity measure
when the selected word and clock change. The source surplus proves
the favorable comparison (6) **after integrality is supplied**; it
does not prove that integrality. The residue bound (9) does not justify
replacing the actual endpoint by a generic one. The finite control
shows why stopping at source exhaustion is insufficient even for the
more permissive whole-word merger construction.

No new Lean theorem is claimed. The exact finite control and the
all-parameter arithmetic deductions are kept separate from the missing
universal existence step.

## 6. Combination with the fresh sparse-return and run-clock results

The subsequent PR176 head `fdcb137214f4be8ac30dbb025d6eeb6568e22e2a`
adds `LOGARITHMIC_SPARSE_RETURN_DESCENT.md`: for fixed `S`, `C>0`
and `0<eta<=1`, sufficiently large actual endpoints with at most `S`
binary runs, separated by `h<=C log n` odd steps with
`h` outside the finite set `H_S`, force an input below `n^eta`.
PR177 head `0444986571f09f302cb3687b4bba3552600e4119` adds the
all-input clock and run bounds `a<=2R(n)` and
`R(U(n))+1<=3R(n)`. Exact paths, Git blob hashes, SHA256 hashes,
and the read-only evidence scope are recorded in `input-pins.json`.
The cited Lean source is not counted as new compilation in this packet.

**An actual logarithmic-window restriction.** Fix `S>=1` and `C>0`.
For every sufficiently large least bad target `t`, at most
`|H_S|+1` of its first `floor(C log t)+1` odd states can have at
most `S` binary runs. Here the logarithm is natural and the threshold
depends only on `S,C`.

The least bad target is odd, since an even target immediately halves
to a smaller positive start. To prove the count, put `B=1+C log 2`
and `eta=1/B`. Write the actual
odd states as `q_i`. Leastness gives `q_i>=t`, while
`U(q)<=2q` gives `q_i<=2^i t<=t^B` throughout the specified
window. For two low-run visits `i<j`, put `n=q_i` and `h=j-i`.
Then `h<=C log t<=C log n`, and every intervening input is at
least `t>=n^eta`. The logarithmic theorem therefore forces
`h` to lie in `H_S`, once `t` exceeds its fixed threshold.
Anchoring at the first low-run visit makes all later differences distinct
members of `H_S`, proving the count. This uses the original target
floor and actual odd clocks; it does not replace the target word by a
symbolic history.

**Why the run-clock bound does not supply the required pair.** There is
an elementary obstruction to choosing the cutoff after choosing the
clock:

\[
 \boxed{\{1,2,\ldots,2S\}\subseteq H_S\qquad(S\ge1).}
 \tag{11}
\]

Recall the pinned definition: `H_S` contains the nonzero absolute
ternary valuations of positive coordinate ratios in all nondegenerate
signed `{2,3}`-unit zero relations with at most `4S` terms.
Expand `3^h` into its distinct nonzero binary powers. The relation
`3^h-sum(2^b)=0` is nondegenerate: a proper subset of its negative
terms has sum strictly smaller than its sole positive term. The ratio
between that term and any binary power has ternary valuation `h`.
For `h=1,2` there are three terms. For `h>=3`,
`3^h<2^(2h-1)`, so there are at most `2h-1` binary positions
and at most `2h` relation terms. If `h<=2S`, this is at most
`4S`, proving (11).

Consequently, the available forward estimate
`R(U^h(n))<=3^h R(n)` provides a common endpoint cutoff
`S_h=3^h R(n)` for which `h<=2S_h`; this is an **exceptional**
separation by (11). It cannot certify the nonexceptional return needed
for the descent theorem. Allowing the cutoff to grow also changes the
theorem's threshold, which is only asserted for each fixed cutoff.

The phase occupation estimate and the logarithmic-window restriction
both limit visits to fixed low run counts. They do not give opposing
bounds. The attempted whole-word combination still needs either an
actual nonexceptional sparse pair within a permitted logarithmic window,
or a member of the legal smaller-ancestor reservoir (3). The joint
minimum-grade and maximum-source hypotheses have not been shown to
force either existence statement. The minimum ancestor can therefore
still remain `t` under every adaptive choice of endpoint and inverse
clock allowed by the current argument.

## Reproduction

`python check_whole_word_control.py` writes `whole-word-control.json`.
It checks the source path and all prefix coefficients, certifies the
finite low-gap predecessor closure behind the one-four source list,
completes all smaller ordinary orbits, checks their union is forward
closed, and checks disjointness from the actual target prefix. Every
failure raises an explicit exception. The complete closed set is saved
so the universal alternative-clock conclusion is reviewable.
