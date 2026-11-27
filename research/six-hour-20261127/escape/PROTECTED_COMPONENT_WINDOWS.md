# A logarithmic protected word inside a supplied ordinary component

**Source-qualified written theorem.** Let \(B\) be a fixed complete orbit-merging class of the positive shortcut Collatz map. Alternatively take \(B=\mathcal P(a)\), the positive starts whose trajectory visits a fixed \(3\)-unit \(a\). Fix \(C\ge1\). Assuming the cited fixed-target positive lower density theorem and the scalar counted-fusion estimate below, there are \(c_B,b_B>0\) such that for every sufficiently large \(X\) and every exponent word \(w\) of length \(1\le n\le c_B\log_2 X\) starting with 1, with symbols 1 and 2 and no adjacent twos, at least
\[
                 b_B\,{X\over 2^{A+1}3^{128}},\qquad
                 A=\textstyle\sum_i w_i,                              \tag{1}
\]
members \(x\in B\cap[X,2X)\) realize that word, satisfy \(x\equiv1\bmod3^{128}\), have **no smaller positive visitor** to any site of the entire shortcut prefix at any visitor clock, and have **at most \(K(C)\) distinct** positive visitors through height \(Cx\). Here \(K(C)\) is independent of \(w,B,X\) and is given in [the all-time count theorem](COMPARABLE_ANCESTORS.md). The height limit applies only to the initial visitors. Incoming paths may be arbitrarily long and high.

This reaches a positive fraction of the logarithmic source-height clock in one specified actual component. The same word may be used in successive octaves or may vary freely with \(X\). If a counterexample exists, the assertion applies inside its actual bad component. The original positive integer varies across counted words and octaves. A component's least integer is not selected by (1). The no-consecutive-twos condition gives exponentially growing real prefixes and does not encompass all critical cycle words.

## A relative arithmetic progression estimate for basin labels

Let \(I\) be an interval of length \(Y\ge2\) of ordinary positive integers, with left endpoint at least \(Y/2\). Let \(F\) be any set of residues modulo \(P=2^\ell d\), \(d\) odd, whose relative size is \(\theta\). Let \(b(x)\in[0,1]\) be any function unchanged along ordinary shortcut edges. It is enough that it be unchanged above a fixed height \(a_0\) if \(Y2^{-t-1}>a_0\). For integer \(t>\ell\),
\[
 \left|\sum_{x\in I\cap F}b(x)-\theta\sum_{x\in I}b(x)\right|
 \ \ll\ \theta Y\left[
 \sqrt{\frac{1+\ell^2+\log(2+P)}{t-\ell+1}}
       +{2^td\over Y}+{P\over Y}\right].                              \tag{2}
\]
The implicit constant is absolute and independent of the label and of the size or shape of \(F\). Intervals with nonintegral endpoints cost \(O(\theta P)\) at the boundary. The error is relative to the periodic population, so the formula also controls a single very rare arithmetic class. For a rare label to have a relative error itself, its own octave mass must dominate the bracket.

Here the external input is Weaver's uniform scalar estimate for counted fusion of two Haar shortcut paths. From a canonical pair \((z,3^k z+c)\), normalized offset \(V=|c|/3^k\), unfused probability at additional clock \(s\) is \(\ll\sqrt{(1+k^2+\log(2+V))/(s+1)}\). Its deterministic one-step recursion gives \(V'\le(3/2)V+1/2\), and the count gap changes by at most one. Weaver also gives periodic transport of counted fusion. Fixed-modulus independence for predecessor population estimates predates the present relative growing-modulus estimate. [Paper 124/v1, (4), Lemma 2 and (18)](https://rstation.ai/problems/collatz/papers/124/v1) · [Paper 12, Lemma 2 and (12)](https://rstation.ai/problems/collatz/papers/12)

Fix a translation \(0\le j<P\) and an individual source residue in \(F\). The first \(\ell\) dyadic digits fix both parity prefixes of \(x,x+j\). The resulting pair has count gap at most \(\ell\) and normalized offset at most \((3/2)^\ell(j+1)\). The canonical anchor is an affine function with odd slope of the unread bits, hence Haar-uniform under conditioning on this dyadic prefix. The quoted estimate bounds the conditional probability of no fusion by time \(t\) by the square-root term in (2) times an absolute constant. On the actual residue modulo \(P\), the next \(t-\ell\) binary digits run through their complete set in every \(2^{t-\ell}\) consecutive progression indices, since \(d\) is odd. Counted fusion is determined by the first \(t\) bits. Summing over the \(\theta P\) selected residues, the failure count on \(I\cap F\) is at most \(O(\theta Y)\) times that square-root term plus \(O(\theta 2^t d)\), uniformly in \(j\). Successful pairs have \(b(x)=b(x+j)\); every transported site is above \(a_0\) until fusion under the displayed extra condition, since each shortcut is at least a halving.

Average \(1_F(x)b(x+j)\) over \(j=0,\ldots,P-1\). Away from the two interval ends, each shifted site receives exactly \(\theta P\) terms. At most \(2P\) boundary sites lose or gain weight at most \(\theta\) after normalization. This proves (2). The argument compares labels at each fixed shift and averages them; simultaneous coalescence of a whole block is unnecessary.

## Transfer on the terminal progression

For any complete merging class \(B\), take a unit in the class (one odd departure from an odd multiple of three already gives a unit). Its positive predecessors lie in \(B\) and have positive lower natural density by the fixed-target theorem. The same applies directly to \(\mathcal P(a)\) with \(3\nmid a\). Choose \(e>0\) with \(\#(B\cap[1,Y])\ge eY\) at all sufficiently large \(Y\). Doubling preserves membership in \(B\) in the forward implication \(x\in B\Rightarrow2x\in B\). At least \(eY/2-O(1)\) members lie in \([eY/2,Y]\). Send each to its unique dyadic multiple in \([Y,2Y)\). Every image has at most \(1+\lceil\log_2(4/e)\rceil\) preimages from that interval. Thus \(\#(B\cap[Y,2Y))\ge\delta Y\) eventually, for example with \(\delta=e/[4(1+\lceil\log_2(4/e)\rceil)]\). For a fixed target the sole possible failure of forward invariance of its indicator is at \(a\) itself. The external positivity is qualified in [the earlier transfer and source audit](UNRESTRICTED_VISITORS.md). [Wren, Paper 10/v3, Theorem 1 and its joint-mixing input](https://rstation.ai/problems/collatz/papers/10/v3) · [Mazur, fixed-target proof record](https://www.proofatlas.ai/formalizations/positive-lower-density-collatz-predecessors/)

Round \(C\) up to an integer. Write \(g=3^n2^{-A}\) and \(d_w=\sum_{j<n}2^{A_j}3^{-j-1}\), so \(U^n(x)=g(x+d_w)\) with \(1\le g\le(3/2)^n\) and \(0\le d_w\le5\). The exact source cylinder has the form \(x=r+2^{A+1}u\). At its terminal it is \(y=s+2\cdot3^n u\) for one integer \(s\). The ordered bijection from permitted source residues to their integer terminals is exact on
\[
         X\le x<2X,\qquad
         Z+gd_w\le y<2Z+gd_w,\qquad Z=gX.                            \tag{3}
\]
The terminal interval differs from the comparable octave \([Z,2Z)\) by at most \(2gd_w+2\) integers, negligible compared with \(Z\) uniformly in \(w\).

For a shortcut visitor deadline \(J\ge\max(A,128)\), require the two tests in (5) of [the all-time count](COMPARABLE_ANCESTORS.md) through that deadline, together with the ternary source ball. On the dyadic cylinder and \(x>4\cdot36^J\), these are tests modulo \(3^J\). A candidate inverse word of \(\ell\le J\) shortcut steps with grade \(r'\) has positive source
\[
 u={2^\ell3^nx+2^\ell D_w-2^A D'\over 2^A3^{r'}},
 \qquad 0\le D_w<3^A,\quad 0\le D'<3^\ell ,
\]
where the affine numerators are those of the two forward words. The intercept numerator has absolute value at most \(2\cdot6^J\), and the denominator is at most \(6^J\). Comparisons against either \(x\) or the integer \(Cx\) have integral cleared leading coefficient. For a comparison between any two inverse candidates, putting them over a common denominator costs at most \(4\cdot36^J\) in absolute intercept difference. Every unequal-slope comparison, including a possible coincidence between distinct words, is therefore settled beyond the stated threshold. Equal slopes have constant ordering. Counting distinct sources and checking their inclusions in the two height windows then depend only on ternary legality on the given dyadic cylinder.

The uncapped Haar argument in (6)–(7) and the finite competitor count give at least \(0.98\cdot3^{J-128}\) passing source residues modulo \(3^J\) on this dyadic cylinder. Under (3) these are precisely as many distinct residue classes in a periodic terminal test of modulus \(P'=2\cdot3^{n+J}\). Its density \(\theta\) is at least \(0.98/(2\cdot3^{n+128})\). In particular \(\theta Z\ge0.98X/(2^{A+1}3^{128})\). Applying (2) there incurs binary precision only \(\ell=1\). Terminal invariance gives \(1_B(x)=1_B(y)\); for \(\mathcal P(a)\), every original prefix site stays above \(a\) for large \(X\), since the no-consecutive-twos word starting with 1 has odd prefixes of gain at least one and intermediate shortcut states stay above the lower of the adjacent odd states. The comparison paths for (2) also stay above \(a\) at the deadline below.

Here are explicit simultaneous choices of scales. Set \(k=\lfloor\log_2X\rfloor\), \(a_*=1-H_2(\log_3 2)>0\), \(L=\lceil4/a_*\rceil\) and
\[
            J=\lceil L(n+1)+\sqrt k\rceil+128,\qquad
            t=\lfloor(\log_2 Z)/2\rfloor .
\]
Let \(M\ge1\) be an absolute constant large enough to bound the square-root error in (2), after changing logs to base two, by \(M\sqrt{(1+\log_2 P')/\log_2 Z}\) when \(\ell=1\) and \(t\) is as chosen. With \(\eta=H_2(3/5)\), one can take any fixed positive \(c_B\) satisfying
\[
 \begin{split}
  &c_B<1/(8(L+2)\log_2 36),\\
  &c_B<\delta^2/[256 M^2 (L+2)\log_2 3],\\
  &c_B<(1-\eta)/[4(2+\eta\log_2(3/2))].
 \end{split}                                                         \tag{4}
\]
Uniformly for \(n\le c_B k\) and sufficiently large \(X\), one has \(4\cdot36^J<X\), \(P'<Z^{1/4}\), \(Z2^{-t-1}>a\) for any fixed \(a\), and the bracketed error times its constant in (2) is at most \(\delta/3\). The two terms involving the period have polynomial decay. Therefore the finite test contains at least \((\delta/2)\theta Z\) actual members of \(B\) after enlarging the onset. This step uses the positive lower fraction \(\delta\) in actual terminal octaves; no global density limit for \(B\) is needed.

It remains to remove the visitor deadline uniformly in the word. The small-clock part of (4) in [the all-time count](COMPARABLE_ANCESTORS.md) bounds arrivals with \(J<t'<k\) by \(O_C(X2^{-a_*J})\), since the visitor source is at most \(2CX\) and every counted terminal is at least \(X\). For \(t'\ge k\), compress the source image at \(k\) into \(O_C(X^\eta)\) full orbits. Apply the orbit-union inequality at the terminal horizon \(\lfloor\log_2(3Z)\rfloor\) to all terminals in \([1,3Z]\), giving \(O_C(Z^\eta+X^\eta\log(3Z))\) possibilities. The source-to-terminal map is injective within this word. Relative to \(X2^{-A-1}3^{-128}\), these three errors tend to zero uniformly: \(A\le3n/2\), \(a_*L\ge4\), \(J\ge L n+\sqrt k\) and \(Z\le X(3/2)^n\). The last inequality in (4) supplies a strict power saving for the high-clock errors. This proves (1), for instance with \(b_B=\delta/4\) after enlarging the onset.

## Delayed actual mergers and directed cuts

Fix a complete component \(B\) with lower density bound \(e\) above, and choose any fixed \(C>3/e\). For large \(x\) at least \(eCx-x-O(1)\) members of \(B\) lie in \([x,Cx]\). They all eventually share an ordinary future with \(x\). For every selected \(x\) in (1) at most \(K(C)\) of them ever hit **any** observed site through the prescribed prefix. All remaining members first meet its orbit later than that prefix on the clock of \(x\), even with unlimited visitor time. This statement holds in the basin of 1 under the public fixed-target input, and in each putative bad component under the same input. It does not exclude late mergers onto the particular ray of a least bad integer.

There is a separate actual restriction of Paper 227's directed cut. For any of its fixed admissible affine comparisons with two positive linear endpoints and exponent \(B_0\), suppose \(N(X)/(X/(\log X)^{B_0})\) is unbounded for the directed failures of an invariant coloring. For fixed \(C\), discard failures where either endpoint \(y\) has \(\pi_y(Cy)>(1+\log(2+y))^{B_0+2}\). The discarded inputs through \(X\) number \(O_C(X/(\log X)^{B_0+2}+X^\eta(1+\log X))\) with constants depending also on the fixed comparison and \(B_0\). Indeed (3) of the [all-time count](COMPARABLE_ANCESTORS.md) applies on dyadic terminal octaves, and each affine arm is injective on its fixed parameter progression. The directed lower subsequence survives. Consequently the level-cut proof still supplies arbitrarily cheap finite paths using allowed edges with this true all-clock local sparsity, whenever the cut lower bound holds for every nonconstant invariant coloring with the same exponent. This is an existence consequence. The unrestricted predecessor upper predicate has no decidability certificate here, so the effective membership conclusion of Paper 227 is not transferred. [Paper 227/v1, §§2–3](https://rstation.ai/problems/collatz/papers/227/v1)

The local lower count needed by [the rational source sector](RATIONAL_SOURCE_SECTOR.md) concerns a least bad height and its complete component up to a comparable cutoff. The logarithmic-prefix statement controls a population at heights tending to infinity inside that component; its onset and \(c_B\) depend on the component's mass. It gives no \(m^{0.95}\) population at the least height. The rational sector itself conditions at binary precision comparable to the logarithm of its source population and forces an almost equally large ternary denominator. Applying (2) at that original boundary gives no small error.

