# Independent review of residual norm obstructions and rotations

Date: 2026-11-22.
Reviewed source: `zero_atom_attack/CYCLOTOMIC_ZERO_FIBER.md`, Sections 8--10,
equations (N18)--(N27).
Source SHA256: `045844e3e89a36dd0480ed495f5635df52a9b16342dec0fbc20ae18735cf2bbd`.

**Verdict: the three stated obstructions are mathematically sound.** The
small residual denominator family, the nonzero resultant at wrong
conjugates, and the exact rotation-unit relation all retain the stated
primitive-word and whole-denominator hypotheses. These are obstructions
to specified unrestricted proof routes, not counterexamples to Collatz.

This review is independent of the supplied finite checker. It does not
claim to have rerun that checker or the earlier finite Collatz modules.
The original family exclusion (N1)--(N17) has a separate scoped review in
`CYCLOTOMIC_FAMILY_REVIEW.md`.

## 1. Residual denominator and wrong-conjugate counterexample
The subsequently added Sections 8--9 were also inspected.

For Section 8, the two indicator supports in (N18) are disjoint by
parity. At the simple roots of `Y^L-1`, the evaluations listed after
(N20) exhaust the cases: zero outside the roots of `H`, and respectively
`n`, `m*zeta`, `L+n+m`, and `n-m` in the remaining cases. Thus the monic
polynomial gcd is exactly `G`. The degree `2m+2n-2` follows from the
intersection `gcd(Y^(2m)-1,Y^(2n)-1)=Y^2-1`.

The primitivity argument does not require the two supports to have
different coefficient values. Their unequal counts rule out odd shifts;
an even shift `2h` preserves each parity class and forces both `m|h` and
`n|h`. The profile is primitive. Every embedded boundary gap is at least
two, so the subsequent gap-word argument is valid without a merging
edge case. The extra factor `X^2+2X+4` is coprime to the carry denominator
by its different root modulus. The reciprocal substitution retains
exactly the displayed cyclotomic gcd. Finally `n=m+1` gives degree `4m`
and the precise upper bound `D_pol < 2^(20m+2)` with
`A=10m(m+1)`. This disproves an exponential-in-A lower bound for the
residual polynomial denominator under only primitivity and the stated
cone condition.

For Section 9, the wrong-conjugate obstruction can be verified without
recomputing the large resultant certificate. Let `x=2^(13/8)`. The
identity `13*5-8*8=1` gives

\[
2^{1/8}=x^5/2^8.
\]

Hence \(\mathbb Q(x)=\mathbb Q(2^{1/8})\) as number fields, and
`X^8-2^13` is irreducible
because `Y^8-2` is Eisenstein. Its degree-eight polynomial cannot share
a nonconstant rational factor with the displayed degree-seven `Q`.
Their resultant is therefore nonzero.

Direct evaluation gives

\[
F(3)=F(-3)=-1631=-7\cdot233,
\quad Q(3)=7553\equiv97\pmod{233},
\quad Q(-3)=-1165=-5\cdot233.
\]

Also `7|Q(3)`. The shared root `3` modulo seven and the shared root `-3`
modulo 233 imply that `7*233` divides this nonzero resultant. Yet it
does not divide `Q(3)`. Thus the mathematical counterexample to universal
residual-resultant nondivisibility is independently verified. The exact
larger resultant value in (N24) remains the author's additional integer
determinant certificate; its value is unnecessary for this independent
argument. The separate evaluation ideals really must be retained.

These two new obstructions do not invalidate the specific family
exclusion of Section 5. They invalidate two proposed ways to extend that
exclusion uniformly to arbitrary primitive words, exactly as the note
states.

## 2. Exact unit relation under rotations

For an even initial shortcut letter, every one position shifts left by
one, so `2 Q_rot=Q`. For an odd initial letter, the first one moves from
position zero to position `A-1`; the remaining one indices decrease by
one. Directly grouping those terms gives

\[
2Q_{\mathrm{rot}}=X(Q-X^{p-1})+2^A=XQ-F.
\]

Iterating in the finite algebra `E=Q[X]/(F)` proves

\[
Q_{\mathrm{rot},\ell}=X^{p_\ell}2^{-\ell}Q.
\]

The algebra has dimension `p`, and `X^p=2^A`. Therefore
`|Norm_E(X)|=2^A` and `Norm_E(2^(-ell))=2^(-p*ell)`, which gives the
absolute norm identity (N27), including when that norm is zero.

In the localized integer order `Z[1/2,X]/(F)`, the element `X` is a unit:
its inverse is `X^(p-1)/2^A`. Hence every rotation multiplier is a unit
at every odd-prime ideal of that order. In any number-field component,
`p*v(X)=A*v(2)=0` at an odd prime, so the prime-ideal valuations are
unchanged as stated. The formula also proves identical odd parts for all
nonzero resultant values.

The distinguished evaluation is preserved as well. Reducing the same
identities at `X=3` modulo the full odd denominator gives a unit multiple
of the previous numerator because both two and three are invertible
there. Thus cyclic rotations do not convert the root `-3 modulo 233`
from Section 9 into the required root `3`. Every rotated example retains
the wrong-conjugate obstruction. This is an exact dependency among the
rotated conditions, not merely a failure to prove their independence.

## 3. Exact review boundary

The Section 8 family refutes a uniform exponential lower bound on the
polynomial residual denominator using only primitivity and the strict
cycle cone. Section 9 refutes universal residual-resultant nondivisibility
even when the polynomial gcd is one. Section 10 shows that rotations do
not repair that norm route because they are units in the same algebra.
None of those statements proves the desired strict evaluation-ideal gcd
bound (N26), which the source correctly marks as unproved.

The exact large integer resultant in (N24) is not an independently
recomputed assertion of this review. The irreducibility and two modular
root calculations above independently establish all properties needed
for the counterexample without its full value. No external analytic
Collatz input or GRH is used in this review.

