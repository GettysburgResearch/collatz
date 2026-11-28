# The ordinary grid consumes a ternary denominator in its fair physical time

**Written theorem, conditional on the published real small-ball bound identified below.** For an integer \(u\) sampled uniformly through \(2^k3^r\), form the actual parity trajectory of \(u/3^r>0\). Let \(\sigma_r\) be the number of shortcut steps through its \(r\)-th odd departure. For every fixed \(C_0,D>0\), uniformly for \(1\le r\le C_0 k\),
\[
 \Pr\left(|\sigma_r-2r|>C_{C_0,D}\sqrt{k}\,(\log(k+2))^2\right)
       =O_{C_0,D}(k^{-D}).                                           \tag{1}
\]
This includes \(r>k/(2-\log_2 3)\), where a single complete binary prefix need not reach the \(r\)-th odd. All probabilities in (1) are for ordinary uniform numerators, including numerators divisible by three. The \(r\)-th odd is a specified stopping date even when a reduced denominator reaches one earlier.

The proof restarts on a smaller lattice once a complete block of numerator bits is exhausted. Its cost is polynomial per block and the remaining denominator degree contracts geometrically. The post-entrance orbit of the resulting **ordinary positive integer** remains unrestricted.

## A spatially weighted real concentration estimate

Let \(f_0(x)=x/2,\ f_1(x)=(3x+1)/2\). Let \(R\) have the nonnegative real stationary affine law under independent fair bits, defined by the outer composition. Write \(a_i=1/2\) or \(3/2\), \(b_i=0\) or \(1/2\), \(A_0=1,\ A_j=\prod_{i=1}^j a_i\). Then
\[
 R=\sum_{j\ge0} A_j b_{j+1},\qquad
 R=B_j+A_j R',\qquad
 \mathbf E A_j^\alpha=\rho_\alpha^j,\quad
 \rho_\alpha=(1+3^\alpha)/2^{1+\alpha}<1\quad(0<\alpha<1).
\]
Here \(R'\) is independent of the first \(j\) branches. The input is Weaver's uniform estimate \(\sup_x\Pr(R\in[x,x+\epsilon])\ll\epsilon\log(e/\epsilon)\) for \(0<\epsilon\le1\). The cited proof obtains the real bound by covering the ternary coordinate in a joint small-ball estimate. [Weaver 19/v2, equations (S2), (Q7)](https://rstation.ai/problems/collatz/papers/19/v2)

For fixed \(0<\alpha<1\), this implies
\[
 \Pr(R\in[x,x+\epsilon])\ll_\alpha
   {\epsilon\log(e/\epsilon)\over(1+x)^{1+\alpha}}
 \qquad (x\ge0,\quad 0<\epsilon\le1).                               \tag{2}
\]
For \(x\ge1\), choose \(c>0\) so that \((c/2)\sum_{j\ge0}(j+1)^{-2}<1\). If \(R\ge x\), one of the prefix events \(A_j\ge cx/(j+1)^2\) occurs. On this event condition on the first \(j\) letters and apply the uniform bound to the independent \(R'\) on an interval of length \(\epsilon/A_j\). For intervals longer than one, the trivial probability bound is dominated by \(C(\epsilon/A_j)\log(e+A_j/\epsilon)\) as well. Since \(A_j\le(3/2)^j\), the logarithm is at most \(C(1+j+\log(1/\epsilon))\). On the prefix event,
\[
 A_j^{-1}\le A_j^\alpha \bigl((j+1)^2/(cx)\bigr)^{1+\alpha}.
\]
The resulting sum is bounded by the right side of (2) times a finite polynomial-geometric series in \(j\). The original uniform bound handles \(x<1\). In particular periodization over positive integer translates costs only the displayed logarithm.

## An exact restart on a smaller numerator lattice

Write \(\mu_{N,r}\) for the uniform law on the numerators \(1\le u\le S=N3^r\), with \(N\) a positive integer. Let \(L=\lfloor\log_2 S\rfloor\). The first \(L\) bits of \(u/3^r\) have density at most two relative to independent fair bits, since the parity word is a triangular permutation of the residues modulo \(2^L\). No approximation error from an incomplete period is needed for this upper bound.

In the subpopulation where \(q=Q_L<r\), write \(j=r-q\) and \(v=3^j T^L(u/3^r)\). This is a positive integer. For every \(v\) there is an exact atom formula
\[
 \Pr_{\mu_{N,r}}\{Q_L=q,\ 3^jT^L(u/3^r)=v\}
 ={1\over 3^jY}\Pr_{\rm fair}\{|w|=q,\ v/3^j-Y\le B_w<v/3^j\},
 \quad Y=N3^q/2^L\in[3^{-j},2\cdot3^{-j}).                       \tag{3}
\]
Here \(F_w(x)=A_w x+B_w\) with \(A_w=3^q2^{-L}\). Indeed the unique possible numerator for this \(w,v\) is \(u=2^Lv-3^j C_w\), where \(C_w=2^L B_w\). Its correct binary class follows by the usual inverse parity induction. Its allowed range is exactly the interval in (3). Each fair word has mass \(2^{-L}\), and \(3^jY=S/2^L\).

Let \(R'\) be an independent stationary real seed. For an absolute \(p_0>0\), \(\Pr(0\le R'\le1)=p_0\): a finite real interval has positive stationary mass and a sufficiently long initial run of zero branches sends it into \([0,1]\). On the word event in (3) and \(R'\le1\), the stationary endpoint \(F_w(R')\) lies in \([v/3^j-Y,v/3^j+Y]\), because \(A_w=Y/N\le Y\). After removing the event \(|w|=q\), the law of \(F_w(R')\) is stationary by independence and iteration. Estimate (2), splitting an interval of length \(2Y>1\) into boundedly many pieces when necessary, proves
\[
 \Pr_{\mu_{N,r}}\{Q_L=q,\ v\}
 \le C_\alpha(1+j)\,\pi_j(v),\qquad
 \pi_j(v)=3^{-j}(1+v/3^j)^{-1-\alpha}.                              \tag{4}
\]
If the lower real endpoint is negative, use the uniform estimate at zero and \(v/3^j=O(1)\). This is an unnormalized joint bound for each count and endpoint. No conditional probability is divided by a small binomial atom.

To restart with an ordinary uniform numerator, note the elementary majorization
\[
 \pi_j(v)\le C_\alpha\sum_{\ell\ge0}2^{-\alpha\ell}\,
                              \mu_{2^\ell,j}(\{v\}).                 \tag{5}
\]
Use just \(\ell=\max(0,\lceil\log_2(v/3^j)\rceil)\) on the right. The full majorant in (4) summed over \(q<r\) and \(\ell\) in (5) has total coefficient at most \(C_\alpha(r+1)^2\), independently of the incoming \(N\).

## Iteration and final deterministic steps

All constants below may depend on \(C_0,D\); take \(k\) large. At each retained block use the actual initial bits through \(L\) and discard the exceptional event
\[
 \max_{0\le s\le L}|Q_s-s/2|>\sqrt L\,(\log(k+2))^2 .
\]
Its mass under that uniform block is \(O(\exp(-c(\log k)^4))\) by the pointwise density bound of two and the fair maximal Hoeffding inequality. If the \(r\)-th odd occurs within this block, that prefix already proves the desired clock estimate up to its displayed block error. Otherwise \(q<r\). Split by \(q\) and use (4)–(5) for the new source. Discard all terms \(\ell>(\log(k+2))^3\); their total coefficient is at most \(C(r+1)^2\exp(-c(\log k)^3)\). For each retained new block, \(N=2^\ell\) and \(\log_2 N\le(\log(k+2))^3\). Use the new \(j\) as its denominator degree.

While the current degree \(r\ge (\log(k+2))^8\), the retained block has \(L\ge(\log_2 3)r-1\), and the fair deviation bound is at most \(L/10\) for all sufficiently large \(k\). Thus \(q\ge 2L/5\) and the next unfinished degree \(j=r-q\le r/2\) since \((2/5)\log_2 3>1/2\). There are \(O(\log k)\) such blocks. The initial block always has \(L=O_{C_0}(k)\). Every subsequent one has \(L\le(\log_2 3)r+(\log(k+2))^3\), with \(r\)'s geometrically decreasing while the iteration runs. The sum of the square roots of these block lengths is \(O_{C_0}(\sqrt k)\). Thus the absolute clock errors of all completed blocks and the final partial native block sum to \(O_{C_0}(\sqrt k(\log(k+2))^2)\).

If an unfinished degree \(1\le r<(\log(k+2))^8\) is reached **after a restart**, the retained numerator has \(u\le 2^{(\log(k+2))^3}3^r\). Until the \(r\)-th odd departure, the formal numerator update at remaining degree \(j\ge1\) is \(u\mapsto u/2\) on even inputs and \(u\mapsto(u+3^{j-1})/2\) on odd inputs, with degree dropping only in the latter case. All future numerators are at most \(\max(u,3^r)\). Consecutive odd departures are consequently at most \(1+\lfloor\log_2\max(u,3^r)\rfloor\) steps apart. This final segment has at most \(O((\log(k+2))^{16})=o(\sqrt k)\) steps. For initial degrees below the cutoff, run the initial native block first: if it remains unfinished, the same terminal argument applies after the first restart.

The full coefficients in each positive majorant grow by at most \(C(C_0k+1)^2\), for \(O(\log k)\) rounds. Hence their accumulated factor is \(\exp(O_{C_0}((\log k)^2))\). This is absorbed by both displayed exceptional errors, leaving \(O_D(k^{-D})\) after summation. The physical source follows its exact trajectory in every accepted block; uniform majorants only bound the propagated exceptional sets. This proves (1).

## Consequence for the moderate tail

Keep \(m=\lfloor\kappa k+g\rfloor\), \(H=\lceil m/2+ag\rceil\), \(g=k^\gamma,\ \gamma>1/2\), \(r_*=\kappa k/2\), in the [denominator ladder](MODERATE_DENOMINATOR_LADDER.md). If \(r\le H\) and the high-tail event occurs, then \(\sigma_r\le m\) and \(H\le r+(m-\sigma_r)\). Thus for every fixed \(v>1/2-a\) with \(r=\lfloor r_*+vg\rfloor\le H\), equation (1) gives \(P_r=O_D(k^{-D})\). The new upper bound follows from actual rational entrance clocks, while the elementary \(r=H\) anchor remains available without the real small-ball input.

The law of the integer at entrance and its subsequent parity bias have separate roles. Equation (1) determines the physical date of entrance sufficiently accurately to make the residual duration \((1-2v)g+o(g)\) for \(r=r_*+vg\) with \(v<1/2\). It leaves the parity sum on this genuine integer suffix open. Positive real affine regularity alone does not set that suffix's mean equal to one half.
