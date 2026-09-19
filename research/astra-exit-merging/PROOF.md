# Two-exit source merging through expanding 110 blocks

**Status: PROPOSED pending independent mathematical review.**
**Date:** 2026-09-19. **Programme:** issue #121, GettysburgResearch/collatz.
**Baseline:** `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`.

This packet obtains one guarded, composable, unbounded two-stage certificate,
not a universal Collatz proof. Its strongest specialization simultaneously
has no smaller pure ancestor at the original source and no forward descent
on the entire displayed forward arm, yet meets a source below one third of
the original at the same shortcut clock. The numerical corpus is evidence
for these written proofs, not the reason their quantifiers are asserted.

The first odd-exit identity was rederived during this investigation and then
found in related form in Sodelin's earlier L6 note. It is credited, not claimed
as a discovery. No external-priority claim is made for the new assembly either.
All necessary arithmetic is proved below; no external theorem or computation
is a premise. See [sources and limits](SOURCES_AND_LIMITS.md).

## 0. Map, words, source order, and the actual objective

Use the **raw shortcut map**, on positive integers,

$$
T(n)=\begin{cases}n/2,&n\text{ even},\\(3n+1)/2,&n\text{ odd}.\end{cases}
$$

Raw iteration continues around `1 -> 2 -> 1`. Stopping a certificate procedure
at 1 is a separate convention. A word is read left to right; `1` is an odd
shortcut step and `0` an even step. Thus `110` is two odd steps and one even
step, not three unaccelerated Collatz steps. A word is **physical** when its
bits are exactly the parities encountered from its indicated source.

An accepted macro-certificate consists of positive integers n,m, physical
words F,B, and a common endpoint E with

$$
T^{|F|}(n)=T^{|B|}(m)=E,\qquad 1\le m<n.
$$

The inequality compares m with the original n of the macro, not with an
inflated intermediate value. No rank decrease is substituted for that test.
Such a certificate transports convergence from m to n. A successful cover
of every n>1 would therefore prove Collatz by strong induction. This closing
observation is elementary and is not counted as the new result.

### AEM-001a: composition and cancellation bookkeeping

Suppose an accumulated certificate has

$$
T^A(n_0)=T^B(n_i),
$$

and the next macro has `T^a(n_i)=T^b(n_{i+1})`. Set `C=max(B,a)`. Then

$$
T^{A+C-B}(n_0)=T^{b+C-a}(n_{i+1}).
$$

Indeed, both expressions equal `T^C(n_i)`: advance the first identity by
C-B and the second by C-a. Every exponent is nonnegative. If each accepted
macro strictly decreases ordinary source value, a chain of accepted macros
is finite. It may end at an **UNRESOLVED** source, not necessarily at 1.

An exact meeting alone is insufficient: `7 -> 11 -> 17` and `11 -> 17`
share 17, but 11 is larger than 7. The verifier rejects this genuine physical
meeting as a proposed lower-source certificate. The same applies to the
mixed-rank edge 11 -> 17. We do not forbid a valid smaller source from also
appearing somewhere on the forward orbit; ordinary forward descent is valid.
What is forbidden is counting cancellation or a larger intermediate source
as net reduction of the fixed original source.

## 1. AEM-001b: lifting a collision out of a repeated affine shadow

This is a reusable arithmetic interface, not a novelty claim.

Let w be a nonempty parity word of length L with q odd bits. Put
`D=2^L`, `P=3^q`, and write its affine map as

$$
T_w(x)=\frac{Px+A_w}{D}.
$$

Suppose an integer c is a physical fixed point of w for the same signed
shortcut formulas. Thus `A_w=(D-P)c`. Let k>=1 and u>=1 be integers, and suppose

$$
n=c+D^ku,\qquad m=c+\frac{D^k}{2}u
$$

are positive. Both sources follow w repeated k-1 times and arrive at

$$
N=c+Dv,\qquad M=c+\frac D2v,\qquad v=P^{k-1}u.
$$

**Proof.** A parity word has a unique source residue modulo D: at each
extension, the two lifts of a length-j cylinder have opposite parity after
j steps. Consequently every integer congruent to c modulo D follows w.
As long as j<k-1, both

$$
c+D^{k-j}P^ju,\qquad c+\frac{D^{k-j}}2P^ju
$$

are congruent to c modulo D. Applying `T_w(c+y)=c+(P/D)y` proves the displayed
formulas inductively. Intermediate positivity follows from actual positive
shortcut iteration. At j=k-1 we obtain N,M. Finally,
`n-m=D^k u/2>0`.

It follows that any **proved physical seed collision** between N and M lifts
to a lower-source collision between n and m. A seed collision verified only
for one numerical value of v does not supply a parameter theorem. The tails
must be proved on their stated arithmetic domain. The next sections provide
such tails, including another variable-length phase.

For our application `c=-5`, `w=110`, `D=8`, `P=9`; indeed
`-5 -> -7 -> -10 -> -5`. These signed values are only an affine template.
All sources and witnesses in the claimed certificates are positive integers.

## 2. AEM-002: the good odd-exit half-source identity (credited)

Let n>1 be odd and write the actual source as

$$
n=2^r u-1,\qquad r=v_2(n+1),\qquad u\text{ positive and odd}.
$$

Assume the explicit good-exit guard

$$
3^r u\equiv1\pmod4. \tag{G}
$$

Then m=(n-1)/2 is positive and smaller, and

$$
\boxed{T^{r+2}(n)=T^{r+1}(m)=\frac{3^r u-1}{4}.} \tag{1}
$$

The respective physical words are `1^r 00` and `1^(r-1) 01`.

**Proof.** The first r bits at n are odd, and
`T^j(n)=2^(r-j)3^j u-1` for 0<=j<=r. Guard (G) permits two following even
steps. At m the first r-1 bits are odd; this is an empty prefix when r=1.
Their endpoint is `3^(r-1)u-1`. Since (G) implies
`3^(r-1)u=3 mod4`, that endpoint is 2 mod4. One even and one odd step then
produce `(3^r u-1)/4`. All intermediates are positive. This proves (1).

For every even r>=2, the Mersenne source `2^r-1` satisfies (G) and merges with
`2^(r-1)-1`. This does **not** prove convergence of all Mersennes: the reduced
odd-exponent source may still need a different certificate. In particular,
this is not a replacement of one finite horizon by an infinite ordinary orbit.

**Credit boundary.** Sodelin's L6, at the pin in SOURCES_AND_LIMITS, gives the
same good-exit condition and the half-source formula for even r, with a
different smaller witness for odd r. The uniform half-source proof above is
elementary; no claim of external novelty is made. The result is useful here
because it can be inserted into a longer physical two-sided diagram.

## 3. AEM-003: two-exit half-source merging

### Statement

Let k>=1 and u>=1 be integers, with u odd, and put

$$
n=8^ku-5,\qquad z=9^ku+1.
$$

These parameters can be read from the given input: `v2(n+5)=3k`.
Assume

$$
s=v_2(z)\ge5,\qquad h=s-4,\qquad a=z/2^{h+4},
$$

so h>=1 and a is positive odd. Require the second guard

$$
3^{h+1}a\equiv1\pmod4. \tag{H}
$$

Then

$$
m=\frac{n-5}{2},\qquad E=\frac{3^{h+1}a-1}{4}
$$

are positive integers, and the following words are physical:

$$
F=(110)^k\,0100\,1^h\,00,\qquad
B=(110)^{k-1}\,1110000\,1^{h-1}\,01.
$$

They certify

$$
\boxed{T^{3k+h+6}(n)=T^{3k+h+5}(m)=E,\qquad 0<m<n/2.} \tag{2}
$$

Neither k nor h has a uniform upper bound. The assertion is for **every input
satisfying its guards**, not merely sources constructed later by CRT. No future
beyond these physical words is assumed, and convergence is not a premise.

### Proof: identify a physical bridge, not an inverse echo

Set v=9^(k-1)u. The first k-1 repetitions of 110 from n and m take them to

$$
N=8v-5,\qquad M=4v-5.
$$

This is AEM-001b, or follows directly from the block identity

$$
8A-5\longrightarrow12A-7\longrightarrow18A-10\longrightarrow9A-5.
$$

Since `9v+1=z` is divisible by 32, `v=7 mod32`, in particular v>=7. Thus all
initial sources are positive, including m. At the seed pair the exact paths
are

| N path, word 1100100 | M path, word 1110000 |
|---|---|
| 8v-5 | 4v-5 |
| 12v-7 | 6v-7 |
| 18v-10 | 9v-10 |
| 9v-5 | (27v-29)/2 |
| (9v-5)/2 | (27v-29)/4 |
| (27v-13)/4 | (27v-29)/8 |
| (27v-13)/8 | (27v-29)/16 |
| X=(27v-13)/16 | Y=(27v-29)/32 |

Every indicated division is integral and every branch parity is correct
on the whole progression v=7+32t, t>=0. For example, the two final affine
functions are `X=54t+11`, `Y=27t+5`. In particular,

$$
X=2Y+1. \tag{3}
$$

The bridge does not yet yield a common endpoint. It yields a pair to which
the **second, variable-length odd-exit theorem** applies. Indeed,

$$
X+1=\frac{27v+3}{16}=3\cdot2^h a,
$$

so the actual odd-run length of X is exactly h, with odd quotient 3a.
Guard (H) is precisely guard (G) for X. By AEM-002, the physical tails
`1^h00` from X and `1^(h-1)01` from Y meet at E. Concatenating the paths gives
F,B and their displayed clocks. Finally `m=(n-5)/2` is positive and less than
n/2. This proves (2).

### Why this controls a transition rather than just a repeated phase

For j<k-1, the value after j blocks is

$$
n_j=8^{k-j}9^ju-5.
$$

Its first two steps are odd and its first even exit has valuation exactly
one, so it is a hard odd-run exit. It takes a strictly expanding 110 block
to n_(j+1). At the last block the actual exit changes because v=7 mod32.
The bridge then leads to a second odd run of exactly h steps. The theorem
controls both that first change and the second run's guarded exit while
retaining the **original** n as the comparator.

It does not assert that every subsequent trajectory transition is covered.

## 4. AEM-004: actual composition to an equal-clock one-third source

If an input of AEM-003 additionally satisfies `3|n`, define

$$
x=\frac n3-2.
$$

Then x is positive and odd, and

$$
T(x)=\frac{n-5}{2}=m.
$$

Consequently, prefixing B by one odd bit gives an **equal-clock** certificate

$$
\boxed{T^{3k+h+6}(n)=T^{3k+h+6}(x)=E,\qquad 0<x<n/3.} \tag{4}
$$

Positivity holds because the guards imply n>=51. Also n=3 mod4 for k>=1;
with 3|n this is n=3 mod12, so x is an odd positive integer.

For k>=2, the reduced source satisfies

$$
x=(8^ku-11)/3\equiv7\pmod{32}.
$$

Thus its next odd run has length exactly three, with odd quotient 1 mod4,
and its odd exit is a hard one. This identifies the next residual class;
it does not claim that that class is solved. The reduction below n/3 is
already a valid composable induction step regardless of how x is later handled.

## 5. AEM-005: a strong distinction from forward descent and pure inversion

### 5.1 No forward descent anywhere on the declared arm when k>=23

Every guarded input of AEM-003 with k>=23 satisfies

$$
T^j(n)>n\qquad(1\le j\le3k+h+6). \tag{5}
$$

**Proof.** Each of the first k-1 complete 110 blocks increases its starting
value, and each intermediate state exceeds that block's starting value.
This follows immediately from the displayed block identity with A>=1.

On the seven-step N bridge, the smallest value is X for v>=7. Along the
subsequent odd run values increase; of the last two even steps E is the
smaller endpoint. Now

$$
E=\frac{(3/2)^h(X+1)-1}{4}
\ge \frac38(X+1)-\frac14
=\frac{81v-23}{128}.
$$

Also `X >= (81v-23)/128`. Hence every bridge-and-tail state is at least
that lower bound. Compare it to the original source:

$$
\frac{81v-23}{128}-n
=\frac{(81\cdot9^{k-1}-128\cdot8^k)u+617}{128}.
$$

The integer inequality `81*9^22 > 128*8^23`, and monotonicity of the ratio
by a factor 9/8 for each further k, make this strictly positive for k>=23.
Together with the initial increasing blocks, this proves (5).

The cutoff is a sufficient uniform cutoff for this bound, not an asserted
optimal threshold for every h,u. Indeed the CRT example k=22,h=1,t=0 has
n=10551537610161863524347 and E=9901563680549278568108<n.

### 5.2 No smaller pure ancestor at a source divisible by three

If n>0 and 3|n, its only positive one-step predecessor is 2n. An odd
predecessor would have to be `(2n-1)/3`, which is not integral. Since 2n is
again divisible by three, induction gives

$$
\{y>0:T^b(y)=n\}=\{2^b n\}\quad\text{for every }b\ge0. \tag{6}
$$

Thus no positive pure ancestor is smaller than n, at **any** backward depth.
For the divisible-by-three specialization with k>=23, (4), (5), and (6)
coexist: a lower-source two-sided merger is available even though pure
inversion at n never reduces and the entire certified forward arm never
falls below n.

This does not exclude a shorter *different* merging diagram, or later
ordinary forward descent. It is not an all-diagram lower-bound theorem.

### 5.3 Non-vacuity: two independently unbounded parameters and an old residual class

For any integers k,h>=1 and t>=0, put

$$
p=9^k,\quad M=3p,\quad
\epsilon=\begin{cases}1,&k\text{ odd},\\-1,&k\text{ even}.\end{cases}
$$

Let representatives in the indicated ranges be

$$
a_0=((1+\epsilon p)2^{-(h+4)})\bmod M,\qquad0\le a_0<M,
$$

$$
d=((3^{h+1}-a_0)M^{-1})\bmod4,\qquad0\le d<4,
$$

and define

$$
a=a_0+Md+4Mt,\quad
u=\frac{2^{h+4}a-1}{p},\quad n=8^ku-5. \tag{7}
$$

All modular inverses exist.

The congruences give

$$
2^{h+4}a=1+\epsilon p\pmod{3p},\qquad a=3^{h+1}\pmod4.
$$

Thus a is positive odd; u is a positive odd integer with `u=epsilon mod3`;
`v2(9^ku+1)=h+4` exactly; and (H) holds. Since `8^k epsilon=2 mod3`, n is
divisible by three. Also n=3 mod4, hence **n=3 mod12**. For each fixed k,h,
varying t gives infinitely many distinct inputs; k and h can vary without
bound. They are all in the residual class proved for the old ATT-304
normalizer, but that source qualification is contextual and not needed for
any proof here.

The independent verifier reconstructs the same inputs by solving instead
for u modulo `3*2^(h+6)`, and literally replays both physical arms.

This CRT construction establishes that the guard is populated at all stated
lengths. It is **not** a method of forcing a future for an arbitrary fixed n.
The all-input theorem is AEM-003, which reads its parameters from that n.

## 6. Examples, failed extensions, and the first remaining obligation

### Small readable example

With k=h=1 and t=0 in (7), u=103, a=29, n=819 and m=407. The paths are

```text
819 -> 1229 -> 1844 -> 922 -> 461 -> 692 -> 346 -> 173 -> 260 -> 130 -> 65
407 -> 611  -> 917  -> 1376 -> 688 -> 344 -> 172 -> 86  -> 43  -> 65
```

Furthermore `271 -> 407`, so 819 and 271 meet at 65 after ten shortcut steps
each. This example has forward descent; it is not an instance of (5).

### Residual source with no forward descent on the whole certified arm

Take k=23,h=1,t=0, so u=343 and

```text
n = 202471462953036038537211
m = 101235731476518019268603
x =  67490487651012012845735
E = 213749140432556803774475
```

The n and x paths meet at E at **76 shortcut steps each**. Every positive-time
state of the n path through that meeting is greater than n; its minimum is
E. The source is divisible by three and therefore has no smaller pure
ancestor at any backward depth. These numerical claims are independently
replayed in the fixed corpus; the corresponding quantified facts are proved
in Sections 4–5.

### Guards cannot be discarded

- k=2,u=5 gives n=315 and `v2(9^k u+1)=1`: the seven-step bridge guard fails.
- k=2,u=47 gives n=3003, h=1, a=119, but `3^(h+1)a=3 mod4`: the final good-exit
  guard fails. The specified F/B words are not authorized by AEM-003.
- Arbitrarily large members of the ambient form fail either guard. The code
  retains such cases as UNRESOLVED by this rule, never as divergent inputs.
- Dropping the original-source comparison would accept the genuine echo
  7/11 meeting at 17. The checker explicitly rejects it.

The current partial selector implements four elementary rules plus AEM-002
and AEM-003. It is not the complete ATT-304 dictionary normalizer and does not
claim to replace or outperform every earlier algorithm. It terminates at 1
or an unresolved source. The corpus's CORE counts are not a Collatz
convergence census or a percentage of the conjecture proved.

### What this changes, and what is still unproved

The result is not merely a favourable rank along a prescribed expanding
phase. A lower-source correction can now be carried through arbitrarily many
expanding 110 blocks, an actual exit from them, a second arbitrarily long odd
run, and its guarded exit. In the residual specialization, a further inverse
step composes uniformly and lowers the source below n/3 at an equal clock.

The first unresolved branch is the complement of the explicit exit guards,
including the hard odd-exit class encountered by the reduced source. There
is no theorem that every source reaches a certified guard, no closed
well-founded cover of all residual transitions, and no claim to have settled
Collatz. A useful next strengthening must handle a complementary actual
transition while preserving the fixed original source order, not simply
construct a new input on which these same guards hold.
