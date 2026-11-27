# Closing checks on the two missing global steps

These were the final focused challenges of the three-hour sprint. They
extend the written proposal and its finite controls. They add no Lean
declaration and do not prove universal convergence.

## An arbitrary common prefix still cannot rescue one protected swap

The two-block exclusion extends to any common physical shortcut prefix.
Suppose distinct positive integers execute the same finite prefix, followed
by the same two complete blocks in opposite orders, and reach a common
odd terminal \(z\). If the first entrance is \(x\), then necessarily
\(3(z+1)<x+1\). The prefix has no length bound and only the original
trajectory has the floor hypothesis in the contrapositive statement.

If the prefix contains \(p\) odd departures and has physical length \(H\),
the difference \(\delta\) between its two ordinary outputs satisfies
\(2^H\delta=3^p(x'-x)\). It is nonzero and divisible by \(3^p\). Meanwhile
shifted height is multiplied by exactly \(3/2\) at an odd step and
decreases at an even step. Combining this with the two actual reset
corrections and the terminal floor bounds the same transposition formula
from above. The resulting finite reduction has at most three for the
smaller tail ascent, 28 for the larger, 26 prefix odd departures and 38
total tail reset depth. Of the resulting tuples, 480,300 pass the gain
constraint. None has the required ternary divisibility.

Root reconstructed those inequalities. A separate reviewer evaluated the
direct rational difference on every eligible tuple, independently of the
author's integer-valuation checker. Both Python modes reproduce the
entire saved control. This finite exhaustion is not a new Lean kernel
certificate.

A common suffix can be canceled because its affine map is injective.
The theorem then applies when the floor holds immediately after the swap.
A floor only at the end of the suffix is insufficient: the explicit
sources 19,806,321 and 19,806,293 merge at 174,079 after the opposite orders
of \((1,1),(1,7)\), then both reach 7,528,747 after \((11,1)\). They have
already dropped below the required floor at the merger. Multiple
simultaneous word changes remain outside the theorem.

[Full proof](defects/PREFIX_SWAP_EXCLUSION.md) ·
[exact control](../../reports/unconventional-20261126/PREFIX_SWAP_CONTROLS.json).

## Exact gate telescoping exposes the required lower bound

Let \(A_N=H_{N-1}\|J_N\|_1\), let \(G_N=H_{N-1}J_N(N)\), and let
\(r_N\) be the surviving weight from \(N\) to its first strict upcrossing,
zero if it repeats first. Routing the old gates to the next height and
adding the new source gives exactly

\[
 A_{N+1}=A_N+r_N/N-(1-r_N)G_N,
 \qquad
 H_{X-1}-A_X=\sum_{N<X}(1-r_N)(1/N+G_N).
\]

Positivity bounds the sum by the harmonic total. Vanishing needs the
opposite asymptotic inequality, attaining the entire harmonic total along
a sequence. Under the pinned distinct-path reciprocal estimate, all
losses at odd heights and at heights \(6\bmod8\) together have finite
sum. Therefore gate losses on just \(2,8,20\bmod24\) would have to supply
at least \((5/8-o(1))\log X\) along a vanishing sequence. We have no such
lower bound.

For a hypothetical escaping core ray, its record-to-record survival
products multiply to a positive number under the stated source input.
Its own record losses are summable; their normalized gate contribution
vanishes on every sequence. Thus selecting a favorable height scale does
not remove the unresolved future of the core. The binary comparison
graph in the earlier note retains positive gate mass despite finite-core
tightness. Its branches differ from Collatz, so the remaining congruence
information cannot be discarded.

The recurrence is elementary. The summability and charge interpretation
are source-qualified. A separate exact-rational calculation checked 158
successive finite-height identities, but no finite check proves the
missing logarithmic lower bound.

[Derivation and exact residue classes](trace/HEIGHT_GATE_TELESCOPING.md).

## What full cycle closure actually forces on a common factor

On an ordinary cycle put \(b_* =\gcd_j b_j\), \(M=2^{b_*}-1\),
\(T=\sum_j t_j\), \(B=\sum_j b_j\), and
\(D=2^{T+B}-3^T\). Let \(g\) be the gcd of the odd parts of all shifted
block entrances \(Y_i\). The reset-divisor identity gives \(g\mid M\).
Unrolling one lap at any boundary shows \(M\mid D Y_i\), because every
shifted correction contains \(2^{b_j}-1\). Taking the gcd over boundaries
and removing its power of two gives \(M\mid Dg\). Consequently

\[
             M/g\mid \gcd(M,D)=\gcd(M,3^T-2^T).
\]

This accounts for all prime powers in this necessary common-factor
allocation. If \(b_*=1\), however, \(M=1\) and it is vacuous. Even when
\(M>1\), it controls shared factors rather than relative squareclasses.
Indeed the span of \([Y_i/Y_0]\) has dimension differing from the shifted
rank by at most one, and is invariant under multiplication of all \(Y_i\)
by any common rational factor. Removing the determinant or the common
divisor therefore does not by itself bound this rank. A new argument
must constrain the different shifted carry ratios on the **exact** closed
orbit. Arbitrarily precise endpoint congruences do not supply equality.

[Divisor transport](defects/RESET_DEPTH_RATIOS.md) ·
[shifted rank criterion](defects/SHIFTED_SQUARECLASS_CLOSURE.md).
