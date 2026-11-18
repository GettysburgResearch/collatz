# Common clocks for the whole ternary rank ladder

**PROPOSED consequences of a source-qualified external rate.** Let \(u>1\) be odd and \(3\nmid u\), and let
\[
 y_j=(3^j u-1)/2,\qquad 0\le j\le v .
\]
Then \(y_{j+1}=3y_j+1\) and \(P(y_j)=3^j u^2\). All \(j\ge1\) are native section sources. Write \(q_t(n)\) for the odd count through \(t\) shortcut steps. A balanced merger of the ladder at \(t\) means the \(T^t(y_j)\) all agree and all \(q_t(y_j)+j\) agree. Both equalities persist under further common steps.

## External input

For adjacent Haar inputs \(z,z+1\in\mathbb Z_2\), the probability of failing to merge at a common shortcut time by \(t\) **with equal odd counts** is \(O((1+t)^{-1/2})\). We use only this upper bound. Said Duran gives the qualitative theorem; Leen states the stronger exact positive leading constant. The source inspection here checked Leen's definition of \(A\), exact-rates theorem and cylinder dictionary in the deposited TeX (SHA-256 `d2f961635d339a4b215c82b1f2f8b9ca53143043f4c58b9aa67290f46056996e`). This is a source-qualified import, without an independent formal replay. [Said Duran, September 2026](https://doi.org/10.5281/zenodo.23003524) · [Leen, October 2026](https://doi.org/10.5281/zenodo.23268751).

## Finite ordinary populations

Take \(1<u\le U\) as above. For \(v,t\ge1\), the fraction failing balanced merger by \(t\) is at most
\[
 C v/\sqrt{t+1}+O(2^t/U).                                   \tag{1}
\]
The fraction with even an ordinary *unbalanced* common endpoint at \(t\) is at most
\[
 \exp(-v^2/(2t))+O(2^t/U).                                  \tag{2}
\]
Constants are absolute. In particular, at the ordinary native precision where \(2^t=o(U)\), fusion has probability tending to zero for \(t=o(v^2)\) and probability tending to one for \(v^2=o(t)\). This is a statement about growing families of ordinary inputs, without a claim on a specified \(u\).

For (1), set \(m=y_j\). The adjacent pair \(4m,4m+1\) reaches \(m,3m+1\) after exactly two steps with initial odd counts zero and one. As a Haar root varies, the event on the class \(0\bmod 4\) has conditional failure probability at most four times the unconditional adjacent failure at \(t+2\). Thus the two rungs merge with \(q_t(y_j)=q_t(y_{j+1})+1\) except on Haar mass \(O((1+t)^{-1/2})\). Each \(y_j\) as an affine function of \(y_0\) has odd slope and preserves dyadic Haar. A union bound over the \(v\) successive pairs gives (1) on Haar.

For (2), from a Haar \(y_0=x\) consider the extreme pair \(x,3^vx+(3^v-1)/2\). On fixing the low \(k\) bits of \(x\), both current states are affine functions of its fresh Haar high part with odd slopes. Their next parities are therefore either identical or opposite with each orientation equally likely. The difference of their accumulated odd counts starts at zero and each step conditionally adds either zero or a fair sign. Its exponential moment at \(t\) is at most \((\cosh\lambda)^t\le e^{\lambda^2t/2}\). Balanced endpoint slopes require difference \(v\); optimize Markov's inequality at \(\lambda=v/t\).

For the ordinary transfers, every balanced-fusion event is a set of complete dyadic residues of \(x\) modulo \(2^t\): the word slopes agree by the count condition, so equality of the two endpoint affine functions is constant on a cylinder. The extra requirement \(3\nmid(2x+1)\) changes the limiting fraction by zero and the finite fraction by \(O(2^t/U)\), by complete CRT periods. For (2), if the extreme endpoint slopes disagree, their affine equality has at most one solution per dyadic class of \(x\), hence only \(O(2^t)\) further starts. This proves the ordinary estimates. Once the whole ladder agrees, \(y_1\) is a cheaper section witness for every rung \(j>1\), and \(y_0\) is the cheapest rung for the global \(P\)-rank.

## The minimum forward arm, with every inverse companion available

For fixed \(a\ge0\), the resistant-word fraction \(p_a\) of [the centered merger theorem](CENTERED_MERGERS.md) satisfies
\[
 p_a\asymp (a+1)^{-1/2}.                                     \tag{3}
\]
Its middle-weight binomial lower bound is internal to that theorem. For the upper bound take a single adjacent-rung pair with \(y_1=3y_0+1\). Balanced fusion by \(a\) produces a length-\(a\) centered competitor of weight one greater than the word of \(y_1\). Indeed the two affine endpoint maps in \(y_0\) have equal slopes when counts differ by one and are equal on the entire prefix cylinder. Evaluating the affine identity formally at \(y_0=-1/2\) gives the shared centered numerator. Since \(y_1\) is dyadically Haar, its \(a\)-word is uniformly distributed. Thus its resistant probability is at most the adjacent-rung failure in (1).

Let \(C_{\rm fwd}(y)\) be the minimum forward length for a strict-\(P\) merger with any positive cheaper partner and any reverse clock, allowing infinity. By [the unlimited ordinary rank obstruction](ORDINARY_RANK_OBSTRUCTION.md), for \(0\le a\le\eta v\) and sufficiently large \(v\), the ordinary limiting proportion on the exact-depth-\(v\) slice with \(C_{\rm fwd}(y)>a\) is bounded above and below by absolute positive constants times \((a+1)^{-1/2}\). First take the limit over \(U\) at fixed \(v,a\). Consequently the limiting average of \(\min(C_{\rm fwd},A)\) is \(\asymp\sqrt A\) for integral \(1\le A\le\eta v\), by summing the tails for \(0\le a<A\). This concerns the best allowed forward arm, a different quantity from the common time for full ladder stripping.
