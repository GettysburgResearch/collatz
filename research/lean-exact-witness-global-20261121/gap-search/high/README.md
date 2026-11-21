# High first-exponent witness rewrites

**Status: exact conditional rewrites and a finite search receipt. Universal
reverse tripling, and hence the full Collatz goal, remain open.**

This checkpoint changes the decreasing quantity in one source-witness
construction. A child source may be numerically larger and have a longer
witness, while the sum of powers of the witness's accelerated exponents
strictly decreases. The search does not produce a complete dispatcher.

## Original result and source pins

The starting rule is SZD-001/SZD-002 in
[`SOURCE_ZERO_DESCENT.md`](https://github.com/GettysburgResearch/collatz/blob/4e3231167d1e044e84f4a8b4469bf57225814d86/research/witness-global-closure-20261121/SOURCE_ZERO_DESCENT.md),
at repository commit
`4e3231167d1e044e84f4a8b4469bf57225814d86`. Its checker is
[`check_source_zero_descent.py`](https://github.com/GettysburgResearch/collatz/blob/4e3231167d1e044e84f4a8b4469bf57225814d86/research/witness-global-closure-20261121/check_source_zero_descent.py)
at the same commit. Their file SHA256 values are respectively
`34dd2294996192279f894fa35d29610773e31a762c272d7da689f88af7d3813c`
and `9aaa78707aa44ab5caad92b1a52155374b0fda14f26ca208eb999945026dbc3b`.

The original rule uses

\[
m=69984u+50063,\qquad p=65536u+46881
  =\frac{2048m-277}{2187},\qquad u\ge0.
\]

It replaces a complete source witness for \(27m\) by

\[
(a)\mathbin\Vert w\quad\longmapsto\quad
(1,2,1,2,3,1,3,a-2)\mathbin\Vert w,\qquad a\ge5,
\]

and transports a target witness for \(9p\) back to \(9m\). Its original
proof used \(p<m\). Here the same source substitution also decreases
\(\sum_i3^{a_i}\): the decrease is
\(8\cdot3^{a-2}-81>0\). This observation motivates allowing expanding
children in a broader grammar.

## HG-001. The exact uniform high-gap grammar

Write

\[
R(m):\quad \operatorname{Basin}(27m)\Longrightarrow
\operatorname{Basin}(9m),
\]

for positive odd \(m\). Complete witnesses use the accelerated odd map,
with one positive exponent for each odd step. If the first source
exponent is \(a\), then

\[
a=v_2(81m+1),\qquad
a\ge5\iff m\equiv15\pmod{32}.
\]

Put \(t=(81m+1)/32\), \(h=v_2(t)\); thus \(a=5+h\).
For a word \(W=(w_1,\ldots,w_r)\), define

\[
B=\sum_iw_i,\qquad
C=\sum_{i=0}^{r-1}3^{r-1-i}2^{w_1+\cdots+w_i},
\qquad F_W(x)=\frac{3^r x+C}{2^B}.
\]

Every source letter in this checkpoint belongs to \(\{1,2,3,4\}\).
Let \(k\in\{0,1\}\), and require a target word \(V\) satisfying

\[
|V|=r+2+k,\qquad B(V)=B+k-1,
\qquad C(V)=3^k(2^B+3C)-2^{B+k-1}.
\tag{1}
\]

Define

\[
q=2^B,\qquad d=\frac{q-32C}{81},\qquad D=3^{r-1},
\qquad p=\frac{qm+d}{32D}.
\tag{2}
\]

The integrality guards are

\[
q-32C\equiv0\pmod{81},\qquad
m\equiv-dq^{-1}\pmod D,
\tag{3}
\]

together with \(m\equiv15\pmod{32}\). The latter guarantees divisibility
by the binary factor in (2), because
\(81(qm+d)=q(81m+1)-32C\). The lower endpoint of the progression is
shifted, when necessary, until both \(m\) and \(p\) are positive.
The retained residue and its first positive parent are recorded exactly.

Let \(A_0=(1,1,2)\) and \(A_1=(1,1,2,1)\). Direct substitution in
(1)--(2) gives identities for the entire affine progression:

\[
F_{(5)}(27m)=F_W(27p)=t,
\]

\[
F_{A_k}(9m)=F_V(9p)=
\begin{cases}
6t+1,&k=0,\\
9t+2,&k=1.
\end{cases}
\tag{4}
\]

These are identities in an unbounded parameter. The checker verifies
each rational affine coefficient at every step: all states before the
last step are positive odd, with positive even slope and positive odd
intercept. Only the final endpoints are allowed to be even. No finite
list of values of \(a\), \(h\), or the parent parameter substitutes for
this verification.

For the source, increase the last letter of \(W\) by \(h\). Both source
prefixes then end at the same positive odd integer \(t/2^h\). For the
target, let \(g\) be the valuation of the common endpoint in (4), and
increase the last letters of \(A_k,V\) by \(g\). Both target prefixes
then end at the same positive odd integer. Thus the source substitution
is

\[
(a)\mathbin\Vert w\longmapsto
(w_1,\ldots,w_{r-1},w_r+a-5)\mathbin\Vert w.
\tag{5}
\]

The entire supplied source tail is copied, including any terminal
exponent-two padding. Once the child target is known to converge, the
target prefix in (4) can be replaced by the parent target prefix and its
tail copied. If a target witness ends before a displayed forced prefix,
terminal exponent-two loops can first pad it to the required length.
Consequently each retained rule proves \(R(p)\Rightarrow R(m)\), and
membership of both paired sources and targets is equivalent along their
ordinary prefixes. No bound is imposed on the returned target witness.

## HG-002. A natural-number source measure

For a complete source exponent word \(w\), define

\[
\mathcal G(w)=\sum_{b\in w}15^b.
\]

This is an energy of the **accelerated exponent word**. It differs from
the other checkpoint's energy \(\sum C^{\text{trajectory value}}\).
It also differs from ordinary shortcut length or the number of odd
steps.

Every retained word has \(r\le14\), and every letter of \(W\) is at
most four. In (5), every inserted fixed letter is therefore less than
\(a\), while its final letter satisfies

\[
w_r+a-5\le a-1.
\]

For every \(a\ge5\), without an upper cutoff,

\[
\mathcal G(w_1,\ldots,w_{r-1},w_r+a-5)
\le14\,15^{a-1}<15^a.
\tag{6}
\]

The common tail cancels from the comparison. This is a strict natural
number descent even when the child parameter, source clock, and odd
length all increase. In the retained catalogue, 7916 child affine slopes
exceed one and 231 are less than one; no magnitude-contraction guard was
used.

## HG-003. Finite search scope and exact receipt

The generator enumerates source lengths \(1\le r\le14\), letters
\(1\le w_i\le4\), the exact integral guards (3), and only the two
uniform target templates \(k=0,1\). It uses a signed rational reference
to determine the forced target word for each permitted length. If a
first arrival with \(k=0\) can be padded by an exponent-one signed loop
to give \(k=1\), the first arrival is retained; the source word and its
ternary cell are unchanged. The reference test has an
exact grade bound derived from (1), not an arbitrary orbit cutoff.
Once the denominator clears, every run of exponent-one steps away from
\(-1\) is finite; each other step increases the nonnegative grade, so
the bound terminates the test.

The mod81 filter depends only on the last four source letters, because
the earlier correction is multiplied by \(3^4\). Exactly six such
suffixes pass; they are listed in the receipt. This pruning discards no
word from the stated finite grammar. Every accepted result is then
replayed by the independent affine identities (4).

The full default run returns:

| Quantity | Exact result |
|---|---:|
| Retained conditional rules | 8147 |
| Minimal ternary prefix cells after all sibling merges | 5532 |
| Union measure of these ternary guard cylinders | \(5950/531441\) |
| Complement of that ternary union | \(525491/531441\) |
| Complete high-gap ternary cover | false |
| Exponent-energy base for the retained length guard | 15 |

The fraction is the exact Haar measure of the specified **ternary guard
cylinders within this high-first-gap grammar**. It is not a percentage
of the full theorem proved, a density statement about the unknown basin,
or a coverage assertion for all possible witness transformations.
Finite positive lower endpoints are checked and stored separately.

About 98.88% of that ternary space remains outside this union. Source
first exponents one through three still require a global dispatcher.
First exponent four has the separate ordinary merger from the direct-R
normal forms; this generator does not replace it. Any auxiliary
comparison state activated by a proposed global dispatcher also needs a
proof. In particular, no closure for all high-gap F3 states is supplied
here. Increasing the finite source length is not a proof that the
uncovered cells will disappear.

## Replay

Run from this directory:

```bash
python3 high_gap_source_zero.py --receipt /tmp/collatz-high-gap-replay.json
python3 -O high_gap_source_zero.py --receipt /tmp/collatz-high-gap-replay-O.json
```

Both commands generate and check all 8147 rules and emit deterministic
receipts. They use explicit validation, not Python assertions. The full
catalogue is deliberately omitted from the checkpoint. To regenerate it:

```bash
python3 high_gap_source_zero.py --receipt /tmp/collatz-high-gap-replay.json --catalog /tmp/collatz-high-gap-catalogue.json
```

The canonical mathematical-record hash is
`0d9e8db87714dfc066fb9c6a9a5a9fffc1fee8a7357d63db0b8a1fffb102b377`.
It includes every rule and the reduced ternary union, but excludes
runtime, formatting, and prose. It matches the original search output
before the generator was made portable. The checked results are exact
integer and rational computations; this checkpoint does not claim that
the general dispatcher or this search implementation has been formally
verified in Lean.
