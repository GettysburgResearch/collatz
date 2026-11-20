# Independent reconstruction of the symbolic-order lane

**Verdict: VERIFIED WITH A NOTATION FIX at the exact content below.**
This is a separate AI-agent reconstruction of the named deductions, not
human referee acceptance, proof-assistant certification, or a proof of
Collatz. The scientific packet remains **PROPOSED**.

## Frozen scope

| Source | SHA-256 |
| --- | --- |
| `research/creative-closure-20261120/symbolic_order.md` | `1806a2ebba515c2e606e97e2fa86c2077f456e4a6ed0cbaadc01497ddd137385` |
| `experiments/creative_symbolic_order.py` | `7eec3869f0639983a4c1121c327b618ac028a30102509c3b0f3979301313a2e7` |
| `reports/2026-11-20-creative-closure/symbolic-report.json` | `1be6160c79f4ce5b8689fb83b8a171202365be4bcf24e3282c3389a89093acb0` |

The reviewer read the complete proof and checker, independently opened
[Yolcu–Aaronson–Heule, arXiv:2105.14697v3](https://arxiv.org/pdf/2105.14697v3),
and checked the attribution of the ten-rule matrix interpretation against
Example 4.3. The source's unary-system obstruction and its proper-subsystem
termination result are not asserted to be discoveries of this packet.
The review does not reclassify every result in the earlier repository PRs.

## CSO-001: exact work accounting

**VERIFIED.** For a ternary letter immediately after a binary letter, its
prefix changes from `2x` or `2x+1` to `x`, so its bitlength cost decreases
by exactly one. Subsequent prefixes are identical because the rewrite is
an affine identity. A left-boundary rule removes a cost of one. A terminal
even dynamic rule changes no ternary prefix. A terminal odd dynamic rule
adds the bitlength of its prefix, namely `b(n)-1`. These observations give
the work identity by telescoping, with the stated ordinary input cost.

Administrative termination follows from this nonnegative integer
potential. Any irreducible proper administrative word contains no ternary
letter; its binary representation is unique. This proves confluence on
the declared proper words without requiring an unrestricted-word
confluence theorem. Counting ternary letters from the right bounds their
prefix values by `floor(N/3^j)`; summing proves the envelope, and the word
`c e^t d` proves equality at `N=3^t`. The rounding error in the asymptotic
sum is only linear in `log N`.

If an actual source has a supplied first-hit clock, no rewrite prefix can
contain more dynamic events than that clock: dynamic values follow the
same deterministic orbit and value one has only the word `cd`. The work
identity then bounds every prefix before termination is inferred. This
avoids assuming termination to prove schedule independence. The proposed
total ordinary cost function is explicitly an open obligation.

## CSO-002: one persistent carry allowance

**VERIFIED.** Independent affine evaluation at `(0,0)`, `(1,0)` and `(0,1)`
reconstructs all local coefficients without using the author's matrix
composition code. The ten admitted nonexceptional rules have nonnegative
coefficient differences and strictly positive first-coordinate constants.
Every left context preserves this strict decrease because its first
diagonal coefficient is positive.

For the exceptional rule the largest coordinatewise coefficient ratio is
exactly 26. If an affine context is `Ax+b` with nonnegative coefficients,
then `x'<=26x` implies `Ax'+b<=26(Ax+b)`. Therefore the same factor holds
in arbitrary contexts, including a right context substituted into the
local input. Consuming one unit of the original allowance makes
`26^r P+r` decrease even when the local rank grows by the full factor.

The binary source bound uses row sums plus offsets at coordinates at
least one, beginning with the right boundary `(1,1)`. This gives the
stated cubic source estimate. An exhausted budget can halt at a nonnormal
word; the source proof and checker both label that outcome UNRESOLVED.
No mathematical step supplies a sufficient allowance for every source.

## CSO-003: scalar polynomial collapse

**VERIFIED.** Nonconstant polynomials with natural coefficients have
positive degrees. Comparing leading degrees of the six indicated rules
gives `g>=f`, `e>=f`, `af>=eb`, `bf>=ga`, `f>=a^2`, `b>=g`.
Multiplying the middle inequalities cancels `ab` and gives `f^2>=eg`,
forcing `e=f=g`; then `a=b` and `a>=f>=a^2` force all five degrees to one.

The same reasoning applies to their positive integral slopes. A nonlinear
left boundary does not invalidate the comparison: its leading degree
raises both slopes to the same positive power. In the offset argument,
strict monotonicity of each nonconstant natural polynomial permits the
boundary comparisons to be canceled. The five offset inequalities force
all offsets to zero. Reversal exchanges the side of boundary composition
but leaves those necessary comparisons intact. Constant boundaries are
excluded for a real reason: they can erase a locally strict inequality.

## CSO-004: triangular matrix collapse

**VERIFIED.** Componentwise affine inequalities for every nonnegative
integer vector imply coefficientwise inequalities: test zero and send one
coordinate to infinity. After homogenization, each diagonal coordinate
obeys the preceding scalar slope constraints. All interior diagonals are
therefore one.

Choose the first superdiagonal distance carrying any nonzero interior
entry. At that distance products of interior matrices add their entries;
all shorter cross terms vanish. In a boundary comparison such as
`C(G-AB)` or `(B-G)D`, only a positive diagonal boundary coefficient
multiplies the first nonzero difference. Thus the same five offset
inequalities apply, an impossibility. This includes the offset column.
Matrices with zero diagonal coordinates or feedback below the diagonal
are outside the statement; the credited ten-rule interpretation uses
both features. There is no contradiction between CSO-002 and CSO-004.

## CSO-005: signed additive polynomial run energies

**VERIFIED WITH A NOTATION FIX.** The author clarified that `r(n)` counts
one-runs, while `s_2(n)` is popcount. On the Mersenne edge the one-run
count rises by one; the total count of both kinds of run would rise by
two. Either convention contributes only a bounded term to the proof,
but the frozen text now uses a consistent one.

The two carry families have the claimed ordinary endpoints, valuations,
bitlengths and run patterns. At the maximal degree `d>=2`, their changes
have leading coefficients respectively `beta` and `gamma`, while their
height changes have degree at most `d-1`. Monotonicity forces
`beta<=0` and `gamma<=0`. On `2^m-1`, the Mersenne step increases height
by one and shortens the long one-run by one. Its leading change is
`d(alpha-beta)m^(d-1)`, so `alpha<=beta`. The countdown changes by minus
one, one-run count by one, popcount by zero, and logarithmic height by a
bounded amount; none interferes even when `d=2`.

Boundedness below on these all-one sources forces `alpha+beta>=0`.
The three nonnegative quantities `-beta`, `beta-alpha`, `alpha+beta`
have the identically zero sum with coefficients `2,1,1`, so all vanish.
With `alpha=beta=0`, boundedness below on `2^m+1` forces `gamma>=0`.
This contradicts the existence of a nonzero maximal coefficient. The
argument covers all finite polynomial degrees and signed real
coefficients; a finite coefficient search is unnecessary. It does not
exclude position-sensitive, nonadditive or history-dependent energies.

## Independent execution and its limits

The independent program
[`creative_symbolic_review.py`](../../experiments/creative_symbolic_review.py)
imports no author checker. It reconstructs the local affine certificates,
rejects a factor-25 replacement, checks two exact cone identities, and
replays 14 ordinary carry edges with 126 moment identities at degrees
9, 12 and 17. Its binomial controls also check the leading Mersenne
coefficients through degree 32. These are finite implementation controls;
the unbounded statements rest on the deductions above.

Normal generation and optimized comparison were actually executed and
passed. The independent retained report is
[`symbolic-independent-report.json`](symbolic-independent-report.json),
SHA-256 `6c0be9746ebc67d2c942e030d4e70c868656b4d19049b1801c07b8653e19c26a`.
Complete-checkout and publication receipts are reported separately.

```sh
python -X utf8 -B experiments/creative_symbolic_review.py --compare reports/2026-11-20-creative-closure/symbolic-independent-report.json
python -O -X utf8 -B experiments/creative_symbolic_review.py --compare reports/2026-11-20-creative-closure/symbolic-independent-report.json
```
