# Attempt to pay the actual sibling current by adaptive valuation repair

**22 November 2026. Status: UNSUCCESSFUL CLOSING ATTEMPT.**

This pass attacks the actual canonical potential at persistent linear
spikes. It does not replace the ordinary orbit by a probability model.
The adaptive correspondence below is valid, but its cost was not
amortized sharply enough to prove the required sibling-current lower
bound. Its crude lower estimate is weaker than the existing obstacle
floor and is not presented as improved leakage.

## 1. Exact target and dependencies

The target is OPEN-S, with its sufficient finite formulation OPEN-F, in
[PR180, CRITICAL_BOUNDARY.md](https://github.com/GettysburgResearch/collatz/blob/a9f471543d7fed0a76f348e6d97a9d6d44fa369e/research/central-step-20261122/CRITICAL_BOUNDARY.md),
Section 6, at full head
`a9f471543d7fed0a76f348e6d97a9d6d44fa369e`.

Its domain is the nonperiodic positive odd ternary units; transport is
killed on entering a periodic state. Write

\[
 (P f)(q)=\sum_{U(z)=q}\frac3{2^{v_2(3z+1)}}f(z),
 \quad B(n)=64n+21,
 \quad \mathscr L_G(n)=\sum_{j\ge1}64^{-j}\frac{G(B^j n)}{G(n)}.
\]

The pinned source gives \(PG=G\), \(G\le V\le2\chi G\),
and finite obstacle iterates
\(V^{[0]}=1\), \(V^{[r+1]}=\max(1,PV^{[r]})\) on this unit
domain. It proves summability of \(\mathscr L_G(q_i)\) on an
escaping path while \(G(q_i)\ge\eta q_i\) persists. The missing
bound is \(\mathscr L_G(n)\ge c_\eta/\log(2+n)\) at all large
such spikes.

The path-product input used below is Section 2 of
[PR185, ORDINARY_HARMONIC_FLOW_AND_COLLISIONS.md](https://github.com/GettysburgResearch/collatz/blob/53f01ca5b443ef57ef2160b4996dbb2cc87f7395/research/whole-repo-closure-20261122/ORDINARY_HARMONIC_FLOW_AND_COLLISIONS.md):
for every retained nonperiodic finite path,

\[
 \delta\le\prod\lambda(z)\le1,
 \qquad\lambda(z)=\frac{3z}{3z+1},\quad
 \delta=e^{-200/3}.
 \tag{1}
\]

The original population, envelope, and normalization qualifications of
these sources remain in force. In the intended escaping application,
\(n\), every \(B^j n\), and all their inverse ancestors are retained.

## 2. A legal adaptive correspondence

An inverse exponent \(a\ge1\) is admissible at \(q\) precisely
when \((2^a q-1)/3\) is a positive odd ternary unit. The admissible
lists depend on \(q\bmod9\):

| \(q\bmod9\) | Admissible exponents, in increasing order |
|---|---|
| 1 | \(2,4,8,10,14,16,\ldots\) |
| 2 | \(1,3,7,9,13,15,\ldots\) |
| 4 | \(2,6,8,12,14,18,\ldots\) |
| 5 | \(3,5,9,11,15,17,\ldots\) |
| 7 | \(4,6,10,12,16,18,\ldots\) |
| 8 | \(1,5,7,11,13,17,\ldots\) |

Each row consists of two residue classes modulo six. The exponents of
the same rank in any two rows differ by at most three.

Starting with two retained roots \(n,m\), pair their first, second,
and subsequent inverse parents by rank; repeat at each paired vertex.
This gives a genuine prefix-preserving bijection of their ordinary
inverse trees. It adapts the valuations instead of requiring the same
exponent word. Every paired source remains integral and in the retained
domain.

For paired words of depth \(r\), let their exponents be
\(a_1,\ldots,a_r\) and \(a'_1,\ldots,a'_r\), and write

\[
 w_n=3^r2^{-\sum a_i},\qquad w_m=3^r2^{-\sum a'_i}.
\]

The correspondence gives the correct, but crude, estimate

\[
 8^{-r}\le\frac{w_m}{w_n}\le8^r.
 \tag{2}
\]

It also gives \(V^{[r]}(m)\ge8^{-r}V^{[r]}(n)\): transport a
stopping policy of depth at most \(r\) along the prefix-preserving
map, or induct directly in the obstacle recursion.

This avoids the integrality failure of identical-word copying. It
does **not** improve the relevant quantitative estimate. The six row
sums of \(P1\) are respectively

\[
 \frac1{21}(20,40,17,10,5,34).
\]

Thus

\[
 1\le V^{[r]}(q)\le(40/21)^r,
 \qquad
 \frac{V^{[r]}(m)}{V^{[r]}(n)}\ge(21/40)^r,
 \tag{3}
\]

and the elementary floor ratio in (3) is stronger than (2). Moreover,
a finite linear spike \(V^{[r]}(n)\ge\eta n>1\) already requires
\(r\ge\log(\eta n)/\log(40/21)\). There is no upper bound on
the needed depth here. The depth-dependent comparison cannot be
passed to the canonical limit with a positive uniform constant.

## 3. The exact cost is distortion of the ordinary source heights

The attempted improvement was to amortize the changes in valuations.
Let \(z\) and \(z'\) be the terminal ordinary sources of paired
words ending at \(n\) and \(m\). Telescoping the actual affine
edges gives an exact identity:

\[
 w_n=\frac nz\Lambda,\qquad
 w_m=\frac m{z'}\Lambda',
 \qquad
 \frac{w_m}{w_n}
   =\frac mn\frac z{z'}\frac{\Lambda'}\Lambda.
 \tag{4}
\]

Here \(\Lambda\) and \(\Lambda'\) are the products in (1).
Consequently no separate estimate for all the valuation changes is
necessary if the terminal height distortion can be controlled.

For \(m=B^j(n)=64^jn+(64^j-1)/3\), the weight in the actual
sibling budget cancels its leading height factor:

\[
 64^{-j}\frac{w_{B^j n}}{w_n}
 =\left(1+\frac{1-64^{-j}}{3n}\right)
      \frac z{z'_j}\frac{\Lambda'_j}{\Lambda}.
 \tag{5}
\]

In particular,

\[
 \delta\frac z{z'_j}
 \le64^{-j}\frac{w_{B^j n}}{w_n}
 \le\delta^{-1}\left(1+\frac1{3n}\right)\frac z{z'_j}.
 \tag{6}
\]

This retains the ordinary source and the exact critical weight; it
does not resample the source or replace the canonical potential.

For example, let \(\mathcal W\) be any finite prefix-free set of
inverse words at \(n\), all of depth at most \(r\), representing
part of a finite-obstacle stopping policy. Pair each of its words into
each tree rooted at \(B^j n\), and denote its sources by \(z_w\)
and \(z'_{j,w}\). The mapped words remain prefix-free. Summing (6)
therefore proves the quantitative finite inequality

\[
 \boxed{
 \sum_{j=1}^{J}64^{-j}V^{[r]}(B^j n)
 \ge\delta\sum_{w\in\mathcal W}w_n(w)
                   \sum_{j=1}^{J}\frac{z_w}{z'_{j,w}}.
 }
 \tag{7}
\]

The relevant attempted amortization was to lower-bound the weighted
reciprocal distortions on the right by a constant times
\(\sum_{w\in\mathcal W}w_n(w)/\log(2+n)\), for stopping
policies carrying the persistent spike. A uniform bound
\(z'_{j,w}\le C_\eta\log(2+n)z_w\) for enough of that policy
mass would suffice, but is stronger than necessary.

No such bound, even in the weighted averaged form, was obtained.
Pairing the admissible valuations by rank guarantees legality but
does not keep their cumulative discrepancy bounded. Equation (4)
shows exactly where that discrepancy reappears: in the ratio of the
two actual terminal heights. The endpoint control needed in (7) does
not follow from a bound on each individual valuation adjustment.

## Outcome

The attempt replaces impossible identical-word transport by a legal
adaptive correspondence and computes its exact ordinary cost. Its
worst-case comparison is weaker than the existing floor. The
amortized endpoint estimate needed to obtain OPEN-F or OPEN-S remains
unproved. No positive nonsummable sibling-current lower bound, escape
exclusion, cycle exclusion, or new Lean theorem is claimed.
