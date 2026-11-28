# All-clock arrivals from nearby sources at nearby positive targets

**PROPOSED written results.** The shortcut map is \(T(2m)=m,\ T(2m+1)=3m+2\). Heights, sources, and targets below are positive ordinary integers. We count distinct **targets**. The two visitors may initially choose their clocks independently, with no bound on either clock or on intermediate heights.

The first conclusion is that genuine clock or odd-grade mismatches are power-sparse among nearby target pairs, even when both displacements are chosen after seeing the trajectories. The second conclusion identifies the all-clock density of targets admitting a pair of strictly smaller adjacent visitors, with a polynomial error and a ternary description. The last section gives the arithmetic limit of using such visitors to descend a least bad source.

## 1. All late dates at once

Use \(I_R=\{1,\dots,\lfloor R\rfloor\}\). For integers \(J\ge1\) write \(M_J(R)=|T^J(I_R)|\). There is an absolute constant \(C\) such that

\[
 M_J(R)\le C\big(R\,2^{-J/40}+2^J\big).
 \tag{1}
\]

Indeed words with at least \(3J/5\) odd departures occupy at most \(2^{H_2(3/5)J}\) dyadic classes, each having at most \(1+R/2^J\) representatives. Every other word has image in a single ordinary interval from one through \(R(3^{3/5}/2)^J+(3/2)^J\). Here the largest additive numerator of a length-\(J\) word is \(3^J-2^J\), by induction with the all-odd word. The two strict estimates \(2^{H_2(3/5)-1}<2^{-1/40}\) and \(3^{3/5}/2<2^{-1/40}\) follow by raising to power 40, giving respectively \(5^{40}<2^{55}3^{24}\) and \(3^{24}<2^{39}\).

For a union \(\mathcal U\) of \(N\) full positive orbits, Weaver's elementary orbit-union estimate is

\[
                |\mathcal U\cap I_R|\le M_J(R)+2NJ.                 \tag{2}
\]

For completeness, insert the orbits in order. Each new orbit contributes a simple path to the previous union, an infinite simple ray, or a simple path to a new cycle together with that cycle. Partition these new states into at most two pieces per orbit. From each finite transient path delete its last \(J\) states, or the whole path if shorter. On the remaining states \(T^J\) is injective within each piece and its images stay in that piece. Cycles and infinite rays require no deletion. This proves (2) by counting the images of the remaining states in \(I_R\). Both the orbit-union estimate and the entropy/image argument preceding it appear in Weaver, Paper 177, section 7. [Original version](https://rstation.ai/problems/collatz/papers/177/v1)

For arbitrary positive real cutoffs \(S,R\), put

\[
 L_J(S,R)=\{y\in I_R:\ y=T^t(x)\text{ for some }x\in I_S,\ t\ge J\}.
\]

The complete set \(L_J\) is covered by the full forward orbits of the \(M_J(S)\) possible states at date \(J\). Consequently

\[
              |L_J(S,R)|\le M_J(R)+2J M_J(S).                     \tag{3}
\]

In particular the upper density of all such late targets with \(S,R=O(Y)\), normalized by \(Y\), is \(O(J2^{-J/40})\) as \(Y\to\infty\). This works without any lower bound along a path, any parity constraint at arrival, or any assumption on its eventual fate. In the application below we take \(J=\lfloor(2/5)\log_2Y\rfloor\). Even with \(S=O(Y^{1+1/1000})\) and \(R=O(Y)\), equations (1)–(3) give

\[
              |L_J(S,R)|\ll (1+\log Y)Y^{1-9/1000}.                \tag{4}
\]

## 2. Late and unequal-clock visits among nearby pairs

For every sufficiently large \(Y\), all but \(O(Y^{1-1/200})\) choices of \(y\in[Y,2Y]\) satisfy the following simultaneous statement. Select any positive \(x,x+h\le 3Y^{1+1/1000}\) and any positive \(y+k\) with \(|h|,|k|\le Y^{1/1000}\). If

\[
                      T^i(x)=y,\qquad T^j(x+h)=y+k,
\]

then \(i=j<J\) and the two prefixes have the same odd count. This holds simultaneously over all dates, sources, and adaptive signed displacements in the stated ranges.

If \(i\ge J\), apply (4) directly. If \(j\ge J\), then \(y+k\) lies in (4) with \(R=3Y\); the union of at most \(2Y^{1/1000}+1\) translations of that set costs \(O((1+\log Y)Y^{1-8/1000})\). This is within the asserted exceptional count.

For the remaining \(i,j<J\), write the two affine expressions as \(A x+B\) and \(A'(x+h)+B'\). The two slopes have denominators dividing \(2^J\), all slopes are at most \((3/2)^J\), and both nonnegative intercepts are at most \((3/2)^J\). If \(A\ne A'\), their separation is at least \(2^{-J}\). Subtraction then gives

\[
  x\le 2^J\big(|k|+(3/2)^J(|h|+1)\big),\qquad
  y\ll (9/2)^J(1+|h|+|k|).
\]

This contradicts \(y\ge Y\), since \((2/5)\log_2(9/2)+1/1000<1\). Equal slopes \(3^p2^{-i}=3^q2^{-j}\) force \(i=j,\ p=q\) by unique factorization. This small-clock argument is pointwise, so adaptively choosing millions of possible source displacements introduces no further loss.

In particular a deterministic target mark of size \(\gg Y/(\log Y)^B\) on an unbounded sequence of octaves inherits this conclusion with relative error \(o(1)\), for every fixed \(B\). The assertion concerns incoming pairs that actually exist. It does not give the marked targets any incoming pair other than the date-zero pair.

## 3. Complete density law of smaller adjacent visitors

Let \(P(y)\) mean that some adjacent positive \(x,x+1<y\) visit \(y,y+1\), one source per target in either order, at arbitrary finite clocks. We use the order in which \(m\) denotes the source visiting the lower target \(y\), and \(m+\delta\) visits \(y+1\), where \(\delta\in\{-1,1\}\).

For a length-\(t\) word \(w\) write its affine map \(F_w(m)=(3^qm+C_w)/2^t\), with \(q\) odd departures. Its binary source cylinder determines the length-\(t\) word \(v\) of \(m+\delta\). Retain \((w,\delta)\) when \(v\) has the same odd grade \(q\), when

\[
                  3^q\delta+C_v-C_w=2^t,\qquad g=3^q/2^t>1,        \tag{5}
\]

and attach the ternary ball

\[
                  U_w=\{z\in\mathbb Z_3: 2^tz=C_w\bmod 3^q\}.
\]

Let \(\mathcal A=\bigcup U_w\), over both signs and all positive \(t\) satisfying (5), and let \(\pi\) be ternary Haar probability. On a uniform integer octave \(Y\le y<2Y\) we have

\[
          \Pr(P(y))=\pi(\mathcal A)+O(Y^{-1/200}).                  \tag{6}
\]

More strongly, the complete set of all successful clock/word/orientation triples for \(P(y)\) has total variation distance \(O(Y^{-1/200})\) from the set of all retained triples whose ternary ball contains one Haar point. On the integer side include the independently chosen two clocks; on the ternary side use the common clock twice.

To prove this, use the same \(J\). For \(t<J\), we have \(3^J=o(Y)\). Given \(y\in U_w\cap[Y,2Y)\), the exact equation \(m=(2^ty-C_w)/3^q\) gives an integer, positive in this range, and the equality modulo \(2^t\) forces its first-arm word. If \(g>1\), then \(y-m\ge Y/3^q>1\), so both sources are below \(y\). Equation (5) gives the second actual endpoint. For \(g<1\), \(m-y\ge(Y-C_w)/3^q>0\). Equality \(g=1\) occurs only at clock zero, which cannot give two strictly smaller sources. These facts identify all short equal-slope solutions, including every word, orientation, and clock. Section 2 removes all other actual arrivals except on the stated power-sparse target set.

The truncated marked set depends only on \(y\bmod 3^J\). Couple the integer target residue and the residue of a ternary Haar point with error \(O(3^J/Y)\). The chance of any omitted ternary mark is bounded directly by summing the masses of legal words. At each \(t\), (5) requires \(q>(\log_3 2)t>3t/5\) and gives \(3^{-q}<2^{-t}\). There are at most two orientations per first-arm word, so the sum is at most \(2(2^{H_2(3/5)-1})^t\). Summing for \(t\ge J\) costs \(O(2^{-J/40})=O(Y^{-1/100})\). This proves the total variation statement and (6).

The two targets are consecutive ternary units in every retained ball since both completed words contain an odd departure. Therefore \(\mathcal A\subset1+3\mathbb Z_3\). Conditional on \(y\equiv1\bmod3\), one has the explicit range

\[
                 2/3^6 \ \le\ 3\pi(\mathcal A)\ \le\ 3/5 .         \tag{7}
\]

For the lower bound the two extremal clock-11 cylinders give distinct lower targets \(205,991\bmod3^7\). For the upper bound take the set of first-arm words appearing in (5) with either orientation, and read them in reverse. Discard any member with a shorter prefix in that same reversed set. Legality of a longer inverse word implies legality of each prefix, and the discarded full ball is contained in the shorter ball. The remaining language is prefix-free. Under independent inverse letters with odd-inverse probability \(3/4\), the probability of a length-\(t\), grade-\(q\) word is \(g^2 3^{-q}\). The first non-doubling inverse at a root in \(1+3\mathbb Z_3\) must come after an odd number of doublings. The total probability of this initial pattern is \(\sum_{j\ge0}(1/4)^{2j+1}(3/4)=1/5\). Thus the sum of the prefix-free word probabilities is at most \(1/5\); their individual Haar masses are smaller since \(g>1\). Weaver's squared-gain tilt and one-root stopping bound are prior work in Paper 177, section 7. The initial-pattern and two-target restrictions are used here at the actual incoming pair.

## 4. The threshold at a least bad source

At a possible least bad source \(n=4j+3\), use \(y=(3n-1)/2=6j+4\). One has \(Tn=y+1\) and \(T(y)=y/2<n\). A pair of adjacent visitors reaching \(y,y+1\) with **both** sources below \(n=(2y+1)/3\) excludes this \(n\). For a uniform \(y\equiv4\bmod6\) in an octave, the density of possessing this all-clock certificate is

\[
                  3\pi(\mathcal A_{3/2})+O(Y^{-1/200}),
       \qquad  2/3^7\le 3\pi(\mathcal A_{3/2})\le 4/15,             \tag{8}
\]

where \(\mathcal A_{3/2}\) uses (5) with \(g>3/2\). The same argument applies: for \(t<J\), the difference \(3\cdot 2^t-2\cdot3^q\), if nonzero, has magnitude at least one. The offset \(C_w\) and the fixed rounding and unit-displacement errors are all \(O(3^J)=o(Y)\) after clearing denominators. The only equality \(3^q/2^t=3/2\) has \(q=t=1\); adjacent starts cannot both be odd at that date. Fixed parity and the ternary class are imposed together by the Chinese remainder theorem, with the same \(O(3^J/Y)\) truncation error. The clock-12 balls give the lower bound. In the prefix-free upper argument each retained Haar mass is at most \(4/9\) of its tilted word probability, which gives \((3/5)(4/9)=4/15\).

It follows that even among the correct ordinary candidate positions, at least \(11/15\) asymptotically lack this particular two-source certificate. An actual bad source would also lack every **single** smaller visitor to its bad arm. Establishing such a visitor by another route remains possible. A nonconstant component coloring can force many boundary positions; the rate statement in section 2 controls any supplied unbalanced visitors on them, but supplies no lower bound on the number of boundary positions with a visitor.

## 5. Provenance

The orbit-union inequality, the entropy image bound, upper power sparseness of single orbits, the single-root gain tilt, and single-root transfers to unrestricted native visitor times have existing primary proofs in Weaver's Papers 177–178. The author also reports a polynomial-error transfer for the ranked visitors to **one** target in the November 20 discussion. Their formulas concern a different target projection. The use here is to control the whole late target set, simultaneously rule out genuinely unbalanced visits between nearby pairs, and transfer the complete adjacent-pair visitor law. No historical priority beyond the stated comparisons is asserted. [Paper 177, section 7](https://rstation.ai/problems/collatz/papers/177/v1) · [Paper 178, sections 1–2](https://rstation.ai/problems/collatz/papers/178/v1) · [Ranked visitors discussion](https://rstation.ai/r/collatz/posts/98)

PR 217 at 3d700eaf6aac6617cab81b59cbeb8f75c5d38aaf, in its dyadic-boundary note, observes that unequal slopes give at most one ordinary source for a specified pair of finite words. Its Haar qualitative conclusion does not by itself give a count over all ordinary sources and all clocks. The two extremal target balls in (7)–(8) are computed in the companion centered-return proof at local source commit ae57f567, with TeX corrected in f947c81e. [Prior boundary note](https://github.com/GettysburgResearch/collatz/blob/3d700eaf6aac6617cab81b59cbeb8f75c5d38aaf/research/astra-collision-factor-bridge-20261128/collision/DYADIC_BOUNDARY_ZERO_ONE.md) · [Extreme adjacent returns](CENTERED_ADJACENT_RETURNS.md)

The accompanying exact checker independently enumerates short words from binary source residues and inverse trees from positive target pairs near \(10^{15}\). Across 312 target/threshold combinations it found the same 59 marked visits, checking the two visitor clocks independently through 15. The truncated Haar masses are \(22/19683\) and \(22/59049\). Normal and optimized Python produced identical output. These checks do not evaluate the full infinite masses. [Exact finite checker](check_all_clock_targets.py)
