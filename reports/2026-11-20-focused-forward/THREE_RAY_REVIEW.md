# Independent review of the ordinary three-ray packet

## Scope and source pins

This review reconstructs the new local claims in
`research/focused-forward-20261120/three-ray/PROOF.md`. It does not review
the external universal-three-ray equivalence mentioned as motivation,
and does not establish Collatz.

The content was reviewed before the parent publication commit. The parent
report supplies that full commit SHA; the following hashes identify the
exact mathematical text reviewed here.

| Path under `research/focused-forward-20261120/three-ray/` | SHA-256 | Git blob SHA |
|---|---|---|
| `PROOF.md` | `7ea7d3013e9820bd219da9ddf5294cbfbc731d68ec4195942f512e86d8666959` | `445fc7703d8e97e2c73a2189cb127c9a65cc1b11` |
| `README.md` | `d5a1778016dddfb8470699b65c4bfccc955eed4651739e999c5ca06294281ce5` | `d463372c80c6ab3db78d3854dbab39d73a3add9d` |
| `check.py` | `4b8f28464d7e2e5b92da729b8b8205f1a0a7da9e85d307a827065c71d6aec902` | `fa3f037e06d26ac64ada74623101bee42b5ec99e` |

The mathematical verdict is **VERIFIED at this exact text, with its stated
partial scope**. The checker required an optimization guard; its final
digest and replay result appear below. No pressure-packet files were
changed during this review.

## Claim-by-claim reconstruction

### TR-001: uniform cylinder criterion

**VERIFIED**, conditional on both `n` and `3n` reaching `1` as stated.

For fixed parity words the affine slopes are `3^a/2^p` and
`3^(b+1)/2^q`. Equality on an infinite binary class forces `p=q` and
`a=b+1` by uniqueness of prime factorization. The grade splitting identity
then gives `g(n)-g(3n)=2`. Conversely, that grade difference makes the two
first-arrival times have equal parity. At a sufficiently late common
clock both paths have the same endpoint on `1 -> 2 -> 1`, and their odd
counts differ by one. Their affine slopes coincide, and equality at the
given ordinary source forces equality of the intercepts. The binary class
modulo `2^h` preserves both words, including the word on `3x`.

The examples `(1,3)` and `(5,15)` have actual mergers but fail the grade
criterion. Thus a pointwise merger and a uniform fixed-word neighborhood
certificate are correctly kept distinct.

### TR-002: exact ray-to-ray pullbacks

**VERIFIED**, including unequal clocks.

After the first odd shortcut input, the orbit is a unit modulo `3` and
remains one. Therefore a path ending at `3m` has no earlier odd input and
forces `u=2^q m`. The lower path cannot reach `m` before the initial `q`
halvings. A later arrival is exactly a periodic return from `m` to itself.
The conclusion rules out another odd part for this exact diagram only;
it does not rule out more general diagrams with offset endpoints.

### TR-003: guarded physical returns

**VERIFIED**, with every displayed guard retained.

The initial `k`-step formulas were reconstructed directly. The second arm
uses its specific first three steps before the remaining odd run, so the
edge case `k=3` is included. The `R=3 (mod4)` case genuinely merges after
two further shortcut steps.

For `R=1 (mod4)`, the two endpoints after `k+2` steps are `9v+2` and `v`.
If `v=2^(2r+1)m` with `m` odd, the latter arm reaches `m` after `2r+1`
halvings. The former arm reaches `T(3^(r+1)m)` after `2r+2` steps. Shifting
along an actual forward path preserves the independent-clock meeting
relation, giving the equivalence claimed in (7).

The finite chain of obligations is `C(m),...,C(3^r m)`: its largest
**source** is `3^r m`, so `3^r m<n` is precisely the descent guard needed.
There is no requirement that the upper endpoint `3^(r+1)m` be below `n`.
For `r=0`, the valuation condition is exactly `R=9 (mod16)`, and the
source comparison changes sign between `k=7` and `k=8`. The construction
prescribing `v_2(m+1)=k'` retains this guard and shows the asserted failure
of every rank `log n+alpha*v_2(n+1)` by taking `k'=k>=8`.

Even valuations of `v`, and odd valuations failing the explicit size
guard, are not covered by this descent argument.

### TR-004: exact repetitions and finite schedule realization

**VERIFIED**, restricted to the prescribed guarded return system.

For a constant valuation, the identity
`d*u_(i+1)+7=(p/q)*(d*u_i+7)` gives the necessary divisibility by `2q^r`.
Conversely, that divisibility makes every transformed value an even
integer; reduction modulo the odd `d=p-q` proves the corresponding odd
part is integral, and parity makes it odd. Positivity follows from the
positive affine recurrence. Thus (12) is an exact maximum, not merely a
one-sided stopping bound.

For a periodic block, the `x`-coordinate formula (14) remains only a
necessary bound. The exact maximum (14a/b) uses the composed **odd-part**
map `F(u)=(P*u+C_u)/Q`, with `P,C_u` odd, `Q` a power of two, and
`d=P-Q>0`. Its endpoint transformation satisfies
`d*F^r(u)+C_u=(P/Q)^r*(d*u+C_u)`. The valuation condition makes this
endpoint a positive odd integer.

The crucial sufficiency step is valid: a nonintegral reduced dyadic
rational stays nonintegral under `(p*u+7)/q` with `p` odd and `q` an even
power of two, because the reduced numerator stays odd and the denominator
grows. Final integrality therefore forces every earlier odd-part expression
to be integral. Each preceding input must be odd for its next numerator
to be divisible by its even denominator. The endpoint is odd by the
valuation condition. These facts give every exact displayed valuation and
every physical `R=9 (mod16)` guard. Consequently the periodic formula is
sufficient at intermediate stages as well as at block endpoints.

The same argument proves realization of any finite valuation list with
entries at least `3`: the stated residue modulo `2Q` gives a positive odd
initial part and a positive odd final part, and the intervening stages
are forced integral and odd. The zero-transition case is separately
immediate. The source is allowed to depend on the finite list. No fixed
ordinary source for an infinite list is inferred.

### TR-004: complexity of a hypothetical bounded-alphabet run

**VERIFIED**, assuming one infinite physical run with `8<=k_i<=K`.

Every return is expanding, so different start positions have distinct,
increasing ordinary `x` values. Equal valuation factors yield the same
affine block `(P*x+C)/Q`. Subtracting integer endpoints and using
`gcd(P,Q)=1` gives `Q | x_j-x_i`, while `Q>=2^(11L)`. The elementary
growth estimate `x_j<=a_K^j*C_0` yields the stated exclusion of an equal
factor whose later occurrence starts before the threshold in (16).
Counting the integer positions strictly before that threshold gives the
ceiling in (17), including nonintegral thresholds and the zero lower
bound when the threshold is negative.

The coefficient is `11/log_2(a_K)`, approximately `16.18` for `K=9` and
`8.70` for `K=10`. The argument excludes eventually periodic expanding
schedules but permits aperiodic schedules of sufficient complexity. It
does not control unbounded valuation alphabets or the residue classes
outside the return guard.

## Actual bounded replay

Executed:

```sh
python -X utf8 -B research/focused-forward-20261120/three-ray/check.py
```

The result was `PASS`, with `universal_collatz_claim=false`, and the
following scopes:

| Check | Count |
|---|---:|
| Grade pairs | 2,000 |
| Uniform / nonuniform grade pairs | 466 / 1,534 |
| Pointwise pairs without cylinder certificates | 18 |
| Aligned pullback diagrams | 1,139 |
| Initial guarded endpoint replays | 2,048 |
| Immediate mergers / offset reductions | 1,024 / 1,024 |
| Odd-valuation returns / descending lists | 346 / 117 |
| Forced odd-valuation returns | 130 |
| Prescribed next valuations | 360 |
| Equal-valuation expansion controls | 13 |
| Constant / periodic schedule witnesses | 108 / 48 |
| Equal-factor divisibility checks | 1,698 |
| Variable finite schedule witnesses | 16 |

An additional independent direct shortcut-map reconstruction, importing
none of the author checker, tested all `256` length-four valuation lists
over `{3,4,5,6}`. It also tested `468` exact periodic maxima over every
block of lengths one through three over `{8,9,10}`. The latter sources
were constructed to have prescribed exact numerator valuations, including
maximum zero, rather than only to realize successful repetitions. The
two checks collectively replayed `2,856` physical guarded returns and
passed. This supplementary execution is reported as an executed local
review check, not as a separately saved standalone verifier.

## Verifier repair and remaining boundary

The initial checker relied on assertions and did not refuse optimized
Python, which can remove those assertions. The author added an explicit
`if not __debug__` rejection before the checker definitions. The final
checker has the digest in the source-pin table and is **VERIFIED WITH
THIS SOFTWARE FIX** at the bounded scope above.

The reviewer reran the normal command successfully after the repair and
also executed both commands below:

```sh
python -O -X utf8 -B research/focused-forward-20261120/three-ray/check.py
python -OO -X utf8 -B research/focused-forward-20261120/three-ray/check.py
```

Each exited with status `1` and reported
`Refusing optimized execution: this verifier requires assertions.`
No mathematical source text changed in this repair.

The first mathematical gap in a proposed full proof is unchanged:
there is no complete terminating selector for every fixed positive
ordinary input, and no exclusion of all variable expanding schedules.
The exact finite-word realization theorem specifically prevents replacing
that all-time obligation by absence of a finite admissibility obstruction.
