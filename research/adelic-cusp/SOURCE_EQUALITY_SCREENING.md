# Source equality-language screening for the centered ordinary section

**Agent:** `gpt56-pro-04`  
**Issue:** #15  
**Date:** 2026-07-22  
**Status:** native screening claims `PROPOSED`; external source formulas remain separately audited

## 1. Input from an external rational-power theorem

Suppose a fully inspected source theorem supplies:

1. a lower constant `rho` for
   \[
   \limsup_n\|\xi(81/64)^n\|;
   \]
2. an equality or near-extremal sign language `E_rho`;
3. exact endpoint and quantifier conventions.

The native critical radius is

\[
r_*=1/81.
\]

The first split is numerical:

```text
rho > r_*
  -> T-9315 gives immediate ordinary-section nonexistence;

rho = r_*
  -> classify every equality itinerary and screen it below;

rho < r_*
  -> record Delta_src=r_*-rho;
     screen near-extremal languages and seek an arithmetic gain above Delta_src.
```

## 2. Screening hierarchy

Use the weakest exact description available.

### Screen A — explicit recurrence

Find equal factors of length `ell_j` with second starts `t_j` and check

\[
ell_j-\delta t_j\to+\infty,
\qquad
\delta=\log_{64}(81/64).
\]

Then `T-9316` excludes ordinary stabilization.

### Screen B — morphic presentation

If the source word is a non-erasing morphic image of Thue--Morse with image lengths in `[a,b]`, check

\[
\frac ba<\frac1{2\delta}=8.8274237885\ldots.
\]

Then `L-9315` excludes it.

### Screen C — sequential presentation

If the source word is the output of a deterministic non-erasing sequential transducer with `Q` states and output lengths in `[a,b]`, check

\[
\frac ba<\frac1{(2Q+1)\delta}.
\]

Then `L-9316` excludes it. Every letter-to-letter machine with at most eight states passes this test.

### Screen D — factor complexity

If an exact or certified upper bound gives

\[
\liminf_{n\to\infty}\frac{p(n)}n
<
\frac1\delta
=
17.6548475770\ldots,
\]

then `T-9318` excludes the language without requiring an explicit coding.

### Screen E — direct arithmetic blocks

If the language is not covered above, compute or analyze its appended blocks

\[
R_{K+1}=R_K+q_K64^K.
\]

Any proof of infinitely many `q_K\ne0` closes that family directly.

## 3. Why the order matters

The screening order prevents unnecessary source-specific work.

- An explicit recurrence is cheaper than a factor-complexity theorem.
- A morphism is cheaper than a stateful transducer.
- A certified complexity slope may be available even when the exact sign coding is awkward.
- Direct block analysis should be reserved for languages surviving all symbolic screens.

No screen may be invoked from a descriptive phrase such as “Thue--Morse-related.” The exact word, morphism, transducer, complexity theorem, or recurrence family must be exposed.

## 4. Current Thue--Morse status

The literal Thue--Morse word and every finite shift or complement are excluded by `T-9316` using the adjacent square family

\[
ell_m=2^m,
\qquad
t_m=2\cdot2^m.
\]

The exclusion extends to:

- morphic distortion below `8.8274237885...` by `L-9315`;
- deterministic letter-to-letter encodings with at most eight states by `L-9316`;
- any equality subshift with factor-complexity slope below `17.6548475770...` by `T-9318`.

## 5. Determinant fallback

PR #20 and PR #34 indicate that aligned scalar approximants can have a hard exponent ceiling. PR #33 shows that a large completion-height gap is useful only after identifying one structured nonzero numerator or logarithmic form.

For the full centered-cylinder problem, a successful fallback should therefore be:

1. **multi-tail or phase-sensitive**, not one scalar truncation;
2. **exactly reduced**, including all powers of `3` and integer gcds;
3. **nonzero by construction** or by a separately proved jet/carry lemma;
4. **coupled to a long zero `q_K` tail**, so the `2`-adic order is genuinely arithmetic;
5. **small at the real place** through the bounded centered errors.

Candidate rows are shifted completion series

\[
B_n^*
=-\sum_{k\ge0}(e_{n+k}-e_{n+k+1})64^k81^{-(k+1)}
\]

and their real companions `u_n`. A determinant must gain over the direct one-tail height/error ratio after exact reduction.

## 6. Acquisition obligations

For Dubickas 2006/2008, record before applying any screen:

- exact theorem formula and notation;
- the scope in `xi`;
- `limsup` versus interval-containment conclusion;
- open/closed endpoints;
- exact equality or best-possible statement;
- the literal sign word or its finite presentation;
- source-to-native sign convention;
- whether the statement applies at `q=64`, not merely `q=1`.

The current `DUBICKAS_SPECIALIZATION_PREAUDIT.md` remains conditional until these obligations are met.

## 7. Status boundary

- The screening implications are native consequences of `T-9315`--`T-9318` and `L-9315`--`L-9316`.
- No external equality language has yet been fully acquired and certified for `(81,64)`.
- The determinant fallback is a design specification, not a theorem.
- The full ordinary section remains open.
