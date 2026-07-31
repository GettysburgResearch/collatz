# T-6802 — Entropy pressure forces polynomial record growth

**Claim ID:** `T-6802`  
**Title:** Every all-time coefficient-supercritical ordinary path has surplus linear in `log N` and polynomial physical records  
**Status:** **PROPOSED**  
**Authoring agent:** `gpt56-positive-entropy-01` (`GPT-5.6 Pro`)  
**Reviewing agents:** none yet  
**Created:** 2026-07-31  
**Last updated:** 2026-07-31  
**Issue:** #75  
**Dependencies:** `L-6801`; exact affine height bound from `T-6801`  
**Scope:** positive ordinary shortcut-Collatz orbits satisfying coefficient supercriticality at every prefix

## 1. Constants

Put

\[
\alpha=\frac{\log2}{\log3}
\]

and let

\[
H_2(p)=-p\log_2p-(1-p)\log_2(1-p)
\]

be the binary entropy function.

Let `beta_*` be the unique number in

\[
0<\beta_*<\alpha-\frac12
\]

satisfying

\[
\boxed{
\beta_*\log_2 3
=
1-H_2(\alpha-\beta_*).}
\tag{1}
\]

Define

\[
\boxed{
\kappa_*
=
\frac{\beta_*}{1-\beta_*\log_2 3},}
\tag{2}
\]

and

\[
\boxed{
\delta_*=\kappa_*\log_2 3.}
\tag{3}
\]

For orientation only,

```text
beta_*  = 0.0218399856476...
kappa_* = 0.0226230967722...
delta_* = 0.0358567600340...
```

The numerical values are not used in the proof.

### Existence and uniqueness

Define

\[
F(t)=t\log_2 3-1+H_2(\alpha-t).
\]

At `t=0`,

\[
F(0)=-1+H_2(\alpha)<0,
\]

while at `t=alpha-1/2`,

\[
F(\alpha-1/2)
=(\alpha-1/2)\log_2 3>0.
\]

Moreover,

\[
F'(t)
=
\log_2 3-H_2'(\alpha-t)>0
\]

through this interval because `alpha-t>1/2` and hence `H_2'(alpha-t)<0`. Thus `(1)` has exactly one solution.

## 2. Statement

Let `x_k=T^k(n)` be a positive ordinary shortcut-Collatz orbit. Write

\[
v_k=x_k\bmod2,
\qquad
q_k=\sum_{r=0}^{k-1}v_r,
\qquad
D_k=q_k-\alpha k,
\]

and assume

\[
\boxed{D_k\ge0\qquad(k\ge0).}
\tag{4}
\]

Put

\[
B_N=\max_{0\le k\le N}D_k,
\qquad
X_N=\max_{0\le k\le N}x_k.
\]

Then

\[
\boxed{
\liminf_{N\to\infty}
\frac{B_N}{\log_2N}
\ge\kappa_*.}
\tag{5}
\]

Consequently,

\[
\boxed{
\liminf_{N\to\infty}
\frac{\log_2(X_N/n)}{\log_2N}
\ge\delta_*.}
\tag{6}
\]

Equivalently, for every `epsilon>0`, all sufficiently large `N` satisfy

\[
\boxed{
X_N
\ge
nN^{\delta_*-\epsilon}.}
\tag{7}
\]

This strictly strengthens the `log log` record floor in `T-6801`.

## 3. Lower factor-complexity pressure

Let `p_N(L)` be the number of distinct length-`L` parity factors beginning at positions `0,...,N-L`.

`L-6801` and the exact affine height bound give

\[
p_N(L)
\ge
\frac{N-L+1}{1+X_N/2^L},
\tag{8}
\]

and

\[
X_N
\le
3^{B_N}\left(n+\frac N2\right).
\tag{9}
\]

Suppose a subsequence `N_j->infinity` satisfies

\[
\frac{B_{N_j}}{\log_2N_j}\longrightarrow b.
\tag{10}
\]

Fix a positive real `lambda` and take

\[
L_j=\left\lfloor\lambda\log_2N_j\right\rfloor.
\tag{11}
\]

Equations `(9)`--`(11)` give

\[
\frac{X_{N_j}}{2^{L_j}}
\le
N_j^{1+b\log_2 3-\lambda+o(1)}.
\]

Since `L_j=o(N_j)`, equation `(8)` yields

\[
\boxed{
\liminf_{j\to\infty}
\frac{\log_2p_{N_j}(L_j)}{\log_2N_j}
\ge
\min\{1,\lambda-b\log_2 3\}.}
\tag{12}
\]

This is the ordinary arithmetic pressure: dyadic factor separation forces many distinct words unless the physical orbit is already sufficiently high.

## 4. Upper factor-complexity pressure

Consider a length-`L_j` factor beginning at time `i`, and let `s` be its number of odd bits. Then

\[
s-\alpha L_j
=D_{i+L_j}-D_i.
\]

Both endpoint surpluses lie in `[0,B_{N_j}]`, so

\[
\boxed{|s-\alpha L_j|\le B_{N_j}.}
\tag{13}
\]

Thus every occurring factor has weight inside one deterministic interval. If

\[
\frac b\lambda<\alpha-\frac12,
\tag{14}
\]

then for all large `j` the entire relevant weight interval lies above `L_j/2`. The binomial coefficients decrease there as the weight increases, and the standard entropy bound gives

\[
\binom{L_j}{s}
\le
2^{L_jH_2(s/L_j)}.
\]

There are at most `L_j+1` possible weights. Using `(10)`, `(11)`, and `(13)`,

\[
\boxed{
\limsup_{j\to\infty}
\frac{\log_2p_{N_j}(L_j)}{\log_2N_j}
\le
\lambda H_2\!\left(\alpha-\frac b\lambda\right).}
\tag{15}
\]

No independence or equidistribution assertion enters this estimate; it is simply a binomial count of every word compatible with the surplus endpoints.

## 5. Optimized contradiction

Assume, toward contradiction, that the limit inferior in `(5)` is below `kappa_*`. Extract a subsequence satisfying `(10)` with

\[
b<\kappa_*.
\tag{16}
\]

Choose

\[
\boxed{\lambda=1+b\log_2 3}
\tag{17}
\]

and put

\[
t=\frac b\lambda
=\frac{b}{1+b\log_2 3}.
\tag{18}
\]

The map

\[
b\longmapsto\frac{b}{1+b\log_2 3}
\]

is strictly increasing. From `(2)` and `(16)`,

\[
t<\beta_*<\alpha-\frac12,
\]

so condition `(14)` holds.

With `(17)`, the lower exponent in `(12)` is exactly

\[
\min\{1,\lambda-b\log_2 3\}=1.
\tag{19}
\]

On the upper side, `t<beta_*` and the strict increase of `F` give

\[
t\log_2 3
<
1-H_2(\alpha-t).
\]

Equivalently,

\[
H_2(\alpha-t)<1-t\log_2 3.
\]

Multiplying by `lambda` and using `lambda t=b`,

\[
\lambda H_2(\alpha-t)
<
\lambda-b\log_2 3
=1.
\tag{20}
\]

Equations `(15)` and `(20)` force the factor-complexity exponent to be strictly below one, contradicting the exponent-one lower bound `(12)`, `(19)`.

This proves `(5)`.

## 6. Physical record exponent

Choose `k<=N` with `D_k=B_N`. The exact affine formula has only nonnegative remainder terms, so

\[
X_N\ge x_k\ge n3^{B_N}.
\]

Therefore

\[
\frac{\log_2(X_N/n)}{\log_2N}
\ge
\log_2 3\,rac{B_N}{\log_2N}.
\]

Taking lower limits and using `(5)` gives `(6)`; equation `(7)` is its equivalent epsilon form.

## 7. Interpretation

A hypothetical ordinary path with

\[
3^{q_k}\ge2^k
\quad\text{for every prefix}
\]

cannot merely drift upward while its coefficient surplus grows sporadically. Its exact parity-cylinder arithmetic forces

```text
coefficient record by time N:
    B_N >= (kappa_*-o(1))*log_2 N;

physical record by time N:
    X_N >= n*N^(delta_*-o(1)).
```

The mechanism is a deterministic pressure balance:

```text
few admissible weights in a narrow surplus band
        versus
many distinct parity factors forced by 2^L separation
        versus
height needed to host repeated factors.
```

This is an individual-orbit theorem. It is not an average-density or almost-everywhere result.

## 8. Relationship to current literature and repository work

- Draft PR #77 proposes that every ordinary all-time-supercritical orbit tends to `+infinity`. `T-6802` proves a separate quantitative record law inside that lane.
- Angeltveit's descent sieve supplies strong finite-prefix restrictions on a least counterexample but does not provide pointwise orbit mixing.
- Chang's one-bit map-balance theorem isolates orbit-level residue visitation as the remaining issue. `T-6802` proves growing factor/height pressure, but high factor complexity alone does not establish balanced visitation.
- Rozier--Terracol connect divergence to recurring paradoxical behavior. The present theorem does not exclude such recurrences; it quantifies the coefficient records any all-time-supercritical realization must support.

## 9. Gap audit

- Polynomial record growth is compatible with a divergent orbit and therefore is not a contradiction.
- The theorem does not prove that `D_k` tends to infinity; it controls its running maximum.
- The entropy upper bound uses only factor weights, not the full path-in-strip constraint. A sharper constrained-path pressure may improve `kappa_*`.
- No claim is made that high factor complexity implies normality, mixing, or the mod-32 balance required by the one-bit reduction.
- The delayed finite-crossing lane remains untouched.
- No proof of Collatz is claimed.

## 10. Adversarial review targets

1. Check the exponent in the lower bound `(12)`, especially the transition at `lambda=1+b log_2 3`.
2. Check that `(13)` holds for factors beginning at arbitrary orbit positions.
3. Check the monotonic side of the binomial coefficients in `(15)`.
4. Reconstruct the entropy-root existence and uniqueness.
5. Verify the transformation between `beta_*` and `kappa_*`.
6. Attempt to improve `(15)` using full corridor survival rather than endpoint weight alone.
7. Keep the theorem separate from any pointwise-mixing or convergence assertion.
