# Independent review: the quantitative density-free germ criterion

23 November 2026. Reviewer: the finite-mass research lane. **VERIFIED at
the written, source-qualified scope of DG1--DG6.** No universal germ
construction or full Collatz proof is included in this verdict.

## Exact object and independence

Reviewed source:

`research/lean-exact-witness-global-20261121/construction-attacks-20261123/germ/DENSITY_FREE_DEFLATED_GERM.md`

SHA256:
`dd9f6d886e85ce7c58bbcf701b584ecefe05df50885c0edd3bb64c0405f45990`.

The reviewer did not author the germ argument. The separate full-source
projection packet is this reviewer's work and is not a premise of DG1--DG6.
This review reconstructs the arithmetic, local realizations, potential
matrix, rational-series consumer and frozen cycle attachment. It does not
claim an independent proof of the external arithmetic-geometric theorem.

The primary paper was opened directly at
<https://arxiv.org/pdf/2305.17210>. Sections 2.3--2.7 and 4.1--4.3 were
read, including the matrix convention and the full integral-model and
local-realization hypotheses. An initial attempt at the version-suffixed
URL failed; the unversioned primary PDF was then successfully read.
The parent also supplied its saved primary-tool excerpt, which agrees
with the relevant theorem text. The entire frozen PR182
[`RATIONAL_SELECTION.md`](https://github.com/GettysburgResearch/collatz/blob/e4367dd2c4406c1041e66d82dfba822908747fa3/research/profound-round6-20261123/RATIONAL_SELECTION.md)
was fetched independently, with particular attention to R6-SEL-1--4 and
its prefix formula.

## DG1: actual positive source and local radii

For a positive ordinary source, an odd shortcut step multiplies height by
at most two, whereas an even step divides it by two. Hence
`1<=x_k<=n*2^(2p_k-k)`. This gives the stated lower bound on every
`p_k`, without the existence of a density limit. It yields the complex
radius at least `sqrt(3)`. The independent upper bound `p_(k+1)<=k+1`
gives ternary radius at least `1/3`. Binary and all other prime-integrality
statements also follow directly from the coefficients.

The identity `B_n(2)=-n` is binary: its finite remainder
`2^k*x_k/3^p_k` has binary valuation at least `k`. It is not an evaluation
of the original complex series at two. The actual translated binary germ
is therefore well-defined. The discs `|z|_2<1` and `|z-2|_2<1` are the
same disc, so `F_n=(z^2-3)B_n` gives one analytic function there with both
literal Taylor germs. Multiplication does not create any new asserted
radius at infinity or three. These distinctions are retained in the note.

## DG2--DG3: potential matrix and strict strategy

For a disc of radius `r`, the diagonal Green constant in the coordinate
`z-center` is `log r`. Disconnected components give zero off-diagonal
terms. In the common binary unit disc the distance between zero and two
is `1/2`, giving off-diagonal term `log2` and zero diagonal terms. This
agrees with the primary paper's matrix convention.

The contributions at infinity and three give exactly

`[[log(4/9),log2],[log2,log(2/3)]]`.

The strategy `(2/5,3/5)` has column payoffs
`log(128/81)/5` and `log(32/27)/5`; both are strictly positive.
Their minimum therefore bounds the payoff against every mixed column.
Finite shrinkage of the selected discs preserves a strict margin.

For the improved threshold, set
`A=log(3/(2-b))`, `B=log(1/b)`, `L=log2`, with `1/2<b<1`.
The derivative computation is correct. One direct sign check is
`A>log2`, `B<log2`, `b<1<2-b`, which gives
`bB<(2-b)A`. Hence `AB<L^2` by comparison with `b=1/2`.
The first strategy coordinate `(L+B)/(2L+A+B)` lies strictly between
zero and one, and direct multiplication gives equal column payoffs
`(L^2-AB)/(2L+A+B)>0`.

Choosing a radius at zero slightly below `2-b` is permitted since
`2-b<3/2<sqrt3`. The complex discs can have disjoint closures; the
ternary radii can be slightly below `1/3` and `1`. At the other finite
places, the specified open unit residue discs are exactly the integral
model's reduction fibers. No strict-radius assertion at a boundary point
is needed.

## DG4: the actual external-theorem interface

Take the projective line over the rationals, centers zero and two, and
the smooth proper model over `Z[1/6]`. Both formal functions have
coefficients in that base ring under the stated arithmetic hypothesis.
The prescribed reduction-fiber domains are present at every remaining
finite prime. At two, the common actual binary analytic function realizes
both germs. At infinity and three, the functions are placed on disjoint
components, where no extra agreement on an overlap is required.

These are the hypotheses actually required in Section 4.1. The primary
Theorem 4.3 concludes one rational function realizing the formal germs
when the global game value is positive. Thus its application here yields
rational `F_n`, and division by `z^2-3` yields rational `B_n`. A finite
Taylor fit or a freely chosen second germ would not establish these
hypotheses.

The recalled rational-series consumer is valid without a density limit.
A fixed coefficient recurrence becomes a deterministic rule for the next
parity bit after multiplication by `3^p_k`: its two possible leading
terms are distinct. There are finitely many preceding parity blocks, so
the actual tail is eventually periodic. For its repeated actual word,
coprimality of the powers of two and three gives all repeated-word
divisibilities of the same integer displacement. That displacement must
be zero. This is ordinary eventual periodicity, with no change of source.

## DG5: standard-cycle selection and converse

The formal inverse of `1+4t+t^2` has integer coefficients by the displayed
two-term recurrence. Therefore the new arithmetic hypothesis on `K_n`
does imply the coefficient-ring hypothesis on the actual `J_n`, even
though no preservation of the complex radius through division is needed.

The frozen R6-SEL-4 proof applies after eventual periodicity has already
been obtained. Its positive pole cannot cancel: the chronological carry
polynomial is positive at the positive denominator root. For
`u=A/gcd(A,p)` and `v=p/gcd(A,p)`, the factor `z^u-3^v` is irreducible by
the constant-term and coprime-exponent argument. Any prime dividing
`2^u-3^v>1` is neither two nor three and forces a pole strictly inside
the corresponding unit disc centered at two. That contradicts the
`Z[1/3]` coefficient condition. If `2^u-3^v=1`, the modulo-eight argument
forces `(u,v)=(2,1)`, and equality in the actual positive cycle product
forces every odd state to be one.

Thus the use of R6-SEL-4 does not import R6-SEL-5's density assumption.
The actual successful-prefix formula gives a polynomial `K_n` with one
common power-of-three denominator, proving the converse for every source
already reaching one.

## Verdict boundary

The resulting equivalence is supported under its exact quantitative germ
hypotheses. It removes the density-limit premise by paying explicit
complex and ternary radius requirements. It does not show that the older
qualitative Jet/J3 package already pays those requirements. The actual
arithmetic coefficients and the two required radius bounds remain
unconstructed for unrestricted positive ordinary sources.

No scientific correction was required. This review did not rerun the
separate Lean capacity module; its actual execution evidence is recorded
by the module's author/root. The written analytic criterion is not thereby
claimed as a Lean theorem.
