# Finite rational filters and the Pólya--Carlson denominator condition

23 November 2026. **PROPOSED written exact obstruction for the specified
regularization class. No universal source recurrence is constructed.**

This is a companion to `SCALAR_BOUNDARY_AND_SECOND_CENTER.md`. It tests
whether finite rational pole removal can put the actual source series
into a directly applicable arithmetic Pólya--Carlson class. The answer
is exact: for this particular source series, the required subexponential
denominator growth already forces the filtered series to be a polynomial.

## 1. The primary theorem being tested

Bell--Gunn--Nguyen--Saunders, *A general criterion for the Pólya--Carlson
dichotomy and application*, arXiv:2206.00862v1, Theorem 1.2, assumes
convergence in the unit disc at every embedding and subexponential growth
of the common coefficient denominator outside an exceptional set of size
`o(N/log N)`. It concludes either a natural boundary or agreement with a
rational series outside that set. With no exceptional set this is the
usual rational/natural-boundary alternative. Theorem 1.6 adds a
subexponential individual-denominator condition on the exceptional set
to obtain full rationality in the continuation branch.

The primary theorem and its exact exceptional-set condition were read
directly. Only these stated hypotheses are tested below. The result is
not a limitation of all arithmetic rationality methods.

## 2. Every nonzero filtered coefficient retains an exponential denominator

Keep the same positive source and notation as the main note and put

\[
F_n(w)=B_n(2w)=\sum_{k\ge0}
        2^ke_k3^{-p_{k+1}}w^k.
\tag{1}
\]

Fix a nonzero polynomial `P(w)=sum_(i=0)^d q_i w^i` over `Q`, and write
`c_k=[w^k](P F_n)`. The polynomial and the source remain fixed.

**Lemma.** There is a constant `C_P`, independent of `k` and of the
particular source, such that for every `k>=d` with `c_k!=0`,

\[
\boxed{v_3(\operatorname{den}(c_k))
       \ge p_{k+1}-C_P.}
\tag{2}
\]

Moreover positivity of this actual source gives

\[
\boxed{\log\operatorname{den}(c_k)
       \ge\tfrac12 k\log3-O_{n,P}(1).}
\tag{3}
\]

Here `den` is the full positive reduced rational denominator. Equation
(2) is a lower bound on its three-part, hence also a lower bound on the
full denominator; the other prime factors are not declared absent.

**Proof.** Exact convolution gives

\[
c_k=\frac{2^k}{3^{p_{k+1}}}
\sum_{i=0}^d q_i2^{-i}e_{k-i}
          3^{p_{k+1}-p_{k-i+1}}.
\tag{4}
\]

The sum in (4) depends only on the literal last `d+1` parity bits.
There are finitely many possible rational values. Let `C_P` be the
maximum three-adic valuation among its nonzero values. Such a value
exists because `P!=0`: a word with a single one at an index of a nonzero
coefficient produces one. Since `2^k` is a three-adic unit, (2) follows.

For the ordinary source, an odd shortcut step is at most doubling,
and an even step halves exactly. Consequently

\[
1\le x_t\le n\,2^{2p_t-t},
\qquad 2p_t\ge t-\log_2 n.
\tag{5}
\]

Substitution of `t=k+1` in (2) proves (3). This step uses one fixed
positive ordinary source, not arbitrary finite parity witnesses. `QED`.

The finite-window normalization in (4) is the same underlying device
used by the credited PR180 `HOLONOMICITY.md` recurrence argument. The
new deduction here is the surviving denominator bound and its precise
effect on the chosen Pólya--Carlson hypotheses.

## 3. Exact consequences for finite regularization

**Theorem.** If

\[
\log\operatorname{lcm}\{\operatorname{den}(c_k):0\le k\le N\}
=o(N),
\tag{6}
\]

then `P F_n` is a polynomial. Thus `B_n` is rational and the actual
ordinary source is eventually periodic.

**Proof.** If infinitely many `c_k` were nonzero, taking `N=k` along
those clocks in (3) would contradict (6). Therefore only finitely many
coefficients survive. Rationality follows from `P!=0`; eventual
ordinary periodicity is the credited complete-denominator consumer in
the main note. `QED`.

The same conclusion holds for any fixed rational regularization

\[
H(w)=R(w)F_n(w)+S(w)\in\mathbb Q[[w]],\qquad
R,S\in\mathbb Q(w),\quad R\ne0,
\tag{7}
\]

if the coefficients of `H` satisfy (6). Clear the two rational
function denominators to obtain `Q H=P F_n+L` with nonzero polynomials
`Q,P` and a polynomial `L`. Multiplication by a fixed polynomial changes
the common denominator by at most a fixed factor: every resulting
coefficient is a finite convolution of the original ones. Thus
`P F_n` satisfies (6), and the theorem applies. All denominators of the
rational filters are cleared in this argument.

Conversely, when `B_n` is rational, a polynomial denominator makes
`P F_n` a polynomial. Therefore **the existence of a finite rational
regularization with this arithmetic property is already equivalent to
eventual ordinary periodicity**. It is not a newly constructed route
to that property.

For an arbitrary exceptional set `E`, the same proof shows that the
common-denominator condition outside `E` holds if and only if
`c_k=0` for all sufficiently large `k` outside `E`. Thus the sparse
exception version would require an eventual finite recurrence with
all its defects confined to that sparse set. Such a recurrence is not
proved here. One cannot erase the exceptional coefficients from the
primary theorem's conclusion. If its extra individual-denominator
condition is also imposed, (3) forces all but finitely many of those
exceptional coefficients to vanish as well.

## 4. Application boundary

Any finite product of the rational cycle factors in PR180's Blaschke
construction is a filter of the class (7), after `z=2w`. Applying the
tested arithmetic criterion through such a filter requires the
periodicity information just identified. The infinite product is a
different object: its coefficients have not been shown to lie in a
fixed number field with the needed denominator bounds.

This does not rule out the multipoint gain in the main note, a genuinely
new source-specific arithmetic germ, or another theorem with different
hypotheses. It rules out treating the subexponential denominator
requirement as a free consequence of finite rational pole cancellation.

No new Lean theorem or numerical census is claimed for this companion.
