# Testing an ordinary positive drift certificate

Take the shortcut map \(T(2n)=n,\ T(2n+1)=3n+2\) on the positive integers. The proposed certificate is a positive function \(w(n)\) tending to zero at infinity and satisfying, for every \(y\) above a verified floor \(M\),
\[
 w(y)> w(2y)+{\bf1}_{y\equiv2\ (3)}w((2y-1)/3).
\]
This would prove **unrestricted** descent to the verified floor. Along a trajectory that stays above \(M\), the weight strictly increases. A repetition contradicts strict increase; an injective positive trajectory tends to infinity, where the weight tends to zero. This proof requires only vanishing at infinity, a weaker condition than summability. In particular positivity, pointwise finiteness, and a strict local surplus without control at infinity do not suffice.

## An attempted construction

On the ternary integers define the positive transfer
\[
 (L_s h)(y)=2^{-s}h(2y)+(3/2)^s{\bf1}_{y\equiv 2\ (3)}h((2y-1)/3).
\]
Haar measure gives \(\int L_s h=\lambda_s\int h\), where \(\lambda_s=2^{-s}+(3/2)^s/3\). Multiplication by two preserves Haar measure. On the second branch the domain is one ternary cylinder, mapped affinely onto the entire space with Haar mass factor \(1/3\). Strict convexity and \(\lambda_1=\lambda_2=1\) give \(\lambda_s<1\) for \(1<s<2\). With \(1<t<1/\lambda_s\), the nonnegative series \(G_{s,t}=\sum_{k\ge0}t^kL_s^k1\) is Haar-integrable and \(L_sG_{s,t}=(G_{s,t}-1)/t\) wherever finite.

If this profile were finite on the ordinary positive integers and \(G_{s,t}(y)=o(y^s)\) there, then \(w(y)=G_{s,t}(y)/y^s\) would satisfy the displayed certificate for every sufficiently large \(y\). The odd-branch ratio needed in the physical inequality is at most \((1-1/(2y))^{-s}\) times the leading-order factor in \(L_s\); taking \(y\) large enough makes this smaller than \(t\). The threshold is explicit from \(s,t\) and the values below it can be checked separately. For example \(s=3/2\), \(t=51/50\) gives \(t\lambda_s<1\) and \(y\ge40\) suffices. This reduces the construction to the stated ordinary growth estimate with no restrictions on the parity word.

The untilted \(G_{s,1}(y)\) is finite at every ordinary \(y\). For a nonperiodic endpoint a particular ancestor \(b\) occurs at most once, and its product of leading forward coefficients is at most \(y/b\), since all forward additive terms are nonnegative. This gives \(G_{s,1}(y)\le y^s\zeta(s)\), the previously recorded estimate. At a periodic endpoint, the same bound on the first arrival and the cycle multiplier \(R<1\) give \(G_{s,1}(y)\le y^s\zeta(s)/(1-R^s)\). Here strict \(R<1\) follows because the cycle has at least one odd step, hence a strictly positive additive term.

## Why smoothing the ordinary trace fails

To preserve all the ordinary inverse edges simultaneously one might evaluate the Haar profile at perturbed arguments \(n+\delta_n\) in place of \(n\). The required affine compatibility would be \(\delta_{Tn}=3^{[n\ {\rm odd}]}\delta_n/2\). The only such family with every \(\delta_n\in\mathbb Z_3\) is zero. Indeed an odd positive ternary unit \(y\) has unit-preserving accelerated ancestors at every odd depth. Choose exponents from \(1,3\) if \(y\equiv2\bmod3\), or \(2,4\) otherwise: both choices give an integer predecessor and at most one gives a multiple of three. Iterating shows \(\delta_y\in3^j\mathbb Z_3\) for every \(j\). Even unit endpoints also have zero shift by division by two. Ordinary multiples of three reach a unit after at most their initial even divisions and one odd step, so their shifts vanish by the same compatibility. In particular a common random perturbation with exact affine transport cannot use the Haar-a.e. finite profile to obtain its ordinary trace.

The untilted pointwise bound loses exactly the power \(y^s\) needed for the certificate. Moreover a fixed ordinary source \(b\) following an escaping trajectory contributes at its \(k\)-th forward endpoint \(y\) at least the single term
\[
 \frac{G_{s,t}(y)}{y^s}\ \ge\
 \frac{t^k}{b^s}
 \prod_{\substack{0\le j<k\\T^j b\text{ odd}}}
       (1+1/(3T^j b))^{-s}.
\]
On any escaping ordinary path that product is subexponential: its log divided by \(k\) tends to zero because \(T^j b\to\infty\). Thus at any \(t>1\) the normalized profile would grow exponentially on such a path, even without a reciprocal-summability theorem. This isolates the exact positivity issue: the Haar resolvent tolerates these spikes, while the required ordinary \(c_0\) estimate would eliminate every escaping path. I obtained no proof of that estimate or of universal descent. This construction is an attempted full-domain certificate; it provides no new excluded family of initial sources.

The earlier odd-map trace obstruction is in [CENTRAL_CLOSURE.md](../astra-high-variance-20261124/CENTRAL_CLOSURE.md). The operator used here is a positive weighted inverse transfer. The known absence of nontrivial fixed points in the Hardy space in Neklyudov's operator approach does not give a bound on this ordinary trace. In particular an invariant component indicator has infinitely many coefficients equal to one because it contains every dyadic multiple of each of its elements. [Neklyudov, *Functional analysis approach to the Collatz conjecture*](https://arxiv.org/abs/2106.11859).

## A source-dependent smoothing with an exact ordinary recurrence

Let \(\mu_j\) be Haar probability on \(3^j\mathbb Z_3\). For \(0<r<1\) take the absolutely continuous noise law \(\nu=(1-r)\sum_{j\ge1}r^{j-1}\mu_j\) and average the Green profile at \(y+\delta\) over \(\delta\sim\nu\). Multiplication by 2 preserves \(\nu\). Multiplication by \(2/3\) sends it to \(r\nu+(1-r)\mu_0\). Thus this smoothing allows controlled edge loss instead of demanding exact coherent perturbations.

Write \(g_N(y)\) for the average of the Green sum through depth \(N\), and \(H_N=\sum_{k=0}^N(t\lambda_s)^k\). At *every ordinary* \(y\),
\[
 g_{N+1}(y)=1+t2^{-s}g_N(2y)+t(3/2)^s{\bf1}_{y\equiv2\ (3)}
 [r g_N((2y-1)/3)+(1-r)H_N].
\]
All terms at a finite horizon are integrals of bounded cylinder functions; the formula follows by the two pushforward identities. Put \(d=-\log_3 r,\ \sigma=s-d,\ \tau=t2^{-d}\). The two coefficients multiplying \(g_N\) are exactly those of \(\tau L_\sigma\) on ordinary vertices. The remaining positive forcing is between 1 and \(K=1+t(3/2)^s(1-r)/(1-t\lambda_s)\). Hence the limiting \(g\) is bounded above and below by respectively \(K\) and 1 times the ordinary series \(\sum_{k\ge0}\tau^k L_\sigma^k1\), including infinite values.

For \(\sigma>1,\tau<1\) this **proves** \(\sum_y y^{-\sigma}g(y)\le K\zeta(\sigma)/(1-\tau)\). For each fixed \(k\), sum first over the positive origins \(b\). Each maps to one endpoint \(y\), and \((3^u/2^k)^\sigma/y^\sigma\le b^{-\sigma}\) by positivity. This range gives the desired decay, but loses the coefficient surplus. At \(\tau>1\) the surplus is available, and the fixed-origin escaping-path estimate above applies with \(s,t\) replaced by \(\sigma,\tau\). At \(\tau=1\) the geometric series proof supplies no finite bound. An integrable trace with a surplus has not resulted.

A uniform Hölder estimate for this candidate cannot bridge the gap. For \(1<p<\infty\), the density of \(\nu\) belongs to \(L^{p'}\), \(p'=p/(p-1)\), only if \(d>1/p\): on valuation shell \(j\) it equals \((1-r)\sum_{\ell=1}^j r^{\ell-1}3^\ell\), and the shell has mass \(2/3^{j+1}\). On the other hand \(G_{s,t}\ge [t(3/2)^s]^j\) on \(-1+3^j\mathbb Z_3\) by the all-odd inverse word. Summing over exact valuation shells around \(-1\) forces \(t(3/2)^s<3^{1/p}\) for \(G_{s,t}\in L^p\). Positive \(\sigma\) and \(\tau>1\) give \(s>d,\ t>2^d\), hence \(t(3/2)^s>3^d>3^{1/p}\). This disproves this particular global Hölder construction; the following estimate instead controls all repeated words using the positive integer endpoint.

## A physical bound on all powers of words

For \(s=7/4,\ t=101/100\), let \(q=t/2^s\). Take any positive endpoint \(y\), and consider the sum of \(y^{-s}t^k(3^u/2^k)^s\) over all admissible binary inverse histories of length \(k\) which in forward order are \(W^j\) for a nonempty word \(W\) and \(j\ge2\); here \(u\) counts all odd steps of the history. Omit stationary histories for which one copy of \(W\) fixes \(y\). The resulting sum tends to zero as \(y\to\infty\), uniformly over ordinary positive integers. For nonperiodic endpoints the omission is empty. The result covers all word lengths at once and does not require a restriction on the source itinerary. It controls just the imprimitive-word part of the Green series.

Indeed, write \(h=|W|,\ v=\#\mathrm{odd}(W)\), and \(C\) for the carry in the forward affine map \((3^v x+C)/2^h\). We have \(C\le2^{h-v}(3^v-2^v)\): moving an odd bit one slot later past an even bit increases its carry contribution, so the maximum is attained with all odd bits last. For \(v=0\) the bound reads zero. For \(j\) repetitions with a positive integer origin \(b\), set \(D=2^h-3^v\ne0\). Iterating gives
\[
 2^{hj}(D y-C)=3^{vj}(D b-C).
\]
If the left factor \(D y-C\) is zero then \(y\) is stationary for \(W\). Otherwise \(3^{vj}\le |D y-C|\le 3\,2^h(3/2)^v y\). Consequently the normalized contribution of that word is at most
\[
 3^s 2^{sh}(3/2)^{sv}q^{hj}.
\]
Summing the binomial multiplicities over \(v\) gives \(3^s[(2^s+3^s)q^j]^h\). Summing \(j\ge2\) and \(h\ge H\) gives at most
\[
 \frac{3^s}{1-q}\,\frac{\rho^H}{1-\rho},
 \qquad \rho=(2^s+3^s)q^2<1.
\]
The inequalities are strict with rational bounds: \(3.36<2^{7/4}<3.37,\ 3^{7/4}<6.85\) by taking fourth powers, so \(\rho<(3.37+6.85)(1.01/3.36)^2<1\). Also \(t\lambda_s<1\), since \(2^{7/4}>3.36\) and \((3/2)^{7/4}<2.04\), checked by fourth powers. Double counting powers with multiple representations only increases the upper bound. For each fixed pair \((h,j)\) the finitely many words give a sum \(O_{h,j}(y^{-s})\); summability of the double majorant gives the asserted limit. The remaining unrestricted primitive histories have no repeated-word divisibility of this size. No estimate here bounds their total normalized contribution, or excludes stationary positive cycles.

**Arbitrary flanks.** At a nonperiodic endpoint the same \(c_0\) result holds for the summed contribution from all words \(U W^j V\) with \(j\ge2\) and \(|U|+|V|\le |W|/25\). Write \(a=|U|,c=|V|\), and \(z\) for the ordinary endpoint of the powered portion. Positivity gives \(y\ge A_V z\), with \(A_V\) the product of the leading forward coefficients on \(V\); the extra prefactor is therefore bounded by \([t(3/2)^s]^a t^c\). A stationary powered portion would put \(z\), and hence \(y\), on a cycle. The core estimate applies uniformly to \(z\). There are at most \(2^{a+c}\) choices of the two flanks and \((h+1)^2\) choices of their lengths. Thus the previous exponential majorant after summing \(j\) acquires a factor at most \((h+1)^2[2t(3/2)^s]^{h/25}\). Since \(\rho<0.925,\ 2t(3/2)^s<4.13\), and \(0.925^{25}\,4.13<1\), the amended majorant is summable. For each fixed tuple of words the contribution tends to zero with \(y^{-s}\). This extension allows arbitrary bits on both ends and leaves unrestricted primitive histories open. It does not imply a frequency estimate along any ordinary path.

**Uniform rate.** In fact the entire flanked contribution just bounded is at most \(200{,}000{,}000\,y^{-1/200}\). For a particular core its raw term at \(y\), including its flanks, is bounded by
\[
 y^{-s}\,[t(3/2)^s]^{a+c+hj}.
\]
Interpolate this bound with the arithmetic flanked bound, putting weight \(\theta=1/350\) on the raw bound and \(1-\theta\) on the arithmetic bound. The prefactors \(3^s2^{sh}(3/2)^{sv}\) in the arithmetic bound are at least one, so can be restored in full. The common bound for the flanks is \([t(3/2)^s]^{a+c}\). In the core replace \(q\) by \(\widetilde q=q\,3^{s\theta}=q\,3^{1/200}\), and gain \(y^{-s\theta}=y^{-1/200}\). We have \(3^{1/200}<1.006,\ \widetilde q<0.303,\ (2^s+3^s)\widetilde q^2<0.937\). After applying the flank allowance the geometric rate is smaller than \(0.995\), since \(0.937^{25}\cdot4.13<0.995^{25}\). Finally \(3^s/(1-\widetilde q)<10\) and \(\sum_{h\ge1}(h+1)^2(0.995)^h<2/(1-0.995)^3\). These estimates give the stated conservative constant. If only unflanked nonstationary words are counted, the same bound applies even at a periodic ambient endpoint.

The companion descent.lean formalizes the literal chronological word relation, its realization on actual shortcut iterates, the affine word identity, its iterated signed determinant, the coprime divisibility transfer, the nonstationary lower bound and the one-copy stationary case. Lean 4.34.1 with the Std library and warnings as errors checked six public theorems. The carry upper bound, interpolation, shell estimates, and infinite-series bounds are written proofs. The companion descent.py checks the rational numerical comparisons, the finite-depth smoothing identities, and 756 literal powered histories with ordinary integer endpoints.

## Quantitative bound for distinct words with matching carries

Fix the same \(s=7/4,\ t=101/100\). At every nonperiodic ordinary endpoint \(y\) the sum of normalized contributions from **both of the following classes together**, allowing arbitrary flanks of combined length at most \(h/25\) as before, is at most \(10^{15}y^{-1/200}\). A history may be counted once for each description. All words below are chronological. Write \(Q=2^h,\ P=3^v\), where the nonempty reference word \(W\) has length \(h\), \(v\) odd bits, and carry \(C_W\).

1. The core is \(V W\), where \(V\) has length \(h\), has \(v\) odd bits and \(C_V\equiv C_W\bmod P\). The two words can differ.
2. For any \(k\ge3\), the core is an arbitrary word \(X\) of length \(kh\) and \(kv\) odd bits satisfying \(C_X\equiv C_{W^k}\bmod P^k\). The reference \(W\) need not appear anywhere in \(X\).

The powered word theorem is a special case. The second class allows cancellations across a whole history, with no individual congruence or count constraints on its internal chunks. Neither condition is forced on an arbitrary primitive history.

**Arithmetic.** Write \(z\) for the core endpoint and \(b\) for its physical origin. In class 1, \(C_{VW}=P C_V+Q C_W\) agrees with \(C_{WW}\) modulo \(P^2\). Thus both classes have \(P^k\mid Q^k z-C_{W^k}\). As \((Q-P)C_{W^k}=(Q^k-P^k)C_W\) and \(Q\) is coprime to \(P\), we obtain
\[
 P^k\mid (Q-P)z-C_W.
\]
If that deviation is zero, \(Qz=Pz+C_W\) forces the actual word from the positive integer \(z\) to be \(W\): the carry equation fixes its initial residue modulo \(Q\), and the parity cylinders at depth \(h\) partition those residues into singletons. Its endpoint after \(h\) steps is then \(z\). This makes \(z\) and every forward endpoint \(y\) periodic. For class 1 the physical last copy of \(W\) also gives this directly. The full pair may start off that cycle. For nonperiodic \(y\) we have \(P^k\le H_W z\), where \(H_W=Q+P+C_W\). The all-even reference has \(v=0\), \(P=1\), \(C_W=0\), and the statements still apply.

**Multiplicity of the residue class.** Among words of length \(H\) with \(U\) odd bits, the integer carry determines the word uniquely. Indeed \(2^H\) and \(3^U\) determine the initial parity cylinder from the carry. Every carry lies in \(0\le C<2^{H-U}3^U\), including the all-even case. Hence any given residue modulo \(3^U\) is attained by at most \(2^{H-U}\) words. For each fixed \(W\) this bounds the number of cores by \(\ell^{h-v}\), with \(\ell=2\) in class 1 and \(\ell=2^k\) in class 2. This counts all allowed words, including overlapping descriptions.

**Weighted carry estimate.** Give each reference word weight \(\ell^{h-v}\) and let \(\|\cdot\|_s\) denote the resulting unnormalized finite \(L^s\) norm at that length. Put \(M_\ell=\max((\ell+1)2^s,\ell+3^s)\). The binomial formula gives \(\|Q\|_s,\|P\|_s\le M_\ell^{h/s}\). Appending a bit gives \(C_{W0}=C_W,\ C_{W1}=3C_W+2^h\). Minkowski's inequality therefore gives
\[
 \|C\|_{s,h+1}\le(\ell+3^s)^{1/s}\|C\|_{s,h}
                       +2^h(\ell+1)^{h/s}.
\]
Induction yields \(\|C\|_{s,h}\le h M_\ell^{h/s}\), and hence
\(\sum_{|W|=h}\ell^{h-v} H_W^s\le(h+2)^s M_\ell^h\).

**Summation.** At the core endpoint, the contribution of each actual matched word is bounded by \(H_W^s q^{hk}\) using the divisibility just proved. Interpolate with its raw bound at \(y\), exactly as in the uniform-rate argument, retaining \(H_W^s\ge1\) in full and charging the same flank factor. The resulting base per \(h\), before flanks, is \(M_\ell\widetilde q^k\), where \(\widetilde q<0.303\). For class 1 it is smaller than \(0.937\), using \(M_2<10.11\). For class 2 at \(k=3\), \(M_8<30.33\), so the base is smaller than \(0.85\); each increment in \(k\) multiplies it by at most \(2\widetilde q<0.606\), since \(M_{2\ell}\le 2M_\ell\). The flanks contribute the same polynomial \((h+1)^2\) and factor \(4.13^{h/25}\) as above. Both classes together are therefore bounded by
\[
 y^{-1/200}\left(1+\frac1{1-0.606}\right)
 \sum_{h\ge1}(h+1)^2(h+2)^s\,0.995^h.
\]
Using \((h+2)^s(h+1)^2\le16(h+1)^4\le384{h+4\choose4}\) gives the stated conservative constant \(10^{15}\).

The new Lean theorems **pair_identity** and **matching_pair_divides** verify the paired arithmetic for actual distinct chronological histories, in addition to the six theorems above. The weighted norm proof, the \(k\ge3\) counting argument, and the infinite sum are written mathematics. The controls verify strict rational constants and test matched nonidentical pairs and primitive words that omit the reference. The essential unresolved contribution is from ordinary histories outside these congruence classes. In particular a fixed escaping source could contribute at its growing endpoints through just such unmatched histories; the estimate establishes no universal descent.
