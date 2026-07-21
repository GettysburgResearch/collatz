# T-0016 — Collatz–Kraft martingale and renewal-code pressure

Claim ID: `T-0016`  
Title: Exact Kraft identities, likelihood-ratio interpretation, and negative typical Lyapunov drift for complete parity renewal codes  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: `D-0001`, `T-0009`, `T-0013`  
Scope: finite or countable complete binary prefix codes of Collatz parity blocks  
Related counterexample candidates: none

## Statement

Let \(\mathcal W\) be a finite or countable complete prefix-free collection of finite binary words. For \(w\in\mathcal W\), write

\[
L(w)=|w|,
\qquad
a(w)=\#\{\text{ones in }w\},
\]

and define its real Collatz multiplier

\[
\lambda(w)=\frac{3^{a(w)}}{2^{L(w)}}.
\tag{1}
\]

Assume that the cylinders \([w]\) partition the full binary sequence space up to a null set for every Bernoulli product measure with parameter \(0<p<1\). This holds for every finite complete prefix code and for the usual countable complete renewal codes.

Then:

### 1. Bernoulli partition identity

For every \(0<p<1\),

\[
\boxed{
\sum_{w\in\mathcal W}
p^{a(w)}(1-p)^{L(w)-a(w)}=1.
}
\tag{2}
\]

### 2. Collatz–Kraft identities

At \(p=1/2\),

\[
\boxed{
\sum_{w\in\mathcal W}2^{-L(w)}=1.
}
\tag{3}
\]

At \(p=3/4\),

\[
\boxed{
\sum_{w\in\mathcal W}\frac{3^{a(w)}}{4^{L(w)}}=1.
}
\tag{4}
\]

Equivalently, if a codeword is selected with fair-Haar probability

\[
\mathbb P_{1/2}(w)=2^{-L(w)},
\]

then

\[
\boxed{
\mathbb E_{1/2}[\lambda]=1.
}
\tag{5}
\]

### 3. Likelihood-ratio interpretation

Let \(\mu_p\) denote Bernoulli measure with probability \(p\) of an odd parity bit. Then for every codeword,

\[
\boxed{
\lambda(w)=\frac{\mu_{3/4}([w])}{\mu_{1/2}([w])}.
}
\tag{6}
\]

Thus the real Collatz multiplier is exactly the Radon--Nikodym likelihood ratio between the \(3/4\)-odd and fair parity measures, evaluated on one renewal cylinder.

### 4. Exact negative logarithmic drift

Assume

\[
\sum_{w\in\mathcal W}L(w)2^{-L(w)}<\infty.
\tag{7}
\]

Then

\[
\boxed{
\sum_{w\in\mathcal W}a(w)2^{-L(w)}
=\frac12\sum_{w\in\mathcal W}L(w)2^{-L(w)}.
}
\tag{8}
\]

Consequently

\[
\boxed{
\mathbb E_{1/2}[\log\lambda]
=\frac12\log\left(\frac34\right)\mathbb E_{1/2}[L]<0.
}
\tag{9}
\]

A complete renewal code therefore has mean multiplier one but strictly negative typical logarithmic growth.

### 5. Bernoulli renewal dynamics

For a one-target negative-template return code as in `T-0009`, suppose its return cylinders form a complete prefix code. Under Haar measure on \(\mathbb Z_2\), the selected return words are independent with probabilities

\[
2^{-L(w)},
\]

and the post-return quotient is again Haar distributed. Therefore, when (7) holds, almost every 2-adic quotient has asymptotic block multiplier

\[
\lim_{n\to\infty}\frac1n\sum_{j=0}^{n-1}\log\lambda(w_j)
=\mathbb E_{1/2}[\log\lambda]<0.
\tag{10}
\]

Every orbit with positive asymptotic block growth lies in a Haar-null exceptional subset of the complete renewal system.

### 6. Graph-directed pressure matrices

For a finite phase graph with return edges \(e:i\to j\), define

\[
\mathcal A_s(i,j)
=\sum_{e:i\to j}2^{-L_e}\lambda_e^s
=\sum_{e:i\to j}\frac{3^{s a_e}}{2^{(s+1)L_e}}.
\tag{11}
\]

Then:

- \(\mathcal A_0\) records fair 2-adic cylinder mass;
- \(\mathcal A_1\) records the \(3/4\)-odd tilted mass;
- if the outgoing edges at each phase form a complete prefix code, both matrices are row-stochastic;
- an incomplete candidate grammar should be judged by both pressure radii
  \[
  \rho(\mathcal A_0)
  \quad\text{and}\quad
  \rho(\mathcal A_1),
  \]
  rather than by branch count alone.

For a complete finite graph code with stationary phase distribution \(\pi\) and finite mean return length, the stationary mean logarithmic multiplier is

\[
\boxed{
\sum_i\pi_i\sum_{e:i\to *}2^{-L_e}\log\lambda_e
=\frac12\log\left(\frac34\right)
\sum_i\pi_i\sum_{e:i\to *}L_e2^{-L_e}<0.
}
\tag{12}
\]

## Proof

Equation (2) is the total Bernoulli measure of a complete prefix partition.

Substituting \(p=1/2\) gives (3). Substituting \(p=3/4\) gives

\[
\sum_w\left(\frac34\right)^{a(w)}\left(\frac14\right)^{L(w)-a(w)}
=\sum_w\frac{3^{a(w)}}{4^{L(w)}}=1,
\]

which is (4). Since

\[
2^{-L(w)}\lambda(w)=\frac{3^{a(w)}}{4^{L(w)}},
\]

this is equivalent to (5). The same calculation gives (6).

Under (7), differentiate (2) at \(p=1/2\). Termwise differentiation is justified by the finite first moment. We obtain

\[
0=\sum_w2^{-L(w)+1}\bigl(2a(w)-L(w)\bigr),
\]

which is equivalent to (8). Therefore

\[
\begin{aligned}
\mathbb E_{1/2}[\log\lambda]
&=\log3\,\mathbb E_{1/2}[a]-\log2\,\mathbb E_{1/2}[L]\\
&=\left(\frac12\log3-\log2\right)\mathbb E_{1/2}[L]\\
&=\frac12\log(3/4)\,\mathbb E_{1/2}[L],
\end{aligned}
\]

proving (9).

For the one-target renewal dynamics, a cylinder has the form

\[
q=r_w+2^{L(w)}k.
\]

Conditioned on the cylinder, \(k\) is Haar distributed. The return map multiplies \(k\) by the odd unit \(3^{a(w)}\), so the returned quotient is again Haar distributed. The branch label and returned quotient are independent. Iteration therefore gives an i.i.d. renewal process with codeword probabilities \(2^{-L(w)}\), and the strong law proves (10).

For a graph-directed complete code, the same cylinder decomposition gives the phase transition probabilities

\[
P(i,j)=\mathcal A_0(i,j).
\]

The identities (3)--(4) applied at each phase make \(\mathcal A_0\) and \(\mathcal A_1\) row-stochastic. Equation (12) follows by applying (9) at each phase and averaging with \(\pi\). ∎

## Corollaries

### No complete uniformly expanding code

Equation (5) immediately implies that a complete prefix code cannot satisfy

\[
\lambda(w)>1
\]

for every branch. This recovers and strengthens the finite obstruction in `T-0009` without identifying the specific all-even branch.

### Quantitative mass bound

For every \(R>0\),

\[
\sum_{\lambda(w)\ge R}2^{-L(w)}\le\frac1R.
\tag{13}
\]

Thus strongly expanding returns necessarily occupy small fair 2-adic mass.

## Strategic interpretation

The project has repeatedly enlarged collision alphabets and return libraries. This theorem identifies the correct conservation law:

> 2-adic coverage and real Collatz expansion are two probability measures on the same prefix language, and the branch multiplier is their exact likelihood ratio.

A counterexample grammar cannot be a typical broad cover. It must be an entropy-thin exceptional language with positive logarithmic pressure and, separately, one ordinary finite starting point.

The appropriate score for a proposed regular renewal grammar is therefore not cardinality, Kraft mass, or cycle multiplier in isolation. It is the pair of pressure operators \(\mathcal A_0,\mathcal A_1\), together with the ordinary-boundary condition.

## Gap audit

- Haar-null does not mean empty and does not exclude an ordinary positive integer.
- Negative typical drift is consistent with exceptional divergent trajectories.
- Pressure radii do not solve the finite-versus-adic problem.
- A graph may contain a positive-cycle survivor subgrammar even though its complete stationary code has negative typical drift.

## Adversarial tests

`X-0008` verifies (3)--(9) exactly on several complete finite prefix codes, including the nonuniform code

```text
0, 10, 110, 111
```

and verifies the likelihood-ratio identity word by word.

## Suggested next attack

Construct a finite or countable subgrammar for which:

1. the fair pressure \(\rho(\mathcal A_0)\) is small enough to isolate an exceptional survivor language;
2. the tilted pressure and every realizable grammar cycle support positive real growth;
3. the accepted transducer has an explicit ordinary finite boundary state.

This is a thermodynamic version of the graph-directed target in `T-0013`.
