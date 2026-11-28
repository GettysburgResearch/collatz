# Separated collisions below the critical physical clock

This restriction of [the slowly growing source spectrum](SLOW_SOURCE_CHARGE_SPECTRUM.md) uses one common physical odd depth \(n\). Take fixed \(a,b>0\) with \(a+b<1\). Put \(X_n=n^a,\ D=\log(4/3),\ \lambda=\log_2 3\). For each specified unit row at endpoint \(y\) and native time \(s\), put \(p=y2^s/3^n,\ \omega=3^n2^{-s}\). Retain only rows with
\[
                      p\le X_n,\qquad \omega\ge n^b .                  \tag{1}
\]
Here the endpoint is any genuine positive odd integer; at positive odd depth it is automatically prime to 3. Every contributor is an actual original odd source \(x\le p\le X_n\). On (1) the scalar geometric total obeys the strict short-clock bound \(s\le\lambda n-b\log_2 n\).

Let \(E_t(n)\) be the sum of \(t\)-th powers of normalized genuine first-arrival row masses on (1). For \(t=2,3\), as \(n\to\infty\) **in natural density**,
\[
 \frac{E_2(n)}{\sqrt{\log X_n}}\ \longrightarrow\
        \frac{\sum_C H_C^2}{\sqrt{2\pi D}},\qquad
 \frac{E_3(n)}{\log\log X_n}\ \longrightarrow\
        \frac{\sum_C H_C^3}{4\pi\sqrt3}.                               \tag{2}
\]
The ordinary dyadic averages of the displayed normalized quantities have the same limits. If one imports the uniform simple-path count
\(\#\{y_j\le T\}\ll T^\theta\), \(\theta<1\), the range extends to \(a+b<1/\theta\). Multiplying an exponent bound by a fixed power of \(\log T\) gives the same strict range. The elementary \(a+b<1\) assertion uses only distinctness in addition to the source inputs of the preceding spectrum. Initial halving clocks can be included, multiplying the corresponding coefficient by \(2^t\).

Indeed the full positive upper for the physical crop is furnished by the slow-source theorem because \(x\le p\le X_n\). For the lower fix finitely many escaping spines and a large bounded central Gaussian window \(B\). The contributing true rows there occur at \(y_{n-k}\) for
\(K_0\le k\le(1-\epsilon)\log X_n/D\); their corrected heights satisfy \(p^*\le X_n\), so \(p=f_{n-k}p^*\le X_n\). For \(N\le n<2N\), any violation \(y_{n-k}\le (2N)^{a+b}\) on one chosen spine has at most \(O_{a}(\log N)\) possible values of \(n\) per low spine site, because the distinct date \(n-k\) determines its location. There are at most \(O((2N)^{a+b})\) such sites by distinctness, or \(O((2N)^{(a+b)\theta})\) using the sparse path count. The union for these fixed spines has \(o(N)\) dates. On every other date the *same* central row obeys \(\omega=y_{n-k}/p\ge n^b\). Summing that central family as in the slow-source theorem, then taking \(B\to\infty,\epsilon\downarrow0\) and expanding the finite component list, gives the lower in natural density. The uniform upper bound for the normalized sums gives convergence of their dyadic means as well. This is a density-one clock statement; excursions back below a polynomial height at isolated very late dates have not been ruled out.

The same coefficients hold when the sums in (2) retain only ordered pairs or triples of *distinct and separated* sources within a common true cell. For any \(\eta>0\), discard a tuple if some pair has
\[
 |x_i-x_j|\le p(1+\log p)^{-1/2-\eta}.
\]
One may also discard pairs of equal initial residues modulo a cell-dependent integer \(m_p\ge(1+\log p)^{1/2+\eta}\), with the modulus fixed within that cell. Equivalently, up to an absolute scale factor, every row in octave \(p\asymp2^h\) may use any integer modulus \(m\ge (1+h)^{1/2+\eta}\); the modulus may differ among rows. For each individual source in this row at most \(O(1+p(1+h)^{-1/2-\eta})\) other integers satisfy either pair exclusion: for modular equality this counts one progression inside \([1,p]\), using that row's own modulus. For \(t=3\) the remaining unselected coordinate has at most \(p\max m_{n,s}(y)\ll p(1+h)^{-1/2}\) choices. Summing over primary coordinates \(x\) in the octave costs only its \(O(1)\) total row mass, since at common depth no original source is repeated. The discarded normalized pair contribution per octave is therefore \(O((1+h)^{-1/2-\eta}+2^{-h})\). For triples it is \(O((1+h)^{-1-\eta}+2^{-h})\). The pair error through \(X_n\) is \(o(\sqrt{\log X_n})\) and the triple error is bounded. This includes the diagonals and does not assume randomness of the positions of the ordinary sources.

At the polynomial crop \(y=p\omega\le n^a(3/2)^n<3^n\) for large \(n\). Thus the full rows in (2) are given directly by the least positive odd representative in [the finite IID formula](FINITE_IID_CUBIC_ENERGY.md), with its finite primitive-lap test. For (2) one may alternatively omit those targets with a positive return through \(n\), because the entire eventually-periodic contribution has zero normalized limit in the slow-source proof. Any proof of a strict upper below the corresponding coefficient using the fair scalar tail alone would miss the normalization and the multiple genuine histories at the specified representative.
