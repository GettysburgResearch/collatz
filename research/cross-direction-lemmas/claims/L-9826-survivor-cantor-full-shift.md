# L-9826 — Exact full-shift geometry of the survivor Cantor set

Claim ID: `L-9826`  
Title: The infinite `64 -> 81` survivor set is a dimension-`1/6` full shift and has no nontrivial eventually periodic ordinary point  
Status: `PROPOSED`  
Authoring agent: `gpt56-synthesis-01`  
Reviewing agents: none yet  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: none; the chart and coding algebra are proved below  
Scope: the induced partial chart `T(64q+e)=81q+e`, `e in {0,1}`, on `Z_2` and ordinary nonnegative integers  
Source-direction audit: reconstructs and metrically sharpens the coding in `PR16/D-9302`; complements `L-9812`, `L-9815`, and `R-9804`  
Related counterexample candidates: none

## Definitions

Let

\[
\Sigma=\{0,1\}^{\mathbb N}
\tag{1}
\]

with left shift `sigma`. For `epsilon=(epsilon_i)_(i>=0)`, define

\[
\boxed{
\Phi(\varepsilon)
=17\sum_{i\ge0}
\varepsilon_i64^i81^{-(i+1)}
\in\mathbb Z_2.
}
\tag{2}
\]

The series converges because its `i`-th term has 2-adic valuation `6i`.
Let

\[
\mathcal S=\Phi(\Sigma).
\tag{3}
\]

On a 2-adic integer with residue `e in {0,1}` modulo `64`, use the partial
chart

\[
T(x)=\frac{81x-17e}{64},
\qquad
T(64q+e)=81q+e.
\tag{4}
\]

Thus `S` is the set of 2-adic points on which every forward chart step is
defined. An **ordinary survivor** is a point of
(S\cap\mathbb Z_{ge0}); this is a claim about the induced chart, not by itself
a translation to a full Collatz counterexample.

Use the 2-adic metric

\[
d_2(x,y)=2^{-\nu_2(x-y)}.
\tag{5}
\]

## Statement

### 1. Exact coding and shift conjugacy

The map `Phi` is a bijection from `Sigma` onto `S`, and

\[
\boxed{T\circ\Phi=\Phi\circ\sigma.}
\tag{6}
\]

If two directive words first differ at position `k`, then

\[
\boxed{
\nu_2\bigl(\Phi(\varepsilon)-\Phi(\eta)\bigr)=6k,
\qquad
d_2\bigl(\Phi(\varepsilon),\Phi(\eta)\bigr)=2^{-6k}.
}
\tag{7}
\]

Hence `Phi` is an exact symbolic ultrametric isometry after assigning symbolic
scale `2^(-6k)` to a first disagreement at `k`.

At depth `n`, the `2^n` directive prefixes give exactly `2^n` distinct
surviving residue classes modulo

\[
64^n=2^{6n}.
\tag{8}
\]

Their canonical representatives are

\[
\boxed{
R_n(\varepsilon)
\equiv
17\sum_{i=0}^{n-1}
\varepsilon_i64^i81^{-(i+1)}
\pmod{64^n}.
}
\tag{9}
\]

### 2. Exact fractal geometry

The set `S` is compact, perfect, nowhere dense, and has normalized 2-adic Haar
measure zero. Its Hausdorff and upper/lower box dimensions are all

\[
\boxed{dim_H\mathcal S=dim_B\mathcal S=\frac16.}
\tag{10}
\]

If `mu` is the pushforward under `Phi` of the fair Bernoulli measure on
`Sigma`, then at every symbolic scale

\[
\boxed{
\mu\bigl(B(x,2^{-6n})\bigr)
=2^{-n}
=\bigl(2^{-6n}\bigr)^{1/6}
\qquad(x\in\mathcal S).
}
\tag{11}
\]

Thus `mu` is Ahlfors `1/6`-regular, with exact equality at the natural scales.
The restricted chart `(S,T)` has topological entropy `log 2`.

### 3. Exact periodic-point formula

Let `w=(e_0,...,e_(p-1))` and let `w^omega` be its infinite repetition. Put

\[
D_p
=\frac{81^p-64^p}{17}
=\sum_{i=0}^{p-1}64^i81^{p-1-i},
\tag{12}
\]

and

\[
N(w)=\sum_{i=0}^{p-1}e_i64^i81^{p-1-i}.
\tag{13}
\]

Then the same geometric series converges in both `R` and `Q_2`, and

\[
\boxed{
\Phi(w^\omega)=\frac{N(w)}{D_p},
\qquad
T^p\Phi(w^\omega)=\Phi(w^\omega).
}
\tag{14}
\]

All weights in (12) are positive, so

\[
0\le N(w)\le D_p.
\tag{15}
\]

Consequently the periodic point is an ordinary nonnegative integer if and
only if

\[
\boxed{
w=0^p\text{ and }\Phi=0,
\quad\text{or}\quad
w=1^p\text{ and }\Phi=1.
}
\tag{16}
\]

Thus the induced chart has no nontrivial ordinary periodic survivor.

### 4. Eventual-periodicity obstruction

If an ordinary survivor (A\in S\cap\mathbb Z_{ge0}) has an eventually periodic
directive word, then

\[
\boxed{A\in\{0,1\}.}
\tag{17}
\]

Hence every hypothetical nontrivial ordinary survivor has an aperiodic
directive word. Its one-sided factor complexity therefore satisfies

\[
\boxed{p_A(n)\ge n+1\qquad(n\ge1).}
\tag{18}
\]

This is a single-word complexity theorem only. By `L-9819`, it does not force
aligned correlation with the next finite survivor.

### 5. Exact real shadow and automatic divergence

Evaluate the same digit series in the real absolute value:

\[
x_\infty(\varepsilon)
=17\sum_{i\ge0}\varepsilon_i64^i81^{-(i+1)}
\in[0,1].
\tag{18a}
\]

If `A=Phi(epsilon)` is an ordinary survivor and
`A_j=T^j(A)`, then

\[
\boxed{
A_j
=\left(\frac{81}{64}\right)^j
\bigl(A-x_\infty(\varepsilon)\bigr)
+x_\infty(\sigma^j\varepsilon).
}
\tag{18b}
\]

Consequently every nontrivial ordinary survivor `A>=2` is automatically a
divergent induced-chart orbit, with the explicit lower bound

\[
\boxed{
A_j\ge
\left(\frac{81}{64}\right)^j(A-1)
\ge\left(\frac{81}{64}\right)^j.
}
\tag{18c}
\]

Thus the remaining difficulty is entirely the ordinary intersection and the
chart-class translation, not growth after such an intersection is found.

## Proof

### Coding and exact metric

Modulo `64`, the first term of (2) is

\[
17\varepsilon_0 81^{-1}\equiv\varepsilon_0\pmod{64},
\tag{19}
\]

because `81 congruent to 17 mod 64`. Hence the first chart directive is
`epsilon_0`. Direct calculation gives

\[
\begin{aligned}
T(\Phi(\varepsilon))
&=\frac{81\Phi(\varepsilon)-17\varepsilon_0}{64}\\
&=17\sum_{i\ge1}
\varepsilon_i64^{i-1}81^{-i}\\
&=\Phi(\sigma\varepsilon),
\end{aligned}
\tag{20}
\]

which proves the conjugacy and shows that every coded point survives forever.

If `epsilon` and `eta` first differ at `k`, factor their difference as

\[
\Phi(\varepsilon)-\Phi(\eta)
=17\,64^k81^{-(k+1)}
\left(
\varepsilon_k-\eta_k
+64Z
\right),
\tag{21}
\]

for some `Z in Z_2`. The parenthesis is odd, proving (7). This proves
injectivity. Conversely, any point surviving at every depth has one directive
prefix at each depth. Formula (20), iterated backward modulo `64^n`, gives
(9); completeness of `Z_2` makes those compatible residues converge to (2).
Thus `Phi` is onto `S`.

### Geometry

A length-`n` symbolic cylinder has diameter exactly `2^(-6n)` by (7), and the
`2^n` such cylinders partition `S`. They therefore give the upper Hausdorff
and box estimate

\[
2^n\bigl(2^{-6n}\bigr)^s
\longrightarrow0
\quad(s>1/6).
\tag{22}
\]

The fair Bernoulli measure assigns mass `2^(-n)` to each cylinder, proving
(11). The mass-distribution bound gives the reverse Hausdorff estimate, and
the exact covering count gives both box dimensions. This proves (10).

The level-`n` survivor union consists of `2^n` residue classes modulo
`2^(6n)`, so its Haar measure is

\[
2^n2^{-6n}=2^{-5n}\longrightarrow0.
\tag{23}
\]

Their nested intersection `S` has measure zero and hence empty interior. It is
compact by continuity of `Phi`, and perfect because every finite directive
prefix has two infinite extensions. This proves the remaining topological
claims. Entropy is preserved by the conjugacy with the full two-shift.

### Periodic and ordinary points

Summing (2) over repeated copies of `w` gives

\[
\begin{aligned}
\Phi(w^\omega)
&=17\sum_{i=0}^{p-1}
e_i64^i81^{-(i+1)}
\sum_{j\ge0}\left(\frac{64}{81}\right)^{pj}\\
&=\frac{17N(w)}{81^p-64^p}
=\frac{N(w)}{D_p}.
\end{aligned}
\tag{24}
\]

The ratio `64/81` has absolute value below one both really and 2-adically, so
the two sums equal the same rational. Equations (15)--(16) follow because an
integer in `[0,1]` is zero or one and equality at either endpoint forces every
binary digit of `w` to be the corresponding constant.

Finally, suppose the directive word of an ordinary survivor `A` becomes
periodic after `j` steps. Conjugacy gives

\[
A_j=T^j(A)=\Phi(\sigma^j\varepsilon).
\tag{25}
\]

The right side is the periodic rational (14), while the left side is an
ordinary nonnegative integer. Thus `A_j` is zero or one. The chart is
injective on its legal domain: equality

\[
81q+e=81q'+e',
\qquad e,e'\in\{0,1\},
\tag{26}
\]

forces `q=q'` and `e=e'`. Therefore the only legal backward orbit of zero is
zero and the only legal backward orbit of one is one, proving (17).
Morse--Hedlund applied to the resulting aperiodic one-sided word proves (18).

Finally, the real series (18a) obeys the same affine shift recurrence as (20):

\[
x_\infty(\sigma\varepsilon)
=\frac{81x_\infty(\varepsilon)-17\varepsilon_0}{64}.
\]

Subtract this from the ordinary chart recurrence for `A_j`. The difference is
multiplied by `81/64` at every step, so iteration gives (18b). Since both real
companions lie in `[0,1]`, inequality (18c) follows. QED

## Motivation

Finite survivor cylinders occur throughout the adelic, active-cylinder,
regular-language, and successor-gap directions. The exact carry recurrence in
`R-9804` shows how to read those cylinders; this lemma identifies their entire
inverse limit geometrically. One directive bit consumes six 2-adic bits, so
the survivor set is a thin but dynamically complete Cantor repeller.

The real/2-adic coincidence for periodic words is especially useful. It turns
periodic symbolic proposals into a bounded rational number before any large
divisibility search: integrality leaves only the two trivial fixed points.
Any credible ordinary counterexample in this chart must therefore use an
aperiodic directive word and satisfy the separate ordinary-section condition.

## Dependency audit

- The coding, metric, dimension, and periodic formula are proved directly.
- `PR16/D-9302` is source provenance, not an imported proof dependency.
- `R-9804/(14)` is the same finite cylinder formula, but (9) is independently
  recovered from the infinite series.
- Morse--Hedlund is used only for the standard aperiodic complexity bound.
- No empirical minimum-survivor record or unreviewed ordinary-room exclusion
  enters the proof.

## Gap audit

- Haar measure zero and dimension `1/6` do not imply that `S` has no ordinary
  nontrivial point; a countable set can meet a null Cantor set.
- Aperiodicity and complexity `n+1` do not supply the pairwise correlation
  needed by `L-9818`--`L-9819`.
- The chart is an induced subsystem. A nontrivial ordinary point would still
  require the independently checked chart-class translation to give a full
  Collatz counterexample.
- The theorem rules out eventually periodic directive words, not automatic,
  morphic, Sturmian, or other low-complexity aperiodic words.
- The real coordinate of a general nonperiodic code lies in `[0,1]`, but its
  2-adic value need not equal that real number. Equality was used only for the
  rational periodic geometric series.

## Adversarial tests

- The 2-adic scaling is `64^k`, so the exact valuation in (7) is `6k`, not
  `k`.
- Congruence (19) uses `17*81^(-1) congruent to 1 mod 64`; replacing it by
  the real ratio `17/81` without the modular inverse is invalid.
- Formula (14) has denominator `D_p=(81^p-64^p)/17`; the factor `17` cancels
  exactly. All-zero and all-one words test both endpoints.
- A rational number can have different real and 2-adic series expansions.
  Here both geometric sums converge to the same rational because the common
  ratio has absolute value below one at both places.
- An eventually periodic tail is evaluated at `A_j`, not silently at the
  initial `A`; injectivity is what propagates the trivial value backward.
- The ordinary-section conclusion uses nonnegative integers. Signed integer
  points are outside the stated chart-survivor scope.

## Remaining uncertainty

The exact Cantor dynamics is complete. The central unresolved question is the
ordinary intersection

\[
\mathcal S\cap\mathbb Z_{\ge2}.
\tag{27}
\]

Every point in it would have an aperiodic directive word and exponentially
growing forward chart orbit, but no result here constructs or excludes such a
point.

## Suggested next attack

Exploit the exact Ahlfors measure and full-shift coding to study arithmetic
transversality with the discrete ordinary section. A useful intermediate goal
is to rule out one broader low-complexity class—automatic, substitutive, or
bounded-discrepancy directive words—by comparing their real and 2-adic coding
values, without assuming that null measure alone forbids an integer point.
