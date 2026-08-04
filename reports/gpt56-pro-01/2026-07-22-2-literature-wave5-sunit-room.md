# Session report — literature wave 5, scaled-tail S-units, and the fixed room

Date: 2026-07-22  
Agent: `gpt56-pro-01`  
Issue: `#2`  
Branch: `agent/gpt56-pro-01/2-collision-rewrite-bootstrap`

## Requested review

Before extending PR #3, this session read:

- PR #13 `LITERATURE.md`;
- PR #13 `literature/LIVE_REPO_REVIEW_WAVE5.md`;
- the latest `gpt56-pro-03` review comment on PR #3;
- PR #34 `L-9887`, `L-9888`, `L-9893`, and `L-9898` on cap collars, triple seams, and the constant-width seam graph;
- PR #33's residue-cylinder dichotomy interfaces.

The literature advice was to freeze one symbolic word, expose one fixed finite
sum of powers of two and three, prove that scales yield distinct solutions, and
audit every proper subsum before invoking Evertse--Schlickewei--Schmidt.

## Main discovery: the connector chain telescopes

For the four stabilized phase-34 tower types, introduce

```text
p = (5,30,20,56)
b = (9,54,36,24).
```

After scaling an ordinary high tail by

\[
W=p_i+64h,
\]

every local connector/tower transition becomes

\[
2^{11(t_{j+1}+1)}W_{j+1}
=
3^{7(t_j+1)}W_j+b_{i_j}.
\]

The seed, cap, and residual-offset terms telescope completely. Over one corrected stage,

\[
2^{\mathcal E_m}W_{m+1}
=
3^{\mathcal A_m}W_m
+
\sum_{k=0}^{255}
2^{U_{m,k}+\alpha_{i_k}}
3^{V_{m,k}+\beta_{i_k}},
\]

with

\[
\mathcal A_m={5369\over2}2^m+1792,
\qquad
\mathcal E_m={8459\over2}2^m+2816.
\]

Every toll coefficient is itself a `{2,3}`-unit. This is `L-0031`.

## Exact S-unit consequence

Assume the prime divisors of all ordinary boundary words `W_m` belonged to one
finite set. A repeated 256-symbol source word would then produce infinitely many
solutions in one fixed finite-rank multiplicative group of the equation

\[
x_*+x_0+\cdots+x_{255}=1.
\]

All coordinates are positive, so every solution is automatically nondegenerate.
The ratio of the first two toll coordinates changes injectively with the scale.
PR #13 `LIT-KTHM-0043` therefore gives a contradiction.

Thus every infinite ordinary corrected-stage path must introduce infinitely many
fresh prime factors. This is `T-0032`.

The result completes the literature applicability checklist but also identifies
the surviving escape hatch: unrestricted endpoint prime support.

## Fixed-room structure

The homogeneous stage multiplier has an exact antiderivative in scale. Put

\[
a_m={5369\over2}2^m+1792m,
\qquad
e_m={8459\over2}2^m+2816m,
\]

\[
H_m={3^{a_m}\over2^{e_m}}.
\]

Then `H_(m+1)/H_m=3^(mathcal A_m)/2^(mathcal E_m)`. For any assumed infinite
ordinary path,

\[
C_m={W_m\over H_m}
\]

increases to one fixed real number `C_infinity`. Exact toll ordering gives

\[
0<C_\infty H_m-W_m
<
{216\over3^{7(2^m+1)}}<1.
\]

Therefore

\[
\boxed{W_m=\lfloor C_\infty H_m\rfloor}
\]

and

\[
0<\{C_\infty H_m\}
<{216\over3^{7(2^m+1)}}.
\]

This is `T-0033`. The ordinary route is now simultaneously:

1. a canonical cap-stitch path in a dyadic shrinking cusp;
2. a positive finite-rank equation that must escape through fresh primes;
3. a real fixed-room orbit hitting doubly-exponentially shrinking targets.

## Relationship to PR #34

PR #34 reduces any late cap chain to two-cell collars and 84 exact triple seams,
then to a 1024-state seam graph. The present scaled-tail coordinate is compatible
with that reduction: it telescopes connector arithmetic globally, while the cap
collar retains the canonical-minimum constraints discarded by the scaled
coordinate.

The two analyses locate complementary hard parts:

```text
scaled-tail equation:
    clean finite S-unit structure, but uncontrolled endpoint primes;

cap/triple graph:
    exact canonical stitching, but a nonautonomous odd-radix carry.
```

A full result must couple fresh-prime creation to the canonical seam graph or
prove that the fixed-room shrinking targets cannot be hit by bridge-compatible
words.

## Verification

Added `X-0016`:

```bash
python3 -m py_compile experiments/X-0016-scaled-tail-sunit/run.py
python3 experiments/X-0016-scaled-tail-sunit/run.py

python3 -m py_compile experiments/X-0016-scaled-tail-sunit/fixed_room.py
python3 experiments/X-0016-scaled-tail-sunit/fixed_room.py
```

The exact assertions were independently replayed in the available Python
environment. The scripts check stabilized anchors, actual canonical connector
chains, 96 local scaled-tail transitions, finite toll composition, stage exponent
sums, injective scale ratios, finite room increments, floor identities, and the
integer inequalities used by the shrinking-target proof.

## Honest status

No positive integer, cap-stitch tail, or counterexample is claimed. `T-0032` is
conditional on the imported S-unit theorem and awaits independent reconstruction.
`T-0033` begins from an assumed infinite ordinary stage path and derives its real
structure; it does not prove existence.

## Next attacks

1. Add the PR #34 triple-seam state to the scaled-tail equation and determine
   whether bridge-compatible fresh-prime creation is possible.
2. Search for a scale-transfer law for the first triple-seam odd-radix carry,
   using the fixed-room defect as the archimedean state.
3. Test whether the ordinary quadratic generator `V_m` can supply the required
   fresh primes while satisfying one canonical collar seam.
4. Seek a product-formula inequality coupling the doubly-exponential real window
   to the dyadic cusp of `T-0031`.
