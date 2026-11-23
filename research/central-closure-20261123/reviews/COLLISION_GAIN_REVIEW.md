# Independent review of the all-clock collision and height bounds

Date: 2026-11-23. Reviewer lane: `nov23_surgery`.

**Verdict:** the written finite inequality (12), critical-exponent
collision bound (16), and bounded-height duration bound (21) pass this
independent review. They retain one actual source and the stated clock.
The proposed closing upper bound remains unproved.

## Reviewed snapshot

| File in `nov23_escape/` | SHA256 |
|---|---|
| `COLLISION_LOGARITHMIC_GAIN.md` | `5a71d0f241bf9ac60b8125909b010d32d6b1d1716cb6b991ff8d3babf58fd017` |
| `check_collision_budget.py` | `df04d7e7f631e9bea613027f8120e6167e054aff4ba2059f44b2f27836d2d29e` |
| `DistinctWordBudget.lean` | `2b5c3d9e4ccc96f9923c33bf38feb9670810da87ae08bbe33cf54d5dd126eb54` |
| `verification.json` | `2c744f96b9296df99893e11fce5d5de9dae83dc37c21444b0d3fe986afb6ae8f` |
| `lean-check.log` | `20a55375066d28b6a5f4b40a9d97164c8f3050165dc8b9af4fc71f948f554784` |

This review independently checks the written argument and reruns the
finite Python checker. It records the formal artifact but does not claim
a second independent Lean compilation or a formal proof of the harmonic
flow, stars-and-bars, or Stirling's formula.

## 1. Finite composition budget

For words of length $m$ with positive entries, total $s$ has capacity
$\binom{s-1}{m-1}$. Summing positive deficits and squared positive
deficits over all words gives exactly

\[
Q_1(K,m)=\binom K{m+1},\qquad
Q_2(K,m)=\binom K{m+1}+2\binom K{m+2}.
\]

The second identity follows from the difference of consecutive squared
deficits, together with the first identity and the ordinary hockey-stick
sum. Empty ranges and $K\le m$ produce zero as required.

For a probability law on distinct support words, the mean-cost bound
implies $K-B\le\sum p_w(K-S(w))_+$. Cauchy--Schwarz compares that square
with $\sum p_w^2$ times the **unweighted** squared-deficit count. That
count is at most $Q_2$. No expectation under a different word law enters.
The denominator is positive whenever a nonempty length-$m$ word law has
$K>B$, since then $B\ge m$ and $K\ge m+1$.

## 2. Exact original-source and inverse-clock transfer

For the actual past windows ending at $q_m,\ldots,q_M$, each gap is
counted at most $m$ times. This gives precisely the stated mean bound
$mA_M/(M-m+1)$.

The affine identity determines $q_J$ modulo $3^m$ from its actual length
$m$ word. Grouping word masses by endpoint residue increases the sum of
squares. The original window has $M+1$ points and the shorter window has
$M-m+1$, so measure domination supplies the square of the exact ratio
displayed in (8).

For the inverse law, deterministic forward iteration and injectivity of
the original orbit imply that the only root in the shifted root window
that can return to $q_j$ after $r$ inverse steps is $q_{r+j}$. The unique
retracing path has probability $v_j/v_{r+j}$. Thus the exact mass in (10)
and the lower domination by $v_0/C$ are correct for every integer
$r\ge0$. After residue projection, monotonicity of each nonnegative
squared coordinate gives (12).

In particular this proof never subtracts a total-variation error from an
exponentially small collision probability. It needs no uniform rate for
the earlier capacity defect and has no hidden condition $r=o(M)$.

## 3. The critical exponent and the square-root factor

The real product telescope is exact. On an injective prefix, the source
states are distinct positive integers, so their reciprocal sum is bounded
by the first $M$ terms of the harmonic series. This proves (15) with a
constant depending only on the fixed starting height.

For fixed $0<T<\infty$ and $m^2\le TM$, expanding the denominator
$M-m+1$ gives

\[
B_{M,m}=\ell m+O_{q_0,T}(1).
\]

The boundary term is bounded by a constant times $m^2/M$, while the
reciprocal-state correction is bounded by a constant times
$m\log(M+1)/M$. The latter tends to zero uniformly over the stated
precision range. Choosing an integer $K=\ell m+O(1)$ at least one above
this mean is therefore legitimate.

For fixed integer offsets, Stirling's bounds give
$\binom K{m+j}=O(m^{-1/2}\exp(m\Phi(\ell)))$, for $j=1,2$.
The fixed offsets alter the multiplicative constant, not the power of
$m$. Bounded $m$ can be absorbed in the same constant. Also
$(M-m+1)/(M+1)$ is uniformly bounded below for sufficiently large $M$.
Substitution into (12) therefore gives exactly the factor $\sqrt m$ in
(16). This is a collision/Renyi-2 improvement; it has not been promoted
to a Shannon-entropy improvement.

## 4. The ordinary bounded-height duration bound

Choose $m=\lceil\log_3 H\rceil$. Equal actual past words imply equal
endpoint residues modulo $3^m$. Since all endpoints are distinct and
lie in $[1,H-1]$ with $3^m\ge H$, their length-$m$ past words must be
distinct. This is the key ordinary-height input missing from a generic
word law.

Injectivity also gives $N+1\le H$ and the telescope gives
$A_N\le\ell N+O(\log H)$ with absolute constants. If
$N\ge(\log H)^2$, the mean word cost is $\ell m+O(1)$ after discarding
the first $m-1$ endpoints. The distinct-word deficit bound and the
single-binomial Stirling estimate then give

\[
N-m+1\ll H^\theta/\sqrt{\log H}.
\]

The discarded $O(\log H)$ endpoints, the case $N<(\log H)^2$, and
bounded $H$ are absorbed by an absolute constant. This proves (21).
The inversion to (22) is valid because $H\ge N+1$, so the logarithmic
factor on its right can be replaced by $\log(N+1)$ before taking the
$1/\theta$ power.

The result bounds the duration of a segment contained below height $H$.
It does not bound the total number of visits below $H$ with arbitrarily
large intervening excursions. The note correctly preserves this
distinction.

## 5. Execution and minor presentation observations

`python check_collision_budget.py` passed independently, reporting:

- 1,944 composition-identity cases;
- 2,758 actual word windows;
- 940 distinct-word height cases;
- positive odd sources from one through 511, at most 256 odd steps.

Those computations check indexing, residue projection and finite scaling,
not the asymptotic theorem or existence/nonexistence of an escape.

Two non-mathematical observations were sent to the author. Writing
$0<T<\infty$ explicitly would make Theorem 3's parameter range clearer
than merely $T<\infty$. The reviewed Python version uses assertions;
if the checkpoint is meant to remain a checking program under
`python -O`, these should be explicit failure checks, as in the cycle
lane. Neither issue changes the reconstructed written proof.

The first outstanding mathematical line remains the same-law arithmetic
upper estimate (20). This review establishes no such upper bound and no
full Collatz conclusion.
