# A power bound for one ordinary slow tail is equivalent to uniform logarithmic total stopping

Use the shortcut map T(n)=n/2 for even n and (3n+1)/2 for odd n. Let τ(n) be its **first** hitting time of 1, with τ(n)=∞ if it never hits. All logarithms are natural. Write D=log(4/3), μ=2/D, and
\[
  E_C(X)=\#\{n\le X:\tau(n)>C\log n\}.
\]

**Theorem 1.** The following statements are equivalent.

1. For some finite C>0 and ε>0, one has E_C(X)=O(X^{1−ε}).
2. Every n terminates, and τ(n)=O(log(2+n)) uniformly in n.
3. For each C>μ there exists ε(C)>0 with E_C(X)=O_C(X^{1−ε(C)}).

The deduction from one power-sparse bound to every C>μ was proved by Inselmann. The pointwise conclusion in (2), with the quantitative coefficient below, comes from transferring a physical delay at one positive target back to many genuine starts. Replacing E_C by its count restricted to terminating integers gives the equivalence of (1) and the uniform logarithmic bound **within the basin of 1**. This restricted statement leaves other components unrestricted. [Inselmann, arXiv:2402.03276v3, Definition 2.6 and Corollary 3.5](https://arxiv.org/pdf/2402.03276)

More precisely, if (1) holds with 0<ε≤1 and C>μ, then on all positive integers
\[
  \tau(n)\le \left(\mu+\frac{C-\mu}{\varepsilon}\right)\log n
       +O_{C,\varepsilon,B}(\log\log(3+n)),                         \tag{1}
\]
where B is the constant in E_C(X)≤BX^{1−ε}, enlarged for bounded X. The same estimate holds among terminating starts if their restricted exceptional count satisfies the power bound. If C≤μ, even the restricted exceptional count has full upper counting exponent one, so no such power bound holds.

## The fixed-target input and the first hit

For any positive odd ternary unit y and all sufficiently large integers k, the central fixed-total positive row supplies at least c exp(Dk)/sqrt(k) distinct odd starts x≤y exp(Dk) whose path reaches y in exactly 2k shortcut steps and k odd steps. The extra terminal trit can make the starts units, at an absolute change in c. The threshold and c are uniform in y. This is the pure ternary case of the source row theorem, including its bounded first-edge change for all unit roots and induction giving positivity when the real offset bound exceeds y. All statements about ordinary inputs here already follow from that pure ternary theorem. [Weaver–Wren 48 v2, bounded-real joint atom floor and bridge](https://rstation.ai/problems/collatz/papers/48) · [Positive ordinary row and exact chronology, equations (4)–(5)](../ARITHMETIC_PROGRESSION_FLOOR.md)

If y is a terminating odd unit with y>1, the preceding path never touched 1. Otherwise y would be on the eventual cycle of 1, whose only odd state is 1. Hence τ(x)=2k+τ(y). For a nonterminating unit y, all its ancestors are nonterminating. Their count up to y exp(Dk) alone is ≫exp(Dk)/sqrt(k), contradicting any fixed power saving as k→∞. Every counterexample has a nonterminating odd unit in its future, by stripping the initial powers of two and taking the next odd state. This proves termination under (1)'s all-source hypothesis without a separate density theorem.

For the endpoint C=μ choose, for example, y=41, whose shortcut orbit reaches 1 for the first time after 69 steps, exceeding μ log41. (The orbit of 27 reaches 41 in one shortcut step.) Every central row source then has τ(x)>μ log x and there are ≫exp(Dk)/sqrt(k) of them by height y exp(Dk). Monotonicity gives the same full upper exponent at C<μ. The value 69 can be replaced by the explicit fact that the first 27 shortcut iterates of 41 all exceed 1, since μ log41<26; the finite control records the full clock.

## Sharp coefficient from central rows

Fix a terminating odd unit y>1, T₀=τ(y). When T₀−C log y is large, let k be the largest integer strictly below (T₀−C log y)/(CD−2). Every row source above is exceptional, since 2k+T₀>C log(y exp(Dk)). The assumed count implies
\[
    \varepsilon D k\le (1-\varepsilon)\log y+\tfrac12\log k+O(1).
                                                                    \tag{2}
\]
First absorb the logarithm to obtain k=O_{C,ε,B}(log(2+y)). Substitute this back and use the definition of k to get (1). Bounded k or nonpositive numerator satisfy the same conclusion by increasing the constant. For a general ordinary n write n=2^a w with w odd, b=v₂(3w+1) and z=(3w+1)/2^b. Then z is an odd ternary unit, τ(n)≤a+b+τ(z), and z≤4n/2^{a+b}. For K=μ+(C−μ)/ε≥1/log2, this gives
\[
   a+b+K\log z\le K\log n+K\log4+(1-K\log2)(a+b)
                  \le K\log n+K\log4.
\]
The log-log error at z is O(log log(3+n)). Treat z=1 directly. Thus the coefficient in (1) survives both reductions. Implication (2)⇒(1) follows by taking C large enough, and (2)⇒(3) follows from Inselmann's published implication. The reverse (3)⇒(1) is immediate.

For a limiting formulation, let L be the limsup of τ(n)/log n on the basin of 1, and s(C) the upper counting exponent of its slow tail. For μ<C<L one has
\[
      s(C)\ge\frac{L-C}{L-\mu},                                    \tag{3}
\]
where the right side is one at L=∞. Indeed every ε<1−s(C) is an admissible deficit exponent in (1). Thus unbounded logarithmic delay somewhere within the known terminating basin implies full counting exponent for every finite logarithmic slow threshold there. Conversely one strict exponent on a single such tail bounds every normalized finite delay. The existence of a strict exponent is open. The universal equivalence uses all sources, including those of infinite delay.
