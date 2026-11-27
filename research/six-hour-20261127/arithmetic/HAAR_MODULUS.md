# Almost-sure modulus in the infinite cubic rotation group

**Written consequence of the all-time cubic calculations.** On an injective sequence of positive odd integers coprime to three, let $V_n=\prod_{i<n}U_{x_i}$. Sample, independently for each Pell field label, a uniform cubic rotation over the multiquadratic field containing $\mu_3$. This is Haar probability on the inverse limit of the finite rotation groups from [the field calculation](CUBIC_HEIGHT_COST.md). Then

* if $\sum_i x_i^{-2/3}<\infty$, the random $\log|\sigma V_n|$ converges almost surely and in $L^2$ to a finite real number,
* if $\sum_i x_i^{-2/3}=\infty$, the random $|\sigma V_n|$ has almost surely lower limit zero and upper limit infinity.

Here the physical positive embedding gives $\log|V_n|=\sum_{i<n}\log U_{x_i}$, which tends to infinity exactly when $\sum x_i^{-1/3}$ diverges. All assertions concern a single fixed sequence. No hypothesis on ordinary orbit frequency selects one of the Haar cases.

For a positive real root put $a_x=\log U_x>0$. The formula $U_x=w_x^3(3x+1)/(3x)$ and the positive Kummer expansion of $w_x$ show $a_x\asymp x^{-1/3}$. The other two cubic conjugates of $U_x$ are complex conjugates and have modulus $U_x^{-1/2}$, since $U_x$ has cubic norm one. With $E_x=\eta_F^{e_x}$, $3\nmid e_x$, a nonzero rotation of $\eta_F^{1/3}$ always sends the physical root at $x$ to one of these two conjugates. Thus
\[
 \log|\sigma V_n|=\sum_{i<n} a_{x_i} Z_{F_i},\qquad
 \Pr(Z_F=1)=1/3,\quad \Pr(Z_F=-1/2)=2/3.
\]
The variables for distinct labels are independent. By [the repeated-label bound (7)](ALL_TIME_CUBIC_TRACE.md), terms with $e_x\ge5$ have absolutely summable $a_x$ uniformly over injective sequences. Their series converges uniformly for all rotations and in $L^2$. There is at most one remaining term per label. Its summands, written $a_jZ_j$ in their original order, are independent and centered, of variance $a_j^2/2$; all $a_j$ are bounded. Finite total variance gives almost sure and $L^2$ convergence by the independent-sum maximal inequality. For completeness, a subsequence of tail variances below $2^{-3k}$ has probability at most $2^{-k}$ of any partial tail sum exceeding $2^{-k}$, proving almost sure Cauchy convergence.

When the variance sum diverges, choose disjoint successive blocks with standard deviations $s_m$ exceeding $m$ times one plus the sum of all preceding absolute coefficient sizes. For each such block sum $B$, independence and centering give $\mathbb E B^4\le C s_m^4$ for an absolute $C$ (a centered $Z$ has fixed second and fourth moments). Hölder's inequality gives $\mathbb E|B|\ge s_m/\sqrt C$. Centering splits this expectation equally between positive and negative parts. Applying the second-moment inequality to each part gives absolute constants $c,c'>0$ with $\Pr(B\ge c s_m),\Pr(B\le-c s_m)\ge c'$. The blocks are independent. Both signs occur infinitely often at this scale almost surely, and each such excursion dominates the entire preceding partial sum. Restoring the uniformly convergent repeated-label remainder preserves both divergent subsequences.

The bounded normalized trace of $W_n=\prod w_{x_i}$ established earlier is a complex signed average. The variance dichotomy measures moduli of $V_n$ under full rotations. The distinguished physical place and the selected nonarchimedean places do not supply an ordinary escape contradiction in either case.
