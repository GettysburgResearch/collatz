# Every odd rotation in the near-octave spectral regime

Let $h,p,q$ denote the least shortcut period, odd period and complete reduced denominator of a primitive positive rational Collatz cycle. For the actual odd division exponents write $s(\ell)=\#\{i\bmod p:e_{i+\ell}\ne e_i\}$. In the regime of the [complete spectral denominator theorem](SPECTRAL_NEAR_OCTAVE.md), namely $h\to\infty$, odd minimum $m_0\ge h^{2-o(1)}$ and odd maximum-to-minimum ratio $R\le2+h^{-1+o(1)}$, one has
\[
              \min_{0<\ell<p}s(\ell)\,\frac{\log_2 q}{h}\ \ge\ 1-o(1).
                                                                        \tag{1}
\]
This is uniform over rotation orders and mismatch counts. Quantitatively, sufficiently small complete denominators in this physical range force many unequal actual odd valuations at **every** proper rotation. The initial spectral denominator theorem uses its stated two-logarithm estimate. The finite mismatch bound below is elementary.

## Preserving the allowed frequencies

Use $g=\gcd(h,p)$, $a=h/g$, $b=p/g$, and $d_i=\lfloor ia/b\rfloor-E_i$, where $E_i$ is the elapsed shortcut length after $i$ odd steps. The $j$ coordinate runs through $i=k+jb$, $j\bmod g$, for each $0\le k<b$. This merely reorders the $b$ rank columns of the spectral theorem. Write $J$ for the cardinality of the union of the Fourier supports of the physical columns $2^{-d_{k+jb}}$ on $\mathbb Z/g$, including frequency zero.

Whenever each $d$-column takes at most two values, there is an affine function of $2^{-d}$ agreeing with $d$ on that column. The two possible inputs are distinct when the column is nonconstant. Its Fourier support is contained in the same global union since frequency zero is already present. The physical clipping theorem ensures this condition eventually in the stated regime. No condition on the mean or sign of the individual column is needed for the finite bound.

Native exponents obey $e_i=\lfloor(i+1)a/b\rfloor-\lfloor ia/b\rfloor+d_i-d_{i+1}$. On a fixed $k$-column the floor difference is constant; increasing the phase by one selects another column, possibly rotating its $j$-index. An arbitrary lag $\ell$ also permutes columns and cyclically rotates their $j$-indices. All Fourier coefficients of every column of $f_i=e_{i+\ell}-e_i$ therefore remain in the same set of $J$ frequencies. Some column of $f$ is nonzero: a proper period of the valuation word repeats its whole shortcut word and the corresponding rational state, contrary to primitivity.

For a nonzero function on $\mathbb Z/g$ with $t$ nonzero entries and $j$ nonzero Fourier coefficients, $tj\ge g$. Indeed, for the unnormalized discrete transform, $\|\widehat f\|_\infty\le\|f\|_1\le\sqrt t\|f\|_2$ and Parseval gives $g\|f\|_2^2=\|\widehat f\|_2^2\le j\|\widehat f\|_\infty^2$. Apply this to one nonzero discrepancy column. Its support contributes to the actual number of unequal exponents and $j\le J$, so the exact finite result is
\[
                        s(\ell)J\ge g .                                \tag{2}
\]
More precisely, if $R_\ell$ discrepancy columns are nonzero, summation gives $s(\ell)J\ge gR_\ell$. For a whole-cell lag $\ell=tb$, translation in $j$ multiplies each frequency by its character value and subtraction annihilates all frequencies of order dividing $t$. The same proof then gives $s(tb)J_t\ge gR_{tb}$ with $J_t=\sum_{k\in\mathcal A,\, k\nmid t}\varphi(k)$: some surviving column exists for every proper such lag.

This also works for $g=1$. The spectral theorem gives $\log_2q/h=(1+o(1))J/g$ along every sequence in the physical regime. Its error is independent of the choice of lag, which yields (1).

## An explicit upper example within a factor four

Use [the two independent prime markers](INDEPENDENT_CLOCKS.md) with distinct primes $5\le Q<P$, $N=QP$, and a coprime mechanical cell of length $n$, odd weight $b$, from an upper continued-fraction convergent $n/b>\log_2 3$. Select the two phase markers described in that construction. For each choice of $Q,P$ take $n$ arbitrarily large (for instance $n>N^N$), so the actual primitive rational cycles are in the same high-minimum near-octave regime and all their odd valuations are one or two. Formula (5) of the construction, or its spectral calculation, gives $J=1+(Q-1)+(P-1)=P+Q-1$ and $g=N$. Both marker columns are nonconstant; a single changed odd date has distinct column from the other marker. Their singleton divisibility indicators have all frequencies at their respective prime orders.

Shift by $Q$ complete cells, that is by $\ell=Qb$ odd slots. The $Q$-marker is unchanged. The $P$-marker differs precisely in the cells $j\equiv0,-Q\pmod P$, totaling $2Q$ cells. In such a cell one specified odd date moves by one, with no change to any other odd date in that cell. Each moved date changes the preceding and following odd gap. They are distinct gaps, and these gap pairs for different altered cells are disjoint since the altered date has fixed within-cell odd index and $b\ge2$. Thus $s(Qb)=4Q$ exactly. If $P/Q\to\infty$, the near-octave denominator formula now gives
\[
                     s(Qb)\,\frac{\log_2q}{h}\longrightarrow4.
\]
A fixed $Q$ gives a family with a constant displayed mismatch count. Choosing $Q\to\infty$ arbitrarily slowly relative to the available cell lengths gives genuine rational families with growing mismatch counts and $\log_2q/h\to0$. This bounds how large a universal constant can replace the one in (1); equality in (1) is not established. None of these examples has denominator one.

[Finite controls](check_spectral_rotations.py) check the rank-support transfer, the native inequality for every rotation and the selected two-marker discrepancy. [Archived counts](../../../reports/astra-infinite-descent-20261127/cycles/SPECTRAL_ROTATIONS.json)
