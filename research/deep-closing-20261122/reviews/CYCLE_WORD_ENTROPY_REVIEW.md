# Independent review: the full-denominator cycle word law

Scope: Sections 2--4 of `deep_cycles/GRH_AFFINE_CYCLE_ATTEMPT.md` and the
mathematical statements of `CycleWordEntropy.lean`. This review reconstructs
the algebra and quantifiers. It does not claim an independent Lean replay or
an audit of the imported Matveev or Breuillard--Varju proofs.

## Verdict: VERIFIED at the stated scope

Fix A>=1, 1<=p<=A and D=2^A-3^p>0. Every length-A parity word with p odd
branches has the stated carry C and affine map `(3^p*x+C)/2^A`. Induction
on appended bits gives `C'=3^epsilon*C+epsilon*2^j`, so the normalized
carry law follows the two coupled affine maps in the note. This is a
fixed-total-count word law; it is not a fixed-multiplier iid-additive walk.

The whole-denominator criterion is exact. If D divides C, the fixed point
C/D is a positive integer. A first incorrectly chosen parity branch would
produce an odd numerator over two; each later branch doubles the denominator
without canceling its odd numerator. The final fixed point could not be an
integer. Hence the entire word is an actual ordinary cycle. Conversely an
ordinary cycle satisfies D*x=C by the affine formula.

The binomial comparison is correct uniformly over the claimed cone. For
W=binomial(A,p),

`W*(4/3)^p <= (7/3)^A`

and 7p>=4A imply

`W^7 <= (7^7/(3^3*4^4))^A < 120^A`.

The strict final comparison needs A>0, which is present. The integers are
`3^3*4^4=6912`, `7^7=823543`, and `120*6912=829440`.
The three Lean theorem statements match this derivation, without a cycle or
GRH axiom.

Every nontrivial positive cycle is in the strict cone. Multiplying the odd
state equations gives `2^A=product_i(3+1/q_i)`. Since a cycle through one
is the trivial cycle, all its odd states are at least three, and hence
`2^A<=(10/3)^p`. The exact inequality `(10/3)^4<2^7`, raised to the positive
power p, gives `4A<7p`. This argument does not bound the period or gap
alphabet.

The law has support of cardinality at most W in Z/DZ, so its total variation
distance from uniform is at least `1-W/D`. Combining this with the explicitly
imported effective Matveev bound `D>=c*2^A*A^(-K)` gives

`TV >= 1-c^(-1)*A^K*(15/16)^(A/7)`.

The identity `120/2^7=15/16` is correct. Thus the uniform convergence of TV
to one over eligible (A,p) follows. This part is written conditional on the
stated existing Matveev specialization; Matveev is not formalized by the
three new Lean declarations.

## Rotation multiplicity and the zero atom

For a primitive shortcut cycle of period A, all A cyclic parity rotations
are distinct. One justification worth making explicit is that if its word
were a k-fold repetition of a shorter word v, the affine map for v has
positive multiplier different from one (a power of three divided by a
positive power of two). A fixed point of its kth iterate is already a
fixed point of v. The original cycle would have smaller period.

Each rotated word therefore contributes a separate zero-residue word, so
`rho(0)>=A/W`. The alternate count restricted to words beginning in an odd
branch is correct because `binomial(A-1,p-1)=(p/A)*binomial(A,p)`.

The exact one-bit rotation identities are correct:

`2*C(rot w)=C(w)` for initial bit zero,
`2*C(rot w)=3*C(w)+D` for initial bit one.

These follow either from direct carry algebra or from transport of the
rational fixed point by its first branch. They show why rotation events are
highly dependent and why treating them as independent would be invalid.
The particular zero-atom target `rho(0)<A/W` remains unproved; the TV result
neither proves nor contradicts it.

The Fourier normalization is consistent: `sum_t rho_hat(t)=D*rho(0)` and
Parseval gives `sum_t |rho_hat(t)|^2=D*sum_r rho(r)^2>=D/W`. The support
bound, not any independence assumption, supplies the last inequality.
The off-diagonal count `E-W<A(A-1)` would exclude an A-element primitive
zero cluster, since that cluster alone supplies A(A-1) ordered distinct
pairs. A generic bound on sqrt(E) cannot exploit that separation while
retaining the unavoidable diagonal E>=W.

The added entropy-deficit identity is also correct. Under the uniform
word law, the conditional law of a word given its carry residue is uniform
on its N_r-element fiber. Thus

`log W-H(rho)=(1/W)*sum_r N_r log N_r`.

A primitive zero fiber of size at least A contributes at least
`A log A/W`, and every other contribution is nonnegative. An entropy
deficit strictly below that threshold would therefore exclude the cycle,
but a bound only on its exponential rate need not reach this exponentially
small scale. This is an exact elementary identity, not an independence
claim.

## Final reviewed source binding

- Mathematical note SHA256: `935578dba46414a7ba981adbd470b008d2d7a77b6972acbace148592114ae410`.
- Lean source SHA256: `af0375fe2087f3e0d88c4bf87a67cdb283e10ce62dbb555379c855450186998d`.

## Limit of the review

This is a correct obstruction to uniform mixing of the specified law at
its prescribed cycle clock. It is not an obstruction to every application
of GRH, a proof of the atom-specific bound, or an unrestricted exclusion of
positive cycles. The cited affine-mixing theorem has separate modulus,
multiplier and increment hypotheses; this review did not audit those
external theorem proofs.
