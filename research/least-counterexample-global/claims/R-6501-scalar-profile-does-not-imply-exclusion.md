# R-6501 — The four Lane-A scalar estimates do not imply ordinary exclusion

**Claim ID:** `R-6501`  
**Status:** `PROVED` as an elementary nonreduction statement  
**Authoring agent:** `gpt56-positive-02` (`GPT-5.6 Pro`)  
**Created:** 2026-07-31  
**Dependencies:** finite shortcut parity-cylinder bijection only  
**Scope:** logical sufficiency of the four scalar surplus estimates  
**Related candidates:** none

## 1. Statement

Put

\[
\alpha={\log2\over\log3},
\qquad
c={8\over9}.
\]

There is an explicit infinite binary word

\[
v_0v_1v_2\cdots
\]

whose prefix weights `q_k=sum_(i<k)v_i` satisfy, with

\[
D_k=q_k-\alpha k,
\]

all four conditions

\[
D_k\ge0\qquad(k\ge0),
\tag{1}
\]

\[
{1\over K}\sum_{k=1}^{K}D_k
\ge {8\over9}\log_3K-O(1),
\tag{2}
\]

\[
\max_{k\le K}3^{D_k}\gg K^{8/9},
\tag{3}
\]

and, for every fixed `H`,

\[
\#\{k<K:D_k\le H\}=O_H(1),
\tag{4}
\]

which is stronger than `O_H(K^(1/9))`.

Every finite prefix of this word is the exact parity prefix of infinitely many positive ordinary integers, and the complete word selects one unique `2`-adic Collatz state.

Therefore the package

```text
all finite parity cylinders are nonempty,
+ one compatible 2-adic path,
+ the four displayed scalar estimates
```

is logically consistent. It cannot, by itself, prove that the selected completion is not an ordinary positive integer.

The unresolved extra assertion is exactly ordinary extraction/nonextraction.

## 2. Explicit construction

For `k>=0`, define

\[
f(k)=\alpha k+c\log_3\left({k+2\over2}\right),
\tag{5}
\]

and

\[
\boxed{q_k=\lceil f(k)\rceil.}
\tag{6}
\]

Since `f(0)=0`, one has `q_0=0`.

Moreover,

\[
f(k+1)-f(k)
=
\alpha+c\log_3\left({k+3\over k+2}\right).
\]

This increment is positive and is largest at `k=0`. At that point,

\[
\alpha+c\log_3(3/2)
=
\alpha+c(1-\alpha)
=
{8\over9}+{\alpha\over9}<1.
\tag{7}
\]

Thus

\[
0<f(k+1)-f(k)<1
\]

for every `k`. Consequently

\[
\boxed{v_k=q_{k+1}-q_k\in\{0,1\}.}
\tag{8}
\]

So `(q_k)` is the prefix-count sequence of one genuine binary word.

## 3. Surplus bounds

From `(6)`,

\[
f(k)\le q_k<f(k)+1.
\]

Subtracting `alpha k` gives

\[
\boxed{
 c\log_3\left({k+2\over2}\right)
\le D_k<
 c\log_3\left({k+2\over2}\right)+1.}
\tag{9}
\]

This proves `(1)`.

### Mean surplus

Summing the lower bound in `(9)`,

\[
{1\over K}\sum_{k=1}^{K}D_k
\ge
{c\over K}\log_3
\left(
\prod_{k=1}^{K}{k+2\over2}
\right)
=
{c\over K}\log_3
\left({(K+2)!\over2^{K+1}}\right).
\tag{10}
\]

Stirling's elementary estimate gives

\[
{1\over K}\log_3((K+2)!)
=
\log_3K-O(1),
\]

so `(2)` follows with `c=8/9`.

### Record size

Taking `k=K` in `(9)`,

\[
3^{D_K}
\ge
\left({K+2\over2}\right)^{8/9},
\]

which proves `(3)`.

### Fixed low bands

If `D_k<=H`, then `(9)` gives

\[
{k+2\over2}\le3^{H/c}=3^{9H/8}.
\]

Hence

\[
\boxed{
k\le2\,3^{9H/8}-2.}
\tag{11}
\]

The number of such indices is bounded independently of `K`, proving `(4)`.

Finally, `(9)` also gives

\[
D_k/k\to0,
\]

so the word lies on the critical-density boundary required of an ordinary divergent rational `2`-adic orbit by the López--Stoll source theorem. Adding that source-qualified condition does not create a scalar contradiction either.

## 4. Finite compatibility and completion

For the shortcut Collatz map, every length-`K` parity word selects exactly one residue class modulo `2^K`. That class contains infinitely many positive ordinary representatives.

The residue classes selected by the nested prefixes of `(v_k)` are compatible, so they determine one unique point

\[
\xi\in\mathbf Z_2.
\]

Because `(1)` holds, every finite prefix is coefficient-supercritical. Thus this explicit word passes every finite symbolic and scalar test appearing in the four-condition package.

No assertion is made that `xi` is ordinary. Deciding whether it lies in `Z_(>0)` is precisely the missing boundary.

## 5. First invalid inference

The following implication is false as a matter of proof architecture:

```text
finite compatibility at every depth
+ compatible 2-adic point
+ D_k >= 0
+ logarithmic mean bank
+ polynomial coefficient records
+ sparse fixed-band returns
--------------------------------
therefore no positive ordinary realization.
```

The hypotheses describe a nonempty inverse-limit object. They do not control the Archimedean height of its least representatives.

A valid exclusion must use an additional ordinary-arithmetic statement, for example:

- escape of the least positive parity-cylinder representatives;
- a `2`--`3` canonical-boundary uncertainty theorem;
- pointwise orbit mixing tied to the same integer;
- a complete inverse-tree/minimality contradiction.

## 6. Why this is not a counterexample construction

The constructed object is an infinite parity directive and its `2`-adic completion. A positive ordinary realization is neither asserted nor inferred.

If the completion were proved to be a positive integer, it would indeed be an all-prefix-supercritical Collatz counterexample. This file does not cross that ordinary-extraction gate.

## 7. Consequence for the current request

The four displayed conditions can be strengthened substantially and still remain compatible with an exact infinite parity path. Therefore they cannot be the final contradiction.

The remaining Lane-A problem is not to amplify those estimates again. It is to prove that **no ordinary integer** realizes any path in this critical logarithmically banked boundary class.
