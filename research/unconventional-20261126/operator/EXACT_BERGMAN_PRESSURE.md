# Exact Bergman radius from the entropy of an inverse branch process

**Proposed theorem O15, for independent review.** The spectral radius of Béhani's shortcut Collatz transfer on the classical Bergman quotient by degrees 0, 1 and 2 is exactly

$$
R=\sqrt{20}/3 .
$$

The assertion concerns an operator on the specified Hilbert space. It does not decide whether every positive Collatz orbit reaches 1.

The main new step proposed here extends the entropy-gain argument of *Stationary inverse laws, optimal window limits, and slow terminating Collatz families*, rStation paper 127/v1, Sections 3–6 and 9. That source assumes fixed exponent caps and locally constant inverse probabilities. Its exact conditional independence is unavailable for the measurable, countable-alphabet pressure policy below. We prove a sublinear conditional mutual information estimate, use its chain rule on overlapping windows, and prove the required averaged component entropy estimate directly. No uniform convergence rate or continuity of the pressure policy is assumed.

## 1. The pressure theorem

Write X=Z_3 with additive Haar probability, let p=(p_e) be the positive geometric law p_e=p(1-p)^(e-1), 0<p<1, and define

$$
Bf(x)=\sum_{e\ge1}3p_e\,{\bf1}_{\,2^ex\equiv1\bmod3}f(I_e x),\qquad I_e x=(2^e x-1)/3 .
$$

It acts positively on C(X) in the supremum norm. The series converges in operator norm. Its adjoint relative to Haar sends g to the Markov average of g((3x+1)/2^e) with probabilities p_e. In particular the integral of Bf equals that of f. We prove

$$
r(B)=\max(1,3p). \tag{1}
$$

The first lower bound follows from the preserved integral. The branch e=1 fixes x=-1 and gives the lower bound 3p by iteration. O13 gives R=sqrt(20)/3 when r(B)=1 at p=1/10, proving O15 from (1).

Here and below, for an X-valued variable Y, write Y[k] for its reduction modulo 3^k, H_k(Y)=H(Y[k]), and take all entropies with natural logarithms. For conditional laws H(Y|C) denotes the averaged conditional entropy; when the entropy of the conditional probability vector is needed as a random variable we write h(Y|C)(c). All variables with at most 3^m outcomes have entropy between zero and m log 3.

## 2. From a maximum row to an invariant policy

For each n choose x maximizing B^n1 and sample its legal length-n paths under probabilities proportional to the word weights $\prod_{j=0}^{n-1}3p_{E_j}$. Put X_0=x and X_(j+1)=I_(E_j)X_j. Let eta_n be the average of the n laws of (X_j,E_j), and mu_n its state marginal. All relevant entropies are finite at each n: the unnormalized word law is bounded by 3^n times the iid law, and a geometric letter has finite mean. The Gibbs identity for this finite-time normalized countable distribution, conditioning on X_j instead of the full previous word, and concavity of conditional entropy give

$$
n^{-1}\log\|B^n\|\le\log 3-D(\eta_n\Vert\mu_n\otimes p). \tag{2}
$$

In detail H(W_n)=sum H(E_j|E_0,...,E_(j-1)), and X_j is determined by those labels and the fixed start. The average of H(E_j|X_j) is at most H_(eta_n)(E|X), by adjoining the time index and then discarding it. Expanding the relative entropy gives (2).

The row norm is at least one, so the divergences in (2) are bounded by log 3. The entropy inequality applied to tE for a sufficiently small t>0 yields

$$
\sup_n\int e\,d\eta_n\le[\log3+\log\sum_e p_e e^{te}]/t<\infty .
$$

For unbounded tE use its increasing bounded truncations first. Compactness of X and this bound give tightness. Extract a weak limit eta, with state marginal mu. The edge set is closed in the state-label product with the label discrete; the limit remains legal. The endpoint map is continuous on that closed legal set, and the expected terminal-state law differs from the expected initial-state law by a telescoping endpoint term of total variation at most 2/n. Thus eta has equal initial and final marginals. Relative entropy is jointly lower semicontinuous under weak convergence of both measures (equivalently use its bounded-continuous variational formula); mu_n times p converges weakly to mu times p. Disintegrate eta into measurable inverse probabilities q_e(x). Then

$$
\log r(B)\le\log3-\int D(q(x)\Vert p)\,d\mu(x)=\log3+\beta+\mathbb E\log p_E,\quad \beta=\int H(q(x))\,d\mu(x). \tag{3}
$$

The limit has finite mean letter by lower semicontinuity. Finite mean bounds countable entropy by comparison with a geometric law, and for geometric p the log likelihood is integrable.

Start a two-sided stationary Markov edge process with state law mu and this transition rule. Its ergodic components still use the same transition rule almost surely. Indeed, invariant events of the two-sided stationary process belong to the completed past sigma-field: approximate such an event in probability by cylinders and shift those cylinders arbitrarily far into the past, using invariance. Conditioning on that field of invariant events thus preserves the conditional next transition given the past and present state. Using a countable generator gives the same Markov kernel in almost every ergodic component. Equivalently one may use the ergodic decomposition theorem for stationary Markov laws. The right side of (3) averages the corresponding component rewards and the means are finite almost surely. It suffices to upper-bound the reward of each ergodic component of finite mean.

We prove the following dichotomy for **any** stationary ergodic Markov process on legal inverse edges with measurable q and finite mean positive exponent:

$$
F:=\lim_{k\to\infty}H_k(X_0)/k=h_E-\beta,\qquad \beta=0\ \text{or}\ F=\log3. \tag{4}
$$

where h_E is the stationary label entropy rate; the last identity applies also when beta=0. Once (4) is proved, a zero-branch-entropy component has reward at most log(3p), since p_e≤p. A positive-branch-entropy component has reward h_E+E log p_E≤0: h_E≤H(E_0), and H(E_0)+E log p_E is the negative divergence of its marginal label law from p. Equation (1) follows.

## 3. Near-independence and the conditional information rate

Fix the ergodic process in (4). Put W_n=(E_0,...,E_(n-1)) and B_n=X_0[n]. The inverse affine relation gives B_n as a deterministic function of W_n: the reverse maps G_e(y)=(3y+1)/2^e contract by exactly one ternary digit. Also (B_n,E_0,...,E_(j-1)) determines X_j[n-j]. By the Markov property H(W_n|X_0)=n beta. Hence

$$
I(W_n;X_0\mid B_n)=H(W_n\mid B_n)-n\beta
 \le\sum_{d=1}^n\bigl(H(E_0\mid X_0[d])-\beta\bigr)=o(n). \tag{5}
$$

The last conditional entropies decrease to H(E_0|X_0)=beta since H(E_0)<infinity. Because B_n is a function of W_n, H(B_n)=H(W_n)-H(W_n|B_n). Thus

$$
H_n(X_0)/n\longrightarrow F=h_E-\beta. \tag{6}
$$


Let G be the entire past label sigma-field, lambda the conditional law of X_0 given G, and J_k=-log lambda(B_k(X_0)), where B_k(x)=x+3^kX. Write S for the path shift, a_e=P(E_0=e|G), and b_(k,e)=P(E_0=e|G,X_0[k]). For the realized letter, Bayes' formula and the affine branch bijection from the current k-ball to the next (k-1)-ball give the exact recursion

$$
J_k=J_{k-1}\circ S-\log a_{E_0}+\log b_{k,E_0},\qquad k\ge1,\quad J_0=0. \tag{7}
$$

In particular, the factor is the average branch probability on the ball, even when q_e varies across it. Conditional on G and X_0 the next probabilities are q_e(X_0). Thus b_(k,E_0) converges almost surely to q_(E_0)(X_0), which is positive almost surely. The nonnegative random variables -log b_(k,E_0) converge in L¹: their expectations H(E_0|G,X_0[k]) converge to H(E_0|G,X_0)=beta, since the unconditional countable entropy is finite. Nonnegative convergence almost surely with convergence of the means gives L¹ convergence. Also E[-log a_(E_0)]=h_E.

Iterate (7). Replacing each log b_(k-j,E_j) along the shift with the corresponding log q incurs mean absolute error o(k) by the Cesàro average of the preceding L¹ differences and stationarity. The L¹ ergodic theorem for the remaining integrable increment gives

$$
J_k/k\to F\quad\text{in }L^1. \tag{8}
$$


## 4. The needed component porosity is averaged over scales

Write H_k=H_k(X_0) and let

$$
s_{k,m}(B_k)=h(X_0[k+m]\mid X_0[k])(B_k),\qquad t_{k,m}(W_k)=h(X_0[k+m]\mid W_k)(W_k).
$$

For each fixed word the affine isometry between the free m digits identifies its terminal m digits with the extra m initial digits. Thus t_(k,m) has the distribution of h(X_0[m]|E_(-k),...,E_(-1)). For fixed m these conditional vectors converge by the martingale theorem, so their entropies converge in L¹ to

$$
R_m=h(X_0[m]\mid\mathcal G)=\mathbb E[J_m\mid\mathcal G].
$$

Consequently E|R_m/m-F| tends to zero by (8).

Since B_k is determined by W_k, the entropy-of-mixture identity for each B_k writes

$$
s_{k,m}=\mathbb E[t_{k,m}\mid B_k]+d_{k,m}(B_k),\quad d_{k,m}\ge0,\quad
\mathbb E d_{k,m}=H_{k+m}-H_k-\mathbb E t_{k,m}. \tag{9}
$$

Fix any positive integer K. Averaging over k=n,...,n+Kn-1, the average of H_(k+m)-H_k tends to mF for fixed m, by telescoping the m boundary terms at either end and using (6). The average of E t_(k,m) tends to E R_m. By (9) and the triangle inequality,

$$
\lim_{m\to\infty}\limsup_{n\to\infty}
\frac1{Kn}\sum_{k=n}^{n+Kn-1}\mathbb E\,|s_{k,m}/m-F|=0 . \tag{10}
$$

Indeed the fixed-m upper bound is
$\mathbb E|R_m/m-F|+F-\mathbb E R_m/m$.
No all-scale uniform assertion is required.

## 5. Branch noise has linearly many informative digits

Suppose beta>0 and F<log 3. Fix an integer K>E E_0, L=Kn, B=B_n, and A=sum of the n letters. Put C=(B,A) and represent B by its least nonnegative integer. Write X_0=B+3^n Z. The actual endpoint decomposes as

$$
X_n=U+V,\qquad U=2^A Z,\qquad V=(2^A B-c_{W_n})/3^n,\quad c_0=0,\quad c_{j+1}=2^{E_j}c_j+3^j. \tag{11}
$$

Here V is an integer. For fixed total A, c_(W_n) determines the word: c_1=1 and all nonempty carries are odd. At each backward step j≥1, the exact binary valuation of c_(j+1)-3^j recovers E_j, then division recovers c_j. The total supplies E_0. Also 0<c_(W_n)<2^A3^n for n≥1 by expansion of the recurrence. If A≤Kn, two different fixed-total words therefore cannot produce the same V modulo 3^L: such a collision would force their distinct carries to differ by a nonzero multiple of 3^(n+L), whereas 2^A<3^L.

The total entropy H(A) is O(log(n+1)): a nonnegative integer variable of mean n E E_0 has entropy at most $1+\log(1+n\,\mathbb E E_0)$ by the maximum-entropy geometric bound. On A>Kn, the conditional word entropy given A is at most A log 2 by counting compositions. Ergodicity and finite mean give A/n→E E_0 in L¹, so E[A 1_(A>Kn)]=o(n). In conjunction with H(W_n|B)≥n beta, this yields

$$
H(V[L]\mid C)\ge n\beta-o(n). \tag{12}
$$

For the dependence between the two summands, conditioning on C and applying data processing gives

$$
I(U;V\mid C)\le I(Z;W_n\mid B,A)\le I(X_0;W_n\mid B)=o(n) \tag{13}
$$

by (5). The second inequality uses that A is a function of W_n.

## 6. Conditional independence on a typical short window

For i≥0, denote by U and V's local m-digit blocks their next m ternary digits after i digits, reducing in the group Z/3^m. Condition on C and both lower prefixes U[i],V[i]. Let P_i be the actual conditional *joint* law of the two blocks. Let Q_i be the product of the conditional input block laws obtained when each component is conditioned only on C and its own lower prefix. The chain rule for relative entropy gives exactly

$$
\mathbb E D(P_i\Vert Q_i)=I(U[i+m];V[i+m]\mid C)-I(U[i];V[i]\mid C).
$$

The increments are nonnegative. For each fixed m, summing i=0,...,L-1 costs at most m times the total mutual information in (13). In particular

$$
\sum_{i=0}^{L-1}\mathbb E D(P_i\Vert Q_i)=o(n). \tag{14}
$$

Pinsker's inequality and bounded uniform continuity of entropy on the fixed 3^m-symbol simplex imply that the sum over these i of the expected absolute discrepancies in the *output* block entropies is o(n). The output block is the sum modulo 3^m of the two blocks plus a carry fixed by their two lower prefixes. The limit n→infinity is taken with m fixed throughout (14).

We also need the base block before and after recording A to be close on most scales. Given B,A, the map Z↦2^A Z permutes the i-prefix cells and permutes their free m digits. Thus the entropy of U's block given C,U[i] equals that of Z's block given B,A,Z[i]. Compare this conditional vector with the law given B,Z[i] alone. The expected relative entropy of these two block laws is the increment from i to i+m of I(A;Z[i]|B). Its sum over i<L is at most m H(A)=O(m log(n+1)). Pinsker and finite-alphabet continuity again give total expected absolute entropy discrepancy o(n). The latter, unconditioned-on-A block entropy is exactly s_(n+i,m) of the realized source. It follows from (10) that for any given epsilon>0 we can choose a fixed m so large, and then n so large, that the expected proportion of base blocks whose entropy exceeds m(log3-c) is at most epsilon, where c=(log3-F)/2. No hypothesis concerning regularity of q at a particular cylinder enters this comparison.

## 7. Local addition gives a contradiction

Choose epsilon=beta/(8K log3) and gamma=beta/(4K). A one-digit noise block is good when the entropy of the next digit of V conditioned on C,V[i] is at least gamma. From (12) and the digit entropy chain rule the sum over i<L of its good probabilities is at least

$$
(n\beta-\gamma L-o(n))/\log3 .
$$

After subtracting the expected number of bad base blocks from Section 6, the sum of probabilities that both the base and noise are good is at least a positive constant times n. No independence is needed for this subtraction. The constants are admissible since beta≤H(E_0)≤E E_0 times log 2 for positive integer letters, by comparison with the law 2^(-e).

On the finite cyclic group Z/3^m there is a number d>0, depending on fixed m,c,gamma, such that

$$
H(u*v)-H(u)\ge d\quad\text{if}\quad H(u)\le m(\log3-c),\quad H(v\bmod3)\ge\gamma.
$$

Indeed convolution is a mixture of translates. Equality forces all translates with positive weights to coincide by strict concavity of entropy, and two support elements of v whose residues differ modulo 3 have a unit difference generating the entire group. Equality would force u uniform. Compactness of the constrained simplices gives a positive gap. Without these two hypotheses the gain is still nonnegative. This is the finite-group observation in paper 127, Section 5.

Set $g_j=H(X_n[j]\mid C)-H(U[j]\mid C)$. Conditioning on both lower input prefixes gives at least as much information as conditioning on their lower sum, hence

$$
g_{i+m}-g_i\ge \mathbb E\bigl[H(\text{actual local sum law under }P_i)- H(\text{local base law given }C,U[i])\bigr].
$$

Replacing P_i with the product Q_i changes the sum of the lower bounds by o(n) in absolute value by (14). The finite-group gain and the positive linear number of good overlaps give

$$
\sum_{i=0}^{L-1}(g_{i+m}-g_i)\ge c_1n-o(n),\qquad c_1>0 . \tag{15}
$$

In the opposite direction stationarity gives H(X_n[j]|C)≤H_j, while

$$
H(U[j]\mid C)=H(Z[j]\mid B,A)\ge H_{n+j}-H_n-H(A).
$$

Consequently $g_j\le H_j-H_{n+j}+H_n+H(A)=o(n)$ for each j=L,...,L+m-1 by (6). Also the first m values g_0,...,g_(m-1) have absolute value at most m log3. The left side of (15) telescopes to the sum of the last m values less the sum of the first m values, hence is bounded above by o(n). This contradiction proves (4), and completes (1) and O15.

## Boundaries and checks

The unused stronger conclusion that the biased stationary density is bounded need not follow from (1). The proof identifies the exponential rate of its largest cylinders, which is sufficient for the Bergman spectral radius. Branching entropy zero is a genuine alternative: at x=-1 the stationary deterministic e=1 path has beta=0 and supplies the lower bound 3p. For p=1/2 formula (1) gives the known maximal density growth 3/2. For p=1/10 it gives one.

Sources for definitions and the comparison argument:

- V. Béhani, *Linear dynamics of an operator associated to the Collatz map*, Proc. Amer. Math. Soc. 152 (2024), 1191–1206, Proposition 4.2 and Question 4.1, <https://arxiv.org/pdf/2303.03203>.
- Lyapunov Weaver, *Stationary inverse laws, optimal window limits, and slow terminating Collatz families*, rStation paper 127/v1, Sections 3–6 and 9, <https://rstation.ai/problems/collatz/papers/127/v1>. The finite-group entropy gap and local addition argument are taken from there. Sections 3–7 above replace its finite-memory conditional independence and its fixed-cap offset bound at the places stated.
- T. Tao, *Almost all orbits of the Collatz map attain almost bounded values*, Forum Math. Pi 10 (2022), Lemma 6.2, <https://doi.org/10.1017/fmp.2022.8>. Fixed-total offset decoding is included above.
- The untilted maximum-density exponent is recorded in rStation paper 9, <https://rstation.ai/problems/collatz/papers/9>, as a check at p=1/2. Neither this value nor numerical finite tables is used to prove O15.
