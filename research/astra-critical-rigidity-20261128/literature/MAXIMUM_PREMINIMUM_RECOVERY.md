# Largest multiplicative recovery before the genuine global minimum

**Proposed, source-qualified written theorem.** For the positive shortcut let
\[
 M(n)=\max_{0\le i\le t\le\tau(n)}T^t n/T^i n,
\]
where \(\tau\) is the first global minimum date. This maximum compares a later height with an earlier height on the same descent. For uniform \(U_X\) through \(X\), and every fixed \(b>0\), there are absolute \(c,C>0\) such that
\[
  1-e^{-c/b}\ \le\ \liminf_{X\to\infty}\Pr(M(U_X)\ge b\log X)
   \ \le\ \limsup_{X\to\infty}\Pr(M(U_X)\ge b\log X)
   \ \le\ \min(1,C/b).                                                 \tag{1}
\]
Thus the genuine preminimum maximum recovery is of order \(\log X\) in probability (tight above and away from zero after that scaling). Its upper-tail order is \(1/b\) in this two-limit sense. We do not identify the full preminimum limiting distribution.

For comparison the entire homogeneous random-walk law *does* transfer on a shorter uncapped native prefix. Fix \(0<d<1\), take \(K=\lfloor d\log_2 X\rfloor\), and let \(M_K(n)\) be the same maximum with \(\tau(n)\) replaced by \(K\). Then, for each \(b>0\),
\[
                  \Pr(M_K(U_X)<bK)\ \longrightarrow\ \exp(-c_*/b)       \tag{2}
\]
with a fixed \(0<c_*<\infty\) specified below. This second statement treats a deterministic clock. Weaver's Paper 194, equation (14), already controls drawup uniformly on an early clock with a polynomial exceptional probability at a polynomially large threshold. Paper 215 studies the peak from the original source on a capped tree. Leen's stopped-height fluctuations control changes on the larger logarithmic scale \(\sqrt{\log X}\). Here (1) uses all pairs of dates through the genuine global minimum and finds the scale of their multiplicative ratios. [Weaver, Paper 194](https://rstation.ai/problems/collatz/papers/194) · [Paper 215, peak from the source](https://rstation.ai/problems/collatz/papers/215) · [Leen, original proper minimum and landing transport](https://doi.org/10.5281/zenodo.23269488)

## Every downward gate resets the running minimum

An odd first entrance at \(z\) from an odd source above \(z\) is a new native record low: all prior odd states exceed \(z\), and the evens on any previous halving string exceed the odd value at its end. On the final halving string they exceed the first odd landing. Thus any recovery crossing this date can be enlarged by moving its starting date to the landing. Given a series of successively lower odd gates, the maximum is attained within one of the intervening segments. The initial halving string of an even source cannot enlarge the eventual recovery from its odd part.

Take the notation \(\alpha=1001/1000\) and \(W_y\) uniform on odd \([y,2y)\). For large \(z\le y\le z^{\alpha^2}\), the probability of any recovery of factor at least \(A\ge2\) up to the first odd entrance at \(z\) is
\[
                    O((1+\log z)/A)+O(z^{-c_0}).                        \tag{3}
\]
The same bound covers a failed entrance, on its own exceptional event. By the [short reference descent proof](ALL_HIGH_TARGETS.md), a native entrance at most \(z\) occurs by \(K_z=\lfloor(\ln z)/10\rfloor\) outside probability \(O(z^{-c_0})\). After a first even entrance only halvings remain until the odd entrance, so no additional recovery is created. Through \(K_z\), the true correction factor on *any* subinterval is at most \(\exp(K_z2^{K_z}/(3y))\le2\). On the fair parity model each homogeneous multiplier \(3^\epsilon/2\) has mean one. At a fixed starting date its subsequent products form a nonnegative martingale; the chance of ever exceeding \(A/2\) is \(O(1/A)\). The possibly fixed first odd bit costs at most \(3/2\). Sum the bound over all \(K_z+1\) possible starting dates. The exact native parity transfer error \(O(2^{K_z}/y)\) is exponentially small in \(\log z\), proving (3).

From the original source \(W_y\) use the grid \(z_j=y^{\alpha^{-j}}\) down to the last threshold at least \(B_0\), where \(B_0\) is large and fixed. For the portion after the first odd landing at \(z_j\), test that landing by whether a recovery of factor \(A\) occurs by its next lower gate. Take the test as false if the landing overshot the lower gate. The original uniform-source probability is compared by Leen's Proposition *Transport* to the reference source \(z_j^\alpha=z_{j+1}^{\alpha^2}\), with error \(O((\ln z_j)^{-c})\) for the bounded test. Its event is contained in a full recovery from that reference source before the lower gate. The first portion uses (3) directly. Gate log errors sum to \(O((\ln B_0)^{-c'})\) and \(\sum_j(1+\ln z_j)\ll\ln y\) uniformly, since the logs form a geometric progression down to \(\ln B_0\). If \(m(W_y)\le B_0\), all bottom states after the last landing and through the minimum belong to finitely many true stopped paths depending only on \(B_0\); their recoveries are bounded. The proper minimum theorem makes the exception arbitrarily small by increasing \(B_0\) after the source limit. Conditioning on the initial powers of two and finitely many top odd source octaves, then releasing the truncation, gives the upper bound in (1). The discarded mass is geometrically small, and the retained \(\ln y\) are at most \(\ln X\).

For the lower bound put \(j=\lfloor\log_2 X\rfloor\), \(K=\lfloor j/64\rfloor\). With probability \(1-o(1)\) the source is at least \(X^{3/4}\). The fair native parity model through \(16K\) has total variation error \(O(2^{16K}/X)\) from this ordinary experiment before imposing the source-size restriction. Its genuine date-\(16K\) height is less than \(n2^{-K}\) with probability \(1-o(1)\), by the \(9K\)-odd Chernoff estimate and true additive correction in [Sharp multiscale targets](SHARP_MULTISCALE_TARGETS.md). All dates through \(K\) precede the true minimum. In the first \(K\) native bits, the iid odd-gap excursion trials in [Critical log-square masks](CRITICAL_LOG_SQUARE_MASKS.md) have probability at least \(1-\exp(-c K/A)-O(e^{-c_0 K})\) of a completed odd-to-odd word with homogeneous multiplier at least \(A\). This follows from at least \(\lfloor b_0K\rfloor\) completed excursions except exponentially rarely, and per-excursion probability at least \(c/A\), without conditioning on their total duration. The estimate holds for every fixed positive limiting \(K/A\) with one absolute \(c\), by absorbing integer rounding for large \(K\). The true multiplier is at least its homogeneous value because all additive corrections are positive. Set \(A=b\ln X\) and decrease the absolute constant to obtain (1).

## The deterministic early-clock law

For (2), the comparison uses native iid increments \(X_i=\epsilon_i\ln3-\ln2\) with \(\epsilon_i\) fair. Let \(S_j=\sum_{i\le j}X_i\), \(D=\inf\{j\ge1:S_j<0\}\), and \(H=\max_{0\le j\le D}S_j\). The successive strict descending ladder excursions have iid pairs of lengths and heights. The classical discrete Cramér–Iglehart estimate states
\[
 \lim_{u\to\infty}e^u\Pr(H>u)
       = C_H=\Gamma\,(1-\mathbb E e^{S_D})\in(0,\infty),\qquad
 \Gamma=\lim_{u\to\infty} e^u\Pr(\sup_{j\ge0}S_j>u).
\]
The present walk has negative mean, \(\mathbb E e^{X_1}=1\), finite tilted positive drift and all exponential moments. It is nonarithmetic in the renewal sense: the two increments generate a nondiscrete additive subgroup since \(\log_2 3\) is irrational. In particular the strict ascending ladder heights themselves have nondiscrete span: both \(\ln(3/2)\) and \(2\ln(3/2)-\ln2>0\) are possible first ascending heights, by respectively one up step and one down followed by two up steps; their ratio is irrational. The ladder length \(D\) has an exponential tail since \(D>j\) implies \(S_j\ge0\), and the mean drift is negative. This uses the discrete formula, as reviewed in equations (1.1)–(1.3) of the original paper. [Doney and Griffin, *Cramér's estimate for the reflected process revisited*](https://arxiv.org/abs/1708.02470)

Up to time \(K\), the maximum \(\max_{i\le t\le K}(S_t-S_i)\) is bracketed by the maxima over the first \(\lfloor(1-\delta)K/\mathbb E D\rfloor\) and \(\lceil(1+\delta)K/\mathbb E D\rceil+1\) complete excursions with probability tending to one. Use the law of large numbers for the lengths; their dependence on their own heights is harmless for these deterministic bracketing counts. At \(u=\log(bK)\), independence of the full excursion heights gives the limit \(\exp[-C_H/(b\,\mathbb E D)]\) after \(\delta\downarrow0\). Changing a strict inequality at the moving threshold follows by a fixed multiplicative squeeze in \(b\). The disclosed constant is \(c_*=C_H/\mathbb E D\).

Finally the complete first \(K\) native bits of a uniform source through \(X\) have total variation error \(O(2^K/X)\). Outside the negligible set \(n<X^{(1+d)/2}\), all true states in this prefix are at least \(n2^{-K}\). The correction to any interval's log multiplier is between zero and \(O(K2^K/n)=o(1)\), simultaneously. Thus the true finite-date maximal recovery divided by its homogeneous counterpart tends to one in probability under the physical parity coupling. This proves (2).
