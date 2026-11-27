# Consecutive mismatch quotients and the near-circuit bound through eight mismatches

The conclusion of [the five-mismatch theorem](NEAR_CIRCUIT_FIVE.md) holds with **eight** in place of five and with the same $\varepsilon=1/4096$. In detail, if a primitive positive rational cycle of large odd period $p$ satisfies $\sum_{i\ne j}(e_i-1)\le p/4096$ for some departure $j$, and if any proper odd rotation has at most eight mismatches, then its complete reduced denominator satisfies $q>2^{p/4096}$. For ordinary integer cycles this excludes all sufficiently long examples in the indicated class. The period onset is ineffective.

The argument uses consecutive native mismatches together. It permits either sign for every nonzero paired quotient $g_i$ in the preceding paper. The new arithmetic input below is that the expansion has no vanishing nonempty subsum on its right, including after separating the **final** payload into two terms. Earlier local constraints and their floating-point exploration for the near-circuit problem are due to Armstrong's project. [Prior near-circuit proposal and heuristic six-event boundary](https://github.com/stgoa/collatz/blob/d99505da4bc51849169cce0a7a46f0fce302afd0/areas/cycles/results/near-circuit-rotation-forced-relation/README.md)

## Native chains

Use the block notation of [the local inequality](NEAR_CIRCUIT_FIVE.md). At each selected post-mismatch choose either positive numerator $w_i$ from the actual pair $y_i,z_i$. There is a positive integer $c_i$, equal to $A_{i+1}$ plus the excess on the opposite side, such that
\[
 3^{L_i}g_i=2^{c_i}g_{i+1}+P_i,\qquad P_i=(2^{v_i}-2^{u_i})w_i .
\]
The integers $g_i$ and $P_i$ are signed nonzero odd numbers. Take consecutive indices $a,\ldots,b$, cyclically unwrapped, with length bounded by a fixed integer. Put $U_i=\sum_{a\le j<i}c_j$ and $V_i=\sum_{i<j\le b}L_j$. The exact identity is
\[
 3^{\sum_{a\le i\le b}L_i}g_a
   = 2^{U_{b+1}}g_{b+1}
       +\sum_{i=a}^b 2^{U_i}3^{V_i}P_i.                               \tag{1}
\]
The dyadic valuations of the compact right-hand terms are the strictly increasing integers $U_a,\ldots,U_b,U_{b+1}$. Each nonempty subsum has a unique least valuation and is nonzero.

One may instead split the last term into $2^{U_b+v_b}w_b$ and $-2^{U_b+u_b}w_b$. Include the negative left side temporarily, so the signed sum is zero. A proper nonempty vanishing subsum whose two last-date terms are taken together or omitted would give a proper vanishing subsum of the compact tuple, ruled out by choosing the side that omits the left side and using the distinct dyadic valuations. If the last-date terms are separated, choose the side omitting the terminal $2^{U_{b+1}}g_{b+1}$. This side contains precisely one pure last-date term, coprime to three. Every earlier payload and the left side is divisible by three because $L_b\ge1$. This side cannot sum to zero either. In particular every nonempty subsum of the split right-hand terms is nonzero; the full right side itself equals $3^{\sum L_i}g_a\ne0$.

Apply Evertse's Theorem 2 at $T=\{3\}$, precisely as quoted in [the local proof](NEAR_CIRCUIT_FIVE.md). In the compact version $\max|T_i|_3\ge1/(3D_b)$ by the valuation of the last payload. In the split version $\max|T_i|_3=1$. The ternary absolute value of the right-hand sum is at most $3^{-\sum L_i}$. Removing all powers of two and three costs at most $|g_{b+1}|$ for the terminal term, at most $2^{D_i}w_i$ per compact payload, and at most $w_b^2$ for the product at a split last date. The maximal ordinary term has logarithm $O_r(h)$ for a chain of at most $r$ mismatches, by the native height estimates in the local proof. Thus
\[
 \gamma\sum_{i=a}^b L_i+A_{b+1}
 \le \log_2\max(y_b,z_b)+\sum_{i=a}^b(\log_2 w_i+D_i)+o_r(h).         \tag{2}
\]
At the final date its cost may be replaced by $2\log_2 w_b$, or by the smaller of these two costs. This statement holds for all the positive rational cycles under consideration and all choices of endpoints. Uniformity uses fixed-length Evertse inequalities only. [Evertse, Theorem 2, p. 228](https://www.numdam.org/item/CM_1984__53_2_225_0.pdf)

## Certificates for six, seven and eight mismatches

Suppose $q\le2^{\varepsilon p}$ and the nonexceptional excess is at most $\varepsilon p$. Retain the sawtooth bounds and normalized times $t_i,r,l_i,z_i,z'_i$ in the five-mismatch proof. In a chain of cuts with **no interior exceptional comparison**, choose the smaller post-mismatch numerator at each date. A small-date compact cost is at most $p\min(z_i,z'_i)+3\varepsilon p+O(\log p)$. At an exceptional final comparison the split cost is at most $4\varepsilon p+O(\log p)$ since one post-mismatch numerator is $y_0$. The smaller modeled branch height is zero at each exceptional comparison. The terminal maximum is at most $p\max(z_b,z'_b)+2\varepsilon p+O(\log p)$.

For any chain of at most $r_0\le8$ cuts of this kind, (2) therefore gives
\[
 \max(z_b,z'_b)+\sum_{i=a}^b\min(z_i,z'_i)
      - l_{b+1}-\gamma\sum_{i=a}^b l_i
 \ge -(3r_0+3)\varepsilon-o(1).                                       \tag{3}
\]
Here $h=O(p)$ by the five-mismatch minimum argument. Since $27/4096<1/128$, the right side of (3) is at least $-1/128$ eventually. The two single-cut rows and the next spacing row from that proof have at least the same margin.

For $s=6,7,8$ there are respectively $5,6,7$ order types, specified by how many ordinary mismatches precede the comparison at $1-r$. The exact verifier uses the same rational bracket for $\gamma$. On each order type the maximum and minimum of the two branch heights are fixed affine expressions. The [18 nonnegative certificates](near_circuit_chain_duals.json) use (3), singleton rows, the shorter-lag bound, and next spacings. Each weighted sum with $1/128$ added to the physical rows, divided by its sum of integer weights, has maximum less than $-1/100$ on the entire lag-and-times unit cube at both rational endpoints. Interpolation in $\gamma$ for fixed variables preserves the bound. Thus no growing counterexample with these event counts exists. The [verifier](check_near_circuit_chains.py) uses rational arithmetic throughout. [Archived dual values](../../../reports/astra-infinite-descent-20261127/cycles/NEAR_CIRCUIT_CHAINS.json)

[Physical controls](check_mismatch_chains.py) replay both endpoint conventions, signs, ternary-unit bounds and every nonempty right-hand subsum of 100,456 chains in 574 native primitive positive rational cycles. These are finite checks of (1) and its hypotheses. They do not supply an effective constant in Evertse's theorem. [Native receipt](../../../reports/astra-infinite-descent-20261127/cycles/MISMATCH_CHAINS.json)
