# Independent review of CUBE-4

**Verdict: VERIFIED WITH EXTERNAL INPUTS at the exact files below.** This is
an independent reconstruction of the stated written proof, retaining its
**source-qualified, ineffective** scope. It is not a proof of Collatz, a
formal verification, or an independent proof of the external analytic
theorems. Review performed on 20 November 2026 by the forward-bridge agent,
separately from the cycle packet's author.

## Frozen scope

| File | SHA-256 |
| --- | --- |
| `research/independent-attack-20261120/PROOF.md` | `7d3a63cfd53fd0298c5beebe9fe80ee414a7d43780169a6aab3e2c3920c55bed` |
| `research/independent-attack-20261120/check_cubic_descent.py` | `93ddaab395a81e26e4af2fb7ebaab1631de8941373dbc4e31bab06c506804d2e` |

The reviewed claim is finiteness of primitive positive ordinary cycles
admitting an **exact four-power factorization**, every exponent at least
two, whose global minimum lies in a factor of exponent three. The other
roots and exponents are unrestricted. No sparse-gap extension, no effective
period bound, no emptiness claim, and no square-descent exclusion is included.
The proof's added explanatory inequality in Section 1 and its explicit use
of the outward lower saving `b_C` in Section 4 were reread before freezing
these hashes. The latter preserves all strict margins and does not require
equality with the actual error saving.

## Independent reconstruction

The reviewer derived the powered endpoint brackets and the positive integer
multiplier, including why a contracting root repeated at least twice must
actually decrease: an increasing segment would require a nonzero multiple
of `B^e` strictly between zero and `C_W<B^2`.

The first-copy minimum argument uses the stronger bound
`B^e <= 2^(w+(c-1)q)(m+1)`, not merely the preceding coarse length bound.
It yields the claimed small entry height. The four-factor sweep then gives
`L=O(H)`, and the sum of logarithmic odd-step corrections is `O(log L)=o(H)`.
The cube floor, multiplier upper bound, and leading-monomial saving were
reconstructed from the two endpoint brackets.

For the comparison lemma, the reviewer checked both the projective product
and the degenerate outcomes. Each outside-prime contribution is bounded by
the corresponding integer multiplier, so the total charge is `M^k N`.
Outside-S coordinate norms are at most one, and the product of S-norms is
therefore at least projective height. For two retained monomials, the
strict saving beyond their gap forces any fixed rational relation to be
the exact displayed sum; the one-term case is analogous. The resulting
2-divisibility contradicts the included strict multiplier-size bound.

Both transport cases were checked. For a nonminimum descending power of
exponent `e>=2`, its endpoint bracket bounds `cq` by
`(H_exit+drop_per_copy)/(e-1)`. This gives the required lower phase height
`h_exit/c - (c-1)*total_drop/(2c)`. It justifies transport through the
extra descent in the two-rise case. In the three-rise case, intervening
factors have the stated lower phase height independently of their exponents.

The floor-three abstraction is valid for arbitrary exponents above two:
only their total gain enters the height domain, and they never supply
comparison coordinates. Replacing `c` by `485/306` enlarges the domain,
increases multiplier charges, and decreases the savings and divisibility
floors in the required directions. The reviewer also reconstructed the
bounded-polytope vertex argument and the recursive complement-of-strict-
comparisons algorithm, including boundary and lower-dimensional cases.

No gap was found in these steps under the stated analytic inputs.

## Execution actually performed

From the complete local repository directory, the reviewer ran:

```sh
python -B research/independent-attack-20261120/check_cubic_descent.py
```

The command exited with status zero. It reported seven covered cubic-descent
cones in **308** exact recursion nodes; the all-nonsquare domain was empty.
It replayed **378** ordinary powered-block arithmetic examples. The
square-descent point survived every proposed comparison, and deleting all
comparisons produced an uncovered witness, as the two negative controls
require. The scalar check returned
`944067/2887091` for the extra-drop upper bound and
`56369617346/250642805165` for the comparison-margin lower bound.

The reviewer read and reconstructed the checker but did not write a second
implementation of its cone search. This run does not independently certify
every possible ordinary cycle or execute the analytic Subspace Theorem.

## Dependency and acceptance boundaries

The review assumes the logarithmic-form consequence
`log(minimum+1)=O(log period)` and the rational p-adic Subspace Theorem in
dimensions two and three, as cited in Section 7. It checks their role and
the stated application hypotheses; it does not reprove those inputs.

The earlier PR #145 four-factor classification is not re-reviewed here.
Combining it with CUBE-4 to leave only a descending square retains that
earlier result's separate source and review qualifications. The verdict
above does not automatically extend to later edited proof bytes or to any
stronger statement.
