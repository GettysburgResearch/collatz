# How many distinct numerical states remain on a ternary tower?

Keep the fixed towers \(X_n^\pm=c+M3^{\pm n}\), conditional capacity \(\kappa(c,M)>0\), and shortcut deadline \(t=\lfloor\log_2 N\rfloor\) of the [tower synchronization theorem](TERNARY_TOWER_SYNCHRONIZATION.md). Let
\[
       D_{a,N}^{\pm}=\#\{T^t(X_n^\pm):a\le n<a+N\}.
\]
Then, uniformly in the exponent origin \(a\ge0\) and in the choice of the two directions,
\[
 \sqrt{2/\pi}-o(1)\ \le\ \frac{\sqrt t}{N}D_{a,N}^{\pm}\
                           \le\ \kappa(c,M)+o(1).                         \tag{1}
\]
These are the actual distinct rational or integer values present at one common date. In particular the capacity constant for every such translated dyadic coset obeys \(\kappa(c,M)\ge\sqrt{2/\pi}\).

The upper bound counts consecutive runs of equal endpoints. There is one initial run and each subsequent change is an adjacent failure in (1) of the tower theorem.

For the lower bound, write \(g_j(n)\) for the ordinary number of odd-input departures along the first \(j\) shortcut steps from \(X_n^\pm\). On the full two-coset Haar law conditioned to the fixed set \(U\) in that theorem, \(g_j\) has a mixture of two distributions \(g_d+\operatorname{Bin}(j-d,1/2)\), with \(d=v_2(M)+3\) fixed and \(g_d\) determined by the initial coset. This follows from the bijective parity-word cylinder map; equivalently the residual base after the first \(d\) fixed letters is Haar. Take \(j=t-\lceil2\log_2(t+2)\rceil\). Over every exponent interval of length \(N\), the empirical probability of any event depending on its first \(j\) letters differs from its conditional Haar probability by at most \(2^{j-v_2(M)-2}/N=O(t^{-2})\). The binomial central limit theorem thus gives, uniformly over interval origins,
\[
  \frac{g_j-(j/2)}{\sqrt{j}/2}\Longrightarrow\mathcal N(0,1).
\]
The centered final increment has absolute value at most \((t-j)/2=o(\sqrt t)\); the same convergence holds with \(t\) in place of \(j\). This use of a shorter deadline controls incomplete exponent periods without presuming a local limit law for the final grade.

Discard the initial \(O_{c,M}(t+1)\) indices at which (4) of the tower theorem permits unbalanced equality, including all smaller indices. From the remainder, any two distinct exponents having the same \(g_t\) have distinct values at date \(t\): balanced equality requires their grades to differ by their positive exponent gap. For each fixed \(\varepsilon>0\), a proportion \(\Phi(2\varepsilon)-\Phi(-2\varepsilon)+o(1)\) of the initial interval has \(|g_t-t/2|\le\varepsilon\sqrt t\), where \(\Phi\) is the standard normal distribution function. There are at most \(2\varepsilon\sqrt t+1\) integer grades there. Keeping the most numerous such grade gives
\[
 \liminf_{N\to\infty}\ \inf_{a,\pm}\frac{\sqrt t}{N}D_{a,N}^{\pm}
     \ \ge\ \frac{\Phi(2\varepsilon)-\Phi(-2\varepsilon)}{2\varepsilon}.
\]
Letting \(\varepsilon\downarrow0\) proves (1). The endpoints may merge at later dates. The argument gives no lower bound for the number of eventual integer basins.

The cylinder and conditional-survival inputs are Leen's original fixed-state statements. The two-sided assertion above also uses the numerical equality equation for the widely separated endpoints in the exponent interval. [Leen, exact cylinders](https://doi.org/10.5281/zenodo.23268755) · [Leen, fixed-state harmonic capacity](https://doi.org/10.5281/zenodo.23268751)
