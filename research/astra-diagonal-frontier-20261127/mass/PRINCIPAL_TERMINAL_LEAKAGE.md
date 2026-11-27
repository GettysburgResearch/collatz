# Ordinary one-step loss from tight prefixes and a physical source-height cutoff

**PROPOSED written theorems with a kernel-checked finite residue certificate.** The results concern the first moment of positive ordinary principal sources of the odd map. They give an unconditional lower bound for actual one-step loss at every sufficiently large dyadic depth and an asymptotic loss fraction for an explicit family, down to a polynomial cutoff in normalized source height. The loss estimate for every surviving source remains open.

## A finite prefix certificate works after every tight suffix

Use the odd map \(U(x)=(3x+1)/2^{v_2(3x+1)}\). For a gap word of length \(n\) write \(A_j=\sum_{i<j}e_i\). It passes if \(4A_j\le7j\) at every prefix, and is tight if also \(4A_n=7n\). Write \(m\) for its least positive odd dyadic source and \(y=U^n(m)\). At depth \(n\), \(J_n\) assigns weight \(1/m\) to each passing principal source. Let \(D_{n,n+1}\) be the part failing on its actual next step. All prefix probabilities below use independent \(\Pr(e)=2^{-e}\). In particular a word with total \(A\) has probability \(2^{-A}\).

The positive affine carry is determined by \(C_\emptyset=0\) and \(C_{we}=3C_w+2^{A(w)}\). At length \(n\),
\[
 2^{A}y=3^n m+C_w,\qquad 0<m<2^{A+1},\qquad 0<y<2\cdot3^n .
\]
Indeed, take the unique odd representative \(0<y<2\cdot 3^n\) in the class \(2^{-A}C_w\bmod 3^n\). The inverse steps \((2^e y-1)/3\) are successively integral by the carry congruence, positive by their positive odd input and positive exponent, and odd. Their composition gives \(m<2^{A+1}\) and the required odd itinerary. The forward word fixes \(m\) uniquely modulo \(2^{A+1}\).

Let \(w\) range over tight eight-letter prefixes. Their terminal residue set \(S\subset\mathbb Z/6561\) has 227 elements. Every cyclic interval of 3280 consecutive integers contains at least four points of \(cS\), for **every** unit \(c\bmod 6561\). This exact finite calculation is reproducible in [check_seed_spread.py](check_seed_spread.py). A smaller 14-word subset has maximum circular gap 2982 over all unit dilations. [SeedSpread.lean](SeedSpread.lean) verifies the selected words, carry congruences and gap test through dilation 3280 by kernel reduction. Negation preserves circular gaps and supplies the other half. The four-point version is checked by the integer replay. Its one-point consequence suffices for all asymptotic conclusions here.

Fix any tight suffix \(v\), of length \(s\), total \(B\), and put \(L=3^s, Q=6561\). Its least odd representative \(y_0\bmod L\) is understood to be 1 for \(L=1\). For each juxtaposition \(wv\) the **actual principal terminal** is \(y_0+2Li\) with \(0\le i<Q\). From \(2^B y\equiv L y_w+C_v\bmod LQ\),
\[
  2^{B+1}i\equiv y_w +(C_v-2^B y_0)/L\pmod Q .                 \tag{1}
\]
The index is therefore an invertible dilation and translation of the *same* finite set of certified prefix residues, independent of how long the common suffix is. The condition \(y\equiv1\pmod4\) selects one parity of \(i\); this finite arithmetic progression becomes an interval of length at least 3280 on multiplying by \(2^{-1}\bmod Q\). At least four of the 227 words meet it. The opposite terminal parity also occurs at least four times. All words are tight at \(n=8+s\). The first group has next gap at least two, which fails the gate. Each contributes at least \(2^{-7n/4-1}\) to \(D_{n,n+1}\), with the original principal source retained. Different words give distinct sources at the same depth.

Consequently for \(n=8+s\), \(4\mid s\), \(s\ge4\),
\[
 D_{n,2n}\ge D_{n,n+1}\ge
 4\cdot 2^{-7n/4-1}\, {1\over s}{7s/4-1\choose s-1}
 \gg n^{-3/2}\gamma^n,\qquad
 \gamma=(7/8)(7/6)^{3/4}<1 .                                  \tag{2}
\]
For the suffix count, rotate a composition of \(7s/4\) into \(s\) positive parts at a maximum of its cumulative excess \(4A_j-7j\). The resulting word passes, and at most \(s\) original rotations give the same result. Stirling's formula gives the stated order for the displayed lower bound. This includes every dyadic depth \(n\ge16\). At \(s=0\) the actual 14-word certificate supplies losses directly. The exponential rate in (2) matches the known gate probability on the logarithmic scale. It does not bound the rate of the entire loss from above.

## Programmable terminal and reciprocal mass away from the smallest seeds

Start with any **fixed word** \(p\) of length \(t\). Repeat the following pair of choices \(r\) times, then append any common suffix \(v\):
\[
 (1,2)\ \text{or}\ (2,1),\qquad
 (1,3)\ \text{or}\ (2,2).
\]
Each choice uses two odd steps. The first has division multiplier 8, the second 16, and their respective integer carries both range over \(\{5,7\}\). Each four-letter segment spends seven divisions. The original word probabilities of the \(4^r\) choices are identical. All four options pass every local prefix from debt at least one and return to that debt. For example, the prepended gap 1 supplies debt three; after all the options, three fixed gaps of 2 restore zero. One may then append *any* tight suffix. The distributional result also applies with arbitrary left and right words without a gate condition. Write \(n=t+4r+|v|\), \(A=A_n\), and define
\[
 H={r+t+2\over t+2+\log(2+r)},\qquad
 \eta={-\log(\cos(\pi/26))\over\log16}>0 .
\]
All asymptotic statements concern \(H\to\infty\). Average uniformly over these equally probable words, retaining each actual least ordinary source and terminal. For a source interval \(I\subseteq[0,1]\), a power of two \(q\ge1\) and **any** odd class \(a\bmod 2q\), the joint estimate is
\[
 \Pr\{m/2^{A+1}\in I,\ y\equiv a\pmod{2q}\}
   ={ |I|\over q} + O(H^{-\eta/2}+3^{-t-4r}+2^{-n}).               \tag{3}
\]
The error is absolute and uniform over all the supplied fixed words, all interval locations, all powers of two, and the chosen class. The leading term resolves classes only when it exceeds this error.

**Uniform Fourier estimate.** Set \(Q=9\), \(P=3^tQ^{2r}\), \(u_{2i}=8, u_{2i+1}=16\) and \(h_j=\prod_{i<j}u_i\), with \(h_0=1\). Before the final suffix the repeated two-letter recurrence gives
\[
 h_{2r} y_{pB}\equiv Q^{2r}y_p+
  \sum_{j=0}^{2r-1} Q^{2r-1-j}h_j(5+2b_j)\pmod P ,
\]
where \(y_p\) is the fixed terminal residue modulo \(3^t\). Formula (1), now with prefix modulus \(P\), transfers this residue to the index of the full principal terminal by an affine unit transformation. For every additional unit dilation and every frequency \(1\le l\le r^2\), the modulus of its characteristic function is
\[
 \prod_{j<2r}|\cos(\pi\theta_j)|,\qquad
 \theta_j={2lc h_j\over 3^t Q^{j+1}}\pmod 1,\quad 3\nmid c .    \tag{4}
\]
Translations affect only the argument of that characteristic function. Take \(b=\lceil\log_Q(l+1)\rceil\). At \(j\ge b\) the phase is nonzero and its distance to the nearest integer is at least \(3^{-t}Q^{-j-1}\). The signed representatives in \([-1/2,1/2)\) satisfy \(Q\theta_{j+1}-u_j\theta_j\in\mathbb Z\). At two consecutive distances less than \(1/26\), this integer has modulus at most \(25/26<1\). The next signed phase is exactly \((u_j/9)\theta_j\). The two integer cases of this inference are kernel-checked.

On a run of \(L+1\) small phases starting at \(j\ge b\), the growth factor across its \(L\) edges is at least \((8/9)(128/81)^{\lfloor L/2\rfloor}\). Therefore \((128/81)^{\lfloor L/2\rfloor}\le(9/8)3^t9^{j+1}\). As \(128/81>9/8\), \((128/81)^3>3\) and \((128/81)^5>9\), one obtains \(L\le 2+6t+10(j+1)\). Advance past each small run and its following large phase, including a final truncated run. The augmented index \(j+t+2\) increases by a factor at most 16 per advance, also when a small run is empty. If there are \(g\) large phases in \([b,2r)\), this gives \(2r+t+2\le16^{g+1}(b+t+2)\) whenever \(b\le2r\). Each large phase contributes at most \(\cos(\pi/26)\) to (4). Hence (4) is \(O(H^{-\eta})\) uniformly over these frequencies and dilations. Bounded small \(r\) can be absorbed in the absolute constant.

**From phases to ordinary sources.** The interval discrepancy of every such dilated index distribution on \(\mathbb R/\mathbb Z\) is \(O(H^{-\eta/2})\). For detail, smooth an interval indicator by averaging translates uniformly over \([-h,h]\), with \(h=H^{-\eta/2}\). Use intervals enlarged and shrunk at each end by \(h\) to sandwich the unsmoothed test, including wraparound. The smoothing multiplies its \(l\)-th Fourier coefficient by \(\sin(2\pi lh)/(2\pi lh)\), giving absolute coefficients \(O(\min(1/l,1/(hl^2)))\) for \(l>0\). Up to \(r^2\) their contribution to the error is \(O(H^{-\eta}(1+\log(1/h)))\). The remaining absolute sum is \(O(1/(hr^2))\); the two boundary expansions cost \(O(h)\). These errors give the asserted bound, with intervals shorter than \(2h\) covered by the upper estimate.

For all words with positive exponents the normalized source and terminal obey
\[
 0\le {y\over2\cdot3^n}-{m\over2^{A+1}}=
 {1\over2}\sum_{j<n}{2^{A_j-A}\over3^{j+1}}
 \le 2^{-n-1}(1-(2/3)^n).                                        \tag{5}
\]
Indeed \(A-A_j\ge n-j\). Writing \(y=y_0+2Li\) gives \(y/(2\cdot3^n)=i/P+y_0/(2LP)\). Imposing a terminal interval for this quantity and a class mod \(2q\) amounts to one progression of index stride \(q\), because \(L\) is odd. After multiplication by \(q^{-1}\bmod P\), it is a single circular interval with normalized length \(|I|/q+O(1/P)\); if empty its expected length is \(O(1/P)\). Expand and shrink \(I\) at its ends by the bound (5). The interval discrepancy proves (3).

**Actual first-moment consequence.** Let each word have equal mass \(1/4^r\) temporarily for normalization, and set \(X=m/2^{A+1}\), \(E=O(H^{-\eta/2})\). Equation (3) and partial summation, including a possible endpoint atom at the lower cutoff, give
\[
 \mathbb E[X^{-1}\mathbf1_{X\ge z}\mathbf1_{y\equiv a\,(2q)}]
     ={1\over q}\log(1/z)+O(E/z),\qquad 0<z<1 .                 \tag{6}
\]
For instance integrate the interval tests \([z,s]\) with kernel \(s^{-2}\) over \(z\le s\le1\) and add the endpoint interval test \([z,1]\). Multiplying (6) by \(4^r2^{-A-1}\) returns the sum with the **actual PR200 weight \(1/m\)**. Setting \(q=1\) gives the total weighted mass above the cutoff.

If every word passes at depth \(n\) and its final debt is \(d=7n-4A\), failure on the next odd step is exactly \(e\ge1+\lfloor(d+7)/4\rfloor\), one odd terminal class modulo \(2q\) where \(q=2^{\lfloor(d+7)/4\rfloor}\). Take \(z=H^{-\eta/8}\) and allow \(q\le H^{\eta/8}\). The share of this truncated reciprocal mass killed on the next step is
\[
                   q^{-1}(1+o(1))                                  \tag{7}
\]
uniformly, including in the right suffix. For tight words it is \(1/2+o(1)\). A growing debt is allowed in the indicated logarithmic range. This estimates genuine deterministic losses of the original principal sources after the truncation. It has no independent-post-gate resampling premise.

## Which source heights remain

Each selected four-letter segment carries an odd ordinary state \(x\) to \((81x+C)/128\) with \(C\le9\cdot7+8\cdot7=119\). A run of \(r\) such segments starts at a state \(x\ge(128/81)^{r-1}(3-119/47)+119/47\) for \(r\ge1\). Indeed the state at the beginning of the last segment is at least 3, since the orbit of 1 uses gaps \(2,2\) while its first two choices are \((1,2)\) or \((2,1)\). Iterating the affine upper bound over the preceding segments proves the claim. In particular with an empty left prefix this construction eventually excludes any specified fixed source. With a prescribed left prefix it retains the parity cylinder, and the ordinary integers realizing that cylinder can vary with the block choices.

For a fixed least bad component source \(m\ge3\), all odd states \(y_i\ge m\), giving \(2^{A_n}=(m/y_n)\prod_{i<n}(3+1/y_i)\le(10/3)^n\). Its own debt is at least \((7-4\log_2(10/3))n>0\) at every positive depth, and its normalized height \(m/2^{A_n+1}\le m/2^{n+1}\) vanishes exponentially. Neither the tight boundary in (2) nor the source-height and debt range in (7) includes that fixed atom at late depths. There is no lower bound comparing (2) to \(J_n/(1+\log n)\), and no claim that all surviving mass consists of the selected families. The uniform discrepancy in (3) is an absolute estimate and cannot be used as a relative estimate for microscopic intervals.

PR201's global prefix trace supplies the original reciprocal weights and principal representatives. PR200's joint-moment paper bounds all-word fractional moments and its rare-gate profile locates typical heights; its doubling-loss proposal asks for a lower bound relative to all ordinary first-moment mass. Here the additional arithmetic is the fixed prefix-carry certificate, uniform physical dyadic selection after arbitrary suffixes, and the weighted one-step result on the specified cutoff. These arguments do not rely on a stationary exit law or an independence of the source and its continuation.

- [PR201, global prefix trace at d21bac74](https://github.com/GettysburgResearch/collatz/blob/d21bac748e705a64b6b57a7996a8ad6282f0bcbf/research/six-hour-20261127/escape/GLOBAL_PREFIX_TRACE.md)
- [PR200, quantitative loss at eb910869](https://github.com/GettysburgResearch/collatz/blob/eb91086951b66923787f696801f0c3ca52a0077d/research/six-hour-20261127/NEXT_FIRST_MOMENT_TARGET.md)
- [PR200, joint fractional pressure](https://github.com/GettysburgResearch/collatz/blob/eb91086951b66923787f696801f0c3ca52a0077d/research/six-hour-20261127/pointwise/JOINT_GATE_FRACTIONAL_PRESSURE.md)
- [PR193, endpoint-rate test at aa686899](https://github.com/GettysburgResearch/collatz/blob/aa6868996f6f30b12d91c367f7c6edcfd93784b2/research/astra-six-hour-20261127/escape/ENDPOINT_RATE_TEST.md)
