# Distinct genuine paths matching finitely many closure moments

**Written theorem.** Fix a length \(h\ge1\), a degree \(d\ge1\), a minimum state \(m\ge1\), and a positive modulus \(M\). There is a finite nonempty collection of genuine positive Syracuse paths
\[
  x_{i,0},\ldots,x_{i,h},\qquad
  2^{e_{i,t}}x_{i,t+1}=3x_{i,t}+1,\qquad e_{i,t}\in\{1,2\},
\]
such that all \(x_{i,t}\ge m\) are odd units modulo three, and **all vertices indexed by distinct pairs \((i,t)\) are distinct**. At each of the \(h+1\) time slices the multisets of residues modulo \(M\) are identical. Independently their exact integer power sums of degrees \(0,\ldots,d\) are identical across all slices.

The native word frequencies can also be prescribed. If \(\gcd(M,6)=1\), any strictly positive rational probability vector on the \(2^h\) words is allowed. For arbitrary \(M\), any strictly positive rational vector whose length-\((h-1)\) prefix and suffix marginals agree is allowed. This includes all nondegenerate rational Bernoulli laws. The degree, path length and modulus are fixed before building the collection. Endpoint and initial sets are disjoint, so these tests falsely accept the collection as returning even when they include positivity, injectivity, native paths and arbitrarily many prescribed residue classes. This is an obstruction to any fixed finite collection of *these* necessary conditions. It makes no assertion about sufficient moment data when the number of tested moments grows with the size of the candidate. In particular it does not give an ordinary cycle.

**Predecessor and scope.** Freelan Lab already obtained positive integer *weights* on disjoint genuine single shortcut steps matching polynomial moments in each residue class. Their Theorems A and B give quantitative degree and modulus growth with bounded height. They also use Prouhet averaging, finite binary/ternary windows and auxiliary-prime matchings. The results here fix the tests, pass to full native paths of an arbitrary prescribed finite length, match every time layer, prescribe the stationary native word law, and remove all multiplicities for the polynomial tests. The rational-function extension below retains weights. No quantitative upper height bound for these constructions is claimed. [Freelan Lab, rStation 199/v2, Theorems A and B, Sections 4–5](https://rstation.ai/problems/collatz/papers/199/v2)

### Genuine cylinders with a shift parameter

Write \(q_t=3^t/2^{S_t}\) for the linear multiplier on the first \(t\) letters of a word, where \(S_t\) is the partial exponent sum. For a path from \(y\) write \(x_t=q_t y+c_t\), with \(q_0=1,c_0=0\). Every chosen string of positive native exponents occurs on an arithmetic progression of positive odd starts: the affine composition through its \(H\) letters fixes a unique residue modulo \(2^{S_H+1}\) giving an odd terminal state. Indeed the terminal identity modulo \(2^{S_H+1}\) has the invertible coefficient \(3^H\) on the start, and reduction to each partial sum gives the required odd intermediate values and exact valuations. One may refine this progression modulo any modulus prime to two, as compatible residues require. Start sufficiently high that all the finitely many ensuing vertices exceed \(m\).

For \(M=M_0\) prime to six, take all central words, initial classes modulo \(M_0\), and actual starts \(y\) in their cylinders with \(3\nmid y\); every subsequent state is then also prime to three. For general \(M=2^a3^bM_0\), use \(B=\max(1,b)\) extra prescribed letters before the central word and \(a\) after it. The central vertices now all have a genuine predecessor and are prime to three. A central state's residue modulo \(3^b\) is fixed by its preceding \(b\) letters: the affine identity over that segment eliminates its initial state modulo \(3^b\). Its residue modulo \(2^a\) is fixed by its following \(a\) letters, since their total division exponent is at least \(a\). These observations include the empty modulus-one parts. Independently the central initial residue modulo \(M_0\) can be prescribed: all affine branch maps over \(M_0\) are bijections. All such extended-word types and initial classes give unbounded progressions of realizable central starts \(y\).

Fix a common positive multiple \(Q\) of \(6M\,2^{2h+2}\). For each allowed central path, adjoin an arbitrary positive multiple \(v\) of \(Q\). For any nonnegative integer parameter \(T\) the translated start \(y+vT\) follows those same real \(h\) native transitions, with central vertices
\[
                         x_t+v_tT,\qquad v_t=q_tv .
\]
Indeed all \(v_t\) are integer multiples of \(2\cdot3M\). The old equations still hold exactly, and each new vertex retains its odd parity and its original residue modulo \(3M\). The padding above was used to specify actual central residues; no claim about the continued padding of every translated path is needed.

### Exact polynomial balance by finite-dimensional separation

Associate a rational vector to each parameterized path. Include the coefficients of \(T^j\) in
\[
                 (x_{t+1}+v_{t+1}T)^k-(x_t+v_tT)^k
                \quad (0\le t<h,\ 1\le k\le d,\ 0\le j\le k).
\]
Append each consecutive layer difference of the indicators of residue \(r\bmod M\), and the centered word indicators \(\mathbf1_{w=u}-\pi_u\) for the prescribed rational law \(\pi\). A rational positive combination with vector sum zero will give all the required equalities, and will preserve the polynomial moment identities under every common \(T\).

To see such a combination exists, consider a real linear functional nonnegative on every attainable vector. Suppose it has a nonzero coefficient on a degree-\(k\) moment and choose the largest such \(k\). As the actual start \(y\) tends to infinity within any fixed word/residue cylinder, choose the available multiples \(v\) so that \(v/y\to\lambda>0\). Divide the functional by \(y^k\). Its limit has the form
\[
                    \sum_{t=0}^{h-1} C_t(\lambda)(q_{t+1}^k-q_t^k),
                    \tag{1}
\]
where the polynomials \(C_t\) have the binomial coefficients absorbed into their coefficients. Some \(C_t\) is nonzero, since each tested coefficient contributes its distinct power \(\lambda^j\) at its own time. Choose a positive \(\lambda\) for which not all \(C_t(\lambda)\) vanish. Then (1) must be nonnegative for every native word.

Choose the digit at each time according to the sign of \(C_t(\lambda)\). Use \(e=2\) when this coefficient is positive and \(e=1\) when it is negative, and use either digit if it vanishes. Since \(q_{t+1}^k-q_t^k=q_t^k((3/2^e)^k-1)\), every term in (1) is now nonpositive and at least one is strictly negative. This is an allowed word, contradicting nonnegativity. Thus every nonnegative functional has zero polynomial part.

For \(M=M_0\) choose the prescribed positive word law and an independent uniform initial class in \(\mathbb Z/M_0\); at each central time the class is uniform even conditional on the word, since the branch maps are permutations. Hence every remaining bounded test has mean zero, while every available type has positive probability. In the general case extend the balanced law \(\pi\) to a stationary full-support word process. For \(h=1\) use independent letters. For \(h>1\), take the common prefix/suffix mass on length-\((h-1)\) words as initial law, with the usual shift transition appending a letter with probability equal to the prescribed \(h\)-word mass divided by its prefix mass. The stated equality of marginals makes this stationary; all allowed extensions have positive probability. Use this law on the padded segment and an independent uniform \(M_0\) residue. The \(2^a\) and \(3^b\) components at each central time are given by the same functions of the adjacent future and past digit blocks. Stationarity therefore gives the same joint law of both components across times. The remaining component stays conditionally uniform. Again all bounded tests have mean zero under a strictly positive law on all realizable padded types. Consequently a nonnegative functional must vanish on every attainable vector.

In the finite-dimensional linear span of the attainable vectors, the last property implies that zero lies in the relative interior of their convex hull. Otherwise separation from the relative interior supplies a nonzero functional on that span which is nonnegative on every vector; for an affine hull missing zero a strictly separating constant linear functional already suffices. In particular some finite collection admits a real positive convex combination equal to zero, dropping zero-weight entries. All its equations, including normalization, are rational. Rational Gaussian elimination gives a rational affine parametrization of the solution set, and its strictly positive region is relatively open. Approximating the parameters by rationals provides positive rational weights. Clearing denominators gives finitely many integer tokens. Each token carries a true parameterized path, repeated according to these weights. At this stage multiplicities are allowed.

### Removing all repeats through equal-power-sum classes

Let \(W\) be the total number of tokens. For \(W>1\), partition \(0\le j<W^{d+1}\) into \(W\) classes by the sum of the \(d+1\) base-\(W\) digits modulo \(W\). Each class has exactly the same sums of \(j^k\) through degree \(d\), including degree zero. For a character \(\zeta\ne1\) with \(\zeta^W=1\), the corresponding generating polynomial is
\[
        \prod_{\ell=0}^{d}\ \sum_{c=0}^{W-1}\zeta^c z^{cW^\ell}.
\]
It has a zero of multiplicity at least \(d+1\) at \(z=1\), since every factor vanishes there. Applying \((z\,d/dz)^k\) for \(k\le d\) and using Fourier inversion on the \(W\) classes proves the claim. For \(W=1\) take the singleton class \(\{0\}\). This is the generalized Prouhet equal-power-sum construction.

Give one class to each token. Replace its parameter \(T\) by \(T_0+Lj\), once for every \(j\) in its class, using the same positive integers \(T_0,L\) throughout. The coefficientwise identities persist when summed over all these specialized trajectories: each power of \(T_0+Lj\) has the same sum across the classes. Word frequencies and residue histograms persist because the classes have equal size.

Finally select \(L\) greater than all absolute differences between the finitely many constant terms \(x_t\) in the token list. Between different indices \(j\) and \(j'\), equal positive slopes thus yield different specialized integers. For unequal slopes there is at most one forbidden value of \(T_0\) for any pair of vertex occurrences. The same \(j\) occurs in only one path, and on that path \(q_t v\) has distinct slopes at distinct times, since \(3^{t'-t}=2^{S_{t'}-S_t}\) is impossible for \(t'>t\). Take \(T_0\) larger than all the finitely many forbidden integers. All specialized vertices are then distinct as asserted, and stay above \(m\). This finishes the construction.

### A separate product calibration

The theorem above concerns ordinary power moments. Exact product balance by itself can also occur without a return, even for distinct sources and distinct successors. For the five sources \(19,25,29,43,143\), the actual odd successors are respectively \(29,19,11,65,215\). Both products are \(84{,}702{,}475\), and the native exponents sum to eight. Thus \(\prod(3x+1)=2^8\prod x\) holds exactly for this nonclosed set. This finite example gives no claim that simultaneous product balance can be added to the general power-moment theorem.

### Matching polynomial moments inside every residue and word class

**Stronger statement for a stationary prescribed word law.** The same conclusion holds simultaneously for
\[
            \sum_{i:\ x_{i,t}\equiv r\bmod M}x_{i,t}^k
                \qquad(0\le k\le d,\ r\bmod M)
\]
at every central time. One may further split each sum by any fixed finite block of neighboring native digits, padding actual paths with the required true letters. The balance concerns the indicated central layers. All their vertices can still be made distinct. This rules out the entire fixed family of polynomials whose coefficients are allowed to depend on a residue and a bounded native window.

Use a finite marked type \(s\) containing the \(M_0\)-residue at the current date and a block of native letters \([-L_-,L_+)\), with \(L_-\ge \max(1,b)\) and \(L_+\ge h+a\). Enlarge the padding on each side as needed for additionally requested word tests. An edge shifts the word one position, appends an arbitrary digit and updates the marked residue by \(\tau_e(r)=(3r+1)/2^e\) modulo \(M_0\), using the current digit \(e\). All edges have true unbounded CRT cylinders, as above.

This marked directed graph is strongly connected. On the finite \(M_0\)-residues the two permutations generate a group even using only positive compositions. It contains doubling \(D=\tau_1\tau_2^{-1}\). Since \(D\tau_1(x)=3x+1\) and \(\tau_1D(x)=3x+1/2\), their composition with the latter inverted is translation by \(1/2\). This acts transitively on residues. To connect two marked types, first follow the prescribed future suffix of the first word. The left and right letters of the target block can be imposed at the end of the path, with the target's past determining which residue is required at the start of that last fixed segment. Between the two fixed pieces insert a word carrying the current residue to that required residue. Arbitrary intervening digits are allowed. The all-one word with residue \(-1\) has a self-loop of multiplier \(3/2\); the all-two word with residue \(1\) has one of multiplier \(3/4\).

In the polynomial separation argument replace all moment tests by the coefficients of
\[
   \mathbf1_{s_1=s}(x_1+v_1T)^k-
   \mathbf1_{s_0=s}(x_0+v_0T)^k \qquad (s\text{ marked},\ 1\le k\le d).
\]
Also impose the unweighted marked-type counts at the two layers, and the desired centered word indicators. Consider a nonnegative functional whose largest polynomial degree is \(k\). For \(v/y\to\lambda>0\) its leading limit at every marked edge \(s\to s'\) is
\[
       (3/2^e)^k C_{s'}(\lambda)-C_s(\lambda)\ \ge0 .                 \tag{2}
\]
These are polynomials in \(\lambda\) made from the dual coefficients, as before. The expanding loop makes \(C_{s_{\rm hi}}(\lambda)\ge0\), the contracting loop makes \(C_{s_{\rm lo}}(\lambda)\le0\). A nonnegative value propagates forward along every edge by (2), so strong connectivity gives \(C_s(\lambda)\ge0\) everywhere and zero at the contracting loop. A strictly positive value would also propagate there, so all values vanish. This holds for every \(\lambda>0\), hence every coefficient of largest degree vanishes. The stationary full-support padded word law and the uniform independent residue again dispose of the bounded part. Finite convex separation and rational approximation now give a positive integer token list with identical *conditional polynomial moments* through degree \(d\) of its two layers at each marked type.

Here these one-step identities control the whole truly realized \(h\)-edge path. For \(0\le j<h\), the prescribed future letters of the marker fix an affine expression \(x_j=q x+c\) from its current state \(x\). Its residue at offset \(j\) is determined by the marker: the \(M_0\) component uses its recorded start and digits, the \(2^a,3^b\) components use the corresponding padded future and past digits. Each additional local word test is determined by the enlarged marker as well. Thus a class-filtered \(k\)-th moment at offset \(j\) is a fixed polynomial of degree at most \(k\) in the current \(x\) on each type. Applying this polynomial to the parameterized conditional moment balance from the first to second layer equates the quantities at offsets \(j\) and \(j+1\).

When choosing the shift modulus \(Q\), include \(6M\,2^{2(h+L_++L_-+2)}3^{L_-+1}\). The future native digits persist by their dyadic cylinder; the preceding \(L_-\) letters have integral odd predecessors after translation, since the new predecessor shifts are the old-parameter increment times \(2^{S}/3^\ell\), and are even integer multiples of \(3M\). A sufficiently positive translation retains positivity throughout the fixed padding. The vertex-distinct specialization by the same Prouhet classes therefore preserves every requested conditional identity and word test. This proves the stronger statement.

### Finite rational observables with positive integer multiplicities

There is a separate extension for which the conclusion allows positive integer multiplicities. Replace the degree-\(d\) power tests, within any of the indicated marked classes, by any *finite* list of rational functions in \(\mathbb Q(X)\), including reciprocal powers. Require states above all their real poles. Actual \(h\)-edge paths with positive integer multiplicities can match every indicated time slice exactly under the same stationary word law. Their initial and terminal supports can still be forced disjoint.

For a one-step list, work directly with the unshifted parameter \(y\). A nonnegative dual has the form
\[
             F_{s'}(q y+c)-F_s(y)+b_{\rm edge}\ \ge0
\]
on all large starts in each genuine cylinder, where \(F_s\) are real linear combinations of the requested rational functions and \(b_{\rm edge}\) denotes the bounded type and word tests. A largest positive growth degree \(k\), if present in any \(F_s\), would give the same nonnegative edge inequalities (2) for its leading coefficients. The two loops and strong connectivity force these coefficients to vanish. Hence every \(F_s\) has a finite limit at infinity. The limiting edge tests are nonnegative and have zero mean under the stationary positive type law, so their value is exactly zero on every edge. Subtract these constants. If any \(F_s\) has a nonconstant remainder, choose the smallest \(k\ge1\) for which the coefficient of \(y^{-k}\) in any remainder is nonzero. Scaling by \(y^k\) yields (2) with \(q^{-k}\) in place of \(q^k\). The expanding and contracting loops exchange roles, and the same argument again forces all coefficients to vanish, a contradiction. Thus the dual is zero on every vector.

The original input vectors are rational, so finite separation again gives positive rational and then integer weights. To cover \(h\) layers, include the finitely many translates \(f(q_jX+c_j)\) given by the finite future words and apply the one-step conditional identities as above. One may exclude overlaps of the initial and terminal supports in advance by requiring \(y\equiv r\bmod\ell\) for an auxiliary prime \(\ell\nmid6M\). Choose \(\ell>2^h\) dividing none of the \(3^h-2^S\) for \(h\le S\le2h\). For each terminal word the congruence \(q_h r+c_h=r\bmod\ell\) then has one solution; avoid all of these finitely many disallowed residues. This extra class leaves every required cylinder unbounded by CRT. The polynomial Prouhet argument used to make all vertices distinct above does not extend directly to the rational functions in this paragraph; other vertices and positive multiplicities may coincide.
