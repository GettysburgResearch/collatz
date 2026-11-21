# Ordinary renewal: a critical first moment detects every escaping source

**Status.** This is a written conditional closure argument, not a Lean proof
of Collatz. The main new deduction is that the proposed uniform ordinary
predecessor population in PR180 turns **one** injective positive orbit into
an infinite logarithmic first moment of actual orbit minima. Consequently,
under that population hypothesis, a finite first moment would force a
finite global periodic attractor. A weighted version of Tao's first-passage
transport gives a precise sufficient estimate for that first moment. The
estimate is not established here. Identifying the surviving periodic
attractor with the cycle through 1 is a further obligation.

The argument retains positive ordinary sources and all of their future
states. It does not transfer an almost-everywhere ternary statement to a
prescribed positive integer.

## 1. Primary literature and the input being sought

The following primary sources were inspected for this route.

| Source | Usable statement and role |
|---|---|
| Terence Tao, [*Almost all orbits of the Collatz map attain almost bounded values*, corrected arXiv v7](https://arxiv.org/html/1909.03562v7), [published version](https://doi.org/10.1017/fmp.2022.8) | Theorem 3.1 gives the uniform logarithmic survivor bound (R12) below. Proposition 1.11 compares the first-passage laws of logarithmically sampled ordinary sources at consecutive scales. Proposition 1.9 supplies a geometric valuation law under an explicit approximately uniform binary-source hypothesis. These are quantitative transport inputs, with their source distributions retained. |
| Ivan Korec, [*A density estimate for the 3x+1 problem*](https://www.dml.cz/bitstream/handle/10338.dmlcz/133225/MathSlov_44-1994-1_8.pdf), Theorem 1 | For every exponent greater than log-base-4 of 3, the integers with some iterate below that power of their starting value have natural density one. Its finite parity-prefix counting does not provide the weighted transport defect in (R15). |
| Ilia Krasikov and Jeffrey Lagarias, [*Bounds for the 3x+1 problem using difference inequalities*](https://arxiv.org/pdf/math/0205002), Theorem 1.1 and §2 | For each fixed positive target prime to 3 and sufficiently large source cutoff, the predecessor count is at least the cutoff to the power 0.84. This validates a substantial quantitative inverse-tree mechanism. It does not provide the uniform linear population used in this note. |
| Ian Melbourne and Dalia Terhesiu, [*Operator renewal theory and mixing rates for dynamical systems with infinite measure*, corrected author PDF](https://math-ianmelbourne.github.io/papers/oprenew_corrected.pdf), introduction and §§2–3 | First-return operators obey an exact renewal convolution. Quantitative renewal requires the paper's measure, return-tail, and spectral hypotheses. The useful design principle here is to retain both the transported source and the return defect, rather than infer a contraction from formal renewal alone. |
| Kenneth M. Monks, [*The Sufficiency of Arithmetic Progressions for the 3x+1 Conjecture*](https://monks.scranton.edu/content/pubs/SufficiencyRev4.pdf), Theorem 1.1 and Lemma 3.8 | Every nonconstant arithmetic progression meets every ordinary merger component. The construction preserves an actual merger. Its theorem does not assert a uniform height or population bound for those representatives. |

### The repository population hypothesis is separately qualified

Freeze PR180 at
`d0349de2108abb7c8fb8393c086610e3372df116`, specifically
[`research/lean-forward-band-20261121/GLOBAL_RENEWAL_ATTACK.md`](https://github.com/GettysburgResearch/collatz/blob/d0349de2108abb7c8fb8393c086610e3372df116/research/lean-forward-band-20261121/GLOBAL_RENEWAL_ATTACK.md),
§5. Its written analytic argument claims absolute constants
`c_u,C_u>0` such that

\[
 X\ge C_{\rm u}a\quad\Longrightarrow\quad
 \#\{n\le X:n>0,\ n\text{ odd},\ 3\nmid n,\ n\to a\}
       \ge c_{\rm u}X/a                                      \tag{PDU}
\]

for every positive target `a` prime to 3. The shortcut hitting relation is
the one in that source. The source's joint-clock argument is stronger than
the predecessor-count theorem of Krasikov–Lagarias; it is not a direct
quotation of Tao's almost-bounded-orbit theorem. This pass does not
independently certify that new analytic argument. **Every result below
which invokes (PDU) is conditional on this exact statement.** The
population assertion is not added as a Lean axiom.

The published classical lower count cannot be substituted silently:
integrating `X^0.84` against `X^-2` does not produce a positive coefficient
of `log X` for one fixed basin. That coefficient is the amplification
used below.

## 2. Ordinary definitions and a harmonic population identity

Work on

\[
 \mathcal O^*=\{n\ge1:n\text{ odd},\ 3\nmid n\},\qquad
 U(n)=\frac{3n+1}{2^{v_2(3n+1)}}.
\]

This state space is forward invariant. Every positive shortcut orbit
enters it after removing initial powers of two and, if necessary, taking
one accelerated odd step. Thus excluding injective orbits here excludes
positive nonperiodic shortcut orbits.

For `a` in this state space define

\[
 B(a)=\{n\in\mathcal O^*:U^q(n)=a\text{ for some }q\ge0\},
 \qquad m(n)=\min_{q\ge0}U^q(n).
\]

The minimum exists in the positive integers without any convergence
assumption. A shortcut hit to an odd target is an accelerated odd hit, so
(PDU) applies to `B(a)`.

Increase `C_u` to at least 2 if necessary. Put
`A_a(X)=#(B(a) intersect [1,X])`. Partial summation gives the exact identity

\[
 \sum_{\substack{n\le X\\n\in B(a)}}\frac1n
  =\frac{A_a(X)}X+\int_1^X\frac{A_a(t)}{t^2}\,dt.
\]

Its nonnegative terms and (PDU) imply

\[
 \boxed{\quad
 \sum_{\substack{n\le X\\n\in B(a)}}\frac1n
 \ge \frac{c_{\rm u}}a\log\frac X{C_{\rm u}a}
 \quad(X\ge C_{\rm u}a).\quad}                    \tag{R1}
\]

For finitely many pairwise disjoint basins these inequalities may be
summed at every common cutoff `X>=C_u max a`. There is no exchange of an
infinite family with a target-dependent onset.

The normalization below is by `log X`, not by the harmonic mass of
`O* intersect [1,X]`. The latter is `(1/3)log X+O(1)`, since `O*`
consists of the two residue classes 1 and 5 modulo 6.

## 3. One escaping source gives an all-time survivor antichain

The entire construction in this section is unconditional.

Suppose `n_q=U^q(n_0)` is injective. It tends to infinity: a finite
interval contains only finitely many distinct positive integers.
Enumerate its successive **suffix minima** `t_0,t_1,...`. Namely, take
the minimum of the full orbit, then the minimum of the tail after that
value, and continue. Their occurrence clocks increase, the values
strictly increase, and every state after the occurrence of `t_j` is at
least `t_j`. The immediate successor belongs to the next tail, whence

\[
 t_{j+1}\le U(t_j)\le\frac{3t_j+1}{2},\qquad
 t_j+1\le(3/2)^j(t_0+1).                            \tag{R2}
\]

For every `t_j`, exactly two exponents `a` in `{1,...,6}` satisfy
`2^a t_j = 4 or 7 modulo 9`. This follows because 2 runs through all six
units modulo 9. They give two distinct positive odd unit predecessors

\[
 b=(2^a t_j-1)/3,\qquad U(b)=t_j.
\]

At most one is the state immediately before `t_j` in the original orbit.
Choose another and call it `b_j`. No `b_j` is anywhere on that orbit:
injectivity would force any orbit state mapping to `t_j` to be its unique
previous state. Set

\[
 K=64/3,\qquad b_j<Kt_j.                             \tag{R3}
\]

The full predecessor sets `B(b_j)` are pairwise disjoint. Otherwise one
forward trajectory would hit two different `b_j`. After its first such
hit its next state is on the original orbit; that original orbit
contains none of the `b_j`, a contradiction.

Choose the actual least ordinary source in each basin:

\[
 r_j=\min B(b_j).
\]

The `r_j` are distinct, `r_j<=b_j<Kt_j`, and the basins `B(r_j)` are
pairwise disjoint subsets of `B(b_j)`. Before a trajectory in `B(r_j)`
hits `b_j`, every one of its states belongs to `B(b_j)`, hence is at
least `r_j`. Its remaining trajectory starts at `t_j`, a suffix minimum.
Both `r_j` and `t_j` are actually attained. We have therefore proved the
stronger exact identity

\[
 \boxed{\qquad
  n\in B(r_j)\quad\Longrightarrow\quad
  m(n)=\min(r_j,t_j)\ge r_j/K.
 \qquad}                                             \tag{R4}
\]

This is an all-time lower bound on the trajectory of every counted
source. No assertion about typical future valuations is used.

## 4. The critical first-moment theorem

Define the ordinary logarithmic first moment

\[
 \mathcal M(X)=\frac1{\log X}
     \sum_{\substack{n\le X\\n\in\mathcal O^*}}\frac{m(n)}n,
 \qquad X\ge2.                                      \tag{R5}
\]

**Theorem R1, conditional on (PDU).** If any positive accelerated orbit
is injective, then

\[
              \liminf_{X\to\infty}\mathcal M(X)=\infty.       \tag{R6}
\]

**Proof.** For any fixed finite selection of `N` roots from §3, disjointness,
(R4), and (R1) give

\[
 \mathcal M(X)\ge
  \frac{c_{\rm u}}K
  \sum_{j=1}^{N}
   \frac{\log(X/(C_{\rm u}r_j))}{\log X}
   \qquad(X\ge C_{\rm u}\max_{1\le j\le N}r_j).
                                                               \tag{R7}
\]

Each of these finitely many quotients tends to 1. Thus the lower limit
is at least `Nc_u/K`. Since `N` is arbitrary, it is infinite. This order
of the two limits avoids any uniformity assumption on the root sequence.

**Corollary R2, conditional on (PDU).** The estimate

\[
              \liminf_{X\to\infty}\mathcal M(X)<\infty         \tag{FM}
\]

would imply that every positive orbit eventually enters a periodic orbit
and that there are only finitely many ordinary merger components.

For the second assertion, choose the least odd unit `s_i` in each
component. Its full basin has `m(n)=s_i`, because the entire future stays
in that same component and actually visits `s_i`. For any finite set of
components, (R1) now gives a contribution of at least `c_u` per component
in the lower limit of (R5). Infinitely many components would contradict
(FM). In fact, if that lower limit is `L<infinity`, their number is at
most `L/c_u`.

Consequently there would be a finite set of positive cycles attracting
every input. The maximum of their least odd members would bound `m(n)`
for every positive odd `n`. Conversely, any such global bound immediately
implies (FM). The conditional theorem therefore promotes a finite
ordinary first moment to a finite global attractor. It does not select
the cycle through 1 from that finite set.

## 5. A sharper necessary survivor tail from the same antichain

Let

\[
 \tau(M)=\limsup_{X\to\infty}\frac1{\log X}
       \sum_{\substack{n\le X\\n\in\mathcal O^*\\m(n)>M}}\frac1n.
\]

For every finite subset `F` of the roots with `r_j>KM`, the same
source-preserving argument gives the finite-scale inequality

\[
 c_{\rm u}\sum_{j\in F}\frac1{r_j}
     \log\frac X{C_{\rm u}r_j}
 \le \sum_{\substack{n\le X\\n\in\mathcal O^*\\m(n)>M}}\frac1n
 \quad(X\ge C_{\rm u}\max_{j\in F}r_j).              \tag{R8}
\]

First take the lower limit in `X`, then enlarge finite subsets. This proves

\[
             c_{\rm u}\sum_{r_j>KM}\frac1{r_j}\le\tau(M).     \tag{R9}
\]

The sum over all roots converges: counting disjoint basins by (PDU) and
using the density `1/3` of the source space gives
`c_u sum_j 1/r_j <= 1/3` by the same finite-family limit.

There is a useful improvement over taking just one term in (R9). Sort
the roots increasingly as `rho_0<rho_1<...`. At least `k+1` original
roots are less than `Kt_k`, so

\[
 \rho_k\le K(t_0+1)(3/2)^k.
\]

For a strictly increasing sequence with this bound and summable
reciprocals, put `h_k=rho_k sum_{l>=k}1/rho_l`. Then

\[
 h_k=1+\frac{\rho_k}{\rho_{k+1}}h_{k+1},\qquad
 \limsup_{k\to\infty}h_k\ge3.                        \tag{R10}
\]

For completeness, if `h_k<=H<3` eventually, take `H>1` and multiply the
recursion to obtain

\[
 \frac{\rho_N}{\rho_J}
   =\frac{h_N}{h_J}
      \prod_{k=J}^{N-1}\frac{h_k}{h_k-1}
   \ge\frac1{h_J}\left(\frac H{H-1}\right)^{N-J}.
\]

Its growth rate exceeds `3/2`, contradicting the displayed upper bound
on `rho_N`. This proves (R10).

Take the integer `M_k=ceil(rho_k/K)-1`. It is strictly less than
`rho_k/K`, tends to infinity, and satisfies `M_k/rho_k -> 1/K`.
Using the entire reciprocal tail in (R9) now gives

\[
 \boxed{\qquad
 \limsup_{M\to\infty}M\tau(M)\ge\frac{3c_{\rm u}}K
                       =\frac{9c_{\rm u}}{64}.
 \qquad}                                             \tag{R11}
\]

Thus, conditional on (PDU), a proof of `tau(M)=o(1/M)` would exclude
every escaping source. This is a quantitative necessary consequence of
one orbit, not merely a statement that exceptional sources could remain.

Tao's Theorem 3.1 supplies absolute positive constants with the following
bound. Here `U` and `m` are evaluated on all positive odd sources by the
same formulas as above:

\[
 \frac1{\log X}
  \sum_{\substack{n\le X\\n\text{ odd}\\m(n)>M}}\frac1n
       \le C_T(\log M)^{-\kappa}\qquad(M,X\ge2).       \tag{R12}
\]

Consequently the left side of (R8) is also at most
`C_T log X/(log M)^kappa`. This gives a finite-scale, ordinary-source
capacity inequality for the whole antichain. The bound is quantitatively
compatible with (R11). A reciprocal tail is the critical target here;
the logarithmic tail bound alone does not reach it.

## 6. A concrete weighted first-passage renewal that would prove (FM)

In this section work on all positive odd integers. Fix an `alpha>1`
in the range of Tao's Proposition 1.11. Let `N_y` have logarithmic law
on the odd integers of `[y,y^alpha]`, and set

\[
 L(y)=\mathbb E\,m(N_y).
\]

For a threshold `x`, let `T_x(N)` be the first accelerated clock with
`U^q(N)<=x`, with value infinity if it never occurs. On successful
passage, write `Pass_x(N)=U^{T_x(N)}(N)`. Every earlier state is greater
than `x`, so the full all-time minimum is preserved **exactly**:

\[
               m(N)=m(\operatorname{Pass}_x(N)).       \tag{R13}
\]

Let `nu_x^(1)` and `nu_x^(2)` be the subprobability laws on odd
`u<=x` of the successful endpoints from `N_(x^alpha)` and
`N_(x^(alpha^2))`, respectively. Tao assigns the artificial value 1 to
failed passages; here that atom is removed. The change in the comparison
of the two laws is at most the sum of their non-passage probabilities,
which preserves the crude total-variation order used below. Keep the
unpassed sources in the nonnegative quantities

\[
 Q_i(x)=\mathbb E\bigl[m(N_{x^{\alpha^i}})
             1_{\{T_x(N_{x^{\alpha^i}})=\infty\}}\bigr],
 \qquad i=1,2.
\]

The actual-source identities are

\[
 L(x^{\alpha^i})=\sum_{u\le x,\ u\text{ odd}}m(u)\nu_x^{(i)}(u)
                      +Q_i(x).
\]

Since `m(u)<=u` and `Q_1>=0`, they imply the exact sufficient estimate

\[
 \begin{split}
 L(x^{\alpha^2})&\le L(x^\alpha)+E(x),\\
 E(x)&=\sum_{u\le x,\ u\text{ odd}}
             u\,|\nu_x^{(2)}(u)-\nu_x^{(1)}(u)|+Q_2(x).
 \end{split}                                                   \tag{R14}
\]

**The new analytic target is** a source-preserving weighted defect bound
such that, for some sufficiently large `x_0`,

\[
             \sum_{j\ge0}E(x_0^{\alpha^j})<\infty.             \tag{R15}
\]

Indeed, (R14) telescopes along `x_j=x_0^(alpha^j)` and bounds
`L(x_j)` uniformly for `j>=1`. These logarithmic sampling annuli cover
`[x_1,x_J]`. Their harmonic masses sum to `O(log x_J)`; shared endpoints
are harmless nonnegative overcounts, with bounded total harmonic weight.
Multiplying their uniformly bounded
expectations by those masses proves a finite upper bound for (R5) along
the cutoffs `x_J`. Restricting from all odd sources to `O*` only decreases
that nonnegative sum. Thus (R15) implies (FM), and with (PDU) would prove
the finite-attractor conclusion of Corollary R2.

This exposes a specific attempted upgrade of published transport. The
total-variation estimate of Proposition 1.11 gives only
`sum u |nu_x^(2)-nu_x^(1)| << x/(log x)^c` by direct bounded-observable
comparison. Its non-passage probability bound also requires multiplication
by the **actual surviving minimum** in `Q_2`; discarding those sources
would invalidate (R14). Bounding that minimum just by its initial value
gives `Q_2(x) << x^(alpha^3-c)`, with no useful summability conclusion.
In particular the first of these crude bounds already increases along
the scale sequence. A weighted transport estimate or a separate bound on
the unpassed-source cost is therefore required. Neither is supplied by
the total-variation theorem as stated.

The first unsupported step in this renewal attempt is precisely (R15),
not an implicit restart with a freshly random source. There may be
sharper ways to estimate the signed observable difference in (R14), but
none is claimed here.

## 7. Why two apparent shortcuts do not furnish the weighted defect

### Inverse padding retains the original source's exhausted precision

PR175 at `2055b8a311ab87d07bffc730154a7f8546fe382c`,
[`INVERSE_CARRY_CONTINUATION.md`](https://github.com/GettysburgResearch/collatz/blob/2055b8a311ab87d07bffc730154a7f8546fe382c/research/lean-global-closure-20261121/INVERSE_CARRY_CONTINUATION.md),
records the actual quotient identity for the shortcut map `T`:

\[
 \left\lfloor\frac{T^t(n)}{3^{a_t(n)}}\right\rfloor
                   =\left\lfloor\frac n{2^t}\right\rfloor,
\]

where `a_t(n)` is its actual odd-step count. If an ancestor `M` reaches
the fixed source `n` at clock `k`, with `a` odd steps, it follows that

\[
             2^{k+h}\le M\quad\Longleftrightarrow\quad
                         3^a2^h\le n.                \tag{R16}
\]

Thus making the inverse ancestor very large does not independently create
an arbitrarily large real binary horizon *after* arrival at `n`. The
source-uniformity premise of Tao's Proposition 1.9 cannot be inferred from
the size of the padded ancestor alone. An actual conditional source law
would still need proof.

### Arithmetic-progression sufficiency is qualitative population

Monks's construction may first move forward from the supplied input and
then backtrace. Its conclusion preserves merger membership, but does not
supply (PDU) or a bounded-height representative. This is a real logical
distinction: enumerate all positive arithmetic-progression tails, and
choose one representative from the `i`th tail larger than `2^(2^i)` and
all previous choices. The selected set meets every progression cofinally
while having zero natural and logarithmic density. This example concerns
the strength of a qualitative intersection statement; it is not proposed
as a Collatz component.

Therefore arithmetic-progression sufficiency by itself cannot replace
the harmonic population input in (R1). A quantitative real-height or
source-count bound is still needed.

## 8. Relation to the Green and ordinary envelope routes

The preceding packet's
[`GREEN_FRACTIONAL_MOMENTS.md`](../reframe-20261121/GREEN_FRACTIONAL_MOMENTS.md)
proves subcritical Haar moments of the compact squared inverse Green
function; its first Haar moment is infinite. The companion
[`GREEN_TOPOLOGY.md`](../reframe-20261121/GREEN_TOPOLOGY.md)
proves that the compact infinite-Green set is a dense residual null set,
whereas every positive ordinary unit has finite Green value. Those are
different observables and a different sampling measure from (R5).
No domination or change-of-measure inequality identifying their moments
has been established. In particular, a compact fractional-moment bound
does not estimate either the ordinary defect `E(x)` or `Q_2(x)`.

The updated PR180 source, §8, also constructs an ordinary envelope
`P F<=F`, with a positive unit floor and a finite polynomial upper bound,
for the **first-power** inverse operator

\[
 (PF)(q)=\sum_{\substack{e\ge1\\2^eq\equiv1\ (3)}}
             \frac3{2^e}F((2^eq-1)/3).
\]

It explicitly leaves uniform sublinearity `F(q)/q -> 0` unproved. Taking
that construction as a separate source-qualified input gives the
following exact connection to an escaping orbit.

Choose an off-orbit unit parent `b_j<K n_j` at **every** state of the
injective orbit, using the same two-parent choice as in §3. Their full
basins are disjoint. Hence (PDU) gives
`sum_j 1/n_j <= K/(3c_u)`. The actual inverse term for the edge
`U(n_j)=n_(j+1)` gives

\[
 \frac{F(n_{j+1})}{n_{j+1}}
 \ge\frac{3n_j}{3n_j+1}\frac{F(n_j)}{n_j}.
\]

The reciprocal sum makes the product of these factors positive, so

\[
 \inf_j\frac{F(n_j)}{n_j}
 \ge\frac{F(n_0)}{n_0}
          \exp\!\left(-\frac13\sum_{j\ge0}\frac1{n_j}\right)>0.
                                                               \tag{R17}
\]

Thus an escaping orbit would force linear envelope growth on its own
trajectory. This is compatible with the source's available linear bound
for nonperiodic targets. Its raywise sublinearity on predecessors of a
fixed target concerns a different set of inputs and does not contradict
(R17). Neither (FM) nor uniform envelope sublinearity is deduced here.

## 9. Precisely what this route has and has not closed

The source antichain (R2)–(R4), the partial-summation calculation, and the
weighted first-passage identity (R13)–(R14) are direct written proofs.
Conditional on the frozen (PDU), a single escaping source forces both an
infinite ordinary logarithmic first moment and the reciprocal survivor
tail (R11). No finite-source exceptions survive either contradiction
criterion.

The remaining analytic task is a bound such as (R15), or another proof
of (FM), with the original ordinary sources retained. The remaining
periodic task is exclusion of positive cycles other than the cycle
through 1. Neither obligation is replaced by a compact almost-everywhere
claim, an assumption of independent future valuations, or a Lean axiom.
