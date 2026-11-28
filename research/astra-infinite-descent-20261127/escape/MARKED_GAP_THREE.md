# Fractional source positions for the full marked trace

Use the original all-visits definitions and clocks in [the signed gap-three calculation](GAP_THREE_TRACE.md). Write \(a=9k+2,b=9k+5,c=9k+8\), and \(H_n=h_d(n)\) at the actual grade \(d\) odd landing from \(n\). Put \(I_n(q)=\mathbf1_{(n-q)H_n\le t}\) and \(S_n=I_n(1/2)-I_n(0)\). Then, at every \(d,y,t\),
\[
 \pi(y)\big[L_{d+1,y}(t)-L_{d,y}(t)\big]
 =\tfrac32\sum_{k\ge0}\left[
    v_c(d,y)I_c(1/2)-v_b(d,y)I_b(0)+v_a(d,y)S_a+v_c(d,y)S_c
                         \right].                                      \tag{1}
\]
This includes the exact signed unmarked identity by setting \(t=1\). All quantities are physical apart from the explicitly displayed half-unit shift in the threshold tests.

## Removing all but the single first halving

For every positive integer \(n\), define the signed finite-mass measure on real source positions
\[
 \nu_n=\sum_{e\ge1:\,z=(2^en-1)/3\in\mathbb N}
              3\,2^{-e}\rho_1(z)\,\delta_{n-2^{-e}}-\rho_1(n)\delta_n.
\]
Here \(\rho_1(n)=n\bmod3\) on both parities. For odd \(n\), the incoming letter takes odd \(z\) to \(n\), and the full mark at \(z\) is \(H_n(n-2^{-e})\) because \(3z=2^e n-1\). Thus the original signed column equals \(\sum_{n\ {\rm odd}}v_n(d,y)\nu_n(({-}\infty,t/H_n])\). The equalities retain actual word multiplicities even when a positive cycle is visited repeatedly.

To rewrite the sum on all integers, replace \(\nu_n\) by \(\tilde\nu_n=\nu_n-\frac12(s_{1/2})_*\nu_{2n}\) where \(s_{1/2}(x)=x/2\). The equality of the marked series follows by telescoping on each full dyadic cone, using \(v_{2n}=v_n/2\), \(H_{2n}=H_n/2\). The finite cone remainder is its last omitted scaled measure; its total variation is bounded by a constant times \(2^{-R}\) at depth \(R\). Absolute convergence at each fixed grade/target follows by the unit inverse row bound \(K^d1\le2^d\), the bounded total variation of \(\nu_n\), and the factor two from initial halvings. Measures vanish on ternary nonunits.

In \(\tilde\nu_n\), an incoming term with \(e\ge2\) cancels precisely the scaled incoming term from \(2n\) with exponent \(e-1\): the predecessor and the real source position coincide. The remaining measure is zero unless \(n\equiv2\bmod3\), in which case it is
\[
 \tilde\nu_n=\tfrac32\rho_1((2n-1)/3)\delta_{n-1/2}
                    -\tfrac32\delta_n.
\]
The three nonnegative birth coefficients \(\rho_1((2n-1)/3)\) at \(a,b,c\) are respectively \(1,0,2\). Grouping one half-unit strip at each of \(a,c\) gives (1).

## Uniform cost of the two boundary strips

For \(0\le t_y\le1/(d+1)\), one may choose the threshold separately at every target. With both strips kept,
\[
        \sum_y\sum_{n\equiv2,8\pmod9}v_n(d,y)S_n(t_y)
                          =o((d+1)^{-1})                                \tag{2}
\]
uniformly over those choices as \(d\to\infty\). An absolute \(O((d+1)^{-1})\) holds at every \(d\). Indeed, fixing \(y,m,d,t_y\) fixes \(h=3^d2^{-m}/y\), and the active strip requires \(t_y/h<n\le t_y/h+1/2\). At most one positive integer occurs. The weights over distinct clocks form a subset of a geometric progression. Choose \(n_y\) at the smallest clock for which a strip is active, omitting empty targets. All strip weights at \(y\) sum to at most \(2H_{n_y}/(3y+1)\), and
\[
      (d+1) H_{n_y}\le1/(n_y-1/2)\le2/n_y .
\]
The chosen \(n_y\) are distinct because each ordinary source has a unique target at grade \(d\). Cauchy–Schwarz gives \(\sum_y1/(y n_y)\le\sum_{n\ge1}n^{-2}\). Restricting to \(n_y>R\) bounds this sum by \((\sum_y y^{-2}\sum_{n>R}n^{-2})^{1/2}\), uniformly in all the thresholds. For each of the finitely many \(n\le R\), either the positive odd orbit has distinct vertices forever, in which case the uniform simple correction floor \(b_d(n)\ge c_0>0\) eventually precludes \((n-1/2)H_n\le1/(d+1)\), or it has an eventual cycle, in which case \((d+1)H_n\to0\) geometrically up to the polynomial factor. Taking the finite-source limit first proves the little-oh. The simple floor follows from the [formal reciprocal packing and trace](ActualPacking.lean). Neither alternative assumes convergence to one.

## One unpaid-loss budget for both parts of the original statistic

Whenever the starts \(b,c\) have the same actual clock and landing at grade \(d\), they have the same \(H\) and loss. Since \(c-1/2>b\), their first two terms in (1) have nonpositive sum for **every threshold**. At \(t=1\) the pair cancels exactly. Outside this synchronization event, their positive part is at most \(v_c(d,y)\), simultaneously for all thresholds, including \(t=1\). Write \(y_d(n)\) for the physical landing and \(\chi_d(k)\) for the missed grade-clock synchronization. Thus
\[
 Q_d^*\le \tfrac32\sum_{k\ge0}\chi_d(k)
            \frac{b_d(c)-b_{d+1}(c)}c\,\mathbf1_{y_d(c)>1}
          +o((d+1)^{-1}).                                              \tag{3}
\]
Here \(o((d+1)^{-1})\) denotes the absolute nonnegative envelope of (2); a fixed multiple of \(1/(d+1)\) suffices for all \(d\). Each per-target supremum can be approximated arbitrarily on any finite target set and (2) is uniform in simultaneous thresholds. The maximum in \(Q_d^*\) is covered because the unmarked case is exactly \(t=1\) and has no strip. The first summand retains only the positive member's true one-step loss. One can truncate \(k<\lceil 2^{20D}/9\rceil\) on a grade block \(D\le d<2D\), with total omitted error \(O(D\theta^D)\) as in the signed calculation.

Keeping the narrow threshold in the unpaid positive member also yields a **pointwise** \(O((d+1)^{-1/2})\) bound for the marked branch alone. On its contributing sources \((c-1/2)H_c\le1/(d+1)\), hence \(v_c(d,y)\le 2/[(d+1)c]\). Truncate at the preceding exponential source cutoff with \(D=d\ge1\). In a dyadic octave \([2^j,2^{j+1})\) use the scalar comparison of \((9k+5,9k+8)\) by clock \(L=\min(d,\lfloor j/2\rfloor)\). Counted merger by clock \(L\le d\) forces \(\chi_d=0\). The residual harmonic source weight is \(O((1+L)^{-1/2}+2^{L-j})\): the progression has odd step nine, runs through every binary residue per period, and its fixed gap is three. The complete periods obey the scalar square-root estimate; a leftover incomplete period has at most \(2^L\) elements. Summing this bound in \(0\le j\le20d+1\) costs \(O(\sqrt{d+1})\). The strip and omitted-source errors give the assertion. The [earlier dyadic-sum estimate](ORIGINAL_TRACE_VARIATION.md) for the marked branch is stronger on average. Exponential decay of the unpaid unmarked losses, and an exponential estimate for the narrow strips in the presence of unknown cycles, remain open.
