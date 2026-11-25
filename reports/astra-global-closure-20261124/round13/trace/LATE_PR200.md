# Late review of PR200's ordinary trace onset

**Verdict VERIFIED as implications of the stated source inputs I and II.**
Reviewed PR200 at 8e6add443b13acbcfd553676898c120183f07377, file
research/regularity-rigidity-20261124/global-trace-20261125/TRACE_ONSET.md,
Git blob b0dda8ec84f31bfcfceeeaa9e17ca0469d986975. The intake copy
has one additional final newline; removing that byte reproduces the
pinned Git hash. The cited primary manuscripts state the canonical
ordinary trace formula and the first-hit bounds, and the weak
$L^2$ tail and finite-cylinder energy respectively. These external
analytic results were checked at statement level only. No upstream
code or proof formalization was compiled in this review.
[Frozen PR200 note](https://github.com/GettysburgResearch/collatz/blob/8e6add443b13acbcfd553676898c120183f07377/research/regularity-rigidity-20261124/global-trace-20261125/TRACE_ONSET.md) · [Weaver, paper 12 v1, §§7–8](https://rstation.ai/problems/collatz/papers/12) · [Weaver, paper 146 v1, (1), (2a)](https://rstation.ai/problems/collatz/papers/146)

* For escape, nested predecessor sets retain a fixed positive density
  under I, and the canonical formula then gives $h(a_i)\gg_{a_0}a_i$.
  First crossings supply one site in every sufficiently large octave.
  Counting full ternary residues up to $3^K\le X$ and applying
  Jensen proves the opposing early second-moment bound via II.
  The conclusion compares a limit at each fixed ordinary target with
  a truncation on a moving target. It provides a necessary delay under
  escape, not an upper onset at any exceptional integer.
* For a fixed clock $D$ and odd depth $k$, each integral carry is
  determined by the word and identifies the word: after subtracting
  $3^{k-1}$ from the carry, its binary valuation recovers the last
  exponent, with $k=1$ supplied by $D$. The permitted carries for
  one terminal are in one class modulo $3^k$ in an interval of length
  at most $2^D((3/2)^k-1)$. Multiplying the lattice count by
  $3^k2^{-D}$ bounds this clock's trace. The geometric tail beyond
  $8k$ costs at most $[6(3/4)^8]^k$. Summing and taking the Cesàro
  mean gives $A_K(a)\ll(3/2)^K$ independently of II. To reach a
  fixed fraction of the limiting trace **along the hypothetical
  escaping ray** still uses I for $h(a_i)\gg_{a_0}a_i$.
* At an actual periodic target, first hits partition later hits by
  the number of complete laps. Each lap multiplies inverse weight
  by the same $\lambda_a<1$. Input I and
  $1-\lambda_a\le p/(3s)$ give the displayed ratio
  $A_K(a)/h(a)\ll(p+K)/s$. An order-$s$ onset lower bound follows
  in the specified $p=o(s)$ branch when a fixed trace fraction is
  attained. Excluding that branch still requires a contrary uniform
  upper onset and a treatment of any remaining finite cases.

**Relation to round thirteen.** Write $N$ for the size of a selected
mixed-cell packet in the round-thirteen original-source band. Its
contribution to PR200's exact-depth density at the common gate $a$
is precisely $N3^k2^{-S}$. The integer lattice upper bound
$N\le1+C_*2^H/(3^k2^h3^J)$ gives
$$
 N3^k2^{-S}\le3^k2^{-S}+C_*\,2^{H-S}/(2^h3^J).
$$
At the later endpoint $q_i$ the contribution of the same packet at
the balanced row is $N(3/4)^b$. Both are exponentially small at the
reported long-pad scales $S\asymp b$, $k,H=O(\log b)$, even though
the packet can occupy a power of the width in **integer count**.
Other inverse sources and other clocks can contribute to PR200's
density. Thus neither the selected-row lower count nor its
known-convergent finite controls supply fixed-fraction early onset.
The convergent controls change the gate and their carry threshold
tends to zero. Conversely, the onset estimates do not bound the
later unrestricted density at the fixed bad gate or produce a
deficit of raw sources at the selected moving balanced rows.
Universal convergence is still open.
