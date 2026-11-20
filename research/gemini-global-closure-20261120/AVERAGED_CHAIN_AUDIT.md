# What the Gemini residue operators actually prove

**Status: PROPOSED exact audit and replacement statements.** The verified finite statements here do not establish ordinary Collatz convergence. The paired actual-transport result is in `ACTUAL_TRANSPORT.md`.

## 1. Exact full-spectrum identity for the binary averaging model

Fix m>=1. Let pi_m(r) be the first m parity bits of the shortcut orbit of r mod 2^m. This is a bijection to binary words of length m: at each induction step the two lifts modulo 2^(m+1) have opposite next parity, since the affine parity-prefix numerator has odd multiplier.

Under pi_m, the Gemini transition from r to the two T-images of its lifts becomes the binary shift

\[
 (b_0,\ldots,b_{m-1})\mapsto(b_1,\ldots,b_{m-1},c),
 \quad c\in\{0,1\},
\]

with probability 1/2 on c. For arbitrary positive weights w_0,w_1 the operator is

\[
 (Mf)(b)=\frac{w_{b_0}}2\sum_{c=0}^1f(b_1\cdots b_{m-1}c).
\]

After m steps,

\[
 (M^mf)(b)=\left(\prod_{i=0}^{m-1}w_{b_i}\right)
 \frac1{2^m}\sum_{v\in\{0,1\}^m}f(v).
 \tag{1}
\]

Thus M^m has rank one and its sole nonzero eigenvalue is `((w_0+w_1)/2)^m`. Also `h(b)=product_i w_(b_i)` is a strictly positive eigenfunction of M with eigenvalue `(w_0+w_1)/2`. Consequently

\[
 \rho(M)=\frac{w_0+w_1}{2}.
 \tag{2}
\]

The Gemini formula with `w_0=2^(-alpha)` and `w_1=(3/2)^alpha` is therefore exact for all m, not just the floating-point samples. Its nonzero eigenvalue is independent of residue precision. Increasing m leaves this contraction factor unchanged and does not by itself supply pointwise arithmetic control.

The strict-convexity proof of the moment window `0<alpha<1` is correct. It is an averaged multiplicative-coefficient statement. It is not an exact formula for the ordinary height ratio on an odd step, which also contains `1/(2n)`.

## 2. The killed matrix kills the wrong event for fixed-floor survivors

The uploaded code deletes every even current state: every even positive integer locally decreases in one step. It does not delete the all-ones parity window, since numbers `n=2^m(k+1)-1` have

\[
 T^j(n)=3^j2^{m-j}(k+1)-1>n\qquad(1\le j\le m).
\]

Consider any deletion rule that removes every window whose first bit is zero and retains the all-ones window. Additional deleted odd windows are permitted. In the directed surviving graph, every directed cycle must have every emitted bit equal to one; after m shifts its state must be the all-ones window. The sole possible cyclic component is therefore that one vertex, with self-loop weight w_1/2. All other components are acyclic, so

\[
 \boxed{\rho(K)=w_1/2=(3/2)^\alpha/2.}
 \tag{3}
\]

At alpha=1/2 this is exactly `sqrt(3/2)/2`, the reported 0.612372. It persists for every m for this elementary graph reason, not because the hard unsafe-return process was controlled.

For a fixed original floor N, a state y is killed only when it actually reaches a value below N (or the designated absorbing core). Local descent below y is a different event. The ordinary path

\[
 27\longmapsto41\longmapsto62\longmapsto31
\]

stays above its original floor 27, while the Gemini killed operator deletes the even state 62. This gives a direct semantic counterexample to its use as a fixed-floor survivor operator. It is not a Collatz counterexample.

## 3. Exact worst-lift rate

Replacing fresh random lifts by the worst possible lift gives the nonlinear positive operator

\[
 (\mathcal Rf)(b)=w_{b_0}\max_{c\in\{0,1\}}f(b_1\cdots b_{m-1}c).
\]

For alpha>0, w_1>w_0. For every strictly positive finite-residue potential h, the all-ones self-loop gives

\[
 \max_b\frac{\mathcal Rh(b)}{h(b)}\ge w_1.
\]

Taking h=1 attains this bound. Thus the best one-step factor in this robust finite-residue model is exactly

\[
 \inf_{h>0}\max_b\frac{\mathcal Rh(b)}{h(b)}
 =w_1=(3/2)^\alpha>1.
 \tag{4}
\]

The same conclusion holds after the above deletion, because the all-ones self-loop survives. The mean factor w_1/2 becomes w_1 when the missing bit is held adversarially rather than averaged. Every finite string of these odd steps has arbitrarily large positive ordinary realizations, so this is also a sound obstruction to a globally valid fixed-depth deterministic contraction estimate of this precise kind. It does not exhibit an ordinary infinite all-odd orbit.

## 4. Repairs to the inverse graph claims

The uploaded route-2 graph has units modulo 27 as states and legal macro-actions `E^j O`, j=0,...,5. Their total step cost is k=j+1, and there is one odd lift per action. The three listed children are possible next residues of the actual source's three higher ternary lifts.

Choosing the minimum child is an optimistic abstraction; it may choose hidden source digits. It cannot certify a path for every fixed ordinary source. Choosing the maximum child is the appropriate robust Bellman inequality at that fixed precision.

### 4.1 The all-state cycle criterion

For a finite one-player directed graph with positive event counts t(a), an all-state bounded potential for `min_a[k(a)-alpha t(a)+V(v)]<=V(u)` exists exactly when **each state can reach some cycle of nonpositive adjusted total cost**. A global minimum cycle ratio alone is insufficient. Two disconnected self-loops of ratios 1 and 3 have global minimum 1, yet no all-state certificate at alpha=2. This repairs the missing reachability hypothesis in Lemma 2.1.

Necessity follows by selecting an action satisfying the inequality and following the resulting finite graph to a cycle. For sufficiency, choose one good cycle and its entire backward-reachable basin, orient that basin toward the chosen cycle, and remove the basin. Any remaining state still reaches a good cycle in the remaining graph, since a path entering the removed basin would have made that state part of the basin. Repeat this finite construction. The selected functional graph has only the chosen nonpositive-cost cycles, so its finite difference inequalities admit a potential; transient costs are paid by that bounded potential. This avoids accidentally selecting a positive-cost cycle when separately chosen paths intersect.

### 4.2 Exact values for the actual mod-27 graph

The optimistic graph's optimal all-state slope is exactly **1**. Every edge costs at least 1; the following nonnegative potential certifies slope 1:

\[
 V=(3,2,4,3,5,3,2,3,1,4,4,1,4,1,2,5,6,0)
\]

in increasing order of the unit states `(1,2,4,5,7,8,10,11,13,14,16,17,19,20,22,23,25,26)`. The value one is attained by the cost-one self-loop at residue 26, corresponding to the negative fixed point -1 in the ternary inverse system. It is not a positive ordinary inverse compiler below the physical height threshold.

For the robust graph, the following integer additive eigenvector h is exact in that same state order:

\[
 h=(-2,-3,-1,-1,0,-2,-2,-2,-3,-1,0,-4,-1,-3,-3,0,1,-4).
\]

It satisfies, state by state,

\[
 \min_a\left\{k(a)+\max_{v\in C(u,a)}h(v)\right\}=3+h(u).
 \tag{5}
\]

The minimizing action supplies an upper finite-credit certificate at slope 3. For every action an adversary can choose a child with `k+h(child)>=3+h(source)`; telescoping proves a lower bound `cost>=3t+h(start)-h(end)`. Since h is bounded, no robust finite-credit slope below 3 is possible on this graph. The exact optimal robust slope is therefore **3**, without interpreting a finite iteration timeout as an impossibility proof.

Equation (5) is independently checked using only integers. Neither Karp's algorithm nor Howard policy iteration appears in the supplied route-2 verifier; its implementation is finite Bellman iteration. The advertised 10–20 policy-iteration rounds have no supplied proof or run supporting them.

### 4.3 Finite timeout is not a negative certificate

A graph with N+1 states in a chain, cost one on each edge, followed by a zero-cost terminal self-loop has a finite nonnegative Bellman potential equal to distance to the terminal loop. Starting from zero, the clamped value iteration requires N+1 rounds to report a fixed point. An arbitrary 200-round timeout therefore cannot prove nonexistence. This general control is separate from the exact mod-27 dual certificate (5).

## 5. Scope

The averaged identity (2) and strict moment window survive the audit. Their proposed use as actual unsafe transport does not. The exact polynomial-rank-to-logarithmic-domain repair is supplied in the companion note. For the inverse graph, the audit replaces the unsupported timeout inference by an explicit primal/dual equality and preserves the crucial fixed-source versus chosen-lift distinction. No improvement of this finite inverse game is a proof of forward convergence.
