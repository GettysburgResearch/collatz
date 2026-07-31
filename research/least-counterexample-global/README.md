# Least-counterexample global proof attack

**Agent:** `gpt56-positive-02` (`GPT-5.6 Pro`)  
**Issue:** #78  
**Namespace:** `65xx`  
**Status:** theorem-level claims are **PROPOSED** unless explicitly marked otherwise

**No proof of the Collatz conjecture is claimed.**

## Objective

This packet attacks only an exhaustive least-counterexample contradiction.

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

## Synchronized proof heads for this wave

```text
PR #77  3efcbfb2e38f02b04eb6bba35eb258ec552d655c
PR #81  5609d8b76f8b0b1e2b9a3b3e9e1122b67732e648
PR #83  674f36cb6f2bb620e6fab21da2838c7c52a5072d
```

PR #80 is the present branch. The newest PR #77 files `T-6710/L-6711` are copied into this branch: `SC*` is exactly universal finite coefficient stopping, and its missing fixed-source form is

\[
v_2(3^{q(w)}n+A_w)<|w|
\]

beyond a source-dependent threshold. PR #81 supplies the canonical source/end ray and the same exact `SC*` source-escape target. PR #83 primarily advances the finite first-crossing lane through the corrected shifted-denominator equation and polynomial family sparsity.

# I. Lane A — exact ordinary consequences

## 1. Polynomial correction product

For an all-prefix-supercritical ordinary orbit,

\[
{x_k\over n}
=C_k
\prod_{x_i\text{ odd}}
\left(1+{1\over3x_i}\right).
\]

The orbit cannot repeat. After the first step, every odd source is coprime to six. Distinctness gives

\[
\boxed{P_k\le e^{7/9}k^{1/9}.}
\]

This acts on the actual ordinary orbit values, not on a free symbolic word.

## 2. `8/9` logarithmic mean surplus

Distinct-state packing and the product bound give

\[
\boxed{
\sum_{k=1}^{K}D_k
\ge
{1\over\log3}
\left[
\log{(n+K)!\over n!n^K}
-{1\over9}\log(K!)-{7K\over9}
\right].}
\]

Hence

\[
\boxed{
{1\over K}\sum_{k=1}^{K}D_k
\ge {8\over9}\log_3K-O_n(1).}
\]

In particular

\[
\max_{k\le K}3^{D_k}
\ge {K^{8/9}\over n e^{5/3+o(1)}}.
\]

## 3. Fixed low-surplus bands have density zero

The correction product has the exact additive form

\[
P_k
=1+{1\over3n}
\sum_{\substack{i<k\\x_i\text{ odd}}}3^{-D_i}.
\]

For every fixed `H`,

\[
\boxed{
\#\{i<k:D_i\le H\}=O_{n,H}(k^{1/9}).}
\]

Therefore

\[
D_k\to+\infty
\quad\text{in natural density one}.
\]

## 4. Critical-density boundary and subexponential cusps

López--Stoll Theorem 1, source-qualified in `T-6506`, says that a rational `2`-adic integer with a divergent noncyclic Collatz orbit must satisfy

\[
\liminf q_k/k={\log2\over\log3}.
\]

Thus an ordinary Lane-A orbit must satisfy

\[
\boxed{\liminf D_k/k=0.}
\]

There is a subsequence `k_j` for which

\[
\boxed{\log T^{k_j}(n)=o(k_j).}
\]

So the remaining orbit has logarithmically growing mean bank and density-one bank escape, but also arbitrarily late subexponential physical cusp returns.

## 5. Canonical two-boundary collapse

At those cusp times, the exact parity-cylinder source/end representatives satisfy

\[
\boxed{r_{k_j}=n,\qquad s_{k_j}=T^{k_j}(n),}
\]

and

\[
\boxed{
{\log r_{k_j}\over k_j}\to0,
\qquad
{\log s_{k_j}\over q_{k_j}}\to0.}
\]

Lane A is therefore reduced to a simultaneous zero-rate `2`-adic source / `3`-adic endpoint problem.

## 6. Tail-minimum ladder

Every divergent positive orbit has tail minima

\[
h_0<h_1<h_2<\cdots
\]

with infinite ordinary stopping time and

\[
\boxed{h_{i+1}\le(3h_i+1)/2.}
\]

Their coefficient-stopping depths tend to infinity.

# II. Fixed-integer adelic attack

## 1. Exact affine point and apparent product gain — `L-6505`

At one actual cusp prefix write

\[
\boxed{A+n3^q=s2^k.}
\]

The affine numerator is prime to six. For

\[
X=(A,3^q,2^k),
\]

choose determinant-one systems of forms at `infinity,2,3` using

```text
X_0,
X_0+nX_1=s2^k,
X_0-sX_2=-n3^q.
```

The exact three-place product is

\[
\prod_{v,i}|L_{i,v}(X)|_v
=
{A\over2^k3^q}|s|_2|n|_3.
\]

All-prefix supercriticality gives

\[
A\le(q/3)3^q.
\]

At a zero-rate cusp this yields the normalized estimate

\[
\boxed{
\prod_{v,i}{|L_{i,v}(X)|_v\over\|X\|_v}
\le H(X)^{-4+o(1)}.}
\]

That appears to cross a three-variable Subspace threshold.

## 2. Exact saturation by the physical plane — `L-6505/R-6502`

The point lies identically in the slowly moving hyperplane

\[
\boxed{X_0+nX_1-sX_2=0,}
\]

whose coefficient height is `o(h(X))` at the cusp. This is precisely the degeneracy returned by a moving-target argument.

After quotienting that plane, use

\[
Y=(3^q,2^k).
\]

The coordinate product is exactly

\[
|Y_1Y_2|_\infty|Y_1Y_2|_2|Y_1Y_2|_3=1,
\]

so the normalized quotient product is exactly

\[
\boxed{H(Y)^{-2}.}
\]

There is no residual power saving. The one-place approximation

\[
\left|n+A/3^q\right|_2=2^{-k}|s|_2
\]

also has only height exponent `1+o(1)`, below a Roth/Ridout threshold.

Thus the standard product-formula attack is not missing a technical constant. It is missing a second independent form.

## 3. Multiplicative-rank escape — `T-6507`

Normalize the two positive pieces of the exact affine equation:

\[
U_j={A_j\over s_j2^{k_j}},
\qquad
V_j={n3^{q_j}\over s_j2^{k_j}},
\qquad
U_j+V_j=1.
\]

Along a cusp subsequence with increasing odd counts,

\[
V_j=P_{k_j}^{-1}
\]

strictly decreases. The pairs are distinct solutions of one fixed two-variable equation.

Let `r_J` be the rank of the subgroup of `(Q^*)^2` generated by the first `J` pairs. Beukers--Schlickewei Theorem 1.1 gives

\[
J\le2^{8(r_J+1)},
\]

hence

\[
\boxed{r_J\ge{\log_2J\over8}-1.}
\]

If `S_J` is the set of primes dividing

\[
6n\prod_{j\le J}A_js_j,
\]

then

\[
\boxed{|S_J|\ge{\log_2J\over16}-{1\over2}.}
\]

If `N_J` and `E_J` are the new numerator and endpoint prime sets, respectively, then more precisely

\[
\boxed{|N_J|+2|E_J|\ge{\log_2J\over8}-O_n(1).}
\]

Therefore no fixed finite-rank, fixed-prime-support, or fixed multiplicative-alphabet cusp tail exists.

This is a genuine all-depth arithmetic exclusion. It still does not force a positive raw endpoint-height rate because the affine numerators may pay all fresh multiplicative rank.

## 4. Bilateral canonical propagation — `L-6506`

For a cusp prefix of length `K`, fix `0<epsilon<alpha`. For every sufficiently large cut

\[
t_0\le t\le(\alpha-\varepsilon)K,
\]

the same internal state is simultaneously:

```text
the canonical endpoint of the prefix [0,t),
the canonical source of the suffix [t,K).
```

Explicitly,

\[
\boxed{x_t\le\min\{3^{q_t},2^{K-t}\}.}
\]

For

\[
B_t=\min\{3^{q_t},2^{K-t}\},
\]

distinctness of the same ordinary orbit gives the exact capacity inequality

\[
\boxed{
\#\{t:B_t\le Y\}\le\lfloor Y\rfloor-n+1.}
\]

A capacity overload at one subexponential scale would close Lane A. Current estimates leave the capacities exponentially large.

# III. Necessary firewalls

## `R-6501`: scalar profile is insufficient

The explicit word

\[
q_k=\left\lceil
\alpha k+{8\over9}\log_3\left({k+2\over2}\right)
\right\rceil
\]

has binary increments and satisfies all current scalar Lane-A conditions, including `D_k/k->0`. Every finite prefix has positive ordinary representatives and the word has one compatible `2`-adic realization.

Therefore scalar drift/density plus completion does not imply ordinary exclusion.

## `R-6502`: the phrase “Subspace Theorem” is also insufficient

The fixed-integer product gain is genuine, but the known physical affine plane consumes it exactly. After quotienting, the product is at equality. A proof must produce one more independent arithmetic input.

# IV. Exact remaining Lane-A inequality

Any one of the following closes Lane A.

## 1. Second-form product saving

Find an independent quotient form of coefficient height `o(k)` producing

\[
H(3^q,2^k)^{-2-\varepsilon}
\]

for one fixed `epsilon>0`.

## 2. Numerator-rank transfer

Prove that simultaneous zero canonical source/end rates force

\[
\operatorname{rank}
\langle(U_1,V_1),\ldots,(U_J,V_J)\rangle
=o(\log J).
\]

This contradicts `T-6507`.

## 3. Bilateral capacity overload

At one cusp prove, for some `Y=exp(o(K))`,

\[
\#\{t:\min(3^{q_t},2^{K-t})\le Y\}>Y-n+1.
\]

This contradicts `L-6506`.

No current source supplies any of these three inequalities.

# V. Lane B — finite first crossings

## 1. Every word has a complete finite ordinary decision

For a first-crossing word `w`, let `r_w` be its least positive residue and `y_w=T^j(r_w)`. Every source is

\[
x=r_w+2^jt,
\]

and no descent occurs exactly for

\[
0\le t\le
\left\lfloor{y_w-r_w\over2^j-3^q}\right\rfloor.
\]

## 2. Latest cross-branch state

PR #81 folds positive cycles into the first-crossing canonical-displacement target and proves complete upper-mechanical/no-wrap closure, leaving a thin square-root-rough complete-denominator language.

PR #83 proves the corrected universal shifted equations

\[
A=D\,r+2^jd=D\,s+3^qd,
\qquad
0\le d<q/3,
\]

and polynomial sparsity of the entire family of first-crossing failures, source-dependently at the logarithmic-form input.

High-bank, high-complexity, growing-support denominator cancellation remains.

# VI. Literature position

- Rozier--Terracol is the live paradoxical-sequence source; its global finiteness assertion remains conjectural.
- López--Stoll supplies the critical-density equality used in `T-6506`.
- Beukers--Schlickewei supplies the exact two-variable unit-equation bound used in `T-6507`.
- Ru--Vojta moving targets motivate `R-6502`, but no theorem is invoked across the explicit moving hyperplane degeneracy.
- Kramer diagnoses the `2`--`3`--infinity corner but proves no canonical-boundary lower bound.
- Chang proves map-level balance but leaves pointwise one-bit orbit mixing open.

See `LITERATURE_AUDIT.md`.

# VII. Exact remaining proof target

A complete proof from this route must close both:

```text
A. no positive ordinary orbit occupies the zero-rate,
   rank-escaping, bilaterally canonical Lane-A cusp;

B. no positive first-crossing cylinder or positive cycle survives all time.
```

No such proof is currently present.

## Review order

1. `claims/L-6505-adelic-affine-plane-saturation.md`
2. `claims/T-6507-cusp-multiplicative-rank-escape.md`
3. `claims/L-6506-bilateral-canonical-split.md`
4. `claims/R-6502-subspace-ridout-applicability-boundary.md`
5. `claims/R-6501-scalar-profile-does-not-imply-exclusion.md`
6. `claims/T-6506-critical-density-subexponential-cusp.md`
7. `claims/L-6504-two-boundary-cusp-subsequence.md`
8. `claims/L-6503-tail-minimum-syndetic-ladder.md`
9. `claims/T-6504-distinct-state-packing-mean-surplus.md`
10. `claims/T-6505-low-complexity-first-crossings-are-finite.md`
11. `Q-6501-close-two-coefficient-lanes.md`
12. `LITERATURE_AUDIT.md`
13. latest session report

## Scope boundary

This wave proves a sharp logarithmic rank/prime-place escape and exact bilateral fixed-integer constraints. It does not transfer fresh numerator rank to endpoint height and therefore does not exclude Lane A. No completion, product threshold, or source theorem is promoted beyond its proved scope.
