# T-0015 — Cycle-padded mismatch return towers

Claim ID: `T-0015`  
Title: Exact return towers obtained by shadowing a negative cycle before one complementary mismatch  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: `T-0013`, `T-0014`  
Scope: countable graph-directed return families generated from one negative Collatz cycle  
Related counterexample candidates: none

## Statement

Let \(P\) and \(C\) be the negative-phase and complementary maps from `T-0014`.

Suppose \(v_0\) lies on a nonzero negative Collatz cycle of period \(\ell\). Write

\[
P^\ell(v_0)=v_0
\]

and let

\[
a=\sum_{j=0}^{\ell-1}(P^j(v_0)\bmod2)
\tag{1}
\]

be the number of odd phases in one circuit. Put

\[
\Lambda=\frac{3^a}{2^\ell}>1.
\tag{2}
\]

Fix an index

\[
0\le k_0<\ell,
\]

and define

\[
w=P^{k_0}(v_0),
\qquad
A_0=\sum_{j=0}^{k_0-1}(P^j(v_0)\bmod2),
\tag{3}
\]

\[
\delta=1-(w\bmod2),
\qquad
g_0=A_0+\delta.
\tag{4}
\]

Let

\[
z=C(w).
\]

Assume that after \(r\ge0\) ordinary negative-phase steps, \(z\) reaches a selected target phase \(v_1\):

\[
P^r(z)=v_1.
\tag{5}
\]

Let

\[
b=\sum_{j=0}^{r-1}(P^j(z)\bmod2)
\tag{6}
\]

be the odd count along this synchronized recovery segment.

For every integer \(t\ge0\), put

\[
k_t=k_0+t\ell,
\qquad
g_t=g_0+ta.
\tag{7}
\]

Choose an odd integer \(m\) satisfying the unique congruence

\[
\boxed{
3^{g_t}m\equiv-1\pmod{2^{r+1}}.
}
\tag{8}
\]

Set

\[
q=2^{k_t}m
\tag{9}
\]

and

\[
q'=\frac{3^b(3^{g_t}m+1)}{2^{r+1}}.
\tag{10}
\]

Then the following hold.

### 1. Exact graph-directed return

After

\[
L_t=k_t+r+1
\tag{11}
\]

shortcut steps,

\[
\boxed{
T^{L_t}(q-v_0)=q'-v_1.
}
\tag{12}
\]

The block contains exactly

\[
a_t=g_t+b
\tag{13}
\]

odd steps.

### 2. Signed rational-base equation

With

\[
M_t=2^{L_t},
\qquad
N_t=3^{a_t},
\]

we have

\[
\boxed{
N_tq=M_tq'-2^{k_t}3^b.
}
\tag{14}
\]

Thus the natural signed digit of the return edge is

\[
\boxed{
\alpha_t=-2^{k_t}3^b.
}
\tag{15}
\]

### 3. Geometric multiplier tower

The real multiplier of the return is

\[
\lambda_t=\frac{N_t}{M_t}.
\]

It satisfies

\[
\boxed{
\lambda_t=\lambda_0\Lambda^t.
}
\tag{16}
\]

Since \(\Lambda>1\), every fixed phase type \(k_0\) becomes supercritical after finitely many cycle paddings.

### 4. Disjoint countable cylinders

Condition (8) selects one odd residue class modulo \(2^{r+1}\). Therefore (9) describes one nonempty dyadic cylinder of depth

\[
L_t=k_0+t\ell+r+1.
\]

The cylinders for distinct \(t\) are disjoint because their members have distinct exact valuations

\[
\nu_2(q)=k_0+t\ell.
\]

Consequently one finite cycle phase, one complementary exit, and one synchronized recovery path generate a countable, finitely parameterized family of exact return edges.

## Proof

By `T-0014`, the first \(k_t\) steps are synchronized with the negative cycle. Since

\[
q=2^{k_t}m,
\qquad m\text{ odd},
\]

we obtain

\[
q_{k_t}=3^{g_t-\delta}m,
\qquad
v_{k_t}=P^{k_t}(v_0)=w.
\]

The next step is the first mismatch. Equation (13) of `T-0014` gives

\[
q_{k_t+1}=\frac{3^{g_t}m+1}{2},
\qquad
v_{k_t+1}=C(w)=z.
\tag{17}
\]

Congruence (8) is exactly the assertion that the first quantity in (17) is divisible by \(2^r\). Hence the next \(r\) values of the difference are even. During those steps the phase follows

\[
z,P(z),\ldots,P^r(z)=v_1,
\]

and the difference is multiplied by \(3^b/2^r\). Therefore

\[
q_{L_t}=\frac{3^b(3^{g_t}m+1)}{2^{r+1}}=q',
\]

which proves (12). The synchronized cycle prefix contributes \(g_t-\delta\) odd steps, the mismatch contributes \(\delta\), and the recovery contributes \(b\), giving (13).

For (14), multiply (10) by

\[
M_t=2^{k_t+r+1}.
\]

Then

\[
\begin{aligned}
M_tq'
&=2^{k_t}3^b(3^{g_t}m+1)\\
&=3^{g_t+b}(2^{k_t}m)+2^{k_t}3^b\\
&=N_tq+2^{k_t}3^b,
\end{aligned}
\]

which is equivalent to (14).

Finally,

\[
\frac{\lambda_{t+1}}{\lambda_t}=\frac{3^a}{2^\ell}=\Lambda,
\]

proving (16). Uniqueness of the residue in (8) follows because \(3^{g_t}\) is odd and therefore invertible modulo \(2^{r+1}\). ∎

## Interpretation

The parameter \(t\) counts complete synchronized circuits of a negative cycle before the first mismatch. Each additional circuit:

- adds \(\ell\) binary cylinder bits;
- adds \(a\) odd steps;
- leaves the mismatch phase type unchanged;
- multiplies the real edge slope by the supercritical cycle factor \(\Lambda\).

This is the precise exchange between 2-adic specificity and real expansion. It upgrades a single finite return edge into an infinite regular tower of increasingly narrow but eventually expanding edges.

## Consequence for graph design

`T-0009` showed that a finite complete all-supercritical code around one target is impossible. The present theorem exhibits the natural countable replacement:

> a finite collection of phase types, each carrying a nonnegative cycle-padding counter.

The arithmetic data are finite modulo the cycle period; only the padding counter is unbounded.

## Gap audit

- The union of the return cylinders in one tower need not cover all ordinary quotients.
- Supercriticality for large \(t\) does not prove that a forward orbit visits only those large-padding branches.
- The congruence in (8) controls one synchronized recovery; failure of that congruence causes another mismatch and may leave the selected phase graph.
- An ordinary finite starting quotient and a closed infinite grammar are still required.

## Adversarial tests

`X-0008` verifies (8)--(16) for every phase type of the negative eleven-cycle and for the first four padding levels. It directly iterates the corresponding ordinary positive and negative Collatz states.

## Suggested next attack

Construct a finite graph whose vertices are negative cycles or selected phases and whose edge types are the finite mismatch/recovery types in this theorem. The only unbounded state should be the padding counter. Seek a substitution or stack rule that forces the counter to remain above each edge's supercritical threshold and proves that one ordinary finite quotient follows the resulting graph forever.
