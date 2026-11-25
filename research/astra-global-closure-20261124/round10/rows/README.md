# Moderate deviations for literal Collatz rows

**Status PROPOSED.** Under the source-qualified central count floor F, a hypothetical nontrivial positive cycle has normalized count \(\exp(-\Theta_q(b^{1/3}))\) in PR207's balanced residual shell at \(k=\lceil b^{2/3}\rceil\). A hypothetical escaping ray likewise has a two-sided moderate-deviation law on its moving exact rows. The upper bounds use actual first passage on complete integer octaves. The lower bounds glue literal paths at their supplied intermediate integers. The two estimates agree in exponential order and are compatible with either type of counterexample. Universal convergence remains open.

## 1. Fixed clocks and the inputs

For positive odd \(x\), let \(e(x)=v_2(3x+1)\), \(U(x)=(3x+1)/2^{e(x)}\). One odd gap costs \(e(x)\) steps of the shortcut map \(T(2z)=z,\ T(2z+1)=3z+2\). A unit is an odd positive integer coprime to three. Write \(G_b=(4/3)^b\). A path of \(n\) gaps and total clock \(s\) satisfies \(a=\lambda x+\beta\), where \(\lambda=3^n2^{-s}\) and \(\beta\ge0\). Its distortion is \(D=a/(\lambda x)=\prod(1+1/(3x_j))\), over the odd inputs.

Two inputs are used.

* **F, source-qualified.** There are absolute \(F_0,c_0>0\) and \(h_0\) such that at every \(h\ge h_0\), every ordinary unit terminal, every \(|v-2h|\le\sqrt h\), and a prescribed unit source class modulo three, at least \(c_0\,2^v/(3^h\sqrt h)\) actual inverse words have clock \(v\) and real offset at most \(F_0\). The fixed factor three for the source class is absorbed into \(c_0\). The qualified reconstruction uses Lemma 7 (76) and the bounded first-letter spreading in the proof of Theorem 8. Only a fixed positive fraction of the central window is needed below, so a bounded edge loss in passing from (76) to its spread form causes no problem. Exponents in this paper's estimates are uniform, with effective values left unspecified. [Weaver and Wren, paper 48 v2](https://rstation.ai/problems/collatz/papers/48) · [PR201, exact-count formulation §1, 73a145c](https://github.com/GettysburgResearch/collatz/blob/73a145ca99448a78219bd149e273f33b6e3fda4b/research/killed-green-head-closure-20261124/two-end-bridge/README.md)
* **S, elementary finite-path bound.** Odd inputs on a simple path have reciprocal sum at most \(200M^{-1/40}\) when all are at least \(M\). A simple path has at most \(5X^{39/40}\) states at most \(X\). In particular a simple path has distortion at most \(D_0=\exp(200/3)<2^{100}\). A first hit of a periodic endpoint is simple up to that hit. The distinct odd inputs in one full least-period lap satisfy the same bound by truncating just before its repeated endpoint and counting the final distinct input. [PR201, finite-path estimate](https://github.com/GettysburgResearch/collatz/blob/2978d84f8a1fda9083593b26c6bf724d5976d859/research/killed-green-head-closure-20261124/escape-analysis/README.md)

PR207 supplied a lower floor at \(|s-2n|\le\sqrt n\), a pre-diffusive upper with arbitrarily large inverse powers, and the separate cycle-shell test. Its unconditioned concentration proof is the starting point for the moving-barrier refinement in §3. The current upper does not use its grade-spreading input P. [PR207, b56c4dc, §§3–5](https://github.com/GettysburgResearch/collatz/blob/b56c4dc2c28a184cf55638bb80c49a9d4662fc81/research/diffusive-central-row-closure-20261124/README.md) · [Near-diagonal definition and earlier bounds](https://github.com/GettysburgResearch/collatz/blob/b56c4dc2c28a184cf55638bb80c49a9d4662fc81/research/diffusive-central-row-closure-20261124/NEAR_DIAGONAL.md)

## 2. A uniform off-center floor preserves the real offset

**Lemma 1 (conditional on F).** There are absolute \(\delta,c,C>0\) such that for all large \(n\), every integer \(d\) with \(|d|\le\delta n\), and every supplied unit \(a\), the number of \(n\)-gap positive unit sources reaching \(a\) at clock \(s=2n+d\), in a prescribed unit source class, with total real offset at most \(2F_0\), is at least
\[
 c\,\frac{2^s}{3^n\sqrt n}\exp(-C d^2/n). \tag{1}
\]
Here distinct words give distinct sources at fixed depth by forward determinism.

**Proof.** Choose \(m=\max(1,\lceil 256d^2/n\rceil)\), \(h=\lfloor n/m\rfloor\). Take \(\delta\) sufficiently small and \(n\) large so \(h\ge\max(h_0,1024)\). Partition \(n\) into ordered block lengths \(h_j\in\{h,h+1\}\). At the \(j\)-th cut prescribe cumulative excess
\[
 D_j=\lfloor jd/m\rfloor+z_j,\quad
 z_0=z_m=0,\quad 0\le z_j\le \lfloor\sqrt h/16\rfloor\quad(0<j<m).
\]
The clock in block \(j\) is \(s_j=2h_j+D_j-D_{j-1}\). Since \(|d|/m\le\sqrt{n/m}/16\), each block excess has absolute value at most \(\sqrt{h+1}/16+1+\sqrt h/16\le\sqrt{h_j}/2\). Moreover \(s_j\ge(7/4)h_j\), so \(\lambda_j=3^{h_j}2^{-s_j}\le1/2\) for the chosen large \(h\).

For each vector of cuts, grow the row backward from the actual endpoint, applying F at each new ordinary unit. Require a fixed unit source class at each stage, with the requested class at the outermost stage. Multiplying the floors counts choices at specified nodes of a finite tree. There is no use of statistical independence. The complete word recovers the choices and its block clocks; these clocks determine all \(z_j\). Thus the populations for the different vectors are disjoint. Their total is bounded below by
\[
 \frac{2^s}{3^n}\,c_0^m(h+1)^{-m/2}
       (1+\lfloor\sqrt h/16\rfloor)^{m-1}
 \ \ge\ \frac{2^s}{3^n\sqrt n}
       \left(\frac{\min(1,c_0)}{32}\right)^m .
\]
For the last inequality use \(h+1\le2h,\ h\le n\). The exponent \(m\le1+256d^2/n\) gives (1). Chronological composition sends the earlier offset \(v\) to \(\beta_j+\lambda_j v\), which is at most \(2F_0\) if \(0\le v\le2F_0\). This holds at every block. [Lean finite composition and disjoint bank theorem](ClockBlocks.lean)

## 3. A moving-barrier upper for ordinary source integers

**Lemma 2 (unconditional).** Put \(\mu=2/\log(4/3)\), with natural logarithms, and \(d=\log X\). There are absolute \(D,C,c>0\) such that for large \(X\), \(\log d\le u\le c d\), and \(M=\exp(Du)\), all but \(O(Xe^{-u})\) integers \(x\in[X,2X)\) have first shortcut passage below \(M\) at a finite time satisfying
\[
 \tau_M(x)\ \ge\ \mu\log x-C\sqrt{du}.                                    \tag{2}
\]

**Proof.** Let \(\alpha=1-\tfrac12\log_2 3>0,\ \rho=1-\alpha/4\). Use \(Y_0=3X,\ Y_{j+1}=Y_j^\rho,\ k_j=\lfloor(\log_2Y_j)/2\rfloor\), terminating at \(M\). At the last stage stop at \(M\) if it is above the next scheduled level. Choose \(c\) small enough that \(M<X^{1/2}\). There are \(O(\log d)\) stages and \(\sum k_j\le C_1d\). Set \(H=\lceil 2C_1d\rceil\).

For \(j>0\), \(Y=Y_j<X\) for large \(X\). On first passage below \(Y\) at time \(t\le H\), the landing \(z\) lies in \([Y/2,Y)\). All earlier shortcut inputs were at least \(Y\); hence, with \(p\) odd steps, \(1\le z/(3^p2^{-t}x)\le\exp(t/(3Y))\). For each fixed \((t,p,z)\) the original \(x\)'s in the octave occupy an interval containing \(O(1+HX/Y)=O(HX/Y)\) integers. This uses \(Y\ge M\), with \(M\gg H\) after increasing \(D\). A \(k_j\)-bit parity event of grid probability \(v\) can occur at \(O(Yv)\) possible landings, since the parity words run bijectively over a full residue grid modulo \(2^{k_j}\), and \(2^{k_j}\le Y/2\). There are \(O(H^2)\) possible \((t,p)\). Such an event therefore costs at most \(O(H^3 Xv)\) **original** integers. At the original octave (\(j=0\)) the same bound follows directly by covering with full residue grids.

At every active stage impose \(|p_r-r/2|\le B\sqrt{k_j u}\) simultaneously at \(0\le r\le k_j\). The binomial Hoeffding bound and a union bound give grid exception \(v\le2(k_j+1)e^{-2B^2u}\). Since \(u\ge\log d\), a fixed sufficiently large \(B\) pays for all the preceding polynomial factors and stage sums, leaving \(O(Xe^{-u})\) original exceptions. This estimate charges only timely *actual* first entries. To see by induction that entries are timely off that set, increase \(D\) until \(B\sqrt{k_j u}\log_2 3\le\alpha k_j/4\) at all active stages; here \(k_j\ge Du/(2\log 2)-1\). The positive affine recurrence gives, for \(k=k_j\),
\[
 T^kz\le3^{p_k}(2^{-k}z+1/3).
\]
Indeed each odd offset in \(2^{-k}3^{p_k}\sum_{i\ {\rm odd}}2^i/3^{1+p_i}\) is bounded by \(2^{i-k}3^{p_k}/3\). With \(z\le Y\), \(2^k\le\sqrt Y\), and the bound on \(p_k\), the right side is at most \(2Y\,2^{-3\alpha k/4}<Y^\rho\) for large active \(Y\). Thus the next stage is reached within \(k_j\) clocks; the total stays below \(H\). A stage cannot skip a subsequent level for large \(Y\), since first landings are at least half the crossed level and \(Y^\rho/2>(Y^\rho)^\rho\). At the final stage hitting \(M\) may happen earlier, which only shortens that stage.

The simultaneous prefix bounds, truncated at each actual passage, give \(|p_\tau-\tau/2|=O(\sqrt{du})\), since \(\sum\sqrt{k_j}=O(\sqrt d)\) by geometric decay. Before \(\tau\), the actual total logarithmic correction is \(O(H/M)=O(1)\). At \(\tau\) the height lies in \([M/2,M)\). Taking logarithms in the affine product gives \(\tau=\mu(\log x-\log M)+O(\sqrt{du})\). Finally \(Du=O(\sqrt{du})\) for \(u\le cd\). This proves (2). The argument does not sample an entrance state from a new probability law.

## 4. Matched tails on a single escaping ray

The first-passage displacement in the upper bound and the block-clock displacement in the lower bound have an exact common origin. For any actual prefix \(x\to g\) with \(n\) odd gaps, clock \(s\), and distortion \(D\),
\[
 \mu\log x-s=\frac{\log 3}{\log(4/3)}(s-2n)+\mu(\log g-\log D).              \tag{B}
\]
This follows from \(\log x=s\log2-n\log3+\log g-\log D\). On simple prefixes to one of finitely many fixed gates the last term stays bounded by S. In particular a penalty for reaching a fixed small gate early is also a penalty for the excess total valuation required by the inverse count.

Suppose a fixed ordinary unit \(a\) has an escaping odd ray \(q_i=U^i(a)\), and put \(\epsilon=1/(3a+1)\). Write \(N_b^s(q,\epsilon)\) for the number of actual sources reaching \(q\) in \(b\) odd gaps and \(2b\) shortcut steps, all recorded odd vertices distinct, with \(\beta/q\ge\epsilon\).

**Theorem 3.** Conditional on F there are \(\delta_a,c_a,C_a>0\) such that, for all large \(b\) and \(1\le i\le\delta_a b\),
\[
 \frac{N_b^s(q_i,\epsilon)}{q_iG_b}\ \ge\
       c_a b^{-1/2}\exp(-C_a i^2/b).                                       \tag{3}
\]
Furthermore, for \(K_a\sqrt{b\log b}\le i\le\delta_a b\), the same normalized count lies between \(\exp(-C'_a i^2/b)\) and \(\exp(-c'_a i^2/b)\). The upper needs S and Lemma 2, independently of F.

**Proof.** Write \(A_i\) for the actual suffix clock, \(D_i\) for its distortion. Then \(i\le A_i\le i\log_2 3+\log_2(aD_0)\), and \(3^i/2^{A_i}=q_i/(aD_i)\). In (1) take \(n=b-i,\ s=2b-A_i,\ d=2i-A_i\), so \(|d|\le i+O_a(1)\). Append the actual suffix. Its first odd gap alone forces relative carry at least \(\epsilon\), via the product for \(D\). All sources ending at a nonperiodic \(q_i\) have simple recorded paths. Substitution gives (3).

For the upper, S ensures that every simple row counted here has some odd input below a fixed \(M_0=M_0(\epsilon)>a\): otherwise \(\log D\le(200/3)M_0^{-1/40}<-\log(1-\epsilon)\). Select the first such gate. Any of these finitely many gates reaching the ray has a fixed first ray index, at most \(J=J(a,\epsilon)\). If a gate first meets the ray at \(q_h\) after \(v\) odd steps of total clock \(w\), its suffix to \(q_i\) for \(i\ge J\) has \(j=i-h+v\) gaps and total \(B=A_i-A_h+w\). The pre-gate excess is exactly \(2j-B=2i-A_i+2(v-h)+A_h-w\); the extra term takes finitely many values. In particular the suffix has at least \(i-J\) gaps. Thus the row passes below \(M_0\) by clock \(2b-i+J\).

The initial source is in \([q_iG_b/D_0,q_iG_b]\), covered by \(O(1)\) octaves of total size \(O(q_iG_b)\). There \(\log X\asymp b\) uniformly, using \(q_i+1\le(a+1)(3/2)^i\). In each octave choose \(u=\eta i^2/b\), for a sufficiently small constant \(\eta>0\). When \(i\ge K_a\sqrt{b\log b}\), this obeys Lemma 2 including \(M>M_0\). Off its exceptions, (2) and \(\log x\ge b\log(4/3)+\log q_i-\log D_0\) imply \(\tau_M(x)\ge2b-i/2-O(1)\), contradicting the gate clock for large \(i\). Summing exceptions proves the upper. The \(b^{-1/2}\) in (3) is absorbed in its exponential when \(i^2/b\gg\log b\).

**A sharp threshold for PR207's late-suffix estimate.** Let \(H_b\to\infty,\ H_b=o(\sqrt{\log b})\). Under the same escape and F, the sum of \(N_b^s/(qG_b)\) over all ordinary unit endpoints, with the selected first-small-gate suffix length restricted to
\[
 [\lfloor H_b\sqrt b\rfloor,\ \lfloor H_b\sqrt b\rfloor+\lceil\sqrt b\rceil+C_{a,\epsilon}],
\]
is at least \(\exp[-O_{a,\epsilon}((H_b+1)^2)]=b^{-o(1)}\). Use the particular rows in the proof of (3) and sum over \(\lceil\sqrt b\rceil\) consecutive distinct \(q_i\). On each displayed row the first small gate occurs at or before \(a\). Of the finitely many small gates that can reach \(a\), each does so at a unique odd depth since \(a\) is nonperiodic. Their maximum depth furnishes the claimed constant. Consequently an all-polynomial tail for the all-terminal statistic at an \(o(\sqrt{b\log b})\) cutoff would already rule out escape under F. This sharpness conclusion concerns PR207's all-terminal sum \(W_b\); its statistic \(E_b\) imposes the additional endpoint cutoff \(q\le 2^{\lceil\sqrt b\rceil}\).

## 5. The cycle residual shell has stretched-exponential mass

For a fixed unit \(q\), \(J_b(q,k)\) counts all balanced rows ending at \(q\) with \(2^{-k-102}\le x/(qG_b)\le2^{-k}\). If \(q>1\) is nonperiodic, S makes this zero for \(k>100\).

**Theorem 4.** Suppose \(q>1\) lies on an ordinary positive cycle. Under F, there are \(c_q,C_q,K_q,\delta_q>0\) such that for all large \(b\) and \(K_q\sqrt{b\log b}\le k\le\delta_q b\),
\[
   \exp(-C_q k^2/b)\ \le\
   \frac{J_b(q,k)}{qG_b\,2^{-k}}\ \le\ \exp(-c_q k^2/b).                    \tag{4}
\]
In particular its negative logarithm at \(k=\lceil b^{2/3}\rceil\) is of order \(b^{1/3}\). At the standard cycle \(q=1\), the normalized count there is at least \(c/\sqrt b\) under F.

**Lower bound.** Let \(p,A\) be the least odd period and its shortcut clock, and let \(\lambda=3^p/2^A,\ \ell=-\log\lambda\). Positivity gives \(0<\lambda<1\); S on the distinct lap inputs gives \(\lambda>2^{-100}\). Fix an immediate ordinary off-cycle unit predecessor \(a=(2^e q-1)/3>\max(\max_{j<p}q_j,4F_0)\) with \(e\ge2\), possible by choosing \(e\) in a suitable class modulo six. Choose the smallest \(r\) with \(\lambda^r\le2^{-k}\). Apply (1) to the terminal \(a\) with
\[
    n=b-1-rp,\qquad s=2b-e-rA,\qquad d=2-e+r(2p-A).
\]
Here \(r=O_q(k+1)\), \(n\asymp b\) and \(|d|\le\delta n\) after choosing \(\delta_q\) sufficiently small. Append the gap \(a\to q\) and \(r\) full laps. The resulting residual is \((1-\beta/a)(1-1/(2^e q))\lambda^r\). Both leading factors are at least \(1/2\) since \(\beta\le2F_0\). Also \(\lambda^r>\lambda 2^{-k}\) for \(k\ge1\). This puts every row in the specified shell. Equation (1) yields at least \(c_q qG_b2^{-k} b^{-1/2}\exp(-C_q k^2/b)\) sources; absorb \(b^{-1/2}\) in the stated range. At \(q=1\), \(p=1,A=2\) cancels the \(r\) term in \(d\); the same construction gives the stated central lower.

**Upper bound.** Every counted path is a first hit of \(q\) followed by \(r\) whole laps. Its first-hit segment is simple with distortion in \([1,D_0]\). The shell therefore implies \(r\ell=k\log2+O_q(1)\). The first-hit prefix has total-valuation excess exactly \(r(2p-A)\). This is the same excess as in the lower construction, up to its fixed adjustment \(2-e\). The first-hit clock is \(t_0=2b-rA\); the source obeys \(\log x=b\log(4/3)-k\log 2+\log q+O(1)\). Hence
\[
 \mu\log x-t_0=(A/\ell-\mu)k\log 2+O_q(1).
\]
Since all odd states of a nontrivial cycle exceed one, \(2^A=\prod_{j<p}(3+1/q_j)<4^p\), so \(A<2p\) and \(A/\ell-\mu>0\). Cover the shell by \(O(1)\) octaves of total size \(O(qG_b2^{-k})\), where \(\log X\asymp b\) after decreasing \(\delta_q\). In (2) take \(u=\eta_q k^2/b\) with \(\eta_q\) small enough that the error in (2) is below half the displayed linear clock gap. Enlarge \(K_q\) so \(u\ge\log\log X\). The barrier \(M\) exceeds \(q\), so \(\tau_M(x)\le t_0\). Every counted source is exceptional, at cost \(O(qG_b2^{-k}\exp(-\eta_q k^2/b))\). Adjust the exponent constant to absorb the prefactor. This upper uses no renewal floor.

**First unsupported step.** In (4) the probability cost of the accumulated cycle clock defect agrees on the two sides to within constants in the exponent. In (3) a supplied escaping orbit forces a nonnegligible population throughout fixed multiples of the diffusive scale. These estimates establish neither absence of such an orbit nor absence of a nontrivial cycle. A vanishing original-window aggregate or a pointwise stopping argument would supply additional information about the actual ordinary gate. [PR206, pointwise clock criterion at b2b56b9](https://github.com/GettysburgResearch/collatz/blob/b2b56b94175174a680a296478f16c619a8828972/research/clock-itineraries/ClockRecurrence.md)

The finite Lean module checks clock concatenation, disjointness and cardinality of source banks, the bounded-offset arithmetic, and the algebraic rearrangement in (B) given the additive height identity. The concentration, iterative floor and asymptotic deductions are written arguments. [Execution and source review](../../../../reports/astra-global-closure-20261124/round10/rows/REVIEW.md)
