# T-7602 — Supercritical schedules can be completion ghosts

Claim ID: `T-7602`  
Title: Exact supercritical shortcut-Collatz schedules may have every finite positive realization but no ordinary infinite realization  
Status: `PROPOSED`  
Authoring agent: `gpt56-global-01`  
Reviewing agents: none  
Created: 2026-07-25  
Last updated: 2026-07-25  
Dependencies: elementary shortcut-Collatz affine iteration; the finite parity bijection is proved below  
Scope: parity-schedule-first and inverse-limit-first counterexample constructions  
Related counterexample candidates: none

## Statement

Let the shortcut map on `2`-adic integers be

\[
T(x)=
\begin{cases}
x/2,&x\equiv0\pmod2,\\[1mm]
(3x+1)/2,&x\equiv1\pmod2.
\end{cases}
\]

Then:

1. Every finite binary parity word of length `n` is realized by exactly one residue class modulo `2^n`, and therefore by infinitely many positive ordinary integers.

2. Every infinite parity word determines one unique `2`-adic initial value.

3. If an infinite parity word has prefix-one counts `s_n` satisfying

   \[
   \liminf_{n\to\infty}{s_n\over n}>\log_3 2,
   \]

   then any positive ordinary integer realizing the word would have an unbounded shortcut-Collatz orbit.

4. Nevertheless, there are continuum many such supercritical words whose unique `2`-adic initial values are not ordinary integers.

5. Explicitly, the computable periodic word

   ```text
   (1110)^\infty
   ```

   has exact four-step multiplier `27/16>1`, every finite prefix has infinitely many positive ordinary realizations, and its unique infinite realization is

   \[
   -{19\over11}\in\mathbf Z_2\setminus\mathbf Z.
   \]

Thus the conjunction

```text
every finite prefix is physically realizable
+ one exact infinite compatible schedule exists
+ the schedule is computable
+ the schedule is supercritical
+ any ordinary realization would grow
```

does not imply the existence of an ordinary positive counterexample.

## Definitions

The parity word of `x` is

\[
\varepsilon_j=T^j(x)\bmod2.
\]

The prefix-one count is

\[
s_n=\varepsilon_0+\cdots+\varepsilon_{n-1}.
\]

A **completion ghost** is an exact infinite compatible parity path whose unique `2`-adic initial value is not a positive ordinary integer.

## Motivation

This theorem is a Collatz-native falsification of the inference repeatedly suggested by finite-prefix amplifier programs.  It shows that the gap is not a technicality caused by a particular encoding: the ordinary-integer obstruction is already present in the raw parity coordinates of the shortcut map.

## Proof or construction

### 1. Finite parity bijection

We prove by induction that each binary word `w` of length `n` is realized by one residue class modulo `2^n`.

The claim is trivial at depth zero.  Suppose the word `w` of length `n` is realized by the residue `r modulo 2^n`.  Its two lifts modulo `2^(n+1)` are

\[
r
\quad\text{and}\quad
r+2^n.
\]

They have the same first `n` parity bits.  Indeed, along those common first `n` branches the exact affine formula gives

\[
T^j(r+2^n)-T^j(r)
=
3^{s_j}2^{n-j}
\]

for `0<=j<=n`, where `s_j` is the number of odd branches among the first `j`.  For `j<n` the difference is even, so the parity bits agree.  At `j=n` the difference is the odd integer `3^(s_n)`, so the next parity bits are opposite.  Therefore exactly one lift realizes `w0` and exactly one realizes `w1`.

This proves the bijection.  Every residue class modulo `2^n` has infinitely many positive representatives.

Passing to the compatible residues of an infinite word gives one unique element of `Z_2`.

### 2. Supercritical words force growth if ordinary

Along a prescribed parity prefix,

\[
T^n(x)={3^{s_n}x+C_n\over2^n},
\qquad C_n\ge0.
\]

For a positive ordinary `x`,

\[
T^n(x)\ge x\,{3^{s_n}\over2^n}.
\]

If

\[
\liminf s_n/n>\log_3 2,
\]

then `3^(s_n)/2^n` tends to infinity exponentially.  Hence the orbit is unbounded.

### 3. Abundance of ghosts

There are continuum many binary words with limiting one-frequency `3/4`: start from `(1110)^infinity` and alter arbitrary bits on any subset of a fixed zero-density infinite set of positions.  The set of those subsets has cardinality continuum, while the alterations preserve limiting frequency `3/4`.

The set of ordinary integers is countable and each integer has only one parity word.  Therefore continuum many supercritical words have nonordinary `2`-adic initial values.

### 4. Explicit periodic ghost

For the block `1110`, direct symbolic iteration gives

\[
T^4(x)={27x+19\over16}.
\]

The shifted point `T^4(x)` has the same infinite periodic parity word as `x`; uniqueness of the infinite-word realization therefore gives `T^4(x)=x`.  Hence

\[
x={27x+19\over16},
\]

so

\[
x=-{19\over11}.
\]

The denominator `11` is odd, so this value lies in `Z_2`; it is not an ordinary integer.  Directly,

\[
-{19\over11}
\longmapsto
-{23\over11}
\longmapsto
-{29\over11}
\longmapsto
-{38\over11}
\longmapsto
-{19\over11},
\]

whose parities are `1,1,1,0`.  The block multiplier is `27/16>1`, and the one-frequency is `3/4>log_3 2`.

By the finite parity bijection, every finite prefix of this exact infinite word is realized by infinitely many positive integers.  By uniqueness of the inverse-limit realization, no positive ordinary integer realizes the whole word. ∎

## Dependency audit

The finite parity bijection and the growth estimate are proved in this file.  No literature theorem or unmerged repository claim is required.

## Gap audit

- The explicit `2`-adic orbit is not a positive orbit and is not a counterexample.
- Finite representatives of longer prefixes are different integers; they do not form one fixed seed.
- The positive drift calculation is conditional on ordinary realization.
- The cardinality argument proves abundance of ghosts, not absence of all ordinary supercritical words.
- An adaptive seed-first machine may still succeed; this theorem only proves that compatibility and drift alone do not supply extraction.

## Adversarial tests

1. The block map can be checked step by step:
   `(3x+1)/2`, `(9x+5)/4`, `(27x+19)/8`, `(27x+19)/16`.
2. Substitution of `-19/11` returns the same value.
3. Its four numerators have parity odd, odd, odd, even.
4. The similar word `(110)^infinity` has the negative integer realization `-5`; this confirms that periodicity alone does not decide ordinary versus nonordinary status.
5. The all-one word has realization `-1`, again showing that supercritical symbolic data can land on the wrong signed boundary face.

## Remaining uncertainty

None in the theorem.  Its strategic application is a methodological classification: it does not itself decide any seed-first current machine.

## Suggested next attack

Require a candidate architecture to prove boundedness of its least ordinary roots or eventual zero pulled-back digits.  Do not treat the construction of another exact high-drift inverse-limit word as progress toward a positive seed.
