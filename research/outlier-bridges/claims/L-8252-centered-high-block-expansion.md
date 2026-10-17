# L-8252 — Centered high-block quotient has positive toll and pointwise expansion

**Claim ID:** `L-8252`  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-outlier-01`  
**Reviewing agents:** none yet  
**Created:** 2026-07-23  
**Last updated:** 2026-07-23  
**Issue:** #52  
**Dependencies:** `L-8251`; branch-qualified PR #51 `T-8003` for the physical divergence implication  
**Scope:** the common \(D_9\)-residue class of the nine-B synchronized map  
**Related counterexample candidates:** none

## Statement

Retain

\[
D_9=16^9-9^9,
\qquad
\omega=37\,933\,813\,917
\tag{1}
\]

from `L-8251`, and define the exact Bezout quotients

\[
\boxed{
a=\frac{9^9\omega+1}{D_9}=215\,072\,362,}
\tag{2}
\]

\[
\boxed{
b=\frac{16^9\omega+1}{D_9}=38\,148\,886\,279.}
\tag{3}
\]

They satisfy

\[
b-a=\omega.
\tag{4}
\]

Write every synchronized boundary in the common invariant class as

\[
\boxed{
W=\omega+D_9X.}
\tag{5}
\]

For a proposed next high run `s>=0`, define

\[
\boxed{
T_s=9^s a-8^s b,}
\tag{6}
\]

\[
h_s=3s+36,
\qquad
M_s=9^{s+9}.
\tag{7}
\]

Then the raw boundary branch of `L-8251` is defined exactly when

\[
\boxed{
2^{h_s}\mid M_sX+T_s.}
\tag{8}
\]

When defined, the next centered quotient is

\[
\boxed{
X'=\frac{M_sX+T_s}{2^{h_s}}.}
\tag{9}
\]

For every `s>=44`,

\[
\boxed{
T_s>0,
\qquad
M_s>2^{h_s}.}
\tag{10}
\]

Consequently every defined high branch on `X>=0` satisfies

\[
\boxed{X'>X.}
\tag{11}
\]

Thus the grouped positive-counterexample problem becomes a one-place changing-cylinder map with a strictly positive toll and pointwise expansion. All fixed prime-to-`6` congruences, the current run's automatically refunded power of `3`, the nine-run resource total, and physical growth are already carried by the synchronized coordinate.

More explicitly, define the unique branch residue

\[
\boxed{
\xi_s=
[-T_sM_s^{-1}]_{2^{h_s}}.}
\tag{12}
\]

Then

\[
X=\xi_s+2^{h_s}k
\tag{13}
\]

if and only if branch `s` is defined, and its exact quotient output is

\[
\boxed{
X'=c_s+M_sk,}
\qquad
c_s=\frac{M_s\xi_s+T_s}{2^{h_s}}.
\tag{14}
\]

For two prospective consecutive high runs `s,t`, let

\[
\boxed{
\rho_{s,t}
=
[(\xi_t-c_s)M_s^{-1}]_{2^{h_t}},}
\tag{15}
\]

\[
\boxed{
\sigma_{s,t}
=
\frac{c_s+M_s\rho_{s,t}-\xi_t}{2^{h_t}}.}
\tag{16}
\]

Then continuation from `s` to `t` is exactly

\[
\boxed{
k=\rho_{s,t}+2^{h_t}\ell,
\qquad
k'=\sigma_{s,t}+M_s\ell.}
\tag{17}
\]

Equation `(17)` is the complete ordinary top-boundary law. There is no hidden directive and no remaining odd modulus.

## Motivation

The run-core program previously had several simultaneously moving pieces:

```text
divisibility by seven;
current powers of three;
next powers of two;
nine-run growth accounting;
an ordinary top quotient.
```

`L-8251` compresses a high run plus eight zero runs and discovers the maximal common odd boundary residue. Centering at that residue causes a second cancellation: at exactly the resource threshold `s=44`, both the multiplicative coefficient and the additive toll change to the favorable side.

The result is not merely a reformulation. A defined high branch can no longer lose growth through a negative affine correction. The only remaining reason a candidate stops is failure of the next dyadic cylinder.

## Proof

### 1. Centered branch equation

Substitute `(5)` into the raw branch equation

\[
2^{3s+36}W'
=
9^{s+9}W+9^s-2^{3s}.
\tag{18}
\]

By the invariant, write \(W'=\omega+D_9X'\). After moving the terms involving `omega` and using `(2)--(3)`,

\[
\begin{aligned}
D_9\,2^{3s+36}X'
&=
D_9\,9^{s+9}X\\
&\quad+
9^s(1+9^9\omega)
-
2^{3s}(1+16^9\omega)\\
&=
D_9\left(9^{s+9}X+9^sa-8^sb\right).
\end{aligned}
\]

Canceling \(D_9\) proves `(6)--(9)`.

Because \(M_s\) is odd, it is invertible modulo \(2^{h_s}\). Therefore `(8)` is equivalent to the single residue `(12)`, and substitution gives `(13)--(14)`.

### 2. Exact threshold for the multiplicative term

At `s=44`,

\[
M_{44}=9^{53}>2^{168}=2^{h_{44}}.
\tag{19}
\]

This is the exact integer inequality already used by PR #51 `T-8003`. Increasing `s` by one multiplies the left side by `9` and the right side by `8`. Hence

\[
M_s>2^{h_s}
\qquad(s\ge44).
\tag{20}
\]

The inequality fails at `s=43`.

### 3. Exact threshold for the toll

Direct exact arithmetic gives

\[
T_{43}
=
-2\,788\,172\,562\,281\,392\,386\,412\,760\,966\,019\,781\,661\,287\,651\,427\,750
<0,
\tag{21}
\]

while

\[
T_{44}
=
869\,233\,576\,299\,134\,175\,527\,700\,066\,803\,552\,549\,855\,475\,174\,698
>0.
\tag{22}
\]

Moreover,

\[
T_s>0
\quad\Longleftrightarrow\quad
\left(\frac98\right)^s>\frac ba.
\tag{23}
\]

The left side increases strictly with `s`, so `(22)` proves \(T_s>0\) for every \(s\ge44\).

### 4. Pointwise growth

For a defined branch and `X>=0`,

\[
2^{h_s}(X'-X)
=
(M_s-2^{h_s})X+T_s.
\tag{24}
\]

Both terms on the right are nonnegative for `s>=44`, and \(T_s>0\). Thus \(X'>X\), proving `(11)`.

### 5. Two-branch quotient law

From `(13)--(14)`, continuation with next label `t` is the congruence

\[
c_s+M_sk\equiv\xi_t\pmod {2^{h_t}}.
\tag{25}
\]

The odd multiplier \(M_s\) is invertible, giving `(15)`. Write

\[
k=\rho_{s,t}+2^{h_t}\ell
\]

and substitute in `(14)`. The definition `(16)` then gives

\[
X'
=
\xi_t+2^{h_t}(\sigma_{s,t}+M_s\ell),
\]

which is exactly `(17)`.

## Counterexample criterion

An unconditional positive result is now the following finite object.

Find an explicit integer

\[
X_0\ge0
\tag{26}
\]

and let

\[
W_0=\omega+D_9X_0.
\tag{27}
\]

Supply an initial run `r_0>=44` with

\[
9^{r_0}\mid1+16^9W_0,
\tag{28}
\]

and prove that the deterministic centered map `(9)` is defined forever with every emitted label `s_j>=44`.

Then:

1. every physical `A^{r_j}B^9A^{r_{j+1}}` block replays exactly by `L-8251`;
2. every nine-run block has total at least `44`;
3. the physical Collatz section grows by PR #51 `T-8003`;
4. the centered ordinary quotient grows strictly at every step by `(11)`.

The corresponding initial positive integer is explicitly

\[
v_0=\frac{1+16^9W_0}{7\,9^{r_0}},
\qquad
z_0=7\,2^{3r_0}v_0,
\qquad
n_0=6z_0-5.
\tag{29}
\]

No separate limiting, positivity, or growth argument remains.

## Refund cone

Equation `(17)` also gives a simple sufficient top-capacity condition. If

\[
s\ge t\ge44,
\tag{30}
\]

then

\[
M_s=9^{s+9}
\ge9^{t+9}
>2^{3t+36}
=2^{h_t}.
\tag{31}
\]

Thus a nonincreasing high-run transition refunds more binary magnitude than the next cylinder consumes. An infinite nonincreasing sequence of integer labels is eventually constant, so `(31)` is not itself a construction; it is an exact local capacity certificate for adaptive nonlinear schedules.

## Dependency audit

1. `L-8251` supplies the raw synchronized map and invariant residue.
2. PR #51 `T-8003` is used only for the final physical divergence implication.
3. All centered algebra, thresholds, residues, and quotient laws are proved here.
4. No external theorem is used.

## Gap audit

This result does **not** prove that any `X_0` has an infinite legal orbit.

In particular:

- the branch residues \(\xi_s\) are extremely thin dyadic cylinders;
- positive toll and pointwise expansion do not imply future divisibility;
- a compatible infinite branch word may select only a nonordinary `2`-adic point;
- eventually affine and periodic schedules remain completion ghosts or negative objects;
- the absence of zero-carry pairs in `X-8251` is bounded evidence, not a theorem;
- no candidate `K-####` is proposed.

The exact remaining statement is:

> Find one nonnegative ordinary integer whose deterministic orbit stays in the union of the high branch cylinders `(12)` forever.

## Adversarial tests

`X-8251` checks two independent implementations of:

- `(8)--(17)` for runs through `96`;
- 1,649 raw/centered branch agreements;
- 901 pointwise high-growth instances;
- 5,110 quotient-pair identities;
- 650 exact physical high-block replays;
- and the absence of an exact zero-carry pair for `44<=s,t<=80`.

The finite zero-carry result is not extrapolated.

## Suggested next attack

The new state is small enough for a focused boundary-memory search:

```text
current high label s;
ordinary centered quotient X;
one dyadic branch residue xi_s;
top lift k;
next-label residue rho_(s,t).
```

Search first on a bounded nonlinear alphabet such as `{64,65}`. Both labels satisfy the physical and centered growth gates, while their quotient multipliers exceed the opposing cylinder radices in the relevant local directions. A certificate must be an ordinary finite-word invariant, not a prescribed infinite branch sequence.
