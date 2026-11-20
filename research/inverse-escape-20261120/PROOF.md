# A physical inverse-credit certificate with slope 25/12

**Status: PROPOSED, computer-assisted universal conversion theorem.**
The finite integer inequalities have been checked independently. This is an
inverse construction, and does not prove Collatz convergence or merging.

The predecessor packet is PR #147 at
`b74b2d466f58844a742a6ed6bcdf06844269f361`, principally
[`research/robust-inverse-credit/PROOF.md`](https://github.com/GettysburgResearch/collatz/blob/b74b2d466f58844a742a6ed6bcdf06844269f361/research/robust-inverse-credit/PROOF.md).
That packet supplies an explicit `13/6` compiler. Its stronger existential
claims have separate external hypotheses; none is used below.

## 1. Statement

Use the shortcut Collatz map

\[
T(n)=\begin{cases}n/2,&n\text{ even},\\(3n+1)/2,&n\text{ odd}.\end{cases}
\]

**Theorem P1.** There is an explicitly supplied nonnegative integer potential
`W` on the unit residues modulo `M=3^17=129140163`, with `0<=W<=133`,
having the following property. For every `t>=1` and every integer
`0<c<3^t`, `3` not dividing `c`, one can construct `k,r` and a length-`k`
parity word with exactly `t` odd events such that

\[
0<r<2^k,\qquad T^k(2^k x+r)=3^t x+c\quad\text{for every integer }x\ge1,
\]

and

\[
k\le\left\lfloor\frac{25t+W(c\bmod M)-13}{12}\right\rfloor
\le\boxed{\left\lfloor\frac{25t+120}{12}\right\rfloor}.
\tag{1}
\]

Every nonterminal inverse block chosen by the certified selector has exponent
at most ten. The final exponent is at most two. The same word works for every
positive prefix `x`; no higher digit of `x` is chosen or inspected.

The terminal offset in (1) uses the physical potential's exact relation
between the two unit classes. Merely using `W>=0` would give the weaker
numerator `25t+132`.

Compared with the earlier explicit bound `floor((13t+65)/6)`, both the
asymptotic slope and the displayed additive term improve. This is an
improvement to that explicit bounded-alphabet online construction, not a
claim to the best existential inverse-prefix estimate. In particular, the
earlier packet credits a source-qualified existential `2t` statement from
[rStation paper 48, version 2](https://rstation.ai/problems/collatz/papers/48/v2),
whose onset and alphabet have different specifications. That external proof
has not been independently reconstructed in this pass.

## 2. Two physical inverse actions

For ternary units, write

\[
E(z)=2z,\qquad O(z)=(2z-1)/3.
\]

The action `E` is always legal. The action `O` has an integral unit target
exactly when `z` is `2` or `8` modulo nine. Both preserve positivity when
applied legally to positive ordinary integers. Each action costs one shortcut
inverse step, and `O` accounts for one odd event. In particular, `e-1`
successive `E` actions followed by `O` give

\[
I_e(z)=(2^e z-1)/3.
\]

For positive integers `p,q`, the physical credit inequalities are

\[
q+W(Ez)\le W(z),\tag{2}
\]

or, for a legal odd action,

\[
q-p+W(Oz)\le W(z).\tag{3}
\]

At least one of (2) and (3) must hold at every unit. All potential arguments
are reduced modulo `M`. Inequality (2) is checked at one residue; (3) is
checked for all three possible next ternary digits. Indeed, for
`z=r+Mu`, the even image is fixed modulo `M`, while

\[
O(z)=(2r-1)/3+2(M/3)u.
\]

Checking `u=0,1,2` therefore checks every ordinary input in the supplied
residue class. No averaging over the missing digit is allowed.

Choose `O` whenever it is legal and satisfies all three inequalities;
otherwise choose `E`. Along each chosen `E`, the nonnegative credit decreases
by at least `q`. Consequently an `O` is reached within
`floor(max W/q)+1` physical steps. Summing (2)--(3) through that block yields

\[
qe+W(I_ez)\le p+W(z).\tag{4}
\]

For `p=25,q=12,max W=133`, this argument alone gives exponent at most twelve.
The separate exhaustive scalar verification collapses the actual selector
at every one of the `86093442` unit residues and obtains the sharper maximum
ten. It also checks (4) directly on all three lifts, rather than relying on
telescoping the physical checks. The distinction between the a priori bound
and the checked sharper bound is retained in the replay receipt.

## 3. Reduction to one unit class

Write `N=M/3=3^16`, `H=N/3`. Store only

\[
V_i=W(3i+2),\qquad 0\le i<N.
\]

Define the other class by

\[
W(3i+1)=q+V_{2i\bmod N}.\tag{5}
\]

This makes (2) an equality in class one. In class two, an even action enters
class one, so a consecutive pair of even actions has cost `2q` and takes
index `i` to `4i+2 mod N`.

For `i=3j`, the odd image of `3i+2` is in class one. Applying (5) to this
image adds one forced even action. Its cost is `2q-p`, and the three possible
reduced image indices are `4j+kH mod N`. For `i=3j+2`, the odd image is in
class two; its cost is `q-p`, and the three indices are `2j+1+kH mod N`.
For `i=3j+1`, the odd action is illegal.

Set

\[
B_j=\max(V_j,V_{j+H},V_{j+2H}),\qquad 0\le j<H.
\]

The complete reduced conditions are therefore

\[
\begin{aligned}
V_{3j}&\ge\min\{2q+V_{12j+2\bmod N},\;
                 2q-p+B_{4j\bmod H}\},\\
V_{3j+1}&\ge2q+V_{12j+6\bmod N},\\
V_{3j+2}&\ge\min\{2q+V_{12j+10\bmod N},\;
                   q-p+B_{2j+1\bmod H}\}.
\end{aligned}\tag{6}
\]

Every index and coefficient here is integral. The minimization can be
replaced by one selected action per row. That is the compact certificate
actually published.

## 4. The strategy file is the certificate

[`policy_25_12.bits.gz`](policy_25_12.bits.gz) is a deterministic gzip container
whose decoded payload has `3587227` bytes encoding `28697814=2H` bits.
In increasing `j`, bit `2j`
selects the second expression in the first line of (6), and bit `2j+1` selects
the second expression in the third line. A zero selects the even expression.
The middle line is forced and needs no bit. Bits are packed least significant
bit first within each byte; unused high bits in the last byte are zero.

The published container is `1872249` bytes. The exact digest of its decoded
strategy and the digest of the reconstructed credit are in
[`certificate.json`](certificate.json). The format is independent of native
integer endianness.

The strategy's potential is defined by a finite calculation. Start all `V_i`
at zero. Replace each row by the maximum of zero and its selected right side
in (6), simultaneously, using the previous vector. Iterate at most 202 times.
The supplied strategy reaches an exact fixed point at iteration 202, with
`min V=0`, `max V=121`. Equation (5) then gives `max W=133`.

[`reconstruct_policy.cpp`](reconstruct_policy.cpp) implements this fixed
strategy recurrence. It contains no action minimization and performs no
search. It rejects an overflow, invalid bit count or padding, or failure to
reach a fixed point within the specified horizon. It writes one byte per
reduced credit only after a successful exact check. The output's SHA-256 is

```
bdf70ec223fbd08baa6ae3040dfb394185e98b08b5b388c09a5ff844d57faf33
```

The `43046721` output bytes have been compared byte for byte with the
class-two entries of the independently checked full potential. Reconstructing
the full little-endian signed-32-bit vector in increasing unit-residue order
gives SHA-256

```
e88a51546c4ccb6951164c19877675e462f108dc246eb18223f3c9aa43d52a8f
```

The strategy recurrence by itself defines a completely reproducible finite
artifact. The hashes identify that artifact; they are not substitutes for
its inequality checks. [`verify.py`](verify.py) reads the strategy, rebuilds
the potential, authenticates its bytes, and independently checks all selected
reduced rows before replaying affine cones.

For context, the search used the minimum in (6). If `G` is that operator,
including clipping below at zero, and `A` is the operator of a selected
strategy, then `Gf<=Af`. Suppose the final reduced potential `V_*` satisfies
`G V_*=A V_*=V_*`. Monotonicity gives `G^n0<=A^n0<=V_*`. Thus
`G^n0=V_*` at a known finite horizon implies `A^n0=V_*` at that horizon.
This explains why a successful minimum-cost search
can be replaced by a short fixed-strategy reconstruction. The published
proof does not assume that the search finds an optimum, and the actual
202-step reconstruction is checked directly.

## 5. Terminal repayment and the cone proof

At a unit constant `c`, use the final exponent

\[
a_{\rm f}(c)=\begin{cases}1,&c\equiv2\pmod3,\\2,&c\equiv1\pmod3.\end{cases}
\]

The final predecessor is positive and integral; its being a ternary unit
is unnecessary. Equations (5) and `V>=0` give the sharper terminal refund

\[
q a_{\rm f}(c)-W(c)\le q.\tag{7}
\]

For `c` in class two this is `q-W(c)<=q`. For class one it is
`2q-[q+W(2c)]<=q`, with `2c` in class two. Since `min V=0`, the maximum
is exactly `q`; the independent
full-state checker also obtains this value directly.

Begin with the affine target `3^t x+c`. For each of its first `t-1` inverse
odd blocks, apply the certified gap to the constant term. A symbolic state

\[
2^b3^s x+d,\qquad s\ge2,\quad d>0,\quad3\nmid d,
\]

is sent to

\[
2^{b+e}3^{s-1}x+I_e(d).
\]

Its integrality and unit constant are uniform in `x`. Telescoping (4) over
these blocks and then using (7) gives

\[
qk\le p(t-1)+W(c)+q=pt+W(c)+q-p.\tag{8}
\]

Equivalently, the nonnegative conversion rank at `s>=1` can be taken as
`ps+W(d)+q-p`, with terminal rank zero. For `s>=2` it decreases by at least
`qe`; at `s=1`, (7) pays the remaining inverse block. The prescribed
remaining-depth coordinate `s` is the source of well-foundedness.

Maintain `0<d<2^b3^s`. Each inverse step preserves it because

\[
0<(2^e d-1)/3<2^{b+e}3^{s-1}.
\]

At termination this gives the source `2^k x+r` with `0<r<2^k`.
For an integral positive target `Y`, its integral predecessor
`z=(2^eY-1)/3` is odd and satisfies `T(z)=2^(e-1)Y`, followed by `e-1`
even steps to `Y`. Reverse the constructed block list. This proves the
affine identity, its odd count, and (1). The last affine target may be even,
so this is an exact shortcut-block statement, not an assertion that the
last exponent is the full valuation of an odd-only map.

For `x>=1`, all inverse affine endpoints are at least three. The intermediate
forward values are powers of two times such endpoints. The displayed
trajectories stay above one.

## 6. Scope toward the forward problem

This construction builds predecessors of an arbitrary target. It does not
show that the target reaches one. Its decreasing coordinate is the chosen
number of ternary factors still to invert; no such counter has been
constructed for the forward orbit of a supplied positive integer.

The new slope is still greater than two, and hence greater than
`log_2(3)`. The real multiplier allowed per inverse odd event is
`2^(25/12)/3>1`. Furthermore, the preceding packet's entropy-counting
obstruction applies even to larger same-prefix dictionaries: this interface
cannot become a universally contracting construction merely by optimizing
its finite table. No forward descent, all-input merger selector, positive
cycle exclusion, or resolution of Collatz follows from P1.
