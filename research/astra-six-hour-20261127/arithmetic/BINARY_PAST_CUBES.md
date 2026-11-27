# Exact energy extremizers in the binary Collatz past within ratio eight thirds

The exponent \(\kappa=\log_2 6\) in PR201's hereditary energy bound is attained on the **actual ternary binary-predecessor tree**, even by sparse sets of fixed-total words in a physical band of ratio below \(8/3\). For arbitrarily large lengths \(n\), one can take
\[
             k=(2-\log_2 3)n+O(1),\qquad N=2^k .
\]
The \(N\) words have distinct endpoint residues modulo \(3^n\). Their raw affine numerators and their ternary endpoint residues both have exactly \(6^k=N^\kappa\) ordered four-sum collisions. Freezing any subset of the \(k\) choices preserves the exact formula with the remaining dimension.

There are two different physical realizations.

- Every word in a family can occur, on disjoint intervals, in **one finite positive ordinary trajectory** with all its intermediate odd values, including those between the intervals, in a common band of ratio strictly below \(8/3\). This realizes the raw and modular collisions in a single trajectory.
- The actual terminal odd integers themselves can instead be chosen to have exactly \(6^k\) integer four-sum collisions, one arbitrary common odd residue modulo any prescribed power of two, and all their prescribed binary pasts in a common band of ratio below \(8/3\). This construction chooses the endpoints separately.

These statements concern finite trajectory segments. No ordinary cycle or infinite path in that band is supplied. PR201 proves the hereditary upper bound for arbitrary two-child ternary trees and for actual binary pasts, and records sharpness on the abstract class. PR200's bridge construction uses independent binary choices in ordinary numerator energies. The construction here locates sharpness at the exact exponent simultaneously for actual ternary endpoint residues and fixed-total words in one finite ordinary orbit. [PR201, ternary past energy](https://github.com/GettysburgResearch/collatz/blob/860a67dedc860adcd82b964958d91b9e21d610f1/research/six-hour-20261127/arithmetic/TERNARY_PAST_ENTROPY.md) · [PR200, free binary bridges](https://github.com/GettysburgResearch/collatz/blob/2346db2d49030ef385b73e1ee3e27dcbff86d2d9/research/six-hour-20261127/cycles/FOUR_BRIDGE_BINARY_CYCLE_BOUND.md)

## Two tile types fix the clock

Put \(\gamma=\log_2 3,\ \alpha=\gamma-1,\ a=2\gamma-3,\ b=2-\gamma\), so \(a+b=\alpha\). At a tile boundary let \(y=E_i-i\gamma\) be the total dyadic-clock discrepancy. Start at \(y=0\). If \(y\ge a\), append either \(12\) or \(21\) and subtract \(a\) from \(y\). If \(y<a\), append the single letter \(2\) and add \(b\). Thus the boundary value stays in \([0,\alpha)\), where it rotates by \(b\) modulo \(\alpha\). When a two-letter tile is open its intermediate discrepancy is either \(y-\alpha\ge-b\) or \(y+b<1\). Every prefix, with every mixture of swaps, has discrepancy in \([-b,1)\).

Stop at a boundary after \(n\) odd edges. If there have been \(k\) two-letter tiles the total clock is \(T=2n-k\), so \(k=bn+O(1)\). For a word \(w\) with prefix clocks \(E_i\) the ordinary affine numerator is
\[
             B(w)=\sum_{i<n}3^{n-1-i}2^{E_i}.
\]
Switching a tile at \(i\) from \(12\) to \(21\) changes only the term at \(i+1\). Its positive increment is \(L_i=2^{E_i+1}3^{n-2-i}\), independent of every other swap. Accordingly the raw numerators form an affine Boolean cube with these generators.

The \(3\)-adic valuations of the \(L_i\) are distinct and smaller than \(n\). Any nonzero signed sum of these generators with coefficients in \(\{-2,-1,0,1,2\}\) has valuation equal to the smallest generator valuation present. Consequently every modular four-sum equality is equality of the bit-pair sums separately at each free tile. A single bit admits six ordered solutions to \(\epsilon_1+\epsilon_2=\epsilon_3+\epsilon_4\), giving \(6^k\) solutions. They are literal integer equalities as well. The same reasoning with coefficients in \(\{-1,0,1\}\) proves all vertices distinct modulo \(3^n\). Multiplication by \(2^{-T}\) transfers the modular statement unchanged to the actual terminal residues.

## Physical realizations

The tile rotation has irrational angle \(b/\alpha\), since \(b/\alpha=1/\alpha-1\). Its nonnegative orbit meets the interior of every nonempty interval infinitely often. Each finite initial tile skeleton has a nonempty interval of intercepts realizing it: the initial intercept 0 has a right neighborhood, since none of its finitely many decision times lands on the threshold \(a=\alpha-b\), nor returns to zero after a positive number of steps. Thus the skeleton reappears on arbitrarily many disjoint blocks of the infinite schedule. Assign every free-bit pattern to one such occurrence, choose the other swaps arbitrarily, and truncate after the last required occurrence. This gives a single finite word, including all connecting edges, still obeying the same discrepancy bounds globally.

For any fixed finite word, the congruence \(3^m x+B\equiv2^H\bmod 2^{H+1}\), for its length \(m\), total \(H\) and numerator \(B\), specifies an ordinary odd source with that exact word. It admits arbitrarily large positive lifts. Equivalently the congruence makes the last state odd, and its reductions modulo successive clock powers make each preceding division and oddness exact. On such lifts the entire finite path, relative to its initial state, converges to \(2^{i\gamma-E_i}\) at edge \(i\). The largest to smallest ideal ratio is strictly below \(2^{1+b}=8/3\) by the finite discrepancy bounds. Take the ordinary lift sufficiently large to preserve that strict inequality.

For the separate endpoint construction let \(q=3^n\), prescribe any modulus \(2^u\), \(u\ge1\), and an odd endpoint residue modulo \(2^u\). Choose integer generators \(L_i'\) congruent to \(2^{-T}L_i\bmod q\) and zero modulo \(2^u\), all nonnegative. Choose an arbitrarily large odd base \(y_0\) with the prescribed dyadic residue and the unswapped word's terminal residue modulo \(q\). The integers \(y_0+\sum\epsilon_iL_i'\) form the required ordinary cube. Modular uniqueness again gives its exact integer energy. Each endpoint has its designated binary past, because the endpoint residue modulo \(3^n\) recovers the entire inverse word, and each inverse step of a positive odd unit with exponent one or two stays a positive odd integer. As \(y_0\) grows in its fixed congruence class the terminal ratios all tend to one. All the words have the same terminal discrepancy, so their normalized inverse paths have the same strict joint ratio bound as the finite forward family. This proves the second realization.

In particular a prospective sparse restriction bound \(E(A)\ll_\epsilon N^{2+\epsilon}+N^4/3^n\) fails already on these fixed-total local families for every \(0<\epsilon<\log_2(3/2)\). Indeed \(N<3^{n/2}\) eventually, so the right side is \(O_\epsilon(N^{2+\epsilon})\). A stronger energy bound for words conditioned on one *periodic integer orbit* must use information beyond the existence of all those words on one ordinary finite path of unrestricted height.

The [exact checker](check_binary_past_cube.py) uses integer comparisons to select the tiles. It checks 64 words of odd length 15 and common clock 24, energy 46,656 for their raw, modular and separate ordinary endpoint sets, and all 64 disjoint words on one 3,234-odd-edge integer trajectory of ratio below \(8/3\). [Replay output](../../../reports/astra-six-hour-20261127/arithmetic/BINARY_PAST_CUBES.json)
