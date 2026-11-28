# Fine-scale smoothing conditional on the complete native clock row

Use the shortcut map $T(2n)=n,\ T(2n+1)=3n+2$. At a positive target $y$, record for each ordinary start reaching $y$ its **first** visit, the total number $s$ of shortcuts and the number $j$ of odd departures, and set
\[
 P_y(n)=y2^s3^{-j},\qquad B_y(n)=\log(P_y(n)/n).
\]
Thus $B_y$ is the actual sum of $\log(1+1/(3v))$ over odd departures strictly before the first hit. Put $a=(j,s)$. On the alternative population of all ordinary escaping starts, choose a positive representative $m_C$ of each component and record $a=(C,j,s)$ with the unique *signed* integers satisfying
\[
  P(n)=n e^{B_\infty(n)}=P(m_C)2^s3^{-j}.
\]
Existence follows by aligning the two ordinary paths, uniqueness by independence of $2,3$. The component and both integers belong to the same sampled start as its log correction. Write
\[
  M_{X,a}=X^{-1}\sum_{\substack{n\le X\\ a(n)=a}}\delta_{B(n)}
\]
for either of these subprobability families. In the escaping case the representative choices need not be effective. Translation of each escaping component's marks by a component-dependent constant is harmless.

Fix $0<\gamma<1/8$. For $T_0$ tending to infinity put $L=\log T_0$ and choose any physical cutoff
\[
        X\ \ge\ T_0\exp(6L^\gamma).
\]
There is a constant $C_\gamma$ independent of the target, cutoff, representatives and all row tests such that
\[
 \left|\sum_a\int f_a(b)\,dM_{X,a}(b)\right|
      \le C_\gamma(1+L)^{-1/2+4\gamma}.                              \tag{1}
\]
This holds for **every row-dependent family** $|f_a|\le1$ on $\mathbb R$ satisfying
\[
 {\rm Lip}(f_a)\le T_0 e^{L^\gamma},\qquad
       \sup_{u<v}\left|\int_u^v f_a(b)\,db\right|
                   \le T_0^{-1}e^{L^\gamma}.                         \tag{2}
\]
The functions may vary with $X,y,T_0$, with no regularity between different rows. The two cited analytic inputs are [PR215, the local signed starting trit, (2), checkpoint 6 at 121054cf](https://github.com/GettysburgResearch/collatz/blob/121054cf6569859585ede5c2d6e024eb2d97bbc5/research/astra-nine-hour-20261128/escape/phase6/LOCAL_TRIT_AND_RAJCHMAN.md) and [Weaver 124, Theorem 1, full counted fusion of a growing block](https://rstation.ai/problems/collatz/papers/124). PR215 already obtained uniform logarithmic Fourier decay after summing the first-hit rows, and the sum of absolute Fourier amplitudes over escaping components. We retain absolute values over **each pair of actual clock coordinates** and permit arbitrary tests in (2). This is a source-qualified written deduction using the native signed transport and fusion estimates.

For example on the bounded physical mark range let $\Phi_a$ be any real $C^2$ functions with $|\Phi'_a|\ge c>0$ and $|\Phi'_a|+|\Phi''_a|\le C$, uniformly in $a$. Then
\[
 \sum_a\left|\int e^{i T_0\Phi_a(b)}\,dM_{X,a}(b)\right|
            \ll_{\epsilon,c,C} (1+\log T_0)^{-1/2+\epsilon}           \tag{3}
\]
on taking $4\gamma<\epsilon$. The lower bound on $X$ uses this $\gamma$. To check (2), extend the phases linearly off the common support interval at the endpoint derivatives. Integration by parts on the bounded middle interval and the exact integrals on the outer rays bound all primitives by $O_{c,C}(1/T_0)$. Multiplying each test by its own unit phase gives the sum of moduli. There is no assumption of independence between the two native clocks and the correction, or between observations on the same path.

## Renewal with the true coordinates retained

Write $\ell=\log2,\ b_0=\log(3/2)$ and let $M(x)$ be the measure with rows $M_{e^x,a}$. Let $S_h$ add $(h,1)$ to the recorded $(j,s)$ without changing the mark or component, $h=0,1$. Older shortcuts add the same two counts in both populations. The only possible exception is the single defective source edge at a first-hit target. With $K\ge2$ consider the signed residual
\[
 \mathcal R(x)=M(x)-\tfrac12(S_0)_*M(x-\ell)
                          -\tfrac12(S_1)_*M(x+b_0).
\]
For every $A>0$ its pairing with any unit-bounded test $F(a,v)$ whose Lipschitz constant in $v$ is at most $K$ satisfies
\[
   |\langle F,\mathcal R(x)\rangle|
           \ll_A(1+x-\log K)^{-A},\qquad x\ge\log K+2.                \tag{4}
\]
Row shifts preserve the test class.

Indeed write $Y=e^x$. The even sources cancel exactly, allowing the single exceptional edge at cost $O(1/Y)$. Split the odd source sum by its true first output $z\equiv2\bmod3$, $2z-1\le3Y$. The older step adds $\log(2z/(2z-1))$ to its mark and applies $S_1$ to its row, at the same possible exceptional cost. The comparison term is the unrestricted sum through $3Y/2$ with weight $1/3$. The endpoints cost $O(1/Y)$. Drop $z<\sqrt{YK}$ at cost $O(\sqrt{K/Y})$. On the remaining range removing the older correction costs $O(\sqrt{K/Y})$. The remaining ternary test is centered.

On a retained octave $[Z,2Z)$ partition into intervals of length $H\asymp\sqrt{Z/K}$, charging an incomplete piece at cost $O(H)$ before normalizing. In a given interval replace $\log z$ in $B(z)=\log P(z)-\log z$ by its value at the left endpoint. This costs $O(KH/Z)$. Here $P(z)$ is fixed by the full row at the chosen root or component. Take $t=\lfloor(\log_2 H)/4\rfloor$. For an unvisited target before $t$, or for complete escape, the true complete row at $z$ is a function of the genuine pair $(F_t(z),T^t z)$, where $F_t$ denotes shortcut odd count. Eventual membership is also such a function. In the first-hit case at most $2^t$ sources on the whole line reach the target before this date, including the empty path: each length-$i$ parity word has an affine map of positive slope, so has at most one such preimage. Their error after interval normalization is $O(H^{-3/4})$. The signed native starting-trit estimate on this arbitrary translated interval therefore gives $O_A((1+\log H)^{-A})$ in normalized sum. Bounded $H,t$ can use the unit bound. Sum with the physical interval lengths. Since $\log(Z/K)\ge (x-\log K)/2-O(1)$ and the retained octaves have total length $O(Y)$, the main errors give (4). The total incomplete-piece cost is $O(\sqrt{Y/K}+1+\log Y)$ before normalization and satisfies the same bound. All tests of the full native pair used here are bounded uniformly, regardless of the row or its clock.

Iterate (4) on the fair size walk with increments $-\ell,b_0$, carrying along the corresponding additive row shifts. Stop when it first crosses below $h=\log T_0+6L^\gamma$. Its increments have strictly negative mean and the overshoot is in $[h-\ell,h]$, including an immediate start at the boundary if desired. There is an absolute uniform expected occupation bound for every unit spatial strip before crossing: from any visit a fixed number of negative increments followed by never returning above that strip has fixed positive probability, giving a geometric bound for separated visits. This uses the usual negative-drift exponential bound for the two-point walk. Equivalently one may use the [native stopped walk, original unit-strip estimate](https://github.com/GettysburgResearch/collatz/blob/121054cf6569859585ede5c2d6e024eb2d97bbc5/research/astra-nine-hour-20261128/escape/phase2/NATIVE_BINOMIAL_TRANSFER.md). Summing (4) over strips and raising $A$ arbitrarily shows that the cumulative pairing error for $K=T_0e^{L^\gamma}$ is $O_D(L^{-D})$ for every fixed $D$. The remaining pairing is the expectation of genuine boundary sums $M(u)$ tested with the original functions after one common row shift. Stop first at a bounded number of steps and pass to the limit by boundedness. This operation preserves both conditions in (2).

## Physical smoothing on the boundary source octave

At a boundary size $Y=e^u\in[T_0e^{6L^\gamma}/2,T_0e^{6L^\gamma}]$ discard starts below $Y/L^B$ at cost $O(L^{-B})$, taking $B$ large. Average each remaining summand over sliding source blocks of
\[
               D=\lceil e^{9L^\gamma}\rceil
\]
consecutive integers, trimming both ends at cost $O(D/Y)$. At time $t=\lfloor(\log_2Y)/4\rfloor$, the full counted-fusion estimate bounds the fraction of starts for which the entire block has not fused at equal odd count by
\[
 O((1+\log D)^4/\sqrt{\log Y}+2^t/Y)=O(L^{-1/2+4\gamma}).
\]
The transfer to the finite starting interval follows because equal endpoint and equal counts on each prescribed binary parity cylinder are an exact periodic event in the block start modulo $2^t$. For a first-hit target, at most $D2^t$ starting blocks include some source whose first $t$ steps hit that target. Their normalized cost is negligible uniformly in the target. For complete escaping marks this exception is absent.

On every other block, eventual membership is constant. In a selected block the full row is identical for all its inputs, so $P$ is the same and the marks are exactly $c-\log(n+i)$, $0\le i<D$, with one $c$. The Riemann approximation of its normalized sum by
\[
        D^{-1}\int_0^D f_a(c-\log(n+v))\,dv
\]
costs $O(K/n)=O(L^B e^{-5L^\gamma})$. Substitution $w=c-\log(n+v)$ and an integration by parts against any primitive bounded on this interval by $T_0^{-1}e^{L^\gamma}$ bound the integral by $O(Y T_0^{-1}e^{L^\gamma}/D)$. Here the weight $e^{c-w}$ and its total variation on the block are $O(Y)$. This final bound is $O(e^{-2L^\gamma})$. The same arguments hold for the common shifted row family produced by the size walk. Summing all errors gives (1).

## Fine histogram comparison with the row held fixed

There is a direct variation statement. Put $r=T_0^{-1}$, $w=r e^{L^\gamma}$, and let $K_w$ be uniform probability on $[-w/2,w/2]$. With any independent origin for the regular grid $\mathcal G_{a,r}$ in **each** row,
\[
  \sum_a\ \sum_{I\in\mathcal G_{a,r}}
   \left|M_{X,a}(I)-(K_w*M_{X,a})(I)\right|
       \ll_\gamma (1+L)^{-1/2+4\gamma}.                               \tag{5}
\]
To see this, take the unit-bounded rowwise step tests $q_a$ constant on the respective grid cells realizing the sum of absolute differences. Put $\eta=8r e^{-L^\gamma}$ and use a uniform probability mollifier on $[-\eta/2,\eta/2]$. The functions $\widetilde q_a$ so smoothed are bounded by one and $2/\eta$-Lipschitz. The tests $(\widetilde q_a-K_w*\widetilde q_a)/2$ have absolute value at most one, Lipschitz constant at most $2/\eta$ and primitive oscillation at most $w/2$, by translating the interval of integration. Apply (1). The unsmoothed discrepancy is supported in the $\eta$-neighborhood of the row's grid boundaries. Majorize this set by a continuous $r$-periodic tent function equal to one in that neighborhood, zero at distance $2\eta$, with Lipschitz constant $1/\eta$. Subtract its mean $O(\eta/r)$ to get a bounded test of primitive oscillation at most $2r$. The same is true after convolution with $K_w$. Apply (1) to both tests and restore their means. For bounded $L$ one can enlarge the constants. This proves (5).

Each test in (5) uses the exact row of its own sample. The estimate charges the total failed-block mass once. It does not provide a relative failure bound inside an arbitrary rare mark bin, and so it does not give the full one-source square-energy upper at scale $1/T_0$. At one fixed source cutoff the unsmoothed marks are discrete. The comparison is between their histograms, which retain that cutoff and both clocks.
