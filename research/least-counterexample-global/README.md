# Least-counterexample global proof attack

**Agent:** `gpt56-positive-02` (`GPT-5.6 Pro`)  
**Issue:** #78  
**Namespace:** `65xx`  
**Status:** all theorem-level claims are **PROPOSED** pending independent reconstruction

**No proof of the Collatz conjecture is claimed.**

## Objective

This packet takes the newest positive-direction repository chain seriously and attacks only an exhaustive least-counterexample contradiction.

For

\[
T(n)=
\begin{cases}
n/2,&n\text{ even},\\
(3n+1)/2,&n\text{ odd},
\end{cases}
\]

write

\[
C_k={3^{q_k}\over2^k},
\qquad
D_k=q_k-{\log2\over\log3}k.
\]

Branch-qualified PR #76--#77 reduces a least positive counterexample to:

```text
Lane A:
  C_k >= 1 for every k,
  and the actual ordinary orbit tends to +infinity;

Lane B:
  a finite first crossing C_j < 1,
  with j >= 217,976,794,617.
```

A nontrivial positive cycle belongs to Lane B after rotation to its minimum.

## New result 1 — the correction product is polynomial

For an all-prefix-supercritical ordinary orbit,

\[
{x_k\over n}
=C_k
\prod_{x_i\text{ odd}}
\left(1+{1\over3x_i}\right).
\]

Such an orbit cannot repeat a value. After the first step, every odd source is coprime to six. Distinctness and the density of the prime-to-six integers give

\[
\boxed{
P_k
\le e^{7/9}k^{1/9}.}
\]

This is an ordinary-orbit theorem, not a bound on an arbitrary parity word.

## New result 2 — coefficient records must grow polynomially

Let

\[
M_k=\max_{m\le k}D_m.
\]

`T-6501` proves

\[
\boxed{
3^{M_k}
\ge
\left({\alpha\over2ne^{7/9}}\right)^{1/2}k^{4/9},
\qquad
\alpha={\log2\over\log3}.}
\]

At every coefficient-record time `r`,

\[
\boxed{
C_r\ge{\alpha\over2ne^{7/9}}r^{8/9}.}
\]

Therefore bounded coefficient surplus is impossible. The critical mechanical/Sturmian sublane is eliminated for positive ordinary Lane-A orbits.

## New result 3 — low surplus has density zero

The correction product also has the exact additive form

\[
P_k
=1+{1\over3n}
\sum_{\substack{i<k\\x_i\text{ odd}}}3^{-D_i}.
\]

For every fixed `H`, `T-6503` obtains

\[
\boxed{
\#\{i<k:D_i\le H\}=O_{n,H}(k^{1/9}).}
\]

Hence

\[
\boxed{D_k\to+\infty\text{ in natural density one}.}
\]

The remaining Lane-A object may return to low surplus only on a quantitatively sparse sequence of times.

## New result 4 — cofinal first-crossing harmonic window

For an acyclic no-descent crossing with `q` odd sources,

\[
\lambda=j\log2-q\log3>0
\]

satisfies

\[
\lambda
\le
\min\left\{
{q\over3n},
{1\over3n}+{1\over6}\log\left(1+{2(q-1)\over n}\right),
{7\over9}+{1\over9}\log q
\right\}.
\]

This strengthens the coefficient window when the crossing length greatly exceeds the starting value. It applies to a divergent least-counterexample crossing and to one period rotated at a positive-cycle minimum.

## New result 5 — every crossing word has a complete finite ordinary decision

For a first-crossing word `w`, let `r_w` be its least positive residue modulo `2^j` and `y_w=T^j(r_w)`. Every positive source in its cylinder is

\[
x=r_w+2^jt,
\]

and

\[
T^j(x)-x
=(y_w-r_w)-(2^j-3^q)t.
\]

Thus the complete no-descent list is exactly

\[
0\le t\le
\left\lfloor{y_w-r_w\over2^j-3^q}\right\rfloor.
\]

Lane B is not missing a local decision. It is missing a uniform theorem over the infinite family of first-crossing words.

## Latest-literature correction

The live paradoxical-sequence source is Rozier--Terracol, arXiv:2502.00948v5 / *Discrete Mathematics* 349 (2026), 115167.

The May 2026 Niu note arXiv:2605.13886 is withdrawn and is not used as an independent theorem. Angeltveit's new algorithm is a finite-verification advance. Chang's map-balance theorem explicitly leaves pointwise orbit-level one-bit mixing open.

See `LITERATURE_AUDIT.md`.

## Exact remaining proof target

A complete proof of Collatz from this route must close both:

```text
A. no positive ordinary orbit has all coefficient prefixes >= 1;

B. no positive first-crossing cylinder or positive cycle survives all time.
```

The new theorems eliminate the bounded-surplus and positive-frequency-return portions of A, and reduce each individual B word to an exact finite list. They do not eliminate the sparse-return, unbounded-record Lane A or the cofinal family of Lane-B words.

## Review order

1. `claims/L-6501-distinct-odd-source-product-bound.md`
2. `claims/T-6501-supercritical-coefficient-record-growth.md`
3. `claims/T-6503-low-surplus-density-zero.md`
4. `claims/T-6502-paradoxical-harmonic-window.md`
5. `claims/L-6502-first-crossing-cylinder-decision.md`
6. `claims/D-6501-least-counterexample-two-lane-framework.md`
7. `Q-6501-close-two-coefficient-lanes.md`
8. `LITERATURE_AUDIT.md`

## Scope boundary

This packet is a genuine positive-direction narrowing, not a completed proof. It introduces no new symbolic counterexample architecture and performs no bounded experiment. The remaining blockers are stated without disguising them as technical cleanup.
