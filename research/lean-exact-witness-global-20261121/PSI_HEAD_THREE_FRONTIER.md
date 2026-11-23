# Remaining psi head-three rank boundary

This note isolates the initial-even-exponent-two, first-odd-gap-three
branch. It records exact identities and a limitation of two natural
source-prefix rewrites. It does not assert that this branch is impossible
to close, and it does not assert complete interval coverage.

## 1. Exact target word

Write

\[
 S=4q,\qquad 3q+1=8u,\qquad
 \operatorname{Certificate}(u;\tau).
\]

The wanted target is \(2S-1=8q-1\). Its exact positive-gap target word is

\[
 \operatorname{Prefix}(8q-1;[1,1,2,1,1];81u-10).
\]

The word has five odd steps, total clock six, and correction 251:

\[
 243(8q-1)+251=64(81u-10).
\]

The shorter word \([1,1,2,1]\) ends at \(54u-7\), not at
\(81u-10\). The last endpoint \(81u-10\) is odd because \(u\) is
odd, so there is no free halving at that endpoint.

The source edge forces \(u\equiv2\pmod3\). In the original complete
rank, the initial even run contributes grade five and the first odd gap
contributes grade six. Removing that gap can fund arbitrary new gaps at
most two and an initial exponent at most two. Retaining the old gap three
while lowering the initial exponent from two to one can instead fund
additional gap-one/two predecessors of the original \(q\).

## 2. An exact ternary class where both low-gap inverse chains stop

Consider the entire odd class

\[
 u\equiv23\pmod{27}.
\]

Writing \(u=54j+23\) gives

\[
 q=\frac{8u-1}{3}=144j+61\equiv7\pmod9.
\]

Among gaps one and two, the only integral odd predecessor of \(u\) uses
gap one:

\[
 p_u=\frac{2u-1}{3}=36j+15=3(12j+5).
\]

The only such predecessor of \(q\) uses gap two:

\[
 p_q=\frac{4q-1}{3}=192j+81=3(64j+27).
\]

Both are divisible by three. An integer divisible by three has no odd
inverse predecessor at any positive gap, since
\(3r+1=2^a p\) would give \(1\equiv0\pmod3\).
Thus each of these two low-gap inverse chains terminates after its first
step. Repeating a gap-one/two prefix cannot make either chain cofinal.

This limits those particular predecessor constructions. It does not rule
out a source rewrite that consumes additional literal tail gaps or uses a
different target transport.

## 3. The class occurs with a complete alphabet-four source

The member \(u=77\) gives \(q=205\). Their complete odd paths are

\[
 205\xrightarrow{3}77\xrightarrow{3}29\xrightarrow{3}11
 \xrightarrow{1}17\xrightarrow{2}13\xrightarrow{3}5
 \xrightarrow{4}1.
\]

The exact supplied words and affine certificates are:

| Odd source | Complete gap word | Total clock | Correction |
|---|---|---:|---:|
| 205 | \([3,3,3,1,2,3,4]\) | 19 | 75953 |
| 77 | \([3,3,1,2,3,4]\) | 16 | 9403 |

They satisfy \(3^r n+C=2^A\) exactly. Every source gap is at most four,
so the example does not leave the remaining source alphabet. Its two
inverse dead ends are \(p_u=51\) and \(p_q=273\).

For \(S=820\), the wanted target is 1639. The five-gap target word in
Section 1 reaches

\[
 81\cdot77-10=6227.
\]

## 4. A smaller ordinary merger partner has a larger source rank

For this same example, the ordinary paths merge:

\[
 T^{10}(1639)=3503=T^5(1383).
\]

The partner is

\[
 1383=2\cdot692-1,\qquad
 692=9\cdot77-1=4\cdot173<820.
\]

Thus both the proposed new source and the wanted partner are numerically
smaller than the originals. The complete source rank behaves differently.

The actual odd certificate at 173 is

\[
 173\xrightarrow{3}65\xrightarrow{2}49\xrightarrow{2}37
 \xrightarrow{4}7\xrightarrow{1}11\xrightarrow{1}17
 \xrightarrow{2}13\xrightarrow{3}5\xrightarrow{4}1.
\]

Its gap word is

\[
 [3,2,2,4,1,1,2,3,4],
\]

with total clock 22 and correction 789145. Its exact certificate identity
is

\[
 3^9\cdot173+789145=2^{22}.
\]

The original odd source 205 has one gap four. The proposed new odd source
173 has two. Both powered sources have initial exponent two, and neither
odd certificate has a gap larger than four. Therefore the highest changed
grade is eight, whose multiplicity **increases from one to two**. The new
complete source rank is strictly larger.

The positive-gap certificate determines the ordinary odd path until its
first one. Every certificate for 173 must therefore include both displayed
gap-fours; appending terminal gap-two loops cannot lower that grade-eight
multiplicity. The numerically smaller partner does not supply an
admissible lower-ranked source certificate in the current induction.

In particular, proving membership of \(9u-1\) through the interval
hypothesis and then extracting an arbitrary output certificate is
insufficient for this next call. This example exhibits the missing rank
bound explicitly.

## Verification and scope

A compact one-off exact-integer replay checked:

- Every displayed odd source edge, odd endpoint, and complete affine
  identity for 205, 77, and 173.
- The target word \([1,1,2,1,1]\), its correction 251, and its endpoint
  6227 for the example.
- The ordinary merger \(T^{10}(1639)=T^5(1383)=3503\).
- The two inverse candidates 51 and 273 and their divisibility by three.
- The one-versus-two counts of gap four that determine the rank comparison.

There was no interval search, numerical cutoff, or unproved target
certificate assumption. The universal ternary-class calculation in
Section 2 is algebraic. The example identifies a concrete source-rank
boundary for this partner construction; a different complete-rank return
for the head-three branch remains to be supplied.
