# Independent review of the global parity-series construction

Date: 23 November 2026. Reviewer: `positive_cycle_close`, independently of
the `global_construction` author. **Verdict: VERIFIED at the written-proof
scope specified below.** This is not a proof of Collatz, a Lean check, or
an endorsement of every inherited analytic input mentioned in the note.

## Frozen target and scope

- Target: `research/closing-step-20261123/GLOBAL_CONSTRUCTION.md`.
- Exact SHA256:
  `6293818c1de954c12ed04031680d43a807ff9544f083a29ba4568518f260c0b5`.
- Working base: PR180,
  `7d4ad9f11d3d7a54c67b0c6cff4f13a2ab967161`.
- This is a review of the new file at that content hash, before its next
  commit, not a claim that the file already belongs to the base commit.
- Primary scope: Sections 1--5, especially the finite-rank resolvent
  formula (7), Theorem 1, Theorem 2, and Theorem 3.
- Secondary scope: the elementary identities and the diagnostic parity
  construction in Section 6. The earlier reciprocal-sum/product inputs
  and finite-window rigidity theorem are retained as dependencies and
  were not re-audited here.

The target hash was checked against the actual file after reconstructing
the arguments. No author file was edited during review.

## 1. Actual operator and meromorphic construction — VERIFIED

The map is the shortcut map on positive ordinary integers. Multiplying
the literal parity weights gives
`(K^j g)(n) = e_j(n) 3^{-p_{j+1}(n)}`: when `e_j=1` the forcing
contributes the additional factor `1/3`, and when `e_j=0` both sides
vanish. Thus the displayed resolvent is the specified original series,
initially in the stated Neumann disc.

Conjugating by `f(n)=n h(n)` gives row weight
`a(n)=1/2+e_0(n)/(6n)`. The maximum is `2/3`, attained at `n=1`.
The diagonal difference from `(1/2) C_T` tends to zero and is a norm
limit of finite-rank diagonals. Truncating the first `M` output rows
gives exactly the norm bound in (6), with inverse radii increasing to
two.

The finite-dimensional inverse in (7) follows by applying `L_M` to
`f=Q_M g+z Q_M J_M L_M f`. Its determinant is one at zero; the
adjugate construction gives isolated finite-rank polar parts, and the
formulas agree on overlaps by their common inverse germ. This proves
the asserted operator-valued meromorphy throughout `|z|<2` without
assuming orbit convergence or an unmentioned Fredholm alternative.

For the first-return formula, a term `L_M A_M^j J_M` is nonzero at
input `i` precisely when the first `j` intermediate inputs following
`i` are outside `[1,M]`, and the endpoint at time `j+1` is in `[1,M]`.
Consequently the row has exactly the single monomial in (9), or is
identically zero if there is no return. The note correctly distinguishes
the convergent operator construction from a finite decision procedure
for the no-return case.

## 2. Interior poles and semisimplicity — VERIFIED

For `|lambda|>1/2`, choose `M` with `q_M<|lambda|`. A positive
non-eventually-periodic orbit consists of distinct integers and hence
eventually leaves every finite set. Repeated eigenvector equations then
bound its normalized amplitude by an arbitrarily long product of
factors at most `q_M/|lambda|<1`. The eigenvector vanishes there.

Multiplication around a cycle gives exactly
`lambda^A=3^{-p}`. Every compatible cycle meets `[1,M]`; otherwise its
normalized product would be strictly too small. Disjointness therefore
gives at most `M` compatible cycles. Conversely, pulling back one cycle
amplitude to its basin gives an element of `X`: before first entry no
state repeats, so there are at most `M` potentially expanding small-state
factors, independently of the source. This verifies the claimed kernel
dimension, support, and boundedness.

For a possible Jordan chain `(K-lambda)f=g`, restrict to each compatible
cycle. Its finite weighted permutation has minimal polynomial dividing
`t^A-3^{-p}`, whose roots are simple. Its shifted range therefore has
zero intersection with its eigenkernel. Thus `g` vanishes on every
compatible cycle and, by the proved kernel classification, everywhere.
The Laurent coefficient equations turn any pole of order at least two
into exactly the forbidden Jordan chain. The meromorphic construction
already supplies finite-rank polar coefficients. Conversely an actual
cycle eigenvector prevents a removable inverse singularity.

The carry identity for a positive cycle forces `2^A>3^p`, so all the
listed pole roots lie strictly inside the constructed disc. This proves
the complete pole statement for the **full operator resolvent**. It
does not imply that each complex pole survives in each scalar
`B_n`; the target explicitly preserves that distinction. Its separate
positive-real scalar pole claim follows from the positive cycle
numerator.

## 3. The actual forcing has the stated norm boundary — VERIFIED

For the known sources `2^k`, the first `k` parities are even and the
subsequent source is one. Hence
`B_{2^k}(z)=z^k/(3-z^2)`. The restriction
`f -> (f(2^k)/2^k)_k` is bounded from `X` to `ell^infinity` and
sends `(3-z^2)B(z)` to `((z/2)^k)_k`.

At any `|z_0|=2`, a putative meromorphic extension of this latter family
cannot have a pole: every coordinate is an entire polynomial, so all
negative vector Laurent coefficients have every coordinate zero.
Holomorphy would force norm continuity, contradicted by the exact
radial norm difference `sup_k(1-t^k)=1` for every `0<t<1`.
The scalar prefactor is nonzero at every such `z_0`.

This argument uses only known convergent sources. It remains valid if
additional cycle poles exist inside the disc, since the bounded
restriction eliminates their polar parts by the coordinate identities.
It proves an `X`-valued boundary, not a natural boundary for any single
ordinary-source coordinate.

## 4. Every polynomial-weight essential radius — VERIFIED

For fixed `k`, the row coefficient after conjugating `X_alpha` is
`3^{-p_k}(T^k(n)/n)^alpha`. The finite set of length-`k` affine
branches makes its asymptotic formula uniform in `n`; this remains
valid for negative real `alpha`, since the leading branch ratios are
strictly positive. Finite output-row truncation gives the asserted
upper essential-norm bound.

The lower bound uses actual unbounded positive cylinders:

- `n=2^k m` realizes the all-even word and ends at `m`.
- `n=2^k m-1` realizes the all-odd word and ends at `3^k m-1`; its
  intermediate states are `3^j 2^{k-j}m-1`, odd for `j<k`.

After conjugacy, distinct endpoint singleton vectors are weakly null
in `ell^infinity`. Indeed, for any bounded complex linear functional,
finite sums with unit-modulus phases show absolute summability of its
values on these singletons. A compact operator sends this bounded
weakly null sequence to zero in norm. Evaluating the selected output
rows therefore gives both necessary lower bounds against every compact
perturbation. Taking the spectral radius in the quotient by compact
operators yields exactly (17), with the unique minimum `1/2` at
`alpha=1`.

The stated forcing consequences are correctly qualified. For
`0<=alpha<=1`, the powers-of-two restriction gives its norm boundary at
`2^alpha`. For `alpha<0`, the forcing is outside the space. For
`alpha>1`, the operator essential radius grows; this alone says nothing
about a single-source scalar natural boundary.

## 5. Secondary identities and limits of this review

The finite affine identity (19) follows by one-step induction. Its
right side tends to zero in `Q_2` because `T^k(n)` is an integer and
`3^{p_k}` is a binary unit. For an eventually periodic source, its
rational continuation at two equals `-n`, since the cycle denominator
is nonzero there.

The Section 6 diagnostic has increments in `{0,1}` because the
increasing interpolating function has derivative strictly between zero
and one. Its coefficient bound at two is `O(k^{-2})`, and its infinitely
many nonzero coefficients have `k`th-root limsup `1/2`; its radius is
therefore exactly two. Its irrational parity density rules out an
eventually periodic word. The non-D-finiteness conclusion additionally
uses the pinned earlier rigidity theorem and is not an independent
result of this review. Crucially, the diagnostic is not presented as
an ordinary integer orbit.

The real boundary value for an escaping source still depends on the
earlier qualified analytic inputs; none was established by the
operator construction or this review. No inference from interior
meromorphy to scalar boundary continuation, from polynomial
reweighting to arithmetic smoothing, or from pole classification to
cycle exclusion is justified or claimed.

**No corrective edit is required for the reviewed claims at the frozen
hash.** The result is a rigorous written construction and obstruction
analysis. Collatz, the exclusion of unknown positive cycle poles, and
the required fixed-source arithmetic continuation remain open here.
