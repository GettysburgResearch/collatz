# Late harmonic losses come from the ordinary inverse tree of one

**PROPOSED, written.** The formulas below identify the outgoing reciprocal mass in the unchanged \(7/4\) gate up to an exponentially small absolute error. The main term is a positive measure supported on dates congruent to one modulo four. Each coefficient counts actual first-hit paths into the specified integer 1. The estimate on these coefficients required for universal convergence is open.

## The ordinary objects

Use \(U(x)=(3x+1)/2^{v_2(3x+1)}\) on positive odd integers, \(x_j=U^jm\), \(A_j=\sum_{i<j}v_2(3x_i+1)\), \(a=7/4\), \(\lambda=\log_2 3\), \(d=H_2(4/7)<1\), and \(\eta=a-\lambda>0\). A word of \(n\) gaps is accepted if \(4A_j\le7j\) at every \(j\le n\). Its principal source is the least positive odd integer realizing it. Let \(\mathcal M_n\) consist of these sources, \(J_n=\sum_{m\in\mathcal M_n}1/m\), \(J_0=1\), and \(D_{n,N}\) be the mass of members of \(\mathcal M_n\) whose *own* first failure falls in \((n,N]\).

At height \(q\ge0\) define \(a_q\) by reversing paths from 1. Use positive odd preimages \(x=(2^e y-1)/3\) whenever integral. Forbid the edge from 1 back to 1. On a reversed path of length \(h\), let \(s_k\) be the sum of its first \(k\) gaps and \(b_k=7k-4s_k\). Include its leaf \(m\) exactly when
\[
       2h-s_h=q,\qquad b_k\le b_h\quad(0\le k\le h).
\]
Give the leaf weight \(1/m\). Include the empty path, which supplies \(a_0=1\). Different included paths have different leaves: determinism gives their first-hit histories to 1. The record condition is weak, including ties.

Set \(R=2^{\eta(1-d)}>1\). For every \(1<r<R\) there is a constant \(C_r\) such that, uniformly in \(N\ge n\ge0\),
\[
\begin{split}
  \left|D_{n,N}-\sum_{n<4q+1\le N}a_q\right|&\le C_r r^{-n},\\
  \left|J_n-J_\infty-\sum_{4q+1>n}a_q\right|&\le C_r r^{-n}.
\end{split}                                                     \tag{1}
\]
Here \(J_\infty\) is the sum of reciprocals of permanently accepted ordinary sources. In particular, the total harmonic death mass at all sufficiently late dates outside this residue class decays exponentially, whether or not an exceptional positive component exists.

Each \(a_q\) is a finite rational number. Its complete first-hit paths satisfy
\[
 q\le h\le4q,\qquad m\le(128/81)^q.                              \tag{2}
\]
Thus a given coefficient can be computed either by a bounded inverse search or by scanning ordinary positive odd integers up to this exact height. The rate \(R\) is an absolute error guarantee and does not assert decay of the main term.

## Actual first exit and its reverse record

Fix \(m\) and its first odd hit of 1 at \(h\), if it has one. On passing the gate through \(h\), its full clock after the hit is \(A_{h+k}=A_h+2k\). Its first exit occurs exactly at
\[
                   \tau=8h-4A_h+1=4q+1,\qquad q=2h-A_h .
\]
Since \(h\le A_h\le7h/4\), this gives the two bounds on \(h\) in (2). The forward debt at date \(j\le h\) equals \(b_h-b_{h-j}\) in the reversed first-hit path. Thus passing through \(h\) is exactly the record condition. For \(h>0\), the positive affine offset gives \(m<2^{A_h}/3^h=(4/3)^h2^{-q}\le(128/81)^q\). The equality case \(m=1,h=q=0\) is included in (2).

Such a source is already principal by its hit. Its class has modulus \(2^{A_h+1}\), and the preceding inequality gives \(m<2^{A_h+1}\). It stays principal at all subsequent dates before first failure. In particular *every* leaf counted above contributes \(1/m\) to ordinary one-step death at \(\tau\), including leaves that were initially nonprincipal.

Let \(\Delta_t\) denote the mass of members of \(\mathcal M_{t-1}\) that fail at \(t\). Any contribution to \(\Delta_t\) omitted by the preceding inverse-tree rule must have \(x_i\ne1\) for every \(0\le i<t\). It can hit 1 *at* \(t\) without passing that date. The departing states \(x_0,\ldots,x_{t-1}\) are distinct. Indeed a repetition at \(i<j<t\) gives a positive cycle entirely above 1 with gap sum at most \((j-i)\log_2(10/3)<a(j-i)\), by multiplying its genuine updates. Forward debt increases strictly across a lap, so the safe earlier date \(t-(j-i)\ge i\) makes failure at \(t\) impossible.

On this simple prefix the positive correction satisfies
\[
 \prod_{i<t}\left(1+\frac1{3x_i}\right)
    \le \exp\!\left(\frac13\sum_{k=1}^{t}\frac1{2k+1}\right)
    \le (2t+1)^{1/6}.
\]
The *same* path fails at \(t\), hence \(2^{A_t}>2^{at}\). Multiplying its affine updates gives
\[
              m=\frac{2^{A_t}x_t}{3^t\prod_{i<t}(1+1/(3x_i))}
                   \gg 2^{\eta t}(t+1)^{-1/6}.                       \tag{3}
\]
This uses the actual positive sign and the absorbing odd state 1. No density theorem or prior finite verification enters.

For completeness let \(\mathcal D=\bigcup_n\mathcal M_n\). If \(m\in\mathcal D\cap[2^k,2^{k+1})\), its witnessing word has total \(A\ge k\). Stop at its first completed gap reaching \(k\). At least \(4k/7\) of the first \(k\) shortcut departures are odd, by acceptance at that completed gap. Finite shortcut parities prescribe one residue modulo \(2^k\), hence at most one source in the shell. The binomial bound gives \(O(2^{dk})\) such sources and \(\sum_{m\in\mathcal D,\ m\ge Y}1/m\ll Y^{d-1}\). This is the principal-source census of PR 201. Applied to (3), it gives
\[
 0\le\Delta_t-\mathbf1_{\{t=1\pmod4\}}a_{(t-1)/4}
       \ll (t+1)^{(1-d)/6} R^{-t}.                                  \tag{4}
\]
A term with noninteger subscript is defined as zero. The tail constant is explicit: the shell estimate above gives at most \(2^{1-d}Y^{d-1}/(1-2^{d-1})\). The correction-product bound follows from \(\sum_{k=1}^t(2k+1)^{-1}\le\int_0^t(2u+1)^{-1}du\). Thus (4) holds with \(2^{1-d}(2t+1)^{(1-d)/6}R^{-t}/(1-2^{d-1})\) on the right. In particular the off-residue estimate controls a positive mass before any cancellation.

## Births, analytic remainder, and the unresolved normalization

Let \(B_t\) be the reciprocal mass of accepted children at depth \(t\) whose principal source changes from the parent. An old integer continues on exactly one child if it passes. A new least representative could not previously have been principal and then lost, since the increasing moduli preserve minimality on extensions and a failed prefix excludes every continuation. Thus \(J_t-J_{t-1}=B_t-\Delta_t\). The original sibling and geometric gate estimates give \(B_t\le\gamma^{t-1}\) for \(\gamma=2^{-a(1-d)}<1/R\). In (4), summing over \(t>n\) costs \(O_r(r^{-n})\). Passing from all deaths in \((n,N]\) to deaths of members already present at \(n\) costs at most \(\sum_{t>n}B_t\). This proves the first line of (1). Each source contributes to the death measure at most once and all births are summable. Limit passage in the ledger, or dominated convergence on \(\mathcal D\), proves the second line.

Equivalently, write \(F(z)=\sum_{n\ge0}J_nz^n\) and \(L(z)=\sum_{q\ge0}a_qz^q\). There is a power series \(E\) analytic throughout \(|z|<R\), given explicitly by the birth at \(n+1\) minus its omitted pre-hit death mass at that date, such that
\[
             (1-z)F(z)=1-zL(z^4)+zE(z)\qquad (|z|<1).
\]
In particular \(J_\infty=1+E(1)-L(1)\). The fourfold calendar and exponential remainder are unconditional. Showing \(L(1)=1+E(1)\), or proving a nonsummable relative loss on the original dyadic blocks, is still open. A change in the geometric word law or an argument retaining only the exponential remainder does not evaluate the first-hit record mass \(L(1)\).

## Source pins and evidence

* The definition of \(J_n\), the ordinary atom test, sparse census, sibling birth bound, and a fair-word debt reserve appear in [PR 201](https://github.com/GettysburgResearch/collatz/blob/807d67ab049f1646398d8ca8c20948cdc1d87742/research/six-hour-20261127/escape/GLOBAL_PREFIX_TRACE.md). [PR 200](https://github.com/GettysburgResearch/collatz/blob/eb91086951b66923787f696801f0c3ca52a0077d/research/six-hour-20261127/NEXT_FIRST_MOMENT_TARGET.md) proposed the same-source dyadic hazard and observed \(A_j(27)=2j-12\) after its hit. Its [safe-suffix argument](https://github.com/GettysburgResearch/collatz/blob/eb91086951b66923787f696801f0c3ca52a0077d/research/six-hour-20261127/pointwise/CRITICAL_SAFE_ENTRY.md) establishes coercivity for bad points. Formula (4) identifies the positive outgoing mass through the root 1 for every date, including all terminating pre-hit exceptions.
* [SignedDeathClock.lean](SignedDeathClock.lean) checks the literal ordinary first-exit date, reverse-record equivalence, and grade range. The first-hit interpretation of the inverse enumeration, the harmonic estimates and the analytic conclusion are written arguments. [check_death_clock.py](check_death_clock.py) compares forward / reverse enumeration through \(q=12\), including \(27\) at \(\tau=49\), and checks the ordinary principal birth-and-death ledger independently through eight odd steps. The first nonempty positive record grades are \(q=10\) at \(47,63\), \(q=11\) at \(31,55\), and \(q=12\) at \(27\).
