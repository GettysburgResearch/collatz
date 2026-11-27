# A finite endpoint mark for cycles at the stopped-trace rate

The unmarked stopped-rate test detects escape. At a periodic target the slower multiplier of a possible additional cycle can cancel from an unmarked signed depth difference. An endpoint test on exactly the original finite words prevents that cancellation, and makes a common **subsequential** rate sufficient for full convergence. No such rate has been proved.

For \(j\ge0\) and a positive odd unit \(y\), sum over its actual length-\(j\) inverse words ending at a unit \(x\). Their multipliers and real intercepts are \(A_j=3^j2^{-S_j}\) and \(R_j=y-A_jx\). Give each word mass \(A_j\rho_1(x)\), so the total is exactly \(\rho_{j+1}(y)\). At \(j=0\) use \(A_0=1,R_0=0,x=y\). Set
\[
 L_{j,y}(t)=\sum_{\text{these words}}A_j\rho_1(x)
              {\bf1}_{\{(y-R_j)/y\le t\}} \qquad (0\le t\le1).
\]
Nonunit endpoints have zero rows. Each finite-depth series is absolutely convergent; \(\rho_1(x)\) is either one or two on units. The normalized defect of each word equals \(\prod_{u}3u/(3u+1)\) over its forward departed states. Let \(c_0>0\) be the uniform lower bound on that product over every positive distinct-state segment from the reciprocal-packing theorem. One can use any smaller positive constant as well. [Weaver 176, §5.1, uniform packing after (26)](https://rstation.ai/problems/collatz/papers/176/v1)

On any nonperiodic positive odd target all departed states on every legal prefix are distinct. Consequently \(L_{j,y}(t)=0\) when \(t\le c_0/2\), for every \(j\). On a cycle \(C\) of length \(\ell\), let \(\lambda=\prod_{u\in C}3u/(3u+1)\) and \(\gamma=\lambda^{1/\ell}\). At each specified \(y\in C\) there is a constant \(b_y>0\) such that at every sufficiently large \(j\),
\[
 \sup_{0\le t\le c_0/2}
      \big(L_{j+1,y}(t)-L_{j,y}(t)\big)_+\ \ge b_y\gamma^j .         \tag{1}
\]
These are genuine differences with nonnegative signs at the witnessing thresholds.

Indeed the smallest attained defect \(m_{j,y}\) at each finite depth strictly decreases with \(j\). To see attainment, take a sequence of words with intercept tending to the supremum. Passing successively to subsequences, each next gap is eventually constant or tends to infinity. A first diverging gap makes its entire remaining intercept contribution tend to zero, as the length is fixed and each later one-step multiplier is at most \(3/2\). The intercept limit is then that of the preceding finite prefix. Its endpoint is a unit: if the prefix is nonempty, this follows already from its admitting a further legal inverse step. It always has unit parents (choose a gap in one of the two allowed unit classes modulo six) and can be extended with a strictly positive real-intercept increment. This contradicts maximality. If all gaps stabilize there is a maximizing word. Extending that word by one more unit edge strictly increases the intercept. The maximizing word has positive mass because \(\rho_1(x)>0\). On a cycle, the full reverse laps give \(m_{j,y}\to0\).

If an inverse prefix leaves the cycle during its first reverse lap, every later vertex is off-cycle, and its forward segment through first entry is distinct. The product on this segment is at least \(c_0\); the partial cycle segment has product at least \(\lambda\). More generally leaving after \(d\) complete reverse laps and before completing the next lap gives normalized defect at least \(c_0\lambda^{d+1}\), regardless of subsequent prefix length. For all \(b\ge0\) and \(0<t<c_0\), this gives the exact identity
\[
              L_{j+b\ell,y}(\lambda^bt)=\lambda^bL_{j,y}(t).
\]
A prefix leaving before finishing \(b\) laps has defect at least \(c_0\lambda^b\); every remaining prefix begins with the \(b\) laps, returns to \(y\), and multiplies both the mass and the defect by \(\lambda^b\).

In each residue class modulo \(\ell\), choose one fixed \(j_0\) large enough that \(m_{j_0,y}<c_0/2\). Select \(m_{j_0+1,y}<t<m_{j_0,y}\). The positive difference of the two base rows at \(t\) is at least the mass of a maximizing word at depth \(j_0+1\). The exact identity at \(j_0+b\ell\) transfers this difference to the threshold \(\lambda^b t\) with multiplier \(\lambda^b\). Take the minimum of the finitely many resulting positive constants to obtain (1).

Thus the single nonnegative original-word statistic
\[
 \begin{split}
 Q_j=\sum_{y>1\ {\rm odd}}\frac{1}{y(3y+1)}
 \max\bigg\{&(\rho_{j+2}(y)-\rho_{j+1}(y))_+,\\
 &\sup_{0\le t\le c_0/2}(L_{j+1,y}(t)-L_{j,y}(t))_+\bigg\}
 \end{split}
\]
has the following implication on the retained arithmetic inputs. If there is an unbounded sequence of \(j\) with \(Q_j=O(j^A(2/3)^j)\) for any one fixed \(A\), every positive integer reaches 1. Indeed an escaping ray is excluded by the [one-sided stopped-row bound](STOPPED_RATE_TEST.md). Any other cycle has minimum at least three and therefore \(\gamma\ge9/10>2/3\); keeping its single specified \(y\) in (1) rules it out. Each \(Q_j\) is finite since at a fixed depth all row masses are bounded uniformly and the kernel in \(y\) is summable. The quoted ample gap \(9/10\) uses only that an additional positive odd cycle omits 1. The marked part is identically zero when there are no additional cycles. Conversely, one positive finite endpoint-tail mass at a vertex other than 1 already witnesses that a finite inverse path repeated an ordinary state and ended on another cycle. The rate implication does not establish a uniform upper estimate on these statistics.

The restriction to the narrow endpoint band has a separate reason. At the known nonperiodic target \(y=5\), the unrestricted CDF distance of the discrete real-prefix row to its continuous stationary limit cannot decay as \(O(j^A(2/3)^j)\). Take any typical path of the canonical inverse law at 5. Its unit prefix at depth \(j\) has \(A_j=\exp(-Dj+o(j))\), \(D=\log(4/3)\), and its contribution to this one atom is at least \(A_j\). A distribution function with an atom of mass \(a\) differs in supremum from any continuous distribution function by at least \(a/2\), by looking at the jump and its left limit. The ordinary-depth prefix measures do converge weakly to \(M_5\): their normalized path expression is \(\mathbb E_{h,5}[(\rho_1/h)(X_j)f(R_j)]\), and the bounded terminal ratio and fixed-prefix conditioning argument apply as in (4) of the real-fibre note. The endpoint-restricted statistic avoids this obstruction at every nonperiodic site. [Canonical path law](CANONICAL_INVERSE_PATHS.md) · [Non-atomic specified fibres and terminal-ratio argument](REAL_FIBRE_AND_FRONT.md)

## An explicit band and rational truncation

The same full-convergence implication holds for \(Q_j^*\), defined by replacing \(c_0/2\) in \(Q_j\) by \(1/(j+1)\). All nonperiodic bands are empty once \(1/(j+1)<c_0\). In (1) the finitely many families of cycle witnesses have thresholds \(\lambda^b t\) at \(j=j_0+b\ell\); these are at most \(1/(j+1)\) eventually. Thus the numerical statistic uses no value of the packing constant.

For integers \(Y,E\ge1\), keep \(1<y\le Y\) and only inverse words with every gap at most \(E\) in both the \(j\)- and \((j+1)\)-prefix rows. Use their truncated total masses also for the unmarked difference. The resulting rational number differs from \(Q_j^*\) by at most
\[
 \frac{2^{j+2}}{3Y}
  +\frac{2}{3}\big(j3^j+(j+1)3^{j+1}\big)2^{-E}.
\]
At each omitted target the entire positive maximum is at most \(\rho_{j+2}(y)\le2^{j+2}\), since the row sum of the one-step transfer is at most two. Sum \(1/[y(3y+1)]\le1/(3y^2)\) over columns beyond \(Y\). At retained targets and prefix length \(d\), the removed mass is at most \(2\cdot3^d d\,2^{-E}\), by \(\rho_1\le2\) and the union bound on \(d\) geometric gaps. This bounds the error in the total and in every CDF value. The positive part, supremum and maximum change by at most the sum of the two row errors. The retained kernel sums to at most \(\frac13\sum_{n\ge2}n^{-2}\le1/3\). The finite CDF tests require only zero and the rational word-defect breakpoints in the chosen band. These two truncations can therefore give any prescribed absolute precision at each depth.
