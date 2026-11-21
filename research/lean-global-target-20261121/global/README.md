# Inverse pressure and the charged-reset attempt

**Status: unconditional finite identities and ordinary obstruction families;
the global closing estimate is OPEN.** This route attacks the arithmetic
moment rather than adding local return cylinders. It did not prove Collatz.

[Global/InversePressure.lean](../lean/Global/InversePressure.lean) compiles
with Lean 4.34.1 and warnings treated as errors. The formalization boundary
below distinguishes the checked finite statements from their analytic
interpretation.

## Exact quadratic pressure identity

Put
\[
I_a(x)=(2^a x-1)/3,\qquad V(x)=(x+1)(x+2).
\]
For every finite cutoff N and rational x,
\[
\boxed{\sum_{a=1}^N\frac{81}{16^a}V(I_a(x))
=3V(x)-3x^2\,4^{-N}-9x\,8^{-N}-6\,16^{-N}.}
\]
Lean checks the full identity, including its tails, in
**partial_restored_identity**.

The law \(\Pr(A=a)=15/16^a\) therefore satisfies
\(\mathbb E V(I_A(x))=(5/9)V(x)\). This is a real inverse contraction.
For positive integer x, discarding illegal predecessors only decreases
the positive sum. But the fourth-Jacobian operator has weights
\(81/16^a\), which are larger by \(27/5\). Restoring that normalization
gives the factor **three**, not a contraction. The finite probability
normalization is also checked in **partial_probability_identity**.

Treating each successive ternary guard as a fresh independent probability
one third would remove this factor. That replacement is unproved: the
guards depend on the entire earlier inverse history.

## A broad ordinary obstruction to the basic weight ansatz

On positive odd integers let
\[
(Bh)(m)=\sum_{\substack{a\ge1\\I_a(m)\text{ positive odd integer}}}
\frac{81}{16^a}h(I_a(m)).
\]
Consider
\[
h(n)=c(n\bmod M)n^p
       \alpha^{v_2(n+1)}\beta^{v_3(n+1)},
\]
where M is a positive integer, all finitely many c-values are positive,
p is real, and alpha,beta are positive.

**No member of this family satisfies a uniform subcritical bound
\(Bh\le\rho h\), with rho<1, on all positive odd integers.**
Four exact ordinary families prove this.

1. For every q>=0 and t>=1, the pair
   \(n=2^{q+1}t-1,\ m=2\,3^q t-1\) is joined by q exact valuation-one
   steps. With t a multiple of M, both endpoints have residue -1
   modulo M. The single-path weighted ratio tends, as t grows, to
   \[
   ((3/2)^{4-p}\alpha/\beta)^q.
   \]
   Hence alpha>=1, beta<=1 and p<4 give expanding columns. Lean proves
   all the ordinary paths in **ordinary_one_runs** and
   **one_run_sound**. For integral p=0,1,2,3 the arbitrary positive
   rational periodic-coefficient counterexample is itself checked in
   **finite_period_power_counterexample**.

2. The exponent-two inverse step from
   \(m_k=(3\,9^k-1)/2\) to \(n_k=2\,9^k-1\) has
   \[
   v_2(m_k+1)=v_2(n_k+1)=1,\quad
   v_3(m_k+1)=0,\quad v_3(n_k+1)=2k.
   \]
   Since \(n_k/m_k\to4/3\), beta>1 makes its weighted ratio unbounded,
   for every fixed p and alpha. The periodic coefficients have a
   bounded positive ratio and cannot offset it. The exact edge and
   ternary equations are checked in **reset_budget_identity**.
   The binary valuation statement follows from \(9^k=1\bmod8\).

3. Another exponent-two inverse step is
   \(m_k=2\,64^k-1\) to \(n_k=(8\,64^k-5)/3\). Here
   \[
   v_2(m_k+1)=6k+1,\quad v_2(n_k+1)=1,\quad
   v_3(m_k+1)=v_3(n_k+1)=0.
   \]
   Thus alpha<1 also gives unbounded ratios. Lean checks the exact
   ordinary identities and congruences in **binary_reset_budget_identity**.

4. It remains to consider alpha>=1, beta<=1, p>=4. The ordinary
   one-step predecessors \(r_k=(4^{k+1}-1)/3\) of 1 obey
   \[
   \frac{81r_k^p}{256^{k+1}}\ge\frac{81}{256}.
   \]
   When k is divisible by three, their shifted binary valuation is
   one and their shifted ternary valuation is zero, as for 1 itself.
   The positive periodic coefficient has a positive minimum, so the
   infinite sum already diverges at the endpoint 1. Lean checks the
   arbitrary-cutoff linear lower bound for every integral p>=4 in
   **root_pressure_sum_lower** and the budget subsequence in
   **root_predecessor_budget_subsequence**. Real p>=4 follows from
   \(r_k^p\ge r_k^4\).

This excludes the entire stated multiplicative ansatz. It does **not**
exclude an estimate for a distinguished initial observable, a selected
return operator, a nonperiodic coefficient, or an additive resource
retaining reset history. The root-predecessor family lies in the known
good basin; it is not a counterexample on nonzero five-defect support.

## The positive additive-history candidate and the missing estimate

To retain every charged reset, consider
\[
G(m)=\sum_{j\ge0}B^j1(m).
\]
The source-qualified all-time theorem
[PR169 ES3](https://github.com/GettysburgResearch/collatz/blob/6cb9bfdc828f91576066b0e4a099d47d8144e915/research/certificate-renewal-20261121/FIXED_ENDPOINT_SUMMABILITY.md)
already gives pointwise finiteness and finite fifth-denominator weighted
mass. Positive reindexing yields \(BG=G-1\). Thus a legitimate additive
potential remembering all resets does exist; the issue is its ordinary
endpoint growth.

Write \(U\) for the accelerated odd map and
\(J_j(n)=3^j/2^{A_j(n)}\), where \(A_j(n)\) is the total binary exponent
along its first j odd steps. The corresponding second-denominator identity is
\[
\sum_{j\ge0}\sum_{n>0\ {\rm odd}}
\frac{J_j(n)^4}{U^j(n)^2}
=\sum_{m>0\ {\rm odd}}\frac{G(m)}{m^2}.
\]
This is an equality of nonnegative extended sums, which may be infinite.
We did not prove an adequate bound for its right side. Substituting
fifth-denominator summability would lose three endpoint powers.

The weaker critical target from
[PR171 CNM](https://github.com/GettysburgResearch/collatz/blob/2bd243b3e05eaa5543adeb2894637b053c9662ca/research/adaptive-closure-20261121/CRITICAL_NEGATIVE_MOMENT_INTERFACE.md)
is
\[
\sum_{q\ge1}\left(P_q+\tfrac12(3/5)^q\right)^{-\rho/2}=\infty,
\]
where \(P_q=\sum_w J_w^4/r_w^2\) is the actual primitive-word moment
and rho is the critical orbit-count exponent specified in that source.
The new exact identity does not establish this divergence.

A single expanding affine block can consume a finite integer valuation:
if \(E(F(n))=3^rE(n)/2^A\), each repetition consumes A binary factors.
An exit to another affine form can reset the valuation arbitrarily high.
The two reset families above show why charging only the current binary
and ternary valuations cannot pay for those exits. Using G remembers
every exit but returns to the uncontrolled second-denominator tail.
No noncircular finite ordinary resource paying all resets was found.

The moment target excludes nonperiodic orbits only. The Jacobian damping
is compatible with hypothetical positive cycles, so a complete Collatz
argument would still need a cycle exclusion.

## What Lean checks

The checked statements are the finite rational identity at every cutoff,
the ordinary one-run family at every length, periodic-coefficient
counterexamples for integral degrees0--3, all-cutoff root-pressure growth
for integral degrees>=4, and the reset equations/congruences. There is
no sorry, custom convergence axiom, or unproved closing hypothesis in
those theorems.

The real-degree limits, infinite-series conclusions, full mixed-weight
exclusion, and Green-potential interpretation are the written deductions
above. They are not represented as a kernel-checked global moment bound.

The core Collatz import is pinned to
[PR174](https://github.com/GettysburgResearch/collatz/tree/7034109ed60a26bc49824e1ed43c239ceca81194/research/psi-closure-20261121/lean).
The primitive moment normalization is from
[PR169 MQ](https://github.com/GettysburgResearch/collatz/blob/6cb9bfdc828f91576066b0e4a099d47d8144e915/research/certificate-renewal-20261121/MOMENT_QUANTILES.md).
