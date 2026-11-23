# The critical likelihood tilt behind Collatz square pressure

**Status: PROPOSED, complete written proofs; not Lean-formalized.** This note
connects Tao's geometric Syracuse model, the repository's exact square-pressure
operator, and random affine iterations. The connection gives an explicit
change of measure, a sharp exponential transfer threshold, and a singular
stationary measure carried by the divergent Green set. It does not establish
the missing estimate on one fixed positive ordinary orbit.

The primary literature inputs are Tao [T], especially the stationary-process
interpretation after Lemma 1.12, and Diaconis--Freedman [DF], Theorem 1 and
Proposition 1. The results below are proved directly in the normalization used
here. No novelty is claimed for likelihood tilting, random affine series, or
entropy bounds for contracting systems.

## 1. Two laws on exactly the same gap words

For a positive odd integer, use the accelerated map

\[
U(n)=\frac{3n+1}{2^{v_2(3n+1)}}.
\]

For an arbitrary word of positive gaps \(w=(a_1,\ldots,a_r)\), put

\[
A_r=\sum_{i=1}^r a_i,\qquad J_r=\frac{3^r}{2^{A_r}}.
\]

These definitions do not assert that the word belongs to a specified ordinary
source. Let \(\mathbb P\) and \(\mathbb Q\) instead denote the product laws
with one-letter probabilities

\[
p(a)=2^{-a},\qquad q(a)=\frac3{4^a},\qquad a\ge1.
\tag{CT1}
\]

Both sum to one. Their means are respectively \(2\) and \(4/3\).
The first is the geometric law in Tao's Syracuse random variables; the second
will be the exact adjoint law for square pressure.

**CT-A (finite likelihood identity and critical martingale).** On the first
\(r\) gap coordinates,

\[
\boxed{\frac{d\mathbb Q_r}{d\mathbb P_r}(w)=J_r(w).}
\tag{CT2}
\]

Under \(\mathbb P\), \(J_r\) is a nonnegative mean-one martingale, but it is
not uniformly integrable. More precisely,

\[
\begin{array}{ll}
\mathbb P\text{-almost surely:}&
\displaystyle\frac{\log J_r}{r}\longrightarrow\log3-2\log2<0,\\[4pt]
\mathbb Q\text{-almost surely:}&
\displaystyle\frac{\log J_r}{r}\longrightarrow
\delta:=\log3-\frac43\log2>0.
\end{array}
\tag{CT3}
\]

**Proof.** The ratio of the one-letter probabilities is
\(q(a)/p(a)=3/2^a\); multiply over the word. Also
\(\mathbb E_p(3/2^a)=3\sum_{a\ge1}4^{-a}=1\), which proves the martingale
assertion. The strong law of large numbers proves (CT3). Its signs follow
from \(3<4\) and \(3^3>2^4\). Thus \(J_r\to0\) almost surely under
\(\mathbb P\), while its expectations remain one. Uniform integrability
would force convergence in first mean and is therefore impossible. The two
infinite product laws are mutually singular, since their almost-sure gap
averages differ. \(\square\)

All positive real moments of the finite likelihood are explicit:

\[
\mathbb E_{\mathbb P}J_r^s=M(s)^r,
\qquad M(s)=\frac{3^s}{2^{1+s}-1}.
\tag{CT4}
\]

For \(0<s<1\), \(M(s)<1\). Indeed strict concavity of \(x^s\) at
\(2=(1+3)/2\) gives \(2^{1+s}>1+3^s\). The moment loss disappears at
\(s=1\). In the previous packet's notation this is exactly
\(M(s)=\Lambda_{s+1}\), with no asymptotic approximation.

## 2. A quantitative transfer criterion, including its sharp boundary

**CT-B (finite-horizon event transfer).** If \(E_r\) is any event determined
by the first \(r\) gaps and \(s>1\), then

\[
\boxed{\mathbb Q(E_r)\le
M(s)^{r/s}\mathbb P(E_r)^{(s-1)/s}.}
\tag{CT5}
\]

Consequently, a bound \(\mathbb P(E_r)\le C e^{-cr}\) with
\(c>\delta\) implies an exponentially decreasing \(\mathbb Q(E_r)\),
with a suitable fixed choice of \(s>1\). There are events with
\(\mathbb Q(E_r)\to1\) whose \(\mathbb P\)-probabilities have exponential
rate arbitrarily close to \(\delta\). Even the exact upper bound
\(\mathbb P(E_r)\le e^{-\delta r}\) need not force
\(\mathbb Q(E_r)\to0\). Merely knowing that the former probabilities
tend to zero is insufficient.

**Proof.** Apply Holder's inequality to
\(\mathbb Q(E_r)=\mathbb E_{\mathbb P}[J_r\mathbf1_{E_r}]\) and use (CT4).
The resulting exponential exponent is
\((\log M(s)-c(s-1))/s\). Since \(M(1)=1\) and

\[
\left.\frac{d}{ds}\log M(s)\right|_{s=1}
=\log3-\frac43\log2=\delta,
\]

it is negative for some \(s>1\) close to one whenever \(c>\delta\).
For the boundary example, fix \(\varepsilon>0\) and set

\[
E_r=\{\delta-\varepsilon\le r^{-1}\log J_r
\le\delta+\varepsilon\}.
\]

By (CT3), \(\mathbb Q(E_r)\to1\). Reversing (CT2) on this event gives

\[
e^{-(\delta+\varepsilon)r}\mathbb Q(E_r)
\le\mathbb P(E_r)\le
e^{-(\delta-\varepsilon)r}\mathbb Q(E_r).
\]

For the exact endpoint, instead take
\(E_r^*=\{\log J_r\ge\delta r\}=\{A_r\le4r/3\}\).
Equation (CT2) gives \(\mathbb P(E_r^*)\le e^{-\delta r}\).
Under \(\mathbb Q\), each gap has mean \(4/3\) and variance \(4/9\),
so the central limit theorem gives \(\mathbb Q(E_r^*)\to1/2\).
This proves the stated boundary. \(\square\)

This criterion concerns the specified product laws and the same finite event
under both. It is not a claim that an event estimate in Tao's actual
first-passage theorem automatically has this clock, this exponent, or this
source projection. Those identifications must be proved separately.

## 3. What the likelihood identity says at a finite ordinary source scale

For each fixed word \(w\), the odd positive integers having exactly its first
\(r\) accelerated gaps form one residue class modulo \(2^{A_r+1}\). To
see this, write the iterated affine formula as

\[
2^{A_r}U^r(n)=3^r n+B_r,
\quad B_r=\sum_{j=0}^{r-1}3^{r-1-j}2^{A_j},\quad A_0=0.
\]

The final oddness condition is
\(3^r n+B_r\equiv2^{A_r}\pmod{2^{A_r+1}}\), which has a unique solution
because \(3^r\) is odd. Reduction of this congruence at every earlier prefix
gives the corresponding integral odd intermediate value. Thus it imposes
exactly the whole word, including all intermediate valuation guards.

Its probability under normalized Haar measure on the odd 2-adic integers is
\(2^{-A_r}=\mathbb P_r(w)\). Its count among positive sources at most \(X\)
is

\[
\frac{X}{2^{A_r+1}}+O(1),
\tag{CT6}
\]

with absolute counting error at most one before the harmless choice of
endpoint convention. If \(2^{A_r}\) exceeds the ordinary source scale, the
error can be the entire count. A residue cylinder still exists, but most of
its representatives need not lie in the original source interval.

There is an exact bounded stopping version of (CT2). Set
\(\tau_L=\min\{r:A_r>L\}\) for a nonnegative integer \(L\). Since every
gap is at least one, \(\tau_L\le L+1\). Decomposing a stopped event by
\(\tau_L=r\) gives likelihood \(J_{\tau_L}\) between the two stopped laws;
in particular

\[
\mathbb E_{\mathbb P}J_{\tau_L}=1.
\tag{CT7}
\]

This is a usable exact finite identity. Continuing it as a statement about
the future of one fixed positive integer requires information beyond the
finite-cylinder counting approximation. In the repository's terminology,
this is where the exhausted-source core must enter the proof.

## 4. The stationary law of square pressure is singular

Let \(X=\mathbb Z_3^\times\), and let \(\mu\) be additive Haar measure
restricted to \(X\), normalized to total mass one. Define

\[
R_a(u)=\frac{3u+1}{2^a},\quad E_a=R_a(X),\quad
I_a(t)=\frac{2^a t-1}{3}\quad(t\in E_a).
\]

The exact square-pressure operator from the previous packet is

\[
P_2f(t)=\sum_{a\ge1}\frac9{4^a}\mathbf1_{E_a}(t)f(I_a(t)),
\quad F_r=P_2^r1,\quad G=\sum_{r\ge0}F_r.
\tag{CT8}
\]

**CT-C (adjoint, invariant measure, and its Green carrier).** The Markov
adjoint of \(P_2\) is

\[
Q_2\phi(u)=\sum_{a\ge1}\frac3{4^a}\phi(R_a(u)).
\tag{CT9}
\]

It has a unique invariant probability \(\nu_2\). Starting from \(\mu\),
the \(r\)-step law has density \(F_r\), and these laws converge weakly to
\(\nu_2\). Moreover,

\[
\begin{split}
&G<\infty\quad\mu\text{-almost everywhere},\\
&\liminf_{r\to\infty}\frac{\log F_r(\zeta)}r
\ge2\delta>0\quad\nu_2\text{-almost everywhere}.
\end{split}
\tag{CT10}
\]

In particular \(\nu_2\perp\mu\), and \(\nu_2\{G=\infty\}=1\). It has
a full-measure carrier of Hausdorff dimension at most

\[
\boxed{\frac{H(q)}{\log3}
=\frac{8\log2}{3\log3}-1<1,\qquad
H(q)=\frac83\log2-\log3.}
\tag{CT11}
\]

**Proof.** Each \(R_a\) scales additive Haar measure by \(1/3\). Changing
variables in each nonnegative term gives

\[
\int_X(P_2f)\phi\,d\mu=\int_X f(Q_2\phi)\,d\mu,
\]

first for nonnegative functions and then for integrable bounded pairings.
This proves (CT9) and the density assertion by iteration.

Every \(R_a\) contracts 3-adic distance by exactly \(1/3\). For every
infinite gap sequence the backward composition has a limit

\[
\pi(a_1,a_2,\ldots)
=\sum_{j\ge1}\frac{3^{j-1}}{2^{A_j}}\in X.
\tag{CT12}
\]

The tail after any finite prefix is a unit. The law \(\pi_*\mathbb Q\)
is invariant by separating the first term of the composition. Coupling two
copies with the same gaps bounds their distance after \(r\) maps by
\(3^{-r}\) times their initial distance. On this compact space it proves
uniqueness and weak convergence from any initial law, and identifies the
invariant measure as \(\nu_2=\pi_*\mathbb Q\).

For a prefix \(w\) of length \(r\), write
\(R_w=R_{a_1}\circ\cdots\circ R_{a_r}\), \(E_w=R_w(X)\).
The whole inverse word is legal on \(E_w\), its Haar measure is \(3^{-r}\),
and the pressure expansion is

\[
F_r(\zeta)=\sum_{w\in\mathbb N_{>0}^r}
\frac{9^r}{4^{A_r(w)}}\mathbf1_{E_w}(\zeta).
\tag{CT13}
\]

For \(1/2<\eta<1\), subadditivity of the power \(\eta\) gives

\[
\int F_r^\eta\,d\mu\le
\left(\frac{3^{2\eta-1}}{2^{2\eta}-1}\right)^r,
\qquad
\int G^\eta\,d\mu\le
\frac1{1-3^{2\eta-1}/(2^{2\eta}-1)}<\infty.
\tag{CT14}
\]

These are the previous packet's GF1 estimates, reproduced here to specify
the dependence. They prove the first line of (CT10). They also imply
\(F_r\to0\) \(\mu\)-almost everywhere by summing the Markov bounds.

For \(\mathbb Q\)-almost every sequence, \(A_r/r\to4/3\). Its own prefix
is one of the legal words contributing at \(\pi(a)\), because the remaining
tail in (CT12) lies in \(X\). Keeping just that one term in (CT13) gives

\[
F_r(\pi(a))\ge\frac{9^r}{4^{A_r}},
\quad
\liminf\frac{\log F_r(\pi(a))}{r}
\ge2\log3-\frac83\log2=2\delta.
\]

This proves the second line of (CT10) and singularity, without inferring
singularity merely from convergence of densities to zero.

For completeness, the dimension estimate needs only the same word law.
The strong law gives
\(-r^{-1}\log q(w)=r^{-1}(A_r\log4-r\log3)\to H(q)\).
For any \(\varepsilon>0\), the prefixes with
\(q(w)\ge e^{-r(H(q)+\varepsilon)}\) number at most
\(e^{r(H(q)+\varepsilon)}\). Their images lie in balls of radius \(3^{-r}\).
Almost every coding eventually uses only these prefixes. For any
\(d>(H(q)+\varepsilon)/\log3\), the total \(d\)-power of the diameters
of this cover tends to zero. Taking a countable union over the first time
the condition holds, then letting \(\varepsilon\downarrow0\), proves
(CT11). \(\square\)

There is an additional exact ordinary boundary here. For every positive odd
integer \(t\) with \(3\nmid t\), each legal inverse word in (CT13) is an
actual positive ordinary predecessor history. Hence the previous packet's
fixed-endpoint summability gives

\[
G(t)=G_2(t)<\infty
\quad\text{for every such }t.
\tag{CT15}
\]

See [GLOBAL_MASS.md, G10](../reframe-20261121/GLOBAL_MASS.md) and
[GREEN_FRACTIONAL_MOMENTS.md, F10](../reframe-20261121/GREEN_FRACTIONAL_MOMENTS.md)
for that independent ordinary estimate and its exact source pin. The
finiteness also extends to an even positive unit \(t=2^b u\), where
\(u\) is odd: replacing the first inverse exponent \(a\) by \(a+b\)
in (CT8) gives \(F_r(t)\le4^bF_r(u)\) for every \(r\ge1\), and hence
\(G(t)\le1+4^b(G(u)-1)<\infty\). Thus the full-measure carrier in (CT10)
excludes every positive ordinary unit, not just a Haar-typical selection
of them. This explains why replacing the
ordinary counting norm by this stationary probability requires a new
arithmetic transfer theorem: ordinary point masses disappear in that space.

## 5. The same critical exponent in a real random affine series

Formula (CT12) also has a real interpretation under \(\mathbb P\). Let

\[
S=\sum_{j\ge1}\frac{3^{j-1}}{2^{A_j}}
=\frac13\sum_{j\ge1}J_j.
\]

**CT-D (exact moment threshold for the real perpetuity).** Under
\(\mathbb P\), \(S\) is finite and positive almost surely, is the unique
stationary law on \([0,\infty)\) for the random maps \(R_a\) with probabilities
\(p(a)\), and satisfies

\[
\mathbb E S^\theta<\infty\quad\Longleftrightarrow\quad0<\theta<1
\qquad(\theta>0).
\tag{CT16}
\]

For \(0<\theta<1\), one explicit bound is

\[
\mathbb E S^\theta\le
3^{-\theta}\frac{M(\theta)}{1-M(\theta)}.
\tag{CT17}
\]

**Proof.** The negative almost-sure drift in (CT3) makes the positive series
converge exponentially in the real metric. Splitting off its first letter
gives the distributional identity
\(S\overset d=(3S'+1)/2^a\), with \(S'\) independent of \(a\) and having
the same law as \(S\). For uniqueness, the Lipschitz constants are
\(3/2^a\), their mean is one, their mean logarithm is \(\log(3/4)<0\),
and \(\mathbb E|R_a(0)|=1/3\). These check all the hypotheses of [DF,
Theorem 1]. Alternatively the coupled backward compositions directly give
its contraction argument here. Subadditivity and (CT4) prove (CT17).
Tonelli gives \(\mathbb ES=\frac13\sum_{j\ge1}\mathbb EJ_j=\infty\).
Since \(x\le1+x^\theta\) for \(\theta\ge1\), all larger moments are
infinite too. \(\square\)

Under \(\mathbb Q\) the same positive real series diverges, because its
terms \(J_j/3\) grow exponentially. Its 3-adic series still converges and
has law \(\nu_2\). This supplies an explicit two-completion example; it
does not identify the two limits as one rational number. Nor does it
identify reversed random compositions with the successive ordinary values
of a deterministic Collatz orbit. In the random setting their finite-time
distributions agree by independence; a fixed ordinary gap sequence has no
such exchangeability assumption.

## 6. The completion step this isolates

The useful affirmative connection is exact: the square-pressure law is
the derivative tilt of the geometric law, its drift has the opposite sign,
and its stationary ternary mass lies on a quantified singular Green carrier.
This determines the law and function space that a pressure-based use of
the literature must address.

There are now two concrete analytic interfaces to a global proof:

1. **Ordinary survivor renewal.** Prove a source-preserving estimate for the
   actual set whose entire future stays above a floor, with a uniform rate
   strong enough for the basin-amplification criterion in
   [ORDINARY_RENEWAL.md](ORDINARY_RENEWAL.md). That criterion also states
   its separate predecessor-density premise and the remaining cycle issue.
2. **Arithmetic pressure control after source exhaustion.** Bound the
   derivative-weighted actual histories after \(\tau_L\), while retaining
   their original positive source. Equations (CT2), (CT5), and (CT7) give
   exact finite input identities; neither Haar-nullness nor the stationary
   singular measure supplies this missing ordinary bound.

The previous Green route's eventual ordinary column inequality also remains
open. The present theorem neither assumes that inequality nor treats its
compact almost-everywhere failure as an ordinary counterexample. No infinite
ordinary orbit is excluded solely by this note, and no cycle is declared
impossible by the random affine calculation.

## Primary references and provenance

- **[T]** Terence Tao, *Almost all orbits of the Collatz map attain almost
  bounded values*, Forum of Mathematics, Pi **10** (2022), e12. The geometric
  Syracuse laws, Lemma 1.12 and its following stationary-process
  interpretation, and the first-passage transport estimates are in the
  [publisher's full text](https://www.cambridge.org/core/journals/forum-of-mathematics-pi/article/almost-all-orbits-of-the-collatz-map-attain-almost-bounded-values/1008CC2DF91AF87F66D190C5E01C907F).
  [Author's arXiv record](https://arxiv.org/abs/1909.03562).
- **[DF]** Persi Diaconis and David Freedman, *Iterated random functions*,
  SIAM Review **41** (1999), 45--76. Theorem 1 and Proposition 1 are on page 3
  of the [author-hosted preprint](https://www.stat.berkeley.edu/~census/511.pdf).
  [Publisher DOI](https://doi.org/10.1137/S0036144598338446).
- **[R]** This branch's previous paper packet at
  `75f2f9aad4d3f80aaa1f8718e229faa04ee5770e`, especially GF1--GF2 in
  `research/reframe-20261121/GREEN_FRACTIONAL_MOMENTS.md` and G10 in
  `research/reframe-20261121/GLOBAL_MASS.md`. Its 25 Lean statements have
  their own execution receipt; the analytic theorems used here are written
  proofs, not part of that Lean receipt.
