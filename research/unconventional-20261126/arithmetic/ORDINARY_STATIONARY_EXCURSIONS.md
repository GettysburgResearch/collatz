# Low-mean stationary inverse laws on complete ordinary first descents

Use the positive shortcut \(T(2s)=s,\ T(2s+1)=3s+2\). On positive odd integers put \(U(x)=(3x+1)/2^e\) with \(e=v_2(3x+1)\). An inverse edge from \(y\) to \(x\) carries the positive label \(e\) and satisfies \(3x+1=2^e y\). The same equation defines a legal edge on \(\mathbb Z_3\). Write \(\alpha=\log_2 3\).

**Theorem S1, unconditional.** The weak finite-window limits of complete first descents ending at an odd value, as both the ordinary starting value and odd length tend to infinity, are exactly the stationary legal inverse processes of mean gap at most \(\alpha\). Every such process occurs already on triples \(n_j=3q_j\) for which both positive odd \(q_j\) and \(3q_j\) actually reach 1. With a uniform gap bound \(M\ge2\), the exact class consists of those stationary processes supported on \(1,\ldots,M\) and having mean \(\alpha\). Ergodicity is unnecessary in all these statements.

More precisely, let \((X_i,E_i)_{i\in\mathbb Z}\) be any stationary process on legal inverse edges, with positive integer labels of finite mean \(a\le\alpha\). Prescribe any function \(g(k)\to\infty\). There are arbitrarily large \(q_j\) as above satisfying all of the following.

1. Follow each \(n_j\) up to its first shortcut value strictly below \(n_j\). This is an odd value. Every earlier noninitial shortcut value strictly exceeds \(n_j\). Write \(k_j\) for the number of odd steps of the entire excursion. Then \(k_j\to\infty\) and all its division exponents are at most \(g(k_j)\).
2. Read the complete excursions in the inverse direction. The empirical laws of every fixed finite window of actual ternary states and integer labels converge weakly to those of the prescribed process. A state is recorded at the source of its labeled inverse edge.
3. The complete mean division exponent tends to \(\alpha\). If \(a=\alpha\), the empirical label distributions are uniformly integrable, so their first moments converge to the target first moment as well. If \(a<\alpha\), a vanishing fraction of added gaps accounts for the missing mean \(\alpha-a\).
4. At each \(j\) one may further prescribe a ternary residue class for \(q_j\) and a finite list of integer affine functions \(3^{d}q_j+b,\ d\ge0\). All listed sources can be chosen positive and reaching 1. The finite lists and moduli may grow with \(j\).

This realizes the process on complete first-descent histories of actual terminating triples, with the first descent only at the last shortcut. The sources vary. The construction does not supply a single orbit carrying an infinite given process, or prescribe all smaller positive starts at once.

For necessity, let \(x_0=n,x_1,\ldots,x_k\) be the odd states of such a complete excursion. The initial \(k\) states are at least \(n\). The terminal state is at least \(n/2\), since the last shortcut is necessarily a halving of a state at least \(n\). The exact odd-step product gives
\[
 0<\frac1k\sum_{j<k} e_j-\alpha
 =\frac1k\!\left[\log_2(n/x_k)+\sum_{j<k}\log_2(1+1/(3x_j))\right]
 \le \frac1k+\frac1{3n\log 2}.
\]
The label means tend to \(\alpha\) and are bounded, giving tightness of fixed label windows. Averaging inverse windows along longer and longer excursions makes a weak limit shift-invariant, since the two endpoints affect only a fixed number of windows. Legality is a closed edge condition. Lower semicontinuity gives mean at most \(\alpha\) in the limit, and equality if the labels are uniformly integrable, in particular for a fixed cap \(M\). This is independent of how the positive sources were selected.

## A finite word with its first descent at the last shortcut

First choose finite inverse-label blocks of length \(l\to\infty\) whose fixed-window frequencies and mean converge to the target's. In the ergodic case a typical path gives these directly. For a general stationary law, choose a block length \(b_j\to\infty\) and concatenate sufficiently many independent samples of that length. For each of the first \(j\) cylinder indicators on a countable determining list, the expected frequency among the within-sample windows is its stationary probability. The expected mean label equals \(a\). The law of large numbers for this finite set of bounded window counts and the integrable total gives a deterministic choice approximating all their expectations to \(1/j\). For any fixed window length \(m\), sample seams change at most a fraction \(O(m/b_j)\). One can include each bounded finite-label-window indicator obtained from a ternary-state cylinder below in the same determining list. This proves the required simultaneous approximation even for mixtures. If the target labels are bounded by \(M\), all samples may be chosen within that cap.

Reverse the block to obtain its *forward* chronological gaps. If its total exceeds \(\alpha l\), append sufficiently many ones so the new total is at most \(\alpha\) times its new length. At most \(1+\max(0,\sum E_i-\alpha l)/(\alpha-1)=o(l)\) ones suffice.

Cyclically rotate the resulting forward block to have each prefix division total at most \(\alpha\) times its length. To see this, subtract \(\alpha\) from each letter and start immediately after a maximum of the partial sums on one lap, using the nonpositive total on a wrapped prefix. Every nonempty prefix has strict inequality because \(\alpha\) is irrational. The inserted letters affect a vanishing fraction of each fixed-window count. A cyclic cut changes only the windows at its boundary. Reversal is undone when the final trajectory is read back in inverse time.

For the \(j\)-th block, repeat its rotated word sufficiently many times. Write \(N\) for the resulting length, \(A\) for its total, and \(D=\alpha N-A\ge0\). Every positive prefix still has cumulative total below \(\alpha\) times its length. Choose repetitions with \(N\to\infty\), \(N\ge j^2\), and with \(g(k)\) exceeding both the largest observed block gap and \(4j+5\) for every \(k\ge N\). This is possible even for a nonmonotone prescribed \(g\) tending to infinity. Successive periods in the repetition introduce only \(O(m/l)\) boundary exceptions in a window of fixed length \(m\).

Set \(r=\lceil N/j\rceil\) and \(b=\alpha+D/r\). Append \(r\) gaps. Their total through added position \(i<r\) is \(\lfloor ib\rfloor\), with total zero at \(i=0\). Set their final total to \(\lfloor rb\rfloor+1\). Every gap is positive and at most \(\lceil b\rceil+1\). Since \(1\le A/N\le\alpha<2\) and \(N/r\le j\), the added gaps are below \(4j+5\). Before the end,
\[
       A+\lfloor ib\rfloor \le \alpha(N+i)-D(1-i/r)
                              \le \alpha(N+i).
\]
At the end their grand total is exactly \(\lfloor\alpha(N+r)\rfloor+1\). Thus the full mean tends to \(\alpha\), and \(r/(N+r)\to0\). If \(a=\alpha\), the original empirical means converge to \(\alpha\) by construction. The complete empirical laws converge weakly to the target as proved below and their means converge to its finite mean, which gives uniform integrability for these nonnegative variables by truncation. If \(a<\alpha\), the total of the added entries divided by the full length tends to \(\alpha-a\).

For the additional fixed-cap assertion assume \(a=\alpha\) and every target label is at most \(M\ge2\). Here \(D=o(N)\). In place of the preceding terminal construction, append \(r=\lfloor D/(2-\alpha)\rfloor+1=o(N)+1\) copies of gap 2. The coefficient first crosses below one at the final complete gap and the total division excess there is strictly between zero and \(2-\alpha<1\). Strictness follows from the irrationality of \(\alpha\), which precludes an exact tie at a positive length. Thus the preceding shortcut coefficient is above one and all gaps obey the same \(M\). This proves sufficiency at the original cap.

For the resulting forward word \(e_1,\ldots,e_k\), put \(k=N+r\). The corresponding shortcut word is the concatenation of \(10^{e_i-1}\). At every proper nonempty prefix its multiplicative coefficient \(3^{\#1}/2^{\rm clock}\) exceeds one. This follows at the odd-to-odd boundaries from the strict prefix inequality; within a gap the coefficient is smallest at that gap's end. In the last gap the coefficient exceeds one immediately before its final division, because removing that division gives cumulative total \(\lfloor\alpha k\rfloor\). At the last shortcut the coefficient is strictly between \(1/2\) and \(1\). The affine additive offsets are nonnegative and fixed for this particular word. Consequently every sufficiently large positive source realizing the word stays strictly above itself until the final odd value and falls below itself precisely then. The odd parity of the final value is imposed by one further source bit, without taking a further step.

A legal inverse block satisfies \(X_i=G_{E_i}X_{i+1}\), where \(G_e(z)=(3z+1)/2^e\) multiplies ternary distances by \(1/3\). Its first \(m\) inverse labels therefore determine \(X_i\bmod3^m\) regardless of the more remote endpoint. Every fixed finite window of ternary-state residues and labels is determined by a bounded enlargement of its label window. Word repetition, rotation and the added \(o(N)\) gaps affect only vanishing fractions of these enlargements. Bounded full first moments give tightness of each finite collection of label coordinates. This proves the claimed weak convergence whenever the prescribed word is physically realized.

## Ordinary coupled realization in every compatible binary class

A finite ordinary shortcut parity word corresponds to one source class modulo the associated power of two. Fixing one additional parity at the endpoint adds one source bit. This follows by following the affine lifts: after \(h\) fixed bits, each ray \(3^d q+b\) has current value \(A+3^{d+p}t\) for the free integer parameter \(t\), where \(p\) is its number of odd steps so far. The free slope is odd. Since multiplication by 3 permutes binary residues, the prescribed upper word and final odd parity specify a binary class of \(q\) with \(3q\) realizing that full odd-gap word.

Here is an elementary extension making any two of the affine rays coincide. This uses the known affine pair chain in an existence argument. At a fixed prefix orient the two current rays as \(Y=3^hX+c,\ h\ge0,\ c\in\mathbb Z\), by taking the smaller of their two free slope exponents for \(X\). The intercept is integral. Either next parity of \(X\) is available by choosing the next original source bit. After the choice, the new free slopes are again powers of three. This remains true on swapping which ray serves as \(X\).

If \(h>0\), an even nonzero offset can be divided by two until it is odd, by choosing both current inputs even. At \(c=0\), choose both odd instead, obtaining the nonzero offset \((1-3^h)/2\) at the same grade. At an odd offset choose \(X\) odd and \(Y\) even. The grade decreases and the new offset is \((c-3^{h-1})/2\). This reaches grade zero in finitely many choices.

At grade zero, an even nonzero offset again halves by choosing both inputs even. For odd \(c\), the two mixed choices give grade one with offset either
\[
                    C=(3c+1)/2\quad\hbox{or}\quad C=(1-3c)/2.
\]
In the second choice exchange the roles of the two rays. Choose the even \(C\), which is always available modulo four and is nonzero since \(3c\ne\pm1\). Divide it by two to its odd part \(u\) using even steps, then choose the grade-decreasing mixed step. At grade zero the new offset is \((u-1)/2\), of absolute value at most \((3|c|+5)/8<|c|\) for \(|c|\ge2\). For \(c=1\) and \(c=-1\), choosing the even offset gives \(C=2\), then \(u=1\) and final offset zero. The initial case \(h=c=0\) already has equality. Iteration makes the two rays identical on the entire refined cylinder. The same operation can add one ray at a time from any preassigned finite list, since previously identical rays remain identical under the same continuation.

The common terminal on this final binary cylinder is \(A_0+3^P t\). Any prescribed independent ternary congruence on \(q\) restricts \(t\) to a ternary congruence, so the possible common terminals form another progression \(A_1+3^H z\). Choose arbitrarily large even \(J\) with
\[
                       2^J\equiv3A_1+1\bmod 3^{H+1}.
\]
Such \(J\) exist because 2 generates the units modulo every power of 3: 4 has order \(3^{d-1}\) modulo \(3^d\), by induction from \(v_3(4^{3^s}-1)=s+1\), and 2 has order two modulo 3. The residue \(3A_1+1\) enforces even \(J\). The common terminal \((2^J-1)/3\) is then a positive odd point reaching 1, in the required progression. The corresponding \(q\) may be arbitrarily large, so all lower bounds for positivity and the last strict descent can be met, and the \(q_j\) may be chosen strictly increasing. This proves S1. No positive basin density, random synchronization rate, or prior resolution of any trajectory is needed.

## Consequence of the proposed measurable entropy rigidity

**Corollary S2, conditional on the separately reviewed rigidity assertion (4) in O15.** Suppose a fixed ordinary positive odd trajectory has infinitely many distinct values. For every subsequential weak limit of its empirical inverse-edge occupancies, disintegrate the edge law over its initial state, and form the resulting stationary Markov process. At least
\[
                  \frac{a_*-\alpha}{a_*-1}>0.0885
\]
of its ergodic-component mass has zero conditional label entropy. Here \(a_*>1\) is the unique root of \(a\log a-(a-1)\log(a-1)=\log3\). At least one zero-entropy component has mean gap at most \(\alpha\). Zero conditional label entropy means that the incoming gap is a measurable function of the ternary state, almost surely. It does not require a constant gap.

Indeed, telescoping the \(n\) actual forward gaps gives
\[
 \sum_{i<n}e_i=n\alpha+\log_2(x_0/x_n)
          +\sum_{i<n}\log_2(1+1/(3x_i))\le n\alpha+O_{x_0}(\log(n+1)).
\]
The positive odd integers \(x_i\) are distinct, so the reciprocal sum is bounded by a harmonic sum. The state space is compact and the first-moment estimate gives tightness of the inverse-edge occupancies. The difference of their two state marginals tends to zero by the endpoint telescoping identity. Each weak limit is supported on legal edges and has mean at most \(\alpha\) by lower semicontinuity. The ergodic decomposition after Markovization retains the prescribed edge kernel on almost every component, as in O15.

On a component with positive branch entropy \(\beta\), O15 gives label entropy rate \(\log3+\beta\). The entropy of one positive integer label of a given mean \(a\) is at most \(a\log a-(a-1)\log(a-1)\), by comparison with the geometric law. Therefore \(a>a_*\) on every such component, whereas every component has mean at least one. Averaging proves the mass bound and the existence of a deterministic component with mean at most \(\alpha\). For a rational check of the strict separation, \(3^5<2^8\) gives \(\alpha<8/5\), and \(8^8<5^5 3^8\) implies the maximum label entropy at \(8/5\) is strictly below \(\log3\).

S1 applies even to these low-mean deterministic components. At the critical mean it realizes their finite-window laws and their first moments on complete terminating first descents. The remaining pointwise question is whether a single ordinary bad source can support such statistics indefinitely. The deterministic measurable rule, unbounded but arbitrarily slowly growing gap caps, complete finite floor excursions and joint eventual convergence of arbitrarily many supplied nearby comparisons are mutually compatible across varying sources.

The displayed decimal bound also has a direct integer certificate. The inequalities
\[
3^{100000}<2^{158499},\qquad
164179^{164179}<64179^{64179}\,100000^{100000}\,3^{100000}
\]
give \(\alpha<158499/100000\) and \(a_*>164179/100000\). The mass bound therefore exceeds \(5680/64179>177/2000\).

**Provenance.** The affine pair chain and Haar synchronization are established prior work. The forcing argument here supplies direct dense-cylinder existence, which is weaker than the known probability bounds, and uses it to impose actual ordinary termination on the prescribed excursions. Earlier shifted-power families also support long rises and smaller-source certificates. S1 differs in quantifying over every stationary legal edge law of low mean and over complete ordinary first descents. No priority claim is made for affine parity lifting, the cyclic prefix argument or finite-word realizability.

**Exact controls.** The accompanying checker follows the deterministic parity choices from all 2,570 integer pairs \(0\le h\le9,\ -128\le c\le128\), checking physical branch algebra at each step. It constructs five ordinary fused cylinders and tests actual positive members of 64 to 117 binary digits, including two-ray and four-ray inputs, ternary restrictions, a fixed phase, a two-gap period, a bounded critical mechanical block and a mixture. It checks every physical shortcut, every prescribed odd valuation, the exact first descent and the common terminal's eventual arrival at 1. The Lean module proves the physical parity formulas, all-grade finite accessibility and the resulting synchronized binary cylinder for every integral pair of the form above and every odd free slope, including orientation swaps. Its proofs use only standard kernel axioms. The limit theorem is the written proof above.

[Weaver, affine pair chain and synchronization sources, Section 2](https://rstation.ai/problems/collatz/papers/124). [Weaver, earlier shifted-power comparisons](https://rstation.ai/problems/collatz/papers/21). [Weaver, finite-precision inverse laws and slow terminating ordinary families](https://rstation.ai/problems/collatz/papers/127/v1).
