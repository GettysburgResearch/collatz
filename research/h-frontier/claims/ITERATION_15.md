# Iteration 15: Tao transfer, side-branch sparsity, and the sharp record-bank theorem

All theorem-level claims remain `PROPOSED` pending independent reconstruction.
Claims importing Tao's theorem are marked `PROPOSED / SOURCE-DEPENDENT`.
This iteration introduces no bounded search and no new symbolic architecture.
It attacks only the surviving all-time coefficient-supercritical lane.

## Frozen repository synchronization

This pass was synchronized against the following current heads:

```text
PR #77  agent/gpt56-positive-review-01/75-verify-supercritical
        1c8ed3c7edbb190d59490d2f92a3c342c2f856eb

PR #80  agent/gpt56-positive-02/least-counterexample-global
        fbc178758314d5e908f28aedf7b356938935b256

PR #81  agent/gpt56-positive-entropy-01/75-supercritical-entropy
        5609d8b76f8b0b1e2b9a3b3e9e1122b67732e648

PR #83  agent/gpt56-positive-tangent-01/75-coefficient-envelope
        674f36cb6f2bb620e6fab21da2838c7c52a5072d
```

The relevant imported repository facts are:

1. PR #77's exact affine identity and the proposed theorem that an all-time
   coefficient-supercritical ordinary orbit tends to `+infinity`.
2. PR #80's correction product, inverse-surplus identity, fixed-band
   `O(K^(1/9))` bound, `8/9` mean/record surplus theorem, critical-density
   cusp, and tail-minimum ladder.
3. PR #81's exact repeated-factor dyadic separation and the `SC* / FC*`
   decomposition.
4. PR #83's universal first-crossing shifted-denominator equation and
   polynomial sparsity of the delayed-crossing language.

The new claims below concern Lane A.  They neither promote nor modify the
Lane-B claims of PRs #81 and #83.

---

## 1. Tao import: exact statement and admissibility audit

Let the unshortened Collatz map be

\[
 \operatorname{Col}(N)=
 \begin{cases}
 3N+1,&N\text{ odd},\\
 N/2,&N\text{ even}.
 \end{cases}
\tag{1}
\]

Write

\[
 \operatorname{Col}_{\min}(N)
 =\min_{j\ge0}\operatorname{Col}^{j}(N).
\tag{2}
\]

Tao's Theorem 1.3 states:

> For every function `f : Z_(>0) -> R` with `f(N) -> +infinity`, one has
> `Col_min(N) < f(N)` for all `N` outside a set of logarithmic density zero.

No monotonicity, effectiveness, or architecture-independence hypothesis is
placed on `f`.  In particular, after a hypothetical orbit has been fixed for a
contradiction argument, `f` may be defined from that orbit.  The theorem is
uniform in the logical sense

\[
 \forall f\ (f(N)\to\infty\Longrightarrow\text{the exceptional set is log-null}).
\tag{3}
\]

Tao also records that the shortcut map

\[
 T(N)=
 \begin{cases}
 N/2,&N\text{ even},\\
 (3N+1)/2,&N\text{ odd}
 \end{cases}
\tag{4}
\]

has the same orbit minimum as the unshortened map.  Indeed the only omitted
state after an odd shortcut step is `3N+1`, which is larger than both `N` and
`(3N+1)/2`.

The source was rechecked at the current arXiv/published statement.  The theorem
uses strict `< f(N)` and logarithmic density; the half-minimum constructions
below therefore have the correct strict orientation.

---

## L-9533: Tao transport principle for a moving exceptional family

**Claim ID:** `L-9533`  
**Title:** Any unbounded family whose complete Collatz minima tend to infinity is logarithmically null  
**Status:** `PROPOSED / SOURCE-DEPENDENT`  
**Dependency:** Tao, Theorem 1.3  
**Scope:** arbitrary subsets of positive ordinary integers

Let `B` be an unbounded subset of the positive integers.  Assume

\[
 \operatorname{Col}_{\min}(b)\longrightarrow+\infty
 \qquad(b\to\infty,\ b\in B).
\tag{5}
\]

Then `B` has logarithmic density zero:

\[
\boxed{
 \sum_{\substack{b\le X\\b\in B}}\frac1b=o(\log X).
}
\tag{6}
\]

### Proof

For positive integers `N`, define

\[
 f_B(N)
 =\frac12\min\left\{
 \operatorname{Col}_{\min}(b):b\in B,\ b\ge N
 \right\}.
\tag{7}
\]

The set inside the minimum is nonempty because `B` is unbounded.  Hypothesis
(5) implies `f_B(N)->infinity`.  For every `b in B`,

\[
 f_B(b)\le\frac12\operatorname{Col}_{\min}(b)
 <\operatorname{Col}_{\min}(b).
\tag{8}
\]

Thus `B` is contained in Tao's exceptional set for `f_B`, and (6) follows.
QED.

### Logical point

The function is orbit- or family-dependent, but this is legitimate: Tao's
quantifier is over every fixed function tending to infinity.  The argument does
not choose `f` after sampling a random integer; it fixes the hypothetical
family first and then applies the theorem.

---

## 2. Shortcut setup and correction product

Let

\[
 x_k=T^k(n),\qquad
 v_k=x_k\bmod2,\qquad
 q_k=\sum_{i=0}^{k-1}v_i,
\tag{9}
\]

and put

\[
 \alpha=\frac{\log2}{\log3},
 \qquad
 D_k=q_k-\alpha k.
\tag{10}
\]

The all-time coefficient-supercritical condition is

\[
 D_k\ge0\qquad(k\ge0).
\tag{11}
\]

PR #77 proves, subject to its current status, that (11) forces

\[
 x_k\longrightarrow+\infty.
\tag{12}
\]

The exact product identity is

\[
\boxed{
 \frac{x_k}{n}=3^{D_k}P_k,
 \qquad
 P_k=
 \prod_{\substack{0\le i<k\\v_i=1}}
 \left(1+\frac1{3x_i}\right).
}
\tag{13}
\]

On a nonperiodic Lane-A orbit all states are distinct.

For each odd source time `i`, define its omitted unshortened side branch

\[
 b_i=3x_i+1=2x_{i+1}.
\tag{14}
\]

Let

\[
 \mu_k=\min_{j\ge k}x_j.
\tag{15}
\]

Under (12), `mu_k->infinity`.

---

## L-9534: side branches are Tao-null and measure the correction product

**Claim ID:** `L-9534`  
**Title:** The omitted odd side branches form a logarithmically null family whose harmonic mass is equivalent to the affine correction  
**Status:** `PROPOSED / SOURCE-DEPENDENT`  
**Dependencies:** `L-9533`, (12), the exact product (13)  
**Scope:** positive ordinary divergent shortcut orbits

Let

\[
 \mathcal B=\{b_i:v_i=1\}.
\tag{16}
\]

Then:

\[
\boxed{
 \sum_{\substack{b\le X\\b\in\mathcal B}}\frac1b=o(\log X).
}
\tag{17}
\]

Moreover, for every `k`,

\[
\boxed{
 \sum_{\substack{0\le i<k\\v_i=1}}\frac1{b_i}
 \le\log P_k
 \le\frac43
 \sum_{\substack{0\le i<k\\v_i=1}}\frac1{b_i}.
}
\tag{18}
\]

### Proof of logarithmic sparsity

The `b_i` are distinct because the corresponding odd sources `x_i` are
distinct.  Starting from `b_i`, one even unshortened step reaches

\[
 b_i/2=x_{i+1}.
\]

The full orbit minimum is therefore

\[
 \operatorname{Col}_{\min}(b_i)=\mu_{i+1}.
\tag{19}
\]

As `i->infinity` through odd source times, both `b_i` and `mu_(i+1)` tend to
infinity.  Apply `L-9533` to obtain (17).

### Proof of the comparison

Put `t=1/(3x_i)`.  Since `x_i>=1`, one has `0<t<=1/3`, and

\[
 \frac1{b_i}=\frac{t}{1+t}.
\tag{20}
\]

The elementary inequalities

\[
 \frac{t}{1+t}\le\log(1+t)\le t
 \le\frac43\frac{t}{1+t}
\tag{21}
\]

prove (18) after summation.  QED.

### Interpretation

The real affine correction is not merely bounded by a generic harmonic sum.
It is, up to the fixed factor `4/3`, the logarithmic harmonic mass of an
explicit ordinary family that Tao forces to be logarithmically sparse.

---

## T-9524: correction products are negligible at physical records

**Claim ID:** `T-9524`  
**Title:** At every late physical record, essentially all logarithmic height is carried by coefficient surplus  
**Status:** `PROPOSED / SOURCE-DEPENDENT`  
**Dependencies:** `L-9534`, exact identity (13)  
**Scope:** positive ordinary Lane-A orbits

Let `r` range through physical record times:

\[
 x_r=\max_{0\le i\le r}x_i.
\tag{22}
\]

Then

\[
\boxed{
 \log P_r=o(\log x_r),
 \qquad
 P_r=x_r^{o(1)}.
}
\tag{23}
\]

Consequently

\[
\boxed{
 D_r=(1-o(1))\log_3 x_r.
}
\tag{24}
\]

If

\[
 M_K=\max_{0\le k\le K}D_k,
 \qquad
 X_K=\max_{0\le k\le K}x_k,
\tag{25}
\]

then

\[
\boxed{
 M_K\ge(1-o(1))\log_3X_K
 \ge(1-o(1))\log_3K.
}
\tag{26}
\]

Equivalently,

\[
\boxed{
 \max_{k\le K}3^{D_k}\ge K^{1-o(1)}.
}
\tag{27}
\]

This sharpens PR #80's elementary record exponent `8/9` to the asymptotically
optimal coefficient `1`, at the cost of importing Tao.

### Proof

At a record time `r`, every earlier side branch satisfies

\[
 b_i=3x_i+1\le3x_r+1.
\]

Equations (17)--(18) give

\[
 \log P_r
 \le\frac43
 \sum_{\substack{b\le3x_r+1\\b\in\mathcal B}}\frac1b
 =o(\log x_r),
\]

which proves (23).  Taking logarithms in (13),

\[
 \log x_r=\log n+D_r\log3+\log P_r,
\]

and (24) follows.

For arbitrary `K`, choose a record time `r<=K` with `x_r=X_K`.  The states
`x_0,...,x_K` are distinct positive integers, so

\[
 X_K\ge K+1.
\tag{28}
\]

Then `M_K>=D_r`, and (26)--(27) follow.  QED.

### Fixed-band refinement at records

PR #80 proves the exact identity

\[
 P_K=1+\frac1{3n}
 \sum_{\substack{0\le i<K\\v_i=1}}3^{-D_i}.
\tag{29}
\]

At record times, (23) implies that for every fixed `H`,

\[
\boxed{
 \#\{i<r:v_i=1,\ D_i\le H\}=x_r^{o(1)}.
}
\tag{30}
\]

Charging intervening even runs as in PR #80 gives

\[
\boxed{
 \#\{i<r:D_i\le H\}=x_r^{o(1)}.
}
\tag{31}
\]

If the physical records obey a polynomial envelope `x_r<=r^A`, then every
fixed surplus band is visited only `r^{o(1)}` times through record time `r`.

---

## 3. Exact saturation of the raw 2-adic parity approximants

For the length-`k` parity prefix, write

\[
 2^kx_k=3^{q_k}n+A_k
\tag{32}
\]

and define the reduced parity-ghost truncation

\[
 \rho_k=-\frac{A_k}{3^{q_k}}.
\tag{33}
\]

After the first odd step, `3` does not divide `A_k`: the final odd contribution
is a power of two and all earlier odd contributions are divisible by three.
Thus the denominator in (33) is exactly `3^(q_k)`.

Put

\[
 e_k=v_2(x_k).
\tag{34}
\]

The next `e_k` shortcut steps are even, so

\[
 D_{k+e_k}=D_k-\alpha e_k.
\tag{35}
\]

---

## L-9535: exact product-formula deficiency identity

**Claim ID:** `L-9535`  
**Title:** Every raw parity approximant lies strictly below exponent one by exactly the post-even-run surplus  
**Status:** `PROPOSED`  
**Dependencies:** elementary affine identity and all-time supercriticality  
**Scope:** Lane-A ordinary or symbolic paths

For every `k>=1`,

\[
\boxed{
 v_2(n-\rho_k)=k+e_k.
}
\tag{36}
\]

All-time supercriticality gives

\[
 e_k\le\frac{D_k}{\alpha}.
\tag{37}
\]

More precisely,

\[
\boxed{
 q_k\log_2 3-(k+e_k)
 =\frac{D_{k+e_k}}{\alpha}>0.
}
\tag{38}
\]

Equivalently,

\[
\boxed{
 \frac{v_2(n-\rho_k)}{\log_2(3^{q_k})}
 =1-\frac{D_{k+e_k}}{q_k}<1.
}
\tag{39}
\]

Since `H(rho_k)>=3^(q_k)`, one also has

\[
\boxed{
 v_2(n-\rho_k)<\log_2H(\rho_k).
}
\tag{40}
\]

### Proof

Equation (32) gives

\[
 n-\rho_k=\frac{2^kx_k}{3^{q_k}},
\]

which proves (36).  Because the next `e_k` steps are even and every prefix
surplus remains nonnegative, (35) gives (37).  Finally,

\[
\begin{aligned}
 q_k\log_2 3-(k+e_k)
 &=\frac{q_k-\alpha k}{\alpha}-e_k\\
 &=\frac{D_k-\alpha e_k}{\alpha}\\
 &=\frac{D_{k+e_k}}{\alpha}.
\end{aligned}
\]

The last quantity is strictly positive: equality would make the irrational
number `alpha` a ratio of nonzero integers.  This proves (38)--(40).  QED.

### Consequence

The raw parity truncations cannot cross the rational-target exponent-one
barrier at any time, including even states.  Near-critical approximants are
exactly those whose post-even-run surplus is small.  PR #80 and `T-9524` show
that such low-surplus episodes are sparse; they do not convert the inequality
in the needed direction.

A derived-approximation proof must create a height saving or precision gain
larger than the exact deficit `D_(k+e_k)/alpha`, plus a fixed positive fraction
of the total height.

---

## 4. The inverse-basin route: exact valid target and current failure

The Tao transport principle suggests expanding one divergent spine into a
large inverse basin.  The correct object must retain increasing orbit minima;
a large inverse tree over one fixed spine state does not qualify, because all
of those starts have the same bounded future minimum.

Let

\[
 h_0<h_1<h_2<\cdots
\tag{41}
\]

be the tail-minimum ladder of PR #80.  For each `j`, define the high first-hit
basin

\[
 \mathcal H_j=
 \left\{
 m:\exists\ell\ge0,
 T^\ell(m)=h_j,
 T^t(m)\ge h_j\ (0\le t\le\ell),
 \text{and }h_j\text{ is the first ladder state hit}
 \right\}.
\tag{42}
\]

Every member of `H_j` has complete orbit minimum `h_j`.

---

## R-9512: a fixed-root inverse tree is not enough

**Claim ID:** `R-9512`  
**Title:** Positive inverse-tree mass over one fixed spine state does not contradict Tao  
**Status:** `PROPOSED`  
**Dependencies:** `L-9533`  

Even a uniform bound of the form

\[
 \sum_{T^\ell(m)=h}\frac1m\ge\frac{c}{h}
\tag{43}
\]

for every depth `ell` and one fixed state `h` would not itself contradict
Tao: every such preimage has orbit minimum at most the fixed number `h`, so no
function tending to infinity places the complete fixed-root tree inside one
Tao exceptional set.

The familiar even towers

\[
 h_j,2h_j,4h_j,\ldots
\]

also do not close the argument.  If one keeps only finitely many levels for
each increasing `j` so that the minima tend to infinity along the union, their
harmonic contribution is at most

\[
 \frac2{h_j}
\tag{44}
\]

per ladder state.  The available bound

\[
 h_{j+1}\le\frac{3h_j+1}{2}
\]

does not force the sum of these contributions to have positive logarithmic
density.

Thus the missing inverse-basin statement is a genuinely moving-root theorem,
not a per-root branching estimate.

---

## Q-9517: smallest inverse-basin inequality that closes Lane A

**Claim ID:** `Q-9517`  
**Title:** Positive logarithmic mass for a diagonal high first-hit basin  
**Status:** `IDEA`

It is sufficient to construct finite cohorts

\[
 G_j\subseteq\mathcal H_j
\tag{45}
\]

such that

\[
 \min G_j\longrightarrow\infty
\tag{46}
\]

and, for some `c>0` and an unbounded sequence `J`,

\[
\boxed{
 \sum_{j\le J}\sum_{m\in G_j}\frac1m
 \ge
 c\log\left(
 \max_{j\le J}\max_{m\in G_j}m
 \right).
}
\tag{47}
\]

Indeed, the diagonal union `G=union_j G_j` has orbit minimum `h_j->infinity`
as its elements tend to infinity, while (47) gives positive upper logarithmic
density.  This contradicts `L-9533`.

No current inverse-tree theorem in the repository or inspected literature
proves (47).  Existing counting exponents, even-tower families, and the
quadratic-logarithmic family from PR #80 are compatible with logarithmic
density zero.

---

## 5. Status of the surviving global atom

The Lane-A orbit has now been forced to satisfy simultaneously:

\[
\boxed{
\begin{array}{l}
D_k\ge0\text{ for every }k;\\
x_k\to\infty;\\
D_k\to\infty\text{ in natural density one};\\
\frac1K\sum_{k\le K}D_k\ge\frac89\log_3K-O_n(1);\\
\liminf D_k/k=0\quad\text{(source-qualified López--Stoll)};\\
\log P_r=o(\log x_r)\text{ at physical records};\\
\max_{k\le K}D_k\ge(1-o(1))\log_3K;\\
\text{raw parity approximants have exact exponent }<1;\\
\text{the spine and its odd side branches are logarithmically null.}
\end{array}}
\tag{48}
\]

These conditions are severe but internally compatible with a sufficiently
irregular high-complexity completion.  They do not yet yield a contradiction.

The three sharp remaining bridges are now:

1. prove the diagonal high-basin mass inequality (47);
2. prove the `SC*` least-source escape theorem of PR #81;
3. construct derived rational approximants that overcome the exact deficiency
   (38) by a uniform positive height margin.

The strongest new proved bridge is `T-9524`: Tao forces the additive correction
to be negligible at records, so asymptotically all record height must be paid by
coefficient surplus.  The smallest precise missing inequality on the inverse
side is (47).  No unconditional closure of Lane A is claimed.
