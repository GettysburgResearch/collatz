# L-9819 — Two-orbit overlap and carry bounds for survivor gaps

Claim ID: `L-9819`  
Title: Aligned directive agreement forces an exponential gap between ordinary survivors  
Status: `PROPOSED`  
Authoring agent: `gpt56-synthesis-01-a`, integrated by `gpt56-synthesis-01`  
Reviewing agents: `gpt56-synthesis-01`  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: `L-9803`; `L-9815` for the successor-gap application  
Scope: pairwise separation of two ordinary `64 -> 81` survivor prefixes  
Related counterexample candidates: none

## Definitions

Let `A<B=A+d` both survive `n` chart steps. Write their states and directives
as

\[
A_j,\varepsilon_j,
\qquad
B_j,\nu_j,
\qquad
\Delta_j=B_j-A_j>0.
\tag{1}
\]

Put

\[
\delta=\log_{64}(81/64),
\qquad
L=\log_{64}(d+1).
\tag{2}
\]

Let `W_n` be their aligned Hamming distance,

\[
W_n=\#\{0\le j<n:\varepsilon_j\ne\nu_j\}.
\tag{3}
\]

For their length-`n` words `u,v`, define the aligned overlap surplus

\[
\Gamma_n(u,v)
=\max\left(
0,
\max_{\substack{s,r\ge0\\s+r\le n\\u[s:s+r]=v[s:s+r]}}
(r-\delta s)
\right).
\tag{4}
\]

## Statement

### 1. Exact orbit-difference recurrence

The state difference satisfies

\[
\boxed{
64\Delta_{j+1}
=81\Delta_j-17(\nu_j-\varepsilon_j).
}
\tag{5}
\]

Consequently,

\[
\boxed{
(81/64)^s(d-1)+1
\le\Delta_s
\le(81/64)^s(d+1)-1.
}
\tag{6}
\]

### 2. Common-block wedge

If the two directives agree for `r` positions beginning at `s`, then

\[
\boxed{
r<\delta s+\log_{64}(d+1).
}
\tag{7}
\]

Equivalently,

\[
\boxed{d>64^{r-\delta s}-1.}
\tag{8}
\]

Taking the best aligned block gives the exact overlap-to-gap bridge

\[
\boxed{
\log_{64}(d+1)>\Gamma_n(u,v),
\qquad
d>64^{\Gamma_n(u,v)}-1.
}
\tag{9}
\]

In particular, an aligned block of length `rho n-o(n)` beginning before
`sigma n+o(n)`, with `rho>delta sigma`, forces

\[
d\ge64^{(\rho-\delta\sigma-o(1))n}.
\tag{10}
\]

### 3. Exceptional-carry count

The orbit-difference carries

\[
c_j=64\Delta_{j+1}-81\Delta_j
=-17(\nu_j-\varepsilon_j)
\in\{0,\pm17\}
\tag{11}
\]

are nonzero at exactly the `W_n` disagreement positions. They obey

\[
\boxed{
n<\frac{L+1}{\delta}
\left((1+\delta)^{W_n+1}-1\right).
}
\tag{12}
\]

Hence

\[
\boxed{
W_n>
\log_{1+\delta}\left(1+\frac{\delta n}{L+1}\right)-1,
}
\tag{13}
\]

and, conversely, `W_n<=q` implies

\[
\boxed{
d>
64^{\frac{\delta n}{(1+\delta)^{q+1}-1}-1}-1.
}
\tag{14}
\]

Thus bounded aligned Hamming distance forces an exponential gap. More
generally, `W_n=o(log n)` forces the precise lower-bound scale

\[
d>64^{\,n^{1-o(1)}}-1.
\]

### 4. Base-64 shadowing forced by a small successor gap

Let `B=A+D_n(A)<64^n` be the exact successor from `L-9815`, and write

\[
A=\sum_{j<n}a_j64^j,
\qquad
B=\sum_{j<n}p_j64^j.
\tag{15}
\]

If `t` is minimal with `D_n(A)<64^t`, then above position `t` the digit words
agree except possibly for one ordinary addition-carry avalanche: a consecutive
run of digits `a_j=63` becomes zero, its next digit is incremented, and all
higher digits agree again.

If `h(B)` is minimal with `B<64^h`, then more simply

\[
\boxed{p_j=0\qquad(h(B)\le j<n).}
\tag{16}
\]

There are at most `2^h` depth-`n` survivor words whose representative is below
`64^h`. Hence subexponential representatives occupy only `2^(o(n))` of the
`2^n` finite cylinders.

### 5. Successor-minimum application

At a jump `M_K<M_(K+1)`, equations (7)--(16) apply to the first `K`
directives of

\[
A=M_K,
\qquad
B=M_{K+1},
\qquad
d=M_{K+1}-M_K.
\tag{17}
\]

A sufficient missing theorem is therefore:

> **Successor overlap-surplus conjecture.** There is `gamma>0` such that every
> sufficiently large minimum jump satisfies
> `Gamma_K>=gamma K-O(1)`.

Under this exact hypothesis,

\[
\boxed{
M_{K+1}-M_K\ge64^{\gamma K-O(1)}.
}
\tag{18}
\]

This quantifies jumps but does not prove that jumps occur infinitely often.

## Proof

Subtracting the two exact chart recurrences proves (5). Replacing
`nu_j-epsilon_j` by `+1` or `-1` and iterating the two affine comparison
recurrences gives (6).

On an agreement block, (5) is homogeneous, so

\[
64^r\mid\Delta_s.
\]

Put `Z_s=64^s Delta_s`. Then `64^(s+r)` divides `Z_s`, while (6) gives

\[
0<Z_s<81^s(d+1).
\]

Applying the product-formula wedge `L-9803` with `M=64,N=81,H=d+1`
proves (7)--(10).

Every zero-carry run beginning at position `s` has length below `delta s+L`
by (7). Start at zero and cover the prefix successively by a maximal zero run
and one exceptional carry. The next starting position is at most

\[
(1+\delta)s+L+1.
\]

Iterating this affine bound through `W_n+1` zero runs gives (12). Algebraic
rearrangement gives (13)--(14).

Part 4 is ordinary base-64 addition. Adding a number below `64^t` changes no
higher digit unless a carry enters position `t`; such a carry propagates
through exactly one run of `63` digits. Equation (16) is the zero padding of
the standard representative. A depth-`h` survivor has one deterministic
continuation, so at most the `2^h` depth-`h` words can produce a depth-`n`
representative below `64^h`.

Finally, `M_K` and `M_(K+1)` both survive `K` steps. Substitution in (9) proves
(18). ∎

## Motivation

`L-9815` makes the next-survivor gap exact, while `L-9803` controls long
zero-carry runs. This lemma joins them at the two-orbit level. It shows exactly
what a global complexity theorem must provide: aligned correlation between the
minimum and its successor, not merely complexity of either word separately.

## Dependency audit

- The difference recurrence and real comparison bounds are derived directly.
- `L-9803` supplies only the product-formula wedge used in (7).
- `L-9815` supplies the canonical successor interpretation, not any gap bound.
- No single-word complexity theorem is imported.

## Gap audit

- Single-word factor complexity does not imply positive overlap surplus for a
  pair of different survivor rooms.
- A zero base-64 cylinder suffix does not imply a zero itinerary suffix; the
  hidden terminal state remains unbounded.
- Exponential sizes of individual jumps do not rule out eventual stabilization
  of the minimum sequence.
- The overlap-surplus conjecture is a target, not an empirical claim.

## Adversarial tests

- At `s=0`, agreement for `r` positions gives the stronger exact divisibility
  `64^r|d`; the `d+1` in (7) preserves the strict logarithmic inequality.
- Complementary binary words can have identical single-word factor complexity
  and no aligned agreements, showing why a pairwise hypothesis is essential.
- A long addition-carry avalanche can destroy high digit agreement even when
  `D_n(A)` is small; part 4 records this exact exception.

## Remaining uncertainty

No Collatz-specific theorem currently forces a macroscopic aligned block or a
small Hamming distance between successive minimizing directives. This is the
precise cross-correlation gap.

## Suggested next attack

Seek a synchronizing transducer from zero-padded cylinder digits to itinerary
digits. If a common high cylinder suffix resets the transducer in bounded time,
part 4 creates the aligned block needed by (18). `L-9818` isolates the exact
synchronization hypothesis and explains why ordinary regular-language safety
does not yet provide it.
