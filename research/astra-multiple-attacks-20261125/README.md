# Carry arithmetic, additive mixing, and ordinary descent

**PROPOSED research packet. Universal Collatz convergence remains OPEN.** This packet develops three mathematical attacks and a subsequent attempt to combine them into a proof. It includes seven new Lean modules with 29 public theorem declarations. The source-qualified Subspace Theorem deductions and analytic estimates below are written proofs; the Lean files formalize the specified finite identities, ordinary inverse bounds, and certificates. No theorem in this packet proves convergence of every positive integer.

Throughout, the physical map is the shortcut

$$
T(n)=\begin{cases}n/2&2\mid n,\\(3n+1)/2&2\nmid n,\end{cases}
\qquad P_N(a)=\#\{0\le j<N:T^j(a)\text{ odd}\}.
$$

The starting repository head is `aa0b01234735683b413098b81afdf764de503730`. A fresh inventory covered 169 pull requests; the scientific intake concentrated on the changed heads of PR195, PR192, PR201, PR197, and the new PR210. Exact source identities and the scope of inspection are in [SOURCES.md](SOURCES.md) and [the intake receipt](../../reports/astra-multiple-attacks-20261125/INTAKE.json). Those proposals are not silently incorporated into the accepted baseline.

## 1. A carry lower bound for every ordinary source

Define the integer carry by

$$
2^N T^N(a)=3^{P_N(a)}a+C_N(a).
$$

Fix any finite set of primes $S$ containing 2 and 3. For a nonzero rational number with denominator supported on $S$, let $H_S$ be the part of its reduced numerator supported outside $S$, with multiplicities, and set $H_S(0)=1$. The [arithmetic proof](arithmetic/README.md) gives, for every $\epsilon>0$, a threshold depending only on $S,\epsilon$ such that

$$
             a\,H_S(C_N(a))\ge2^{(1-\epsilon)N}
             \quad\text{for every }a\ge1.
$$

This is uniform over all ordinary sources. If $a\le\exp(AN)$, the stronger left side $2^{v_2(a)}H_S(a)H_S(C_N(a))$ suffices, with the threshold also depending on $A$. In particular the carry alone has this lower bound for starts $a=3^r$ with $r=O(N)$. The exponent one is sharp, as the ordinary cycle from 1 shows.

The proof applies the $S$-adic Subspace Theorem to the actual source and normalized carry. Small outside-prime mass forces a fixed rational line. Positivity and the exact dyadic divisibility exclude that line at unbounded clocks. This uses no classification of the parity word. The analytic theorem has an ineffective onset; its elementary line-divisibility step is formalized in [BalancedWindows.lean](arithmetic/BalancedWindows.lean).

### Two windows on the same hypothetical escape

For one injective positive orbit $x_j=T^j(x)$, compare the first $N$ parity steps from $x$ with those from $x_q$. Partition their normalized carry discrepancy into at most a fixed number $K$ of arbitrary time sets, giving rational sums $Y_I$. The same arithmetic proof gives

$$
\liminf_{q,N\to\infty}
\frac{\log_2(x_q+1)+\sum_I\log_2 H_S(Y_I)}{N}\ge1.
$$

The sets need not be intervals, and the two words need not have equal odd counts. A separate argument proves $H_S(U_N(x_q)-U_N(x))\ge2^{N-o(N)}$ at every fixed positive shift $q$ on that orbit. Here $U_N=C_N/3^{P_N}$. The ordinary source is retained in both comparisons.

If the two windows differ only on at most $K$ intervals, with equal odd counts in each paired interval and total changed physical length $L$, the consequence is

$$
\liminf\frac{\log_2(x_q+1)+(\log_2 3)L}{N}\ge1.
$$

The [symbolic applications](arithmetic/APPLICATIONS.md) use the balanced-pair construction of Kebis, Luca, Ouaknine, Scoones, and Worrell to exclude escaping positive realizations of arbitrary nonerasing physical encodings of every $k$-Bonacci word, and of the other substitutions under their stated coincidence hypotheses. A second application allows multiple irrational-rotation channels with different physical block lengths and a time-dependent order. These are consequences for specified symbolic systems, not a classification of arbitrary ordinary parity words. The [cycle comparison](arithmetic/CYCLES.md) explains why full-lap carry divisibility is compatible with the prime-mass bound.

## 2. Fourier cancellation for actual orbit labels

The [global proof](global/README.md) treats a Boolean label $b$ satisfying $b(2n)=b(n)$ and the odd-edge equation $b(2n+1)=b(3n+2)$ with finitely many exceptions. It assumes the cited ordinary adjacent-merger estimate, which gives $V(B)=\sum_{n<B}|b(n+1)-b(n)|\ll B/\sqrt{\log B}$. With the actual row mean $p_N=N^{-1}\sum_{n<N}b(n)$, it derives

$$
\sup_{t\in\mathbb R}\sup_{I\subset[0,1]\text{ interval}}
\left|\sum_{\substack{n<N\\n/N\in I}}(b(n)-p_N)e^{2\pi int}\right|
\ll_b\frac{N}{(\log N)^{1/96}}.
$$

The bound includes frequencies varying with $N$. At zero frequency the exponent improves to $1/16$. The proof combines ordinary row inequalities with a quantitative approximation to $\log 3/\log 2$ and averaging over nearby multiplicative dilations. It assumes no limiting density for $b$.

Together with the cited positive lower density theorem for each fixed ternary-unit target, the bound gives a positive proportion of ordered pairs whose three actual starts $x,y,x+y$ visit any three specified odd targets prime to three. This applies even to target basins that are disjoint. Its dependence on freely chosen summands is essential: for targets $5,5,85$, the exact diagonal $x=y$ has no such pair, and every subpolynomial-width band around that diagonal has vanishing relative frequency. The exact diagonal obstruction is checked in [TargetDiagonal.lean](global/TargetDiagonal.lean).

For a hypothetical nonconstant bad label, the same proof forces the symmetric triangular Fourier polynomial to have $L^1$ norm at least $c_b(\log N)^{1/96}$ for every sufficiently large $N$. The previously proved upper bound still permits this growth. The [component Gram construction](global/COMPONENT_GRAM.md) separately identifies which natural averages lose the information about one fixed bad source. No fixed-source contradiction follows from the mixing estimate alone.

## 3. All smaller rivals, with unrestricted clocks

The [descent proof](descent/README.md) and [SurplusProperness.lean](descent/SurplusProperness.lean) prove the following order of quantifiers:

$$
\forall I,D\ \exists H\ \forall h\ge H,\ x=3^h a,\ a\ge2\cdot3^D,
$$

$$
i\le I,\quad2^i\mid x+1,\quad y<x,\quad T^j(y)=T^i(x)
\quad\Longrightarrow\quad P_j(y)>i+h+D.
$$

The rival clock $j$ is unrestricted. The proof extracts a literal ordinary path between bounded integers from any proposed cheaper merger, while retaining at least $h$ odd departures and a bounded normalized inverse cost. A fixed endpoint admits only finitely many such grades, even when its orbit is not known to converge. The finite maximum closes the contradiction.

The later endpoint can behave completely differently. For every odd positive $x$ divisible by 243, the smaller positive triple

$$
                  w=192(x/243)-3
$$

reaches $(x-1)/2$ in seven shortcut steps, with exactly four odd departures. [MersenneCertificates.lean](descent/MersenneCertificates.lean) includes this formula, its exact work, and a consumer for the resident certificate checker when the two actual components meet.

On the family $x=2^m-1$, $m=2\cdot3^{h-1}$, with even $h\ge102$, every smaller ordinary start reaching upper clock $m+1$ uses more than $m+h+8$ odd departures. At upper clock $m+2$, the displayed smaller triple reaches the same endpoint using exactly $m+4$ odd departures. The native upper arm has grade $m$ at both sites, and $x/3$ reaches 1. The general all-$I,D$ theorem and the explicit certificate are kernel-checked. The numerical threshold 102 uses the separate exact finite replay of the seeds below $3^8$, not a Lean evaluation of that enumeration.

This forces a proposed universal selector to account for endpoint changes. It does not prove that an arbitrary least bad triple ever reaches a certified endpoint. The resident [FinalProposal.lean](../astra-closure-20261125/FinalProposal.lean) still has its explicit source-coverage hypothesis.

## 4. Attempts to finish the cycle and escape arguments

The [cycle synthesis](synthesis/CYCLE_CLOSURE.md) bounds the gcd of a proper physical arc carry with the complete lap determinant. It also constructs actual positive rational cycles with irreducible, undilated rank polynomials of degree $p-1$. The [moving-rank theorem](synthesis/SINGLE_RANK_RESULTANT.md) gives

$$
\log\gcd\left(2^h-3^p,\ Q_s(u)\right)=O(p^{5/6}),\qquad
Q_s(X)=2\sum_{i=0}^{p-1}X^i-X^s,
$$

uniformly in the changing interior rank $s$, under the stated coprime near-critical clock hypothesis. Two short relations and the finite-rank unit-equation theorem of Evertse, Schlickewei and Schmidt produce a nonzero resultant. The full denominator therefore remains exponentially large on this family despite its irreducible factor having the largest possible degree. An arbitrary rank mask still lacks the identity used to obtain the second relation.

The [escape synthesis](synthesis/README.md) works with all predecessor branches entering one hypothetical escaping odd orbit $a_j$. Let $d_a$ be the relative natural density of odd starts that reach $a$, and put $r_j=1-d_{a_{j-1}}/d_{a_j}$. For some absolute $q_*<\theta=H_2(\log_3 2)$, it derives

$$
                         \sum_j r_j^{q_*}<\infty.
$$

The complete reverse-transition entropies are summable as well. The proof uses one setwise first-landing estimate for the entire union of branches and the cited uniform interval-compression theorem. A lower floor of order $(\log(2+a_j))^{-1/\theta}$ on a positive-upper-density set of odd clocks would contradict it; no such floor is proved here. A separate deterministic deduction shows that at density-one odd clocks $j$, every positive start $x\le j^{1/\theta}$ reaching $a_j$ has already visited $a_{j-1}$, at arbitrary arrival times. The exponent $1/\theta$ is approximately 1.0527. The final corollary treats entries to one chosen ray in every escaping component and all periodic cycles simultaneously.

Each note states its exact imported results and its first missing inequality. These efforts do not insert their open closing steps as premises disguised as proved Lean lemmas.

## Evidence and reproduction

The fresh [Lean receipt](../../reports/astra-multiple-attacks-20261125/LEAN.json) covers all seven new modules, their three resident imports, and all 60 public theorem axiom inventories: 29 new and 31 imported. Only `propext`, `Classical.choice`, and `Quot.sound`, or subsets, appear. The build used Lean 4.34.1, a fresh cache for project modules, and the pinned existing Mathlib cache. It did not rebuild Mathlib or formalize the imported analytic theorems.

Run the driver with the paths to those installed dependencies:

```sh
python -B research/astra-multiple-attacks-20261125/check_lean.py \
  --lean /path/to/lean-4.34.1/bin/lean \
  --mathlib /path/to/pinned/mathlib4 \
  --receipt /path/outside/checkout/LEAN.json
```

Mathlib source pin: `d13f23b723b8a846827a245b89c10fc7d3f11612`.

The [finite receipt](../../reports/astra-multiple-attacks-20261125/FINITE.json) contains 2,560 actual two-window arithmetic comparisons; four unequal-length rotation controls; and the exact small-seed replay over 454,255 positive seed/clock pairs. Each script was run normally and with `-O`, with byte-identical output. These are finite controls for the stated formulas and the numerical refinement.

The [root reconstruction](../../reports/astra-multiple-attacks-20261125/ROOT_REVIEW.md) records the analytic review boundaries and the independent lane reviews. The source manifest and clean-checkout publication receipts bind the work to the committed files. Repository validation checks integrity and selected bounded regressions; it is not a proof of universal convergence.
