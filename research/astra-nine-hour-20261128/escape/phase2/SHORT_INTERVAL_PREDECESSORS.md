# True predecessors in a shrinking interval and a specified residue class

**PROPOSED, source-qualified written theorem.** There are absolute \(c,\delta>0\) and \(K_0\) with the following property. Let \(a\) be any positive odd integer prime to three, \(K=X/a\ge K_0\), \(M\le K^\delta\) any odd modulus, and \(u\) any residue modulo \(M\). Uniformly for \((\log K)^{-1/12}\le\epsilon\le1/2\), at least
\[
                 \frac{c\epsilon X}{(a+\epsilon^{-1})M}               \tag{1}
\]
distinct **actual odd** sources \(x\in[X,(1+\epsilon)X]\) satisfy \(x\equiv u\pmod M\) and genuinely reach \(a\). Thus when \(a\ge\epsilon^{-1}\) the bound has the local relative-size factor \(\epsilon\) times the target and progression normalization \(X/(aM)\). For fixed small targets the displayed uniform bound loses an additional factor up to \(\epsilon\). This theorem does not evaluate the complete basin density or an arbitrary outgoing branch choice. The lower bound may be smaller than one, in which case positivity still guarantees a witness.

Two inputs are used. The companion quantitative CRT theorem supplies its **selected** true inverse words at a specified nonperiodic odd unit target \(q\), for each large odd depth \(n\), \(|s-2n|\le\tfrac12\sqrt n\), progression modulo any odd \(M\le\exp(\delta_0 n)\) for a suitably decreased absolute \(\delta_0>0\), and total \(s\). Their source count is at least \(c_0 2^s/(3^nM\sqrt n)\), and they have
\[
  x=\frac{2^s}{3^n}(q-\beta),\qquad 0\le\beta\le F                   \tag{2}
\]
for an absolute \(F\). The bounded real offset belongs to the selected word assembly, including extension by an initial bounded exponent to reach every unit. An arbitrary word need not have the indicated upper bound. All coordinates and the terminal congruence refer to the one supplied target. The other input is the two-logarithm estimate used in PR213, which gives \(\|h\log_2 3\|_{\mathbb R/\mathbb Z}\ge c_1h^{-17/4}\) for integers \(h\ge1\), after weakening its exponent. [Companion selected-floor proof and (5)](../../machinery/ARITHMETIC_PROGRESSION_FLOOR.md) · [Weaver and Wren, Paper 48 v2](https://rstation.ai/problems/collatz/papers/48/v2) · [Bondareva, Luchin and Salikhov, Theorem 1](https://www.mathnet.ru/eng/cheb619)

## A target above the offset scale

Choose \(q=(2^e a-1)/3\) satisfying
\[
   q\ge\max(a,12F/\epsilon),\qquad q\ll a+\epsilon^{-1},
\]
with \(q\) an aperiodic odd ternary unit and \(Uq=a\). Start at the first exponent large enough for the lower bound and then inspect at most twelve consecutive exponents. Modulo nine the factors \(2^e\) cycle through all six units. There are multiple admissible unit children, at most one of which can be periodic. An increase of twelve in the exponent enlarges the height by at most a fixed absolute factor. This proves the assertions uniformly in \(a,\epsilon\).

Put \(L=\log K\), \(L_q=\log(X/q)\) and \(D=\log(4/3)\). Since \(q/a\ll1+\epsilon^{-1}\ll 1+L^{1/12}\), one has \(L_q=L+O(\log(2+L))\). In particular \(L_q\asymp L\) at large \(K_0\). Inspect consecutive integer depths
\[
 |n-L_q/D|\le c_2\sqrt{L_q}
\]
with \(c_2>0\) fixed sufficiently small. There are \(N\asymp\sqrt L\) of them. We seek an integer total \(s\) such that
\[
       (1+\epsilon/3) X/q\le 2^s/3^n
                              \le(1+2\epsilon/3) X/q .                  \tag{3}
\]
This asks that an irrational rotation \(n\log_2 3\), translated by \(\log_2(X/q)\), land in an arc of length
\(\log_2((1+2\epsilon/3)/(1+\epsilon/3))\gg\epsilon\).
Its initial point is arbitrary.

By the Erdős–Turán discrepancy inequality and the finite geometric sum, for any integer cutoff \(H\ge1\) the discrepancy of these \(N\) consecutive rotation points is
\[
  \ll H^{-1}+\frac1N\sum_{h\le H}
               \frac{1}{h\|h\log_2 3\|}
  \ll H^{-1}+H^{17/4}/N .
\]
Choosing \(H\) of order \(N^{4/21}\) gives \(O(N^{-4/21})=O(L^{-2/21})\), uniformly over the starting point and the tested arc. Since \(2/21>1/12\), this is \(o(\epsilon)\) uniformly in the requested range. Thus at least \(c_3\epsilon\sqrt L\) different depths admit (3). For each such depth choose one of its totals. Then
\[
 |s-2n|=|L_q-Dn+O(\epsilon)|/\log2\le\tfrac12\sqrt n
\]
after first choosing \(c_2\) and then enlarging \(K_0\). Decrease \(\delta\) to ensure that \(M\le K^\delta\) fits the selected-floor modulus budget at all these depths. Writing \(M=3^kQ\) with \((Q,6)=1\), its input condition \(k+\log Q\le\delta'_0n\) follows from a small enough absolute choice of \(\delta\).

By (2)–(3) and \(F/q\le\epsilon/12\), every selected source is between \(X\) and \((1+\epsilon)X\). It has the specified original residue and reaches \(q\), hence \(a\). One depth contributes at least \(c_4 X/(q M\sqrt L)\) sources. No source at a different depth can coincide, since a repeat visit to \(q\) would make \(q\) periodic. Multiplying by the number of admissible depths and using the upper bound for \(q\) proves (1).

The same proof allows any threshold \(\epsilon\ge(\log K)^{-\theta}\) with fixed \(\theta<2/21\), adjusting the onset. The numerical \(1/12\) keeps a margin. The Diophantine step locates genuine rows in the unaveraged spatial interval. The proof uses no distributional assertion conditional on an unbounded escaping target, so (1) retains its explicit geometric normalization even for a target of large basin density.
