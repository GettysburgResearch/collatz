# IC-GHOST-001 — the `(1110)^∞` completion ghost

## Status

- **Mathematical status:** `VERIFIED`.
- **Repository role:** accepted integrated reference after merged PR #84.
- **Proof residency:** local proof packet.
- **Collatz status:** exact countermodel to an inference, not a positive counterexample.

## Statement

For the shortcut Collatz map on `Z_2`,

\[
T(x)=
\begin{cases}
x/2,&x\equiv0\pmod2,\\
(3x+1)/2,&x\equiv1\pmod2,
\end{cases}
\]

the periodic parity word

```text
(1110)^∞
```

has all of the following properties:

1. every finite prefix is realized by exactly one residue class modulo the corresponding power of two, hence by infinitely many positive ordinary integers;
2. the complete infinite word determines one unique point of `Z_2`;
3. its four-step affine map is
   \[
   T^4(x)=\frac{27x+19}{16};
   \]
4. its unique infinite realization is
   \[
   x=-\frac{19}{11}\in Z_2\setminus Z;
   \]
5. the block multiplier is `27/16>1`, so any positive ordinary realization would have unbounded orbit growth.

Therefore

```text
finite positive realizability
+ exact infinite compatibility
+ computability
+ supercritical drift
+ conditional growth
```

does **not** imply one positive ordinary all-depth trajectory.

## Lemma — finite parity cylinders are exact

Every binary word of length `n` is realized by exactly one residue class modulo `2^n`.

### Proof

Proceed by induction. The length-zero statement is trivial. Suppose a word `w` of length `n` is realized by the residue `r mod 2^n`. Its two lifts modulo `2^(n+1)` are

\[
r,
\qquad
r+2^n.
\]

Along their common first `j≤n` branches, the exact affine difference is

\[
T^j(r+2^n)-T^j(r)=3^{s_j}2^{n-j},
\]

where `s_j` is the number of odd branches among the first `j` steps.

For `j<n`, this difference is even, so the first `n` parity bits agree. At `j=n`, the difference is the odd integer `3^{s_n}`, so the next parity bits are opposite. Exactly one lift realizes `w0` and the other realizes `w1`. ∎

Passing to a compatible infinite sequence of residues gives one unique point of `Z_2`.

## Lemma — supercritical words grow if realized positively

Let an infinite parity word have `s_n` odd bits in its first `n` positions. Along that prescribed prefix,

\[
T^n(x)=\frac{3^{s_n}x+C_n}{2^n},
\qquad C_n\ge0.
\]

For a positive ordinary `x`,

\[
T^n(x)\ge x\frac{3^{s_n}}{2^n}.
\]

Thus if

\[
\liminf_{n\to\infty}\frac{s_n}{n}>\log_3 2,
\]

the orbit is unbounded. This is a conditional statement: it assumes one positive ordinary realization exists.

## Exact ghost proof

For the block `1110`, direct iteration gives

\[
\begin{aligned}
T(x)&=\frac{3x+1}{2},\\
T^2(x)&=\frac{9x+5}{4},\\
T^3(x)&=\frac{27x+19}{8},\\
T^4(x)&=\frac{27x+19}{16}.
\end{aligned}
\]

The shifted point `T^4(x)` has the same complete periodic parity word as `x`. Infinite parity coding is injective on `Z_2`, so `T^4(x)=x`. Therefore

\[
x=\frac{27x+19}{16},
\]

and hence

\[
x=-\frac{19}{11}.
\]

The denominator `11` is odd, so this rational lies in `Z_2`; it is not an ordinary integer. Direct replay gives

\[
-\frac{19}{11}
\longmapsto
-\frac{23}{11}
\longmapsto
-\frac{29}{11}
\longmapsto
-\frac{38}{11}
\longmapsto
-\frac{19}{11},
\]

with parity pattern `1,1,1,0`.

By the finite-cylinder lemma, every finite prefix has infinitely many positive ordinary representatives. By uniqueness of the infinite realization, no positive ordinary integer realizes the whole word. ∎

## Why it matters

This is a Collatz-native model of the finite-to-infinite failure. It does not depend on a complicated encoding, weak solver certificate, or changing-coordinate artifact. The obstruction already appears in raw parity coordinates.

Any proposed counterexample architecture must therefore prove an **ordinary extraction statement**, such as bounded canonical minima, eventual zero pulled-back blocks, or one explicit forever-defined seed. Compatible symbolic drift is not enough.

## Boundaries and common misreadings

- `-19/11` is a valid 2-adic integer but not an ordinary integer.
- The displayed four-state orbit is not positive and does not disprove Collatz.
- The positive finite representatives are different integers at different depths.
- The growth estimate is conditional on positive ordinary realization.
- The theorem does not prove that every supercritical word is a ghost.
- It does not exclude an adaptive seed-first machine that proves one ordinary seed.
- Similar words may realize negative ordinary integers: for example, `(110)^∞` realizes `-5`.

## Abundance, not universal exclusion

There are continuum many supercritical words: modify `(1110)^∞` on arbitrary subsets of a fixed zero-density infinite set of positions. The limiting one-frequency remains `3/4`. Ordinary integers are countable and each has one parity word, so continuum many such words have nonordinary realizations.

This cardinality argument proves abundance of ghosts, not absence of all ordinary supercritical words.

## Provenance

Primary source: PR #57 at

```text
f12e6ec45a88da98b64ef97bdfd25c3c7d48b435
```

Source file:

```text
research/ordinary-extraction/claims/T-7602-supercritical-ghost-schedules.md
```

Source author: `gpt56-global-01`.

Independent review:

```text
research/positive-coefficient-gate/reviews/PREPUBLIC-PR56-PR57-PR60.md
@ 1c25b5e4be25a7c73b78e80b505c54879f02d8f1
```

The theorem was independently reconstructed. A small exact replay was reported; no expensive computation is a proof dependency.

## Next missing step

For a concrete seed-first architecture, decide the canonical least-root sequence or prove eventual ordinary-boundary stabilization. Constructing another exact high-drift inverse-limit word does not cross the ordinary-extraction boundary.
