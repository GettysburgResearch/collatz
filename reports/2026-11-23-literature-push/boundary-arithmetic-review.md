# Independent review: complete numerical separation for arbitrary packets

23 November 2026. Reviewer: `/root/actual_collision`.

**Verdict: VERIFIED for the all-parameter written family theorem at the
frozen hash below.** The theorem excludes integer closure throughout its
stated family. It does not classify arbitrary parity words or exclude
unrestricted nontrivial positive integer cycles.

## Frozen scope

- Target: `research/literature-push-20261123/arithmetic/FULL_NUMERICAL_SEPARATION.md`.
- SHA256: `91d0afa1661956f7d5a80a22fe3f731925f33b2dc05516dcf2c844e6c22bf044`.
- Base worktree commit: `a9b23dcee61a4b65a63aa4e7ca653d875a405037`.
- Claim scope: equations (1)--(25), primitive realization, complete
  polynomial gcd, full numerical prime-power bound, and the arbitrary-floor
  consequence under exactly the stated parameter hypotheses.
- The proof was reconstructed independently. The two-packet predecessor
  credit is retained; this review does not extend to an uninspected earlier
  PR or to a later version of the target.

## 1. Complete polynomial gcd

Pairwise coprimality of the packet indices implies that any two packet
binomials have exactly the `r`-th roots of unity in common. Their
squarefree lcm is therefore the displayed `H`, with degree `r(1+S)`.
All of its roots lie among the `L`-th roots of unity.

At a root belonging to only one packet, the geometric-sum evaluation is
`(N/n_i) zeta^(s_i)`, which is nonzero. At a common root other than one,
the alleged cancellation is

\[
\sum_i (N/n_i)\zeta^{s_i}=0.
\]

Fix a prime dividing one `n_i`. After reduction modulo a prime ideal
above it, every other coefficient vanishes, while this coefficient
and the root of unity remain units. That contradiction is valid for
arbitrarily many packets, composite indices, and arbitrary allowed
offsets. It is not a geometric claim that positive roots-of-unity sums
cannot vanish. At one the value is positive. Outside `H`, every term
vanishes. Thus the target determines the **whole** common root set,
with multiplicity one.

The reverse coefficient polynomial has the same common cyclotomic root
set. The within-block factor has all its roots at complex modulus two;
the roots of `F` have modulus `2^(a/b)>3`, so it supplies no hidden
common factor. Homogeneous substitution introduces no multiple roots.
The complete monic gcd and residual therefore have the stated forms.
In particular, the sign is `F_0(3)=-KR`, while `Q_0(3)=(Y-V)B>0`.
The exact carry identity (18) agrees with this sign convention because
`G(3)=D/(KR)>0`.

## 2. Primitive word and actual realization

The numbers of exceptional entries in the selected residue classes are
the distinct positive integers `N/n_i`. Any cyclic profile period fixes
each such class, hence is divisible by `r`. Within class `s_i`, its
quotient by `r` must be divisible by `n_i`; pairwise coprimality then
forces the full profile period `L`.

The within-block gaps are one and every block boundary gap is at least
two. Consequently a period of the odd-gap word must respect the blocks.
Periodicity of the boundary differences implies periodicity of `e_j`
itself: the putative shift difference is constant, and its full cyclic
sum is zero. This proves the least odd-gap period `bL`; a shorter binary
period would induce a shorter cyclic odd-gap period. Thus the least
binary period is `aL`.

All rotated carries are positive over the same positive odd denominator.
Their parities agree with the first prescribed bit, and they satisfy the
literal shortcut updates. This verifies a legal rational cycle, not just
a fixed point of an artificially prescribed real composition. The
modulo-`2^A` ordinary realization is also exact; choosing it above `C/D`
makes it descend after the finite word. Such a finite ordinary realizer
is not identified with the rational cycle.

## 3. Full numerical prime powers

The coprime-base strong-divisibility identity gives
`gcd(K R_i,K R_j)=K`; cancelling the common **integer** factor `K`
gives `gcd(R_i,R_j)=1`. Each `R_i` is also coprime to `XY`.
Modulo `R_i`, all numerator terms except its own packet disappear, and
that packet is a unit. Hence `gcd(B,R)=1`.

For a prime dividing `R`, the complete gcd of `KR` and `(Y-V)B` can
use at most the valuation in `Y-V`, since the valuation in `B` is zero.
For a prime not dividing `R`, it can use at most the valuation in `K`.
This proves `g|K(Y-V)` without assuming `K` and `R` are coprime. The
same calculation proves `R/gcd(R,Y-V)|q`, including primes shared
among all three factors.

The strict estimates `R_i>X^(r(n_i-1))`, `Y-V<Y<X`, and
`K(Y-V)<X^(r+1)` yield (10)--(11). Since `S>=3` and `r>=2`, the
surviving logarithmic fraction is at least one half. No factor-only
estimate replaces the complete residual denominator.

## 4. Arbitrary floors and exact remaining gap

The block-boundary recurrence yields lower and upper bounds `B_0` and
`2 B_0` by cyclic extrema. A block has at most one initial halving;
its odd steps increase the value, and its final halvings terminate at
another boundary value at least `B_0`. Every rational shortcut state
therefore stays above `B_0/2`. Upper continued-fraction approximants
to `log_2 3` make that floor unbounded while retaining the parameter
inequalities. This remains a rational-cycle statement.

The final global boundary is correctly stated: general coefficient
profiles need not decompose into pairwise-coprime packets with unit
surviving residues. No argument in this packet supplies that missing
reduction, and no unrestricted Collatz conclusion follows.

## 5. Independent finite controls and formal scope

The separate reviewer script
`research/literature-push-20261123/boundary/review_packet_arithmetic.py`
was run by:

```text
python -B research/literature-push-20261123/boundary/review_packet_arithmetic.py
```

Its complete output is
`reports/2026-11-23-literature-push/boundary-arithmetic-controls.json`.
All four selected controls passed. They reconstruct the entire binary
word and its least period, the uncancelled carry, every rational and
ordinary shortcut step, the block recurrence and floor, and the
complete integer gcd. Two controls additionally compute the direct
polynomial gcd over `QQ`, with cancelled degrees 16 and 88. Cases with
three and four packets include nonconsecutive offsets and unused
residue classes. Finite controls do not prove the all-parameter theorem.

The specific control `a=4,b=2,r=2`, periods `[5,2]`, offsets `[0,1]`
has

\[
v_5(K)=2,\quad v_5(R)=1,\quad v_5(Y-V)=1,
\quad v_5(g)=1,\quad v_5(q)=2.
\]

It therefore exercises the shared prime-power case rather than only
coprime denominator pieces.

The literal definitions and theorems in
`rigidity/lean/PacketGCD.lean`, SHA256
`cabc44a642841ef376734fed131a708897fca3b5e36c1d571d45f191b8ce892e`,
were also read. They derive the packet-factor coprimality from the base
and index hypotheses and conclude the stated full numerical gcd
divisibility. The use of natural subtraction agrees with the present
specialization because all relevant differences and exponents are
nonnegative under (1)--(3). This reviewer did **not** perform an
additional Lean rebuild; the separate author and root build receipts
cover that execution. The full word construction, root-of-unity
classification, and prime-ideal step remain reviewed written mathematics,
as the target explicitly states.
