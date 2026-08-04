# T-0013 — Graph-directed negative returns with positive cycle mean

Claim ID: `T-0013`  
Title: Multi-target negative-return criterion and phase-potential expansion theorem  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: `D-0001`, `L-0001`, `T-0009`  
Scope: finite graphs of variable-length negative Collatz return blocks  
Related counterexample candidates: none

## Statement

Let \(G=(V,E)\) be a finite directed graph. Associate to every vertex \(i\in V\) a positive integer \(v_i\), representing the negative phase \(-v_i\).

For every edge \(e:i\to j\), suppose there are positive integers

\[
u_e,\qquad L_e\ge1,\qquad a_e\ge0
\]

such that

\[
\boxed{
T^{L_e}(-u_e)=-v_j,
}
\tag{1}
\]

and the return word contains exactly \(a_e\) odd steps. Put

\[
M_e=2^{L_e},\qquad N_e=3^{a_e},\qquad
\lambda_e=\frac{N_e}{M_e}.
\tag{2}
\]

At phase \(i\), use the quotient coordinate

\[
n=q-v_i.
\tag{3}
\]

The edge cylinder and edge map are

\[
\mathcal C_e
=
\{q\in\mathbb Z:q\equiv v_i-u_e\pmod{M_e}\},
\tag{4}
\]

\[
\boxed{
F_e(q)
=N_e\frac{q-v_i+u_e}{M_e}
=\lambda_eq+\lambda_e(u_e-v_i).
}
\tag{5}
\]

Then:

### 1. Exact graph-directed shadow identity

For every \(q\in\mathcal C_e\),

\[
\boxed{
T^{L_e}(q-v_i)=F_e(q)-v_j.
}
\tag{6}
\]

### 2. Graph-directed counterexample criterion

For each vertex \(i\), let \(S_i\subseteq\mathbb Z\) be a set of quotients satisfying \(q>v_i\). Suppose there is a deterministic edge selector on the disjoint phase space

\[
\mathcal S=\bigsqcup_{i\in V}\{i\}\times S_i
\]

such that whenever edge \(e:i\to j\) is selected at \(q\in S_i\),

\[
q\in\mathcal C_e,
\qquad
F_e(q)\in S_j.
\tag{7}
\]

If, in addition, every infinite selected graph path has unbounded quotient values, then every state \((i,q)\in\mathcal S\) yields a positive-integer Collatz counterexample \(q-v_i\).

### 3. Positive-cycle-mean expansion theorem

Assume every directed cycle \(C\) in \(G\) satisfies

\[
\boxed{
\Lambda(C):=\prod_{e\in C}\lambda_e>1.
}
\tag{8}
\]

Then there exist positive phase weights \(w_i>0\), a number \(\eta>1\), and a finite threshold \(Q\) such that for every edge \(e:i\to j\) and every \(q\ge Q\),

\[
\boxed{
w_jF_e(q)>w_iq.
}
\tag{9}
\]

Consequently, under (7), any selected orbit that begins above \(Q\) is unbounded, even when some individual edges are locally subcritical.

### 4. Negative cycles are automatically supercritical spines

Suppose

\[
-v_0\to-v_1\to\cdots\to-v_{\ell-1}\to-v_0
\]

is a nonzero negative Collatz cycle, and group one full circuit into a block with total length \(L\), odd count \(a\), \(M=2^L\), and \(N=3^a\). Then

\[
\boxed{N>M.}
\tag{10}
\]

Thus every ordinary negative cycle supplies a directed cycle with positive logarithmic weight. It is a natural expanding spine for a multi-target renewal grammar.

## Proof

### Edge identity

If \(q\in\mathcal C_e\), write

\[
q-v_i+u_e=M_ek
\]

with \(k\in\mathbb Z\). Then

\[
q-v_i=M_ek-u_e.
\]

The value on the right follows the same first \(L_e\) parities as \(-u_e\). By `L-0001` and (1),

\[
T^{L_e}(M_ek-u_e)=N_ek-v_j=F_e(q)-v_j,
\]

which proves (6).

### Concatenation

Conditions (7) permit (6) to be applied recursively. The resulting ordinary positive trajectory is exactly the concatenation of the selected finite Collatz blocks. If the quotients are unbounded, so are the phase-boundary states \(q-v_i\), because the finite set \(\{v_i\}\) is bounded. This proves part 2.

### Phase potentials from positive cycle mean

Put

\[
\ell_e=\log\lambda_e.
\]

There are finitely many simple directed cycles. By (8), their mean logarithmic weights are positive. Choose

\[
0<\varepsilon<\min_C\frac1{|C|}\sum_{e\in C}\ell_e.
\tag{11}
\]

Consider the finite system of difference inequalities

\[
p_i-p_j\le\ell_e-\varepsilon
\qquad(e:i\to j).
\tag{12}
\]

It is feasible: summing the right-hand sides around any directed cycle gives a positive number by (11), so the standard difference-constraint obstruction—a negative directed cycle—is absent.

Choose one solution and set

\[
w_i=e^{p_i},\qquad\eta=e^\varepsilon>1.
\]

Equation (12) is equivalent to

\[
\lambda_e\frac{w_j}{w_i}\ge\eta.
\tag{13}
\]

Write

\[
b_e=\lambda_e(u_e-v_i).
\]

Then

\[
\begin{aligned}
w_jF_e(q)
&=\lambda_e\frac{w_j}{w_i}(w_iq)+w_jb_e\\
&\ge\eta w_iq-B,
\end{aligned}
\tag{14}
\]

where

\[
B=\max_{e:i\to j}|w_jb_e|<\infty.
\]

Choose \(Q\) so large that

\[
(\eta-1)w_iQ>B
\]

for every phase \(i\). Then (14) implies (9). Along every selected path above \(Q\), the weighted quotient \(w_iq\) strictly increases. More quantitatively,

\[
y_{t+1}\ge\eta y_t-B,
\qquad y_t=w_{i_t}q_t,
\]

so, after increasing \(Q\) once more if needed, \(y_t\to\infty\). Since the phase weights are bounded above and below, \(q_t\to\infty\).

### Negative-cycle product

Let one full negative cycle begin and end at \(-v\), with affine constant \(B>0\). The finite affine formula gives

\[
-v=\frac{-Nv+B}{M}.
\]

Therefore

\[
B=(N-M)v.
\]

The cycle contains at least one odd step, so \(B>0\). Since \(v>0\), we obtain \(N-M>0\), proving (10). ∎

## Motivation

`T-0009` proved that a finite complete all-supercritical return code around one target is impossible: the all-even 2-adic boundary path forces a contracting branch.

This theorem gives the correct escape hatch. Local contraction is harmless if it moves between phases in a finite graph whose every directed cycle has net multiplier greater than one. A phase potential converts that cycle condition into uniform expansion above one finite threshold.

The construction problem is now cleanly separated into two finite tasks:

1. **arithmetic/symbolic coverage:** construct outgoing return cylinders that give a deterministic forward-invariant phase set containing one ordinary quotient;
2. **weighted graph expansion:** verify that every directed grammar cycle has product multiplier greater than one.

Negative Collatz cycles are ideal spines because their own cycle products are automatically supercritical.

## Dependency audit

- `L-0001` supplies each affine shadow edge.
- `T-0009` is the one-vertex special case and motivates the cylinder selector.
- The phase-potential argument is a finite difference-constraints calculation.

## Gap audit

- Positive cycle mean does not produce the invariant cylinder sets \(S_i\).
- The theorem requires every directed cycle available to the selector to have positive product; unused graph cycles may be deleted.
- An infinite path can remain below the asymptotic threshold unless the proposed invariant sets explicitly start above it.
- The graph criterion does not by itself distinguish an ordinary starting quotient from a purely 2-adic path.

## Adversarial tests

`X-0006` verifies the edge formula on the recorded one-target charts. `X-0008` supplies exact cycle-padded edges that can be used in future phase graphs.

## Remaining uncertainty

The finite theorem appears complete. No graph satisfying the arithmetic coverage and ordinary-start conditions is yet known.

## Suggested next attack

Use the negative eleven-cycle, negative three-cycle, and negative fixed phase as graph vertices. Combine the cycle-padded towers of `T-0015` with pressure scoring from `T-0016`, and seek a deterministic survivor grammar whose every realizable cycle has positive mean and whose accepted language contains one explicit positive quotient.
