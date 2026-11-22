# Narrow independent reconstruction of arbitrary-debt transport

**Verdict: VERIFIED WITH A PROSE FIX, as scoped below. The fixed final
wording is verified. The universal successful-capture premise remains OPEN.**

Reviewer lane: asynchronous transport. The reviewer read the two new Lean
proof sources and the exact inherited definitions of `GapTrace`,
`PoweredTrace`, `sourceGrades`, `GradeDrop`, and `IntervalHyp`. It separately
reconstructed the affine and grade arguments below. This is a semantic
paper/source review; the root compiler receipt separately records actual
Lean execution and axiom checks.

## Exact reviewed source bodies

| Source | SHA-256 |
|---|---|
| `research/profound-step-20261122/mergers/ARBITRARY_DEBT.md` | `ba7eb6e601ea863a6d0382c2faa82a8b92a0a0b3a7b318fcf6a3e08e1407796f` |
| `research/profound-step-20261122/mergers/AffineCarry.lean` | `81bdf81fa8ba6916d267e13946a10591ef4211593db9b0ed5f709f25f1396df4` |
| `research/profound-step-20261122/mergers/CarryCapture.lean` | `8163730658fa890765ba11d04db5318332a8380208612464e06f00b6895ad9d9` |

The root publication report binds these working-file hashes to the final
commit. The vendor provenance remains `mergers/DEPENDENCIES.json`, pinned
to PR185 at `276be8154f4e867acc0230466b34d9cb224aacf5`.

The first source review covered note hash
`79b433359f853ad1fd0f06755e2029d00e8b9a6dc228911d69765ce02a461142`.
This final review additionally reconstructs the subsequently added fully
certified variant, the direct five-clock target descent, and the narrower
scope of the obstruction. It also incorporates the explicit-recipe wording
correction that `v_k` is positive and even, while `r_k,u_k` are positive
odd integers. The two Lean proof-source hashes are unchanged.

## AC1--AC2: the complete ordinary debt identity

If `n+b=2t` and `b>0`, then `n` and `b` have the same parity. In the even
case the two images sum to `t`. In the odd case the ordinary `+1` and
complementary `-1` cancel, giving `3t`. Positivity of the complementary
orbit prevents any natural-subtraction underflow. Induction on the full
binary cylinder proves `T^a(n)+S^a(b)=3^(s_a(b))*t`.

For a supplied source gap `3r+1=2^a*u` and target balance `n+d=3^p*r`,
with `p>0`, adding `b=3^(p-1)+d` gives exactly
`n+b=2^a*(3^(p-1)*u)`. Thus the new exponent is
`p-1+s_a(b)` and the new debt is the complete positive integer `S^a(b)`.
Every term survives the transition. The `CarryRun` recursion preserves
the actual sum of source clocks by composition; it is not an abstraction
that forgets intermediate debt. Reaching exponent zero makes further
transition unnecessary, but soundness alone does not prove that this
event happens.

The explicit gap-one transition from `9r-1` gives `3u-2`; retaining
additive debt two is essential. Neither the formal source nor the fixed
note replaces this target by the different target `3u-1`.

## AC3--AC4: padding is paid for in the same complete-source grade

Let the consumed prefix have maximum letter `m`, occurring at least once.
The original grade includes at least one `2m`, with no prefix grade
above it. The padded child has the same literal tail, plus grade `2e+1`
when `e>0`. Since `e<m`, this new grade is strictly below `2m`. The
highest changed multiplicity therefore decreases exactly as required by
the inherited `GradeDrop` relation. Multiplicities in the unchanged tail
cancel, even when that tail has larger grades.

The physical endpoint balance gives `z<=3^p*u`. The explicit guard
`3^p<=2^(e+1)` therefore puts the positive target in
`Interval (2^e*u) z`. `PoweredTrace` for this child uses precisely `e`
halvings and the supplied literal tail. The formal conclusion uses the
displayed `IntervalHyp` for a lower grade; it does not assume the target
already converges or select a new certificate after the fact.

For `e=m-1` the sufficient coefficient test is `3^p<=2^m`. It permits
`p=0` for `m=1`, `p<=1` for `m=2,3`, and `p<=2` for `m=4`.
The parent matrix rank in PR183 is a different object, and the final note
correctly avoids identifying these orders.

## AC5: the full shorter language

Write `D_p(r)=3^p*r-1`. The initial source gap one sends `9r+2` to
`D_2(v)`. For `p=1,2`, the complementary start is respectively two or
four. Direct two- and three-clock computation gives

- a source gap two sends either state to `D_1`;
- a source gap three sends either state to `D_2`.

The additive debt is one in **both** states. Induction therefore works
for every finite word over `{2,3}`. The final gap two gives `3u-1`
after exactly `sum(body)+3` ordinary clocks. No bound on the length or
the ordering of the body is used.

The padded source is `2u`, with initial grade three. Since the consumed
prefix contains a two, its maximal removed grade is at least four;
the grade lemma pays for that new padding. The endpoint is within
`0<3u-1<=4u+1`. This verifies the entire `1 {2,3}* 2` language rule
with the literal supplied tail retained.

**Prose fix made during review:** the first draft called `D_1,D_2`
"debt-one/debt-two" states. That wording confused the ternary exponent
with the additive debt and was especially ambiguous beside the actual
debt-two transition in AC2. The final pinned note states the two `D_p`
forms and says explicitly that their additive debt stays one. The Lean
sources already used the correct coordinates and required no edit.

## AC6: the rational-offset construction is genuinely ordinary and finite

The rational five-cycle `19/5,31/5,49/5,76/5,38/5` has parity word
`11100`; the five-step affine map has multiplier `27/32` and fixed
point `19/5`. The source block `100` has multiplier `3/8` and fixed
point `1/5`. These two exact offsets explain the ordinary affine
identities in the formal source; no convergence property of the rational
cycle is used.

At time `15k`, the source follows `5k` copies of `100`, while the target
follows `3k` copies of `11100`. Their multiplier ratio, including the
initial factor nine, is `3^(4k+2)`. Eliminating the shared input gives
exactly AC6, including the remaining integer constant nineteen.

The explicit recipe is integral for every `k>=0`:

- `r_k=(2^(16k+2)+1)/5`, since `2^16=1 mod5`;
- `u_k=(3^(5k)*2^(k+2)+1)/5`, since `3^5*2=1 mod5`;
- at each source step `j<=5k`, the exponent `16k+2-3j` is at least
  `k+2`, making `(3^j*2^(16k+2-3j)+1)/5` positive and odd;
- consecutive such values satisfy `3r_(k,j)+1=8r_(k,j+1)`, so the
  actual odd valuation is exactly three, including the last gap.

Consequently the displayed `u_k` is an actual endpoint. The target
endpoint is `(3^(9k+2)*2^(k+2)+19)/5`, again an ordinary positive
integer. For `k>=1`, its debt is `(3^(4k+2)-19)/5>0`, which is integral
because `3^(4k+2)=19 mod5`.

Let `M=3^(4k+2)`. Since `u_k>=1` and `M>=729`,
`z_k-8u_k-1=(M-8)u_k-(M-19)/5-1 >=(4M-26)/5>0`.
This exceeds every padded interval with `e<3`, exactly the padding
funded by a consumed prefix whose maximum source gap is three.

The result is an unbounded resource requirement **relative to the
companion source**, not a claim that the target grows relative to its
own original value. Each `k` gives a different ordinary starting
integer and a finite trajectory prefix. No fixed infinite ordinary
orbit and no complete convergence certificate for the original explicit
recipe `r_k` is asserted. The final note supplies a different, fully
certified recipe, checked next.

## Final extension: unbounded intermediate debt on fully certified sources

Fix `k>=1` and put `m=5k+1`. The induction
`v_3(4^(3^j)-1)=j+1` follows by cubing
`1+3^(j+1)*c_j`, with `3` not dividing `c_j`; the higher binomial terms
have an extra factor of three. It implies that four has order `3^(m-1)`
modulo `3^m`, and its powers exhaust the `3^(m-1)` residues congruent to
one modulo three. Since `8/5` is such a residue, there is an even exponent
`h` with `5*2^h=8 mod3^m`. Adding a period preserves the congruence and
allows `h>=4`.

Set `v=(5*2^h-8)/3^m` and `u=(2^h-1)/3`. The first is a positive
integer divisible by eight: its numerator is positive and divisible by
eight, and its denominator is odd. The second is a positive odd integer,
since `h` is positive and even. The exact identity
`3^(5k)*v=5u-1`, together with
`2^(15k)=3^(5k) mod5`, makes
`r=(2^(15k)*v+1)/5` integral and positive odd.

Every intermediate value
`(3^j*2^(15k-3j)*v+1)/5`, `0<=j<=5k`, is integral by the same
modulo-five calculation and odd because `v` is even. Consecutive values
satisfy the exact gap-three equation. The last value is `u`, and
`3u+1=2^h` is an exact terminal gap to one. Hence
`[3 repeated 5k] ++ [h]` is a complete supplied ordinary certificate.
This independently verifies the additional written construction.

At the intermediate endpoint before consuming `h`, AC6 still gives the
same unbounded exponent and the same failure of every padding funded by
the consumed gap-three prefix. The final gap is still available to a
later dispatcher; it must not be discarded when assessing the entire
certificate. For `k>=1` the congruence also rules out `h=4` (its positive
numerator is only 72, below `3^m`), so this does not construct an
alphabet-four family.

## Final scope correction: the targets themselves descend immediately

For either realization of AC6 with `k>=1`, the input identity gives
`5*(9r+2)=9*2^(15k)*v+19`, and therefore `9r+2=23 mod32`.
The exact five-clock arithmetic is

`32a+23 -> 48a+35 -> 72a+53 -> 108a+80 -> 54a+40 -> 27a+20`.

Its endpoint is smaller than its source by `5a+3>0`. Thus the family is
already handled by an ordinary-value descent rule. The unbounded carry
does not refute a complete termination strategy, a finite abstraction
with a sound overflow case, or a dispatcher that also uses this descent.
It refutes treating the two small concrete exponent states as an
exhaustive list, and refutes automatic capture after these particular
prefixes with only their consumed grade budget. The final note now
states precisely these distinctions.

## What this review does not establish

The review verifies the written AC1--AC6 derivations and their stated
formal interfaces. It does not establish a total successful dispatcher,
well-founded descent for every required target, the missing blocked-erasure
cover, or full Collatz. It does not treat the cited termination literature
as supplying an unchecked universal finite abstraction. Compiler and
bounded arithmetic replay receipts are separate evidence and are not
claimed as execution by this reviewer.
