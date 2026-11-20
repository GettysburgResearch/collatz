# Parent reconstruction of the five-ray packet

## Exact scope and pins

The parent reconstructed the statements in the two proof files below and
inspected their arithmetic checkers. The new publication commit is recorded
in the enclosing report's validation record; these content digests pin the
reviewed bytes before that commit existed.

| Path under research/focused-forward-20261120/five-ray | SHA-256 |
| --- | --- |
| `README.md` | `36f706f8795749eaf16247c2f91a3138d54705f8b1ffdf4e84055c371f7ce96e` |
| `PAIRED_RETURNS.md` | `9078e9f0b91324f112febeb74cba163ea7b65cd34a0b6c992f0d4eeb50842150` |
| `check_paired_returns.py` | `e12c78fdd32dc35798d12da0fd5c58bef717668d98b5ad4720f5f5e0306c4ebf` |
| `FINITE_CLOCK_BARRIER.md` | `c365846083fb5ee1e1f8566092d274a7e092dfc72a47a1a24e9d43f8aa554fb0` |
| `check_finite_clock_barrier.py` | `6354edb6022243928abdb6790b093ce14da4e3cdaf5ccc208d534d64d6b01d33` |
| `search_paired_returns.cpp` | `4c6ca0701cb74bdc3e2e0ffd765d583797876023e0496d1ff7eccf25525640d5` |
| `paired_return_cones_24.tsv` | `dd1b0c1d4a0194761d630619452e7300fb4fb00d999c4746c679a1923c188c1d` |

The main source is PR #146 at
`561d48a4d3a793a59b1cdf0406062ae1a6d47515`, especially
`research/upper-bit-mergers/AFFINE_RAYS.md` for the affine and joint-label
interfaces. This review does not endorse every claim in that source family.
The universal five-ray criterion is source-qualified motivation; the new
finite paths and return obstructions can be read without importing it.

## FR-001 and FR-003: what a compression count actually counts

**VERIFIED at the pinned text.** A length-i affine word has numerator
`3^p*x+A`, with `0<=A<=3^i-2^i`. The two-arm meeting equation has a nonzero
coefficient on t, since a rational number supported on primes 2 and 3 cannot
equal 5. Its constant side has absolute value below `3*6^H` for clocks at
most H. This proves the proposed far interval has no meeting within its
compression clock.

Equal joint labels identify the all-time merger question on each fiber, but
the number of failed parameters is the sum of the sizes of the failed
fibers. Dropping those weights is unsupported. The finite-clock interval
exposes this failed transfer on the actual ordinary map. It does not supply
any permanent failure.

## FR-002: natural shells and the analytic input

**VERIFIED, SOURCE-QUALIFIED by the explicitly stated logarithmic-form
theorem.** Each arm separately visits every h-bit parity word exactly once
as t ranges over a complete binary block. Multiplication by 5 is invertible
modulo `2^h`; independence of the arms is not required. The exponential
Markov estimate and union bound therefore apply to the two marginals.

The lower parity-count bound implies a positive exponential state floor
through the first h steps. Every later shortcut step loses at most a factor
of two. This gives the stated floor through clocks below
`(1+log_2(3)/2-epsilon)*h`. A meeting above that floor would make the nonzero
form in logarithms of 2, 3 and 5 exponentially small in h.

The parent opened the primary-author publisher excerpt of G. Wuestholz,
*One Century of Logarithmic Forms*, section 5, and visually inspected printed
page 6. The source is
https://assets.cambridge.org/97805218/07999/excerpt/9780521807999_excerpt.pdf .
It gives the modified heights and the Baker--Wuestholz constant used here.
The rational field has degree one; the three modified heights are
`1,log(3),log(5)`. The coefficient of log(5) is -1, so the coefficient gcd is
one, and the modified coefficient height is at most log(H) once H is large.
The exact upper bound `9393093476352<10^13` and the dyadic threshold
comparison at `h=2^60` are valid. Polynomial lower bounds then contradict
the exponential upper bound as claimed.

The enormous sufficient threshold is an analytic deduction, not an executed
enumeration. The source's transcendence theorem was inspected and applied,
not reproved. No convergence or cycle assumption enters FR-002.

## FR-004: synchronous target gate and its clock boundary

**VERIFIED for every nontrivial synchronous ordinary return, even when the
odd counts differ.** Once an odd step has occurred, all subsequent values
are units modulo three. If the lower target u is divisible by three, its
arm consists only of H halvings, so `t=2^H*u`. The other arm begins odd and
its value at H is at least `3*(5*2^H*u+1)/2^H`, which is strictly above
`5u+1`. If instead `u=1 (mod3)`, the upper arm consists only of halvings;
its resulting formula for t makes `T^H(t)>=t/2^H>u`. Thus only the class
`u=2 (mod3)` is possible.

For fixed words on two distinct parameters, equality of affine slopes
forces equal clocks and odd counts by unique factorization. Hence the
same target gate applies to every nontrivial uniform paired-return
certificate. Its direction is retained: it obstructs backward return
branching from other target classes, but does not disprove adaptive forward
transport into the allowed class. The ordinary example `(19,96)` reaching
`(1,6)` at clocks `(14,4)` correctly shows why arbitrary unequal-clock
pointwise diagrams are outside the gate.

## FR-005 and FR-006: finite affine certificates with all-lift consequences

**VERIFIED at the pinned text.** The two six-step word pairs have the listed
slopes, intercepts, and odd counts. Their physical identities hold for every
nonnegative lift parameter. The 126 binary cells give a complete finite
classification of balanced synchronous returns through clock six: when the
odd counts agree, the relevant affine difference is constant across a cell.
This is not a classification of longer or unbalanced pointwise returns.

For the progression `t=512v+287`, the parent independently generated both
nine-step affine paths and solved all 100 cross-arm intersection equations
with exact fractions. None permits a nonnegative parameter. The final
certificate sharpens that observation: sorting all 20 coefficients also
sorts their intercepts strictly. Thus every cross-arm difference has two
coefficients of the same strict sign and has no nonnegative zero.

The synchronous ray differences are strictly negative at clocks one through
eight, and identically zero at nine. Therefore the claimed first return is
indeed first without an extra balance assumption. Its increase is
`217v+123>0`. The reverse formula reduces the question at `729v+410` to the
smaller question at `512v+287`; this reverses an actual merger equivalence
and does not pretend the lower parameter follows an inverse step as its
forward trajectory.

## FR-007: a terminating partial algorithm

**VERIFIED with explicit unresolved outcomes.** Each accepted rule has a
positive smaller target and an actual two-arm path certificate. The union
of the two binary classes and one ternary class has natural density
`95/2916` by the Chinese remainder theorem. This counts inputs permitting
one certified reduction. It is neither a convergence density nor the
proportion eventually decided by the algorithm.

The guard first performs a finite independent-clock meeting check. On a
reduction, the positive parameter strictly decreases. It consequently
terminates with a merger certificate or an expressly unresolved question.
The unresolved status at 287 after reducing 410 is consistent with FR-006.
An output of `UNRESOLVED` is never used as a counterexample or a successful
universal selector.

## FR-008: conditional unit-domain algebra

**VERIFIED conditional on the displayed unproved hypothesis (U).** Applying
that hypothesis to `4^a*x` for odd ternary units x gives
`f(3^i*5^j*x)=f(x)` for all `i>=0,j>=1`. The decomposition of an arbitrary
integer into powers of 2 and 3 times an odd unit then proves the three
multiplicative invariances of `F(n)=f(5n)`. The equality `F=f` holds on
ternary units and on multiples of five; it is not assumed everywhere.

Both shifted identities have the stated domains. The missing `10h/9h`
identity requires an equality of f and F not supplied on that domain.
The valuation-weight function is a valid countermodel for deriving that
identity solely from the two listed scaling identities. It is explicitly
not a model of all Collatz component constraints and cannot refute the
possibility that the original conditional hypothesis suffices.

## Execution evidence and first unsupported step

The originating agent ran both normal checkers and their optimized-execution
refusals. The parent additionally executes the published bytes in the clean
complete checkout recorded in the validation report. Those execution events
are kept separate from this written reconstruction. The finite assertion
checkers now refuse optimized Python, so removed assertions cannot produce
a false successful verification.

The 178 selected exploratory rows are finite physical witnesses. Their
antichain and exact union measure concern those listed ternary cones only.
The search is not needed for the elementary certificates and is not promoted
to all-depth coverage or to a proof of permanently missing ordinary targets.

The first missing universal step is an actual merger or a certified smaller
question for every retained positive parameter. The fiber-weight argument,
expanding first return, and ternary target gate explain why the attempted
shortcuts do not supply that step. The packet does not resolve Collatz.
