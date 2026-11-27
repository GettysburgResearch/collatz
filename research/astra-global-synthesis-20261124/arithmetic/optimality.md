# When a corrected clock forces the actual minimum orbit

**PROPOSED.** Assume the ordinary nonperiodic orbit and full synchronous classes of [the forward-section packet, §§3–4](../section/proof.md), SHA-256 `cbe95e8adf39ccf90253573005350260ee6ea0d67cb10c206108cbb624c59a02`. We use its convergent class correction envelope and its least-unit representatives. No eventual periodicity of the physical orbit, pointwise bound on its heights, or unproved ordinary realization of a word is assumed.

**Result.** Suppose the actual class-minimum corrected clocks eventually take only the values 1 and 2, with at least two 1s between consecutive 2s. Then, for every sufficiently late $i$, the least ordinary units themselves obey $U(n_i)=n_{i+1}$ with literal valuation $a_i$. All strict replacements cease. Consequently an escaping source cannot have an **eventually periodic** corrected clock satisfying this spacing condition. The elimination of replacements itself allows an arbitrary, nonperiodic layout of the spaced 2s.

## 1. Absolute rather than relative control of all minimum-height units

Use the positive odd map $U(x)=(3x+1)/2^{v_2(3x+1)}$. At sufficiently late indices the section proves that $M_i=M(n_i)$ is the least corrected height over all ternary units of $C_i$, $M_{i+1}=3M_i/2^{a_i}$, and $1\le e_i=v_2(3n_i+1)\le a_i\le b(n_{i+1})\le4$. Here $b$ is the smallest valuation of a ternary-unit predecessor of the specified target. For each $z\in C_i$, $M(z)/z\to1$ uniformly as $i\to\infty$, and $M(Uz)=3M(z)/2^{v_2(3z+1)}$. A positive odd unit stays a unit. Distinct minima satisfy $\sum 1/n_i<\infty$ by the class packing theorem.

Put

$$B_i=\frac13\sum_{k\ge0}\frac{M_i}{M_{i+k}}
=\frac13\sum_{k\ge0}\frac{2^{A(i,k)}}{3^k},\qquad A(i,k)=\sum_{j=0}^{k-1}a_{i+j}.$$

The first sum converges because $M_j>n_j$ and $M_i$ is fixed. The equality comes directly from the corrected clocks. The recursion is $B_i=1/3+(2^{a_i}/3)B_{i+1}$.

Every ordinary unit $z\in C_i$ at corrected height $M(z)=M_i$ satisfies

$$ 1 < M_i-z\le B_i. \tag{1} $$

Indeed for $E_k$ the cumulative **actual** valuations at $z$, the ordinary affine formula is

$$\frac{2^{E_k}}{3^k}U^k(z)=z+\frac13\sum_{j<k}\frac{2^{E_j}}{3^j}.$$

The left side is $M_i U^k(z)/M(U^k(z))$, which tends to $M_i$ by the uniform envelope on the original classes $C_{i+k}$. Also $2^{E_j}/3^j=M_i/M(U^j(z))\le M_i/M_{i+j}$. This proves the upper bound. Since $E_j\ge j$, the lower sum is at least $(1/3)\sum_{j\ge0}(2/3)^j=1$. Equality would require every actual valuation to equal one. A run of $k$ ones implies $2^k\mid(z+1)$ because $2^k(U^k(z)+1)=3^k(z+1)$. No positive integer has such runs from the same start for every $k$. Thus the lower bound is strict.

In particular if $B_i\le3$ the height $M_i$ has a **unique** ordinary unit representative: two different odd integers differ by at least two and cannot both lie in the interval from (1). This is a sufficient test on the *corrected* future clocks, independent of any bound on the unknown time at which the two test sources synchronize.

## 2. Eliminate every strict replacement in the spaced sector

In each length-$k$ prefix of any sufficiently late tail there are at most $\lceil k/3\rceil$ twos. Termwise the series for $B_i$ is bounded by that for the periodic majorant $2,1,1,2,1,1,\dots$, including when there is no subsequent two. Its exact value is

$$B_i\le\frac{1+4/3+8/9}{3(1-16/27)}=\frac{29}{11}<3.$$

At a clock two, the next two clocks are both one; applying the recursion for $B-1$ at these ones gives $B_{i+1}-1\le(2/3)^2(18/11)=8/11$. All sufficiently late minimum heights now have a unique ordinary representative. At a clock one, $e_i=1$, so the literal successor $U(n_i)$ is a unit at height $M_{i+1}$ and must equal $n_{i+1}$.

Consider a sufficiently late clock two. The preceding clock is one, hence its actual edge gives $3\mid n_i+1$. Put $r_j=n_j+1$ and $\eta_j=M_j-r_j$. By (1), $0<\eta_j\le B_j-1$. The even integer

$$Q=3r_i-4r_{i+1}=4\eta_{i+1}-3\eta_i$$

lies between $-54/11$ and $32/11$, so $Q\in\{-4,-2,0,2\}$. Now $4r_{i+1}\equiv-Q\pmod9$. The alternatives $Q=-4$ and $Q=2$ respectively put $n_{i+1}$ at 0 and 3 modulo 9, contrary to being a unit. The alternative $Q=0$ gives $n_{i+1}\equiv8\pmod 9$. Then $(2n_{i+1}-1)/3$ is a positive odd unit predecessor, whence $b(n_{i+1})=1$, contradicting $a_i=2\le b(n_{i+1})$. The only remaining value $Q=-2$ gives $3n_i+1=4n_{i+1}$. Its target is odd, so the valuation is exactly two. This proves the result about every late edge.

The $n_i$ lie in pairwise distinct classes. If the corrected clocks on this sector were eventually periodic with positive period $l$, two different late ordinary $n_i,n_{i+l}$ would share their entire future valuation word by the preceding proof. Equal prefixes with cumulative clock $E_k$ imply $2^{E_k+1}\mid(n_i-n_{i+l})$, by the finite affine cylinder lemma (the terminal parity bit is included). As $E_k\ge k$, the fixed integers must coincide, a contradiction. This proves the complete exclusion of the eventually periodic sector, regardless of the period length.

**Remaining global question.** The full optimality bounds admit clocks 3 and 4, clusters of 2s, and nonperiodic tails. For instance the periodic clock $2,1,2,1,\dots$ gives $B_i=7$ at a two, so (1) alone does not give the uniqueness used above. This is arithmetic of a proposed clock, with no ordinary counterexample asserted. Even on the spaced sector the result permitting a nonperiodic ordinary minimum path does not prove that such a path escapes or converges. The conjecture remains open.

**Verification scope.** `OptimalReset.lean` checks the integer rounding and residue implication at a clock two, the incoming clock-one residue, and the unit inverse at 8 modulo 9, using only Lean's standard distribution. The infinite class estimate, series identity, uniqueness argument and periodic contradiction are written proofs.
