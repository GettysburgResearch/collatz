# The character cancellation required by the ordinary escape trace

**Written finite-character identities and an exact obstruction to a triangle
bound.** This is a follow-up to PR193 at
`795cfa38fbd6a2436285edfe82580680df4f9b0d`,
`research/astra-six-hour-20261127/root/DIRICHLET_TRACE.md`. That source turns
its original-law escape trace into three fixed-conductor twists. The
calculation here expands those twists into actual Dirichlet L-functions and
shows why separate bounds for those L-functions lose exponentially. No
analytic cancellation estimate, no new GRH implication and no escape
exclusion is proved.

## The actual finite law and its multiplicative expansion

Let `q=3^k`, `k>=1`. Starting with `X_0=0`, use independent positive
exponents with `Pr(E=e)=2^(-e)` and the affine recursion

\[
 X_{j+1}=(3X_j+1)2^{-E_j}\quad\hbox{in }\mathbb Z_3.
\]

Write `p_k(a)=Pr(X_k=a modq)` and `rho_k=q*p_k`, extended periodically to
integers. This is the original finite geometric-gap law. It is supported on
the unit group `G=(Z/qZ)^*`, and its total mass over all residues is `q`.
Every unit character below is extended by zero on nonunits. With
`phi(q)=2q/3`, define

\[
 c_k(\psi)=\frac1{\varphi(q)}
       \sum_{a\in G}\rho_k(a)\overline{\psi(a)}
       =\frac32\,\mathbb E\overline{\psi(X_k)}.
                                                               \tag{1}
\]

Finite character orthogonality gives, at every integer `n`,

\[
 \rho_k(n)=\sum_{\psi\in\widehat G}c_k(\psi)\psi(n),
 \qquad c_k(1)=\frac32.                                        \tag{2}
\]

Let `chi` be one of the three real characters `chi_-4,chi_8,chi_-8`,
viewed modulo eight. For `Re(s)>1`, absolute convergence gives

\[
 L_k(s,\chi):=\sum_{n\ge1}\frac{\rho_k(n)\chi(n)}{n^s}
       =\sum_{\psi\in\widehat G}c_k(\psi)L(s,\chi\psi).        \tag{3}
\]

The product `chi*psi` is an ordinary Dirichlet character modulo `8q`,
possibly induced from a smaller conductor. It is never principal: by CRT
one can fix the ternary unit coordinate and choose an odd residue on which
`chi` is not one. Thus every series on the right converges in ordinary
order at `s=1`. The left has a periodic zero-mean coefficient, as shown in
the pinned source. There are finitely many characters, so (3) holds there
as well, with no rearrangement of an infinite character family.

In particular, putting

\[
 B_q(\psi)=-3L(1,\chi_{-4}\psi)
                +L(1,\chi_8\psi)+L(1,\chi_{-8}\psi),
\]

the completed trace in PR193 is exactly

\[
              S_k=\frac14\sum_{\psi\in\widehat G}
                                      c_k(\psi)B_q(\psi).       \tag{4}
\]

This is a finite combination of genuine Dirichlet L-values. The complete
affine Collatz law remains in its coefficients.

## An exponential cost forced by the negative-one cylinder

On the event `E_0=...=E_(k-1)=1`, whose probability is `2^(-k)`,

\[
 X_k=(3/2)^k-1=-1\pmod{3^k}.
\]

Consequently

\[
                         \rho_k(-1)\ge(3/2)^k.                 \tag{5}
\]

Evaluate (2) at the unit `-1`, subtract the principal coefficient, and use
`|psi(-1)|=1`. For every `k>=1`,

\[
 \boxed{\displaystyle
   \sum_{\psi\ne1}|c_k(\psi)|\ge(3/2)^k-3/2.}                 \tag{6}
\]

The right side is nonnegative, so the ordinary real lower bound (5) has
the required direction before applying the triangle inequality. This is
not an estimate derived from a hypothetical positive escape. It occurs
unconditionally because the original finite law includes a negative
ordinary cycle cylinder.

For example, a proof that inserts only a uniform estimate
`|B_q(psi)|<=M(q)` into (4) obtains an upper bound containing
`M(q)*sum|c_k(psi)|/4`. That particular method cannot produce a sublinear
bound in `k` when `M(3^k)` is constant or of logarithmic size: its coefficient
norm already grows exponentially. Equation (6) is a lower bound on the
*cost of that triangle estimate*, not a lower bound on `|S_k|`, and does
not refute cancellation in (4).

The large value at `-1` is situated at the least positive odd representative
`2q-1`. The harmonic trace gives that location a small reciprocal weight.
Characterwise absolute values erase this location information. This
explains why the exponential coefficient norm can coexist with a modest
ordinary harmonic trace, without introducing a different probability law.

## A precise remaining target and the GRH boundary

The principal coefficient contributes a constant independent of `k>=1`:
the principal character modulo `3^k` simply removes the Euler factor at 3
from each fixed `chi` series. It follows from (4) that the unproved target
of the pinned escape result can equivalently be written

\[
 \liminf_{k\to\infty}\frac1k\,
       \Re\sum_{\substack{\psi\bmod3^k\\\psi\ne1}}
                       c_k(\psi)B_{3^k}(\psi)\le0.             \tag{7}
\]

The real part makes the expression manifestly real; conjugate terms pair
and the complete sum is already real. A stronger bound `o(k)` would also
suffice. Its implication for absence of escape retains PR193's ordinary
density, passage and positive atom-charge inputs. It would still need a
separate positive-cycle exclusion for Collatz.

The reported November 2026 verification record for Alpoge's formal release
does cover GRH for all Dirichlet characters and moduli, including induced
characters. It does not claim general Hecke or automorphic GRH. The root
inspected Sutherland's primary verification page and its exact headline
statements; the external archive was not rebuilt here.
[MIT verification record, updated 25 November](https://math.mit.edu/~drew/grh/)

Even accepting that full Dirichlet result, a zero-location theorem or a
uniform single-character estimate does not supply (7). The missing
estimate must retain the correlation between the coefficients of the
original affine law and the L-values. Equation (6) gives an exact reason
to pursue such a correlated estimate instead of taking absolute values
character by character. No use of GRH is made in (1)--(6).

## Later source intake: primitive shells

During this pass PR193 advanced to
`2796977d3f02ad57daeb7510f16da29527f9afde`. Its
[primitive-character calculation](https://github.com/GettysburgResearch/collatz/blob/2796977d3f02ad57daeb7510f16da29527f9afde/research/astra-six-hour-20261127/global/PRIMITIVE_CHARACTERS.md)
organizes (3) into new conductor shells and retains the Gauss-sum phases
of the affine transition. The root read that written argument. Its normal
operator has both expanding and contracting directions; averaging its
squared gains does not give uniform contraction. This is a separate
obstruction from (6): even retaining the complete transition matrix still
requires control of the particular input and the signed L-value pairing.
Neither note proves that correlation estimate. The present result does
not claim priority for the conversion to ordinary Dirichlet L-functions
or for the primitive-shell identities in the newly inspected source.
