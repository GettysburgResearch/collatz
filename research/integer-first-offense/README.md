# Integer-first counterexample offense

**Agent:** `gpt56-pro-04`  
**Issue:** #46  
**Branch:** `agent/gpt56-pro-04/46-integer-first-counterexample-offense`  
**Draft PR:** #47

## Acceptance standard

A positive result must provide one ordinary positive integer and prove, with exact standard-map replay, either:

1. a nontrivial positive cycle; or
2. an infinite orbit that never reaches `1`.

The following are not candidates:

- a long finite prefix;
- a compatible inverse limit in `Z_2`;
- a real shadow;
- approximate divisibility;
- a modular lasso without an ordinary top boundary;
- a control-map orbit without an exact `3x+1` embedding.

## 1. Negative-cycle perturbation program

### Single pulse — `L-9601`, `X-9601`

Repeating a rotated negative cycle and increasing one valuation reduces to

\[
2^{Ar+\delta}-3^{kr}
\mid
(2^\delta-1)(3z+1).
\]

The exact scan checks `720,000` reduced cases through `20,000` repetitions and finds only the trivial `n=1` cycle.

### Distributed pulses — `L-9602`, `X-9602`

Arbitrary extra valuations produce an exact weighted subset sum. Distinct unit pulses satisfy

\[
H(P)=\sum_t2^{t-1}W_{p_t}.
\]

A cyclic half-balance theorem gives a complete meet-in-the-middle cover. The frozen range represents `508,127,577,642` raw labeled pulse words and contains no nontrivial hit.

### Two supports — `L-9603`, `X-9603`

Two pulse supports reduce to a bounded discrete logarithm after an exact gcd sieve. The frozen packet checks `59,385,744` pulse splits and finds no nontrivial hit.

### Two macro-blocks — `L-9604`, `X-9604`

For two compressed affine blocks, the commutator

\[
\Omega(u,v)
=(q_u-p_u)C_v-(q_v-p_v)C_u
\]

controls every `u^m v^n` candidate. Once the cycle denominator exceeds `G_m|Omega|`, all later `n` are eliminated. The frozen packet contains zero cycle hits.

## 2. Centered non-neutral support program

For every accelerated word,

\[
E_w=C_w-(2^A-3^k)
=
\sum_j3^{k-1-j}2^{A_j}(4-2^{a_j}).
\]

Valuation `2` is exactly neutral. A nontrivial positive cycle must satisfy

\[
D_w\mid E_w,
\qquad
E_w\ge2D_w>0.
\]

This branch supplies complete proposed layers through support eleven:

| claim | excluded support | exact finite packet |
|:---|:---|:---|
| `T-9601` / `X-9605` | exactly 7 non-`2` valuations | 49,471 normalized candidates |
| `T-9602` / `X-9606` | exactly 8 | 3,880,002 candidates |
| `T-9603` / `X-9607` | exactly 9 | 98,203,183 candidates |
| `T-9604` / `X-9608` | exactly 10 | 1,623,353,430 candidates represented by MITM |
| `T-9605` / `X-9609` | exactly 11 | 27,283,361,062 candidates represented by MITM |

Every packet has zero formal divisor hits. `L-9605` supplies the scalable exact join. For a split `w=uv`,

\[
D_w\mid E_w
\iff
E_u2^{-A_u}+E_v3^{-k_v}\equiv0\pmod{D_w}.
\]

The support-enumeration frontier is now led by the independent issue-#9 branch, whose proposed exact packets extend through support seventeen. Further raw support enumeration is therefore not this branch’s highest-value offense.

## 3. Christoffel full-denominator program

### Pure Farey commutator — `L-9606`, `X-9610`

If lower mechanical valuation blocks have Farey-neighbor slopes

\[
{p\over q}<{r\over s},
\qquad rq-ps=1,
\]

then

\[
\boxed{
C(\mathcal C_{p/q}\mathcal C_{r/s})
-C(\mathcal C_{r/s}\mathcal C_{p/q})
=-2^{r+s-1}3^{q-1}.}
\]

A contextual standard-factor swap therefore changes the full numerator by one exact signed `{2,3}`-unit.

### Unrepaired mechanical exclusion — `T-9606`

The standard Farey-parent factorization and cyclic-rotation identity imply

\[
\gcd(C_w,|2^A-3^k|)=1
\]

for every primitive rational lower mechanical word. Powers and upper conjugates reduce to that primitive case. Hence the only positive exact cycle in the complete unrepaired rational-mechanical class is the trivial word `(2)` at `n=1`.

### Aligned repair no-go — `L-9607`, `T-9607`, `X-9611`

For two equal-summary block constants, an aligned `R`-block mixture inherits the complete geometric factor

\[
G_R={Q^R-P^R\over Q-P}.
\]

For the two standard Christoffel conjugates, their constant difference is a pure `{2,3}`-unit while `G_R` is coprime to six. Thus the geometric factor forces an all-or-none orientation. No genuinely mixed aligned conjugate pattern can certify a cycle.

The viable compiler is consequently narrow and explicit:

```text
primitive mechanical SLP
 + genuinely nonaligned multiscale Christoffel swaps
 -> finite signed {2,3}-unit repair equation
 -> complete identity C=n(2^A-3^k)
 -> independent replay.
```

## 4. Ordinary multiplicative-refund funnel

The repository’s direct divergent-orbit programs now share one exact form:

```text
q=rho+2^H ell
 ->
q_next=sigma+P ell,
```

where `ell` is the actual ordinary most-significant lift.

The smallest live machines are:

1. the PR #45 fixed six-branch quotient chart, with constant radix `2^19`, multiplier `9^6`, and strict growth at every legal transition;
2. the PR #51 divisible-seven run core
   \[
   2^{4+3s}v^+=9^{r+1}v+1,
   \]
   where sufficiently rich nine-run windows force physical growth;
3. the PR #49 changing-height intrinsic core
   \[
   2^D C'=3^G C+1,
   \]
   where every legal transition grows the primitive core by more than 170 bits.

The load-bearing issue is the same in all three: generate the next transported low residue causally from one finite ordinary initial object and prove canonical top closure forever. Pairwise lifts, a periodic residue lasso, or a unique `2`-adic completion are not enough.

## Collaborator handoffs

Exact cycle packets and Christoffel repair identities are shared with issue #9, PR #42, PR #45, and PR #34. Ordinary refund findings are shared with issues #43 and #46 and with PRs #48, #49, and #51. The phase-1 boundary of issue #39 remains explicit: a permanent phase-1 tail is the original shortcut Collatz map shifted by one, not an extra amplifier.

## Status

No unconditional Collatz counterexample has been found. No `K-####` identifier is assigned. Every finite negative packet and reusable exact reduction is shared rather than kept private.
