# Corrected signed energy and stronger all-clock cones

**Kernel-checked finite and universal algebra.** The construction below
improves the sufficient height in the existing ordinary postpeak theorem
from `21q+9K+3` to `6q+3K+3`, where `q` counts upper even departures.
It retains the original positive source, every smaller positive visitor,
and every lower physical clock. It supplies no universal smaller visitor.

## A dyadically homogeneous energy

For an integer `x`, let `F_a` be the ray `x=−2^j a`, `j≥0`. Define

\[
 E(x)=\begin{cases}
 400x^2,&x\in F_3,\\
 441x^2,&x\in F_5,\\
 450x^2,&\text{otherwise}.
 \end{cases}
\]

Then `400x²≤E(x)≤450x²` and `E(2x)=4E(x)`. Every signed odd edge
`3x+1=2y` with `x≠−1` satisfies `2E(x)≤E(y)`.
For nonnegative `x` this follows directly from the square inequality.
The exceptional inputs `−3` and `−5` give equality. For any remaining
negative odd input, `x≤−7` and `3∤y`; hence it suffices that

\[
 441(3x+1)^2-3600x^2
       =9(-x-7)(-41x-7)\ge0.
\]

The input `−7` is another equality. Thus the exponent ratio is sharp
on the signed cycle `−5→−7→−10→−5`, which has two odd edges and one
even edge. A bounded positive correction to `x²` cannot improve the
odd factor above two while retaining the exact even factor four: the
product around that cycle would contradict it.

For a signed walk of length `h`, odd grade `p`, and endpoints `x,z`
with `z≠−1`, multiplication gives

\[
 2^pE(x)\le4^{h-p}E(z),\qquad
 400\,2^p x^2\le450\,4^{h-p}z^2.                         \tag{1}
\]

The signed point `−1` is absorbing. Consequently the endpoint exclusion
also excludes it at every prior odd edge, as needed for (1).

## A trap with separate prefix and tail costs

Suppose `|z|≤2·3^r`. If

\[
                     4(h-p)+7r+5\le2p,                  \tag{2}
\]

then `z=−1`. Otherwise `x≠0`, since the zero trajectory has odd grade
zero. Equation (1) therefore implies
`2^(p+1)≤9·4^(h−p)9^r`. Squaring and using `81<128`, together with
(2), gives a contradiction. This rational-power proof needs no real
logarithms. The coefficient seven is sufficient; only the odd/even
ratio in (1) is claimed sharp.

[MirrorEnergy.lean](MirrorEnergy.lean) proves all these statements.
The energy is noncomputable only because the ray predicates are written
as propositions; the proof uses ordinary integer arithmetic and the
standard three kernel axioms recorded by the replay.

## Joint bookkeeping improves the ordinary postpeak cone

Retain the notation of [the original cone](../../descent/postpeak/POSTPEAK.md).
The original source is `n=2^H v−1`, `v>0`, and its postpeak word `w`
has length `t`, odd grade `f`, and `q=t−f` even departures. A lower
walk splits before its last `t` letters. Write `p,L` for the odd and
even counts of the translated prefix, and `u,r=t−u` for those of its
tail. Equal endpoint affine numerators bound the translated split state
by `2·3^r`.

For a discount `d≥0`, the exact identities and ordinary size estimate are

\[
 p+d+q=H+r,\qquad L+r+d<2q.
\]

Keeping this combined budget, instead of bounding each term separately,
shows that `H≥6q+3` implies (2). The split state is therefore exactly
`−1`, and the tail has the same signed offset as `w`. For a paid surplus
`b`, the corresponding identities are `p+q=H+r` and `L+r≤2q+b`.
The sufficient height becomes `H≥6q+3b+3`.

[SharpCone.lean](SharpCone.lean) repeats the ordinary source and word
transport from the already checked cone with precisely this new trap
and bookkeeping. Its conclusions are:

- The exact same-length, same-offset criterion for a smaller visitor
  with `k+d=H+f` holds under `H≥6q+3`.
- If `w` is maximal in its offset fiber and `3^K | n−s`, `s=0` or `1`,
  then every smaller positive visitor to its endpoint uses more than
  `H+f+K` odds under `H≥6q+3K+3`.
- Under the previous height condition `2n≥K(1+3^K)`, the exact finite
  scaled-row selector remains equivalent to existence of any smaller
  visitor with at most `H+f+K` odds in this stronger cone.
- The finite prefix budget transports with height
  `H≥6q+3(K+b)+3`. In particular the existing 648-source certificate,
  with `K≥84`, forces more than `H+f+K+12` odds under
  `H≥6q+3(K+12)+3`.

The selectors still inspect every relevant binary scale. Their source
height hypothesis is retained. No lower-clock cutoff is introduced.
All prior cone declarations remain available with their original names.

## Credit and unresolved step

The ordinary ramp barrier, prepayment architecture, translated signed
walk, and postpeak offset-fiber reduction are inherited from the earlier
checkpoints and their credited antecedents, especially PR146. More
specifically PR146's `research/upper-bit-mergers/NEGATIVE_FIVE_CHECKPOINT.md`,
at `f431078244e868dc699fad011044f0d5e7f76437`, already proves the same
optimal per-odd energy gain for reflected paths ending at 5: its potential
is `W(7)=50`, `W(x)=x²` otherwise, and `4W(Sx)≥8^(x mod2)W(x)`.
Its paths avoid the small invariant set `{1,2,3,4}`. The present repair
handles the troublesome reflected state 3, enforces exact homogeneity
on every dyadic ray, and applies to every signed path with endpoint other
than `−1`. The new consumer is the stronger cone obtained from that
universal version and the joint budget. Neither the optimal odd gain
nor the negative-five mechanism is claimed as first discovered here.

The remaining global obligation is still to prove that every positive
source eventually enters a configuration with a smaller visitor, or
otherwise to exclude every orbit that avoids such configurations.
Making a conditional barrier valid at a shorter ramp does not discharge
that obligation.
