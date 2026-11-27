# Uniform inverse-fiber savings for stationary gap languages

**Proposed arithmetic corollary O18, conditional on O15's entropy proof.** Let \(D\) be a finite set of positive Syracuse exponents, and \(S\subset D^{\mathbb Z}\) any nonempty closed shift-invariant language. Let \(\mathcal L_n(S)\) be its length-\(n\) words and \(h(S)=\lim n^{-1}\log|\mathcal L_n(S)|\). At a fixed odd positive endpoint \(a\), count the words in \(\mathcal L_n(S)\) that can actually be followed backwards from \(a\), with \(I_e(a)=(2^ea-1)/3\) an integer at every step. Then
$$
 \lim_{n\to\infty}\frac1n\log\max_a
      \#\{w\in\mathcal L_n(S):w\text{ legal at }a\}
       =\max(0,h(S)-\log3).
$$
The maxima can be taken over odd endpoints from any particular ordinary positive merge component. This gives a uniform, subexponential fiber bound even for positive-entropy languages when \(h(S)\le\log3\).

In particular, fix \(C\ge0\). Consider finite inverse gap words satisfying
$$
       \sum_{j=t}^{t+\ell-1} e_j \le \ell\log_2 3+C               \tag{A}
$$
for every interval contained in the word. The maximal number legal at one ordinary endpoint is \(\exp(o(n))\) for words of length \(n\), uniformly over endpoints. Inequality (A) says that the forward coefficient \(3^\ell/2^{\sum e_j}\) cannot drop below \(2^{-C}\) on any block. It is stronger than placing a floor only under products measured from one starting time. It permits a single infinite ordinary witness, which a multiplicity bound cannot rule out.

## The stationary entropy lemma without Markov restrictions

Let \(\nu\) be an arbitrary stationary ergodic law on two-sided gap sequences of finite mean, and let \(X_0=\pi(E_0,E_1,\ldots)\) be the ternary contraction coding by \(G_e(y)=(3y+1)/2^e\). Let \(\mathcal G\) denote the full past-label sigma-field. Put
$$
                \beta=H_\nu(E_0\mid\mathcal G,X_0).
$$
Writing \(X_j\) for the coding at time \(j\), we claim
$$
        \lim_{n\to\infty}H(X_0[n])/n=\min(h_E,\log3),
        \qquad
        \beta=\max(0,h_E-\log3),                             \tag{B}
$$
where \(h_E\) is the label entropy rate. This is a Shannon-dimension statement, distinct from O15's worst-cylinder conclusion.

To check the extension, retain the notation of O15. The labels before time \(j\), together with \(X_0\), determine \(X_j\), and conversely \(X_j\) and those intervening labels determine \(X_0\) by the affine maps. The chain rule now gives \(H(W_n\mid X_0,\mathcal G)=n\beta\). Also
$$
 H(W_n\mid B_n,\mathcal G)
 \le\sum_{d=1}^n H(E_0\mid\mathcal G,X_0[d])=n\beta+o(n).
$$
Because \(B_n=X_0[n]\) is determined by \(W_n\),
$$
 I(W_n;\mathcal G\mid B_n)\le I(W_n;\mathcal G)
             =H(W_n)-nh_E=o(n).
$$
Consequently \(n\beta\le H(W_n\mid X_0)\le H(W_n\mid B_n)\le n\beta+o(n)\). Both (5) and (6) of O15 follow.

In the Bayes recursion (7), replace \(q_e(X_0)\) by the conditional probability of \(E_0=e\) given \((\mathcal G,X_0)\). The preceding entropy \(\beta\), the log-posterior convergence, and the conditional information rate (8) then have exactly the same proofs. O15 Sections 4–7 use (5), (6), (8), stationarity, ergodicity and finite mean, with no additional Markov assumption. Hence \(F=h_E-\beta\) and either \(\beta=0\) or \(F=\log3\). As \(0\le F\le\log3\), these equalities prove (B), including at \(h_E=\log3\).

## Count actual finite words

Every word fixes one full target cylinder modulo \(3^n\), giving a lower bound \(|\mathcal L_n(S)|/3^n\) on the maximum. There is at least one legal positive endpoint for each word. Every maximizing cylinder is a unit cylinder and contains arbitrarily large positive odd endpoints of each merge component, by the elementary doubling and odd-inverse argument of O16; the branches then have positive ordinary values. Distinct exponent words at a fixed odd endpoint give distinct ordinary sources by forward determinism and uniqueness of the successive odd-to-odd valuations.

For the upper bound, choose a sequence of maximizing cylinders along a subsequence attaining the limsup. At each \(n\), choose uniformly among the maximizing fiber's distinct words. Extend each such word to a two-sided sequence in \(S\), obtaining a law \(\xi_n\). Let \(\nu_n=n^{-1}\sum_{j=0}^{n-1}\sigma^j_*\xi_n\). Compactness gives an invariant subsequential limit \(\nu\) supported on \(S\). For the fixed \(n\)-fiber, all \(X_0[n]\) are the same. For \(0\le j\le n-h\), \(X_j[h]\) is therefore determined by the first \(j\) labels and that common residue.

Fix \(h,m\ge1\). All terms in the chain rule for \(H_{\xi_n}(W_n)\), except at most \(m+h\) endpoint terms, are at most the corresponding
\(H_{\xi_n}(E_j\mid X_j[h],E_{j-m},\ldots,E_{j-1})\), because the conditioning variables here are determined by the preceding labels and the common starting residue. Bound the omitted terms by \(\log|D|\), and add any missing nonnegative terms to the enlarged sum. Concavity of conditional entropy, followed by continuity on these finite alphabets, gives
$$
 \limsup_n n^{-1}H_{\xi_n}(W_n)\le H_\nu(E_0\mid X_0[h],E_{-m},\ldots,E_{-1}).
$$
For this step \(X_0[h]\) is locally constant in the first \(h\) labels. Let \(h=m\to\infty\) to bound the growth exponent by \(H_\nu(E_0\mid X_0,\mathcal G)\).

In the ergodic decomposition of \(\nu\), the invariant sigma-field is contained in the completed past-label sigma-field: approximate any invariant event by cylinders and shift them arbitrarily far into the past. Thus this last conditional entropy is the average of \(\beta\) for the ergodic components. Each has \(h_E\le h(S)\) by the finite word-count bound on entropy. Formula (B) yields the desired upper bound \(\max(0,h(S)-\log3)\).

## The bounded-drawdown application

Property (A) bounds each letter, so the alphabet is finite. It defines a closed shift-invariant language. Every finite word satisfying (A) extends by constant ones on both sides, since \(\log_2 3>1\) and \(C\ge0\). Put \(\kappa=\log_2 3\). Counting all positive compositions of length \(n\) and total at most \(\lfloor\kappa n+C\rfloor\) bounds the language size by \({\lfloor\kappa n+C\rfloor\choose n}\). Hence
$$
   h(S)\le \kappa\log\kappa-(\kappa-1)\log(\kappa-1)<\log3.
$$
The strict comparison follows without numerical approximations: \(\kappa<8/5\) since \(3^5<2^8\), the displayed entropy function increases for \(\kappa>1\), and its value at \(8/5\) is below \(\log3\) because \(8^8<5^5 3^8\). Applying the first theorem gives the claimed all-endpoint savings at every fixed C.

The result controls paths satisfying a condition on every internal interval. An ordinary orbit with nondecreasing lower envelope measured only from its initial point can have unbounded coefficient drawdowns from later peaks. Neither uniform \(C\) for that orbit nor a fixed-floor basin estimate follows here.
