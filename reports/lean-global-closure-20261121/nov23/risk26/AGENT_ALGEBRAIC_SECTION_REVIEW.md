# Independent narrow review: algebraic section rigidity

23 November 2026.

Reviewed file:
`/workspace/scratch/957bb0caa6f2/risk26/triadic/ALGEBRAIC_SECTION_RIGIDITY.md`

Reviewed SHA-256:
`aba3681326833e8a4e035affbb5e8e016615ec294b6a70932b83546fccbbf1e8`

**Verdict: VERIFIED at written-proof scope for Lemma AS-B and Theorem
AS-A, including the Newton-series conclusion, in Sections 1--3.** No
genuine gap was found in the three requested risk points. This review
uses the stated standard finite-singularity and convergent-Puiseux
facts for complex algebraic functions; it does not claim a new proof
or fresh primary-source audit of those background facts. No Lean
formalization or old-corpus replay was performed.

## 1. The section equation and the nonpolynomial reduction

The first equation of AS1 gives exactly
`f(2n)+1=(2/3)(f(n)+1)`. The stated values give `G(0)=0` and
`[z]G=3`, so the eigenseries is nonzero. The exclusion of a nonzero
polynomial eigenseries is correct: its largest positive nonzero
coefficient would force a nonzero coefficient at twice that index.
The only possible constant eigenseries is removed by its zero
constant term.

The all-continuation singular set `S` is the appropriate object.
If it were empty, the only possible finite branch obstruction would
be at zero. The original holomorphic germ is fixed by a small loop
about zero. Since that loop generates the fundamental group of the
punctured plane, continuation of the original germ is single valued
there, and it extends through zero. An entire algebraic function has
at most polynomial growth at infinity and is polynomial. Thus `S`
is nonempty.

This argument does not assume that every branch at zero is initially
holomorphic. It needs only that continuation of the chosen germ is
fixed by the generator; this fixes that germ under every loop in the
punctured plane.

## 2. The all-branch inclusion S contained in S squared

The square-root filter is an equality of germs at zero. To continue
the identity along a path realizing an arbitrary continued branch of
`cH`, one may perturb the path to avoid the finitely many additional
points in `S^2` as well as zero. Added points outside `S` are regular
for every continuation of `H`, so this perturbation does not lose the
prescribed branch.

The two square-root lifts of that path produce continuations of the
original germ of `H`. If a nonzero endpoint is outside `S^2`, neither
of its square roots belongs to `S`. Every such continued branch of
`H` is then holomorphic there, so their sum is holomorphic as well.
Therefore a singular branch of `cH` cannot occur at that endpoint.
This establishes the claimed inclusion for the complete singularity
set, not just for the principal branch.

Finiteness gives `|S^2|<=|S|`; the inclusion forces equality and makes
squaring a permutation. Every point is periodic under squaring, hence
is a root of unity of odd order. In particular `alpha` and `-alpha`
cannot both lie in `S`, since they have the same square. This is the
correct reason that cancellation from `H(-z)` is unavailable.

## 3. Puiseux propagation and the finite coefficient argument

Choose the first nonholomorphic Puiseux exponent `rho` of the selected
singular branch at `alpha`, in the normalized coordinate
`u=1-z/alpha`. All earlier terms, if any, have nonnegative integer
exponents. Since every branch of `H` is regular at `-alpha`, the
term `H(-z)` is holomorphic at `alpha` on the continuation under
consideration.

The local coordinate at `alpha^2` is `2u-u^2`, an invertible local
change with nonzero derivative. It preserves the first nonholomorphic
exponent. Holomorphic terms remain holomorphic under this change,
and no smaller singular term can be produced by a larger exponent.
The coefficient relation is consequently exactly

`|B|=(2c) 2^rho |B'|`.

A different determination of a fractional power changes the phase by
a root of unity and leaves its magnitude unchanged. The continued
branch on the squared path is reachable from the original germ, so it
is a valid branch for the next iteration of the argument. One may
again avoid all finitely many auxiliary singular preimages when
choosing that continuation path.

There are finitely many points in `S` and finitely many Puiseux
branches at each point. The exponent remains the same at every step.
Thus the positive magnitudes in this iteration form a finite set.
Two must repeat, and the fixed positive ratio must be one. This gives
`c=2^(-rho-1)` with rational `rho` outside the nonnegative integers.
For `c=2/3`, clearing the denominator of `rho+2` contradicts unique
factorization of powers of two and three.

The argument uses local expansions, rather than a potentially
cancelling asymptotic sum over dominant singularities. It therefore
does not have the usual hidden cancellation issue of that shortcut.

## 4. Descent from hypothetical Q_2 algebraicity

Choose a separable defining polynomial in `Q_2[z,Y]`, clearing its
rational-function denominators if necessary. Its derivative at `G`
is a nonzero formal series. Let its order be `s`, choose `N>=s`, and
write `G=T+z^(N+1)J` as in the note.

Here are the exact order comparisons needed for the division defining
`Q(z,J)`:

* `P_Y(z,T)-P_Y(z,G)` has order at least `N+1>s`. Hence
  `P_Y(z,T)` has the same order `s` and nonzero leading coefficient.
* Taylor expansion around the actual root `G` shows that `P(z,T)`
  has order at least `N+1+s`. The quadratic and higher terms have
  order at least `2(N+1)>N+1+s`.
* In the polynomial expansion around `T`, a term of degree `k>=2`
  in the new variable has an explicit factor
  `z^(k(N+1)-(N+1+s))`, whose exponent is at least
  `N+1-s>=1`.

All coefficients before division lie in the field `K0` generated by
the finitely many coefficients of `P` and `T`. Their lower-order
coefficients vanish as exact elements of `Q_2`, hence also as elements
of `K0`. Division therefore gives a polynomial in `K0[z,J]`, not
merely a formal or Laurent expression with uncontrolled coefficients.
At zero it is `b+dJ`, with `d` nonzero.

The constant coefficient of `J` is `-b/d` in `K0`. The formal
implicit-function recursion then puts every subsequent coefficient in
the same field. A finitely generated characteristic-zero field embeds
in the complex numbers by choosing images of a transcendence basis
and extending over its finite algebraic extension. No continuous or
whole-field embedding of `Q_2` is asserted or needed.

After applying this embedding, the polynomial implicit equation has
a nonzero derivative at its initial value. The complex analytic
implicit-function theorem gives a convergent solution whose formal
series is the embedded series. Rational constants are fixed, so
the eigenvalue remains `2/3`, the constant term remains zero, and
the first coefficient remains three. Lemma AS-B applies and gives
the required contradiction.

## 5. Newton transform and exact review boundary

The two binomial-transform generating-function identities follow
formally by summing the finite binomial relation coefficient by
coefficient. Their substitutions have zero constant term, so they
are valid over `Q_2` without complex convergence. Algebraicity is
preserved by the rational substitution and rational prefactor.
An algebraic Newton generating series would therefore make `F`
algebraic, proving the stated additional conclusion.

The theorem concerns generating functions of the full sequence. It
does not contradict every individual value being rational or triadic,
and it does not construct a successful triadic witness. Those limits
are stated correctly in the reviewed document.

The independent rational, hypergeometric, simultaneous-Mahler and
2026 value-theorem comparisons in Sections 4--5 are outside this
narrow review. They do not acquire a review verdict from the checks
above. The reviewed core Sections 1--3 have no requested fixes.
