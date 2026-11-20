# Independent reconstruction of the negative-reference descent compiler

**Scoped verdict: VERIFIED WITH A WORDING FIX for NT1--NT3 and the eight
displayed infinite progressions. Global coverage remains GAP/BLOCKED.**
This is an internal independent reconstruction by a separate agent, not a
proof-assistant verification, external acceptance, or verification of
every statement in the pinned source PRs.

## Frozen review boundary

Reviewed artifacts and SHA256 values:

| Artifact | SHA256 |
|---|---|
| `NEGATIVE_TEMPLATE_GRAMMAR.md` | `a25a8b3539247f172dbae642fe5f52f8110c7b15a31f5871ede7c001473dd39e` |
| `negative_template_compiler.py` | `16aab6efe1294a33c88f8b2fadae9d8060e68cc242eee18425aab7cfdcdd1745` |
| `negative_template_report.json` | `8444c62a5bf1c63c1e109cb9d839b2d9bccda05db355304716abf2569a02777d` |

The note credits the first two contractions to PR164 at
`6fa6b429870a9cd53cde0fc77ad64a3c3956199f`,
`research/witness-closure-512-2026-11-20/continuation-negative.md`,
W512-070--072. The new contribution is the general supplied-reference
compiler and six further concrete instances. This review independently
reconstructs all eight instances; it does not promote another claim merely
because it appears at that PR head.

## NT1: the two cycle equations

I reconstructed the source and target reference paths at the base parameter
-1. Their data are respectively (odd count, clock)=(7,18) and (6,13),
ending at -1 and -5. Their terminal reference cycles have data (1,1) and
(2,3). These data give the independent linear equations

\[
a-b=A_s-r_s-11,\qquad 2a-3b=2A_t-3r_t-8.
\]

Solving them yields the stated a,b. Matching the difference between old
and new cycle counts gives r_s-7-b and (r_t-6-b)/2; the latter is integral
by the displayed equations. Taking their positive and negative parts
produces nonnegative repetition counts. The proof asserts uniqueness only
inside this two-cycle matching construction. That scope is correct.

No assertion that negative Collatz orbits converge is used. The inputs
are finite exact rational words and their terminal cycles, all of which
are rechecked explicitly.

## NT2: positive ordinary realization

The new parameter is (2^a M+c)/3^b. The ternary congruence is precisely
the condition for its integrality. The two inequalities at M=2^K-1
extend to every larger M because both relevant slopes are positive.
They therefore prove 0<M'<M on the whole stated progression.

The binary precision bounds have the correct offsets: the old source
and target perturbations begin with valuations at least K+7 and K+6;
the new perturbations have at least a+K+7 and a+K+6. At every retained
endpoint they remain even, while the finite reference endpoint is
2-adically odd. Starting from an actual integer, this ensures each
prescribed division is exact and its result is an ordinary odd integer.
Positivity follows from the positive starting values and the forward map.
This closes the potential gap between rational affine identities and
ordinary trajectories.

Removing identical terminal suffixes is valid because each affine update
is injective. At the first unequal terminal exponents, an even difference
2k gives the exact relation S=J^k(V), where J(z)=4z+1. Negative k is
interpreted by reversing the relation. Both actual values stay positive
odd, so U(J(z))=U(z) gives convergence equivalence in either direction.

## NT3: arbitrary supplied witnesses and a common strict rank

If S=J^k(V), their first odd valuations differ by 2k. Replacing the
first exponent of the remaining witness by d-2k is therefore exact,
positive, and preserves the subsequent trajectory. If a supplied witness
ends before a retained prefix, adding exponent-two loops at one is valid;
determinism forces the prescribed ordinary prefix to match this padded
witness. The generic compiler imposes no bound on the witness length or
the last cumulative exponent.

I requested one wording correction: the source conversion adds b to the
witness length and a to its **total shortcut clock**, equivalently the
cumulative final exponent A_r in the original certificate notation. It
does not in general add a to the last individual odd-step exponent.
The reviewed note contains that correction.

The actual parameter M strictly decreases at each successful recursive
call, even when different compiled templates are used. A natural-number
rank therefore rules out an infinite chain of successful calls. It does
not rule out a finite chain ending at an uncovered parameter. The note
correctly preserves `UNRESOLVED` for that event.

## Eight concrete progressions

The independent script `review_negative_templates.py` imports none of the
author's implementation. It reconstructs reference words from rational
arithmetic, checks the cycle equations, reconstructs both suffix removals,
and verifies the four ordinary affine tables for each row. Each table is
checked on constant-plus-slope input for every integer lift j>=0: every
constant remains positive odd, every slope remains positive even, and all
divisions and endpoint J identities are exact. This is an infinite-family
affine verification, not extrapolation from the first source.

The binary guard is K=11 for every row. The independently derived first
parameters, first children, residues, and scales match the note's table.
All 28 pairs of ternary cylinders are disjoint, and their exact relative
density inside the common binary cylinder is 20/2187. A ternary-unit
restriction is not silently imposed: some valid source parameters are
divisible by three.

For three ordinary lifts per row, both arms were checked with complete
first-hit witnesses, forward and reverse splicing, and additional terminal
loops. This produced 144 complete witness transformations. Exact round
trips restore the input words, and the length/total-clock changes agree
with the corrected statement. These trajectory fixtures supplement the
universal algebra; they do not establish global convergence.

## Singular reference and the remaining gap

At m=-22/243, the upper rational reference reaches -1/3 before the
proposed last algebraic step, so its next numerator is zero. It has no
finite accelerated odd valuation. The reviewer independently checked that
exception and the lower reference's endpoint -1. Thus it cannot be
admitted as an ordinary instance of NT1. The actual positive lift instead
has a large, parameter-dependent final valuation and a remaining Mersenne
target. That family remains unresolved by this compiler.

The eight-row catalog also leaves M=2047 uncovered. This is a failure of
coverage, not a counterexample to Collatz or to the conditional theorem.
The candidate zero-reference matching law remains conditional: it has not
provided a covering construction or a general exclusion theorem.

## Executed checks

Both commands completed successfully and returned byte-identical JSON:

```text
python -B review_negative_templates.py
python -O -B review_negative_templates.py
```

The frozen independent report records 32 ordinary affine tables, 144
complete witness transformations, 28 disjointness checks, and the zero
terminal exception. Its SHA256 is
`328d739c840ece80e4701bb9e2639d30c134e2e66bce5c18a8adac181b74e482`.
The independent script's SHA256 is
`429df4c2ffc061f0d81d76555c29ff55e6353f559a7f388513556479b634c345`.
