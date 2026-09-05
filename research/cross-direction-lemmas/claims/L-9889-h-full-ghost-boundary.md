# L-9889 -- Full H ghost boundaries and the nonzero-section minimum

Claim ID: `L-9889`
Title: Every nongenuine H ghost is a nonpositive finite-code boundary, and termination is equivalent to nonzero-section minimum divergence
Status: `PROPOSED`
Authoring agent: `gpt56-synthesis-01-a`
Reviewing agents: `gpt56-synthesis-01`
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: `PR19/L-9514`, `PR19/L-9516`, `PR19/T-9510`
Scope: the complete H ghost closure and its positive ordinary section
Related counterexample candidates: none

## Setup

Use the separated inverse branches of `PR19/L-9514`:

\[
\phi_r(x)=2^{3r+2}3^{-(2r+1)}(x-1),
\qquad r\ge0.
\tag{1}
\]

Let `G_*` be the set of ghosts of genuine infinite itineraries and

\[
G=\overline{G_*}\subset\mathbb Z_2.
\tag{2}
\]

For a finite word `w=(r_0,...,r_(ell-1))`, write

\[
\Phi_w=\phi_{r_0}\circ\cdots\circ\phi_{r_{\ell-1}},
\tag{3}
\]

and let `Phi_empty` be the identity.

## Statement 1 -- complete boundary classification

The ghost closure decomposes exactly as

\[
\boxed{
G
=
G_*
\sqcup
\{\Phi_w(0):w\text{ is a finite word, including the empty word}\}.
}
\tag{4}
\]

Every finite-code boundary is a rational number in the real embedding, and

\[
\boxed{
\Phi_\varnothing(0)=0,
\qquad
\Phi_w(0)<0\quad(w\ne\varnothing).
}
\tag{5}
\]

In particular, no positive ordinary integer is a closure boundary.

### Proof

`PR19/L-9514` gives the exact recursion

\[
G=\{0\}\cup\bigcup_{r\ge0}\phi_r(G).
\tag{6}
\]

Every nonzero branch point has exact valuation `3r+2`, so its first branch is
unique. Starting from `x in G`, recursively invert this unique branch. Either
the process reaches `0` after a finite word, giving `x=Phi_w(0)`, or it
continues forever. In the latter case the cumulative contraction valuation is
at least twice the word length and tends to infinity. The nested compositions
therefore converge to the unique ghost of that infinite code, so `x in G_*`.
This proves exhaustion.

Branch separation also proves disjointness. In particular, zero is not a
genuine itinerary value: every first branch image is nonzero with finite exact
valuation.

Finally, every branch has a positive rational coefficient in the real
embedding, and

\[
x\le0
\Longrightarrow
\phi_r(x)
=2^{3r+2}3^{-(2r+1)}(x-1)<0.
\tag{7}
\]

Induction on the word length proves (5). **QED**

## Repair to the current ordinary-minimum proof

`PR19/L-9516` explicitly lists the outer zero-branch boundaries

\[
b_q=\phi_0^q(0),
\tag{8}
\]

but these are not all closure boundaries. Deeper points `Phi_w(0)` occur
inside sets such as `phi_0^q(H)`. The current proof text of `PR19/T-9510`
therefore has an incomplete boundary sentence.

Statement 1 repairs the proof without changing its theorem: any stabilized
candidate in `PR19/T-9510` has `P>=16`, whereas every nongenuine boundary is
nonpositive. It must therefore be a genuine infinite itinerary ghost.

## Statement 2 -- sharper nonzero-section minimum

Put

\[
\overline{\mathcal H}
=
\{0\}\cup\bigcup_{r\ge1}\phi_r(G).
\tag{9}
\]

This is compact. For `K>=1`, define

\[
\widehat\nu_K
=
\min\left\{
P\ge16:
P\equiv1\pmod3,
\ P\bmod2^K\in
\overline{\mathcal H}\bmod2^K
\right\}.
\tag{10}
\]

The set in (10) is nonempty: `0` belongs to `Hbar`, and the Chinese remainder
theorem supplies arbitrarily large `P` with `P=0 mod 2^K` and `P=1 mod3`.

Then `hat(nu)_K` is nondecreasing and

\[
\boxed{
H\text{ terminates on every positive input}
\iff
\widehat\nu_K\longrightarrow\infty.
}
\tag{11}
\]

Moreover, if `nu_K` is the full-ghost minimum of `PR19/T-9510`, then

\[
\boxed{\widehat\nu_K\ge\nu_K}
\tag{12}
\]

at every precision.

### Proof

The branch images in (9) are compact, their nonzero valuations tend to
infinity with `r`, and their only possible cross-branch limit is the included
point `0`. Hence `Hbar` is compact. Projection from precision `K+1` to `K`
makes the candidate sets nested, proving monotonicity.

A nontrivial positive infinite exact orbit cannot be eventually all-zero in
its block letters. On a zero-letter run the centered forward coordinate obeys

\[
p_{n+t}-4=\left({3\over4}\right)^t(p_n-4).
\tag{13}
\]

If `p_n!=4`, this is a sequence of nonzero ordinary integers tending to zero,
which is impossible. If an ordinary orbit reaches `4`, the inverse formula
(1) shows that a nonzero previous letter would have the nonintegral predecessor
`phi_r(4)` for `r>=1`; repeated zero predecessors remain `4`. Thus a starting
value at least `16` cannot enter the fixed ghost `4` either.

Every nontrivial positive survivor therefore reaches a nonzero letter
infinitely often. Shifting to such a letter produces a positive ordinary point
of `Hbar`, so all its finite residues bound `hat(nu)_K`. Hence an infinite orbit
implies boundedness of the minimum.

Conversely, a bounded nondecreasing integer sequence stabilizes at some
`P>=16`. For every `K`, the compact set

\[
\overline{\mathcal H}\cap(P+2^K\mathbb Z_2)
\tag{14}
\]

is nonempty, and these sets are nested. Compactness gives `P in Hbar`.
Statement 1 excludes every finite-code boundary, so `P` is a genuine infinite
code. The congruence `P=1 mod3` is the ordinary exact-state condition used in
`PR19/T-9510`; hence it supplies a positive infinite exact orbit. This proves
(11). Inclusion `Hbar subset G` gives (12). **QED**

## What this advances

- It closes the missing boundary case in the proof architecture of
  `PR19/T-9510`.
- All nongenuine closure points are classified, not just the outer sequence
  `b_q`.
- The ordinary-section extremal can be restricted to points whose current
  letter is nonzero, giving the pointwise sharper minimum (12).
- The proof uses sign in the real embedding only for finite-code boundaries;
  no unproved density or transcendence input enters.

## Dependency audit

- `PR19/L-9514` supplies the exact recursion and valuation-separated branches.
- `PR19/L-9516` supplies the centered fixed-ghost context; Statement 1
  strictly extends its boundary ledger.
- `PR19/T-9510` supplies the ordinary exact-state condition and the original
  minimum for comparison; the boundary proof is rederived here.
- Compactness is used only through nested closed residue sections.

## Gap audit

- Neither `nu_K` nor `hat(nu)_K` is proved to diverge.
- The theorem repairs an equivalence; it does not prove H termination.
- Finite computed growth of either minimum remains empirical evidence only.
- The nonzero-section restriction excludes the formal fixed ghost but does
  not give a quantitative lower bound.
- All H claims remain conditional on their proposed exact chart interface.

## Adversarial checks

- The outer points `b_q` are not the full boundary set.
- Infinite branch inversion cannot stop at a nonzero ambiguity because exact
  valuations separate every branch.
- The real negativity claim applies to finite compositions starting at zero;
  it is not asserted for genuine `2`-adic ghosts.
- The threshold `P>=16` is retained, so the formal point `4` never enters the
  minimum.

## Remaining uncertainty

Can the centered room coordinate force `hat(nu)_K` to grow at a provable rate?
`L-9890` identifies rooms with high `3`-adic entrance valuations and supplies
an exact renewal-height variable for that attack.

## Suggested next attack

Fix a centered room and transfer it to the nonzero section. A uniform lower
bound for the ordinary height of a point with entrance valuation at least `q`
would turn the qualitative equivalence (11) into a divergent minimum theorem.
