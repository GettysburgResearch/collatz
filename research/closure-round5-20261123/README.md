# Round five: rational recognition and entropy at one ordinary source

23 November 2026. Parent checkpoint:
`cb1ae1bb4af0c8d082e9ff466b9fe0c84932301c`.

**Full Collatz remains OPEN.** Three parallel attacks, followed by a
joint ternary-coding argument, produced two positive advances and an
exact obstruction. This packet supplies **15 new public Lean statements**,
written proofs with independent in-session reviews, a reusable rational
candidate verifier, and exact bounded replay. Its strongest infinite
entropy and dimension statements remain written mathematics.

| Attack | Result | First missing implication |
|---|---|---|
| Rational complementary candidate | A linear-in-denominator, logarithmic-in-height finite recognition budget; a sharper mixed-denominator budget | A successful candidate or sufficient denominator bound for every unchanged ordinary source |
| Entropy of one ordinary orbit | Polynomial prefix height forces positive entropy; an ergodic gap law of mean at most `log_2(3)` loses zero entropy rate under ternary coding | An unconditional height/ergodicity input and the untrimmed same-source collision estimate |
| Positive cycle exclusion | All-threshold rational circuit examples defeat the proposed small least-root gap bridge, while ordinary finite realizers of those words descend | A full-word arithmetic exclusion retaining the original source grid and complete numerical denominator |

The latest relevant PR178 and PR180 files were read at frozen current
heads. The prior whole-repository inventory and all earlier files are
preserved. [SOURCES.json](SOURCES.json) distinguishes file reads,
metadata refreshes and primary literature scope. No historical-priority
claim is made for the classical coding, entropy or rational-cycle ideas.

## 1. Exact recognition of a supplied rational candidate

Use the shortcut map `T(n)=n/2` for even n and `(3n+1)/2` for odd n.
The complementary parity map `Omega` is the unique 2-adic source whose
entire parity vector is opposite to the original one. Supply a signed
numerator a and positive odd denominator q. For a reduced presentation,
put `B=n max(1,abs(a))` and let `bl` be positive integer bit length.

The written theorem proves that the exact decision

\[
                         a/q=\Omega(n)
\]

requires a state-clock budget of at most

\[
 \boxed{K=14\operatorname{bl}(B)+60q+18.}
\]

The literal pair uses the unchanged original x and the signed numerator
w, with `w -> w/2` if even and `(3w+q)/2` if odd. Opposite parities
are tested at every clock. A mismatch rejects; at original 1 the exact
comparison is `w=2q`; at a repeated small numerator the candidate is
accepted exactly when the original state also repeats.

The improvement comes from two estimates. Before original 1, two
consecutive large-numerator clocks contract `x max(1,abs(w))` by at
least a factor `7/8`, uniformly in q. Before a small value repeats,
the total signed charge is at most

\[
 2\prod_{k=1}^q(1+q/k)^2
 =2\binom{2q}{q}^{\!2}\le2\,16^q.
\]

Counting all excursions together gives the budget above. The original
1 guard is essential; the packet retains a counterexample to extending
the uniform two-step contraction through that state.

For the different sufficient-prefix question, matching the first

\[
 \boxed{H=15\operatorname{bl}(B)+64q+19}
\]

opposite parity tests forces the original orbit to reach 1 or repeat.
Its extra parity tail converts a repeated numerator into an equal
ordinary state. The exact candidate recognizer can reject unequal
original states immediately and therefore uses the smaller K.

If `q=3^r q0`, `3` does not divide q0, `N=bl(n)` and
`L0=bl(max(1,abs(a),q))`, removing the three-part first gives

\[
 K_{\rm mixed}=14N+(15r+14)L_0+60q_0+18.
\]

The automatic verifier selects a proved budget. For pure triadic
candidates it retains the stronger preceding `3(r+1)` stopping bound.
The number of transitions is bounded; no linear bit-complexity claim
is made for arithmetic on arbitrary-sized integers.

### Run the verifier

```bash
python -X utf8 -B research/closure-round5-20261123/verify_rational.py 3 -4 9 --include-trace
python -X utf8 -B research/closure-round5-20261123/verify_rational.py 3 -4 9 --strategy mixed
```

Both accept the exact candidate `Omega(3)=-4/9`. The CLI takes the
**literal denominator**, unlike the preceding specialized triadic CLI,
which takes an exponent. Signed, zero and unreduced numerators are
handled; invalid even denominators are rejected.

This decides one supplied rational. It neither proves that every
`Omega(n)` is rational nor excludes arbitrary positive cycles for a
general denominator. Searching candidates without a successful bound
still leaves an unbounded search.

[Complete proof](TRIADIC_CONSTRUCTION.md) ·
[Finite Lean accounting](TriadicConstruction.lean) ·
[Verifier](verify_rational.py)

## 2. Entropy must pay for low height on the same orbit

Let an unchanged positive ordinary orbit be injective, let `H_N` be
its maximum through shortcut clock N, and let lambda be any stationary
limit of its overlapping parity-word laws along a subsequence `N_i`.
Entropy is in natural logarithms. The written theorem gives

\[
 \boxed{
 \liminf_i\frac{\log H_{N_i}}{\log N_i}
 \ge\frac{\log2}{h(\lambda)}.
 }
\]

A zero-entropy limit forces superpolynomial prefix heights along the
same subsequence. This statement does not require ergodicity of lambda.

The arithmetic reason is exact: equal length-m ordinary parity words
have original sources congruent modulo `2^m`. When `2^m>H_N`, every
sampled word is unique. Its empirical entropy is exactly
`log(N-m+1)`. For fixed `k<=m`, retaining every overlapping endpoint
gives the finite inequality

\[
 H(P_{N,m})\le
 \left\lceil\frac mk\right\rceil
 \frac{N-k+1}{N-m+1}\,H(P_{N,k}).
\]

The growing m is used in this finite inequality; only a fixed k law
is passed to the limit. Thus no unproved growing-block convergence
rate is assumed.

There is a direct counterpart on the exact backward odd-gap clock.
Let eta be an ergodic stationary limit of that same orbit's reversed
gap laws, with mean `a<=ell=log_2(3)`. Let beta be the finite liminf
height exponent for its actual odd-prefix maxima. Then

\[
 \boxed{h(\eta)\ge\frac{a\log2}{\beta}.}
\]

The proof establishes countable-alphabet entropy continuity from the
actual moment bound and proves its growing-window concentration using
bounded truncations and fixed-window averaging first. It permits loss
of the first moment: the limiting mean is not silently declared critical.
Without ergodicity the weaker `h(eta)>=log2/beta` still holds.

[Full same-source proof and controls](FIXED_SOURCE_PRESSURE.md) ·
[Ordinary arithmetic core in Lean](FixedSourcePressure.lean)

## 3. The ternary projection loses zero entropy rate in this drift range

For any ergodic stationary positive-gap process with finite mean
`a<=ell`, set `A_i=G_1+...+G_i` and

\[
 Z=\sum_{i\ge1}3^{i-1}2^{-A_i}\in\mathbb Z_3^\times,
 \qquad\mu=Z_*\eta.
\]

The written theorem proves exact local dimension, information dimension
and sublinear decoding entropy:

\[
 \boxed{
 \dim\mu=\dim_{\rm info}\mu=\frac{h(\eta)}{\log3},\qquad
 H(G_1,\ldots,G_m\mid Z\bmod3^m)=o(m).
 }
\]

At fixed total clock and complete carry the gap word is unique.
Nonnegative logarithmic drift bounds the typical carry quotient by a
subexponential factor, so there are only subexponentially many typical
words over a residue. Shannon--McMillan--Breiman supplies their masses.
The proof explicitly transfers restricted-measure bounds to the full
measure through Radon--Nikodym densities and residue martingales.
It requires neither iid gaps nor mixing.

For the actual gap law above, the complete past affine equation
identifies this code with the same ordinary odd-time residue limit.
Combining the two results gives

\[
 \boxed{\dim_{\rm info}\mu\ge\frac{a}{\ell\beta}>0,}
\]

and at critical mean `a=ell`, the bound is `1/beta`.
The earlier critical height threshold is recovered as a consistency
check; this is not claimed as the strongest general height bound.

The indispensable remaining distinction is between Shannon dimension
and order-two collision dimension. The proof has no exponential bound
on the mass outside its typical sets. Therefore it does not supply
the untrimmed collision upper needed by the repository's convergence
route. Nor does it establish polynomial height or ergodicity for every
hypothetical escaping ordinary source.

An exact critical mechanical gap law illustrates the boundary:
it is ergodic and its ternary factor is nonatomic, yet at depth m it
has only `m+1` possible residues and collision at least `1/(m+1)`.
Its dimension is zero. A sparse symbolic modification with quadratic
height is ruled out as an ordinary realization by the new same-source
entropy theorem. Neither symbolic construction is an escaping orbit.

[Complete coding proof and literature boundary](TERNARY_INFORMATION.md)

## 4. A cycle obstruction with arbitrary thresholds

For the primitive rational circuit word `1^p0^h`, retain

\[
 D=2^{p+h}-3^p>0,\quad C=3^p-2^p,\quad m=C/D.
\]

The least proper gap above its least state m is exactly `(m+1)/2`.
The **full** reduced denominator is

\[
 q=D/\gcd(D,C),\qquad\gcd(D,C)=\gcd(D,2^h-1).
\]

For any prescribed floor B and denominator threshold Q, irrational
rotation supplies arbitrarily long such circuits with every state and
every proper least-root gap greater than B, reduced denominator greater
than Q, and clock slope arbitrarily close to `log_2(3)` from above.
Every proper prefix coefficient is greater than one, while the full
coefficient is less than one.

Consequently those geometric and coefficient conditions cannot force
a proper carry gap smaller than D. The ordinary source arithmetic
still matters: each positive integer realizing the chosen finite word
is `-1 mod 2^p`, lies above the rational fixed point, and strictly
descends over that word. This proves an obstruction to the attempted
general bridge, not an ordinary cycle or an all-word cycle exclusion.

[Complete circuit theorem and source distinction](CYCLE_EXCLUSION.md)

## 5. Verification and continuation

The [execution and review record](../../reports/2026-11-23-closure-round5/README.md)
separates the evidence levels. Root freshly compiled the two unchanged
local dependencies, the two new modules and the audit. All 15 public
declarations were audited; only the standard `propext`,
`Classical.choice` and `Quot.sound` dependencies occur. The entire older
Lean corpus is preserved by hashes, not claimed as freshly recompiled.

Run the exact controls from the repository root:

```bash
python -X utf8 -B research/closure-round5-20261123/exact_replay.py
python -O -X utf8 -B research/closure-round5-20261123/exact_replay.py
```

The controls bind the source bytes, retain full carries and numerical
gcds, and use explicit failures that remain active under optimization.
Their receipt records the executed ranges and counts. The complete
repository integrity gate is separate from mathematical verification.

The most direct next target is a quantitative bound on the omitted
mass, or on complete original-source/carry fibres, strong enough for
the same-law collision estimate. The independent rational route needs
a source-specific approximation that funds its own proved recognition
budget. Neither implication is supplied by this packet.

All earlier work remains available through the
[preceding round](../literature-round4-20261123/README.md) and
[whole-repository review](../whole-repo-round3-20261123/README.md).
The earlier PR description is archived with this round's reports.
