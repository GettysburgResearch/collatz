# The critical gate separates escape from periodicity

Let \(\lambda=\log_2 3\), let \(\alpha\in[\lambda,7/4]\) be an odd-clock slope, and let \(P_\alpha\) consist of the positive odd seeds satisfying \(\sum_{i=1}^j E_i\le\alpha j\) on all actual forward prefixes. Write \(F_\alpha\) for the first forward site in \(P_\alpha\), with a cemetery value if it is never met. The inverse test at a nonperiodic ordinary unit \(z\) is \(q_z^\alpha=Q_z(S_j>\alpha j\ \forall j\ge1)\).

* At the critical slope, \(F_\lambda(v)\) is finite **exactly when the ordinary orbit of \(v\) escapes to infinity**. It has a natural and reciprocal countable limiting law \(\mu_\lambda\), and the finite part has polynomial height tail. For every \(\epsilon>0\),
\[
  \mu_\lambda\{z\ {\rm finite}:z\ge M\}
       \ll_\epsilon M^{-\delta_*+\epsilon},
  \qquad \delta_*=1-H_2(\log_3 2)>0.05004 .                          \tag{1}
\]
* At **every nonperiodic unit**, including members of convergent components, there are absolute \(c>0,C_\epsilon\) such that
\[
          c/z\le d_z q_z^\lambda\le C_\epsilon z^{-\delta_*+\epsilon}. \tag{2}
\]
  For each fixed \(\alpha>\lambda\) the much sharper upper \(C_{\alpha,\epsilon}z^{-1+\epsilon}\) holds, with the same lower \(c/z\). Close to \(\lambda\) an explicit uniform loss is given below. In particular the slope cannot simply be set to critical in the strict-offset proof.
* If an escaping component exists, it has a nonperiodic unit \(m\) minimizing its corrected height among its unit vertices. It satisfies \(q_m^\lambda=1\). Consequently \(d_m\ll_\epsilon m^{-\delta_*+\epsilon}\). A single such fixed positive density is compatible with (2). On the other hand \(q^\lambda_z\to0\) on **every** escaping forward ray, including phases outside \(P_\lambda\); a pointwise rate follows from (2) and \(d_z\ge d_a>0\) downstream of a fixed unit \(a\).

## The corrected-height minimum

Any infinite positive odd trajectory which fails to escape and has no repeated state would visit a finite interval infinitely often, an impossibility. Thus the alternatives are an eventually periodic trajectory and an escaping one. On an escaping trajectory the factor
\[
  f(v)=\prod_{j\ge0}{3U^jv\over3U^jv+1}
\]
exists and is bounded below by an absolute \(c_0>0\). More generally the product over any finite segment of a nonrepeating shortcut path is at least the same \(c_0\). The original packing proof takes \(1/2<r<\log_3 2,\ c=r\log_2 3\) and counts its distinct shortcut states up to \(X\). The parity bijection and binary entropy estimate give \(N(X)\le N(3X^c)+2X^{H_2(r)}+O(\log X)\), also for finite segments with the endpoint indices paid in the logarithmic term. Induction gives \(N(X)\ll_r X^{H_2(r)}\) and dyadic summation bounds the reciprocal sum uniformly; the tail above \(M\) is \(O_r(M^{H_2(r)-1})\). The odd-map states are among these shortcut states, independently of the sizes of their gaps. The source is [Weaver, Paper 176, §5.1, directly after (26)](https://rstation.ai/problems/collatz/papers/176/v1).

Set \(V(v)=v/f(v)\) on an escaping component, where the component consists of orbits with a common future. The exact one-edge identity is \(V(Uv)=3\,2^{-E_1(v)}V(v)\); in particular \(v\le V(v)\le c_0^{-1}v\). Along an escaping orbit \(V(U^jv)\to\infty\). At \(\lambda\) a site is permanently passing precisely if all its future corrected heights are at least its own. The earliest such site is its global minimum on the forward ray, attained at finite time and unique on that ray since \(3^j\ne2^s\) at positive \(j\). Conversely an odd cycle of length \(\ell\) has
\[
        2^{A_\ell}=3^\ell\prod_{i<\ell}(1+1/(3u_i))>3^\ell.
\]
The critical debt on repeated laps goes to minus infinity; no site whose future enters a cycle is critical-permanent. This deals with every cycle, including 1.

Each \(P_\alpha\) is contained in \(P_{7/4}\subset D\); [relative sparse passage](RELATIVE_SPARSE_PASSAGE.md) gives its countable first-entry law, with uniform estimates for this entire family. Every finite \(F_\alpha(v)\) is at most \(v/c_0\): all the earlier cumulative inverse divisions to the first entry exceed \(\alpha j\), and
\[
   x=z\,{2^{S_j}\over 3^j}\prod_{u\ {\rm departing\ from}\ x\ {\rm to}\ z}
                             {3u\over3u+1}\ \ge c_0 z                 \tag{3}
\]
for every prior site \(x\) on a segment first hitting \(z\). A prior repeat on this first-arrival path is impossible. The same identity is valid on the finite path to any nonperiodic specified unit \(z\). When a shortcut path has a repeated state, all its subsequent states lie on that cycle; in the first-arrival use a full earlier lap would already have visited \(z\).

For each fixed input \(v\), \(F_\alpha(v)=F_\lambda(v)\) eventually as \(\alpha\downarrow\lambda\). On an escaping orbit its critical minimizer remains passing for every larger slope; each earlier site has a finite failing witness at \(\lambda\) and thus still fails at close enough slopes. On an eventually periodic orbit, its cycle has mean division total per lap strictly exceeding \(\lambda\), and all its phases fail permanently at slopes below that mean. Uniform label comparison at a fixed finite source cutoff then shows \(\mu_\alpha\to\mu_\lambda\) in total variation, without a uniform modulus in \(\alpha-\lambda\).

## A uniform count for sites passing to a specified target

Let \(\beta\in(\lambda,7/4]\) be fixed. For *any* target \(z\), count the sites \(y\in[Y,2Y)\) admitting a forward odd word of finite length \(j\) to \(z\) with every prefix division sum \(S_i^{\rm fwd}\le\beta i\). Then
\[
                   \#\{y\}\ll_\beta Y^{H_2(1/\beta)}.                 \tag{4}
\]
This bound also applies to the unanchored permanently passing sites, by the long-word case alone. Here is a proof retaining the total shortcut clock. Put \(L=\lfloor\log_2Y\rfloor\). If the complete division total \(s<L\), the word codes a length-\(s\) binary string with \(j\ge s/\beta\) odd departures. The last odd gap may end in arbitrary trailing shortcut-even departures, but listing all length-\(s\) binary words only overcounts. Every full word ending at \(z\) determines at most one ordinary source; count also the empty word. Summing the upper binomial tail over \(s<L\) gives \(O_\beta(2^{H_2(1/\beta)L})\) by the entropy bound and a geometric series.

If \(s\ge L\), choose the first index \(k\le j\) for which \(S^{\rm fwd}_k\ge L\). Each of its \(k\) odd departures has occurred among the first \(L\) shortcut choices since the \(k\)-th departure occurs at \(S^{\rm fwd}_{k-1}<L\). Also \(k\ge L/\beta\) by the passing condition. The first \(L\) shortcut parity bits determine one residue class modulo \(2^L\); each class meets \([Y,2Y)\) in at most three sites. The same entropy bound proves (4). This proof gives constants independent of the ordinary target, with no initial finite exception.

## Transfer from a supercritical test

For a fixed \(\beta>\lambda\), the proof of the [ordinary exponent theorem](ORDINARY_NO_RETURN_EXPONENT.md) applies on replacing \(7/4\) by \(\beta\). The counting constants now involve \(\omega_\beta=2^{\beta-\lambda}>1\) and \(C_\beta=[3(\omega_\beta-1)]^{-1}\). The selected physical lower bound \(c/z\) is unchanged as the \(7/4\) no-return event is contained in the \(\beta\) no-return event. The bound for the target-stopped labels is uniform over \(z\), also by (4). Quantitatively, if \(h=\beta-\lambda\), \(hz\ge C\) for a sufficiently large absolute constant, and \(Y\ge z\), the maximum inverse depth of a strict ancestor in \([Y,2Y)\) is \(O(h^{-1}(1+\log(2Y/z)))\) and there are \(O(1+Y/(hz))\) sources per depth and total. Combining with (2) of the relative sparse-passage note as before gives
\[
 d_zq_z^{\lambda+h}\ll_\epsilon h^{-2}z^{-1+\epsilon}
       \quad(0<h\le7/4-\lambda,\ hz\ge C).                          \tag{5}
\]
The constants in this application of the relative law can use the common \(D\) above the finite region \(z^2+1\), exactly as in the ordinary exponent note; (4) gives an alternative. With \(h=z^{-s},0<s<1/2\), (5) still gives a polynomial saving. The expression \(h^{-2}\) prevents taking \(h=0\) here.

At the critical slope, use the *target-stopped* first passing-to-\(z\) labels of the ordinary exponent note, for both slopes \(\lambda,\beta\). They have countable laws by (4). For fixed nonperiodic \(z\), if an ordinary source reaches \(z\) strictly above the critical reverse barrier at every positive prefix, its first \(\beta\)-passing-to-\(z\) site \(y\) occurs on this very path. Every prior site \(y\), as well as \(z\), satisfies \(y\ge c_0z\) by (3). At each unit \(y\) passing to \(z\), the limiting mass of the cell with *first* such label \(y\) is exactly \(d_yq_y^\beta\): a prior site passes to \(y\) precisely when it passes to \(z\), since \(y\)'s entire continuation to \(z\) passes and the debt accumulated up to \(y\) is nonnegative on a passing word. Thus it is the same strict-prefix event at \(y\). The countable label law justifies summation over cells; a nonunit cell is supported only at its own single source. The fixed-root limiting identity at \(\lambda\) follows by the unique-depth and tightness argument in the ordinary exponent note. It follows that
\[
 d_zq_z^\lambda \le
    \sum_{\substack{y\ge c_0z\\y\ {\rm unit\ passing\ to}\ z\ {\rm at}\ \beta}}
                  d_yq_y^\beta
       \ll_{\beta,\epsilon} z^{H_2(1/\beta)-1+\epsilon},               \tag{6}
\]
using the supercritical pointwise upper and summing (4) over dyadic octaves. For (1), if \(F_\lambda(v)=z\) is finite, \(F_\beta(v)\) occurs no later on the same actual path and is at least \(c_0z\). Bound the collective tail of its law using (4) for \(P_\beta\) and the supercritical atom upper; only its unit sites have nonzero mass. To get (1)–(2), given an ultimate \(\epsilon>0\) choose one *fixed* \(\beta>\lambda\) close enough that \(H_2(1/\beta)<H_2(1/\lambda)+\epsilon/2\), and use the other half in the supercritical upper. No uniformity of those constants at \(\lambda\) is asserted or needed.

Finally an escaping component has unit vertices, with \(V(v)\ge v\), so its unit \(V\)-minimum is attained among finitely many candidates below any initial bound. Different unit minimizers could be incomparable. At any minimizer \(m\), every unit inverse path has \(V(x_j)>V(m)\) at each positive depth, strictly by \(3^j\ne2^{S_j}\). Hence \(q_m^\lambda=1\) and (2) applies. For a moving unit \(z\) on the same escaping ray, its ordinary predecessor density is at least \(d_a>0\) past a fixed unit \(a\), so (2) forces \(q_z^\lambda\to0\). Even qualitatively, the inverse cylinder of any earlier ray site of smaller corrected height excludes the no-return event. As \(V(z)\to\infty\), one can choose earlier such sites with indices tending to infinity; nested basin densities on the ray converge and the corresponding cylinder probabilities tend to one. Selecting forward minima does not reverse this concentration. The fixed minimizer and the moving high phases therefore give no incompatibility from the available lower floor \(c/z\).
