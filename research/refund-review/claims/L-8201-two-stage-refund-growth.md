# L-8201 — Two-stage refund forces quotient growth

**Claim ID:** `L-8201`  
**Title:** Every coherent positive linear-height phase-34 path with a positive lift quotient eventually doubles that quotient at each stage  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-refund-01`  
**Created:** 2026-07-22  
**Dependencies:** PR #3 `L-0031`; the finite word-pair congruence of `LIT-KTHM-0050`  
**Scope:** physically valid linear-height 256-transition stage chains

## Setup

Use stage bases

\[
 B_n=B_0+4096n
\]

and exponents

\[
 A(B)=1792B+3657472,
 \qquad
 E(B)=2816B+5792512.
\]

For one current word and one next word, the exact zipper may be written

\[
 Y_n=y_n+Q_nk_n,
 \qquad
 Q_n=2^{E(B_n+4096)},
 \qquad 0\le y_n<Q_n,
\]

and

\[
 Y_{n+1}=c_n+P_nk_n,
 \qquad
 P_n=3^{A(B_n)},
 \qquad c_n\ge0.
\]

For the next transition also write

\[
 Y_{n+1}=y_{n+1}+Q_{n+1}k_{n+1},
 \qquad
 Q_{n+1}=2^{E(B_n+8192)},
 \qquad0\le y_{n+1}<Q_{n+1}.
\]

The word sequence may be arbitrary. The only hypothesis is that all displayed stages are one coherent ordinary trajectory.

## Exact threshold family

For `r>=1`, let

\[
 B_r=16\left(
 \left\lfloor\frac{611319808r-224459}{20480}\right\rfloor+1
 \right).
\]

Then

\[
 3^{A(B)}>2^{E(B+4096r)+1}
 \qquad(B\ge B_r,\ 16\mid B).
\]

In particular,

```text
B_1=477424,
B_2=955024.
```

### Proof

The exact integer inequality `3^53>2^84` gives

\[
 3^{A(B)}>2^{E(B+4096r)+1}
\]

as soon as

\[
 84A(B)>53(E(B+4096r)+1).
\]

Direct substitution gives

\[
84A(B)-53(E(B+4096r)+1)
 =1280B+224459-611319808r.
\]

The displayed formula for `B_r` is the smallest multiple of sixteen making this quantity positive.

## Growth theorem

If

\[
B_n\ge955024
\qquad\text{and}\qquad
k_n\ge1,
\]

then

\[
\boxed{k_{n+1}\ge2k_n.}
\]

More precisely,

\[
\boxed{k_{n+1}\ge
\left\lfloor\frac{P_nk_n}{Q_{n+1}}\right\rfloor.}
\]

### Proof

From the two presentations of `Y_(n+1)`,

\[
 Q_{n+1}k_{n+1}=c_n+P_nk_n-y_{n+1}.
\]

Since `c_n>=0` and `y_(n+1)<=Q_(n+1)-1`, the right side is at least

\[
P_nk_n-Q_{n+1}+1.
\]

The quotient is integral, so

\[
k_{n+1}\ge\left\lfloor P_nk_n/Q_{n+1}\right\rfloor.
\]

At `B_n>=B_2`, the threshold inequality gives `P_n>2Q_(n+1)`. Therefore the floor is at least `2k_n`.

## Consequence

Once a coherent path has `k_n>=1` after the threshold,

\[
 k_{n+j}\ge2^jk_n.
\]

The corresponding ordinary stage boundary satisfies

\[
W_n=R_n+2^{E(B_n)}Y_n\ge2^{E(B_n)}Y_n,
\]

so the boundary states are unbounded. A complete ordinary initialization and exact physical replay would therefore yield a divergent induced Collatz orbit without any additional drift theorem.

## Gap audit

- The theorem is conditional on one coherent ordinary path.
- It does not produce `Y_0`, select the words causally, or prove most-significant closure.
- Pairwise finite transitions alone do not satisfy the coherence hypothesis.
- The threshold concerns the linear schedule and does not contradict PR #33's doubling-schedule exclusion.

## Verification

`X-8201` checks the threshold formula through lookahead 32 and 50,000 independent exact quotient instances.
