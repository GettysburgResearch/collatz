# Internal reconstruction: retained sibling mass and ordinary inverse transport

23 November 2026. Reviewer: the `global_cycle` lane, separate from the
escape lane that authored these notes. This is an internal written-proof
reconstruction, not an external referee report or Lean verification.

**Verdict: VERIFIED at the stated conditional and finite-path scopes.**

Exact sources, relative to the repository root:

| Source | SHA256 |
|---|---|
| `research/lean-exact-witness-global-20261121/universal-step-20261123/escape/SIBLING_BASIN_COLLAPSE.md` | `da21d0b98230fd190f318a07e04cd2a3069740c7a7a4eba52594ca4165303db2` |
| `research/lean-exact-witness-global-20261121/universal-step-20261123/escape/BALANCED_INVERSE_TRANSPORT.md` | `58f5af3b205fb1ac720593865ea2bcba60fa918c5432f0c1917a467edfa94b9b` |

Frozen parent: PR177,
`f47a5ec51aa5853f104013a6d5046d6220ff7423`.

The only requested changes during this review were wording clarifications:
the inverse trees have countably many branches even at one finite depth,
so the manuscript now says "finite-path" and "finite-depth" rather than
suggesting a finite number of inverse words. Those changes alter no
equation or proof.

## 1. Exact measure and ordinary domain

The source domain is the set of positive odd integers not divisible by
three. E is one escaping eventual-meeting component within that domain.
It is forward closed and closed under every legal unit inverse parent.
No positive odd multiple of three is silently added to its normalization.

The pressure probability uses `r(n)^s`, with s>1 and r as defined in the
note. The inherited positivity bound from `HIGH_VARIANCE_ESCAPE.md`, HE2,
is explicitly a premise; the displayed bound is `exp(-160/3)`. I checked
its application and the retained formula, not a new audit of the parent
research corpus. The estimate r(n)<=1/n makes the normalizing sum finite,
and positivity on E makes it strictly positive.

The edge factor is correctly oriented:

`r(n)/r(Un) = 3/2^a(n)`.

Thus `mu(n)=(3/2^a(n))^s mu(Un)`. This gives `mu P_s=mu` by summing
over the unique ordinary successor. P_s is not divided by its row mass
and is not treated as a Markov probability kernel.

At an ordinary positive odd unit root, every legal inverse exponent in
the unit operator gives a positive odd integer parent with exact
valuation e. Therefore its inverse words remain ordinary, with no
completion-to-integer step needed.

## 2. Predecessor mass and retention of the original source

At q in E, a source can reach q at only one depth: two depths would make
q periodic. Thus the complete Green sum, weighted by mu(q), is exactly
the mass of the ordinary predecessor set:

`A(q)=mu(q) Z_s(q)`.

This proves finiteness of Z_s at the roots actually used in the new
argument. The tree conservation identity includes the root mass
`mu(q)` separately. Distinct immediate-parent subtrees are disjoint.

For one unchanged ray q_j=U^j q_0, the predecessor sets increase, and
their union is E by the definition of eventual meeting. Hence
`A(q_j) increases to 1`. This does not introduce a stationary time law
or a different component measure.

## 3. Simultaneous sibling disjointness and all prefactors

For S(n)=64n+21, the exact identity
`3S(n)+1=64(3n+1)` gives the same successor and increases the valuation
by six. Thus `mu(S^h n)=64^(-hs) mu(n)`.

An upper sibling S^h q_j cannot lie anywhere on the original ray. If two
such roots shared a predecessor, they would lie on one forward path;
after one step the earlier sibling is on the original ray, which
contains no upper siblings. Equality is also impossible except for
identical indices. The predecessor set of q_0 is disjoint from all of
these sibling subtrees for the same forward-comparability reason.

Consequently the double mass sum is bounded by `1-A(q_0)`. Dividing each
term by A(q_j), and then using A(q_j)>=A(q_0)>0, gives exactly

`sum_j sum_h 64^(-hs) Z_s(S^h q_j)/Z_s(q_j)`

`<= (1-A(q_0))/A(q_0)`.

For a fixed h, removing the geometric factor multiplies the right-hand
side by `64^(hs)`, as printed. The sharper local identity correctly
subtracts `mu(q_(j+1))`, because this is the new root mass in the
predecessor decomposition of q_(j+1). The finite telescoping bound and
the L-clock estimate retain the same factor `64^s`.

All infinite sums are nonnegative and use countable additivity or
Tonelli. There is no exchange of an unbounded Green integral with a
weak limit in this argument.

## 4. Near-logarithmic collapse and the unproved comparison

The physical inequality `q_(j+1)+1 <= (3/2)(q_j+1)` is valid for every
positive odd source. It implies that the stated logarithmic denominator
is at most a q_0-dependent constant times `(j+1) log(j+2)`. Its reciprocal
series therefore diverges, even though the actual ray need not increase
monotonically.

A nonnegative summable Green-ratio sequence cannot stay above a positive
multiple of this divergent reciprocal sequence. This proves the stated
liminf zero. The proposed (HC) would contradict it on an escaping ray,
which eventually exceeds its fixed threshold Q. The manuscript does
not assume (HC), and correctly warns that a mere infinite subsequence
of good clocks need not retain a divergent reciprocal sum.

The ternary-precision comparison is also correctly scoped. P_s^k1
depends only on the root modulo `3^(k+1)`, by induction through its
literal inverse branches. Since

`v_3(S^h q-q)=v_3(64^h-1)-1=1+v_3(h)`,

the choice h=3^d preserves all depths k<=d. Its actual source weight is
`64^(-s 3^d)`, and its root is S^(3^d)q, not Sq. The cost and changed
sibling are both retained.

## 5. Complete branch address and bijection

For each of the six units q modulo nine and c in {1,2}, the six powers
of two give exactly one base exponent e_c(q) in {1,...,6} satisfying
`2^e q = 3c+1 (mod 9)`. I reconstructed the table; all twelve entries
match. Every legal positive exponent has exactly one address `(c,j)`
with `e=e_c(q)+6j`, j>=0.

For roots in the same residue class modulo three, the corresponding
base exponents have equal parity. Their signed difference lies in
{-4,-2,0,2,4}. Pairing the same address gives parents in the same class
c modulo three, so the construction continues at every depth. Swapping
the roots inverts it. The construction is a bijection of all finite
inverse words, including unbounded exponents, and is prefix compatible.

At a fixed depth, deterministic forward iteration gives one inverse word
for each source vertex; this remains true for periodic roots. Identifying
vertices across different depths would fail for periodic roots, and the
manuscript explicitly reserves the all-depth predecessor-set bijection
for nonperiodic roots.

## 6. Signed pressure cost and physical height

For the complete address, the total exponent difference Delta satisfies
`-4k <= Delta <= 4k`, and the exact pressure factor is
`2^(-s Delta)`. The branch sums converge at each finite depth for every
s>0 by their geometric exponent tails. Summing the bijection therefore
gives the exact weighted identity and both exponential finite-depth
bounds. The full lower bound remains a discounted Green function;
discarding the discount is not licensed.

From the actual equations
`3q_i+1=2^e_i q_(i-1)`, taking the quotient of primed and unprimed
equations gives one-step factor

`(q_i'/q_i) (q_(i-1)/q_(i-1)') lambda(q_i)/lambda(q_i')`.

Telescoping verifies exactly

`2^Delta=(q/q') (q_k'/q_k) product_i lambda(q_i)/lambda(q_i')`.

On an escaping component, each finite predecessor product is at least
the inherited full escaping-orbit product `exp(-160/3)`. Thus the two
inequalities around this physical-height ratio have the printed
constants and orientations.

For q'=Sq in the same component, the transported ancestor mass ratio is

`mu(q_k')/mu(q_k)=64^(-s) 2^(-s Delta)`.

The extra sibling normalization is essential and is present. At a
nonperiodic root the full pressure-address law normalized by Z_s(q)
is exactly the ordinary predecessor mass normalized by A(q). Hence
the full Green ratio is its exponential moment of the signed cost.
No source-height distortion or collision factor has been dropped.

## 7. Independent finite controls and omissions

I separately implemented direct modular exponent selection and rational
edge telescoping, without running the author's checker. The results are
in [escape-independent-controls.json](escape-independent-controls.json):
72 same-class paired-parent controls, 384 depth-three exact signed
telescopes, and fixed-depth collision checks at six ordinary roots.
These bounded controls support the arithmetic reconstruction; they are
not proofs of all-depth bijectivity or infinite summability.

No new Lean verification of the measure arguments is claimed. No
power-boundedness or recurrence theorem from Assani, stationary law from
another PR, or source-free Haar comparison is imported by this review.
Bibliographic characterizations of those external works were not
independently re-audited here.

The remaining load-bearing step is the stated amortized estimate on the
actual signed compiler cost under the retained ordinary pressure law.
The per-edge bound and existence of both signs do not prove it. The
review does not prove (HC), eliminate an escaping component, exclude
positive cycles, or resolve the residue-512 implication.
