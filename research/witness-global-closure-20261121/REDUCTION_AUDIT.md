# Exact-head audit of the reverse closure criterion

**Full witness closure: OPEN.** This note independently reconstructs the
finite reduction in PR146. It proves no new universal Collatz convergence
statement. The equivalence in RGA-002 is credited to that source; RGA-003
is a new, sharper least-failure height consequence for the direct reverse
criterion, extracted from its same frozen certificate.

## Source and review boundary

The current PR146 head was read and re-queried during this pass:

- Repository: `GettysburgResearch/collatz`.
- PR: [146](https://github.com/GettysburgResearch/collatz/pull/146).
- Full head: `fd991063721e9c157d318e40bb20131762f7d750`.
- Branch: `research/upper-bit-merger-cost-20261120`.
- State at the check: open, draft, not merged; 20 commits and 63 changed files.

The mathematical source for RGA-002 is
[`research/upper-bit-mergers/DEEP_REVERSE_BASIN.md`](https://github.com/GettysburgResearch/collatz/blob/fd991063721e9c157d318e40bb20131762f7d750/research/upper-bit-mergers/DEEP_REVERSE_BASIN.md),
specifically the reverse criterion and directed adjacent-pair equivalence.
Its Git blob is `79b051d8c9aa52f2024ee687654640b1dec91794`.

The 71 certificate rows were copied as data from
[`research/upper-bit-mergers/check_deep_reverse_basin.py`](https://github.com/GettysburgResearch/collatz/blob/fd991063721e9c157d318e40bb20131762f7d750/research/upper-bit-mergers/check_deep_reverse_basin.py),
Git blob `0a54986a14afe89162413bab5a238aa1e16f53e2`.
The frozen local [data](reverse-cover.json) has SHA-256
`fac1eb6d3f3217189c6bb9fa8b366428a02ce6bbac67379f6071dc558d95743f`.

The independent [checker](check_reverse_cover.py) reads only that JSON and
Python's standard library. It imports no source replay or search program.
It reconstructs every affine guard, the complete residue cover, the height
ratios, and the strict descent. All checks use explicit exceptions, so they
remain active with Python assertions disabled. An earlier independent
JavaScript BigInt replay gave the same cover totals and height ratio.

## RGA-001. Normalizations and the exact requested assertion

Use the ordinary shortcut map

\[
 T(n)=\begin{cases}n/2,&2\mid n,\\(3n+1)/2,&2\nmid n,\end{cases}
\]

and let C be its positive basin of 1. For positive odd n use
U(n)=(3n+1)/2^(v_2(3n+1)). The witness set E in the question is exactly
the odd part of C. Indeed, from the defining witness equation, reduction
modulo each 2^(A_i) shows that all intermediate values

\[
 n_i=\frac{3^i x+\sum_{j=0}^{i-1}3^{i-1-j}2^{A_j}}{2^{A_i}}
\]

are positive integers. The recurrence
3n_(i-1)+1=2^(A_i-A_(i-1))n_i and the next positive exponent show that
every n_i is odd, including n_r=1. Thus these are the actual accelerated
steps. Conversely, unrolling a finite accelerated trajectory gives the
witness equation.

Write the requested assertion as

\[
 (C_{512}):\quad
 128k+1\in C\Longrightarrow64k+1\in C
 \quad(k>0,\ 4\nmid k).
 \tag{1}
\]

These are exactly the source residues 129, 257 and 385 modulo 512 in
the question. For odd m define

\[
 P(m):27m\in C\Longrightarrow54m+1\in C,
 \qquad
 Q(m):54m+1\in C\Longrightarrow9m\in C.
 \tag{2}
\]

The elementary identity J(n)=4n+1, U(J(n))=U(n), for odd positive n,
and the repeated exponent-two steps give

\[
 4^j n+1\in C\Longleftrightarrow3^{j-1}n\in C\quad(j\ge1),
 \qquad U^j(2\cdot4^j n+1)=2\cdot3^j n+1.
 \tag{3}
\]

The case k=2m in (1) is precisely P(m); the case k=m is precisely Q(m).
Therefore (1) is equivalent to all P and Q. In particular it implies

\[
 (R):\quad27m\in C\Longrightarrow9m\in C
 \quad\text{for every positive odd }m.
 \tag{4}
\]

Equivalently, 3z in C implies z in C for every positive odd multiple z
of nine. These elementary reductions are also proved in the earlier
[witness packet](../witness-closure-512-2026-11-20/README.md), W512-010–020.

## RGA-002. The requested closure is equivalent to full convergence

**Verdict: VERIFIED for the stated frozen reduction and finite certificate.**

\[
 \boxed{(C_{512})\quad\Longleftrightarrow\quad(R)
 \quad\Longleftrightarrow\quad C=\mathbb N_{>0}.}
 \tag{5}
\]

The implication R=>C=N is PR146's theorem. Here is its complete logical
use of the independently checked data.

Each certificate row covers n=mt+r, t>=0, with m divisible by six and
r coprime to six. Its word has three types of move:

| Move | Exact operation | Whole-progression guard | Membership read backward |
|---|---|---|---|
| S_h | u -> (3u+1)/2^h | u odd and numerator divisible by 2^h | ordinary trajectory |
| I_h | u -> (2^h u-1)/3 | output a positive odd integer | reverse of an ordinary trajectory |
| M | u -> 3u | u a positive odd multiple of nine | exactly R |

Here h>=1. S_h comprises one odd shortcut step and h-1 halvings. Its
last output need not be odd. This distinction is checked explicitly and
prevents treating a legal unaccelerated prefix as an exact valuation word.

For every row, replay tracks an integer affine value at+b. Positivity,
parity and divisibility are checked for both coefficients. The endpoint
is a positive ternary unit and is at most 24n/25 whenever n>1. For the
row containing n=1, that one source is omitted from descent because it is
the induction base; the first legal lift is checked instead. Checking the
endpoint inequality at that first lift and checking its slope prove it
for every remaining lift.

The exact replay gives:

| Certificate datum | Verified value |
|---|---:|
| Rows | 71 |
| Common modulus | 62,208 |
| Covered residues coprime to six | 20,736, the complete set |
| Expanded ordinary and exceptional graph moves | 3,974 |
| Eligible M moves | 284 |
| Maximum row length in expanded moves | 198 |
| Endpoint/source ratio | at most 24/25 |

Assume R. Prove that every positive ternary unit belongs to C by strong
induction on its value. An even unit halves to a smaller unit. An odd
unit n>1 lies in one of the rows, whose endpoint is a smaller unit and
therefore already belongs to C. Read the row backward: S_h and I_h
preserve membership, and each M is sound by R. Hence n belongs to C.

For any remaining positive integer, remove factors of two. If the odd
part is divisible by three, one ordinary odd shortcut step sends it to
a ternary unit, which has just been proved to converge. Thus all positive
integers converge. This proves R=>C=N. The reverse implication is
immediate; RGA-001 gives C_512=>R, and full convergence gives C_512.
This proves (5).

No bound on the output witness length or exponents has been inserted
into (5). It applies to the full assertion asked by the user.

## RGA-003. A sharper height floor for the least direct-R failure

**PROVED-IN-NOTE, from the same exact certificate.** If R fails, let N_*
be its least failing antecedent: N_* is an odd positive multiple of 27,
N_* belongs to C, and N_*/3 does not belong to C. Put

\[
 H=\frac{213597}{23},\qquad H'=\frac{355995}{23}=\frac53H.
\]

Then

\[
 \boxed{3\nmid n,\ n<N_*/H\ \Longrightarrow\ n\in C,}
 \tag{6}
\]

and

\[
 \boxed{0<n<N_*/H'\ \Longrightarrow\ n\in C.}
 \tag{7}
\]

**Exact height calculation.** Suppose a row starts at n=mt+r and an M
move has source v=at+b. Its R antecedent is 3v. On the allowed t>=t_0,

\[
 \sup\frac{3v}{n}
 =\max\left(\frac{3a}{m},
      \frac{3(at_0+b)}{mt_0+r}\right),
 \quad t_0=\begin{cases}1,&r=1,\\0,&r>1.\end{cases}
 \tag{8}
\]

The fractional-linear function is monotone or constant, so these two
endpoints suffice. The independent checker evaluates (8) at all 284 M
occurrences. Its maximum is exactly H, uniquely attained at t=0 in
the row n=432t+23, whose 22nd token M has source

\[
 v=1327104t+71199.
\]

The ratio there is 3*71199/23=213597/23. Asymptotic ratios and the
excluded source n=1 are included correctly in the check.

To prove (6), repeat the unit strong induction in RGA-002 below N_*/H.
Every queried R antecedent is at most Hn<N_*. Its implication is valid
by the definition of N_*, so every step of the backward proof is sound.
The row endpoint remains a smaller unit in the same range.

For (7), remove factors of two from n. A unit odd part is already covered
by (6). Otherwise its odd part z is at least three, and its next shortcut
value is a unit with

\[
 T(z)=\frac{3z+1}{2}\le\frac53z\le\frac53n<N_*/H.
\]

Apply (6). This proves (7).

This is a height bound for a least failure of the **direct R assertion**.
It is not a replacement of PR163's separately defined least adjacent-pair
failure. The latter source's constant 176,106 also pays for decomposing
each R query into two adjacent comparisons; that extra conversion is not
used here.

The symbolic-induction agent independently reviewed the fractional-linear
supremum and both induction arguments in RGA-003, accepting them conditional
on the frozen 284-query arithmetic replay. This is an internal review with
that stated dependency, not an independent formal build.

## RGA-004. Strongest current localization and its first missing input

The latest PR146 note
[`FIVE_STEP_SEEDS_AND_MULTIPLIERS.md`](https://github.com/GettysburgResearch/collatz/blob/fd991063721e9c157d318e40bb20131762f7d750/research/upper-bit-mergers/FIVE_STEP_SEEDS_AND_MULTIPLIERS.md)
gives a further ordinary localization of physical multiplication by five.
The following seed was independently replayed here:

\[
 T^{71}(a)=v,\quad T^{71}(5a)=5v,
 \quad a=6375551795,\ v=1215835,
\]

with exactly 37 odd inputs on each arm. Thus for k>=0,

\[
 T^{71}(a+2^{71}k)=v+3^{37}k,
 \quad T^{71}(5a+5\cdot2^{71}k)=5(v+3^{37}k).
\]

For every positive odd ternary unit q, choose b sufficiently large so
that 2^bq has a prescribed unit residue modulo 3^(37+d), and put
k=(2^bq-v)/3^37. Since two generates the units modulo every power of
three, one can require both k>=0 and any fixed ternary class of the
lifted source. Taking b at least D also puts that source in the fixed
binary refinement stated in the source note. Both arms then reach q,5q
after the same additional b halvings.

Consequently universal physical five closure on
x=a modulo 2^71, with 3 not dividing x, is equivalent to universal
physical five closure on all positive odd ternary units. This part is
verified directly by the seed and the lifting algebra. The additional
equivalence of universal physical five closure with full convergence is
imported from PR157, GCM-002, at
`64361ecca770092d6c8242dc6211e38818af2e50`,
`research/global-closure-20261120/merger.md`. That manuscript was read;
its separate 464-cell certificate was not independently replayed in this
audit. RGA-002 does not depend on it.

The first unsupported input is still physical closure itself: no proof
has been supplied here that an arbitrary complete witness for 27m gives
a witness for 9m, or that an arbitrary witness on the sufficient five
class gives one for its product by five. The unbounded target-witness
allowance in the question is retained throughout.

## Analytic route inspected, and its present boundary

The following exact source files were also read for the closing attempt:

| PR and full head | Files read and scope |
|---|---|
| 146, `fd991063721e9c157d318e40bb20131762f7d750` | `DEEP_REVERSE_BASIN.md`, `check_deep_reverse_basin.py`, `ReverseBasin.lean` (source inspection), `REVERSE_BASIN.md`, `THREE_RAY_ONE_SIDED.md`, `LEAST_FAILURE_SIEVE.md`, `FIVE_STEP_SEEDS_AND_MULTIPLIERS.md`, `TRIPLING_VARIATION.md`, `THREE_RAY_DENSITY.md`, `GROWING_ADDITIVE_GAPS.md`, `EXCESS_DENSITY.md`, and the packet README. |
| 163, `051237135a34ae7d4b973ee5fcf5da04ded6f0fc` | `research/deep-reverse-closure-20261120/FIVE_SLICE_ENERGY.md`, `BASIN_CRT_DENSITY.md`, `CLOSING_ATTEMPTS.md`. |
| 155, `92f499b9d340d1ff8cc643c3eef3477d61b477c1` | `research/gemini-dirichlet-global-20261120/ORDINARY_DIRICHLET_COERCIVITY.md` (OD1–OD3 proof sections) and `ENDPOINT_BOUNDARY.md`. |
| 157, `64361ecca770092d6c8242dc6211e38818af2e50` | `research/global-closure-20261120/merger.md`, the global physical-five criterion and its stated finite certificate. |
| 166, `5996b9f525ca50978bc34f423192c36a87765bf3` | `research/grh-certificate-closure-20261120/FIVE_CERTIFICATE_LADDER.md`, its physical rewrite language and explicit uncovered cases. |

PR163 gives a positive all-source comparison of tripling energy with
the energy of the legal odd ternary-unit five slice. It does not supply
a finite upper bound on that five energy. PR155's subcritical coercivity
requires a finite defect moment as input. Its endpoint result retains
an extra logarithmic kernel. PR163 explicitly keeps its fixed-target
positive-density input source-qualified; finite ternary mixing is not a
pointwise predecessor theorem at one prescribed ordinary integer.

The sparse sieve in PR146 restricts the possible global minimum. Its
retained-set count is not an upper bound for all failed comparisons.
An attempted positive summation of the discarded-index reductions led
to the new necessary-loss theorem [PRN-001](POSITIVE_RENEWAL.md). The
theorem preserves the possibility of zero rows, genuine witness-specific
loss and a different multistep proof. No finite-energy conclusion is
claimed from the source results alone.

## Executed validation and limits

These commands were executed successfully in this checkout:

```sh
python3 -B research/witness-global-closure-20261121/check_reverse_cover.py
python3 -O -B research/witness-global-closure-20261121/check_reverse_cover.py
```

Both returned identical PASS JSON, the table totals above, H and H', and
eight expected damaged-certificate rejections. The additional paired-five
seed replay returned the endpoints and odd counts in RGA-004.

The finite checks establish exact whole-progression identities and a
complete residue cover. Together with the written strong induction they
verify the stated reduction. They do not prove R. No Lean execution,
external referee acceptance, or repository-wide validation execution is
claimed by this note. The global theorem remains OPEN.
