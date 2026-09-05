# IC-PERIODIC-001 — periodic tails and the complete denominator

## Status

- **Repository role:** accepted integrated reference after merged PR #84.
- **Component mathematics:** independently reconstructed at exact source SHAs.
- **Proof residency:** local proof packet.
- **Integrated synthesis:** **PENDING NARROW INDEPENDENT REVIEW**.
- **Collatz status:** does not construct or exclude every nontrivial positive cycle and does not resolve Collatz.

The proof below is a clean extraction of the reviewed component arguments. The exact repository-level synthesis still needs one reviewer to check the all-zero endpoint, finite preperiod, complete-denominator orientation, and fixed-block controller scope together. Until then, cite the source-qualified clauses or state this qualification.

## Setup

Use the shortcut map

\[
T(x)=
\begin{cases}
x/2,&x\equiv0\pmod2,\\
(3x+1)/2,&x\equiv1\pmod2.
\end{cases}
\]

Let

\[
w=(\varepsilon_0,\ldots,\varepsilon_{L-1})\in\{0,1\}^L
\]

be a nonempty parity word. Put

\[
s_j=\sum_{i<j}\varepsilon_i,
\qquad s=s_L,
\]

and define

\[
C_w=\sum_{j=0}^{L-1}\varepsilon_j2^j3^{s-s_{j+1}}.
\]

Direct affine composition gives

\[
T^L(x)=\frac{3^s x+C_w}{2^L}
\]

along the prescribed branches. If `w` contains an odd branch, then `C_w>0`; for `w=0^L`, `C_w=0`.

## Lemma — finite parity cylinders and infinite injectivity

Every binary word of length `n` is realized by exactly one residue class modulo `2^n`. Therefore every infinite parity word determines exactly one point of `Z_2`.

### Proof

Suppose a length-`n` word is realized by `r mod 2^n`. Its lifts modulo `2^(n+1)` are `r` and `r+2^n`. Along their common first `j≤n` branches,

\[
T^j(r+2^n)-T^j(r)=3^{s_j}2^{n-j}.
\]

For `j<n`, the difference is even, so the first `n` parity bits agree. At `j=n`, the difference is odd, so the next bits are opposite. One lift realizes the extension by `0`, the other by `1`.

Compatible residues modulo every `2^n` determine one inverse-limit point. Two points with the same complete parity word differ by every power of two and are equal. ∎

## Theorem — exact periodic fixed point

Let `w^∞` denote the infinite repetition of `w`, and let `x_w` be its unique 2-adic realization. Then

\[
\boxed{x_w=\frac{C_w}{2^L-3^s}.}
\]

The denominator is odd and nonzero. Moreover:

1. `x_w` is an ordinary integer exactly when
   \[
   |2^L-3^s|\mid C_w;
   \]
2. if `3^s>2^L` and `C_w>0`, then `x_w<0`, so the periodic schedule has no positive ordinary realization;
3. if `3^s<2^L` and `s≥1`, then `x_w` is positive ordinary exactly when
   \[
   2^L-3^s\mid C_w,
   \]
   and exact parity replay gives a positive cycle whose period divides `L`;
4. the all-zero word is the separate endpoint `x_w=0`.

### Proof

The shifted point `T^L(x_w)` has the same complete periodic parity word as `x_w`. Infinite parity coding is injective, so

\[
T^L(x_w)=x_w.
\]

Substitution into the block identity yields

\[
(2^L-3^s)x_w=C_w.
\]

The denominator is odd because an even number minus an odd number is odd. Equality `2^L=3^s` is impossible for positive `L` by unique factorization.

An odd denominator is a unit in `Z_2`, so the quotient is a valid 2-adic integer. It is an ordinary integer exactly when the ordinary denominator divides `C_w`. When `C_w>0`, the real sign is the sign of `2^L-3^s`. If the subcritical denominator divides `C_w`, the resulting positive integer has parity word `w^∞` and is fixed by `T^L`, hence lies on a positive cycle. For the all-zero word, `C_w=0` and the unique realization is `0`. ∎

## Theorem — eventually periodic positive itineraries cycle

Let an infinite parity word be

\[
u\,w^\infty
\]

with finite prefix `u`. If a positive ordinary integer `x_0` realizes this word, then after the prefix it reaches the periodic fixed point `x_w`. Therefore every positive ordinary eventually periodic parity itinerary eventually enters a positive integer cycle.

### Proof

Put

\[
y=T^{|u|}(x_0).
\]

Then `y` is a positive ordinary integer whose complete parity tail is `w^∞`. By uniqueness of infinite parity coding, `y=x_w`. The preceding theorem gives the full-denominator alternative and the cycle conclusion. The finite prefix must still be replayed exactly to certify a positive preimage. ∎

## Consequences

### Autonomous finite-state schedule firewall

An autonomous finite-state machine emits an eventually periodic word. If that word is realized by a positive integer, the integer eventually cycles; otherwise the output is a signed or nonordinary completion. Such a schedule-first machine cannot certify a divergent positive orbit.

This does not cover a seed-first nonlinear machine whose unbounded ordinary state causally generates a genuinely aperiodic word.

### The complete denominator is mandatory

The periodic class has no compactness gap left. Positive ordinary realization is exactly a finite complete-denominator condition plus exact replay:

```text
2^L-3^s divides C_w
+ the primitive positive cycle is nontrivial
+ every branch replays exactly.
```

A proper-factor hit is not enough.

### Trivial and signed cases

- The ordinary shortcut cycle `1→2→1` has primitive parity necklace `10` or `01`; it is allowed and is not a counterexample.
- Supercritical divisibility may produce a negative ordinary cycle, such as `(110)^∞` with seed `-5`.
- Other supercritical words, such as `(1110)^∞`, have nonintegral rational realizations in `Z_2`.

None is a positive counterexample.

## Fixed-block controller scope

The theorem applies directly to raw parity words. It applies to an accelerated or controller alphabet only after proving that each repeated controller symbol emits one fixed finite parity block. Recurrence of a coarse state label alone does not imply periodicity of the physical parity word.

## Boundaries and common misreadings

- The theorem does not decide genuinely aperiodic itineraries.
- It does not prove that a nonlinear seed-first machine becomes eventually periodic.
- It does not decide the least roots of the six-branch or refund architectures.
- It does not produce a nontrivial positive cycle.
- It does not replace exact finite-prefix replay by tail divisibility.
- The integrated sentence combining all clauses is not yet independently reviewed as one theorem.

## Provenance

### Main source

PR #61 at

```text
8a85b6c96d677143e08568477c26a232d56263a9
```

File:

```text
research/periodic-extraction/claims/T-7401-eventual-periodicity-full-denominator.md
```

Source author: `gpt56-complexity-01`.

### Independent and overlapping sources

PR #62 at `20a4d5d7ba9d9a2b5e7a4dfecb83f6220bb7da36`:

```text
research/ordinary-extraction/claims/T-7701-eventually-periodic-supercritical-firewall.md
```

PR #63 at `3011e6a78bd572c0c15a5b6112904f9c492ef29a`:

```text
research/ordinary-extraction-review/claims/L-7501-periodic-shortcut-fixed-point.md
research/ordinary-extraction-review/claims/T-7501-no-eventually-periodic-divergent-parity.md
```

### Review evidence

```text
reports/gpt56-crossmodel-audit-01/2026-08-01-prepublic-pr61-pr63-review.md
@ e85a9bb709da369852d2b0044a76005082a82897
```

The component statements were independently reconstructed. Frozen PR #61 and #63 packages remained `VERIFIED WITH FIXES`. A small exact audit was reported; no large search is a proof dependency.

## Exact narrow review still requested

An independent reviewer should check, as one integrated theorem:

1. the all-zero endpoint;
2. sign and complete-denominator orientation;
3. the finite-preperiod transfer;
4. positive versus signed ordinary realization;
5. the trivial cycle boundary;
6. fixed-block controller interpretation;
7. that no genuinely aperiodic conclusion is implied.

A passing review would remove this packet’s integration-wording qualification. It would not solve the cycle problem or Collatz.

## Next missing step

Either produce one nontrivial word satisfying the full denominator and exact replay, or prove a global all-word obstruction. In the FC* program, verify that the `d=0` cycle specialization is incorporated without a separate unreviewed premise.
