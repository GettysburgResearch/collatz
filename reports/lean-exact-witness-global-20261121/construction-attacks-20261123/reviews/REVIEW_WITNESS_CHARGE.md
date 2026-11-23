# Independent review: complete-witness charge and power induction

23 November 2026. Reviewer: the `macro_selection` research lane.

**Verdict: accepted at the manuscript's stated scope.** I found no gap in
the written rational-slope classification, the all-clock half-germ
exclusion, the finite-table consequence, the finite-seed power-germ
barrier, or the unbounded edit lower bound. The standalone Lean file
compiled again during this review, with 21 public axiom audits. The
original residue-512 implication and a universal successful witness
selector remain open; neither follows from these results and neither is
claimed by the reviewed manuscript.

## 1. Exact reviewed sources and independence

All three source files are under
`research/lean-exact-witness-global-20261121/construction-attacks-20261123/witness/`.

| Source | SHA256 |
|---|---|
| `WITNESS_CHARGE_AND_POWER_INDUCTION.md` | `c20dbdde1ebb7e1aa7d4a71e7e13091755f8a98b059bebc381d495c14767b591` |
| `WitnessCharge.lean` | `c0c9d658f0de0c344f77f0f4c0a8d11a4f8484695aa953d8d14ec5fb2acc115d` |
| `check_witness_charge.py` | `f8d239f4c397771a62e3cda0570536bf26034a28fc1986db8522be2cc75c6e7e` |

I authored the separate template-selection lane in this checkpoint. I did
not author or edit these witness-lane sources. I independently read the
manuscript, reconstructed the arguments below, inspected the full Lean
source and exact checker, and reran the new Lean file and checker. The
shared project context and the retained four-step family were available
to both lanes. This is an independent argument review within the same
research team, not an external peer review.

## 2. Charge invariance and the rational-slope orientation

For the ordinary shortcut map, the finite profile charge is
`chi(n,L) = 2*p(n,L)-L`. An odd step contributes one and an even step
minus one. Both complete returns to one therefore have equal charge:
the intervening ordinary path is a whole number of the `1,2` cycles.
The formal proof handles arbitrary ordering of the two supplied clocks;
it does not silently assume one certificate is the first hit.

The `complete_tail` construction is also correct after a supplied hit.
Starting with `T^L(n)=1`, the tail after clock `k` is certified for
`L+k` additional steps, since the combined clock is `L+2k`. Thus every
use of a tail beyond the original certificate has explicit legal
standard-cycle padding.

For WC5, let the source and target word profiles be `(k,p)` and `(l,q)`
and let the target input be `a*x+b`, with `a=2^u*3^v>0`. Equality of
affine derivatives gives

\[
\frac{3^p}{2^k}=2^u3^v\frac{3^q}{2^l},
\qquad p-q=v,\qquad l-k=u.
\]

Consequently the complete-charge difference is `2v+u`, in precisely the
orientation printed in WC5. This calculation retains the original
half-map orientation: for `u=-1,v=0`, the target charge is the source
charge plus one.

For sufficiency, write the supplied profiles as `(L,r)` and `(M,s)`.
Choose nonnegative terminal-cycle counts `i,j` with
`i-j=v-(r-s)`. The charge hypothesis gives

\[
(L+2i)-(M+2j)=-u,\qquad (r+i)-(s+j)=v.
\]

Both padded maps end at one, and their derivatives agree after insertion
of the rational slope. Their constants agree as well. There is no
integrality gap in lifting this to an ordinary progression. For example,
with padded source clock `k` and target clock `l=k+u`, the positive
integer increment

\[
D=2^k3^{\max(-v,0)}
\]

satisfies `D/2^k` integral and
`a*D=2^l*3^max(v,0)`. Both actual parity words are therefore preserved
for every nonnegative progression parameter. This supplies the
unbounded family required by the manuscript's definition.

WC5 remains a written theorem. The module formalizes its two specified
specializations and the exact cylinder lift; it does not falsely label
the rational-prime-factor argument as kernel-checked.

## 3. Half-germ bridge and the infinite exclusion

For an affine identity along the actual half-map, derivative equality
forces equal odd counts and source clock exactly one larger than target
clock. Thus `HalfGerm` is precisely the finite-word condition for that
architecture. A numerical meeting alone imposes neither derivative
condition; the manuscript explicitly keeps that distinction.

The constructive half-germ proof pads the two witnesses by the other's
odd count. The resulting odd counts are equal, and charge balance makes
the clocks differ by exactly one. Necessity appends a common actual
tail and cancels its charge. The lift preserves the original relation
`2*y=x+1` exactly, not merely its residue.

For the retained source family, set `m=27k` and
`K=(4^m-1)/81`. The ordinary source profile is

\[
T^{2m+8}(256K+1)=1,\qquad p(256K+1,2m+8)=4,
\]

and the target prefix is

\[
T^{2m+7}(128K+1)=3^m+1,\qquad
p(128K+1,2m+7)=m+4.
\]

These give source charge `-2m` and target prefix charge one. The family
and its tuple are correctly credited to the retained work; the new Lean
file reproves the required profiles from `4^m=81K+1`.

If a half-germ existed, the source's complete witness first constructs a
complete target witness. Only then is the target's complete charge used.
It must be `1-2m`; removing the forced prefix constructs a complete
witness of `3^m+1` with charge `-2m`.

The finite height inequality

\[
2^L T^L(n)\le 4^{p(n,L)}n
\]

is valid for every actual prefix. At an odd positive input it uses
`3n+1<=4n`; at an even input it is equality. A complete witness and
`n<2^B` force `chi(n)>-B`. Since `3^m+1<2^(2m)` for `m>=2`, the derived
charge is impossible. This proves WC16 with no bound on either merger
clock or terminal padding and without assuming target convergence.

The finite-table corollary follows at its stated architecture. After
substituting the half-map, a fixed pair of word formulas with unequal
slopes has at most one numerical solution. A balanced pair would be a
half-germ and hence covers no member of this infinite family. Finitely
many such pairs and finitely many numerical exceptions cannot cover the
family. This does not exclude an infinite, source-dependent,
inhomogeneous, or recursive compiler.

## 4. Power signatures and the finite-seed barrier

For the family `3^a*w+1`, equality of parameter derivatives forces a
common physical clock and `p+a=q+b`. The invariant is therefore
`J(a)=2a+chi(3^a+1)`, with the signs in WC18 and WC19 correct.
The positive construction pads by `s+b` and `r+a` cycles, respectively;
signature equality makes the clocks equal and the full parameter
coefficients match.

Transitivity genuinely covers arbitrary finite chains. Extending an
`a,b` germ by the second germ's clock and a `b,c` germ by the first
clock gives the same total clock. Endpoint equality and exact odd-count
additivity then give the `a,c` germ. There is no hidden uniform bound on
the intermediate words.

For positive `h`, the elementary inequality
`3^(3h)+1<2^(5h)` gives `J(3h)>h` for every supplied complete witness.
Given a germ from a large exponent to a certified seed, transport first
constructs the previously unknown witness and then applies that
inequality. Thus a finite seed set with maximum signature `H` cannot
reach `3h` by this relation once positive `h>=H`. Transitivity covers
all finite chains through intermediate powers. The argument does not
assume convergence of the excluded larger input. An empty seed set is
already vacuous.

The explicit positive cell is consistent with this invariant:

\[
T^8(256t+146)=T^8(768t+436)=81t+47.
\]

Its odd counts are four and three. If `m=21 mod64`, put
`t=(3^(m-1)-145)/256`, a nonnegative integer for `m>=21`.
The two inputs are exactly `3^(m-1)+1` and `3^m+1`. This verifies the
orientation and scope of WC22. The positive cell supplies infinitely
many reductions but does not override the finite-seed obstruction.

## 5. Joint-edit lower bound

The inductive alignment relation matches the retained edit rules: one
ordinary step on either coordinate costs one; a step on both costs zero
only when their current parities match. Each unilateral step changes
the complete-charge difference by exactly one in absolute value, while
a matched-parity step preserves it. A successful path plus a supplied
source witness constructs a target witness in the same induction.

For the retained family with `m=3h`, that target's charge satisfies

\[
\chi(y)-\chi(x)=1+J(3h)>h+1.
\]

The general alignment bound `abs(chi(x)-chi(y))<=t` gives `t>h+1`.
With `h=9k` and integer `t`, this is exactly `t>=9k+2`, as printed in
WC25. The source certificate still has four odd steps. The conclusion
excludes a universally successful edit budget depending only on that
supplied source odd-step count. It does not exclude a budget depending
on the full source tuple or the number of added cycles. Actual padding
cannot change the lower bound, because it leaves charge unchanged.

## 6. Executed checks and evidence limits

During this review I independently executed, from the repository root:

```text
/workspace/scratch/c6766c1207a3/collatz_work/nov23_runtime/lean-4.34.1-linux/bin/lean -j 1 -DwarningAsError=true research/lean-exact-witness-global-20261121/construction-attacks-20261123/witness/WitnessCharge.lean
```

It exited zero. All 21 printed public declarations depend only on
standard Lean logical axioms (`propext`, `Classical.choice`,
`Quot.sound`, or a subset). No `sorryAx` or research axiom appeared.
The file imports only `Std`; the mathematical statements explicitly
retain the witness and arithmetic premises described above.

I also reran the exact checker with `python -X utf8 -B`. It exited zero,
produced no stderr, and its output was byte-identical to the author's
recorded normal run, with SHA256
`9271bb7607b1a54d36a4b312d6ecd3d103587125a1251ee9f7207e6be3c6ddc0`.
I verified the source hashes and the three execution-log hashes in the
author's `REPLAY.json` against the actual files. The recorded optimized
run has the same output hash. The checker's guards use explicit
exceptions, so optimization does not remove them.

The finite all-clock merger oracles are justified for their witnessed
inputs: after both recorded hits, the endpoint and odd-count-difference
conditions are periodic with period two. Their stated finite scan
covers that complete periodic remainder. This is a completeness
argument for each checked pair, not an extrapolation over inputs.

The exact edit control uses the full finite product of the two closed
ordinary orbits, including both terminal-cycle states. Its zero-one
shortest-path search therefore covers arbitrary cycle repetition in
that specific example. The replayed optimum of 138 edits is a finite
control; the universal lower bound uses the written and Lean argument,
not this computed optimum.

The general rational-slope theorem, unique-prime-factor bridge,
infinite parameter construction, and displayed positive cell remain
at the written-proof scope stated by the manuscript. The formal core
and finite execution checks support the specified claims. They do not
resolve the original implication or provide an unrestricted successful
certificate selector.
