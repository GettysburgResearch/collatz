# From stationary inverse policies to uniform finite credit

**Status: PROPOSED general theorem with a complete argument; the Collatz
corollaries below are SOURCE-QUALIFIED by an external stationary-law theorem.**

This note explains why a sufficiently economical stationary inverse policy
can produce an ordinary, deterministic, all-input credit certificate. It
does not transfer the policy's statistical law to the forward orbit of a
supplied integer. The distinction is essential.

## 1. Space, actions, and the imported hypothesis

Let \(X=\mathbb Z_3^\times\), fix an exponent cap \(R\ge6\), and put

\[
 I_e(z)=(2^ez-1)/3,\qquad
 E_R(z)=\{1\le e\le R:I_e(z)\in X\}.
\]

The legal domains are clopen and determined modulo nine. Each branch on
its legal domain is continuous and consumes one ternary digit. A positive
local policy assigns every legal action a strictly positive probability,
with all probabilities determined by finitely many ternary digits. Its
Markov operator is

\[
 Pf(z)=\sum_{e\in E_R(z)}p_e(z)f(I_ez).
\]

It is Feller: it maps continuous functions to continuous functions. Its
expected one-step exponent is the continuous function
\(a_P(z)=\sum_e e p_e(z)\).

We use the following hypothesis only where explicitly stated:

> **UQ(R).** Every positive local policy with cap \(R\) has a unique
> stationary Borel probability \(\mu_P\) on \(X\), among all Borel
> probabilities, not just those with a locally constant density.

[Lyapunov Weaver, rStation paper 127, version 1, Theorem 5](https://rstation.ai/problems/collatz/papers/127)
asserts UQ(R) for every \(R\ge6\), with an explicit finite description of
each stationary density. Its infinite-dimensional proof is an external
input, not something certified by this packet's integer computations.
The implication developed here needs uniqueness, rather than a separately
assumed rate or a forward-orbit equidistribution theorem.

## 2. Why the expected estimate is uniform

**Lemma D1.** If a Feller kernel on a compact metric space has unique
stationary probability \(\mu\), then for every continuous \(f\),

\[
 \sup_z\left|\frac1N\sum_{j=0}^{N-1}P^jf(z)-\mu(f)\right|\to0.
 \tag{1}
\]

**Proof.** If not, choose \(N_i\to\infty\) and \(z_i\) violating (1).
The measures \(\nu_i=N_i^{-1}\sum_{j<N_i}\delta_{z_i}P^j\) have a weakly
convergent subsequence by compactness. For any continuous \(g\),

\[
 |\nu_i(Pg-g)|
 =|P^{N_i}g(z_i)-g(z_i)|/N_i\le2\|g\|_\infty/N_i.
\]

The Feller property therefore makes the limit stationary. It must be
\(\mu\), contradicting the chosen violation for \(f\). This proves (1).

This is the precise source of the universal quantifier in the next step.
Pointwise convergence at each separate root would not suffice by itself.

## 3. The finite min-plus construction

Fix positive integers \(p,q\), and write \(\rho=p/q\). Define

\[
 (Ff)(z)=\min_{e\in E_R(z)}\{qe-p+f(I_ez)\}.
 \tag{2}
\]

Then \(F^j0(z)\) is the minimum adjusted cost
\(\sum_{i<j}(qe_i-p)\) of a legal inverse word of exactly \(j\) steps
from the actual supplied state \(z\). It is integer-valued and constant
modulo \(3^{j+1}\) for \(j\ge1\). The constant function at \(j=0\) requires
no digits.

**Theorem D2 (uniform block to finite credit).** Suppose, for some
\(N\ge1\),

\[
 F^N0(z)\le0\quad\text{for every }z\in X. \tag{3}
\]

There is a nonnegative integer potential \(W\), constant on a finite
ternary quotient, and a legal deterministic selector such that

\[
 qe+W(I_ez)\le p+W(z)\quad\text{for every }z\in X. \tag{4}
\]

One may take

\[
 V=\min_{0\le j<N}F^j0,\qquad W=V-\min_XV. \tag{5}
\]

**Proof.** The operator \(F\) preserves finite pointwise minima and
commutes with addition of constants. Hence

\[
 FV=\min_{1\le j\le N}F^j0
 \le\min_{0\le j<N}F^j0=V,
\]

because \(F^N0\le0=F^00\). Shifting by the finite minimum preserves the
inequality. The minimum exists because the functions in (5) are integer
locally constant functions on a compact space. Choosing a minimizing
action gives (4).

For \(N\ge2\), \(W\) is constant modulo \(3^N\); an action minimizing
\(FW\) can read modulo \(3^{N+1}\). Store the same potential values on
that one-digit-finer quotient. If \(z=r+3^{N+1}u\), then

\[
 I_ez=I_er+2^e3^Nu.
\]

The added term cannot change \(W\). Thus a single selected action at
\(r\bmod3^{N+1}\) works for all unseen higher digits, including all
three lifts required by the verifier format in [PROOF.md](PROOF.md).
For \(N=1\), use the quotient modulo nine. There is no free choice of
the supplied state's higher digits.

The potential is a bounded credit, not an integer-valued rank decreasing
by itself. Along its selected infinite inverse path, (4) telescopes to

\[
 \sum_{i<n}e_i\le \rho n+W(z_0)/q\quad(n\ge1). \tag{6}
\]

An independent exhaustive procedure can find such a certificate: increase
\(N\), compute \(F^N0\) on its full finite quotient, and stop when (3)
holds. No useful complexity bound follows from this observation.

## 4. Stationary means produce uniform certificates

**Theorem D3.** Let \(P\) be a positive local policy with a unique
stationary probability, and let \(A_P=\mu_P(a_P)\). For every rational
\(\rho>A_P\), a finite certificate (4) exists with that slope and the
same action cap \(R\).

**Proof.** Lemma D1 applied to \(a_P\) gives, for some finite \(N\),

\[
 \sup_z\mathbb E_z\sum_{i<N}(qE_i-p)<0. \tag{7}
\]

At each state, the minimum over its finitely many legal words is at most
the expectation under \(P\). Therefore \(F^N0<0\) everywhere. Apply D2.

The policy is used only to prove a uniform finite-word existence
statement. After the finite potential has been found, its exact
inequalities prove (6) without probability or an ergodic theorem.

## 5. Converse and the optimal credit value

For a fixed cap \(R\), let \(\rho_{\mathrm{credit}}(R)\) be the infimum
of rational slopes admitting a finite all-lift certificate (4). Let

\[
 A_*(R)=\inf_{P}\mu_P(a_P), \tag{8}
\]

where the infimum runs over positive local policies with cap \(R\).

**Theorem D4.** Under UQ(R),

\[
 \boxed{\rho_{\mathrm{credit}}(R)=A_*(R).} \tag{9}
\]

**Proof.** D3 gives \(\rho_{\mathrm{credit}}(R)\le A_*(R)\).
Conversely, take a certificate of slope \(\rho=p/q\), with
\(0\le W\le C\), and its deterministic local selector \(D\). Mix \(D\)
with the uniform legal-action rule \(Q\):

\[
 P_\varepsilon=(1-\varepsilon)D+\varepsilon Q,
 \qquad 0<\varepsilon<1. \tag{10}
\]

This is a positive local policy. The adjusted cost
\(qe-p+W(I_ez)-W(z)\) is nonpositive on the \(D\) action and at most
\(H=\max(0,qR-p+C)\) on every legal action. Integrate against its
stationary law. Stationarity cancels the potential, yielding

\[
 q\mu_{P_\varepsilon}(a_{P_\varepsilon})-p\le\varepsilon H. \tag{11}
\]

Thus \(A_*(R)\le\rho\), by taking arbitrarily small positive
\(\varepsilon\). No convergence or continuity of the stationary laws as
\(\varepsilon\downarrow0\) is needed. Taking the infimum over certificates
proves (9).

This identifies two different optimization problems. The finite quotient
policy in the source averages over hidden digits. The certificate here
has one action valid for every hidden lift. Enlarging the precision using
D2, rather than treating an average as a pointwise inequality, supplies
the missing bridge.

Strict positivity cannot be discarded when interpreting (9). A
deterministic local rule can choose \(e=1\) in the class \(8\bmod9\).
Then \(I_1(-1)=-1\), so \(\delta_{-1}\) is a stationary law with mean
cost one. This is a negative integer, not a positive Collatz
counterexample. It shows why the source's positive-policy theorem does
not classify all selectively chosen inverse histories, and why taking
zero-noise limits without proving which stationary law is selected would
be an unsupported step.

## 6. A source-qualified strict sub-two consequence

We independently regenerated a cap-six local policy of the type in
Paper 127, Corollary 8. The included
[small_positive_policy.json](small_positive_policy.json) specifies a
preferred legal exponent at each of the 486 unit residues modulo 729.
That exponent has probability 99/100; the other legal exponent has
probability 1/100. A rational bias vector on the 162 unit cells modulo 243
is checked by [verify_small_policy.py](verify_small_policy.py).

For clarity, let \(K\) be the finite transition matrix obtained by
averaging the three lifts of each source cell modulo 243, and let
\(\bar a\) be the correspondingly averaged exponent cost. A law uniform
within each of these cells remains of this form after one transition:
the policy reads one additional digit, and each inverse branch maps
each refined source cell bijectively onto a whole cell modulo 243.
Thus any stationary vector of \(K\) lifts to a stationary law of the
actual ternary kernel. This does not assert that the projection of an
ordinary integer path is a finite Markov chain.

The integer verifier proves, in every cell, for the supplied bias \(v\),

\[
 1937/1000<\bar a_i+(Kv)_i-v_i<969/500.
 \tag{12a}
\]

Every stationary vector cancels the bias when (12a) is averaged. Under
UQ(6), its locally uniform lift is the unique actual stationary law, and
its exponent mean therefore satisfies

\[
 1937/1000<A_P<969/500=1.938.
\]

Conditional on that source's stationary uniqueness theorem, D3 gives a
finite robust all-lift credit certificate with

\[
 \rho=39/20=1.95,
 \qquad 20e+W(I_ez)\le39+W(z),\qquad e\le6. \tag{12}
\]

Its residue precision and maximum credit are not supplied here. This is
an existence theorem and a terminating exhaustive search specification,
not a claim that the explicit 354,294-row table in this packet already
achieves a slope below two. That table has slope \(13/6\).

The finite numeric input (12a) is independently reproduced in this
packet. The remaining external assumption is UQ(6), including its
infinite-dimensional analytic dependencies. We did not reconstruct that
entire proof or a formal verification of it.

For inverse-cone compilation, fix \(t\ge1\) and
\(0<c<3^t\) with \(3\nmid c\). With \(t\) odd events, use (12) for the first
\(t-1\) inversions and a final integral action of exponent at most two.
Exactly as in [PROOF.md](PROOF.md), this gives

\[
 k\le\left\lfloor\frac{39t+W(c)+1}{20}\right\rfloor.
 \tag{13}
\]

The \(+1\) pays the terminal cost \(40\), which exceeds the per-event
budget \(39\). Positivity, the common-prefix parity word, and the suffix
bound follow from the same elementary inverse-block argument. This
corollary applies to each ordinary positive tail; it chooses no new lift
of that tail.

## 7. What remains open

Neither the explicit \(13/6\) policy nor the source-qualified \(39/20\)
existence result gives forward descent. These are inverse constructions
and both slopes exceed \(\log_2 3\). More fundamentally, the counting
bound already proved in PR #141 places a universal same-prefix compiler
above approximately \(1.641794\), while uniform numeric contraction of
that same-prefix architecture would require a slope below
\(\log_2 3\approx1.584963\). Improving this compiler alone cannot cross
that barrier.

The useful next finite task is to synthesize a smaller explicit credit
table. The separate pointwise task toward Collatz still needs a mechanism
that reaches a smaller original source or excludes every nonterminating
ordinary orbit. No such mechanism is supplied by (9) or (13).
