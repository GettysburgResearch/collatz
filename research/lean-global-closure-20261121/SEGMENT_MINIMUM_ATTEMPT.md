# Follow-on full-closing attempt: segment minima and supplied certificates

Status: **OPEN; no additional closing theorem is claimed.** The proved `ResetReturns.lean` was not changed during this attempt.

Source: PR #173 at `fa0c9e2a2851e6324391e39c17afcb5913185aec`, especially `ForwardSection.lean`, `SectionDynamics.lean`, and the earlier inverse construction in `ShellCover.lean`.

## 1. Re-root the forward argument at an actual segment minimum

Take a segment from one marked point to its first strictly positive marked return, and let `m` be its least ordinary value. If the endpoint is a strict minimum, that particular return already descends. Otherwise re-root at an occurrence of the minimum before the endpoint. The remaining segment has no values below `m`, so the phase-error estimate has the actual floor `m` and an error of at most `j/m` over `j` odd steps. The first strictly positive marked endpoint of this tail is still the original endpoint: an interior root is unmarked, and a root at the original start uses the strictly positive return convention. Its clock can be bounded by applying the visit theorem after one initial shortcut step.

This successfully retains the actual ordinary floor. It does **not** supply the size comparison needed for strong induction at that floor. If the endpoint is

\[
x=2^D+a,\qquad (D+1)a\le70\,2^D,
\]

the forward argument allows a clock of order `sqrt(m)` and an endpoint as large as

\[
m\exp(O(\sqrt m)).
\]

Consequently its permitted offset `a` can be much larger than `m`. No step establishes either `a<m` or a marked endpoint below `m`. A drop below the preceding marked source is insufficient: the next mark may overshoot that source again.

Choosing a shorter rational grid does not fix this comparison automatically. It reduces the possible growth horizon while weakening the available phase resolution. The exact arithmetic relation between the removed low bits and the leading-phase visit is still missing.

## 2. Consume the entire certificate of a smaller offset

For a supplied positive offset `a` with an actual hitting certificate of length `t`, let `p` be its odd count. When `t≤D`, the exact common-prefix identity gives

\[
T^t(2^D+a)=2^{D-t}3^p+1.
\]

For `a>1`, the source affine identity gives `3^p/2^t≤1/a`, so this target is below `2^D+a`. The case `a=1` can use its two-clock return and coefficient `3/4` once `D≥2`. This is a valid finite transfer when the supplied witness fits the binary window. It is not a proof of the missing uniform clock inequality, and ordinary descent from a mark alone does not close the induced-return induction.

When the supplied certificate lasts longer than `D`, consume the first `D` steps exactly. The target becomes

\[
T^D(a)+3^{p_D}.
\]

The source has a shorter remaining certificate, but the discrepancy is now an odd power of three. The two trajectories no longer have a common parity prefix supplied by the original binary lift. If their difference is odd, the next parity choices are opposite, and the discrepancy update depends on the current source value. Continuing to consume the certificate eventually reaches source `1` while leaving a nontrivial target. A rank counting the remaining supplied source clock has then exhausted its resource without proving the target convergent.

The band inequality bounds `a` relative to `2^D`; it does not bound the supplied hitting time by `D`, nor does it settle this terminal target. No new source-certificate rewrite covering every such state was obtained.

## 3. Try an inverse representative near the segment minimum

A possible repair would be to replace the high marked endpoint by a sufficiently low marked predecessor in the same component. The existing `ShellCover.shell_hits` supplies inverse representatives in relative-width `1/h` intervals only after the explicit threshold `Mesh.cost * q`.

The published cost cannot simply be calibrated to the new self-shrinking band at all large scales. To see the exact issue, write the mesh parameters as `p,e`, and put

\[
A=16^p,\qquad B=3^p2^e.
\]

Its guards are

\[
B<A,\qquad hA\le(h+1)B.
\]

Since `A−B≥1`, they give `h≤B<A`. For `h≥1`, they also give `A≤2B`, hence `e≥2p`: otherwise `2^(e+1)≤4^p<(16/3)^p`, contradicting that inequality. The defined cost therefore satisfies

\[
\log_2(\mathrm{cost})=2eB+1+4p\ge4ph>h\log_2h.
\]

At a center `2^D`, ensuring that the entire relative-width `1/h` interval lies within the forward band requires `D+1≤70h` (and `h>1` keeps that interval in one octave). If also `h≥2^70`, then `h log₂ h≥70h≥D+1`, so the displayed cost exceeds `2^D` itself, even before multiplying by the positive target `q`. In particular this failure occurs for all sufficiently large `D` when the precision is calibrated to that band's width. Thus this **particular published threshold** does not yield the required low representative at the new section's own width. This is a written bound on the specified construction, not a new Lean theorem or a claim that all inverse constructions have the same limitation.

A faster inverse construction would still need a sufficiently strong ordinary-height comparison. Merely obtaining some marked predecessor, at unrestricted height, would not prove descent at the segment minimum.

## 4. Why the phase information has not supplied the missing joint control

On odd-only steps,

\[
\log_2 U(x)=\log_2 x+\log_2 3-v_2(3x+1)
 +\log_2(1+1/(3x)).
\]

The integer valuation disappears modulo one. Re-rooting at the segment minimum makes the perturbation small, but does not recover the accumulated integer amount removed. That amount is exactly what distinguishes net ordinary growth from the contraction needed for convergence.

I also considered using the leading zero block of a mark after the low bits are consumed. A long odd run leaves an endpoint of the form `3^b u−1`, with a much smaller remaining factor `u`. Transferring a supplied convergence certificate for `u` to that endpoint would be useful, but the necessary universal arithmetic transfer is not supplied by the phase theorem or by the minimum comparison. Treating that transfer as available would simply insert the missing closure assertion.

## Outcome

The next missing step remains a joint arithmetic statement, not the existence of the section or the smallness of its real phase error: one must control the ordinary endpoint relative to a valid induction reference while tracking the actual low-bit transitions or a complete inherited certificate. This attempt did not obtain that step. No new conditional equivalence, finite residue extension, or rank obstruction was substituted for it.
