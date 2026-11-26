# An arbitrarily deep dyadic test of the original ternary collision energy

**Status.** Source-qualified written implication and equivalence. The lower bound concerns a finite arithmetic statistic of the original Syracuse law, sampled at its actual positive least odd lifts. The upper bound needed for exclusion remains open. The argument uses a one-sided Pliss selection and the uniform ray estimates of PR193.

Write \(S(x)=(3x+1)/2^{e(x)}\) on positive odds, \(e(x)=v_2(3x+1)\), \(\alpha=\log_2 3\), \(A_j(x)=\sum_{i<j}e(S^i x)\). Let \(\rho_k=3^kp_k\) be the whole-Haar density of the original finite ternary offset law with independent gap weights \(2^{-e}\). Write \(\Phi(u)=u^2/(1+u)\). On positive odd integers put
\[
 M_k={1\over k}\sum_{0<y<2\cdot3^k,\ y\ {\rm odd}}
       \Phi(\rho_k(y\bmod3^k)/y)\,\delta_y .
\]
Integer height is measured before projection into any compact group.

## 1. A total-variation replacement on ordinary sites

For each escaping positive component fix one injective odd ray \(a_{C,0},a_{C,1},\ldots\) of units. Use PR193's strictly positive amplitudes \(H_C\), with
\(F=\sum_C\Phi(H_C)<\infty\). Then
\[
 \left\|M_k-\sum_C {\Phi(H_C)\over k}
              \sum_{n=0}^{k-1}\delta_{a_{C,n}}\right\|_1\longrightarrow0. \tag{1}
\]
The norm is the sum of absolute point masses. The replacement is valid against any sequence of tests bounded in modulus by one, even tests depending on the entire future of the marked ordinary integer.

Write \(g_k(y)=L_k(y)/y\) for the first-hit version. PR193 equations (2), (3), (5), (8) in [COLLISION_ENERGY.md](https://github.com/GettysburgResearch/collatz/blob/25f5462e2c43feea65760884f7ea8f53576fbc18/research/astra-unconventional-20261126/global/COLLISION_ENERGY.md) and the associated uniform first-entry estimate are the external inputs. Equation (8) and the 1-Lipschitz property of \(\Phi\) give \(o(1)\) error in normalized norm from deleting repeated laps, regardless of the number of positive cycles. Targets outside the future of starts through \(B\) contribute \(O(B^{-c})\), since \(g_k\ll B^{-c}\) there, \(\Phi(g_k)\le g_k^2\), and \(\sum g_k=O(k)\). Each fixed periodic or transient site contributes \(o(1)\).

On each of the finitely many remaining escaping tails, \(g_k(a_n)=Z_{n-k}+o_{n\to\infty}(1)\) uniformly in \(k\), with \(Z_v\to H_C\) for \(v\to-\infty\) and \(Z_v\to0\) for \(v\to+\infty\). All sites through \(n=k-1\) lie in the representative window for large \(k\), because \(a_n+1\le(3/2)^n(a_0+1)\). The mean of \(|\Phi(g_k(a_n))-\Phi(H_C)|\) over this segment tends to zero by deleting fixed-length ends and then increasing their lengths. Beyond \(k+J\) the normalized clipped sum is \(O(\sup_{v\ge J}Z_v+o(1))\) by the global first-moment estimate. The intervening \(J+1\) bounded terms cost \(o(1)\). Changing the starting ray in a component changes its empirical probability by \(o(1)\), since the rays coalesce up to a fixed time shift. Finally the omitted component amplitudes have summable tail. First increase \(k\), then \(B\). These estimates prove (1) in norm.

## 2. Permanent tests of any increasing precision

Fix \(\alpha<b<2\). For \(m\ge1\) define the dyadic cylinder union
\[
 K_b(m)=\{y\ {\rm odd}: A_j(y)\le b j\ (1\le j\le m)\},\qquad
 K_b=\bigcap_{m\ge1}K_b(m).
\]
A word with total gap \(A\) fixes exactly one odd residue modulo \(2^{A+1}\), by composing the inverse branches \((2^ez-1)/3\) from any odd dyadic \(z\). Thus \(K_b(m)\) is decidable by residues modulo \(2^{\lfloor bm\rfloor+1}\). The infinite test can even be restricted to ordinary positives when integrating against \(M_k\).

**Theorem.** For every sequence \(m(k)\ge1\), with no growth constraint (also \(m(k)=\infty\)),
\[
 \liminf_k M_k(K_b(m(k)))\ \ge\ {b-\alpha\over b-1}\ F . \tag{2}
\]
The liminf on the left is zero exactly when every positive orbit eventually repeats, under the stated PR193 inputs. Cycle uniqueness remains separate.

On an escaping ray corrected height gives \(2^{A_j(a_0)}P(a_j)=3^jP(a_0)\) and \(P(a_j)\ge1\). Thus \(A_j(a_0)\le\alpha j+c\) for all \(j\). Put \(B_j=bj-A_j(a_0)\) and \(l_i=\min_{j\ge i}B_j\), a genuine minimum since \(B_j\ge(b-\alpha)j-c\to\infty\). The sequence \(l_i\) is nondecreasing. If \(l_{i+1}>l_i\), then \(B_i=l_i\), so all later \(B_{i+j}\ge B_i\), or equivalently \(a_i\in K_b\). Each rise is at most \(B_{i+1}-B_i=b-e(a_i)\le b-1\). Hence
\[
 (b-1)\#\{i<N:a_i\in K_b\}\ge l_N-l_0\ge (b-\alpha)N-c-l_0 .
\]
Use this first for finitely many fixed rays in (1), then exhaust the components. On no escape (1) gives \(\|M_k\|_1\to0\). A finite-interval selection discarding the last \(m\) sites would introduce a needless growth restriction on \(m(k)\).

For relative Haar probability \(h_2\) on the odd dyadics, the finite gaps have independent probabilities \(2^{-e}\) by the odd residue calculation. For \(1<b<2\), exponential tilting gives
\[
 h_2(K_b(m))\le \exp[-m I(b)],\qquad
 I(b)=b\log2-b\log b+(b-1)\log(b-1)>0 .
\]
Indeed \(\mathbb E[s^e]=s/(2-s)\); choose \(s=2(b-1)/b<1\) in the lower-tail Markov bound. Equation (2) applies even when the Haar measure of the sieve is doubly exponentially small in \(k\). The proportion of ambient dyadic residues differs from the true ternary trace weight.

The cylinder covers also show \(\dim_H K_b\le H_2(1/b)\) in the dyadic metric. For total exponent \(d\in[m,bm]\) there are at most \(\binom{d-1}{m-1}\) cylinders of diameter \(2^{-(d+1)}\). The bound \(\binom{d}{m}\le 2^{dH_2(m/d)}\le2^{dH_2(1/b)}\) holds because \(m/d\ge1/b>1/2\). Every compact dyadic weak limit \(\nu\) of \(M_k\) satisfies \(\nu(K_b)\ge[(b-\alpha)/(b-1)]F\) by (2) at every fixed depth and continuity from above. Consequently its part singular to odd Haar has mass at least \((2-\alpha)F\), by taking \(b\uparrow2\) through a countable sequence.

## 3. Past and future arithmetic

As a test of an integer \(y\), \(K_b(m)\) is defined by its actual future. The weight \(\rho_k(y)\) sums ternary-admissible past words. Independent ambient Haar coordinates give an exponentially small sieve expectation after any conditioning on the ternary coordinate. The two tested coordinates here are the same integer \(y\), sampled with its physical factor \(1/y\). A past word with sum \(A\) and carry \(D>0\) reconstructs an ordinary positive predecessor \(x\) by \(3^kx=2^A y-D\). For every least odd representative, \(x<2^{A+1}\). Its past word already determines \(x\bmod 2^{A+1}\). No independent higher binary digits of that source remain at this cutoff. Enlarging \(m(k)\) alone creates no averaging at that interface.

Paper 170 proves coarse binary-window rigidity and exhibits biased independent parity measures with equidistributed high-digit windows for every fixed width. Its §5 retains the missing fine conditional independence. Paper 150, §6.3, establishes a related rare ternary past event for a divergent ray. They use different observations from the positive-lift, all-future test (2). [Paper 170](https://rstation.ai/problems/collatz/papers/170) · [Paper 150/v1](https://rstation.ai/problems/collatz/papers/150/v1)

**First unsupported step.** For at least one \(b\in(\alpha,2)\) and some specified depths \(m(k)\), prove \(\liminf_k M_k(K_b(m(k)))=0\) for the exact original ternary law at these least positive lifts. The Haar estimate above, the inverse-pressure radius of PR200 and finite agreement on ambient quotients do not establish that estimate. The all-time tests can include points of another positive periodic basin if its cycle has sufficiently small mean exponent. The normalized collision mass deletes every periodic component.

The integer-valued envelope selection, including attainment of the full tail minimum and its affine prefix-count bound, is checked in [PermanentSieve.lean](PermanentSieve.lean). Scaling a rational budget gives this integer form. The Lean file does not establish the source-qualified representation of \(M_k\) or any upper bound on it.
