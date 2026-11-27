# An ordinary global trace with a fixed finite-word drift test

Use the odd Syracuse map \(U\), the original independent geometric exponents \(\Pr(E=e)=2^{-e}\), and the principal odd terminal \(y(w)\) defined in [the principal trace](PRINCIPAL_SAFE_TRACE.md). For any positive exponent word \(w=(e_0,\ldots,e_{n-1})\), put
\[
 A_j(w)=\sum_{i<j}e_i,\quad g(w)=3^n2^{-A_n(w)},\quad
 G(w)=\sum_{j<n}2^{A_j(w)}/3^{j+1},\quad B(w)=g(w)G(w).
\]
Thus \(B(w)\) is the real terminal from affine input zero. It need not be integral. The finite word gate is
\[
             \mathcal W_n=\{w:4A_j(w)\le7j\quad(1\le j\le n)\}.      \tag{1}
\]
Membership in (1) uses only the listed prefix clocks. The ternary residue is that of the original Syracuse affine channel. For \(z\ge0\) define the finite positive trace
\[
 T_n(z)=3^n\,\mathbb E_{\rm original}
       \left[\frac{\mathbf1_{\{w\in\mathcal W_n\}}}
        {y(w)-(1-z)B(w)}\right].                                    \tag{2}
\]
The denominator is positive. At \(z=1\) the numerator of the contribution at each principal terminal is its original mass **from the words passing (1)**. The full mass of other words in that same cell is excluded. At \(z=0\) the denominator subtracts the actual affine intercept and consequently depends on the individual word.

Let \(\mathcal P\) be the positive odd integers whose actual entire word satisfies (1). Let \(\mathcal E\) and \(\mathcal C\) denote respectively its escaping and eventually periodic members.

**Written theorem.** Both sides below converge, with no stationary-density, natural-basin-density or Dirichlet inputs:
\[
 \begin{split}
 T(0):=\lim_n T_n(0)&=\sum_{x\in\mathcal P}1/x,\\
 T(z):=\lim_n T_n(z)&=\sum_{x\in\mathcal E}
                  \frac{1}{x+zG_\infty(x)}\quad(z>0),\\
 T(0)-\lim_{z\downarrow0}T(z)&=\sum_{x\in\mathcal C}1/x .            \tag{3}
 \end{split}
\]
In particular \(T_n(1)\to0\) exactly when there are no escaping positive orbits. The centered statement \(T_n(0)\to0\) is equivalent to the **full positive Collatz conjecture**. Neither vanishing assertion is established here. Equation (2) gives one finite observable for both questions and isolates exactly where positive cycles enter its boundary value.

## Sparse principal seeds with unbounded individual exponents

The positive inverse argument for the [principal terminal](PRINCIPAL_SAFE_TRACE.md) works for every word. Each \(w\) has a least positive odd dyadic seed \(m(w)<2^{A_n+1}\), obtained by following its specified legal inverse at \(y(w)\). Its exact terminal is \(y(w)=g(w)(m(w)+G(w))\). Thus (2) is exactly
\[
                       T_n(z)=\sum_{w\in\mathcal W_n}
                                 \frac1{m(w)+zG(w)} .                \tag{4}
\]
Different words at fixed depth have different ordinary least seeds by determinism. Different words may have the same ternary cell, and (4) retains their separate original word probabilities in (2).

Let \(D=\{m(w): n\ge0,\ w\in\mathcal W_n\}\) and \(d=H_2(4/7)<1\), where \(H_2(p)=-p\log_2p-(1-p)\log_2(1-p)\). Then
\[
                 \#(D\cap[1,X])\ll X^d,\qquad
                 \sum_{\substack{m\in D\\m>X}}\frac1m\ll X^{d-1}.  \tag{5}
\]
Take \(2^j\le m<2^{j+1}\) with a witnessing word. Its total clock is at least \(j\). Let \(i\) be the first odd-clock index with \(A_i\ge j\). In the **first \(j\) shortcut positions** exactly \(i\) positions are odd: the \(i\)-th odd departure occurs at \(A_{i-1}<j\), and a possibly very long unfinished string of even steps through the cutoff contributes no further odd departure. Since \(j\le A_i\le7i/4\), we have \(i\ge4j/7\). The shortcut parity-prefix bijection gives one residue modulo \(2^j\) per binary word, hence at most one positive integer in this shell per word. The number of admissible binary strings is at most \(2^{jH_2(4/7)}\) by the elementary binomial exponential bound. Summing shells proves (5). The argument uses the gate at the completed exponent \(i\) even when the binary cutoff was strictly inside it.

At fixed \(m\in D\), its term in (4) is zero for all large \(n\) if the gate eventually fails. Otherwise \(m\) is eventually the least representative because its exact modulus \(2^{A_n+1}\) tends to infinity, and \(G_n\) is increasing. The envelope \(1/m\) is summable by (5). Dominated convergence proves the first line of (3) and identifies the \(z>0\) contributions with those having finite \(G_\infty\).

For an escaping positive orbit the odd states are distinct and go to infinity. The reciprocal sum over the odd states is finite. For instance discard its finite prefix through the last visit of the full shortcut orbit below \(2^{71}\), then apply the [ordinary simple-trajectory reciprocal bound](../coupling/FINITE_FLOOR.md) to arbitrary finite tails. This uses the counting theorem only, with no verification of Collatz through that range required. The product identity
\[
             m+G_n=m\prod_{i<n}(1+1/(3U^i m))
\]
now gives finite \(G_\infty\). On an eventually periodic path the same product increases without bound, as each positive cycle lap has a factor strictly above one. This proves the second line of (3). Dominated convergence as \(z\downarrow0\) then gives the last.

Both source classes can also be tested at a single rational sequence of finite parameters. Take \(z_n=1/n\), \(n\ge1\). For escaping seeds \(G_n/n\to0\), while after entering a cycle \(G_n/n\to\infty\) by geometric growth over complete laps. Therefore
\[
 T_n(1/n)\longrightarrow\sum_{x\in\mathcal E}1/x,\qquad
 T_n(0)-T_n(1/n)\longrightarrow\sum_{x\in\mathcal C}1/x .          \tag{6a}
\]
These two limits use the same domination (5).

Any positive start reaching 1 eventually repeats exponent 2 and fails (1). If some positive orbit does not reach 1, take the least positive odd starting point \(m\) in its undirected component. Every visit \(y_i=U^i(m)\) is at least \(m\), and \(m\ge3\). Hence
\[
       2^{A_n}=\frac m{y_n}\prod_{i<n}(3+1/y_i)
                    \le(10/3)^n<2^{7n/4}.                           \tag{6}
\]
The final comparison follows from \(10^4<2^7 3^4\). Thus this same ordinary \(m\) lies in \(\mathcal P\), in the escaping or eventual-cycle class of its component. At every finite depth its actual word is already accepted. Its least positive dyadic lift \(m(w)\) is at most \(m\), including depths before the original \(m\) becomes its own least lift. Therefore \(J_n:=T_n(0)\ge1/m\) at every depth. In particular the finite inequality \(J_n<1/L\) alone certifies that every positive integer at most \(L\) reaches 1: otherwise a bad component reached from that range has a least odd element \(m\le L\). This proves both stated equivalences and also shows that a positive jump in (3) is equivalent to a nontrivial positive cycle.

## An exponential upper budget for newly appearing ordinary seeds

At depth zero the empty word has \(m=y=1\), modulus two, and passes the gate. At any accepted word \(w\) write \(A=A_n(w)\), \(m=m(w)\), \(y=y(w)\). The possible earlier seeds of its next-letter children are lifts \(m+2^{A+1}j\); the corresponding old terminals are \(y+2\cdot3^n j\). The next valuation there is
\[
 1+v_2\left((3y+1)/2+3^{n+1}j\right)=1+v_2(j-r),\qquad
                 r=-\frac{3y+1}{2\cdot3^{n+1}}\in\mathbb Z_2 .
\]
For each possible exact exponent \(e=l+1\), let \(j_l\) be the smallest nonnegative integer with \(v_2(j_l-r)=l\). The child least seed is \(m+2^{A+1}j_l\). Dropping the starting bit of \(r\) gives an elementary estimate, uniform over every dyadic \(r\):
\[
                         \sum_{\{l:j_l>0\}}\frac1{j_l}\le2.          \tag{7}
\]
For \(r\) even, the first sibling is 1 and all later sibling minima are twice those of \(r/2\). For \(r\) odd the first sibling is zero, and all later minima are \(1+2j'_l\) from \((r-1)/2\). At most one \(j'_l\) is zero, since exact valuation cylinders are disjoint. The positive \(j'_l\)'s cost at most half their reciprocal sum; the possible zero contributes at most one. Induct on any finite dyadic depth and then increase it. Equality is attained at \(r=0\). PR193 independently gives the stronger exact statement that there is precisely one positive child lift in each half-open octave of \(j\), at every parent. Its octave bound immediately implies (7) and the per-parent reciprocal estimate below on the ordinary row. The explicit sibling recursion records a direct finite proof of this input. [PR193, canonical births](https://github.com/GettysburgResearch/collatz/blob/2796977d3f02ad57daeb7510f16da29527f9afde/research/astra-six-hour-20261127/global/CANONICAL_BIRTHS.md)

Write \(J_n=T_n(0)\). A parent can retain its own \(1/m\) on at most one child. All accepted children with a new least seed cost at most \(2^{-A}\), by (7), even if all positive exponents are tried. Summing over accepted parents,
\[
 J_{n+1}\le J_n+\Pr_{\rm original}(\mathcal W_n)
       \le J_n+\gamma^n,\qquad
         \gamma=(7/8)(7/6)^{3/4}<1.                                 \tag{8}
\]
Indeed for \(r=6/7\), \(\mathbb E r^E=r/(2-r)\), and the gate implies \(A_n\le7n/4\). Exponential Markov gives the last bound. In particular
\[
          J_n+\frac{\gamma^n}{1-\gamma}
\]
is a computable nonincreasing upper envelope with limit \(T(0)\). The exponential error bounds future **births** only. Existing atoms may die after arbitrary additional clocks. This gives a finite certificate at any prescribed bound \(L\ge1\): if \(J_n+\gamma^n/(1-\gamma)<1/L\), every positive integer at most \(L\) reaches one. Otherwise a failing positive input at most \(L\) would have a least odd representative of its bad component at most \(L\), contributing at least \(1/L\) to \(T(0)\) by (6). The direct test \(J_n<1/L\) established above is stronger at a single depth. The augmented quantity also decreases with depth and bounds the entire limiting mass. The same upper-envelope rule applies for fixed \(z\ge0\), since a retained seed has nondecreasing \(G\), and the children with new seeds still cost at most their reciprocals. A low-mean large deviation for iid exponents establishes (8), not the required disappearance of all surviving principal mass. Formula (8) does not provide a two-sided convergence rate or certify a positive survivor at a finite depth.

The newborn estimate provides a second proof of the summable domination in (3). A fixed positive odd seed can enter the set of least accepted representatives at most once. While its own word continues to pass the gate, its dyadic modulus grows and it remains least once it has appeared. Failure of a prefix gate excludes all longer prefixes of that source. Hence the sum of \(1/m\) over the union of all accepted least seeds is at most its initial mass one plus the sum of all positive birth costs, bounded by \(1+\sum_n\Pr(\mathcal W_n)<\infty\). This proof dispenses with the entropy estimate if only summability is needed; (5) adds an ordinary-height power bound.

## A finite rational reserve at the actual prefix debt

Let \(d=7n-4A_n\) at an accepted parent and put \(P_n=\Pr(\mathcal W_n)\). After the next letter \(e\), the possible remaining debt is \(d'=d+7-4e\). Write \(d+7=4k+r\) with \(0\le r<4\). The accepted next letters are \(1,\ldots,k\), and direct geometric summation gives
\[
  1+\sum_{e=1}^k2^{-e}(d+7-4e+8)=d+8-r2^{-k}.                     \tag{9}
\]
For example the full mean of \(d'+8\) is \(d+7\). Conditional on failure, \(e=k+E\) with \(E\) geometric, so the omitted mass of \(d'+8=r+8-4E\) is \(r2^{-k}\). The finite geometric identity is also kernel-checked.

Set \(V_n=\mathbb E[\mathbf1_{\mathcal W_n}(7n-4A_n+8)]\). Then \(V_n\ge P_n+V_{n+1}\), and \(0\le V_n\le(3n+8)\gamma^n\). Consequently \(J_n+V_n\) decreases to \(T(0)\), starting at \(1+8=9\). This is a rational upper certificate using only a finite debt recurrence. Replacing \(\gamma\) by \(63/64\) in the simpler envelope is also valid, by \(7^7 64^4<8^4 6^3 63^4\). Both reserves bound contributions from future new seeds. Neither bounds when a currently present seed will cease to pass the gate.

The [Lean module](HarmonicBirth.lean) checks the sibling bound, exact debt row, envelope comparison, cutoff implication and integer constant inequalities. The [finite replay](check_global_prefix.py) reconstructs every accepted word through depth 12, independently enumerates all ordinary candidate seeds through depth 7 and tests each parent's actual new reciprocal cost. The rows include rational outward enclosures and the exact dyadic debt reserve. [Retained results](GLOBAL_PREFIX_CONTROLS.json)

The starting principles are the shortcut parity bijection, the positive ordinary inverse, the geometric Syracuse law and the simple-path packing estimate. The earlier [permanent sieve](PERMANENT_SIEVE.md) imposes a permanent low-mean test on the actual forward side of a normalized nonlinear full-cell trace. PR193's [full-cell harmonic dust](https://github.com/GettysburgResearch/collatz/blob/795cfa38fbd6a2436285edfe82580680df4f9b0d/research/astra-six-hour-20261127/escape/EXPONENTIAL_DUST.md) leaves the incoming word law unrestricted. Here the test is on every prefix of the word used in (2). Its principal dyadic seed makes the positive atomic limit and the cycle boundary accessible directly. The centered vanishing question is an equivalent formulation, not a proof of convergence.
