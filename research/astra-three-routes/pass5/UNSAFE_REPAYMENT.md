# Route 3 — a total guarded repayment rule through arbitrarily many unsafe switches

**Status: PROPOSED pending independent mathematical review.** The proof below
handles an unbounded family of actual mode switches using the SAME rank R,
not another infinite family of aligned single modes. Its guard is decidable
and its certified block is total whenever the guard holds. The guard does
NOT cover all positive integers. No global rank or Collatz proof is claimed.

Use A,R,G,U from [RANK_MOMENTS.md](RANK_MOMENTS.md). An unsafe source means
4R(A(n))>R(n); it need not have a rank increase on that particular edge.

## 1. Exact two-mode arithmetic

Let v=111010, split as 1110 | 10. Its affine map is

    F(n)=(81n+73)/64=alpha+(81/64)(n-alpha),
    alpha=-73/17.

The rational fixed point is negative and is used ONLY to compute finite
ordinary cylinders. At alpha the active modes are3 then1: after1110 its value
is beta=-103/17, then10 returns it to alpha. Define Z(n)=17n+73; exactly,

    Z(F(n))=(81/64)Z(n).

The finite word v^K is realized by a positive ordinary n if and only if
2^(6K) divides Z(n). This is ordinary parity-cylinder bijectivity, also proved
by observing that the two next-bit lifts have opposite next parities.

If v2(Z(n))=6K, the endpoint s=F^K(n) is even, because Z(s) is odd. During
the K cycles, the active A-modes are exactly3,1,3,1,...,3,1, each with one
copy: the next active mode differs, and the last one ends at an even state.
This checks A-maximality, rather than merely replaying a nonmaximal word.

## 2. T-A3-1101 — exact ranks along a fully unsafe growing phase

Impose n>=11 and n=10 mod243, equivalently n=alpha mod3^5. At every cycle
boundary s_j=F^j(n) within the legal prefix,

    R(s_j)=(s_j-1)^2/9.                                 (1)

At the intermediate state t_j=(27s_j+19)/16,

    R(t_j)=(t_j+5)^2/9.                                 (2)

These formulas hold for all prefix lengths, not just a fixed number of cycles.
The ternary agreement with alpha gains four digits per cycle; agreement with
beta gains three digits on the first phase. At alpha,

    v3(alpha)=0, v3(alpha-1)=2, v3(alpha+5)=1,
    v3(2alpha+1)=1.

Thus only entries0,1,2 can minimize, and (1) is smallest for s_j>=11. At beta,

    v3(beta)=0, v3(beta-1)=1, v3(beta+5)=2,
    v3(2beta+1)=3, v3(z_3(beta))=4.

The four possible entries are therefore

    t_j^2, (t_j-1)^2/3, (t_j+5)^2/9, (11t_j+19)^2/81.

For t_j>13 the third is strictly smallest. The precision above freezes all of
these valuations, including the moving index3; no omitted infinite feature
can beat them, by the parent exact envelope formula. Positivity and s_j>=11
hold because F expands positive inputs.

The exact ratios are

    R(t_j)/R(s_j)=[(27s_j+99)/(16(s_j-1))]^2>1,
    R(s_(j+1))/R(t_j)=9(t_j-1)^2/[16(t_j+5)^2].          (3)

For t_j>13, the second lies strictly between1/4 and9/16. Thus EVERY one of
the first2K sources lies in U. There are genuinely2K-1 mode changes inside
this unsafe phase; it is not one long repeated A-mode.

Moreover F^K(n)-1>(81/64)^K(n-1), so

    R(F^K(n))>(81/64)^(2K)R(n).                         (4)

The temporary rank increase is unbounded in K, despite the decreasing halves
of each cycle. This also supplies the unsafe shadows used to test power-law
weights in RANK_MOMENTS.md. A fixed CRT cylinder of these conditions has
positive natural density, a fact about FINITE ordinary congruences only.

## 3. T-A3-1102 — a computable rule repays the entire phase

Here is a finite, directly evaluable guard and block selector on n>=11:

1. Require n=10 mod243.
2. Compute t=v2(17n+73); require t=6K with integer K>=1.
3. Compute s=F^K(n) by exact rational-affine arithmetic; the divisibility
   above guarantees a positive ordinary integer. Set L=v2(s).
4. Require L>=K+4; output m=s/2^L.

Every operation terminates for every input; a failed guard returns UNRESOLVED,
not an instruction to search indefinitely. On success this is exactly2K+1
A-modules with words

    (111010)^K 0^L,

and

    R(m)<R(n)/4.                                        (5)

### Proof of repayment

Writing rho=81/64 and -alpha=73/17<5,

    m=[rho^K(n+73/17)-73/17]/2^L
      <(81/128)^K(n+5)/16 <(n+5)/16.

For n>=11, (n+5)/16<(n-1)/6. Hence R(m)<=m^2<(n-1)^2/36=R(n)/4,
using (1). The final even module is itself safe, because its starting rank
R(s)>R(n). Earlier2K sources are all unsafe by (3). Any actual visit to1
already proves convergence and may be killed early; these guarded prefixes
in fact remain positive with the displayed terminal formula.

The total shortcut clock is6K+L. Since K<=log_2(17n+73)/6 and
s<rho^K(n+5), L<=log_2 s, it is O(log n), with absolute constants. The number
of A-modules is unbounded over the guard. This lies outside the earlier
obstruction for a uniformly bounded number of A-like run modules.

### Nonvacuity for EVERY parameter, not just observed inputs

For every K>=1 and L>=K+4, the word (111010)^K 0^L followed by an odd endpoint
bit gives one residue modulo2^(6K+L+1). Combine it with n=10 mod243.
CRT supplies infinitely many positive sources n>=11. The terminal odd bit
makes L exact; the even state before halving makes v2(17n+73)=6K exact.
Every one of these ordinary sources satisfies (1)-(5). The source changes
with K, so this is not an extracted infinite periodic orbit.

Examples (the checker reconstructs all ranks exactly):

    K=1,L=5: n=236935 -> m=9371;
    K=2,L=6: n=115399495 -> m=2888245.

The second example passes through four unsafe sources before the final safe
halving module. At arbitrary K, formula (4) allows arbitrarily large prior
rank increases and arbitrarily many unsafe switches, while(5) uses one common
rank before and after the whole block.

## 4. End-to-end attempt and the still-missing coverage theorem

A total selector assigning EVERY n>=2 either a proved-convergent core case or
a finite physical/merging block to strictly smaller R would prove Collatz by
well-founded induction on the nonnegative integer R. Such a selector may use
unbounded blocks, provided their totality is proved. Different local scalar
ranks cannot be combined by assumption; all blocks here use R.

This guard provides a new all-parameter part of such a selector, not the whole
selector. Inputs such as3,7,9 fail it, and no claim is made that every other
trajectory eventually enters it. A finite core can handle these examples,
but does not prove coverage of all larger failures. The earlier one-edge
normalizer and safe-state exit procedure likewise have explicit unresolved
outputs. Declaring those outputs convergent is the first unsupported inference
in the attempted full rank proof.

The useful improvement is constructive: the prior unsafe obstruction is not
merely renamed. A definite, computable unbounded switch family is now repaid
under an exact ordinary-source guard. The remaining task is a recursively
closed collection of complementary guards or lower-rank merging diagrams,
with proved termination of the guard selection itself.

The neighboring PR #91 used distinct unbounded repayment families for its
fixed-section rank. That motivation is credited; neither its family nor its
rank is imported as a theorem here. No broad external priority claim is made
for specifying numerically descending finite words. The new object is the
common-R, fully-unsafe-prefix contract and its intrinsic exact selector.
