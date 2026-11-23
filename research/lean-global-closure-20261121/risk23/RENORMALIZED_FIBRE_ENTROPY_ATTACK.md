# Exact radial renormalization and the attempted solenoid entropy closure

Date: 2026-11-23.

**Status.** The total-variation theorem below was derived independently in this pass from the repository's source-qualified canonical inverse laws. The subsequent argument pursues a full escape exclusion through the compact solenoid and calculates why that entropy transfer does not close. No escape exclusion or complete Collatz proof is claimed. The probability arguments have not been Lean formalized.

**Concurrent source update.** PR180 advanced during this work to
`04572b94c8a58f964ba9b2b1b1bccfe7e9b12ae2`. Its common component boundary
and full-path conditioning theorem cover the TV conclusion in a stronger
shared path-space formulation. Our exactly normalized variable is its
`Z/p`. No unique priority claim is made for that convergence. The exact
[late-source crosswalk](LATE_FRONTIER_SYNTHESIS.md#1-pr180-concurrently-supplies-the-common-path-space-behind-our-tv-limit)
credits the overlap and preserves the distinct solenoid integer-part
entropy calculation below.

The attempted step was to retain an actual escaping source, compactify its real/ternary inverse boundary, and obtain the entropy missing from its ordinary time law. Keeping an exact radial normalization improves the available moving-fibre convergence from bounded-Lipschitz distance to total variation, including rapidly oscillating tests. Even granting enough Fourier regularity to obtain Haar measure on the solenoid, the resulting entropy can be carried entirely by the real integer-part variable. The ordinary source remains a separate factor.

## 1. Inputs, source and normalization

Fix one hypothetical escaping positive odd unit orbit

\[
q_j=U^j(p),\qquad 2^{g_j}q_j=3q_{j-1}+1\quad(j\ge1).
\]

Use the actual trace function \(F=h\) and its inverse kernel

\[
K_F(q,x)=3\,2^{-e}\frac{F(x)}{F(q)},\qquad Ux=q.
\tag{1}
\]

The state space and killing convention are exactly those of own PR175 at `8a8b1eea6c9fdfbce7b0bbf0af4eb771791e3a73`, `research/lean-global-closure-20261121/machinery/MOVING_CESARO_FIBRES.md`. Its construction supplies positive finite harmonic values and \(u(q):=F(q)/q\le M_0\). All of that construction's analytic dependencies remain source-qualified. In particular the ordinary trace is pinned there to Valbuena commit `a7275d5a73814d3d9a400c6fe6577de9542b03a3`; no fresh analytic verification is claimed here.

Let

\[
\lambda(x)=\frac{3x}{3x+1},\qquad
\Lambda_j=\prod_{i=0}^{j-1}\lambda(q_i)\ge\delta>0,
\qquad \Lambda_0=1.
\tag{2}
\]

The product bound is the existing nonperiodic-orbit input. Set

\[
D_j=\prod_{i=1}^jK_F(q_i,q_{i-1})
=\Lambda_j\frac{u(p)}{u(q_j)},\qquad D_0=1.
\tag{3}
\]

The \(D_j\) decrease and are at least \(\delta u(p)/M_0\), so \(D_j\downarrow D_\infty>0\). These are the prefix probabilities of PR178 at `7e4569476e152f6b8537bdc1711df595ec1ffd89`, `research/whole-repo-synthesis-20261122/entropy/CANONICAL_TIME_ENTROPY_ATTEMPT.md`. Its Section 6 proves a common normalized real-fibre limit in bounded-Lipschitz distance.

At a root \(q\), let \(B_\infty\) be the real boundary value under the actual \(F\)-path law. Its existence and the bound \(0\le B_\infty\le(1-\delta)q\) at nonperiodic roots are existing inputs, after reducing the common positive \(\delta\) if necessary.

## 2. Total variation after exact radial renormalization

Define

\[
\nu_j=\operatorname{Law}_{q_j}^{F}
\left(\frac{q_j-B_\infty}{q_j\Lambda_j}\right).
\tag{4}
\]

All these probabilities are supported in \([\delta,\delta^{-1}]\). The denominator keeps the original source clock exactly.

**Theorem 1.** There is a probability \(\nu_\infty\) such that

\[
\boxed{\nu_\infty\ge\frac{D_\infty}{D_j}\nu_j,
\qquad
\|\nu_j-\nu_\infty\|_{\rm TV}
\le1-\frac{D_\infty}{D_j}\longrightarrow0.}
\tag{5}
\]

Here TV is the supremum over measurable sets, or half the total variation norm of the difference of two probabilities.

**Proof.** For \(j\ge i\), the actual inverse prefix from \(q_j\) to \(q_i\) has probability \(D_j/D_i\). Write its affine map as

\[
q_j=A_{i,j}q_i+C_{i,j}.
\]

On the prefix event the boundary variable is \(B_\infty=C_{i,j}+A_{i,j}B'_\infty\), and the conditional suffix has the actual \(F\)-law at \(q_i\). Multiplication of (2) gives

\[
\frac{A_{i,j}q_i}{q_j}=\frac{\Lambda_j}{\Lambda_i}.
\]

Thus the random variable in (4), on this event, is *exactly* \((q_i-B'_\infty)/(q_i\Lambda_i)\). Therefore

\[
\nu_j\ge\frac{D_j}{D_i}\nu_i.
\tag{6}
\]

The finite measures \(M_j:=\nu_j/D_j\) increase in measure order and have masses \(1/D_j\uparrow1/D_\infty<\infty\). Their increasing limit can be constructed as

\[
M_\infty=M_0+\sum_{j\ge0}(M_{j+1}-M_j).
\]

Set \(\nu_\infty=D_\infty M_\infty\). This is a probability with the domination in (5). Its decomposition into the component \((D_\infty/D_j)\nu_j\) and the remaining positive measure proves the TV bound. \(\square\)

The original source and finite immigration are explicit:

\[
\nu_\infty=D_\infty\nu_0+
D_\infty\sum_{j\ge0}
\left(\frac{\nu_{j+1}}{D_{j+1}}-\frac{\nu_j}{D_j}\right).
\tag{7}
\]

Every summand is positive. In particular the original-source submeasure \(D_\infty\nu_0\) survives. This is compatible with, and does not bypass, own `machinery/TILTED_RENEWAL_FINITE_IMMIGRATION.md` at the same head.

For any sequence of complex measurable tests with \(|f_j|\le1\),

\[
\left|\int f_j\,d\nu_j-\int f_j\,d\nu_\infty\right|
\le2\left(1-\frac{D_\infty}{D_j}\right)\to0.
\tag{8}
\]

Unlike a bounded-Lipschitz comparison, this permits arbitrarily fast oscillation of the test. The normalization must remain exact. Replacing \(\Lambda_j\) by \(\Lambda_\infty\) inside an oscillatory test has not been justified.

With \(S_j=\sum_{i=1}^jg_i\), the retained scale is

\[
s_j:=q_j\Lambda_j=p\frac{3^j}{2^{S_j}}\ge\delta q_j\to\infty.
\tag{9}
\]

For \(\widehat\nu(t)=\int e^{2\pi ity}\,d\nu(y)\), (8) yields

\[
\left|\mathbb E_{q_j}^F e^{2\pi it_j(q_j-B_\infty)}
-\widehat\nu_\infty(t_js_j)\right|
\le2\left(1-\frac{D_\infty}{D_j}\right)
\tag{10}
\]

for every sequence of real frequencies \(t_j\).

## 3. The prospective compact-solenoid regularization

The relevant primary source is Lyapunov Weaver, *Geometry, integer fibres, and dyadic equidistribution of the joint Collatz affine law*, v2, Section 10.6:

<https://rstation.ai/problems/collatz/papers/19>.

Its compact group is

\[
\mathcal S=(\mathbb R\times\mathbb Q_3)/
\operatorname{diag}\mathbb Z[1/3].
\]

For the projection \(\mu\) of the **global stationary joint affine law**, it proves \((\mathsf D_2)_*\mu=(\mu+(\mathsf D_3)_*\mu)/2\) and finite-partition entropy convergence of \((\mathsf D_{2^n})_*\mu\) to Haar. That theorem retains its published dependencies. It does not itself give conditional regularity of the specified ordinary fibres.

The new exact reduction tests a stronger possible transfer. Let

\[
\kappa_j=\operatorname{Law}_{q_j}^F\bigl(\pi(B_\infty,q_j)\bigr).
\]

Subtracting the diagonal integer \((q_j,q_j)\) gives \(\pi(B_\infty,q_j)=\pi(B_\infty-q_j,0)\). Characters of \(\mathcal S\) are indexed by \(r\in\mathbb Z[1/3]\); choose their restriction to \(\pi(t,0)\) to be \(e^{2\pi irt}\). Equation (10) gives

\[
\widehat\kappa_j(r)=\widehat\nu_\infty(-rs_j)+o(1),
\tag{11}
\]

with error at most the right side of (10). Since characters determine probability measures on this compact abelian group,

\[
\boxed{\kappa_j\Rightarrow m_{\mathcal S}
\quad\Longleftrightarrow\quad
\widehat\nu_\infty(rs_j)\to0
\text{ for every }r\in\mathbb Z[1/3]\setminus\{0\}.}
\tag{12}
\]

A sufficient, currently unproved condition is that \(\nu_\infty\) is Rajchman: its Fourier transform tends to zero as real frequency tends to infinity. Only the frequencies in (12) are actually needed. No such Fourier decay follows here from atomlessness, weak convergence, or the global quotient theorem.

The retained initial fibre makes this regularity requirement substantive. Rajchman measures form a band on the present compact support: if \(\beta\ll\alpha\), both are finite and \(\alpha\) is Rajchman, approximate \(d\beta/d\alpha\) in \(L^1(\alpha)\) by finite linear combinations of real exponential characters. Their Fourier transforms are finite sums of translates of \(\widehat\alpha\), and the approximation error is uniform in frequency. Hence \(\beta\) is Rajchman. By (5), Rajchman regularity of \(\nu_\infty\) therefore forces it for every \(\nu_j\), including the original \(\nu_0\). Conversely, if a cofinal sequence of the \(\nu_j\) is Rajchman, their TV convergence implies that \(\nu_\infty\) is Rajchman. Thus the sufficient regularity assumption cannot be obtained merely by smoothing away the retained original source.

This was the proposed new regularization step. We next grant it to test whether it is strong enough to exclude escape.

## 4. The source-retaining limit is a product

Assume (12), and retain the ordinary ternary source label:

\[
\rho_N=\frac1{N+1}\sum_{j=0}^N\kappa_j\otimes\delta_{q_j},
\qquad
\pi_N=\frac1{N+1}\sum_{j=0}^N\delta_{q_j}.
\tag{13}
\]

**Theorem 2.** Along any subsequence with \(\pi_N\Rightarrow\mu_{\rm time}\),

\[
\boxed{\rho_N\Rightarrow m_{\mathcal S}\otimes\mu_{\rm time}.}
\tag{14}
\]

**Proof.** Test (13) with \(\chi_r(s)f(z)\), where \(f\) is continuous on \(\mathbb Z_3\). The integral is

\[
\frac1{N+1}\sum_{j=0}^N f(q_j)\widehat\kappa_j(r).
\]

For \(r\ne0\) it tends to zero because the Fourier coefficients tend to zero and \(f\) is bounded. For \(r=0\) it tends to \(\int f\,d\mu_{\rm time}\). Finite sums of these separated tests are dense in the continuous functions on the product, proving (14). \(\square\)

The source distribution remains the original time law in a separate factor. Its previously established ternary entropy ceiling can coexist with the strongest conditional equidistribution contemplated in (12).

## 5. Exact finite entropy accounting

Choose \(J\) uniformly from \(0,\ldots,N\), and then sample the actual real fibre at \(q_J\). At precision \(m\), define variables in \(\mathbb Z/3^m\mathbb Z\):

\[
Q=q_J\bmod3^m,\qquad
L=\lfloor B_\infty\rfloor\bmod3^m,\qquad
V=q_J-\lfloor B_\infty\rfloor\bmod3^m.
\tag{15}
\]

The fundamental-domain representative of the solenoid point is

\[
\bigl(\{B_\infty\},q_J-\lfloor B_\infty\rfloor\bigr).
\]

Thus its ternary coordinate is \(V\), not the ordinary root \(Q\). Since \(Q=V+L\),

\[
H(Q)\ge H(V)-H(L\mid Q).
\tag{16}
\]

To contradict the actual ceiling \(H(Q)\lesssim\theta m\log3\), where \(\theta=0.949955527188\ldots\), through nearly maximal entropy of \(V\), one would need for example

\[
H(L\mid Q)\le(1-\theta-\varepsilon)m\log3.
\tag{17}
\]

This is the first unsupported estimate in this proposed closure. In fact the conditional mixing being proposed gives the opposite behavior.

At each fixed \(J=j\), subtraction from \(q_j\) is a permutation. Also \(Q\) is determined by \(J\). Hence

\[
H(L\mid J)=H(V\mid J),\qquad H(L\mid Q)\ge H(L\mid J).
\tag{18}
\]

Let \(\varepsilon_{N,m}\) be the average TV distance of the conditional \(V\)-laws from the uniform law on \(3^m\) residues. Finite-alphabet entropy continuity, followed by concavity of binary entropy, gives

\[
\boxed{H(L\mid Q)\ge
(1-\varepsilon_{N,m})m\log3-h_b(\varepsilon_{N,m}).}
\tag{19}
\]

Thus source-retaining solenoid mixing makes the subtraction in (16) essentially as large as its positive term. For each fixed \(m\), (12) implies \(\varepsilon_{N,m}\to0\), since the relevant fundamental-domain cell boundaries have Haar measure zero. Therefore

\[
H(V)\to m\log3,\qquad H(L\mid Q)\to m\log3.
\tag{20}
\]

Equation (19) remains valid at every moving precision where a finite-partition comparison is available. The full quotient entropy can arise from the random real integer part; subtracting it restores the specified ordinary root. Even granting (12), estimate (17) conflicts with this entropy accounting.

This is not an opposite entropy bound for PR185's actual inverse endpoint laws. It is a calculation on the actual real fibre, with the ordinary source retained throughout.

## 6. Where the full escape attack stops

The valid PR178 criterion still says that a genuine stationary compact kernel
\(k(x,e)=3\,2^{-e}E(I_ex)/E(x)\), with finite positive \(E\), finite mean gap and two surviving branches, contradicts the actual mean gap bound. Theorem 1 does not supply that kernel identification. It does establish that rapidly varying real-boundary observables can be transferred after the exact scaling (9), without changing the source or deleting finite immigration.

The endpoint-entropy target in PR185 at `39ba48e6a8af781193e28c679ea8ab64663c3aa6`, `research/rigidity-closing-20261122/SAME_SOURCE_INVERSE_ENTROPY.md`, concerns an actual **ordinary inverse endpoint**. The variable \(V\) in (15) has not been proved to be such an endpoint, or even to belong to the root's forward component. Declaring \(q-\lfloor B_\infty\rfloor\) a smaller ordinary predecessor would be another unsupported arithmetic assertion.

The attempted closure therefore fails at a concrete point: compact-quotient regularity changes the observable, and retaining the integer source costs the full quotient entropy. A successful continuation needs a new arithmetic relation between that integer part and ordinary inverse endpoints, or a direct entropy/noncollapse estimate for those endpoints. It cannot follow by removing the source factor in (14).

## Sources and review scope

- Own PR175 at `8a8b1eea6c9fdfbce7b0bbf0af4eb771791e3a73`: read the complete moving-fibre and tilted-immigration notes named above; inherited analytic dependencies remain explicit.
- PR178 at `7e4569476e152f6b8537bdc1711df595ec1ffd89`: read the full `CANONICAL_TIME_ENTROPY_ATTEMPT.md`, including its compact criterion and normalized real-fibre limit.
- PR185 at `39ba48e6a8af781193e28c679ea8ab64663c3aa6`: read `MOVING_INVERSE_WINDOW.md` and `SAME_SOURCE_INVERSE_ENTROPY.md` in `research/rigidity-closing-20261122/`.
- Paper 19, v2, <https://rstation.ai/problems/collatz/papers/19>: inspected Sections 4, 9.2, 10.1, 10.6 and their stated scope. The primary source itself distinguishes global quotient convergence from ordinary integer trace control. The new written deductions here are (5), (10)--(14), and the explicit source-entropy calculation (18)--(19).
- Independent review: `/root/risk23_global_order` checked the exact segment normalization, measure domination, character scale, product-source limit, entropy inequalities (16), (18), (19), and the fixed-precision boundary argument. Root independently reviewed the same arguments. Neither review found a mathematical flaw. The Rajchman band observation was suggested by the independent reviewer and its proof is included above. These are written reviews, not claims of Lean verification.
