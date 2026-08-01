# Independent review of T-6708

**Reviewing agent:** `gpt56-positive-review-01` (`GPT-5.6 Pro`)  
**Issue:** #75  
**Source branch:** `agent/gpt56-positive-01/75-positive-coefficient-gate`  
**Source file:** `research/positive-coefficient-gate/T-6708-supercritical-implies-unbounded.md`  
**Source blob:** `894b09d737213648a6ee6c10ad8d5313d46dd45b`  
**Review date:** 2026-07-29  
**Verdict:** **PASSED**  
**Status action:** none; promotion belongs to the integrator and is not performed automatically by this review

## 1. Claim restated independently

For the shortcut Collatz map

\[
T(x)=\begin{cases}
x/2,&x\equiv0\pmod2,\\
(3x+1)/2,&x\equiv1\pmod2,
\end{cases}
\]

let

\[
v_i\equiv T^i(n)\pmod2,
\qquad
q_k=\sum_{i=0}^{k-1}v_i,
\qquad
C_k=\frac{3^{q_k}}{2^k}.
\]

`T-6708` asserts that for an ordinary positive integer `n`,

\[
C_k\ge1\quad\text{for every }k\ge1
\]

forces the orbit to be unbounded.

The review reconstructed the argument without using the authoring report or its stated confidence.

## 2. Exact recurrence reconstruction

Put

\[
x_i=T^i(n).
\]

The one-step recurrence is exactly

\[
x_{i+1}=\frac{3^{v_i}x_i+v_i}{2}.
\]

Induction on `k` gives

\[
\boxed{
 x_k
 =\frac{3^{q_k}}{2^k}n
 +\sum_{m=1}^k
   v_{m-1}\frac{3^{q_k-q_m}}{2^{k-m+1}}.
}
\]

Indeed, the constant inserted at step `m` is `v_{m-1}/2`; every later odd step multiplies it by `3`, and every later shortcut step divides it by `2`.

Therefore, if

\[
x_k=C_kn+E_k,
\]

then

\[
E_k
=C_k\sum_{m=1}^k
v_{m-1}\frac{2^{m-1}}{3^{q_m}}.
\]

Now set

\[
\alpha=\frac{\log2}{\log3},
\qquad
D_k=q_k-\alpha k.
\]

Since `2^r=3^{\alpha r}`,

\[
\frac{3^{q_k-q_m}}{2^{k-m+1}}
=\frac12\,3^{D_k-D_m},
\]

so the source identity

\[
\boxed{
E_k=\frac12\sum_{m=1}^k
v_{m-1}3^{D_k-D_m}
}
\]

is exact. There is no limit interchange, no `2`-adic-to-real passage, and no omitted denominator.

## 3. Hypothesis normalization

Because

\[
C_k=\frac{3^{q_k}}{2^k}=3^{D_k},
\]

one has

\[
C_k\ge1\quad\Longleftrightarrow\quad D_k\ge0.
\]

Thus the source proof may legitimately assume `D_k>=0` for every prefix.

## 4. Case reconstruction

### 4.1 Unbounded surplus

If

\[
\sup_kD_k=\infty,
\]

choose `k_j` with `D_{k_j}->infinity`. Positivity of `n` and of every summand in `E_k` gives

\[
T^{k_j}(n)
=3^{D_{k_j}}n+E_{k_j}
\ge3^{D_{k_j}}n
\longrightarrow\infty.
\]

This proves an unbounded subsequence. The source correctly does **not** claim convergence to infinity from this case alone.

### 4.2 Bounded surplus

If instead

\[
0\le D_k\le B
\]

for every `k`, then for every `m<=k`,

\[
D_k-D_m\ge-B.
\]

Consequently

\[
E_k
\ge\frac1{2\,3^B}\sum_{m=1}^k v_{m-1}
=\frac{q_k}{2\,3^B}.
\]

The same-prefix condition `D_k>=0` gives `q_k>=alpha k`, hence

\[
T^k(n)\ge E_k
\ge\frac{\alpha}{2\,3^B}k
\longrightarrow\infty.
\]

The alternatives `sup D_k=infinity` and `sup D_k<infinity` are exhaustive because `D_k>=0`. This proves `T-6708`.

## 5. Tail corollary

For a fixed time `r`, apply exactly the same proof to the positive ordinary integer `T^r(n)` and to parity counts measured from time `r`. Therefore, if every shifted coefficient prefix is at least one, that tail is unbounded.

The formal corollary in the source is correct:

\[
\text{for every }r\text{ in a bounded infinite orbit, some }k\ge1
\text{ has }
\frac{3^{q_{r,k}}}{2^k}<1.
\]

A wording caution is recommended. The introductory phrase “infinitely many subcritical coefficient prefixes after every sufficiently late starting time” could be read as asserting infinitely many subcritical lengths for each fixed `r`. What is proved is the precise and useful statement above: **at least one subcritical block begins at every starting time**, hence such blocks begin arbitrarily late.

## 6. Adversarial attempts

### 6.1 Long excursions with small endpoints

For each finite depth, an abstract prefix consisting of many odd symbols followed by the maximum legal number of even symbols can remain coefficient-supercritical and finish with a modest affine value. This does not refute the theorem: the minimizing finite words need not be nested prefixes of one infinite word, and `T-6708` claims only unboundedness along one fixed infinite ordinary orbit.

### 6.2 Large surplus followed by returns

The source proof allows `D_k` to make arbitrarily high excursions and later return to a bounded band. It extracts only a large subsequence in that case, exactly as warranted. No monotonicity is assumed.

### 6.3 Completion ghosts

The proof starts with an ordinary positive `n`. A prescribed parity word whose unique infinite realization is negative, rational nonintegral, or merely `2`-adic is outside the statement. Finite affine identities are used only after ordinary realization is assumed.

### 6.4 Cycles

A bounded positive cycle cannot satisfy the hypothesis from any one of its points at all shifted depths, because the tail theorem would make it unbounded. This is a consequence, not a hidden premise.

## 7. Dependency and circularity audit

The proof uses only:

1. the one-step shortcut recurrence;
2. finite induction;
3. positivity;
4. elementary real exponent algebra;
5. the bounded/unbounded dichotomy for a nonnegative real sequence.

It does not depend on `T-6707`, the verification floor, Angeltveit, Denjoy--Koksma, probabilistic drift, or an ordinary-extraction theorem. It therefore contains no circular use of Collatz and no imported theorem requiring source verification.

## 8. Verdict

**PASSED.** No unsupported inference was found. The exact affine formula, exponent normalization, case split, and tail corollary all reconstruct.

The review also found that the conclusion can be strengthened from unboundedness to full divergence to `+infinity`. That stronger result is written separately as proposed `T-6709`; it is not silently attributed to the source proof and requires its own review.
