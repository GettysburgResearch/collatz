# The contraction rates of positive cycles in a single spatial and temporal limit

The signed original-word Poisson statistic has a macroscopic limit in which each positive cycle contributes its ordinary basin density at its own transition time. The first jump comes from 1. It occurs exactly where the Fourier cutoff crosses the mean total of the independent geometric exponents. Its size is the density of convergence to 1, whose value remains open. The statements use the ordinary source and the passage and density results specified below.

Use the signed odd map, finite statistic \(\mathcal D_k\), Fourier convention and unnormalized Poisson kernel of [the specified-source formula](POISSON_SOURCE_PROBE.md). Put \(D=\log(4/3)\), with natural logarithms. For every positive odd cycle \(L\) let \(d_L\) be the relative odd natural density of its full ordinary basin and put
\[
 \lambda_L=\frac{1}{|L|}\sum_{y\in L}\log(1+1/(3y)).
\]
The multiplier of one lap is \(\exp(-|L|\lambda_L)\). This follows by telescoping the height ratios along its actual steps. In particular \(\lambda_{\{1\}}=D\), whereas every other cycle has \(\lambda_L\le\log(10/9)<D\) since its odd vertices are all at least three. The relative odd and all-integer basin densities agree by stripping initial powers of two.

Let \(g\) be Schwartz with integral zero and \(I=\int_0^\infty g(u)\,du\ne0\). Take \(g_R(u)=R^{-1}g(u/R)\), \(k=\lfloor C\log R\rfloor\) for fixed \(C>0\), and \(t_R=R^{-\beta}\) for fixed \(\beta>0\). At every \((C,\beta)\) with \(\lambda_L(C-1/D)\ne\beta\) for all positive cycles of positive basin density,
\[
 \lim_{R\to\infty}\mathcal D_k(g_R,t_R)
   =-\frac{\pi I}{2}\sum_L d_L\,
          \mathbf1_{\{\lambda_L(C-1/D)>\beta\}}.                         \tag{1}
\]
For \(t_R=1/\log R\), the limit is zero for \(C<1/D\), and it is \(-\pi I\sum_Ld_L/2\) for \(C>1/D\). This second comparison includes every positive cycle regardless of its contraction rate.

## Ordinary proof on the same signed sources

The fixed-ratio ordinary input is the following. For each fixed odd periodic target \(b\), the proportion in any fixed annulus \([uR,vR]\), \(0<u<v<\infty\), of positive odds reaching \(b\) but with odd first-hit time outside \((1/D\pm\epsilon)\log R\) tends to zero. The upper side follows from the fixed-floor passage argument in the cited central deadline proof. First choose a large floor \(K\ge b\). Outside upper relative error \(O((\log K)^{-2})+o_R(1)\), a shortcut passage to the floor takes at most \((2/D)\log R+O(\sqrt{\log R\log\log R})\) steps. A source reaching \(b\) has one of the finitely many successful landing states at most \(K\), then reaches \(b\) in a fixed additional number of steps bounded in terms of \(K,b\). The lower side follows from the one-arm exclusion against the full prescribed orbit of \(b\) in the same annuli, or from the typical first passage to the intermediate polylogarithmic floor there. To convert the shortcut time \(h\) of the first hit to its odd count \(j\), use \(b=x3^j2^{-h}\exp(E)\), with \(E=\sum\log(1+1/(3x_i))=O(1)\) on a simple first-hit prefix. The identity \(2\log2-D=\log3\) gives the stated coefficient. Restricting to odd sources costs a bounded factor. Take \(R\to\infty\) before \(K\to\infty\). The same sources establish that a positive typical source's eventual component has a tight countable density law, equivalently obtained by pushing forward the tight orbit-minimum law. [Prior fixed-floor passage](../../astra-ordinary-boundary-20261124/transfer/ALL_EVENTUAL_MEETINGS.md) · [One-arm lower clock](../../astra-ordinary-boundary-20261124/transfer/MEETING_CLOCKS.md) · [Minimum and terminal-law inputs](https://rstation.ai/problems/collatz/papers/175)

The exact source identity gives
\[
 \mathcal D_k(g_R,t_R)=\frac1R\sum_{x\in2\mathbb Z+1}
       (g*P_{t_R/(R A_k(x))})(x/R).                                      \tag{2}
\]
The row bound in the specified-source proof is uniform over all widths and here gives \(C_g(1+|x|/R)^{-2}/R\). We can discard \(|x|>MR\) at cost \(O_g(1/M)\) and \(|x|<\varepsilon R\) at cost \(O_g(\varepsilon+1/R)\). Throughout each remaining annulus, \(R/|x|\) stays bounded above and below.

For negative odd \(x\), the real affine intercept \(B_w\ge0\) gives \(A_k(x)|x|\ge |U^k x|\ge1\). For any simple positive prefix, the uniform reciprocal packing bound gives
\[
 A_k(x)x=U^kx\prod_{i<k}(1+1/(3U^ix))^{-1}\ge c
\]
with an absolute \(c>0\). This covers every escaping row for all \(k\). On all these rows the width in (2) tends uniformly to zero, so they read \(\pi g(x/R)+o(1)\) before the factor \(1/R\). This uses the usual uniform convergence of the Poisson approximation to a bounded uniformly continuous function as the width tends to zero.

For a fixed periodic basin choose one odd state \(b\) on the cycle. At the first hit \(j\) of \(b\) we have \(cb\le A_j(x)x\le b\), with a possible unit adjustment for a source already on the cycle. A partial path before that first hit has distinct states. In fact a first hit of a periodic state cannot have an earlier repetition without having traversed that state's whole cycle. On the remaining portion of length \(m\), the exact cycle multiplier is \(\exp(-\lambda_L m+O_L(1))\). Consequently if \(C>1/D\), then in relative probability on the given basin in the annulus,
\[
   \frac{\log(RA_k(x))}{\log R}\longrightarrow -\lambda_L(C-1/D).       \tag{3}
\]
For \(C<1/D\) almost every such row is still simple. At \(C=1/D\) the number of post-hit steps is \(o(\log R)\) in relative probability, and any pre-hit row retains the same positive lower bound on \(RA_k\). This suffices for the width in (2) to tend to zero when \(\beta>0\).

At the strict comparison in (1), each periodic basin therefore has rows converging in probability either to \(\pi g(x/R)\) or to zero, the latter by \(\|g*P_s\|_\infty\le\|g\|_1/s\) when \(s\to\infty\). For \(t_R=1/\log R\) every fixed periodic basin has vanishing rows after the clock \(1/D\). Discard all but finitely many periodic basins with arbitrarily small upper density error using tightness. A finite union with density \(d\) contributes \(d/2\) times the Riemann integral on the positive half line when its rows read \(g(x/R)\), by partial summation. Taking the zero-width value on all signed odd integers would give zero, since \(\int g=0\). Subtracting the missing positive sectors gives (1), including the stated subpower choice. No assertion about negative component densities is necessary.

## Location of the first jump in the actual Fourier sum

One may choose \(g\) with a smooth compact Fourier transform supported at \(a\le|\xi|\le b\), for some \(0<a<b\). For example take \(g=\psi'\) with \(\psi\) Schwartz of such Fourier support and \(\psi(0)\ne0\). Then \(I=-\psi(0)\). In the binary word formula the amplitudes are \(\widehat g(R\ell/2^{d+1})\), where \(d\) is the exact total of the original geometric word. Its damping is at most
\[
 \exp\{-2\pi a\,2^{d-k\log_2 3-(1+\beta)\log_2R}\}.
\]
For fixed \(C,\beta\), the sum over totals exceeding \(k\log_2 3+(1+\beta)\log_2R+2\log_2(k+2)\) tends to zero absolutely. The number of contributing frequencies at each total is \(O(1+2^d/R)\), there are at most \(2^d\) such words, and their original probability is \(2^{-d}\) each. Beyond the displayed cutoff the superexponential damping dominates the exponentially growing prefactor.

Hence the first transition in (1), at \(C=(1+\beta)/D\), lies where the leading Fourier cutoff equals \(2k\), the mean of the original iid total. For \(C\) just below this value the limit is zero. Just above it, and before \(1/D+\beta/\log(10/9)\), the limit is \(-\pi I d_{\{1\}}/2\). For \(t_R=1/\log R\) the leading cutoff instead passes through \(2k\) at \(C=1/D\). This yields two different transitions from the same word law. An evaluation of the first jump as \(-\pi I/2\) would establish full convergence using all-unit positive predecessor density. The current pointwise and averaged Fourier estimates for the conditioned binary source law do not evaluate its signed sum over frequencies in this spatial scaling. [Specified-source sums and Fourier obstruction](POISSON_SOURCE_PROBE.md) · [Count-conditioned binary estimate](https://rstation.ai/problems/collatz/papers/42)
