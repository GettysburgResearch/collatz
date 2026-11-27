# Posterior probability of an ordinary valuation word at its own future target

**Source-qualified written theorem.** Let \(m\) be any positive odd integer, let \(y_k=U^k m\) under the odd Collatz map, and let \(A_k(m)\) be the sum of the first \(k\) actual valuations \(e(x)=v_2(3x+1)\). Write \(p_k(r)\) for the probability of ternary residue \(r\bmod 3^k\) from \(k\) independent positive geometric exponents of mass \(2^{-e}\). Set
\[
 R_k(m)=2^{A_k(m)}p_k(y_k\bmod 3^k).
\]
This is the reciprocal conditional probability of the *particular* valuation word of \(m\), given its endpoint residue. Suppose the cited uniform ternary atom floor holds. The following dichotomy retains the fixed positive ordinary source and its actual odd and physical clocks.

* If \(m\) escapes, \(R_k(m)\) increases to a finite positive number equal to the corrected reciprocal mass of its entire synchronous odd-clock class.
* If \(m\) is eventually periodic, \(R_k(m)\to\infty\) at least exponentially in \(k\).

The endpoint and both clocks move with the source. The ordinary critical trace at a *fixed* positive integer and a depth average is prior work. The rank-one corrected heights and synchronous classes used below are also prior project results. [Valbuena, canonical stationary trace](https://github.com/x1xhlol/collatz-two-coordinate-obstruction/blob/main/paper/positive-stationary-envelope.tex) · [Earlier synchronous-class arithmetic and corrected heights](https://github.com/GettysburgResearch/collatz/blob/a1379492dbaae85e0d16662b41ccc7176ab3c66e/research/astra-global-synthesis-20261124/section/proof.md)

## An ordinary antichain estimate from the atom floor

The external input is El Jaouhari's uniform finite-residue bound in the whole-Haar normalization
\[
 \rho_k(r):=3^k p_k(r)\ge\alpha>0\qquad(3\nmid r,\ k\ge1).
\]
Here is the source arithmetic behind the bound we use on ordinary integers. At any positive odd \(a\), a legal inverse word yields a unique positive odd source by successive \((2^e y-1)/3\). For a nonperiodic odd unit target the depth at which any one source \(x\) reaches \(a\) is unique. The weight \(3^k2^{-A_k(x)}\le a/x\) follows from the positive affine relation. Thus \(\sum_{k=1}^K\rho_k(a)\ge\alpha K\) is a sum of weights of distinct actual sources. If \(x>\exp(8K)\), its exponent sum exceeds \((8K-\log a)/\log2\). For the geometric law \(\mathbb E(4/3)^e=2\). Dropping the ternary congruence and using Markov's inequality, these far sources contribute at most
\[
 a^b e^{-8bK}\sum_{k=1}^K6^k=o_a(1),
 \qquad b=\log_2(4/3),\quad 8b>\log6.
\]
Putting \(K=\lfloor(\log X)/8\rfloor\) gives the relative odd lower logarithmic-density bound
\[
 \liminf_{X\to\infty}\frac{2}{\log X}
 \sum_{\substack{x\le X\text{ odd}\\ x\text{ reaches }a}}\frac1x\ \ge\ \frac{\alpha}{4a}.
\]
This is Weaver's written argument from Input D. Its additional identification with ordinary natural density uses a separate density-existence input C. The harmonic bound suffices here. [Weaver, paper 12, §2, equations preceding (4)](https://rstation.ai/problems/collatz/papers/12)

Fix one escaping component \(C\), and choose an odd root \(m\) in it. Give each odd \(x\in C\) its integer grade \(j(x)=i-t\) whenever \(U^t x=U^i m\). Acyclicity makes this independent of the choice. At any fixed grade \(v\) the distinct odd targets form an antichain: if an orbit visited two of them at separate times, their grades would differ by that time difference. In particular, all ordinary odd predecessor sets of distinct unit targets of that grade are disjoint. Sum the preceding lower harmonic bound over a finite subset and compare with the total odd harmonic sum \(\sim(\log X)/2\). Taking the supremum over finite subsets gives
\[
 \sum_{\substack{x\text{ odd in }C\\j(x)=v,\ 3\nmid x}}\frac1x\le \frac4\alpha .
\]
Every odd \(x\) divisible by three maps to a unit \(y=U(x)\) of grade \(v+1\). With the corrected height \(P(Ux)=3\,2^{-e(x)}P(x)\), all inverse contributions of this kind at one such \(y\) have total at most \(3/P(y)\), since there is at most one \(x\) for each \(e\ge1\). Also \(P(x)\ge x\). Consequently, uniformly at every integer grade,
\[
 Z_v:=\sum_{\substack{x\text{ odd in }C\\j(x)=v}}P(x)^{-1}\le16/\alpha.
 \tag{1}
\]
Even towers multiply this bound by at most two if the grade of a positive even integer is defined by its odd part.

## Moving the target

For a positive odd integer \(y\), ordinary unfolding of the ternary coding gives
\[
 p_k(y)=\sum_{U^k x=y}2^{-A_k(x)}
 \tag{2}
\]
over positive odd \(x\). Integrality of the final inverse endpoint is equivalent to the coding congruence; all intermediate inverse values are positive odd integers. Each source determines its one finite valuation word. At \(y_k=U^k m\) the ratio of the word weights in (2) is
\[
 2^{A_k(m)-A_k(x)}=P(m)/P(x).
\]
The ordinary source sets \(\{x:U^k x=U^k m\}\) increase with \(k\), and their union is precisely grade zero. Therefore
\[
 R_k(m)\uparrow P(m)Z_0<\infty
 \tag{3}
\]
by (1). The actual word retains conditional probability at least \(1/(P(m)Z_0)\) at every depth. For an eventually periodic positive \(m\), any full odd cycle lap of length \(l\) and valuation sum \(S\) has \(3^l/2^S<1\), by its strictly positive affine offset. Its forward odd states are units after the initial step. The same external atom floor now gives \(R_k(m)\ge\alpha 2^{A_k(m)}/3^k\), bounded below eventually by a positive source-dependent constant times \((2^S/3^l)^{k/l}\). This proves the dichotomy. The persistence of the actual source sets, the disjointness of their predecessors for an injective orbit and the ratio identity are algebraically checked in [OddPosterior.lean](OddPosterior.lean).

The ordinary-positive obstruction can be phrased at a single residue per depth. Since \(P(y_k)=3^k2^{-A_k(m)}P(m)\), equation (3) is equivalent to \(\rho_k(y_k)/P(y_k)\to Z_0\). For escape \(P(y_k)/y_k\to1\), since the correction product along the remaining distinct orbit tends to one. Hence escape produces a sequence \(y_k\to\infty\), \(y_k/3^k\to0\), on which \(\rho_k(y_k)/y_k\to Z_0>0\). The known stationary trace at a fixed target gives no uniform upper bound on this sequence. At fixed negative or rational ternary points different behavior is possible.

## A signed integer control

The signed odd Collatz map fixes \(-1\), with exponent one each time. Its ratio \(2^k p_k(-1)\) is bounded. To see this, list the negative odd sources \(-x\) at their first arrival at \(-1\) after \(t\) odd steps. The contribution of each such source to the ratio at every \(k\ge t\) is \(2^{t-A_t(-x)}\), because subsequent exponents are one. For \(t>0\) the earlier odd input magnitudes \(a_i\ge2\) are distinct. The reflected product argument gives
\[
 (3^t2^{-A_t(-x)})x
 =\prod_{i<t}\frac{3a_i}{3a_i-1}\le t+1 .
\]
When \(A_t\le6t\), the sources obey \(x\le(t+1)2^{6t}\). Their harmonic sum is \(O(t+1)\), so this part of the ratio increment is \(O((2/3)^t(t+1)^2)\). When \(A_t>6t\), dropping the congruence costs at most \(2^t\Pr(A_t>6t)\le[4(3/4)^6]^t\). The two bounds sum over all \(t\). This control has the same finite ternary coding and an actual periodic signed-integer trajectory. Positivity in the periodic part of the dichotomy is essential.

## The remaining ordinary question

Any one of the following would exclude positive-integer escape: unbounded \(R_k(m)\) for each positive odd \(m\); or a uniform \(\rho_k(r)/r\to0\) for positive unit residues \(r\to\infty\) with \(r/3^k\to0\). The second statement is sufficient and may be stronger. A lower bound on the unconditioned entropy of the geometric word does not supply either statement. A single highly atypical word can have high conditional probability at its own residue, as the signed integer control shows. Nontrivial positive cycles require a separate exclusion.

## The recovered ordinary source and the change of path measure

The conditional law in (2) can be coupled across all depths without an asymptotic estimate. Let $S_k=\{x:U^kx=y_k\}$ and $L_0=\bigcup_k S_k$. On the fixed countable space of positive odd integers the conditional source has law
\[
 Q_k(x)=\frac{1_{S_k}(x)/P(x)}{\sum_{b\in S_k}1/P(b)}.
\]
Thus $Q_k$ is the conditional restriction to $S_k$ of the probability $Q(x)=1_{L_0}(x)/(P(x)Z_0)$. Its total variation distance from $Q$ is exactly $1-Q(S_k)\to0$. Under this coupling the excess physical clock $A_k(x)-A_k(m)$ has the limiting law of $\log_2(P(x)/P(m))$ for $x\sim Q$, with convergence in total variation. Indeed the two quantities are already equal on $S_k$. The forward affine intercept at the target is $B_k(x)=y_k-3^k2^{-A_k(x)}x$. Its fraction of the actual target size converges in distribution to $1-x/P(x)$, since on $S_k$ the fraction equals $1-(P(y_k)/y_k)x/P(x)$ and $0<x/P(x)\le1$. These laws retain the original ordinary preimage as a marked random variable.

There is a corresponding exact likelihood on the space of *unconditioned* infinite words. Let $L_v$ be the entire odd grade $v$ and put, for $v\ge0$,
\[
 f_v(z)=3^v\!\sum_{x\in L_v,\ x\equiv z\bmod3^v}1/P(x),\qquad z\in\mathbb Z_3.
\]
Start at any fixed ternary point and apply the forward maps $z\mapsto(3z+1)/2^{e}$ with independent exponents of probability $2^{-e}$, obtaining $z_v$. The residue of $z_v$ modulo $3^v$ depends only on the first $v$ exponents. For a particular word $w$ with sum $A$ and terminal residue $r$, its iid probability times $f_v(r)$ satisfies
\[
 2^{-A} f_v(r) = \sum_{b\in L_0:\text{ actual first }v\text{ exponents equal }w}1/P(b).
 \tag{4}
\]
To see this, each ordinary $x\in L_v$ in residue $r$ pulls back along $w$ to one positive odd $b\in L_0$. Conversely, each such $b$ supplies exactly that $x$. The corrected weights on either side agree term by term. At $v=0$ the common total is $Z_0$.

Consequently $f_v(z_v)/Z_0$ is the finite-cylinder likelihood ratio of the countable atomic path law $\sum_{b\in L_0}Q(b)\,\delta_{\mathbf e(b)}$ against the iid geometric law. It is a nonnegative martingale of mean one. It converges to zero iid-almost surely because every fixed infinite word has iid probability zero. For an elementary proof, remove a finite set of atoms of total path-law mass at least $1-\epsilon$. Their likelihood contributions eventually vanish on almost every iid path. The remaining nonnegative martingale has expectation at most $\epsilon$, and Fatou bounds the expectation of its limit by $\epsilon$. Let $\epsilon\downarrow0$. This explicitly identifies the lost mass in a martingale approach to ordinary support. It also shows why constant expectation over iid paths alone cannot give a positive limit on their typical paths.

The fixed-depth inverse identity underlying (2) is also used by [Weaver, Paper 176](https://rstation.ai/problems/collatz/papers/176). The countable source coupling, the path law in (4), and the moving-index profile in [the companion boundary proof](../boundary/TRACE_PROFILE.md) work at different quantifiers from a fixed-root depth average.

There is also a converse concentration at the terminal cylinder. Write $B_n=y_n+3^n\mathbb Z_3$ and let $w_n$ be the true first $n$ exponents of $m$. Among the paths in (4), the event of beginning with $w_n$ decreases to the single source $m$: agreement on that prefix determines the odd source modulo $2^{A_n(m)+1}$, and distinct ordinary integers cannot agree at arbitrarily large binary precision. Thus (4) gives
\[
 P(y_n)\sum_{x\in L_n\cap B_n}1/P(x)\longrightarrow1.
\]
The single ordinary target $y_n$ supplies the leading term on the left. Under the atom-weighted path law $Q$, the probability of the ternary terminal residue $B_n$ tends to one, since each fixed $b\in L_0$ eventually has $U^n b=y_n$ and $Q$ is a probability on that countable set. Equivalently the probability assigned to $B_n$ by the finite law with density $f_n/Z_0$ against the stationary ternary law tends to one. The argument couples the original positive binary source and the same moving ternary target at full precision.
