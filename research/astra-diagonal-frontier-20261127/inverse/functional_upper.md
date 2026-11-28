# The upper functional iterated-logarithm law at a specified ordinary root

Fix a positive odd integer $a$ coprime to three. On its canonical ordinary inverse chain $P_{h,a}$ write $S_j$ for the total of the first $j$ actual gaps and $D_j=S_j-2j$. Interpolate $Z_n(t)=D_{nt}/\sqrt{n\log\log n}$ linearly on the integer clock. Under the averaged joint Syracuse mixing assumption (J) and the fixed-root inputs below, $(Z_n)$ is almost surely relatively compact in $C[0,1]$. Its full cluster set is
\[
  \{f:f(0)=0,\ f\ {\rm absolutely\ continuous},\
                                \int_0^1 |f'(t)|^2\,dt\le4\}.       \tag{1}
\]
In particular the two scalar iterated-logarithm limits superior and inferior are $2$ and $-2$. The same assertions hold under the natural inverse entrance law $Q_a$ at each nonperiodic positive odd unit. The assertion concerns one supplied ordinary root and its actual inverse paths. The lower inclusion is proved in the accompanying [lower functional law](functional_lower.md). Here is the matching upper bound.

The external inputs are (J) in the outward order of Paper 211, its monitored mixing calculation (A.6), the finite specified-root density bound and canonical path Cesàro identity of Paper 12, and the earlier fixed-root upper estimate $D_n=O_\omega(\sqrt{n\log\log n})$. The latter implies $S_n/n\to2$ and will also control the small interval at the origin. No uniform bound on the terminal canonical profile is used. [Weaver, Paper 211 v1, Appendix A, particularly (A.6)](https://rstation.ai/problems/collatz/papers/211/v1) · [Weaver, Paper 12 v1, (18), (19), (26) and (29)](https://rstation.ai/problems/collatz/papers/12/v1) · [Earlier ordinary upper bound and equivalence of path laws, commit aa686899](https://github.com/GettysburgResearch/collatz/blob/aa6868996f6f30b12d91c367f7c6edcfd93784b2/research/astra-six-hour-20261127/escape/CANONICAL_INVERSE_PATHS.md).

## A pointwise counting inequality

For an outward word $w=(e_1,\ldots,e_d)$ put $\omega=3^d2^{-S_d}$ and $\beta_w=\sum_{i=1}^d 3^{i-1}2^{-S_i}$. The terminal ancestor $b=(a-\beta_w)/\omega$ is a positive odd integer whenever the full known residue condition $a=\beta_w\bmod 3^d$ holds. Dividing at each stage proves integrality and positivity, and the numerator of an integral step $(2^e x-1)/3$ is odd. For fixed $d,S_d=s$, all weights equal $\omega$ and the terminal integers are distinct, by the deterministic forward trajectory from each $b$. Also $0<b\le a/\omega$. Hence on any subfamily with this fixed total,
\[
  \sum_w \omega\,|F(b\bmod3^q)|
         \le (a+\omega3^q)\langle |F|\rangle_q.                    \tag{2}
\]
Indeed each residue occurs at most $a/(\omega3^q)+1$ times. Here the mean is uniform on all $3^q$ residue classes. The subfamily can include conditions on the entire initial word.

If $1.9d\le s\le3d$ and $q\le0.12d$, then $\omega3^q\le1$ because $1.12\log3<1.9\log2$. Thus (2) costs at most $a+1$ per group. The proof compares residues only after retaining the actual ordinary endpoint of the already exposed word.

## Comparison for marked partial sums

Fix $0<\gamma<1$, and put $G_I=\{1.9d\le S_d\le3d\text{ at every integer }d\ge I\}$. Almost every canonical path belongs to some $G_I$. Let $v$ be any real threshold and use deterministic integer dates in $[\gamma n,n]$. We need either of the following tests $T_n$.

1. A fixed finite linear functional $\sum_{i=1}^r c_iD_{p_i}\ge v$, with real coefficients fixed independently of $n$.
2. A running increment $\max_{p\in J}\sigma(D_p-D_s)\ge v$, where $\sigma\in\{-1,1\}$, $s\le \min J$ and $J\subset [\gamma n,n]$ is any finite collection of integer dates. In particular $J$ may contain every date in an interval.

Write $T_n(v-w)$ for the same functional with threshold $v-w$. Give the letters of the comparison path independent masses $\Pr(e)=2^{-e}$, writing $\Pr_0$ for this law. For every $B>0$ there are constants such that for every fixed $I$, and all sufficiently large $n$ (so $\lfloor0.9\lfloor n^{1/10}\rfloor\rfloor\ge I$),
\[
 P_{h,a}(G_I\cap T_n(v)) \ \le\
     C_a\Pr_0(T_n(v-C n^{1/3}))+O_{a,\gamma,B,r,c}(n^{-B}).       \tag{3}
\]
Here $C$ depends on $\sum|c_i|$ in case 1 and is absolute in case 2. The constants do not depend on the threshold, the particular dates, or the padded depth used below.

**Projected densities.** On $j$ independent letters use the residue $\beta_j\bmod3^x$ of the outward word, and use the density $3^x$ times its probability with the prescribed checks, with respect to uniform measure on $\mathbb Z/3^x$. This normalization is $3/2$ times the corresponding sum over total slices in Paper 211. Projection commutes with restriction to any full-word event, and $\beta_j\bmod3^x$ is determined by the first $x$ letters for $j\ge x$. For a tail of $t$ letters, a bounded test of centered sums at dates either $\le u<k$ or $\ge q$, $k\le q\le t$, gives residual subdensities $R_k,R_q$ satisfying
\[
      \langle |R_q-R_k\circ p_{q,k}|\rangle_q
                      \le {\rm JOsc}_{k-u,q-u}\le J_b(k-u)^{-b}      \tag{4}
\]
for every $b>0$. This is (A.6) with all totals, using the triangle inequality and increasing finite partial sums of the positive measures. The proof also applies to a joint test of these dates. Conditional on the actual first $u$ letters and total of the next $q-u$, its conditional probability over the remaining letters is a coefficient in $[0,1]$. It depends on the middle letters only through their total, even when the test compares a past and a future date. The fibre-oscillation proof of (A.6) then gives (4) directly. There is no independence assumption on the canonical inverse gaps.

Fix an arbitrary padded depth $j\ge3n$, and start at precision $Q=\lfloor n^{1/10}\rfloor$. Write $\ell=\lfloor n^{1/5}\rfloor$ and $b_n=n^{1/3}$. At the start replace every used date $p$ by $p+2\ell$. When the precision reaches $x=p+\ell$, switch it to its true date $p$. An unswitched date has an independently allowed numerical perturbation in $[-b_n,b_n]$, and a switched date has perturbation zero. The active test is that some allowed choice of perturbations makes the original comparison true. For the linear test the slack is $b_n\sum_{\rm unswitched}|c_i|$. For the maximum it is enough to consider only the two coordinates of each candidate increment. A repeated date is a single coordinate. The trivial candidate $p=s$ is identically zero.

At each precision $x$ from $Q$ onward expose the prefix of length $d=\lfloor0.9x\rfloor$, retaining the condition $1.9d\le S_d\le3d$ on that length and all earlier exposed lengths starting at $\lfloor0.9Q\rfloor$. If $d$ has increased since the previous precision, this exposure with the active event fixed is an exact deletion of nonnegative density. Perform any scheduled switch, then lift with the prefix family and active test held fixed. At the terminal precision complete any required exposure. A path in $G_I$ satisfying the original comparison meets all the final requirements.

**Cost of one lift.** At $x$ put $k=x-d$, $q=x+1-d$. For large $n$, $q\le0.12d$. Evaluated at the prescribed root $a$, the density before this lift is the sum over compatible retained prefixes of $\omega$ times the residual density at their actual endpoints modulo $3^k$. The analogous formula with residual precision $q$ holds after lifting. This follows by conditioning on the independent prefix: its probability $2^{-S_d}$ times the factor $3^d$ for its known residue gives $\omega$, and the affine map $z\mapsto\beta_w+\omega z$ identifies the remaining residue with that of the actual endpoint. Both formulas use the same event on $j$ letters.

Group the prefixes by $S_d$ and the information about already exposed marked dates required for the test. A fixed linear functional needs the values of the at most $r$ already exposed marked sums. For the maximum it suffices to retain the start value if exposed and the maximum of the already exposed signed candidate sums, with flags for empty groups. If an exposed coordinate could carry slack, record separately the two maxima with and without slack. Each stored centered sum, and each such maximum, is an integer of absolute value at most $3d$ since $S_d\le3d$. The set of date positions and their switch statuses are deterministic. Thus at most $O_r((d+1)^{r+1})$ groups suffice for the linear test and $O((d+1)^4)$ for the maximum. The residual test within each group is common to every prefix because future centered sums equal $D_d$ plus a residual centered sum.

After switching, every used date in the residual tail is either at least the new precision $x+1$ on the full clock, or at most $x-\ell$. In (4) take $u$ as the last such past tail date relative to $d$, or zero if none. In the active range $x\in[\gamma n/2,2n]$, $k-u\ge\ell$ for large $n$. Applying (2) to the signed residual differences and then (4) costs at most $O_{a,r}(n^{r+5}J_b\ell^{-b})$ for the sum over all active lifts, enlarging the polynomial to cover both kinds of tests. Below this range every mark is future. Above this range every mark is inside the retained prefix, so its full test is a single Boolean filter. In both cases groups indexed by $S_d$ alone suffice after filtering, and (4) can use $u=0$, $k\ge x/10$. The total for all these lifts, including arbitrarily large $j$, is at most $C_aJ_b10^b\sum_{x\ge Q}(x+1)^{1-b}$. An arbitrarily large fixed $b$ makes both contributions $O(n^{-B})$.

**Cost of switching.** At $x=p+\ell$ the old perturbed test contains the new test except possibly when $|D_{p+2\ell}-D_p|>b_n$. Both dates are in the unexposed tail since $p=x-\ell\ge d$ for large $n$. Discard every other part of the test to bound this extra subdensity. For fixed $S_d$ the residual bad density at precision $k$ has Haar mean at most $2\exp[-\min(b_n^2/(24\ell),b_n/8)]$, by the elementary centered geometric bound (A.3). By (2) it costs at most this bound times $(a+1)O(n)$ at that switch. There are at most $n+1$ switches. Thus the change in the required upper bound is $O_B(n^{-B})$. This accounts for all dates of a running maximum without paying for them in the leading fair probability.

**Starting precision and terminal trace.** At $Q$, discard all selection restrictions. The total density of the first $Q$ letters at $a$ is $\rho_Q(a)\le C'_a$. The part with $S_Q>Q^2$ has density at most $3^Q\Pr_0(S_Q>Q^2)=O_B(n^{-B})$ by the geometric moment generating function. Conditional on any remaining prefix in the projected density, all letters after $Q$ are independent and fair. Couple these letters to the tail of a wholly fair path with a new independent first $Q$ letters. Outside a further $O_B(n^{-B})$ exceptional probability, its own $S_Q\le Q^2$, so changing the initial prefix shifts every later centered sum by at most $Q^2$. On the fair path, all increments $D_{p+2\ell}-D_p$ used in the initial checks have absolute value at most $b_n$ outside $O_B(n^{-B})$, by the same bound and at most $n+1$ dates. Thus the base density is at most $C'_a\Pr_0(T_n(v-Cb_n))+O_B(n^{-B})$, since $Q^2=o(b_n)$. For the linear test one may take $C=4\sum_i|c_i|$; for the maximum $C=8$ suffices.

At precision $j$ the final density bounds the sum of $3^j2^{-S_j}$ over all retained compatible words satisfying $T_n(v)$; we may include terminal multiples of three. Under $P_{h,a}$ a compatible unit word has probability $3^j2^{-S_j}h(X_j)/h(a)$. Therefore, for $E=G_I\cap T_n(v)$,
\[
 \mathbb E_{h,a}\big[1_E\,\rho_1(X_j)/h(X_j)\big]
       \le \frac{2}{h(a)}\,(\text{final projected density at }a).
\]
Here $0\le\rho_1\le2$. The bound is uniform in every $j\ge3n$. Average it over $j$ and apply Paper 12 (29) for the full event $E$. This proves (3).

## Moderate deviations and compactness

Use horizons $n=2^m$ at first, and $z_n=\sqrt{n\log\log n}$. The fair centered geometric cumulant function satisfies $\log\mathbb E_0 e^{\theta(e-2)}=\theta^2+O(|\theta|^3)$ near zero. For a partition $0=t_0<t_1<\cdots<t_r=1$ with rational vertices and any rational vector $(\lambda_i)$, put $V=\sum_i(t_i-t_{i-1})\lambda_i^2$. Every $u>2\sqrt V$ satisfies
\[
 \Pr_0\!\left(\sum_i\lambda_i(D_{\lfloor nt_i\rfloor}-D_{\lfloor nt_{i-1}\rfloor})
                      \ge u z_n-O(n^{1/3})\right)
       \le \exp[-(u^2/(4V)+o(1))\log\log n]                         \tag{5}
\]
when $V>0$. In exponential Markov take $\theta=u z_n/(2nV)$ and sum the independent log moment generating functions. The rounding contributes $O(\theta^2)$ and $n|\theta|^3=o(1)$. The zero vector requires no estimate. Time zero has deterministic value zero and is omitted from the marks. By (3) and (5) the upper-test probabilities intersected with each $G_I$ are summable over $m$. Countable Borel–Cantelli, then the union over $I$, give every rational functional upper bound $2\sqrt V$ on the corresponding limit values.

For equicontinuity fix a rational $\gamma>0$ and a tolerance $\eta>0$. Cover $[\gamma,1]$ by finitely many consecutive tiles of length at most $\Delta$. For integer start $s$ of each tile, the unconditioned fair maximal exponential inequality, applied to both signs through $\Delta n+2$ letters, gives
\[
 \Pr_0\big(\max_{p\ {\rm in\ tile}}|D_p-D_s|
                           \ge \eta z_n-O(n^{1/3})\big)
       \le 2\exp[-(\eta^2/(4\Delta)+o(1))\log\log n].               \tag{6}
\]
This follows from the same positive exponential submartingale and local cumulant expansion, now with length bounded by $\Delta n+2$. Choose $\Delta$ small enough that its exponent exceeds one. Use (3) on both signs of the whole tile, retaining all its dates in one comparison, and apply Borel–Cantelli as above. Tile boundary rounding or linear interpolation adds at most the oscillation within the adjoining tiles. With a regular mesh, points separated by at most half a mesh interval meet at most two such tiles. Their differences are bounded by $4\eta$ after normalization. Intersect over rational parameters tending to zero. At the origin the previously proved fixed-root estimate gives $\limsup_{n\to\infty}\sup_{j\le\gamma n}|D_j|/z_n\le C_\omega\sqrt\gamma$. This supplies equicontinuity on the full interval. Together with $Z_n(0)=0$ it gives almost sure relative compactness on dyadic horizons.

On any uniform dyadic subsequential limit $f$, the linear functional inequalities from (5) extend from rational to arbitrary real coefficient vectors by continuity. Optimizing the vector gives $\sum_i(f(t_i)-f(t_{i-1}))^2/(t_i-t_{i-1})\le4$ on every rational partition. By continuity the same holds on every partition. Equivalently the increment functional $\sum_i\lambda_i(f(t_i)-f(t_{i-1}))$ has norm at most two on step functions in $L^2[0,1]$. Its representing $L^2$ function is the weak derivative of $f$, with squared norm at most four. This proves upper inclusion on dyadic horizons.

For any remaining sequence $n\to\infty$, take a subsequence with $c_n=n/2^{\lceil\log_2n\rceil}\to c\in[1/2,1]$ and a uniform limit $f$ at the corresponding upper dyadic horizons. Exact interpolation and the ratio of the normalizations give uniform convergence along that subsequence to $c^{-1/2}f(c\,\cdot)$. Its energy is $\int_0^c|f'|^2\le4$. This proves compactness and upper inclusion on every horizon. The lower functional law gives equality in (1). Bounded equivalence of the fixed nonperiodic root laws transfers the probability-one conclusion to $Q_a$.
