# Independent semantic review: one two-sided pressure maximum

Reviewer: the in-session `escape_rigidity` agent, 2026-11-23.

**Verdict: PASS for the twelve public statements in `TwoSidedPressure.lean`
and their stated use in `SOURCE_CLOSURE.md`.** The review reconstructs the
arguments from their actual hypotheses. It is internal review, not external
peer review or a new proof of the escaping-orbit count imported from PR177.

## Exact inspected sources

| Source | SHA256 |
|---|---|
| `research/closure-round2-20261123/TwoSidedPressure.lean` | `bb476bfb2481226fc1566d2d44c17fde31d795171a2ca36909b563d5c0b8c84e` |
| `research/closure-round2-20261123/SOURCE_CLOSURE.md` | `50b9ebe3fe972c4c7fbbdd3697bb36917cc010f85335fb527330f2244c669f76` |

The final header and formalization boundary agree: generic maximum
attainment is proved in Lean; constructing and instantiating the positive
infinite Collatz product remains the source-pinned written argument.
Compiler and declaration-dependency receipts are separate execution
evidence maintained by the principal agent.

## Written construction and quantifiers

The exact product gives `0<r(n)<=1/n` and
`2^a(n)*r(n)=3*r(U(n))` on every actual edge. A positive weight bounded
by `1/n` has an attained ordinary maximum: compare with one positive
reference value, discard all sufficiently large integers, and maximize
over the remaining nonempty finite set. This does not assume that a
supremum is attained on a compact 3-adic space.

The chosen root is fixed before the paths or pressure exponent are
quantified. Raising its positive weight to any positive power preserves
its maximizing property. Telescoping the edge identity along every
forward path from that root gives `2^A<3^h`; telescoping every incoming
unit path to that same root gives `3^h<2^A`. Maximum attainment is not
repeated separately for different paths or directions. Positive clock
and parity make both inequalities strict. No fixed positive per-step
gap excess, identification of the two path laws, or entropy upper bound
is inferred from these comparisons.

The floor improvement also checks. The pinned counting bound
`N(x)<=4*x^(39/40)` and the component minimum `m_0` give
`sum 1/n <= integral_(m_0)^infinity 4*x^(-41/40) dx
=160*m_0^(-1/40)`. The inequality `log(1+u)<=u` then yields
`Lambda(n)>=exp(-(160/3)*m_0^(-1/40))`. Comparing the maximum with
`r(m_0)` gives the displayed upper bound on the selected root. It
does not identify that root with `m_0` or decide component membership.

The modulo-36 restriction correctly retains the unit condition. An
incoming gap-one source is a positive odd unit at target residues 2
and 8 modulo 9. At residue 5 modulo 9 the source is divisible by 3
and must not be excluded. Combining this with the forward gap-one
condition gives exactly `{7,19,23,31}` modulo 36.

The finite known graph belongs to the basin of one. Its finite inverse
enlargements stay outside a hypothetical escaping component, so tests
supported there give zero on both sides of that component's pressure
identity. The least-component floor bounds the length of the displayed
actual gap-one strings; it does not remove their pressure masses.
The unchanged-source Green terms remain nonzero at infinitely many
distinct forward endpoints. These observations agree with the note's
explicit failure to obtain an escape contradiction.

The earlier finite-boundary wording was corrected during review: an
arbitrary cheaper complete witness **trims to** a finite competitor
with no larger grade. It need not itself be one of the boundary
competitors before trimming.

## The twelve Lean declarations

1. **`path_endpoints`** retains membership of both ordinary endpoints
   in the supplied component predicate.
2. **`path_positive_clock`** derives a strictly positive total clock
   from a nonempty path and the positive exponent at each edge.
3. **`path_balance`** proves the full finite coefficient balance by
   induction from the supplied one-edge identity. It does not take
   that finite-path balance as an assumption.
4. **`attained_maximum`** constructs the finite cutoff and uses a
   finite maximum. Positivity and `n*r(n)<=1` exclude every integer
   outside that cutoff. Archimedeanness is supplied explicitly.
5. **`distinct_powers`** proves unequal powers of two and three
   when the exponent of two is positive, by reduction modulo two.
6. **`forward_coefficient`** cancels a positive selected weight
   from a forward balance and its maximum comparison; it then
   upgrades the weak comparison using the preceding parity result.
7. **`inverse_coefficient`** proves the opposite strict comparison
   from the incoming balance at that same type of maximum.
8. **`common_root_two_sided`** first invokes attained maximum and
   then returns one root with both universally quantified finite-path
   conclusions. All nonempty paths are allowed; there is no depth,
   valuation, alphabet, or terminal cutoff.
9. **`forward_value_growth`** converts the strict coefficient
   comparison to ordinary growth using the entire supplied affine
   identity, with its natural correction retained.
10. **`forward_gap_one`** obtains exponent one from positivity
    and the strict one-step comparison `2^a<3`.
11. **`no_incoming_gap_one`** excludes an incoming gap-one
    balance from the maximum and positive selected weight.
12. **`maximum_root_residues`** derives the four residue classes
    from a forward exact gap-one identity and absence of positive
    odd unit gap-one sources. It does not exclude nonunit sources.

`GapPath` supplies component membership and positive odd unit status
at every vertex, including the terminal vertex through its `nil`
constructor. Each nonempty edge has `a>0` and
`3*n+1=2^a*q`. Since `q` is odd, this equality indeed specifies the
exact valuation; it is not merely divisibility by a chosen power of
two. The recursive guards also ensure every intermediate vertex is
an actual permitted unit source.

## Scope of the result

The generic field, weight bounds and one-edge balance are explicit
theorem parameters. They are not installed as new axioms. The generic
attainment and all-path implications are formalized; the positive
infinite product, its edge identity, the sharpened floor estimate and
their instantiation for a hypothetical escaping component remain
written mathematics based on the pinned source.

Neither the module nor the written note proves that the simultaneous
forward and inverse restrictions are inconsistent. They do not resolve
nontrivial cycles or complete Collatz. Their gain is a rigorously
selected single ordinary root carrying both sets of coefficient
restrictions with their original clocks and unit guards.
