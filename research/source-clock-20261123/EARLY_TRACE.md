# Adaptive inverse stopping still pays the original source clock

Date: 2026-11-23.

**Status: SOURCE-QUALIFIED written deduction; the early-trace closing target
remains OPEN.** This note tests whether a height-adapted stopping line can
recover the large canonical trace of an actual escaping root before its
original-source clock. The answer, under the retained positive-spine input,
is quantitative: any such reconstruction carrying a fixed positive fraction
of that trace must put a fixed positive canonical probability within a fixed
distance of the original-source clock. This applies to arbitrary stopping
rules based on the observed legal inverse path, including independently
randomized rules. It does not exclude an escaping orbit.

The deterministic source-clock front is already proved in PR178. The new
statement below treats arbitrary inverse stopping lines and makes explicit
the probability, and change-of-measure cost, of bypassing that front. No
infinite result in this note is claimed as a Lean theorem.

## 1. Exact sources and the attempted closing step

Use the positive odd map and critical operator

\[
 U(n)=\frac{3n+1}{2^{e(n)}},\qquad e(n)=v_2(3n+1),\qquad
 P f(q)=\sum_{\substack{e\ge1\\2^eq\equiv1\ (3)}}
       3\,2^{-e}f((2^eq-1)/3),\qquad D_m=P^m\mathbf1.
 \tag{1}
\]

The retained trace \(F=h_{\rm tr}\) satisfies \(PF=F\), vanishes on
multiples of three, and obeys \(\alpha\le F(q)\le M_0q\) on positive
odd ternary units. Its actual ordinary inverse kernel and terminal-digit
observable are

\[
 K(q,x)=\mathbf1_{Ux=q}\,3\,2^{-e(x)}\frac{F(x)}{F(q)},
 \qquad g(q)=D_1(q)/F(q),\qquad 0\le g\le C_g:=2/\alpha.
 \tag{2}
\]

All paths below consist of positive ordinary odd units. The terminal seed
\(D_1\), rather than \(\mathbf1\), is essential: it kills nonunit
endpoints and gives \(K^m g(q)=D_{m+1}(q)/F(q)\).

| Frozen source | Exact input or comparison |
|---|---|
| PR178, `2169884b64871b448cda16c7d74a0d5914ed870b`, `research/high-variance-20261123/entropy/COARSE_DIGIT_MEMORY_AND_TRACE_FRONT.md`, Sections 1 and 3 | The trace, kernel and positive-spine input in (1)--(3); the already established deterministic bilateral trace profile and pre-source-clock suppression. |
| PR175, `8870528daa6a13cc941d602e578e35c8bfa4bf4f`, `research/lean-global-closure-20261121/machinery/MOVING_CESARO_FIBRES.md`, Sections 2--5 | Moving mean trace at depth \(k+r+1\), contact stopping, and the retained original-source normalization. These results do not supply height-scale onset. |
| PR180, `04572b94c8a58f964ba9b2b1b1bccfe7e9b12ae2`, `research/high-variance-20261123/ENTROPY_RIGIDITY.md`, Section 5 | The open sufficient comparison with stationary ternary density at ordinary height precision. |
| Lyapunov Weaver, [Paper 202 v1](https://rstation.ai/problems/collatz/papers/202/v1), Sections 5--8 | A test against convergent small-gain families; the distinction between generic sibling comparison and the excess-normalized closing question. |

The trace construction and positive-spine input retain their source
qualifications. Assume a hypothetical escaping ordinary ray
\(q_j=U^j(q_0)\) in the supplied component. Put

\[
 a_j=K(q_{j+1},q_j),\qquad d_0=1,\qquad
 d_j=\prod_{i<j}a_i.
\]

The retained conclusions are

\[
 d_j\downarrow d_\infty>0,\qquad
 F(q_j)/q_j\longrightarrow u_\infty>0,\qquad q_j\longrightarrow\infty.
 \tag{3}
\]

The substantive open target remains a bound of the form
\(G(n)\le C D_{\lfloor\log_3 n\rfloor}(n)\) on sufficiently large
actual linear spikes, with the supplied comparison between \(F\) and
\(G\). Stationary ternary nonatomicity would then exclude those spikes.
The question here is whether stopping at a path-dependent depth can provide
the missing early comparison.

## 2. Exact mass of an arbitrary inverse stopping line

Start the actual \(K\)-path at an ordinary unit root \(q\). Let
\(\sigma\) be an almost surely finite stopping time for its natural
filtration, allowing \(\sigma=0\). Its stopped finite words form a
prefix-free set \(\mathcal A_\sigma\). For a word \(w\) with endpoint
\(x_w\), length \(r_w\), and valuation sum \(A_w\), set

\[
 b_w=3^{r_w}2^{-A_w},\qquad
 \mathcal T_\sigma(q)=
       \sum_{w\in\mathcal A_\sigma} b_w D_1(x_w).
 \tag{4}
\]

The empty word has weight one. Telescoping the actual cylinder probability
gives

\[
 \mathsf P_q(w)=b_w\frac{F(x_w)}{F(q)}.
\]

Consequently positivity and countable additivity prove the stopped identity

\[
 \boxed{\frac{\mathcal T_\sigma(q)}{F(q)}
       =\mathbb E_q[g(X_\sigma)].}
 \tag{5}
\]

In particular, the sum is finite and bounded by \(C_gF(q)\). For the
constant stopping time \(\sigma=m\), it is precisely \(D_{m+1}(q)\).
Equation (5) is a terminal-payoff identity, not an application of optional
stopping to a purported martingale \(g(X_r)\). No such martingale premise
is available.

An independently randomized stopping rule is handled by adjoining its
independent random source, applying (4)--(5) conditionally on that source,
and integrating. Equivalently its mass is defined by the right side of (5)
times \(F(q)\). A variable-depth mass in (4) is not asserted to be one
fixed stationary ternary cylinder density.

## 3. The clock-payment theorem

For integers \(0\le L\le k\), let \(R_{k,L}\) be the event that the
path starting at \(q_k\) exactly retraces the literal original orbit to
\(q_L\). This event is defined on the continued path even if the stopping
rule has already stopped. Its probability is exactly

\[
 \mathsf P_{q_k}(R_{k,L})=\prod_{j=L}^{k-1}a_j=d_k/d_L.
 \tag{6}
\]

Define

\[
 \varepsilon_L=\sup_{j\ge L}g(q_j)\longrightarrow0.
 \tag{7}
\]

The convergence follows from (2)--(3). On
\(R_{k,L}\cap\{\sigma\le k-L\}\), the stopped state is a literal
\(q_j\) with \(j\ge L\), so its payoff is at most
\(\varepsilon_L\). On the complement it is at most \(C_g\).
The union bound and (5)--(6) therefore give

\[
 \boxed{\frac{\mathcal T_\sigma(q_k)}{F(q_k)}
 \le\varepsilon_L+C_g\left(
       1-\frac{d_k}{d_L}
       +\mathsf P_{q_k}(\sigma>k-L)\right).}
 \tag{8}
\]

This remains valid for independently randomized rules. It permits the rule
to inspect every exposed valuation, predecessor, residue, height, and prior
state. The event (6) retains one fixed positive ordinary source; no
population estimate is substituted for its probability.

Two consequences make the scope of (8) explicit.

* If \(L_k\to\infty\), \(L_k\le k\), and
  \(\mathsf P_{q_k}(\sigma_k>k-L_k)\to0\), then
  \(\mathcal T_{\sigma_k}(q_k)/F(q_k)\to0\).
* For every \(c>0\), choose a fixed \(L_c\) such that
  \(\varepsilon_{L_c}+C_g(1-d_\infty/d_{L_c})\le c/2\).
  If \(k\ge L_c\) and
  \(\mathcal T_\sigma(q_k)/F(q_k)\ge c\), then

\[
 \boxed{\mathsf P_{q_k}(\sigma>k-L_c)\ge c/(2C_g).}
 \tag{9}
\]

Thus a fixed positive recovered fraction requires a fixed positive
probability of reaching within a fixed distance of the original-source
clock. Mere path adaptation cannot move all of that mass to early depths.

### Ordinary-height precision is strictly earlier than that clock

The actual forward recurrence gives

\[
 q_k+1\le(3/2)^k(q_0+1),\qquad
 \lfloor\log_3 q_k\rfloor
 \le\theta_0k+O_{q_0}(1),\qquad
 \theta_0=\log_3(3/2)<1.
 \tag{10}
\]

For all sufficiently large \(k\), set
\(m_k=\lfloor\log_3q_k\rfloor-1\) and \(L_k=k-m_k\).
Then \(0\le L_k\le k\) and \(L_k\to\infty\). Every stopping
rule satisfying \(\sigma_k\le m_k\) almost surely obeys

\[
 \boxed{\mathcal T_{\sigma_k}(q_k)/F(q_k)\longrightarrow0.}
 \tag{11}
\]

The constant-depth case is already contained in PR178's deterministic
front. The added conclusion is that any adaptive prefix-free choice subject
to the same depth cap also loses the linear spike. This is conditional on
the hypothetical escaping source, not a universal statement that rules out
other proof architectures.

## 4. Quantified cost of changing the path law

Let \(\mathsf P=\mathsf P_{q_k}\), with any independent randomization
included, and put

\[
 B_{k,L}=R_{k,L}^{\,c}\cup\{\sigma>k-L\},\qquad
 \delta_{k,L}=\mathsf P(B_{k,L})
 \le1-d_k/d_L+\mathsf P(\sigma>k-L).
 \tag{12}
\]

Suppose a proposed changed law \(\mathsf Q\ll\mathsf P\) achieves
\(\mathbb E_{\mathsf Q}g(X_\sigma)\ge c>\varepsilon_L\), with
\(\varepsilon_L<C_g\). The same pointwise payoff bound forces

\[
 \mathsf Q(B_{k,L})\ge
 a:=\frac{c-\varepsilon_L}{C_g-\varepsilon_L}>0.
 \tag{13}
\]

Data processing to \(\mathbf1_{B_{k,L}}\), followed by the binary
entropy bound \(h_{\rm b}\le\log2\), gives, for \(\delta_{k,L}>0\),

\[
 \boxed{D_{\rm KL}(\mathsf Q\Vert\mathsf P)
       \ge a\log(1/\delta_{k,L})-\log2.}
 \tag{14}
\]

Indeed, writing \(b=\mathsf Q(B_{k,L})\), the binary divergence is
\(b\log(1/\delta)+(1-b)\log(1/(1-\delta))-h_{\rm b}(b)\).
If \(\delta=0\), the premise (13) is impossible under absolute
continuity. In an early-stopping regime with \(L\to\infty\) and
\(\delta\to0\), any changed law accomplishing the stated order-one
payoff pays divergent relative entropy.

This is a conditional obstruction to a proposed change of measure. It does
not assert that a natural terminal tilt has order-one payoff, nor does it
identify this path-space divergence with an entropy of a compact stationary
process.

## 5. Literature test and the exact remaining step

Paper 202 v1 supplies convergent families with arbitrarily small relative
first-doubling gains and sibling-density ratios tending to zero. Therefore
a uniform sibling Harnack estimate cannot be imported as the missing
ingredient. Its Section 6 also shows that the exhibited polylogarithmic
spikes already have bounded excess over the finite ternary density once the
depth passes their inherited initial run. In particular those examples do
not refute the excess-normalized early-trace target at ordinary height
precision. These manuscript claims retain their own analytic input
qualifications; they are a precise test of the proposed strengthening, not
a proof of a new uniform comparison.

The stopped-trace attempt fails at a specific inference: one would need to
obtain an order-one terminal-digit payoff while stopping substantially
before the original source. Equation (8) shows that such a payoff must come
from the vanishing exceptional path mass, or from paths that reach the
source-clock region with positive probability. Equation (14) quantifies the
first alternative for a changed law. No bound supplied here prevents an
escaping component from having the positive spine in (3), and no early
trace inequality has been established.

The new stopping-line estimates preserve the ordinary root and the actual
clock throughout. They narrow this attempted completion to a genuine new
exceptional-mass estimate; they do not turn the existing moving trace into
a proof of Collatz.
