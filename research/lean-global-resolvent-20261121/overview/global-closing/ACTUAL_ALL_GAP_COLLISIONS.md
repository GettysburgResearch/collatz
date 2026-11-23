# Actual all-gap collisions, ordinary height, and entropy occupation

23 November 2026. **Status: new written finite theorems and a closing attempt.**
The results below concern one fixed positive ordinary source. They strengthen
the finite Shannon-deficit branch to a statement about a positive proportion
of the actual orbit, identify where its forced collision mass occurs in the
full gap range, and retain both arithmetic valuations at every rational
anchor. They do not prove the required collision upper bound or exclude the
critical iid branch. No new Lean verification is claimed.

## 1. Fixed source, finite laws, and inspected inputs

Fix a positive odd ternary unit `p`, and suppose its odd orbit

\[
 q_j=U^j(p),\qquad U(q)=\frac{3q+1}{2^{e(q)}},
 \qquad e(q)=v_2(3q+1)
 \tag{1}
\]

is injective. All states, words and empirical probabilities in this note
come from this same orbit. The hypothesis makes it an escaping orbit because
bounded subsets of the positive integers are finite.

For `1 <= m < N`, let `P_(N,m)` be the empirical distribution of the
chronological words

\[
 W_{j,m}=(e(q_{j-m}),\ldots,e(q_{j-1})),\qquad m\le j<N,
 \tag{2}
\]

under the uniform law on these `N-m` times. Write `H_(N,m)` for its Shannon
entropy, using natural logarithms. These are finite empirical distributions,
even though the alphabet of possible valuations is countable. The full
endpoint law is

\[
 \pi_N=\frac1N\sum_{j<N}\delta_{q_j},\qquad
 \operatorname{Col}_Q(\pi_N)=
 \frac1{N^2}\#\{(i,j):0\le i,j<N,\ q_i\equiv q_j\pmod Q\}.
 \tag{3}
\]

Put

\[
 \ell=\log_2 3,\qquad
 \Phi=\ell\log\ell-(\ell-1)\log(\ell-1),\qquad
 \theta=\Phi/\log3.
 \tag{4}
\]

The existing stationary extraction supplies a subsequence `N_i` and a
stationary gap process with finite block entropies `H_k`, such that
`H_(N_i,k) -> H_k` for each fixed `k`. Its mean valuation is at most `ell`.
The source packet records past gaps in newest-first order; (2) reverses
that order. Reversal preserves each finite block entropy and does not
alter this input. There are exactly `N-m` retained endpoints, and no word
crosses the initial time zero.
The finite Shannon-deficit case means that, for some fixed `k`,

\[
 h:=H_k/k<\Phi.
 \tag{5}
\]

The exact new finite results in Sections 2 and 4 require no stationary
extraction. Sections 3 and 5 invoke the stated fixed-block entropy limit.
That upstream stationary extraction remains source-qualified: its analytic
construction and fixed-block entropy convergence are not reproved here.

| Frozen source | Input actually used |
|---|---|
| PR180, `7d4ad9f11d3d7a54c67b0c6cff4f13a2ab967161`, `research/whole-source-20261123/COLLISION_CORE.md` | The actual stationary gap extraction, convergence of fixed-block entropies, strict deficit/iid dichotomy and critical exponent. The finite block-entropy bound used below is reproved. |
| PR178, `c91b80a3156e640ad471cf30c47721145ae21eb1`, `research/central-step-20261123/stationary/FAST_EQUIVALENT_FLOW.md` | Exponentially reweighted positive harmonic flow; simultaneous `O(1/N)` comparison with `pi_N` for arbitrary inverse clocks and moduli. |
| PR180, same head, `research/profound-step-20261123/STATIONARY_REAL.md` and `ENTROPY_ARITHMETIC.md` | Actual-law renewal, fixed-resolution scale-phase independence, and their source/limit qualifications. Neither is used as a collision upper estimate. |
| PR182, `cb1ae1bb4af0c8d082e9ff466b9fe0c84932301c`, `research/literature-round4-20261123/ACTUAL_LAW_RIGIDITY.md` | Finite de Bruijn constructions change the ordinary source with the horizon. Their obstruction is not a counterexample to a fixed-source theorem. |
| Checkpoint17, `4171e1fe40e41842af9f800bd821084b724cf8f9`, `research/lean-global-resolvent-20261121/overview/source-construction/HAAR_AND_ORDINARY_LABELS.md` | Even unthickened Haar convergence, under an additional Rajchman hypothesis, retains the actual endpoint law as a separate marginal. |

## 2. An exact entropy bound for ordinary low-height occupation

### 2.1 Sliding-block entropy, with its sampling law retained

For `1 <= k <= m < N`,

\[
 \boxed{(N-m)H_{N,m}
 \le \left\lceil\frac mk\right\rceil (N-k)H_{N,k}.}
 \tag{6}
\]

To prove this, cover the `m` coordinates by `ceil(m/k)` consecutive
`k`-blocks. Use disjoint blocks from the left, with the last block ending at
the last coordinate; the last block may overlap its predecessor. Their
joint values determine the full `m`-word. Entropy subadditivity therefore
bounds `H_(N,m)` by the sum of the entropies of these block marginals.

For any one offset, that block marginal is the uniform empirical law of
`N-m` consecutive starting positions contained among the `N-k` positions
defining `P_(N,k)`. The full `k`-word law is the convex mixture of this
marginal, with weight `(N-m)/(N-k)`, and the empirical law of the remaining
positions. Concavity and nonnegativity of entropy give the corresponding
bound `(N-k)H_(N,k)/(N-m)` for each marginal. Summing proves (6).

No independence of windows is asserted. There is no change from actual
time sampling to a uniform law on all valuation words.

### 2.2 Low ordinary endpoints have distinct words at adequate precision

Let `X >= 1`, choose `m` with `3^m > X`, and put

\[
 K=\#\{m\le j<N:q_j\le X\}.
 \tag{7}
\]

Then

\[
 \boxed{K\log K
 \le (N-m)H_{N,m}
 \le \left\lceil\frac mk\right\rceil (N-k)H_{N,k},}
 \tag{8}
\]

where `0 log 0` is zero.

For a word `w=(e_0,...,e_(m-1))`, write `A=sum e_r` and

\[
 C(w)=\sum_{r=0}^{m-1}3^{m-1-r}2^{e_0+\cdots+e_{r-1}}.
 \tag{9}
\]

The exact affine identity gives

\[
 2^Aq_j=3^m q_{j-m}+C(w),
 \qquad q_j\equiv 2^{-A}C(w)\pmod{3^m}.
 \tag{10}
\]

Consequently two occurrences of the same `m`-word have the same endpoint
residue. Distinct positive endpoints both at most `X < 3^m` cannot have
the same residue. The `K` low-endpoint times therefore have distinct words.

Let `J` be uniform on the `N-m` retained times and let `L` be the event
`q_J <= X`. If `K>0`, the conditional word law given `L` is uniform on
`K` different words. Conditional entropy and concavity give

\[
 H_{N,m}\ge\Pr(L)H(W_{J,m}\mid L)
 =\frac K{N-m}\log K.
 \tag{11}
\]

Together with (6) this proves (8). This is an ordinary endpoint statement;
compactification, real phases and source quotients have not been removed.

## 3. A fixed block entropy controls a positive fraction of the same orbit

**Theorem 1 (entropy occupation).** Suppose for some fixed `k` and some
subsequence `N_i -> infinity` that `H_(N_i,k) -> H_k < infinity`. Put
`alpha=H_k/(k log 3)`. For every fixed `B>0`,

\[
 \boxed{\limsup_{i\to\infty}\frac1{N_i}
   \#\{j<N_i:q_j\le N_i^B\}
 \le \min\{1,\alpha B\}.}
 \tag{12}
\]

Equivalently,

\[
 \liminf_{i\to\infty}\frac1{N_i}
   \#\{j<N_i:q_j>N_i^B\}
 \ge \max\{0,1-\alpha B\}.
 \tag{13}
\]

**Proof.** Take `m_i=floor(B log_3 N_i)+1`, so that
`3^(m_i)>N_i^B` and `m_i=O(log N_i)`. Apply (8). It yields

\[
 \frac{K_i}{N_i}\frac{\log K_i}{\log N_i}
 \le
 \frac{\lceil m_i/k\rceil}{\log N_i}
 \frac{N_i-k}{N_i}H_{N_i,k}
 \longrightarrow \alpha B.
 \tag{14}
\]

Pass to a subsequence realizing the limsup of `K_i/N_i`. If its limit is
positive then `log K_i/log N_i -> 1`; if its limit is zero the claim is
immediate. The first `m_i` omitted endpoint times have density zero.
This proves (12) and (13).

In the finite Shannon-deficit branch, `alpha<theta`. For every

\[
 \frac1\theta<B<\frac1\alpha
 \tag{15}
\]

a fixed positive fraction of the same orbit lies above `N_i^B`. Thus the
consequence concerns actual occupation, not only one large excursion.
When `alpha=0`, the low-endpoint proportion tends to zero for every fixed
power `N_i^B`.

For the maximum height `H_i^*=max_(j<N_i) q_j`, (12) also gives

\[
 \liminf_i\frac{\log H_i^*}{\log N_i}\ge\frac1\alpha,
 \tag{16}
\]

with the right side interpreted as infinity when `alpha=0`.

These conclusions are compatible with an escaping orbit whose heights
grow exponentially or faster than every fixed power. They do not settle
the finite-deficit branch. In the critical iid branch all finite block
entropies equal `k Phi`, so this argument has `alpha=theta` and supplies no
strict gain.

## 4. Every collision retains a rational anchor and both arithmetic valuations

Fix `i >= 0`, `d >= 1`, and let `w` be the actual word from `q_i` to
`q_(i+d)`. Use `A=A(w)`, `C=C(w)` from (9), and put

\[
 D=2^A-3^d,\qquad g=\gcd(C,|D|),\qquad
 c=C/g,\quad b=D/g,\quad z=c/b.
 \tag{17}
\]

Here `D` is nonzero, and `b` and `g` are odd and prime to three. The
unreduced rational anchor `C/D` is the fixed point of the word's affine
map. Its sign is not prescribed: expanding words have negative anchors.
Write `H(z)=max(c,|b|)` for its reduced rational height.

The affine identity gives, exactly,

\[
 \boxed{bq_i-c=\frac{2^A(q_i-q_{i+d})}{g}.}
 \tag{18}
\]

Since `g` is coprime to `2`, it divides `q_i-q_(i+d)`. Taking valuations
therefore gives

\[
 \boxed{v_2(bq_i-c)=A+v_2(q_i-q_{i+d}),\qquad
 v_3(bq_i-c)=v_3(q_i-q_{i+d}).}
 \tag{19}
\]

Both sides are finite because the actual orbit is injective. Thus if
`q_i == q_(i+d) (mod 3^m)`,

\[
 \boxed{2^{A+1}3^m\mid bq_i-c,
 \qquad
 H(z)\ge\frac{2^{A+1}3^m}{q_i+1}.}
 \tag{20}
\]

The extra factor two uses oddness of both endpoints. The height inequality
follows from `0<|bq_i-c| <= (q_i+1)H(z)`. It is valid for every actual gap,
without a periodic-word assumption.

For the same fixed starting state `q_i`, a fixed reduced anchor `c/b` can
occur only at gaps satisfying

\[
 A\le v_2(bq_i-c)-1,
 \qquad
 m\le v_3(bq_i-c)
 \tag{21}
\]

if that occurrence also collides modulo `3^m`. Since `A>=d` and increases
strictly with `d`, one fixed anchor cannot recur at unbounded gaps from
that same source. More uniformly, all colliding anchors of height at most
`H` obey

\[
 d+1\le\log_2\frac{(q_i+1)H}{3^m}.
 \tag{22}
\]

This is a genuine fixed-source payment. It does not bound anchors of
unrestricted height, and its source is `q_i`, not a uniform replacement
for all positions along the orbit.

### Exact return kernel for each complete word

For any positive valuation word `w` of length `d`, its exact legal ordinary
source cylinder is one residue class modulo `2^(A+1)`:

\[
 a_w\equiv (2^A-C)3^{-d}\pmod{2^{A+1}}.
 \tag{23}
\]

This congruence says that the final affine endpoint is odd. Reading the
affine recurrence backwards, or inducting on the word length, shows that
it also supplies all the prescribed exact intermediate valuations.

On that cylinder the return condition modulo `3^m` is independently

\[
 q\equiv CD^{-1}\pmod{3^m}.
 \tag{24}
\]

The complete return set for this word is consequently one CRT class
modulo `2^(A+1)3^m`. In a source interval of length `X`, it has at most

\[
 \frac{X}{2^{A+1}3^m}+1
 \tag{25}
\]

members. This elementary count cannot be summed as if the actual orbit
were uniform in source intervals or as if its words were independent of
their sources. Equations (18)--(25) retain that dependence explicitly.

## 5. A strict entropy deficit puts the necessary collision mass at long gaps

The entire pair-gap kernel is

\[
 \operatorname{Col}_{3^m}(\pi_N)
 =\frac1N+\frac2{N^2}
   \sum_{d=1}^{N-1}\sum_{i=0}^{N-d-1}
       \mathbf1_{3^m\mid q_{i+d}-q_i}.
 \tag{26}
\]

No lag truncation has been made.

Endpoint residues are a function of the actual past word, by (10).
Grouping atoms increases collision probability, and Shannon entropy
bounds Renyi entropy of order two from above. The tail empirical endpoint
law therefore gives the exact finite lower bound

\[
 \operatorname{Col}_{3^m}(\pi_N)
 \ge\left(1-\frac mN\right)^2e^{-H_{N,m}}.
 \tag{27}
\]

Assume (5), fix `h_bar` with `h<h_bar<Phi`, and put

\[
 m_i=\left\lfloor\frac{\log N_i}{\Phi}\right\rfloor,
 \qquad \beta=1-h_{\rm bar}/\Phi>0.
 \tag{28}
\]

Equation (6) and the fixed-block entropy limit give
`H_(N_i,m_i) <= h_bar m_i` for all sufficiently large `i`. Consequently
there is `c>0` such that

\[
 \#\{(a,b)<N_i:q_a\equiv q_b\pmod{3^{m_i}}\}
 \ge cN_i^{1+\beta}.
 \tag{29}
\]

But at most `N_i(2L+1)` ordered pairs have `|a-b|<=L`. Hence:

**Theorem 2 (all-gap location).** For every nonnegative integer sequence
`L_i=o(N_i^beta)`,

\[
 \boxed{\#\{(a,b)<N_i:|a-b|>L_i,\
             q_a\equiv q_b\pmod{3^{m_i}}\}
 \ge(c-o(1))N_i^{1+\beta}.}
 \tag{30}
\]

In particular, for any fixed `0<epsilon<beta`, the forced collision mass
cannot be accounted for by gaps at most `N_i^(beta-epsilon)`. The critical
precision is only `m_i=O(log N_i)`, whereas the contributing gaps must
include lengths much larger than this precision.

This is why an argument restricted to short shadows, adjacent returns or
a fixed collection of periodic anchors cannot supply the missing critical
upper estimate. Each long gap still obeys (20), but its anchor and its
starting source can both change. There is no implication here that two
colliding endpoints have the same valuation word.

## 6. Closing attempt and the first missing estimate

The fast equivalent-flow construction removes an earlier comparison-rate
problem. For its one fixed reweighting and any deterministic finite inverse
clock list, it gives laws `zeta_N` satisfying

\[
 d_{\rm TV}(\zeta_N,\pi_N)\le D/N,
 \qquad
 |\sqrt{\operatorname{Col}_Q(\zeta_N)}
       -\sqrt{\operatorname{Col}_Q(\pi_N)}|
 \le\sqrt2D/N
 \tag{31}
\]

simultaneously for every finite modulus `Q`. Since
`Col_Q(pi_N)>=1/N`, their collision probabilities are multiplicatively
equivalent uniformly in `Q`. Thus the actual pair sum (26) is also the
closing problem for that regularized inverse law. Reweighting does not
produce new randomness in the retained ordinary endpoint.

The attempted arithmetic closure was to combine (20) at many collisions,
use distinct rational anchors, and rule out so much simultaneous ordinary
height expenditure. The point at which the argument stops is precise:
neither the sum of the changing source heights `q_i` nor the heights of the
changing anchors are bounded by the supplied entropy or renewal inputs.
Equation (30) also prevents us from replacing the full sum by its short
gap part.

A primary arithmetic comparison was inspected in Lyapunov Weaver,
[Paper 28 v3, Sections 7.10--7.11](https://rstation.ai/problems/collatz/papers/28).
Its joint concentration theorem uses independent critical geometric words,
with a specified total-clock treatment. The cross coordinates are
canonical **source modulo a power of three** and canonical **endpoint
modulo a power of two**. They are not the ternary endpoint marginal of
(26). The actual source and endpoint have a shared ordinary quotient:

\[
 q_i=n_w+2^A t,\qquad q_{i+d}=u_w+3^d t.
 \tag{32}
\]

The inspected averaged theorem does not control that actual `t` at every
fixed source. The stationary iid equality case supplies independence of
fixed word coordinates, but no growing-resolution conditional law for this
quotient. No import of that arithmetic theorem closes (26).

There are two useful, distinct closing targets:

1. A critical finite-horizon upper bound
   `Col_(3^m)(pi_N) <= exp(o(m)) 3^(-theta m)` at
   `m=floor(log N/Phi)` would contradict (27) in every finite-deficit
   subsequence. The exponent in (30) quantifies the long-gap contribution
   which such an upper bound must actually control.
2. To include the iid equality branch by the existing stationary collision
   argument, retain one subsequence `N_i` and first take `i -> infinity`
   at each fixed `m`. For its actual limit `nu`, the required conclusion is
   `Col_(3^m)(nu) <= exp(o(m)) 3^(-theta m)` as `m -> infinity`.
   Neither a critical diagonal estimate nor fixed-resolution phase
   independence automatically permits this order of limits.

These are upper bounds on the same endpoint law. Replacing it by compact
Haar measure, by an independent word process, by a source-averaged law, or
by a different ordinary source at each horizon does not prove either one.
The work here proves (8), (12), (20) and (30), and leaves these upper bounds
open.
