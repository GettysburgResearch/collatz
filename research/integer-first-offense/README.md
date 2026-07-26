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

## 4. Fixed-weight pulse-cycle closure

Use the exact negative-three chart

\[
A:\ 8z'=9z+1,
\qquad
B:\ 16z'=9z,
\qquad
n=6z+1.
\]

A macro with exactly `a` letters `A` and `b` letters `B` has common summary

\[
Q=8^a16^b,
\qquad
P=9^{a+b},
\]

while all chronological words of that weight form the complete macro alphabet.

### Minimum-edge and narrow-alphabet reductions — `L-9608`, `L-9609`, `T-9608`, `X-9612`

The first all-repetition packet proves that a narrow common-summary alphabet has zero cycle carry, and that a cycle minimum reduces every arbitrary macro grammar to a finite target set. Its physical specialization excludes every fixed-weight packet with `a<=5`, uniformly in `b` and repetition length.

### Terminal phase — `L-9610`, `T-9609`, `X-9613`

The final physical letter fixes the cycle-minimum level modulo nine. Combining that terminal residue with the exact height and word-independent mod-seven phase closes all fixed-weight packets through

\[
\boxed{a\le13.}
\]

### Two-sided phase floor — `L-9611`, `T-9610`, `X-9614`

For a length-`d` word, let `rho(w)` be its exact dyadic source residue and `sigma(w)` its exact output residue modulo `9^d`. At a macro boundary, the previous suffix and next prefix impose

\[
z\equiv\sigma(u)\pmod{9^d},
\qquad
z\equiv\rho(v)\pmod{Q_v}.
\]

The least positive CRT representative over all ordered suffix-prefix pairs is the universal phase floor `H_d`. The first exact certificates give

```text
H_5  =            26,873,855
H_8  =       195,221,131,263
H_10 =    90,608,969,363,967.
```

At a cycle minimum,

\[
e_w=Dm+Qk=D(m+k)+Pk,
\]

so `m+k<=e_max/D`. The depth-ten floor and a 48-row monotone parameter certificate prove every packet through

\[
\boxed{a\le243.}
\]

Frozen `X-9614` semantic digest:

```text
296074c8e5f59c11bc1de1c7d0d89084ae79012381ff1d850fb611281fe0cf06
```

### Depth-fifteen extension — `T-9611`, `X-9615`

Two independent C++ reconstructions exhaust

\[
4^{15}=1{,}073{,}741{,}824
\]

ordered suffix-prefix phase pairs and prove

\[
\boxed{H_{15}=874{,}917{,}472{,}129{,}210{,}216{,}448.}
\]

The unique minimizing phase pair is

```text
past suffix   BAAABBBBBBABAAA
future prefix BBBAABAABABAAAA.
```

The depth-fifteen floor, 132 exact parameter rows, and 28 monotone endpoint rows extend the all-repetition theorem to

\[
\boxed{
0\le a\le375,\quad b\ge1
\Longrightarrow
\text{no nontrivial positive fixed-weight macro cycle}.}
\]

The result is unbounded in pulse count, macro length, branch count, chronological switching, and repetition length. The first layer not closed by this depth-fifteen certificate is `a=376`; this is a method boundary, not evidence for a cycle.

Frozen `X-9615` file digests:

```text
run.cpp
773b700985e98822028d31d80d80b98372519c3f3163b1d8dbb16c383a7432cf

verify.cpp
d891c5d95cccc5d8cb8a8a2eb7b1e05cd08f9ae83687ef04d6db16434a2abfc3

canonical.json
9c10234f19e6486501510e29afd20f70efcd379303f3cae47fdceb6dd838175b
```

No further isolated phase depth should be added without crossing a declared theorem boundary. The next high-value target is a parameter-uniform lower bound for `H_d`.

## 5. Ordinary multiplicative-refund funnel

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

Exact cycle packets and Christoffel repair identities are shared with issue #9, PR #42, PR #45, and PR #34. The fixed-weight phase-floor theorem supplies a reusable source/output-cylinder interface for every negative-cycle-derived macro alphabet. Ordinary refund findings are shared with issues #43 and #46 and with PRs #48, #49, and #51. The phase-1 boundary of issue #39 remains explicit: a permanent phase-1 tail is the original shortcut Collatz map shifted by one, not an extra amplifier.

## Status

No unconditional Collatz counterexample has been found. No `K-####` identifier is assigned. The strongest new finite-cycle result is the all-repetition fixed-weight exclusion through `a=375`; the positive ordinary blocker remains the six-branch least-root decision.
