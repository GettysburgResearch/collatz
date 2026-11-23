# Independent review of the ordinary sibling-mass consumer

**Verdict: VERIFIED as a source-qualified deduction at the exact bytes
below.** This verdict covers the finite ordinary reconstruction, critical
mass calculation, Bellman and Haar consequences, and the stated failure
to close OPEN-F. It does not certify the analytic proof of the imported
Paper 37 count or reprove the previous repository mixing and floor inputs.

Reviewed file: `research/retained-source-attacks-20261122/SIBLING_MASS.md`.

SHA256:
`91f150e225fbe1c8c714792557714c35ffbf2328fd46094cfbba60413cfb6f8b`.

The initial mathematical review bound SHA256
`e60dafd4640505f7bbc71ac4a20cdc8f36fa1e9b5d4f195b64904c1d8f72a889`.
The final revision only replaces two guessed version URLs by the exact
version-4 Markdown download and adds a two-line access note. Reversing
exactly those changes reproduces the initial reviewed hash. I also opened
the versioned download successfully. This narrow extension changes no
mathematical statement or proof.

Reviewer: the independent legal-descent lane. I reconstructed the
calculations below from the displayed ordinary inverse map and read the
primary v4 statement myself. I did not infer correctness from another
agent's conclusion, run old computational searches, or rebuild old Lean
developments.

## 1. Exact external statement and scope

I opened the [primary Paper 37 page](https://rstation.ai/problems/collatz/papers/37),
whose heading explicitly identifies **version 4**, and read Lemma 11 in
Section 10.4, equation (143), together with Theorem D's actual-integer
reconstruction, equations (145)--(146). The direct `/37/v4` URL was not
accessible through the web reader; the current paper page supplied the
explicit v4 text. The final source link is the successfully opened
[version-4 Markdown download](https://rstation.ai/api/v1/papers/collatz_37/versions/4/download).

The count is exactly the one used in S2: at every unit beta residue
modulo `3^(b+k)`, with `k <= D*(b-1)^theta`, there are at least
`c*4^b/(3^(b+k)*sqrt(b))` words of length `b` and total `2b`.
The real-offset and logarithmic individual-gap bounds are also present.
The constants are independent of the supplied ordinary root. The finite
consumer does not replace this count by the weaker existence statement.

I did not reconstruct the extra-depth Fourier mixing, stopped renewal,
or selected-density proof behind that lemma. The paper itself records
that the full chain has not received formal review. Accordingly S2
remains an explicit recent-manuscript input. The new conclusions are
conditional on that input in precisely the manner stated by the note.

## 2. From a beta class to an actual positive path

For a selected word the affine slope is `omega=3^b/4^b` and
`4^b*beta` is an integer. The prescribed class

`beta = x - 3^b*4^(-b)*a mod 3^(b+k)`

therefore makes

`y = (4^b*x - 4^b*beta)/3^b`

an ordinary integer with residue `a mod 3^k`. Its beta class is a
unit because `x` is a unit and the subtracted term is divisible by
three.

I reconstructed the entire prefix legality. In the first numerator,
the coefficient not divisible by three is a power of two times
`2^e1*x-1`. Integrality of the complete inverse numerator thus forces
the first inverse step to be integral. Substitute this integer and
repeat; all inverse prefixes are integral. Starting from a positive
odd integer `z`, a positive-exponent integral value `(2^e*z-1)/3`
is positive and odd. A nonterminal multiple of three would make the
next numerator nonintegral. The last endpoint is a unit because
`k>=1` and `a` is a unit. Every supplied exponent is the exact forward
valuation because its forward endpoint is odd.

There is no extra assumption `x>F` here. Although the real formula
`(4/3)^b*(x-beta)` might initially suggest a negative endpoint when
`x<F`, the preceding ordinary induction proves positivity. Thus every
selected word satisfying this congruence necessarily has `beta<x`.
The real-offset upper bound does not supersede that arithmetic fact.

Distinct words at the same root and depth have distinct endpoints:
the deterministic forward map recovers their complete valuation word.
This statement does not need the root to be nonperiodic. If the root
is nonperiodic, its inverse paths cannot contain a periodic state.

## 3. Critical mass and the complete antichain

The multiplicity calculation has the right normalization:

\[
\frac{c4^b}{3^{b+k}\sqrt b}\,\frac{3^b}{4^b}
=\frac{c}{3^k\sqrt b}.
\]

Different prescribed terminal classes require different beta classes,
so their chosen word families do not overlap. Summing all
`2*3^(k-1)` unit classes gives the coefficient `2c/(3*sqrt(b))`
against normalized unit-Haar mean. This proves S6 and S7 with every
actual route weight retained. The total exponent and length are the
same for all the selected words.

For S10, a routed endpoint congruent to `n mod 3^(r+1)` admits every
old inverse word of length at most `r`. Dividing by three at most `r`
times preserves at least one ternary digit, so the old terminal unit
status is preserved as well. The ordinary induction above supplies
positivity at every appended prefix. The product word family is
prefix-free, since all routing prefixes have the same length and the
old family is prefix-free.

The source replacement formula S11 follows by subtracting the two
affine inverse equations. It does not claim that an old physical
source is unchanged. When the root is nonperiodic, a collision between
two distinct lengths would make one forward orbit visit the root
twice and hence make that root periodic. Collisions of equal length
are excluded by deterministic valuations. Thus the retained labels,
new source integers, and total mass in S10 are consistent.

## 4. Bellman extension and killed states

The unit-restricted inverse row sum is at most `40/21`. This follows
by grouping exponents modulo six: two of the three admissible parity
classes remain after removing the nonunit parent, and the largest
sum is `3*(1/2+1/8)/(1-1/64)=40/21`.

Inductively `F_r` depends only on the root modulo `3^(r+1)`.
At the next step, a congruence modulo `3^(r+2)` preserves admissible
unit exponents and makes the corresponding parents congruent modulo
`3^(r+1)`. The row-sum bound makes the countable sums finite at every
finite depth. No ordinary-height truncation has been inserted.

At a retained root, all inverse ancestors are retained, so the full
unit Bellman recursion and the killed-domain recursion agree there.
This justifies using the periodic finite-cylinder extension `F_r`
inside the modular minorization. It does not extend the killed
canonical harmonic function `G` to periodic vertices. The explicit
requirement that both `n` and `B(n)` be retained is correct and is
needed in the stated sibling application.

Positivity and `F_(j+1)>=P F_j` give S8; using only the one class of
`n` gives S9. The resulting `3^(-r)` loss is indeed incompatible
with claiming the depth-independent OPEN-F estimate from this
calculation alone.

## 5. Haar means and the density normalization

For each branch `f_e(y)=(3y+1)/2^e`, ternary Haar measure scales by
`1/3`. Normalizing Haar to the units does not change this factor.
Thus the integrated critical coefficient is `2^(-e)`, and summing
over all positive `e` gives exact preservation of unit-Haar mean.
The Bellman inequality `max(1,z)<=1+z` consequently gives
`<F_r><=r+1`; Markov's inequality gives S12. These are finite-cylinder
averages, not values of an almost-everywhere density at an integer.

For S13, I read the pinned local statement (JF) in
`research/lean-forward-band-20261121/JOINT_CLOCK_MIXING.md`, and the
density normalization and floor used in Section 8 of
`GLOBAL_RENEWAL_ATTACK.md` and Section 4 of
`MINIMAL_ENVELOPE_ATOM_REMOVAL.md`. Their existing source qualification
is retained; their analytic proofs were not rebuilt in this review.

Summing the clock in (JF) gives the asserted `L1` Cauchy bound for
the full-Haar densities `D_s`. They have mean one, vanish on nonunits
for `s>=1`, and satisfy `D_(s+1)=P D_s`. The last equality uses the
vanishing on nonunits. It would be wrong to identify `D_1` with
`P1` for the unit-restricted operator. The note explicitly avoids
this mistake. In particular `D_1` is `1` and `2` on the two unit
classes modulo three, whereas the unit-restricted row already depends
on the residue modulo nine.

The positive operator is an `L1` contraction, so its `L1` limit
`rho` is harmonic almost everywhere. A subsequence and the uniform
unit floor give `rho>=c0` almost everywhere on units. Each branch
is nonsingular, so countably many branches preserve almost-everywhere
inequalities. Bellman induction then gives `F_r<=rho/c0` almost
everywhere for each finite `r`. Finally normalized unit Haar is
`3/2` times full Haar on units, giving exactly

\[
\langle F_r\rangle\le\frac{3}{2c_0}.
\]

This proves S13 with its stated source-qualified inputs. It gives no
pointwise bound on `rho(n)` at an ordinary integer and no upper bound
on actual sibling leakage. Its use to show that a high spike need
not occupy a positive fraction of residue classes is properly scoped.

## Review boundary

No gap was found in S4--S13 under the explicitly pinned inputs. The
all-root finite-observable minorization and stopping-antichain
implementation survive the ordinary-legality, unit-domain, collision,
and normalization checks. The note correctly leaves OPEN-F, OPEN-S,
and universal Collatz unresolved. This review does not extend to
later file bytes, the upstream analytic proof of Lemma 11, or any
unwritten claim of quantitative regularity at the exceptional ordinary
spikes.
