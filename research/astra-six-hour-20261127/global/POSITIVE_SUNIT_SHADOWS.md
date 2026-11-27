# Finite sums of positive S-units cannot persist on an escaping ray

**Written deduction using the S-unit equation theorem.** Let \(a_i=U^i(a)\) be an actual positive escaping odd orbit, and let \(\Gamma\subset\mathbb Q_{>0}^{\times}\) be a fixed finitely generated multiplicative group containing 2 and 3. Fix \(D,J\ge1\) and \(0\le\gamma<1\). There are arbitrarily late runs of \(J\) consecutive dates \(i\) where \(a_i\) has no representation
\[
                a_i=u_1+\cdots+u_d,\qquad
                d\le D,\quad u_l\in\Gamma,\quad v_2(u_l)\ge-\gamma i.       \tag{1}
\]
In particular this excludes sums of any fixed number of positive integers supported on any fixed finite list of primes. The factors complementary to two can carry arbitrary exponents. Already the real mantissas of \(2^m3^n\) are dense, so sparsity of real mantissas alone does not yield this assertion.

Write \(A_i\) for the actual cumulative division count. For the positive rationals
\[
      p_i=2^{A_i}3^{-i}a_i,\qquad q_i=2^{A_i}3^{-i-1}
\]
the physical relation gives \(p_{i+1}=p_i+q_i\). The reciprocal sum on a simple orbit gives \(p_i\uparrow P(a)<\infty\), since \(p_i=a/\prod_{j<i}(3a_j/(3a_j+1))\). In particular the sum of all future increments beyond \(i\) tends to zero. At each date satisfying (1), \(p_i\) has at most \(D\) positive \(\Gamma\)-terms, every one of binary valuation at least \(A_i-\gamma i\ge(1-\gamma)i\). [Physical correction and its stated reciprocal input](../escape/GRADED_CORRECTION_SETS.md)

## A uniform comparison inside minimal relations

A relation between two nonempty sums of a total of at most \(2D+J\) positive \(\Gamma\)-terms can be partitioned into minimally vanishing signed subsums. There exists a constant \(K\ge2\), depending only on \(D,J,\Gamma\), such that in every such minimal subsum the ratio of any two real absolute values lies between \(1/K\) and \(K\). To see this, divide by one term. The resulting equation for the tuple of ratios has fixed coefficients in \(\{1,-1\}\), has no vanishing subsum, and has variables in a fixed finite-rank multiplicative group. The S-unit equation theorem gives only finitely many normalized solutions for these finitely many lengths and signs. Take the maximum of all their ratios and reciprocals. The partition of an arbitrary vanishing relation follows by removing a minimal subsum repeatedly. Both sides occur in each minimal subsum by positivity. [Evertse, Schlickewei and Schmidt, *Annals of Mathematics* 155 (2002), Theorem 1.1](https://annals.math.princeton.edu/2002/155-3/p04)

If a fixed number \(V\) has a representation by at most \(D\) positive \(\Gamma\)-terms all at least \(L\), then **every** representation of \(V\) by at most \(D\) positive \(\Gamma\)-terms has each term at least \(L/K\). Compare the two representations in a minimal-subsums partition. Each new term shares its part with at least one old term.

## A positive rational subsum persists across the alleged chain

Suppose, contrary to the assertion, that dates satisfying (1) have gaps at most \(J\) after some date. Fix one such representation at every one of these dates. Put \(M=4(D+1)K^2\) and \(t_l=P(a)M^{-l}/(8D)\) for \(0\le l\le D+1\). Choose a date \(i\) in the chain late enough that \(p_i>P(a)/2\) and \(P(a)-p_i<t_{D+1}\). At least one term in the chosen representation of \(p_i\) exceeds \(t_0\). One of the \(D+1\) bands \((t_{l+1},t_l]\) contains no term. For \(L=t_l\), the sum \(V\) of the terms exceeding \(L\) is positive. All remaining terms are at most \(L/M\). Hence at all later dates \(j\)
\[
                0\le p_j-V < (D+1)L/M < L/K^2.                             \tag{2}
\]

Inductively suppose that a subcollection of the chosen terms of \(p_j\) sums to \(V\). Every term in it is at least \(L/K\), by the uniform comparison with its original representation. Every term outside that subcollection is less than \(L/K^2\), by (2) and positivity. At the next chosen date \(t\), compare the exact positive relation
\[
          p_t=p_j+\sum_{s=j}^{t-1}q_s
\]
using the specified representations. It has at most \(2D+J\) terms; the individual increments are also below \(L/K^2\). Any minimal part containing a selected old term has no old residual term or increment, because their ratio would exceed \(K\). The new terms in all these parts therefore sum exactly to \(V\). This proves persistence at every later date of the chain. But \(V\) is a fixed positive rational number, while **all** new terms at date \(t\) have binary valuation at least \((1-\gamma)t\). Their subsum cannot equal \(V\) indefinitely. This proves (1).

The same proof bounds a finite consecutive chain of such visits after any sufficiently large start \(i\). The initial choices of \(t_l\) and the onset depend only on the fixed orbit and parameters. On a chain ending at \(t\), one has \((1-\gamma)t\le v_2(V)\). For general positive rational terms this upper valuation depends on the denominators of \(V\). If the representatives \(u_l\) are integers, then \(V=2^{A_i}3^{-i}v\) for a positive integer \(v\le a_i\), so \(t-i\le\log_2 a_i\) when \(\gamma=0\): use the sharper terminal lower bound \(v_2(V)\ge A_t\ge A_i+t-i\). This gives a block of \(J\) failures after every sufficiently late \(n\) within \(\log_2(a_n+1)+O_J(1)\) steps in the positive integral case.

## A mixed binary and ternary residue version

Fix \(0<\kappa<\delta\), \(K_0>0\) and \(0\le\gamma<1\). There are arbitrarily late runs of \(J\) dates at which \(a_i\bmod 3^{\lfloor\delta i\rfloor}\) has no representative which is a sum of at most \(D\) positive monomials \(2^m3^b\) with
\[
                -\gamma i\le m\le K_0i,\qquad 0\le b\le\kappa i.            \tag{3}
\]
The margin \(\delta-\kappa\) is part of this assertion.

We spell out the added valuation argument. In a fixed-term signed expression with \(m=O(i)\), \(0\le b\le(\delta-\varepsilon)i\), and coefficients of size \(\exp(o(i))\), any nonzero sum has \(v_3<\lfloor\delta i\rfloor\) for all sufficiently large \(i\). If not, pass to a subsequence on which each \(b/i\) converges. Partition terms by their common limiting ratio. Within a class of ratio \(r\), factor out its least power of three. The remaining powers of three have exponent \(o(i)\), and can be included in the small coefficients of [the moving-coefficient valuation lemma](SPARSE_SHADOWS.md). Since the coefficients are integers and powers of two are ternary units, every nonzero class sum has valuation \(ri+o(i)\). Distinct nonzero classes have distinct such rates. The least rate determines the valuation of the entire sum by the ultrametric inequality. It is at most \(\delta-\varepsilon\), a contradiction. Clearing negative binary exponents does not affect these valuations.

On two visits to (3) separated by at most \(J\) dates, expand their chosen representatives in the exact word equation as in [the ordinary transport argument](SPARSE_SHADOWS.md). Every term fits the preceding estimate with \(\varepsilon=(\delta-\kappa)/2\) at sufficiently late dates. Hence the residuals satisfy the exact homogeneous relation (2) of that note. On an infinite syndetic chain, the terminal residual has binary valuation at least \(-\gamma t\). Telescoping forces the initial residual to be zero. All representatives in the chain then equal the ordinary states, contrary to the positive S-unit result (1). This proves the mixed residue exclusion.

These deductions leave targets with an unbounded minimum number of positive terms. The equal-clock packet construction provides many ordinary vertices at a level; it has not supplied representations of their ordinary heights by a bounded number of terms of (1) or (3).
