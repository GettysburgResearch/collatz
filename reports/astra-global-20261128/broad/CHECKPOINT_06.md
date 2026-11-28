# Broad track, checkpoint 6

## Which inverse stationary laws can a bounded mean gap reproduce?

`FROZEN_MARGINAL_TRANSPORT.md` identifies the exact positive-distance transport problem on the doubling logarithm modulo $N_w=2\cdot3^{w-1}$. For a width-independent ternary law $\nu$, prescribe the width-$w$ stationary marginal to be its $w-1$ low digits plus one uniform new trit. Write $A_W$ for the largest minimum required mean gap at widths $2$ through $W$, and $M$ for the largest $(W-1)$-digit atom of $\nu$. Exact directed transport gives
$$
 2(N_W-2)A_W\ge N_W L M-L^2-1\qquad(1\le L\le N_W).
$$
For the critical iid geometric Syracuse law, the fixed signed ray $-1$ supplies mass at least $\theta_*^{W-1}$. The prescribed costs are exponentially unbounded along a subsequence, even though optimized finite policies have mean gap at most four. More generally, for arbitrary bounded-cost stationary policies at successive widths, a two-sided uniform comparison $l\nu_{w-1}\le\lambda^{(w)}\le u\nu_{w-1}$ with critical $\nu$ requires $u/l\ge3^{(1-2d)/(1-d)}$, where $d=-\log_3\theta_*$. The numerical value is approximately $1.21538639$. This concerns relative errors on every working-precision cylinder. The unrestricted optimal inverse pressure and its critical endpoint remain open.

The root reviewer independently reconstructed the positive-distance flow identity, geometric specialization, multiconductor Fourier estimate, rational tent argument and varying-marginal proof. The three Lean modules `CyclicTent.lean`, `CyclicMarginalTransport.lean` and `CyclicAtomBound.lean` strictly compiled against Lean 4.34.1. The final checked inequality uses finite flows with coherent demand and a uniform exposed trit. The geometric-law application and variable-comparison exponent are written arguments. Normal and optimized runs of `check_cyclic_transport.py` produced identical outputs with active explicit guards across 16 stationary transports, 1,264 positive FIFO packets, 5,808 rational tent inequalities and 960 atom bounds.

## Scores with a genuinely infinite digit context

`INFINITE_DIGIT_CONTEXT_RANKING.md` extends the root's finite-window theorem to every integer radix and two-sided digit observables satisfying $\operatorname{var}_r g=O((1+r)^{-P})$ with $P>2+D(D+3)/2$, where $D$ is the polynomial degree of the positional weights. This includes exponentially decaying infinite-range dependence. Finite upper drift allowances on both actual parity branches force $F(n)=\gamma L_p(n)+O(1)$. A lower-bounded score in this class cannot have uniformly negative odd drift and finite even allowance. Without a lower bound, a negative odd drift $-\varepsilon$ and even allowance $a$ occur exactly if $a\ge\varepsilon\log2/\log(3/2)$.

The proof uses an explicit full-support maximizing-measure coboundary on the pure digit shift, with a loss of two powers in the variation estimate. It then sums both infinite sentinel tails uniformly and transfers the residual leading-digit terms into lower-degree padded observables. Finite cylinder approximations are used only to pass to normalized expectations. The root reviewer independently reconstructed the cohomology, sentinel-tail estimates, regularity induction and sharp drift classification. The infinite-context argument is written mathematics.
