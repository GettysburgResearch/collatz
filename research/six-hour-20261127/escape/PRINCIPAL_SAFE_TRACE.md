# The principal harmonic trace on the no-adjacent-twos language

Let \(U(x)=(3x+1)/2^{v_2(3x+1)}\) on positive odd integers, let \(L_n\) be the chronological words of length \(n\) on \(1,2\) with no adjacent twos, and let \(p_n\) be the **original** ternary residue law with independent exponent probabilities \(2^{-e}\). Put \(\rho_n=3^np_n\). For \(w\in L_n\), let \(y(w)\) be the least positive odd representative of its terminal residue modulo \(3^n\). Its range is \(1\le y(w)\le2\cdot3^n-1\). Write
\[
 A(w)=\sum w_j,\qquad g(w)=3^n2^{-A(w)},\qquad
 R(w)=2^{A(w)}p_n(y(w)).
\]
The probability in \(R\) sums over **all** original exponent words in this same ternary cell. Write \(d=\log_2\lambda=0.551463\ldots\), where \(\lambda>1\) solves \(\lambda^{-1}+\lambda^{-3}=1\).

**Unconditional written theorem.** Let \(S\) be the set of ordinary positive odd seeds whose entire forward word has letters in \(1,2\) with no adjacent twos. For any real \(s>d\),
\[
 \lim_{n\to\infty}\ \sum_{w\in L_n}
      \left(\frac{\rho_n(y(w))}{y(w)}\right)^s
  =\sum_{x\in S}\left(\frac{R_\infty(x)}{x+G_\infty(x)}\right)^s. \tag{1}
\]
The two limits on the right are taken along the actual word of the indicated integer. Both sums count each object once, and the right side converges. In particular the ordinary linear harmonic mass on these cells, **without division by depth**, tends to zero exactly when this language has no positive ordinary survivor. Every such survivor would escape, since each pair of consecutive exponents has total at most three and hence slope at least \(9/8\).

At one fixed infinite word \(w\), its principal depth-\(n\) trace \(\rho_n(y(w_{<n}))/y(w_{<n})\) always has a limit. This limit is positive exactly when one ordinary positive odd integer realizes the entire word. The representative here is essential. Positive rational values of an affine script on an independently supplied ternary source have different heights.

## Principal terminal and principal seed

The forward formula at an ordinary seed \(m\) is
\[
 U_w(m)=g(w)(m+G(w)),\qquad
 G(w)=\sum_{0\le j<n}\frac{2^{A(w_{<j})}}{3^{j+1}}.               \tag{2}
\]
The inverse branches of its prescribed word are ternarily legal at \(y(w)\), because legality to depth \(n\) depends only on the terminal residue modulo \(3^n\). Every such inverse of a positive odd terminal \(z\) is again an ordinary positive odd integer. Indeed \(2^e z-1\) is positive and odd, and divisibility by three makes its quotient positive and odd. This also gives the exact valuation at that predecessor. Thus \(y(w)\) has a positive odd inverse \(m(w)\) using \(w\). Moving to the next positive odd terminal in its ternary class adds \(2\cdot3^n\) to \(y(w)\), hence adds \(2^{A(w)+1}\) to its inverse. All positive exact seeds map to one of these terminals. The forward map of a specified word is strictly increasing. Consequently \(m(w)\) is the least positive odd seed of that exact dyadic cylinder. In particular \(m(w)<2^{A(w)+1}\). Substitution gives
\[
               \frac{\rho_n(y(w))}{y(w)}
                    =\frac{R(w)}{m(w)+G(w)}.                       \tag{3}
\]

Different \(w\in L_n\) have distinct ternary cells. The last letter is determined by \(z\bmod3\) because at a unit exactly one of \(e=1,2\) makes \(2^ez=1\bmod3\). After that letter the inverse residue at depth \(n-1\) is determined, so induction recovers all the letters. This direct decoding also follows from simultaneous division minimality and uniqueness of the zero-excess competitor. Distinct words at one depth have distinct \(m(w)\) by deterministic forward iteration.

On an infinite script in the language the prefix minima \(m(w_{<n})\) are nondecreasing. They stabilize exactly at a positive ordinary seed, and otherwise tend to infinity. Formula (2) gives \(0\le G(w)\le7\) uniformly. The bounds \(A_{2j}\le3j\) and \(A_{2j+1}\le3j+2\) bound consecutive pairs of terms by \((1/3+4/9)(8/9)^j\). Thus \(G\) increases to a finite limit. The [posterior shell theorem](GEODESIC_POSTERIOR.md) gives \(1\le R(w)\le C\) uniformly and monotone convergence along every script. Equation (3) proves the fixed-script assertion.

There is also a principal-height criterion with no posterior input. If the least seed changes on the next symbol \(e\), nesting of exact cylinders gives \(m_{n+1}\ge m_n+2^{A_n+1}\). By (2),
\[
       \frac{y(w_{<n+1})}{3^{n+1}}
       =\frac{m_{n+1}+G_{n+1}}{2^{A_n+e}}
       >2^{1-e}\ge\frac12.                                        \tag{5}
\]
Thus every script with no ordinary positive seed exceeds half the ternary modulus infinitely often. If its principal representatives are eventually at or below half the modulus, the seed stabilizes and the script has its own ordinary positive trajectory. Every such positive trajectory in turn has \(y(w_{<n})/3^n\to0\). This is a sufficient entire-tail test. Infinitely many small principal representatives alone need not bound their inverse seeds.

## A stopped dyadic count at the height of the least seed

Let \(D\) be the union of \(m(w)\) over every finite word in the language. Then
\[
                       \#(D\cap[1,X])\ll X^d.                      \tag{4}
\]
Every eligible finite word parses uniquely into the tokens \(1\) and \(21\), of dyadic costs 1 and 3, followed possibly by one unpaired terminal \(2\) of cost 2. The number of token strings of cost \(j\) is at most \(\lambda^j\) by induction from \(C_j=C_{j-1}+C_{j-3}\), \(C_0=1\), and \(C_j=0\) for negative \(j\). The possible trailing symbol multiplies this bound by an absolute factor.

Fix the ordinary height shell \(2^j\le m<2^{j+1}\), \(j\ge2\). Some finite eligible exact word for this \(m\) has total clock at least \(j\), since \(m<2^{A+1}\). Stop at the first complete exponent for which the clock reaches \(j\). Its total is \(j\) or \(j+1\). There are \(O(\lambda^j)\) possible stopped words. Each imposes one odd class modulo at least \(2^{j+1}\), containing at most one integer in the shell. Summing geometric shell counts proves (4). In particular \(\sum_{m\in D,\ m>X}m^{-s}\ll_s X^{d-s}\) for \(s>d\).

At depth \(n\), regard the summand in (1) as a function of \(m\in D\), set to zero if \(m\) is absent from that depth. Equation (3) bounds it by \((C/m)^s\). For fixed \(m\), finite failure of its actual word eventually makes its summand zero. If \(m\in S\), it is the least positive representative once the cylinder modulus exceeds \(m\), and the term tends to the atom displayed in (1). Dominated convergence proves the claim. The same domination gives total variation convergence of the atomic measures on the **ordinary seed coordinate** carrying these weights.

The only possible residual mass in this family comes from individual fixed ordinary seeds. Its vanishing for the original Collatz map is open. PR193's global first-hit and moving-target profiles already separate positive ordinary atomic traces from diffuse mass under their stated inputs. Its newer all-cell decomposition concerns a normalized sum across the entire residue space. The bounded full posterior on this language gives (1) without the global passage or stationary-floor assumptions and with a subunit moment threshold. [PR193, fixed-source posterior](https://github.com/GettysburgResearch/collatz/blob/25f5462e2c43feea65760884f7ea8f53576fbc18/research/astra-unconventional-20261126/global/POSTERIOR.md) · [PR193, original full-space trace](https://github.com/GettysburgResearch/collatz/blob/795cfa38fbd6a2436285edfe82580680df4f9b0d/research/astra-six-hour-20261127/escape/EXPONENTIAL_DUST.md)
