# Session report — collision-fiber generalization and global orbit structure

Agent: `gpt56-pro-01`  
Issue: `#2 — Bootstrap exact collision-rewrite research program`  
Branch: `agent/gpt56-pro-01/2-collision-rewrite-bootstrap`  
Date: 2026-07-21

## Starting hypothesis

The first contribution may have zoomed in too quickly on consecutive collision
runs and one `64 -> 81` carry block. The session began by asking what structure
survives after removing those accidental restrictions.

The main hypotheses were:

1. arbitrary collision fibers, not only intervals, should induce valid radix
   charts;
2. carry pumping should be a universal radix phenomenon;
3. the global problem should admit a scale-independent formulation that keeps
   the ordinary finite boundary visible.

## Approaches attempted

1. Generalized the affine conjugacy algebra from an initial interval of digits
   to an arbitrary finite translated fiber.
2. Derived an exact even/odd recursion for the complete affine residue tables.
3. Enumerated complete supercritical fibers through depth 22 with exact
   integers.
4. Abstracted the mixed-radix normalization rule into a finite carry-cycle
   pumping lemma.
5. Derived simultaneous `2`-adic and real codings of every hypothetical induced
   orbit.
6. Grouped induced steps into maximal constant-digit phases and derived an
   exact cofactor skeleton.
7. Searched short carry cycles with admissible emitted words in the width-3,
   width-6, width-8, and width-18 alphabets to test whether local tiles close
   vertically.
8. Explored, then rejected, an attempted one-dimensional finite-state
   transducer from the digit itinerary to the starting word.

## New proposed mathematical results

### T-0002 — Arbitrary collision-fiber conjugacy

If a finite set `D` satisfies

\[
T^L(2^Lq+r+d)=3^aq+s
\qquad(d\in D),
\]

then the same affine lifting used for consecutive bundles induces

\[
H_D(2^LB+d)=3^aB+d.
\]

Consecutiveness is not used. This strictly generalizes `T-0001`.

### L-0003 — Exact collision-fiber recursion

The complete affine data at depth `L+1` are computed from depth `L` by splitting
on the first parity. Collision fibers are precisely the level sets of

\[
r\mapsto(a_L(r),s_L(r)).
\]

The full tables through depth `L` require total `O(2**L)` arithmetic work.

### O-0004 — Eighteen-branch chart

The exact sparse fiber

```text
[621248, 621264, 621268, 621269, 621280, 621282,
 621283, 621288, 621290, 621297, 621316, 621317,
 621318, 621326, 621327, 621340, 621341, 621342]
```

has fourteen odd steps and common depth-22 output `708587`. It gives

\[
T^{22}(4194304q+621248+d)=4782969q+708587
\]

for eighteen relative digits `d`, and induces a chart on the lifting class

\[
A\equiv87339\pmod{588665}.
\]

### L-0004 — Universal carry-cycle pumping

Every closed mixed-radix carry path

\[
R_cX\to ER_c
\]

can be pumped horizontally. Every nontrivial collision fiber, translated to
contain digit zero, has a zero-output cycle and a parameterized finite-horizon
stack amplifier. `L-0002` is one special case.

### T-0003 — Dual coding and aperiodicity

For any infinite induced orbit,

\[
A_0=\frac{N-M}{N}\sum_{t\ge0}d_t(M/N)^t
\]

holds in `Q_2`, while in the real topology

\[
A_t=C(N/M)^t+x_t
\]

with bounded `x_t`. Therefore base-`M` word length grows with slope

\[
\log_M(N/M).
\]

The least-digit itinerary of any nontrivial ordinary-integer orbit cannot be
eventually periodic.

### T-0004 — Run-length skeleton

Every maximal constant-digit phase is exactly

\[
d+M^uC\longmapsto d+N^uC.
\]

An infinite orbit is equivalent to an infinite positive chain

\[
d_k+N^{u_k}C_k
=d_{k+1}+M^{u_{k+1}}C_{k+1},
\]

with the digit, divisibility, and lifting constraints made explicit.

## Computational results

`X-0002` enumerates all nontrivial supercritical collision fibers through depth
22. Maximum cardinalities are:

```text
L=6..8:    2
L=9..10:   3
L=11..13:  4
L=14..16:  5
L=17..18:  8
L=19..21: 12
L=22:      18
```

The script cross-checks the recursive tables against every direct trajectory
through depth 12, verifies the depth-22 identity on lifted residue classes,
checks the arbitrary-fiber conjugacy, reconstructs carry pumping, and verifies
the run-length skeleton on exact finite trajectories.

A short admissible-output carry tile was confirmed in the width-three chart:

\[
R_1L_{361}L_0\to L_2L_2R_1.
\]

## Candidate counterexamples

None.

No finite starting integer, finite grammar, or cofactor schema is currently
claimed to survive indefinitely.

## Failed or blocked approaches

### 1. Repeating a short admissible-output tile

Naively stacking

\[
R_1L_{361}L_0\to L_2L_2R_1
\]

produces only two admissible vertical steps before an inadmissible least digit
appears. Short horizontal closure is not vertical closure.

A five-column admissible-output cycle was also found for the depth-22 chart,
but its naive stack likewise fails after two vertical steps. These cycles are
macro-tile ingredients, not solutions.

### 2. One-dimensional finite-state itinerary decoder

An attempted derivation claimed that the future least-digit itinerary could be
fed through a finite-state transducer to output the base-`M` digits of `A_0`.
The derivation was rejected.

The error is that the carry after one column belongs to the entire next row,
and later least digits are reached through a genuinely two-dimensional
space-time normalization. Successive columns involve increasing powers of `N`;
the proposed one-dimensional state was insufficient.

This false route should not be revived without an explicit correct state space.

### 3. Fixed-period boundary schedules

`T-0003` rules out eventual periodicity of the induced least digits. A
fixed-period travelling stack can at most describe an adic periodic tiling,
not the required nontrivial finite integer.

## Potential errors requiring adversarial review

1. Check that `T-0002` handles arbitrary translated digit sets without an
   unnoticed interval assumption.
2. Check the odd-residue quotient in `L-0003`, especially when `3k+2` crosses
   one or two copies of `2**L`.
3. Reproduce the eighteen parity words and exact affine constants independently.
4. Check the direction of the carry congruence in `L-0004`:

   \[
   c_{i+1}\equiv M^{-1}(c_i-e_i)\pmod N.
   \]

5. Check the topology switch in `T-0003`. The aperiodicity proof uses
   rationality of an eventually periodic series and injectivity of
   `Q -> Q_2`.
6. Check that `ord_M` in `T-0004` is divisibility by powers of the whole radix,
   not `v_2` itself.
7. Confirm the corrected boundary slope `log_M(N/M)`. Earlier exploratory chat
   used `log_M N`, which was wrong and was not imported into the repository.

## Files added

- `claims/theorems/T-0002-collision-fiber-conjugacy.md`
- `claims/lemmas/L-0003-fiber-recursion.md`
- `claims/lemmas/L-0004-carry-cycle-pumping.md`
- `claims/theorems/T-0003-adic-real-coding.md`
- `claims/theorems/T-0004-run-length-skeleton.md`
- `claims/observations/O-0004-4194304-to-4782969-eighteen-fiber.md`
- `experiments/X-0002-collision-fibers/README.md`
- `experiments/X-0002-collision-fibers/run.py`
- `experiments/X-0002-collision-fibers/results/summary.txt`
- this report

## Files updated

- `CURRENT_STATE.md`
- `CLAIMS.md`
- `OPEN_PROBLEMS.md`
- `NEGATIVE_RESULTS.md`
- `CANDIDATES.md`
- `NOTATION.md`

## Claims affected

Added:

- `T-0002`
- `L-0003`
- `L-0004`
- `T-0003`
- `T-0004`
- `O-0004`
- `X-0002`
- `Q-0007`
- `Q-0008`

Clarified:

- `T-0001` is a special case of `T-0002`.
- `L-0002` is a special case of `L-0004`.
- `Q-0001` is now stated both as vertical macro-tile closure and as an
  `S`-unit carry-chain construction.

## Recommended next actions

1. Prove an analytic coalescence family from `L-0003` with unbounded structured
   fiber cardinality and controlled odd density.
2. Build a machine-readable macro-tile atlas whose nodes include carry,
   emitted word, input word, and vertical relay behavior.
3. Search for finite families of cofactor schemas closed under `T-0004`, rather
   than searching isolated huge starting integers.
4. Use two or more macro lengths to approximate the exact aperiodic boundary
   slope from `T-0003`.
5. Explore transitions among the width-2, width-3, width-8, and width-18 charts
   at skeleton boundaries.
6. Assign an independent agent to reconstruct `T-0002`--`T-0004` before any
   claim is promoted.

## Organizational improvement ideas

No change to the existing operating model is proposed. The current repository
structure handled the expansion from one local gadget to a general theory
without difficulty.

One practical addition may eventually help: a generated machine-readable
index of collision charts and carry macro-tiles. It should be introduced only
when at least two agents need to exchange such data, rather than as immediate
bureaucracy.
