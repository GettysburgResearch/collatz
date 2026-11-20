# A local simple-path reciprocal budget

**PROPOSED; elementary proof, independently reconstructed.** This
appendix supplies the only orbit-packing input used by SB5 of
`STOPPING_BURDEN.md`. It concerns finite simple paths under the shortcut
map `T(n)=n/2` for even `n` and `T(n)=(3n+1)/2` for odd `n`.
It does not assume that an arbitrary positive orbit terminates.

The stronger translated bound in PR #140,
`fe2247fcd7730c15430941a7b6e011d006d41d84`,
`research/novel-swarm-20261030/pass4/WINDOWS.md`, is an antecedent and
comparison: it yields a reciprocal budget of 320. The shorter proof
below gives 600 and is self-contained. It claims no novelty for the
general orbit-sparsity mechanism.

## LD1. An anchored shell estimate

Let `P=(x_0,...,x_M)` be any finite shortcut-orbit segment whose states
are pairwise distinct, and let `Y>=1` be an integer. Then

\[
\boxed{\#\{x\in P:Y\le x<2Y\}\le8Y^{49/50}.}                    \tag{1}
\]

Set `h=floor(log_2 Y)`. Remove the last `h` positions of `P`, or all
positions if the segment is shorter. This costs at most `h` states.
On the retained positions, `T^h` is injective and its images still lie
in the same simple path: indices `i` map to indices `i+h`, and the
states at distinct indices differ.

For every length-`h` parity word of weight `q`, the exact affine identity
and remainder bound are

\[
T^h(x)=\frac{3^q}{2^h}x+R_w,
\qquad 0\le R_w\le(3/2)^q-1.                                    \tag{2}
\]

To verify the upper bound, write
`2^hT^h(x)=3^qx+C_w`. Swapping an adjacent odd/even pair `10` to
`01` increases `C_w`; moving all even letters before all odd letters
therefore gives the maximum
`C_w=(3^q-2^q)2^(h-q)`. Dividing by `2^h` gives (2). A parity word
selects exactly one residue modulo `2^h`: inductively the next parity
chooses one of the two lifts of the previous residue, since its
current affine coefficient is odd. Hence all words are represented
and have distinct source residues.

**High odd-count lane.** Put `r=3/2`. The number of words with
`q>3h/5` is at most

\[
r^{-3h/5}(1+r)^h
=\left(\frac{3125}{108}\right)^{h/5}
\le2^{49h/50}.
\]

The last comparison follows from the exact certificate

\[
3125^{10}<108^{10}2^{49}.                                        \tag{3}
\]

An interval of `Y` consecutive integers, with `Y<2^(h+1)`, has at most
two lifts of each residue modulo `2^h`. Thus this entire lane
contributes at most `2Y^(49/50)` sources. When `h=0` the lane is
empty, and the same upper estimate remains valid.

**Remaining lane.** Every retained source `x` in `[Y,2Y)` with
`q<=3h/5` has, by (2),

\[
0<T^h(x)
\le(2Y/2^h+1)3^q
\le5\cdot3^{3h/5}
\le5Y^{49/50}.
\]

The last comparison is certified by

\[
3^{30}<2^{49}.                                                   \tag{4}
\]

These images all lie in **one anchored interval**, independent of the
parity weight. Because the map is injective on the retained positions,
the lane has at most `5Y^(49/50)` sources. No bound on the original
path length or its maximum height is used.

Finally `h<=Y^(49/50)`: check `h=0,1,2,3` directly, and for `h>=4`
use `h<=2^(h/2)<=Y^(49/50)`. Adding the removed positions and the
two lanes proves (1), with `1+2+5=8`.

## LD2. A uniform reciprocal and distortion bound

Partition the positive integers into the shells `[2^j,2^(j+1))`.
Equation (1) gives, for every such simple path,

\[
\sum_{x\in P}\frac1x
\le8\sum_{j=0}^\infty2^{-j/50}
=\frac8{1-2^{-1/50}}<600.                                       \tag{5}
\]

The final strict comparison follows from the exact certificate

\[
2\cdot74^{50}>75^{50},                                         \tag{6}
\]

which gives `2^(-1/50)<74/75`. There is no dependence on the number
of states or on their heights.

For the first-hit segment from a convergent source to 1, the odd inputs
are a subset of this simple path. Therefore its product

\[
D(n)=\prod_{\text{odd inputs }u}\left(1+\frac1{3u}\right)
\]

satisfies

\[
\boxed{0\le\log_2D(n)\le D_*:=200/\ln2.}                        \tag{7}
\]

Indeed `ln(1+t)<=t` and (5) give the upper bound. The empty first-hit
path at 1 has product one. A primitive cycle can be counted once in
(5); repeated laps cannot be counted with multiplicity. An entire
predecessor basin is also outside the simple-path hypothesis.

The three exact certificates (3), (4), and (6) were evaluated with
Python integers in `local-distortion-report.json`. These finite scalar
checks support the inequalities; the written argument proves the
all-path statement.
