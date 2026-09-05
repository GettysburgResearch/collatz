# Route 3 — arithmetic-progression certificates and unbounded spike repayment

**Status:** `T-ATR-301` through `T-ATR-303` are **PROPOSED pending independent review**. The all-parameter statements below have elementary proofs. The finite certificate collection does not cover every source. No terminating interpretation of the full mixed-radix rewrite system, global ranking function, or Collatz proof is claimed.

The purpose is to find a finite proof description that retains unbounded arithmetic information. The underlying ordinary map and integer rank are the same `R` and `P` as in [Route 1](ROUTE_1_TRANSFER.md). For the absorbing endpoint only, extend the formula to `P(1)=3`.

## 1. The rank is not globally monotone

The exact hard-state return

\[
R(13)=10,
\qquad P(13)=27,
\qquad P(10)=147
\tag{1}
\]

increases rank by `49/9`. Thus searching for a single-return proof `P(R(n))<P(n)` is already refuted. The successful certificate must sometimes group multiple returns and allow a temporary increase.

This does not invalidate Route 1: that theorem proves rank contraction when the **destination is nonresonant**, whereas 10 is resonant.

## 2. T-ATR-301: one exact rank drop certifies an infinite arithmetic progression

Let a nonempty legal shortcut parity word `w` have length `j`, odd count `q`, and affine constant `A`, and let a positive source `n_0 in H` realize it with endpoint `y_0 in H union {1}`. Suppose

\[
P(y_0)<P(n_0).
\]

Write

\[
h_0=\nu_3(2n_0+1),\quad h_1=\nu_3(2y_0+1),\quad
M=2^j3^{\max(h_0+1,h_1+1-q)}.
\tag{2}
\]

Then every ordinary integer

\[
\boxed{n=n_0+Mt,\qquad t\ge0}
\]

realizes the same word, has the same source and endpoint ternary valuations, and satisfies

\[
\boxed{
\frac{P(T_w(n))}{P(n)}
\le\frac{P(y_0)}{P(n_0)}<1.}
\tag{3}
\]

This is an infinite-family theorem. Finite substitutions are only checks of its implementation.

### Proof

Two inputs congruent modulo `2^j` follow the same length-`j` parity word. An elementary induction proves this: at each branch an even difference is divided by 2 and multiplied by either 1 or 3. Thus `M` preserves the word and

\[
T_w(n_0+Mt)=y_0+3^{q+\max(h_0+1,h_1+1-q)}t.
\]

The source change in `2n+1` is divisible by `3^(h_0+1)`, and the endpoint change in `2T_w(n)+1` is divisible by `3^(h_1+1)`. Their valuations therefore stay exactly fixed.

Now put `z=2n+1`. Both shortcut branches obey

\[
z'=(3^v z+1)/2,\qquad v\in\{0,1\}.
\]

Consequently

\[
2^j(2T_w(n)+1)=3^q(2n+1)+B_w,
\qquad B_w=2A+2^j-3^q>0.
\tag{4}
\]

Positivity follows by induction from the positive added 1 in every `z`-step. With the valuations fixed, the rank ratio is

\[
3^{h_0-h_1}
\left(\frac{3^q}{2^j}+\frac{B_w}{2^j(2n+1)}\right)^2.
\tag{5}
\]

It is decreasing in positive `n`. Evaluating at `n_0` proves (3). Endpoints remain positive; if a path hits 1 before its declared endpoint, that source already converges and may simply be killed earlier.

### A concrete tile

The word `10010` maps `13` to `4`, with `q=2,j=5,h_0=3,h_1=2`. Therefore

\[
\boxed{n=13+2592t\quad(t\ge0)}
\]

has exact five-step image `(9n+11)/32` and rank ratio at most `1/3`. Its first hard return increases rank; the second repays the increase.

The companion report contains 32 such upward-progression certificates, generated from distinct small sources whose first hard return does not decrease rank. Each row is checked by a separate implementation, and each infinite progression is justified by (2)-(5). Their union is **not** claimed to be exhaustive or disjoint.

## 3. T-ATR-302: one parametric certificate repays an unbounded rank spike

For every integer `h>=2`, let

\[
\boxed{w_h=10010(10)^{2h}.}
\tag{6}
\]

Consider **any positive ordinary source** `n` satisfying both:

1. `n` realizes the whole word `w_h`;
2. `nu_3(2n+1)=h` exactly.

There are infinitely many such sources for every `h`, by the CRT argument below. Then the first hard return has an unbounded-in-`h` increase,

\[
\boxed{
\frac{P(R(n))}{P(n)}>\frac{3^{h+1}}{16},}
\tag{7}
\]

but the complete word gives the uniform decrease

\[
\boxed{P(T_{w_h}(n))<\frac34P(n).}
\tag{8}
\]

The word length is `5+4h`; its arithmetic memory and duration are not uniformly bounded. This is not an eventually periodic all-time directive, and no infinite ordinary source is extracted from its finite cylinders.

### First spike and exact final endpoint

The initial `10` gives

\[
R(n)=(3n+1)/4.
\]

Since `n in H`, the endpoint has first ternary valuation 1, and its second carry is exactly `h`. Its rank ratio is

\[
\frac{3^{h+1}(n+1)^2}{4(2n+1)^2}>\frac{3^{h+1}}{16}.
\]

The next three bits `010` end at `(9n+11)/32`. Each subsequent legal `10` acts as `x -> (3x+1)/4`, with fixed point 1. Therefore the final endpoint is exactly

\[
m=1+(3/4)^{2h}\frac{9n-21}{32}.
\tag{9}
\]

Each displayed block ends at a hard state (or the absorbing 1). The first and second are the exact returns from Route 1. The endpoint of (9) has first ternary valuation exactly 1, since

\[
2m+1=
\frac{3\bigl(16^{h+1}+3^{2h}(3n-7)\bigr)}{16^{h+1}}
\]

has a numerator divisible by 3 but not 9. The expression is an ordinary integer because the word is assumed legal.

### Uniform rank repayment

From (9),

\[
2m+1<3+(9/16)^{h+1}n.
\]

Thus

\[
\frac{P(m)}{P(n)}<(a+b)^2,
\]

where

\[
a=3^{(h-1)/2}\frac{3}{2n+1},\qquad
b=3^{(h-1)/2}(9/16)^{h+1}\frac{n}{2n+1}.
\]

The source valuation gives `2n+1>=3^h`, so

\[
a^2\le3^{1-h}\le1/3.
\]

Also `n/(2n+1)<1/2`, and

\[
b^2<\frac{6561}{262144}(243/256)^{h-1}
\le\frac{6561}{262144}.
\]

Using `(a+b)^2<=2a^2+2b^2` and the exact integer comparisons,

\[
\frac{P(m)}{P(n)}
<\frac23+\frac{6561}{131072}<\frac34.
\]

This proves (8) for all `h>=2` and all eligible sources, with no numerical asymptotics or upper bound on `h`.

### Nonvacuity: ordinary sources at every height

Every finite parity word of length `L` selects exactly one residue modulo `2^L`. This can be proved bit by bit: appending the next source bit flips the next parity, because the current affine multiplier has odd numerator. Combine that dyadic residue for `w_h` with

\[
2n+1\equiv3^h\pmod{3^{h+1}}.
\]

The moduli `2^(5+4h)` and `3^(h+1)` are coprime. CRT gives one progression of positive ordinary sources, with the requested **exact** ternary valuation, for every `h`. It has infinitely many positive members.

The checker includes one CRT source at each `h=2,...,32`, but the preceding proof covers arbitrary height. For example, at `h=2`, a sampled source is `141997`, with endpoint `12637`; at `h=3`, a sampled source is `5155501`, with endpoint `258067`. These samples illustrate the theorem rather than establishing it.

### Stronger two-parameter family: initial numerical growth is allowed

The preceding family starts with a numerically descending `10`, even though its arithmetic rank spikes. It is a common-rank certificate improvement, not a newly discovered numerical-descent class. The same mechanism extends to genuine initial numerical growth as follows.

For **all** integers `a>=1,h>=2`, put

\[
b=2(h+a)+3,\qquad w_{a,h}=1^a0(10)^b.
\tag{10}
\]

For every legal ordinary source with `nu_3(2n+1)=h`, the word itself forces `nu_2(n+1)=a`. Its first hard return is

\[
x=\frac{3^a(n+1)/2^a-1}{2},\qquad
\frac{P(x)}{P(n)}>\frac{3^{h+a}}{4^{a+1}}.
\tag{11}
\]

For `a>=2`, this first return also satisfies `x>n`: the numerical multiplier `3^a/2^(a+1)` exceeds 1 and its additive term is positive. Nevertheless, at the final endpoint `m`,

\[
\boxed{P(m)<\frac34P(n).}
\tag{12}
\]

Here is a uniform proof. The exact final expression is

\[
2m+1=3+(3/4)^b\bigl((3/2)^a(n+1)-3\bigr).
\]

Its ternary valuation is 1. Indeed `2x+1=3^a u`, with `3` not dividing `u`; hence `2x-2` is divisible by 3, and at least one subsequent `10` makes `2m+1=3+(3/4)^b(2x-2)` exactly divisible by 3. The first-return source rank is `3^a((n+1)/2^a)^2`, proving (11).

Bounding the final rank ratio as the square of the sum of the constant and source terms, the constant term has square at most `1/3` as before. Since `(n+1)/(2n+1)<=2/3`, the square of the source term is at most

\[
\frac{27}{1024}(243/256)^h(27/32)^{2a}
\le\frac{27}{1024}.
\]

This follows by substituting `b=2h+2a+3`; both displayed geometric ratios are less than 1. Therefore

\[
\frac{P(m)}{P(n)}<\frac23+\frac{27}{512}<\frac34.
\]

CRT again supplies infinitely many ordinary sources for every pair `(a,h)`. The duration `4h+5a+7` and both arithmetic parameters are unbounded. The checker reconstructs 120 pairs `1<=a<=8,2<=h<=16`, while the proof covers every pair. This remains a specified contracting word family, not a claim that every actual trajectory eventually chooses one of its words.

## 4. T-ATR-303: a sound common-rank certificate language

A certificate may use any of the following exact blocks:

- an `R` return whose endpoint is in `G`, which halves `P`;
- a finite word on an upward progression certified by T-ATR-301;
- a parametric block T-ATR-302 whose height and finite parity cylinder are verified.

**Conditional termination theorem.** If every hard source admits at least one legal finite block of the displayed kinds, with endpoint in `H union {1}` and strictly smaller `P`, then Collatz holds. A proved total selector of such blocks is a sufficient way to establish this coverage hypothesis.

The proof is ordinary well-founded descent in the **same positive integer rank** `P`. An infinite block path would produce an infinite strictly decreasing sequence of positive integers. Each block is finite and physically valid. Every positive input reaches `H union {1}` by T-ATR-101. Thus all positive inputs reach 1. A cycle cannot evade the argument: strict decrease around its block decomposition is impossible.

The total-selector or complete-cover hypothesis is not supplied. An instruction to search until an unproved rank drop occurs is not a certificate of that hypothesis. In particular the finite source pilot, even though every tested source has a drop, does not justify unrestricted search.

## 5. Relation to rewriting and the exact remaining task

This is a semantic arithmetic-block approach, motivated by the mixed binary/ternary termination route. It does not claim to orient all eleven Yolcu-Aaronson-Heule rewrite rules, to prove termination for every rewrite strategy, or to evade a proved finite-state obstruction merely by renaming state. The unbounded parameter `h` is a genuine ordinary valuation, and its contract is proved for every height.

The substantive improvement is that a single symbolic block handles **arbitrarily large temporary rank increases**, and every generated finite certificate uses the same rank. Hence future tiles can be composed without the unsound assumption that different local rankings combine into one global proof.

The next task is a complete arithmetic coverage theorem for the remaining resonance-return cases, or a richer parameter family whose contracts reduce that coverage problem. Route 1's explicit first-return fan and certified excursion tail give a complementary way to locate the cases that resist this rank.
