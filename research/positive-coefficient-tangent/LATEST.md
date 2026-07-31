# Latest coefficient-envelope stack

**Updated:** 2026-07-31  
**Active draft PR:** #83  
**Namespace:** `69xx`  

No proof of Collatz is claimed.

## Complete claim map

```text
T-6901  finite no-descent coefficient threshold
T-6902  wave-minimum all-supercritical two-place tangent
T-6903  divergence / CST-violation dichotomy
R-6901  compactness does not extract an ordinary seed

L-6904  canonical first-crossing integer descent defect
L-6905  Box-1 / Box-2 envelope coupling
L-6906  upper mechanical word is the exact envelope
T-6905  explicit scalar envelope G_j

T-6904  logarithmic-bank zero-entropy exclusion
T-6906  bank--complexity repeated-factor ceiling

L-6907  exact one-wrap law for nonmechanical failures
L-6908  dual defect residue and unique late canonical candidate
L-6909  universal shifted full-denominator classification
R-6910  start/endpoint notation correction
T-6911  polynomial sparsity of all non-descending first crossings

T-6907  all-repetition single-pulse positive near-return exclusion
X-6901  exact post-Matveev and finite-case verifier
```

## Universal shifted equation

For **every** first-crossing word `w` of length `j`, weight `q`, and numerator `A_w`, let `x` be a positive realization and put

\[
y=T_w(x)=x+d.
\]

Then

\[
\boxed{
A_w=x(2^j-3^q)+d2^j
=y(2^j-3^q)+d3^q.}
\]

Therefore the requested equation

\[
\boxed{
A_w=n(2^j-3^q)+d3^q}
\]

is correct when `n` denotes the **endpoint** `y`; the starting value is `n-d`.

If `n` denotes the start, the correct coefficient of `d` is `2^j`.

No bank, entropy, periodicity, aperiodicity, pulse, or lateness assumption enters this identity.

For a non-descending realization,

\[
\boxed{
0\le d<\frac{A_w}{2^j}<\frac q3<\frac j3.}
\]

The displacement is the short full-denominator residue

\[
d\equiv A_w3^{-q}\pmod{2^j-3^q}.
\]

## Polynomial sparsity at arbitrary bank

Let `E_j` be the complete set of length-`j` first-crossing words having some positive non-descending realization.

With

\[
\lambda_j=j\log2-q\log3,
\]

`T-6911` proves the exact source-free count

\[
\boxed{
|E_j|
<
\frac{j}{3(1-e^{-\lambda_j})}
\le
\frac{2j}{3\lambda_j}.}
\]

Under a reviewed effective Baker/Matveev lower bound

\[
\lambda_j\ge c_0j^{-\mu},
\]

this becomes

\[
\boxed{|E_j|=O(j^{\mu+1}).}
\]

Hence the entire exceptional language has zero exponential growth and every member is describable from one polynomial-sized ordinary start using `O(log j)` bits.

This closes positive **family entropy** with no bank restriction. It does not by itself bound the internal subword complexity of one exceptional word.

## Exact envelope reduction

Let

\[
m_N^{\rm sup}
=
\min\{m>0:3^{q_k(m)}\ge2^k\text{ for all }k\le N\}.
\]

At each valid crossing length `j`, let `w_mech(j)` be the unique upper mechanical first-crossing word and put

\[
F_j=
\frac{A_{w_{\rm mech}(j)}}{2^j-3^{q(j)}}.
\]

Then

\[
\boxed{m_{j-1}^{\rm sup}>F_j}
\]

forces descent for every length-`j` crossing. Because `F_j` is unbounded along lower continued-fraction convergents, the same cofinal inequality also forces

\[
m_N^{\rm sup}\to\infty.
\]

A coarser explicit bound is

\[
F_j<
G_j=
\frac{q(j)2^{j-1}}{2^j-3^{q(j)}}.
\]

## Infinite regions already removed

Subject to the declared logarithmic-form input, an unbounded acyclic canonical-failure family cannot have

```text
logarithmic coefficient bank + uniformly zero internal factor entropy;
```

or, more generally,

```text
polynomial internal factor complexity degree s
+ bank o(j^(1/s)).
```

In addition, `T-6911` shows that the collection of all failures at a fixed length is only polynomially large, even when the bank is linear or larger.

## One-pulse closure

For a one-pulse lift of either known negative accelerated cycle, arbitrary repetition and rotation, a positive near-return gives

\[
D\mid g(2^\delta-1)-3d,
\qquad
0<D\le g(2^\delta-1).
\]

The Matveev/continued-fraction architecture excludes every repetition, subject to source reconstruction. The sole hit is the trivial cycle

```text
(1,2) -> (2,2),
start=endpoint=1,
d=0.
```

## Remaining frontier

The unrestricted target is now a polynomially sparse sequence of high-bank, potentially high internal-factor-complexity, genuinely nonperiodic words satisfying

\[
\boxed{
A_w
=n(2^j-3^q)+d3^q,
\qquad
0\le d<j/3,}
\]

where `n` is the endpoint and the start is `n-d`.

Equivalent scalar form:

```text
prove m_(j-1)^sup > F_j cofinally.
```

The remaining issue is sparsity versus emptiness: a residue-avoidance, return, or full-denominator theorem must eliminate the final thin exceptional sequence.