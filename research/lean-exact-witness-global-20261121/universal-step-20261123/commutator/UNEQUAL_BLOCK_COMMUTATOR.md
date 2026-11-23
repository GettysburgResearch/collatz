# A common integer lattice excludes cycles in contracting block dictionaries

23 November 2026. **Written all-period theorem for a specified block
dictionary. Full Collatz remains OPEN.** This is the coordinating extension
of the equal-shape argument in [BLOCK_CARRY_CAPACITY.md](../cycles/BLOCK_CARRY_CAPACITY.md).
It permits different block lengths and different odd counts. It retains
the complete cycle equation and uses an ordinary integer lattice that a
positive rational cycle need not occupy.

No assertion is made that every possible Collatz cycle admits a dictionary
satisfying the hypotheses below. The theorem and the sparse-defect
corollary are written mathematics; they are not additional declarations
in `BlockMixture.lean`.

## 1. Objects and the all-word statement

A finite binary shortcut word `w_i` has length `A_i`, odd count `p_i`, and
complete carry `C_i`, defined by the literal identity

\[
 Q_i x'=P_i x+C_i,\qquad Q_i=2^{A_i},\quad P_i=3^{p_i}.
 \tag{UC1}
\]

Assume every dictionary block is nonempty and coefficient-contracting:

\[
 A_i\ge1,\qquad Q_i>P_i,\qquad d_i=Q_i-P_i>0.
 \tag{UC2}
\]

For now assume each block contains an odd bit, so `p_i>=1`. Section 5
explains the harmless extension allowing pure-even blocks. Define the
signed cross-carry quantities

\[
 E_{ij}=d_iC_j-d_jC_i.                                  \tag{UC3}
\]

Their sign orders the real fixed points: `E_ij>0` exactly when
`C_j/d_j>C_i/d_i`. Let `s=2^u3^v`, with `u,v>=0`, divide every `E_ij`.
The choice `s=1` is allowed; the largest available value is the 6-smooth
part of the gcd of the nonzero cross-carry quantities.

**Theorem UC-D (arbitrary contracting dictionary).** Suppose that for
every ordered pair with `E_ij>0`,

\[
 \boxed{E_{ij}<s\,(Q_iQ_j-P_iP_j).}                     \tag{UC4}
\]

Then every closed ordinary integer path formed by an arbitrary finite
concatenation of these blocks has **constant boundary state**. There is
no restriction on the number of blocks, their order, or their frequencies.
Each block used on that constant path fixes the same integer `m`, so
`d_i m=C_i` for each used label.

Consequently, if no block has a positive integer fixed point, the dictionary
admits no positive integer cycle at all. If every positive integer fixed
point is independently known to lie in the standard Collatz basin, the
dictionary cannot realize a nontrivial positive Collatz cycle.

The statement about constant boundary states must be retained: a dictionary
containing a complete word for the standard cycle can certainly have a
constant boundary path. Internal shortcut states are not asserted constant.

## 2. Complete-cycle integrality forces one common residue

Every `d_i=2^{A_i}-3^{p_i}` is coprime to six. Fix a dictionary label `0`.
There is a residue `a` modulo `s` with

\[
 d_0a\equiv C_0\pmod s.
\]

Since `s|E_0i`, cancellation of the unit `d_0` gives

\[
 d_i a\equiv C_i\pmod s\quad\hbox{for every }i.         \tag{UC5}
\]

Consider a closed boundary path `x_0,...,x_N=x_0`, with labels
`i_0,...,i_(N-1)`. Subtract the common residue in each actual edge:

\[
 Q_{i_j}(x_{j+1}-a)\equiv P_{i_j}(x_j-a)\pmod s.
 \tag{UC6}
\]

Multiply through the complete cycle. This gives, at every cyclic cut,

\[
 D\,(x_j-a)\equiv0\pmod s,\qquad
 D=2^{\sum_j A_{i_j}}-3^{\sum_j p_{i_j}}.               \tag{UC7}
\]

Here `D` is the **whole numerical cycle denominator**. It is positive by
(UC2) and coprime to six. Therefore it is invertible modulo `s`, and

\[
 \boxed{x_j\equiv a\pmod s\quad\hbox{at every boundary}.} \tag{UC8}
\]

No division by a power of two modulo an even modulus has been used: the
intermediate equations are composed before the unit `D` is cancelled.
This avoids a false branchwise-invertibility argument.

## 3. The minimum corner pays a full two-block denominator

Suppose the closed boundary path is nonconstant. Let `m` be its minimum.
Some edge enters `m` from a larger boundary value and some edge exits `m`
to a larger value. They need not be adjacent in the list if the minimum
occurs on a plateau. Call their labels `i` and `j`.

By (UC8), write those two neighboring values as

\[
 x_{\rm in}=m+s\alpha,\qquad
 x_{\rm out}=m+s\beta,\qquad \alpha,\beta\ge1.
\]

The two literal edge equations are

\[
 d_i m=C_i+P_i s\alpha,\qquad
 C_j=d_j m+Q_j s\beta.                                 \tag{UC9}
\]

Eliminate the same ordinary integer `m`:

\[
 \begin{aligned}
 E_{ij}
 &=s\bigl(d_iQ_j\beta+d_jP_i\alpha\bigr)\\
 &\ge s(d_iQ_j+d_jP_i)\\
 &=\boxed{s(Q_iQ_j-P_iP_j)>0}.                          \tag{UC10}
 \end{aligned}
\]

This contradicts (UC4), proving UC-D. The proof needs neither a
probabilistic independence assumption nor a sum of local energy drops.
The restrictive input is the common lattice supplied by the complete
ordinary closure.

## 4. Two unequal blocks, smooth factors, and the equal-shape theorem

For two blocks with distinct fixed points, orient them so

\[
 \delta=d_1C_2-d_2C_1>0,
 \qquad \delta=2^u3^v\delta_*,\quad\gcd(\delta_*,6)=1.
\]

**Corollary UC-2.** If both labels occur in a closed ordinary integer path,
then

\[
 \boxed{\delta_*\ge Q_1Q_2-P_1P_2.}                   \tag{UC11}
\]

Indeed, a constant path cannot use two different fixed points. Apply UC-D
with `s=2^u3^v` and its contrapositive. Thus a 6-smooth nonzero
cross-carry quantity excludes every mixed cycle, at every concatenation
length. More generally its part coprime to six must pay the complete
two-block denominator.

For equal shapes `P_1=P_2=P`, `Q_1=Q_2=Q`, put `d=Q-P` and
`Delta=C_2-C_1>0`. Since `d` is coprime to six,

\[
 \delta_*=d\Delta_*,\qquad
 Q^2-P^2=d(Q+P).
\]

Consequently (UC11) becomes exactly

\[
 \Delta_*\ge Q+P,
\]

recovering the all-period equal-shape theorem. That lane additionally
proves a sharper period-dependent statement involving
`gcd(G,Q^N-P^N)`; that refinement is not silently asserted here for unequal
shapes.

If every cross-carry quantity in a dictionary is zero, all fixed points
are the same. In that separate case every block is a strict contraction
toward that common fixed point, so a closed real path is already constant.
There is no need to define the smooth part of zero.

### Strictness is necessary

The abstract affine maps

\[
 f_1(x)=3x/4,\qquad f_2(x)=(3x+23)/8
\]

have the integer cycle `4 -> 3 -> 4`. Their cross-carry quantity is `23`,
and `4*8-3*3=23`: equality in (UC11) is possible. These maps are an
algebraic control, **not a pair of actual Collatz parity blocks**; in
particular their first carry is not the carry of a word containing an
odd bit. This control checks the sharp boundary of the affine argument
without claiming a Collatz counterexample.

## 5. Pure-even blocks and sparse defects

The dictionary theorem also allows blocks with `p_i=0`, provided the
closed path uses at least one block with `p_i>0`. Choose that block for
label `0` in Section 2. Its `d_0` is a unit modulo `s`; (UC5) still follows
for every other block, even when that other `d_i` is divisible by three.
The complete denominator in (UC7) remains a unit modulo six because the
total odd count is positive. The minimum-corner proof is unchanged.
An all-pure-even positive closed path is impossible directly.

Here is an unbounded-length consequence beyond repeating a fixed
equal-shape dictionary. Let `u` be any fixed coefficient-contracting
Collatz word and let `t` be any nonempty Collatz word. Write their data
as `(P,Q,C)` and `(R,S,B)`, and suppose their fixed-point cross expression

\[
 E=(Q-P)B-(S-R)C
\]

is nonzero. The word `u^k t` has

\[
 P_k=RP^k,\quad Q_k=SQ^k,\quad
 C_k=R C\sum_{j=0}^{k-1}Q^{k-1-j}P^j+Q^k B.
\]

Its cross expression with `u` is exactly

\[
 \boxed{(Q-P)C_k-(Q_k-P_k)C=Q^kE.}                    \tag{UC12}
\]

Thus the part coprime to six is the fixed integer `|E|_*`, independently
of `k`, whereas the complete two-block denominator is

\[
 QQ_k-PP_k=SQ^{k+1}-RP^{k+1}\longrightarrow+\infty.
\]

For every sufficiently large `k`, the word `u^k t` is contracting and
this denominator exceeds `|E|_*`. UC-2 excludes every mixed closed
integer path over the two-word dictionary `{u,u^k t}`. Both the block
length `k` and the number/order of blocks in the candidate cycle are
unbounded. This conclusion is for each such fixed `k`; it does not
silently combine all values of `k` into a new infinite dictionary.

## 6. What is still needed for full cycle exclusion

The theorem can be applied directly to actual whole-block cycles and to
finite dictionaries with computable carries. It does not show that a
hypothetical cycle can be decomposed into contracting blocks whose
cross-carry quantities satisfy (UC4). Allowing an expanding block removes
the positive `d_i` factors that make (UC10) a lower bound. The original
one-step odd branch is expanding, so applying UC-D to the two ordinary
one-step branches would violate its hypotheses.

Constant boundary paths also require the full one-block divisibility
test `d_i|C_i` and physical replay. Neither arbitrary-word coverage nor
unrestricted one-block exclusion is proved here. These are the precise
remaining interfaces, not assumptions hidden in the dictionary theorem.
