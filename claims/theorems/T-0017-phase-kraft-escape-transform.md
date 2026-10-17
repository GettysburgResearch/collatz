# T-0017 — Phase–Kraft martingale and the escape transform

Claim ID: `T-0017`  
Title: Absorption of the fair rounded phase, finite graph rigidity, and a positive-drift Doob escape transform  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: `L-0013`, `T-0013`, `T-0016`  
Scope: fair physical-parity phase dynamics, complete prefix codes, and exceptional escape measures  
Related counterexample candidates: none

## Statement

Use the rounded phase maps from `L-0013`:

\[
S_0(v)=\left\lceil\frac v2\right\rceil,
\qquad
S_1(v)=\left\lfloor\frac{3v}{2}\right\rfloor.
\tag{1}
\]

For a finite binary word \(w\), write \(S_w(v)\) for the phase reached by reading \(w\) chronologically.

### 1. Fair phase martingale and almost-sure absorption

Let \(E_0,E_1,\ldots\) be independent fair bits and define

\[
V_{t+1}=S_{E_t}(V_t),
\qquad
V_0=v\ge1.
\tag{2}
\]

Then \((V_t)\) is a nonnegative martingale:

\[
\boxed{
\mathbb E[V_{t+1}\mid V_t]=V_t.
}
\tag{3}
\]

Moreover,

\[
\boxed{
V_t=1
\quad\text{for all sufficiently large }t
}
\tag{4}
\]

with probability one.

Thus the fair physical-parity phase process is absorbed at the negative fixed phase \(-1\) almost surely.

### 2. Exact phase–Kraft identities

Let \(\mathcal W\) be a finite complete binary prefix code. Then, for every \(v\ge1\),

\[
\boxed{
\sum_{w\in\mathcal W}
2^{-|w|}S_w(v)=v,
}
\tag{5}
\]

and, equivalently,

\[
\boxed{
\sum_{w\in\mathcal W}
2^{-|w|}\bigl(S_w(v)-1\bigr)=v-1.
}
\tag{6}
\]

For an incomplete finite prefix-free family, the left side of (6) is at most \(v-1\).

In particular, for \(H>1\),

\[
\boxed{
\sum_{\substack{w\in\mathcal W\\S_w(v)\ge H}}
2^{-|w|}
\le
\frac{v-1}{H-1}.
}
\tag{7}
\]

High-phase endpoints necessarily occupy small fair cylinder mass.

### 3. Rigidity of finite complete phase graphs

Let \(G\) be a finite directed graph whose vertex \(i\) carries a phase magnitude \(v_i\). Suppose the outgoing edges at each vertex are labeled by a finite complete physical-parity prefix code, and an edge \(e:i\to j\) labeled by \(w_e\) satisfies

\[
S_{w_e}(v_i)=v_j.
\tag{8}
\]

Put

\[
P(i,j)
=
\sum_{e:i\to j}2^{-|w_e|}.
\tag{9}
\]

Then \(P\) is row-stochastic and

\[
\boxed{
P(v_i-1)_{i\in V}=(v_i-1)_{i\in V}.
}
\tag{10}
\]

Every recurrent communicating class of this finite complete graph consists only of vertices with phase magnitude \(1\).

Consequently a nontrivial finite multi-phase grammar cannot be both:

1. complete under fair physical parity; and
2. recurrent away from the phase \(-1\).

A counterexample grammar must again be incomplete and exceptional, infinite-state, or equipped with an unbounded stack/counter.

### 4. Exact Doob escape transform

Put

\[
h(v)=v-1.
\]

For \(v>1\), define transition probabilities

\[
\boxed{
\mathbb Q_v(e)
=
\frac{h(S_e(v))}{2h(v)},
\qquad e\in\{0,1\}.
}
\tag{11}
\]

They are nonnegative and sum to one. A transition to phase \(1\) has probability zero.

For every finite word \(w\) of length \(L\),

\[
\boxed{
\mathbb Q_v([w])
=
2^{-L}\frac{S_w(v)-1}{v-1}.
}
\tag{12}
\]

Thus the escape process is the exact endpoint-size-biased transform of fair physical parity.

For a finite phase graph avoiding phase \(1\), its transformed edge matrix is

\[
\mathcal H(i,j)
=
\sum_{e:i\to j}
2^{-|w_e|}
\frac{v_j-1}{v_i-1}.
\tag{13}
\]

It is diagonally similar to the fair cylinder matrix:

\[
\mathcal H
=
D_h^{-1}PD_h,
\qquad
D_h=\operatorname{diag}(v_i-1).
\tag{14}
\]

### 5. Survival conditioning automatically creates positive Collatz drift

Under \(\mathbb Q\), the conditional probability of a physically odd step is

\[
\boxed{
\mathbb Q_v(E_t=1)
=
\begin{cases}
3/4,&v\text{ odd},\\[1mm]
3/4+\dfrac1{4(v-1)},&v\text{ even}.
\end{cases}
}
\tag{15}
\]

Hence

\[
\mathbb Q_v(E_t=1)\ge\frac34.
\tag{16}
\]

Let

\[
\gamma=\frac34\log3-\log2>0
\tag{17}
\]

and

\[
\delta
=
\frac34\log\left(\frac43\right)
+
\frac14\log\left(\frac12\right)
>0.
\tag{18}
\]

Then the one-step physical multiplier and phase growth satisfy

\[
\boxed{
\mathbb E_{\mathbb Q}
\left[
\log\left(\frac{3^{E_t}}2\right)
\middle|V_t
\right]
\ge\gamma,
}
\tag{19}
\]

and

\[
\boxed{
\mathbb E_{\mathbb Q}
\left[
\log\left(\frac{V_{t+1}}{V_t}\right)
\middle|V_t
\right]
\ge\delta.
}
\tag{20}
\]

Since both logarithmic increments are bounded, the martingale-difference strong law gives

\[
\boxed{
\liminf_{n\to\infty}
\frac1n
\sum_{t=0}^{n-1}
\log\left(\frac{3^{E_t}}2\right)
\ge\gamma
}
\tag{21}
\]

and

\[
\boxed{
\liminf_{n\to\infty}
\frac1n\log\left(\frac{V_n}{V_0}\right)
\ge\delta
}
\tag{22}
\]

for \(\mathbb Q\)-almost every path.

Therefore conditioning the phase not to collapse to \(-1\) does not merely preserve a rare symbolic path. It produces a measure under which:

- the phase escapes exponentially; and
- the formal Collatz multiplier has uniformly positive logarithmic drift.

### 6. Three exact measures on one parity language

For a finite physical parity word \(w\), let

\[
\lambda(w)=\frac{3^{a(w)}}{2^{|w|}}.
\]

On any complete prefix code, the following are three probability weights:

\[
\mu_{\mathrm{fair}}(w)=2^{-|w|},
\tag{23}
\]

\[
\mu_{\mathrm{growth}}(w)
=
2^{-|w|}\lambda(w),
\tag{24}
\]

\[
\mu_{\mathrm{escape}}(w)
=
2^{-|w|}
\frac{S_w(v)-1}{v-1}.
\tag{25}
\]

Their likelihood ratios relative to fair parity are respectively:

\[
\lambda(w)
\quad\text{and}\quad
\frac{S_w(v)-1}{v-1}.
\tag{26}
\]

`T-0016` identifies the first tilt with Bernoulli odd probability \(3/4\). The present theorem identifies the second with survival of the moving negative phase. At odd phases the two one-step tilts coincide exactly; at even phase \(v\) their physically odd probabilities differ by only

\[
\frac1{4(v-1)}.
\tag{27}
\]

This is the precise bridge between negative-phase escape and positive Collatz pressure.

## Proof

### Harmonicity and absorption

By `L-0013`,

\[
S_0(v)+S_1(v)=2v.
\]

Therefore

\[
\mathbb E[V_{t+1}\mid V_t=v]
=
\frac{S_0(v)+S_1(v)}2
=v,
\]

proving (3). The process is a nonnegative martingale, so it converges almost surely to a finite limit.

An integer-valued convergent sequence is eventually constant. For every \(v>1\),

\[
S_0(v)\ne v
\quad\text{and}\quad
S_1(v)\ne v.
\]

The only phase at which both branches remain fixed is \(v=1\). Hence the almost-sure limit is \(1\), and absorption occurs in finite time almost surely.

### Phase–Kraft identities

Start with the root contribution \(v\). Replacing any prefix \(w\) by its two children replaces

\[
2^{-|w|}S_w(v)
\]

by

\[
2^{-|w|-1}
\left(
S_0(S_w(v))+S_1(S_w(v))
\right)
=
2^{-|w|}S_w(v).
\]

Expanding the finite prefix tree to its complete leaves proves (5). Combining it with the ordinary Kraft equality proves (6).

For an incomplete family, complete the finite tree by adding missing leaves. Every omitted term \(S_w(v)-1\) is nonnegative, giving the inequality. Equation (7) follows immediately from (6).

### Finite graph rigidity

Equation (6), applied to the outgoing code at vertex \(i\), gives

\[
\sum_jP(i,j)(v_j-1)=v_i-1.
\]

Thus (10) holds. On a finite recurrent communicating class, every harmonic function is constant by the maximum principle.

Suppose such a closed class had constant phase \(c>1\). Concatenating independently fair outgoing codewords produces an ordinary fair infinite physical-parity sequence, while all code-boundary phases remain in that class. Since phase \(1\) is absorbing, the phase could never hit \(1\). This contradicts part 1, which says the fair phase process hits \(1\) almost surely. Therefore every recurrent class has \(c=1\).

### Escape transform

Since \(h(S_0(v))+h(S_1(v))=2h(v)\), equation (11) defines probabilities. Multiplying one-step factors along a word telescopes:

\[
\prod_{t=0}^{L-1}
\frac{h(V_{t+1})}{2h(V_t)}
=
2^{-L}\frac{h(V_L)}{h(V_0)},
\]

which is (12). Equation (14) is immediate.

### Drift calculations

If \(v\) is odd, then

\[
S_0(v)-1=\frac{v-1}{2},
\qquad
S_1(v)-1=\frac{3(v-1)}2,
\]

so the escape probabilities are \(1/4\) and \(3/4\).

If \(v\) is even, then

\[
S_0(v)-1=\frac{v-2}{2},
\qquad
S_1(v)-1=\frac{3v-2}{2},
\]

giving (15).

Equation (19) follows because the physically odd probability is at least \(3/4\).

For even \(v\), the phase ratios are exactly \(1/2\) and \(3/2\), and the odd-branch probability is at least \(3/4\). For odd \(v\ge3\),

\[
\frac{S_0(v)}v\ge\frac12,
\qquad
\frac{S_1(v)}v\ge\frac43,
\]

with probabilities \(1/4\) and \(3/4\). These bounds give (20).

Subtracting the conditional expectations from the bounded logarithmic increments produces bounded martingale differences. Their averages converge almost surely to zero, proving (21)--(22). ∎

## Strategic consequence

The project now has an exact probabilistic description of the exceptional language it is trying to make arithmetically concrete:

> The fair phase process collapses to \(-1\), but its Doob escape transform has positive phase and Collatz drift and is asymptotically aligned with the \(3/4\)-odd growth tilt.

This suggests a targeted construction program:

1. approximate the escape transform by a finite-state or pushdown renewal grammar;
2. preserve positive cycle pressure;
3. then solve the separate ordinary-boundary problem by exhibiting one finite quotient accepted forever.

The correct search distribution is not fair parity and not an arbitrary collection of large multipliers. It is the phase-survival size bias (12).

## Gap audit

- The escape transform is a probability measure on infinite symbolic parity paths. It does not prove that a typical escape path is the trajectory of an ordinary positive integer.
- Almost-sure positive multiplier under \(\mathbb Q\) is not an ordinary Collatz counterexample.
- Finite graph rigidity applies to complete fair codes. An incomplete exceptional subgrammar may evade it.
- The theorem does not yet construct the finite quotient required by `Q-0001`.

## Adversarial tests

`X-0009` verifies:

- the rounded phase formulas on 500,000 exact pairs;
- phase–Kraft identities on several nonuniform complete prefix codes;
- the exact escape probabilities through phase \(10{,}000\);
- the path-density formula on every word through depth 12 from phase 136;
- the positive physical and phase logarithmic drift bounds;
- exact finite-depth fair absorption data while the harmonic first moment remains \(135\).

## Suggested next attack

Construct finite subgraphs that approximate the escape probabilities while retaining exact negative-template return words. Rank them simultaneously by:

- fair cylinder pressure;
- Collatz tilted pressure;
- phase-escape likelihood;
- graph-cycle multiplier;
- and existence of an ordinary finite boundary.

The first concrete target is a pushdown approximation to the phase-136 escape process using the cycle-padding towers of `T-0015`.
