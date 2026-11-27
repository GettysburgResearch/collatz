# Pell rank, fixed ordinary pair fibers, and recurrence on head rays

**PROPOSED research checkpoint. Universal positive Collatz remains OPEN.** This continuation of PR193 combines the latest ordinary-source constructions with published primitive-divisor and unit-equation machinery. Its strongest unconditional counting statement is a uniform bound on physical odd transitions in a multiplicative coset. The paired and head-sampling theorems explicitly retain their manuscript and repository dependencies. The new Lean files certify finite arithmetic and counting deductions; they do not formalize the entire infinite argument.

We use the shortcut map
$$T(n)=\begin{cases}n/2&2\mid n,\\(3n+1)/2&2\nmid n,\end{cases}$$
and the accelerated odd map $U(x)=(3x+1)/2^{v_2(3x+1)}$. A positive odd unit is an odd integer prime to three. A multiplicative coset $t\Gamma\subset\mathbb Q_{>0}$ has rank $r$ when the rational span of its ratio valuation vectors has dimension $r$. The common scale, generators, number of primes in a generator, and sizes of primes are unrestricted.

## 1. An actual transition bound and a complete convergence class

Across all distinct positive odd sources $x$ prime to three, put $y=U(x)$. For every rank-$r$ coset,
$$\#\{x:xy\in t\Gamma\}\ \le\ B(r):=2^{r+1}(r+1).$$
In particular the same bound applies when both $x$ and $y$ lie in one rank-$r$ coset. This counts entire ordinary transitions with arbitrary stripping exponents. It is not a bound on symbolic words of a prescribed length.

The physical equation gives
$$ (6x+1)^2-DV^2=1,\qquad DV^2=12\,2^a xy.$$
Only $2^{r+1}$ squarefree discriminants can occur. At a fixed discriminant, the Pell solutions form a real Lucas sequence. First-appearance odd primes at its admissible indices give a triangular valuation matrix; consequently there are at most $r+1$ accepted indices. The proof handles the exceptional low Lucas indices and deletes the free valuation at two before using rank. [Full proof and published inputs](arithmetic/README.md)

With Hercher's published odd-period bound and Barina's published verification, a hypothetical nontrivial cycle must have **multiplicative affine rank at least 32 even among its adjacent odd-state products**. In particular at least 32 distinct primes divide its odd states. The exact comparison is
$$B(31)=137{,}438{,}953{,}472<137{,}500{,}000{,}000.$$
The stronger period floor uses Hercher's external computation. An independent rational-log/Farey enclosure with Barina's verification alone proves the weaker rank-at-least-31 conclusion. Neither external computation was repeated here.

For one fixed positive source, the proof also supplies convergence: if arbitrarily long odd-state windows put more than $3/4$ of their states in a rank-at-most-30 coset, the source reaches one. A rank-at-most-31 coset works with proportion greater than $4999/5000$. The coset may change with the window. Injective escape windows violate the global transition bound; a nontrivial periodic tail violates its complete-lap version. This covers an infinite class of sources, but its concentration premise has not been established for every source.

[Sparse subsets and arbitrary odd-clock gaps](arithmetic/WINDOWS.md) use Evertse–Schlickewei–Schmidt rather than assuming short physical gaps. [Actual joint head lines](arithmetic/HEADS.md) use Beukers–Schlickewei. [Global ordering attempt](arithmetic/GLOBAL_ORDERING.md) constructs arbitrarily long squarefree physical segments in which every edge is fundamental at a different discriminant, identifying what a stronger prime-ordering argument would have to overcome.

## 2. Near-linear actual pair fibers at every first target

For **each fixed** positive odd unit $y$ and every sufficiently large odd grade $p$, there is a clock $e=2p+O_y(1)$, a companion grade $p+k$, and a companion endpoint $Y$ such that at least
$$G\exp\!\bigl(-C_y\sqrt{p\log(p+2)}\bigr),\qquad G=2^e/3^p,$$
distinct ordinary units $x$ obey
$$T^e(x)=y,\quad T^e(5x)=Y,\quad p_e(x)=p,\quad p_e(5x)=p+k.$$
The first-arm real offset is at most $1/2$, $x\in[G(y-1/2),Gy]$, and $|k|+\log(Y+1)=O_y(\sqrt{p\log p})$. Thus every supplied first endpoint has an exact same-source companion fiber with exponent one. The endpoint $Y$ is selected by counting; it is not prescribed. [Proof, clocks, and dependencies](pressure/README.md)

Allowing separate near-critical clocks gives a fixed companion $u$ on unbounded scales. The stronger [inverse-ray selection](pressure/INVERSE_RAYS.md) fixes the same $u$ across infinitely many low-profile ordinary ancestors on a positive-probability set of actual scalar inverse rays. Its relative source mass is at least $\eta_a d_y$, with $\eta_a>0$ fixed along the selected rays. The constants come from disjoint level antichains, and the second-arm witnesses need not connect across levels.

The late PR201 head adds genuine initial paired recurrence to that same counted family: at least $c\sqrt p$ completed early ratio-five marks, while retaining the exact terminal pair and both grades above. [Combination at PR201 73a145c](pressure/LATE_PR201.md) states its additional fixed-total and renewal inputs. The terminal equality $Y=5y$ is still not obtained.

## 3. Sampling actual ordinary targets and the rank of the resulting families

Put $N_j(t)=\lfloor81^j t\rfloor$ for $7\le t<8$. Under the named fixed-target density and finite-grid fusion inputs, for almost every fixed $t$ the targets visited by infinitely many distinct $N_j(t)$ are **exactly the positive integers prime to three**. This holds on any preassigned infinite row subsequence, with positive upper frequency for each unit target. A sufficiently sparse common schedule gives positive lower frequency for every finite sequence of prescribed unit targets. These are different actual starting integers; no single trajectory is asserted to visit incompatible targets. [Sampling theorem and finite core](descent/README.md)

The actual translated head families from PR197 have first-coordinate ratio rank at least
$$\exp\!\left(c_A d/(\log(d+2))^{12}\right).$$
An elementary smooth-divisor count on their short arithmetic progression yields the bound. Positive-density fixed-endpoint source pools have polynomial rank in their source scale. Moreover one exact pair of clocks and grades simultaneously retains both near-linear multiplicity and polynomial rank. These results show directly why fixed endpoints alone cannot provide the low-rank premise in section 1. [Rank proof and cross-review](descent/RANK_AND_RAYS.md)

If there is a nonconvergent component, every sufficiently high row window $[s,\lceil e^{Ds}\rceil]$ carries a positive amount of the genuine scheduled four-suffix disagreement of PR197. This strengthens mere divergence of that series. The attempted positive-entropy rigidity transfer is also computed explicitly: the natural circle extension is Haar measure times a constant component bit, and the sparse sampling entropy does not couple those bits. No opposing upper bound on the moving block masses has been proved.

## 4. Lean, evidence, and the remaining universal step

The three new Std-only modules are [RankWindows](arithmetic/RankWindows.lean), [ClockTransfer](pressure/ClockTransfer.lean), and [HeadSampling](descent/HeadSampling.lean). The execution record audits every public theorem, including the triangular valuation lemma, Pell identities, numerical cycle implications, actual clock transfer, target transport, and simultaneous rank/count selection. [Kernel and exact controls](../../reports/astra-deep-closure-20261124/kernel/CHECKS.json) · [coordinator review](../../reports/astra-deep-closure-20261124/ROOT_REVIEW.md)

The literature is used at explicit hypotheses: real Lucas primitive divisors, finite-rank unit-equation counts, linear forms in two logarithms, and the cited recent scalar inverse and passage results. [Source ledger](SOURCES.json) records those dependencies. [Repository intake](../../reports/astra-deep-closure-20261124/PR_INTAKE.json) and [head refresh](../../reports/astra-deep-closure-20261124/HEAD_REFRESH.json) distinguish inventory from mathematical review. Prior Lean packets were not rebuilt.

Full closure would require an additional ordinary-source implication: a universal low-rank concentration mechanism, a prescribed anchored companion state of sufficient mass, or an upper bound contradicting the scheduled disagreement lower bound. The current constructions do not establish one of these. They give complete written proofs at the stated scope and finite Lean certificates, without replacing the missing implication by an assumption of independence or by changing the fixed integer.
