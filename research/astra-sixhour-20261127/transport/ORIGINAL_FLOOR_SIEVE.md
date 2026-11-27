# Physical inverse certificates at the original canonical floor

Assume the bounded alternative and the notation of [the original current](ORIGINAL_CURRENT.md). Write \(r=v_3(s-1)\in\{2,3,4,5\}\), \(k=v_2(z-1)=2l+1\) and \(u=(z-1)/2^k\) odd. The pinned capture gives \(2\le l\le r\) and the stronger \(r\)-dependent lower floor
\[
          s\ \ge\ 1+\rho(z-1),\qquad \rho=(3/4)^r .
\]
Indeed if \(l>r\), the native \(l\) two-edges would produce a bad input strictly below \(s\). All \(q_n(z)=1+(3/4)^n(z-1)\), \(0\le n\le l\), are actual bad ordinary odd successors. Start an arbitrary inverse odd exponent word at any of them, allowing arbitrarily high detours. Its terminal \(x\), whenever ordinary and positive, is bad. Each of the following strict comparisons gives an original-floor contradiction:
\[
 \begin{array}{lll}
 x<1+\rho(z-1),&
 x\equiv0\pmod3,\ x<3+2\rho(z-1),&
 x\equiv17\pmod{48},\ x<z.                                         \tag{1}
 \end{array}
\]
They use the same absolute bad floor, first bad triple \(2s+1\), and least bad canonical source \(z\). [Pinned capture at the original source](https://github.com/GettysburgResearch/collatz/blob/03b26119164664d08eaa04a1ea1d159dd4eccd7a/research/astra-unconventional-20261126/cycle/CANONICAL_FLOOR.md) · [Ordinary least canonical floor](../descent/ORIGINAL_CANONICAL_FLOOR.md)

## Finite positive exclusions

Write \(d\) for reversed word length, \(E\) for total clock, and \(c_0=0\), \(c_{j+1}=2^{e_{j+1}}c_j+3^j\). The terminal is
\[
 x(z)=\frac{2^E3^nz+2^E(4^n-3^n)-4^n c_d}{4^n3^d}.              \tag{2}
\]
Congruence of the numerator modulo \(3^d\) ensures all reversed steps are integral since each prefix congruence follows by cancelling the remaining power of two modulo the smaller power of three. The source \(q_n(z)\) starts odd and positive, and (2) together with the prefix formulas checks positivity throughout. A final residue modulo three costs at most one additional ternary digit. The binary class of \(x\) modulo sixteen is obtained by reversing the word on \(q_n(z)\bmod16\). For all \(k,n\) in this note, \(u\bmod8\) determines that class. The right-side inequalities are affine and are checked at \(2^{71}\) and by comparing slopes.

The exact enumeration uses length at most eight and allows intermediate leading slope as large as 4 relative to \(z\). The entries count excluded ternary residues modulo \(3^9\) among the 6,561 possibilities with \(z\equiv2\bmod3\). The same counts hold for each of the four specified \(u\bmod8\) and each listed \(k\) separately.

| \(r\) | Possible \(k\) | Excluded | Remaining |
|---:|---|---:|---:|
| 2 | 5 | 6,080 | 481 |
| 3 | 5, 7 | 5,181 | 1,380 |
| 4 | 5, 7, 9 | 2,704 | 3,857 |
| 5 | 5, 7, 9, 11 | 1,986 | 4,575 |

Every newly contributing word/cylinder has also been checked by lifting the dyadic and ternary classes to an ordinary integer above the cutoff, following its actual odd steps and checking the asserted strict floor. No conjectural label value is inferred for that numerical replay. For example, the inverse ones from \(z\) alone give a true ancestor \(2^t(z+1)/3^t-1\) at \(t=v_3(z+1)\). The weakest floor already forces \(t\le3\). At \(r=2\), the first inverse from \(z\) is below \(2s+1\), and two inverse ones would fall below \(s\), so necessarily \(z\equiv2\bmod9\).

## An all-depth ternary density point missed by the same floor comparisons

Fix one of the possible \(r,k,u\bmod8\). Allow **all** finite inverse words from **any** \(q_n\), without a clock or intermediate-height ceiling. A word covers a ternary class if it is legal there and gives one of (1) for all sufficiently large ordinary \(z\) with those fixed dyadic and ternary digits. Equivalently check its strict affine inequality by comparing slopes, and use the constant terms when the slopes agree. The covered set is a countable union of ternary cylinders. Then the 3-adic point \(2\) is a **density-one point of its complement**:
\[
 \Pr\{\text{some covering word}\mid z\equiv2\bmod3^R\}
                        \longrightarrow0 \quad (R\longrightarrow\infty) .          \tag{3}
\]
This is normalized ternary Haar probability. For each fixed finite family there are arbitrarily large ordinary sources in the prescribed binary class missed by that family, by CRT. The Haar assertion for the countable union does not rate which ordinary source belongs to it.

### Exact control at the ternary point

Set \(z=2\) only in the *ternary* coordinate. The virtual rational targets are \(q_n(2)=1+(3/4)^n\); retain the independently prescribed original dyadic class for testing the final canonical residue. Let \(y\) be the virtual endpoint of a legal prefix, and \(m=(3/4)^n2^E/3^d\) its positive leading slope. Its full affine terminal is \(m(z-2)+y\). After \(E\ge2n+4\), \(y\) is an odd integer, and its residue modulo sixteen agrees with the source terminal in the independently supplied binary class. At every nonempty prefix,
\[
                       y < \big(1+(4/3)^n\big)m .                    \tag{4}
\]
This follows from the strictly positive affine sum subtracted in each inverse map. All legal prefixes are positive on the virtual control. For the finitely many prefixes of cost below \(2n+4\), and the first clearing step, this is checked explicitly in the integer/rational enumeration below. At a short prefix all admissible next exponents have a fixed parity, or there are none. Test them increasingly until the first clearing output exceeds five; all later choices are larger. Beyond a positive odd integer the integral odd inverse maps preserve positivity.

At a cleared endpoint the canonical, absolute and triple alternatives respectively require \(m\le1,\rho,2\rho\), respectively. By (4), \(n\le r\le5\), and \(\rho\le9/16\), a witnessing positive cleared integer has \(y<1+(4/3)^5<6\), \(y<1+\rho<2\), or \(y<2(1+\rho)<4\), respectively. The only positive odd possibilities for their union are \(1,3,5\). Their ordinary forward orbits stay in this set. From a clearing value larger than five they are unreachable by further inverse steps. From a clearing value in the set the only inverse possibilities leading to this set are the loop \(1\to1\), the edge \(1\to5\), and the edge \(5\to3\). Each loop multiplies \(m\) by \(4/3\) and cannot improve any comparison for a fixed final \(y\); remove all such loops. Testing these finitely many tails and every pre-clearing prefix rules out all three alternatives at the virtual point, including equality of leading slopes. For example the largest case \(k=11,r=5\), aggregated over all \(n\), has 140 short prefixes, 123 tested clearing edges and 48 small-vertex tail tests. The positive virtual control is a ternary datum and does not assert badness or canonical parity of the integer two.

### Estimated tails of all fixed-word covers

For each fixed \(n\) and \(\sigma>1\), sum \(m^{-\sigma}\) over the \(d\)-letter prefixes legal at \(q_n(2)\):
\[
                           S_{d,n}(\sigma)\longrightarrow0.           \tag{5}
\]
For large \(d\), every prefix has cleared by the \(j\)-th letter with \(j\le2n+4\). Its final virtual source \(x\) is an ordinary positive odd integer and \(m^{-\sigma}\le (1+(4/3)^n)^\sigma x^{-\sigma}\) by (4). The multiplicity per \(d,x\) is uniformly bounded. Indeed there are finitely many pre-clearing prefixes, whose positive rational terminals have the form \(2^{-h}a\) for an odd integer \(a\) and an integer \(h\). The clearing edge leads to \(x_0=(2^{e-h}a-1)/3\) with \(e-h\ge1\). The remaining \(d-j\) ordinary forward odd steps from \(x\) determine this \(x_0=S^{d-j}x\); hence the previously unknown clearing exponent \(e\) is unique once the short prefix and \(j\) are fixed.

If a specified \(x\) occurs on infinitely many lengths for the same short prefix and \(j\), its ordinary forward orbit hits the fixed \(a=S(x_0)\) at the corresponding times \(d-j+1\). Thus \(a\) is periodic. After the first such hit the later \(x_0\)'s belong to that fixed finite cycle and the clearing exponents belong to a finite set. The increasingly long ordinary path contains increasing numbers of whole laps, each with inverse multiplier \(2^H/3^P>1\) by multiplication of its positive edge equations. Consequently \(m\to\infty\) for these occurrences. Finitely many short prefixes and summability of \(\sum_x x^{-\sigma}\) prove (5) by dominated convergence.

Condition on \(z\equiv2\bmod3^R\). At \(q_n(z)\) the initial \(d=R+n\) ternary digits agree with those at \(q_n(2)\), since the affine slope is \(3^n/4^n\). All shorter legal words also have their final ternary class fixed, so the virtual check excludes all their proposed certificates. The legal prefixes of length \(d\) are exactly those counted in (5). After each such prefix the variable ternary endpoint is Haar on all of \(\mathbb Z_3\), by (2) with its cancellable \(3^{R+n}\) and the remaining unit slope. Different prefixes need not be independent.

Any possible certificate has total leading slope at most \(K=\max(1,2\rho)\). From a prefix of slope \(m\), summing over \(t\ge0\) additional exponents bounds the conditional chance of a certificate by
\[
 \left({K\over m}\right)^\sigma
 \sum_{t\ge0}\left({3^{\sigma-1}\over 2^\sigma-1}\right)^t,\qquad 1<\sigma<2.       \tag{6}
\]
A specified continuation of length \(t\) is legal on just one class modulo \(3^t\), and its additional slope is \(2^{\sum e}/3^t\). Bound the indicator of total slope at most \(K\) by the \(\sigma\)-th power of their ratio. The geometric series converges by strict convexity of \(\log\sum_{e\ge1}3^{-1}(3/2^e)^\sigma\), which vanishes at 1 and 2. The term \(t=0\) allows the first unresolved final ternary digit. Sum (6) over all legal prefixes, apply (5) and then sum over the finite list of \(n\). This proves (3).

[Exact source and virtual-control replay](check_original_floor.py) · [Enumeration receipt](../../../reports/astra-sixhour-20261127/transport/original-floor.json). Formula (3) is a written probability argument using the finite control check. The comparison permits each fixed finite word to have its own sufficiently large real cutoff. It does not exclude a word whose affine crossover height depends on the particular supplied \(z\), the complete good upper arm, additional lower forward steps, or a selector using the ordinary source in some other way.

## An ordinary depth obstruction, including source-dependent crossovers

For an actual positive integer \(z>2^{71}\) with the prescribed dyadic class and \(z\equiv2\bmod3\), put \(R=v_3(z-2)\). Then **no physical inverse word of length \(d\le R+n-8\) from \(q_n(z)\) can meet (1)**. This assertion concerns the actual finite \(z\), without taking the real height to infinity. For \(d<R+n\), the virtual integral-at-three calculation fixes legality and the final ternary class; the original binary class is the one retained in the finite control. Let \(\theta\) be the corresponding test's limiting slope \(1,\rho,2\rho\). A legal word with the required congruence and \(m<\theta\) was ruled out by the virtual calculation. For \(m=\theta\), a finite-source strict inequality would be the same strict virtual-constant inequality, also ruled out. For \(m>\theta\), their explicit rational denominators give
\[
 m-\theta\ge \{4^r3^{\max(d-n,0)}\}^{-1}.
\]
When \(d\ge n\), multiplication by \(z-2\ge3^R\) gives \((m-\theta)(z-2)\ge3^8/4^5>6\). When \(d<n\), use \((z-2)/4^r>6\) directly. All desired affine thresholds at \(z=2\) are at most \(3+2\rho\le33/8<6\), and the virtual endpoint is strictly positive. The affine identity \(x(z)=m(z-2)+y\) now rules out the actual inequality. For \(d=0\) the initial \(q_n\)'s have slopes at least \(\rho\), are ternary units, and for \(n>0\) are \(1\bmod3\). They furnish no earlier canonical or subfloor witness.

CRT gives unbounded ordinary \(z\)'s with \(z\equiv2\bmod3^R\), \(z=O_k(3^R)\), in each prescribed binary class, for example by choosing a lift with \(z/3^R\) in a fixed positive bounded interval away from zero. Thus a logarithmic necessary depth holds on real integer test families even with unlimited intermediate height. These sources have not been identified as bad. In the more restrictive case when the original \(z\) already lies on the distinguished bounded cycle, the unique native inverse letter is determined by its ternary residue in the alphabet \(\{1,2\}\). At the virtual seed 2 these letters are \(1,2,2,\ldots\), as the first step lands at 1. Consequently \(R\le6\) on that cycle, since a native run of six twos is excluded by the cycle-height band. The long-\(R\) family tests a limitation of the finite comparison, including the possibility of an off-cycle original source.

The independent [direct-ordinary checker](audit_original_floor.py) reruns the actual inverse graph from an ordinary CRT representative of every default cylinder, without symbolic congruence inversion. [Its 262,440-source receipt](../../../reports/astra-sixhour-20261127/transport/original-floor-direct.json) agrees in all forty counts.

### Arbitrarily large ordinary sources with a supplied good upper

The logarithmic-in-ternary-precision obstruction persists in the actual rank-three upper-certificate family
\[
 z_m=(2^{m+7}-271)/81,\qquad m=11+162j,\quad j\ge0 .
\]
Here \(k=5\); the positive upper \(3z_m\) reaches \(2^{m-2}\) in nine shortcuts with three odd inputs and then reaches 1 by halving. The verified family and more general positive lower routes at other indices appear in [the earlier Mersenne-family analysis](../../astra-unconventional-20261126/descent/SIGNED_MERSENNE.md).

In this family \(z_m-2=(2^{18}(2^{162})^j-433)/81\). Explicitly \(2^{18}\equiv433\bmod3^5\), and \(v_3(2^{162}-1)=5\) since \(2^{162}=4^{81}\). The valuation of \((2^{162})^t-1\) is \(5+v_3(t)\), by the binomial expansion or repeated cubing. Thus \(j\) modulo \(3^{R-1}\) parametrizes all lifts of \(z_m\equiv2\bmod3\) modulo \(3^R\), bijectively. For any \(R\ge1\) choose its unique class producing \(z_m\equiv2\bmod3^R\), and choose a positive representative \(3^{R-1}\le j<2\cdot3^{R-1}\). Then \(\log\log z_m=R\log3+O(1)\) and every actual lower certificate of the displayed three types needs at least \(R-O(1)\) inverse odd steps from each forced lower successor. No restriction on intermediate height or extra even clocks was used. The upper certificate is explicit at every selected integer. The least-bad-lower hypothesis has not been established there. The finite-level bijections also pull the Haar density-point statement (3) back to the 3-adic index variable of this same family.

### A fully ordinary all-depth control at 353

Take \(w=353\), a canonical ordinary source with \(k=5\). Its first two odd successors are \(265\) and \(199\). In the full positive odd predecessor basin of \(199\), the respective minima of the odd sources, the odd multiples of three, and the \(17\bmod48\) sources are
\[
                              199,\qquad 417,\qquad 353 .
\]
These are global minima, allowing any intermediate values and any depth. Each smaller candidate is checked to hit 1 before 199 and can never visit 199 afterwards; the maxima in the finite check are all below 417. The attaining paths take respectively 0, 9 and 4 shortcuts to 199. The underived control values are good: \(353\) reaches 1 in 80 shortcuts and \(3\cdot353=1059\) reaches 1 in 23. For the strongest \(r=2\) floor, \(1+(3/4)^2(w-1)=199\) and the triple cutoff is 399. An ancestor of any of the three forced vertices also visits 199. Therefore **no** ordinary inverse word from those three vertices, however long or high, gives any strict comparison (1) at this actual good source. The original-scale labels establishing the bounded bad case are separate hypotheses. [All-time finite Lean certificate](OrdinaryBasinControl.lean) · [Strict axiom receipt](../../../reports/astra-sixhour-20261127/transport/ordinary-basin-control-lean.txt)

The same ordinary \(w\) is a second ternary density point for (3), with the center changed to \(w\) and with \(k=5\), including all four binary subchoices \(u\bmod8\). For these subchoices \(z-w\) is divisible by 64. The possible initial binary discrepancy at \(q_n\) therefore still disappears modulo sixteen at every nonempty eligible endpoint: for \(n=0,1\) it already disappears at the root, and at \(n=2\) the initial reversed exponent is even, at least two, because \(q_2\equiv1\bmod3\). At the virtual ordinary \(w\) every legal branch is a genuine positive inverse path ending at some odd \(x\), with
\[
                  x<\{w-1+(4/3)^n\}m .
\]
A slope \(m\le\rho\) gives \(x<199\). A slope \(m\le2\rho\) gives \(x<399\), excluding multiples of three. A slope \(m\le1\) at a canonical endpoint forces \(x\le w\), since canonical integers are 48 apart and \(n\le2\). Equality \(x=w\) gives only the native word to \(q_n\), as these good targets exceed one and are nonperiodic. Its complete slope is one with no strict decrease. Thus every covering word fails at this ordinary ternary control. For the corresponding deep-prefix estimate (5), the endpoint sum now runs over a subset of actual \(x\ge1\), with multiplicity one at fixed \(d,n\); each \(x\) hits a fixed \(q_n\) at most once. Domination by a constant times \(x^{-\sigma}\) proves (5) directly. The conditional Haar tail (6) is unchanged. No all-depth closure is asserted after additional lower forward steps outside the forced initial block.

### A full logarithmic lower rank with an actual good upper

There are also arbitrarily large ordinary canonical-type \(z\) with \(k=5\) and \(3z\) actually reaching 5 for which every physical test (1) from the forced initial block requires \(\Omega(\log z)\) odd inverse steps. This application does not bound the odd rank of the upper certificate. It uses the prior individual-progression estimate of [Weaver, Paper 13, Proposition 1 and its fixed binary prefix reduction](https://rstation.ai/problems/collatz/papers/13), together with a fixed positive lower basin density. The explicit three-odd upper above has the weaker \(\Omega(\log\log z)\) bound.

Here is the initial-block deduction, retaining only the needed lower-density premise. Let \(f(m)\) indicate that the positive shortcut trajectory of \(m\) visits 5. This is invariant while all states exceed 5. Its full-integer lower natural density is positive under the named trace inputs: the weighted odd natural predecessor mean \(\beta_5>0\) follows from the positive ternary-unit trace at the nonperiodic root 5, and every weight is at most one. Restricting first to odd inputs costs at most a factor of two in the full-integer lower bound. No unweighted natural-mean limit needs to be assumed. [Weaver, Paper 12, §8, equations (23)–(24), recording Valbuena's input](https://rstation.ai/problems/collatz/papers/12)

Put \(Q=2^K M\), where \(K\) is fixed and \(M\) odd. Uniformly for representatives \(1\le c\le Q\), take \(b_j=c+Qj\), \(0\le j<J\), and compare \(f(b_j)\) with \(f(b_j+t)\), \(0\le t<Q\). The counted nonfusion event through \(h\) shortcut clocks is a set of binary residue classes with unrestricted Haar probability \(O(\sqrt{(1+\log Q)/(h+1)})\) by Paper 13, equation (1). The fixed binary class costs a factor at most \(2^K\). The input progression visits the \(2^{h-K}\) possible classes uniformly up to total error \(O(2^h/J)\) when \(h>K\). Except for \(O(1+2^h/Q)\) initial indices, both sources exceed \(5\cdot2^h\); neither can visit 5 before fusion through \(h\) clocks, so their two membership labels agree on fused pairs. Averaging in \(t\) produces the full contiguous block \([c,c+QJ)\). Thus
\[
 \left|J^{-1}\sum_j f(b_j)-(QJ)^{-1}\sum_{c\le m<c+QJ}f(m)\right|
 \ll 2^K\sqrt{(1+\log Q)/(h+1)}+2^h/J .
\]
This is the initial-block form of the cited finite progression averaging. Take \(J=\lceil Q^A\rceil\), \(h=\lfloor(\log_2 J)/2\rfloor\). The full block has a uniformly positive lower mean for large \(Q\), since \(c/(QJ)\to0\). Choosing \(A\) sufficiently large in terms of the fixed positive lower density and \(K\) leaves positive mean in **every** class, at ordinary height \(O(Q^{A+1})\). This power depends on the fixed target. No estimate for a moving rare basin is used.

Apply this to \(Q=64\cdot3^{R+1}\), taking the CRT class of \(b=3z\) with \(b\equiv6\bmod3^{R+1}\), \(b\equiv3\cdot33\bmod64\). We obtain \(z\equiv33\bmod64,\ z\equiv2\bmod3^R\), so \(z\) is canonical, \(k=5\), and \(3^R\le z\le\exp(O(R))\) for large \(R\). The actual word taking \(3z\) to 5 certifies its upper. The finite-source depth obstruction then gives the stated logarithmic lower bound. The selected lower label and its status as a potential *least* disagreement are undetermined by this construction.

The on-cycle restriction also distinguishes the control 353 from a bounded bad cycle: its unique inverse choices in the native alphabet \(\{1,2\}\) give \(353\mapsto235\mapsto313\mapsto417\), ending at a multiple of three. Thus the whole ternary class \(353\bmod81\) is unavailable for an on-cycle original \(z\). This extra constraint is not one of the three lower comparison tests in (1).
