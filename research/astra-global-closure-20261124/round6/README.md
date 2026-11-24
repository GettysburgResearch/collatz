# Integral points, fixed-target rays and completed residue routing

**Collatz remains OPEN.** This sixth continuation applies classical integral-point theory, almost-unit gcd estimates, $3$-adic logarithm bounds and prime-power exponential sums to the repository's actual ordinary trajectories. The results below are **proposed written mathematics**, with exact imported interfaces and independent internal reviews. Three new Lean modules check 21 selected finite declarations. They do not formalize the external analytic theorems or prove universal convergence.

Baseline: PR195 `1c6e750e2f6970e6d5456cba5a93c2f3de8c2a97`. The latest PR192 and PR193 continuations were read at their new heads before developing these arguments. Three GPT-6.2 Astra streams developed and cross-reviewed the results; the coordinator independently reconstructed the main arguments. [Source ledger](SOURCES.json) · [Latest intake](../../../reports/astra-global-closure-20261124/round6/LATEST_INTAKE.md) · [Coordinator review](../../../reports/astra-global-closure-20261124/round6/ROOT_REVIEW.md).

## 1. Complete denominator cancellation along a prescribed orbit

Fix an ordinary positive source $n$, write $x_L=T^L(n)$, and let $p_L$ count its odd inputs through clock $L$. Repeat the first $L$ physical bits periodically. This gives two rational fixed points: the physical one and the companion one. Their raw clock differences are

\[
D_L=2^L-3^{p_L},\qquad D_L^*=2^{L+p_L}-3^L.
\]

Let $G_L,G_L^*$ be the **entire numerical gcds cancelled** when reducing those fixed points, including every prime-power multiplicity. The reduced denominators are $|D_L|/G_L$ and $|D_L^*|/G_L^*$.

For every fixed injective ordinary orbit, every $\epsilon>0$, and every fixed window length $H$, all sufficiently late intervals $[L,L+H)$ contain at most

\[
2\left\lceil\left(\frac{\log16}{\epsilon}\right)^2\right\rceil
\]

clocks with $\max(\log G_j,\log G_j^*)\ge\epsilon j$. The threshold depends on $n,H,\epsilon$ and is ineffective. Consequently both complete reduced denominators retain their raw logarithmic exponents in **upper Banach density along that same ordinary orbit**. This is stronger than a census of independently sampled parity words. The physical reduced denominator is also $\gg_n2^L$ at every sufficiently late clock, including exceptional ones.

The new mechanism is avoidance of every fixed algebraic curve by two rational points associated with each prefix. Siegel's theorem forces any curve containing infinitely many such integral points to have a genus-zero normalization with two punctures. The physical coordinate is then ruled out by its opposite valuations at 2 and 3. For the companion coordinate, the rational Laurent limit conflicts with the genuine dyadic scalar's irrationality on an escape, using the pinned PR182 theorem. Low-degree interpolation through the local targets now bounds several full gcds in one short window. A pairwise overlap debit retains all prime powers. No uniform integral-points theorem for a growing family of curves is assumed.

There is an all-positive-source consequence. For fixed $0<\epsilon<\log2$, the clocks of large cancellation have positive upper Banach density **if and only if the starting source itself is periodic**. If its least period is $r$, those clocks eventually coincide with $r\mathbb N$. A nonempty transient into a cycle has bounded cancellation in both coordinates; an escaping source has the bounded-cluster estimate above. This criterion does not prove that any source reaches a cycle or exclude another positive cycle.

The same analysis tracks the genuine scalar $\mathcal D(n)$. With $k_L=v_2(x_L-n)$, the periodically repeated prefix gives a rational scalar $r_L$ satisfying the exact eventual identity

\[
v_2(\mathcal D(n)-r_L)=L+p_L+k_L+p_{k_L}.
\]

Large $k_L$ occur at geometrically separated clocks. Hence the ratio of this agreement to $\log_2 d_L^*$ tends to one in upper Banach density. These remain approximations by wrong rational candidates on a hypothetical escape.

Xiao's almost-unit theorem gives an additional pointwise restriction. Fix any finite prime set containing 2 and 3 and any integer translate of the actual endpoint coordinate. A cancellation of size at least $\exp(\epsilon L)$ forces an exponentially large numerator part outside that prime set in every such fixed translate, at all sufficiently late relevant clocks. A small outside-prime part on a subsequence therefore forces subexponential full cancellation on that subsequence. No assertion that such a small part must always exist is made.

[Complete proof and definitions](arithmetic/README.md) · [Actual scalar, all-source criterion and cycle boundary](arithmetic/COMPANION.md).

## 2. Least-failure induction and finite even lifts of each fixed target

PR193's complete finite rewrite certificate reduces universal convergence to the directed implication $C(9s-1)\Rightarrow C(8s-1)$, where $C$ means eventual arrival at 1. We reconstructed the actual certificate: 291 leaves partition 995,328 residue bins, with 3,483 literal moves. Its intermediate directed edges may exceed the original source. Their parameters nevertheless satisfy $s<22n$. Thus a least failing parameter $r$ would force convergence of every $z>0$ with $22z<r$.

After ordinary normalization the remaining pair is

\[
A=4v,\quad B=8v+1,\quad v=9k+2,
\]

whose forward endpoints after two and three steps are $v$ and $9v+2$. The least-failure argument lets one discard any parameter for which an explicitly connected ordinary representative $w$ of the right arm satisfies $22w<r(v)$.

For an even lift $v=2^ma$, with $a$ odd, the two aligned endpoints are

\[
a,\qquad w=9\cdot3^{\lfloor m/2\rfloor}a+
\begin{cases}2&m\text{ even},\\1&m\text{ odd}.\end{cases}
\]

Writing $h+2=v_3(2^{m+2}a+1)$, survival of the least-failure cutoff forces a linear lower demand on $h$. Yu's rational $p$-adic logarithm bound, with prime 3 and bases $2,-a$, instead gives

\[
h+2\ll(1+\log a)\log(m+3).
\]

It follows that the even lifts still requiring a transfer satisfy the effective bound

\[
m\ll(1+\log a)\log(2+\log a).
\]

For each fixed convergent target $a$, only finitely many even exponents remain in this criterion. The cutoff grows with $a$; this is not a finite verification of all sources.

The odd lifts remain materially different. An explicit inverse ordinary path removes one arithmetic progression of their exponents for each admissible target. But already the fixed target $a=1$ leaves the family related to $3^{18j}-1$. The packet does not establish its convergence for all $j$.

There is also a complete graph obstruction to one natural proof strategy. For every $m\ge4$, infinitely many **both-convergent ordinary pairs** of these residual arms have $\max O(A)=A$, while every undirected shortcut path from $B$ to $A$ must pass through

\[
z=3^{m+1}a-1>(3/2)^m B.
\]

The proof constructs ordinary convergent sources on a synchronized finite binary cylinder, then uses a separating vertex in the full functional graph. It permits arbitrary reverse moves and paths of unbounded length. It rules out a fixed multiplicative height ceiling for connecting these two arms; it does not rule out paths to other smaller integers.

[Rank reduction and Yu application](head/README.md) · [Ordinary convergent forced-peak theorem](head/PEAK.md).

## 3. Pointwise residue routing at genuine completed marks

The elementary paired first-return word yields the inverse branch

\[
A_u(q)=\frac{2^uq-7}{9},\qquad u\ge6.
\]

Pair the outward exponents $E-t,t$, so every pair has the same total clock and carry $7\cdot2^t+63$. Complete divisibility reconstructs both ordinary paths, their intermediate integer, both odd counts and all required stopping marks. The full-period distribution of $2^t$ modulo 243 gives a finite inverse rule with constant degree and invariant ternary unit Haar measure.

Applying Korobov's prime-power exponential-sum estimate to the independent padding labels produces a **pointwise** theorem. For every positive ordinary $q$ coprime to six and every unit residue $a\bmod3^k$, there are actual sources $x\equiv a\bmod3^k$ taking $(x,5x)$ to $(q,5q)$ at exactly $2k$ completed blocks, one common odd count $4k$, and one common clock

\[
e\le\exp(Ck^{2/3}).
\]

The counts in every residue class equal the Haar share with relative error $O(3^{-k})$. This is uniform in the supplied ordinary endpoint, and all the constructed sources lie in one explicit relative real-height interval. The constructed inverse probabilities and the true marked-word weights are kept separate.

Combining this construction with PR200's existing pressure tree gives a further ordinary consequence. For each fixed target $q$, each unit residue class modulo $3^k$ contains at least

\[
X^{1/9}\exp\!\bigl(-O(\sqrt{\log X})\bigr)
\]

marked paired ancestors, up to a positive constant depending on $q$, simultaneously for $k\le c(\log\log X)^{3/2}$. They all lie in the fixed proportional shell $[48\cdot2^{-400}X/55,X]$. The proof first counts old ancestors at the reduced scale, then routes them at one common clock; different intermediate endpoints keep the resulting sources distinct. The power exponent is inherited from PR200, while the growing residue precision is new.

Independently, the repository's marked-gap tail implies a central completed symbolic row of mass $\gg1/(H\sqrt{\log(2H)})$ in each fixed multiplicative clock band. Appending that row after a residue router gives an explicit pointwise lower bound, but costs a factor $(N2^{-E})^{b+1}$ when the row has $b$ odd inputs. Its negative logarithm is much larger than $b$. Thus the present full-precision correction is too expensive to establish critical pressure. This calculation identifies exactly what a sparse-correction improvement must save.

[Pointwise theorem, Fourier proof and exact cost](renewal/README.md).

## Formal evidence and remaining universal obligations

| Module | Selected axiom inventories | Executed scope |
|---|---:|---|
| `arithmetic/PrefixInterpolation.lean` | 4 | Composite-ring local targets, clock overlap, rational interpolant existence and the full gcd product debit |
| `head/FixedTargetRays.lean` | 10 | Ordinary runs and arms, ternary rescue, least-failure induction and the arbitrary-path cut |
| `renewal/MarkedRouter.lean` | 7 | Paired first return, padded ordinary realization, integral pair splitting and whole-list residue decoding |

The [Lean runner](check_lean.py) compiles all three source modules in an empty project output directory and checks the selected transitive axiom inventories. Only the standard axioms `propext`, `Classical.choice`, `Quot.sound` are allowed. Existing Mathlib/package objects are reused and pinned in the receipt. The [finite runner](check_controls.py) replays the three exact checkers in normal and optimized Python against their frozen outputs. Analytic limits, Siegel, Xiao, Yu, Korobov, and the upstream stochastic inputs are outside this formal coverage.

The universal obligations are now concrete: an arithmetic contradiction must still rule out an escape and the final lap of every nontrivial positive cycle; the directed approach must still close the surviving original head implication; and the renewal approach must obtain enough completed-word mass at a prescribed ordinary point in the required physical-height range. Slow moving coefficients alone do not remove the cycle's algebraic degeneracy. A symbolic central average alone does not supply the prescribed ordinary point. The new results strengthen the three routes without asserting any of those missing implications.
