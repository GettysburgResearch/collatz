# A single-digit memory cost and the actual source-clock trace front

Date: 2026-11-23.

**Status: SOURCE-QUALIFIED written deductions; the proposed escape exclusion
remains OPEN.** This attack asks whether a Poisson-boundary or exactness argument
can force branching on the retained ordinary source. It obtains a quantitative
cost already visible in the first ternary predecessor digit, and a complete
profile of the normalized trace across the original-source clock. The scalar
tightness statement that would close the first argument is not established.
The bounded Poisson-corrector premise of the second argument is false on an
explicit family of finite ordinary paths. No infinite result below is claimed
to have been formalized in Lean.

## 1. Exact inputs and normalization

Use the accelerated odd map

\[
U(n)=\frac{3n+1}{2^{v_2(3n+1)}}.
\]

The critical transfer operator on positive odd integers is

\[
P f(q)=\sum_{\substack{e\ge1\\2^e q\equiv1\ (3)}}
3\,2^{-e}f\!\left(\frac{2^e q-1}{3}\right),
\qquad D_m=P^m\mathbf1.
\tag{1}
\]

Let \(F=h_{\rm tr}\) be the supplied positive ordinary trace on ternary
units, with \(PF=F\), \(F=0\) on multiples of three, and

\[
F(q)\ge\alpha>0\quad(3\nmid q),\qquad
F(q)\le M_0q.
\tag{2}
\]

The canonical inverse row and bounded trace observable are

\[
K(q,x)=\mathbf1_{Ux=q}\,
3\,2^{-v_2(3x+1)}\frac{F(x)}{F(q)},\qquad
g(q)=\frac{D_1(q)}{F(q)},\qquad 0\le g\le C_g:=2/\alpha.
\tag{3}
\]

Set \(g=0\) at multiples of three. The identity

\[
K^m g(q)=\frac{D_{m+1}(q)}{F(q)}
\tag{4}
\]

holds on the canonical state space. In particular, no ordinary and critical
inverse kernels are being interchanged.

The frozen sources are:

| Source | Exact scope used |
|---|---|
| PR178, `7e4569476e152f6b8537bdc1711df595ec1ffd89`, `research/whole-repo-synthesis-20261122/entropy/CANONICAL_TIME_ENTROPY_ATTEMPT.md` | Retained-source canonical path products, their positive limiting atom, and the exact all-horizon coupling. |
| PR175, `08fe1388ad63c758680b3695249aca319515c47d`, `research/lean-global-closure-20261121/machinery/MOVING_CESARO_FIBRES.md` | Ordinary trace (1)--(4), positivity/comparison inputs, and the moving mean trace theorem with its original source clock. |
| PR185, `39ba48e6a8af781193e28c679ea8ab64663c3aa6`, `research/rigidity-closing-20261122/MOVING_INVERSE_WINDOW.md` | Current ordinary-source clock obstruction; no onset bound is imported. |

The construction and positivity of the canonical reference retain those
sources' qualifications. Assume a hypothetical escaping ordinary orbit
\(q_j=U^j(p)\) in its retained component. Define

\[
a_j=K(q_{j+1},q_j),\qquad
d_0=1,\qquad d_j=\prod_{i<j}a_i.
\]

The source-qualified positive-atom conclusion is

\[
d_j\downarrow d_\infty>0,\qquad
\sum_{j\ge0}(1-a_j)<\infty,\qquad
F(q_j)/q_j\longrightarrow u_\infty>0.
\tag{5}
\]

Only the consequences of (5) are new here; its proof is not repeated.

## 2. The cost is visible in one ternary output digit

For an ordinary unit root \(q\), put

\[
b_r(q)=K\bigl(q,\{x:x\equiv r\pmod3\}\bigr),\qquad r=1,2,
\]

and define the single scalar observable

\[
\boxed{\Xi(q)=\log\frac{b_1(q)}{b_2(q)}.}
\tag{6}
\]

Both probabilities are strictly positive: the allowed exponents have a fixed
parity, and, as the exponent increases by two, the predecessor residues cycle
through \(0,1,2\pmod3\). Each of the two unit residues therefore occurs
infinitely often with a positive canonical weight.

Let \(r_j=b_{q_j\bmod3}(q_{j+1})\) be the probability of the actual
predecessor's ternary residue, and let \(\epsilon_j=1-r_j\). Since the
single actual predecessor has probability \(a_j\),

\[
0<\epsilon_j\le1-a_j,
\qquad E_J:=\sum_{j\ge J}\epsilon_j\longrightarrow0.
\tag{7}
\]

Consequently \(|\Xi(q_{j+1})|\to\infty\). There is also a quantified
lower bound which retains the source clock. Choose \(J\) so that
\(\eta_J:=\sup_{j\ge J}\epsilon_j<1/2\). For every \(N\ge1\),
Jensen's inequality gives

\[
\begin{aligned}
\sum_{j=J}^{J+N-1}|\Xi(q_{j+1})|
&=\sum_{j=J}^{J+N-1}\log\frac{1-\epsilon_j}{\epsilon_j}\\
&\ge N\log\frac{N(1-\eta_J)}{E_J}.
\end{aligned}
\tag{8}
\]

In particular,

\[
\boxed{\liminf_{N\to\infty}
\frac{1}{N\log N}\sum_{j<N}|\Xi(q_{j+1})|\ge1.}
\tag{9}
\]

The conclusion is stronger than merely a large average produced by rare
outliers. For \(T\ge0\),

\[
\#\{J\le j<J+N:|\Xi(q_{j+1})|\le T\}
\le(1+e^T)E_J.
\tag{10}
\]

Thus for every fixed \(0<\gamma<1\), the fraction with
\(|\Xi|\le\gamma\log N\) tends to zero, at most
\(E_J(N^{-1}+N^{\gamma-1})\) after the fixed initial segment.

For comparison, the accumulated conditional entropy of this first output
digit satisfies the much smaller bound

\[
\boxed{\sum_{j<N}h_{\rm b}(\epsilon_j)=o(\log N),}
\tag{11}
\]

where natural logarithms are used. Indeed, for a block of \(N\) tail terms
with sum \(E\le E_J\), entropy concavity gives
\(\sum h_{\rm b}(\epsilon_j)\le N h_{\rm b}(E/N)
\le E\log(N/E)+E\). Split off a fixed initial segment, divide by
\(\log N\), and then let \(J\to\infty\). These are entropies of the
actual rows at the clock-marked spine roots. They are not an identification
of a compact process's Kolmogorov--Sinai entropy.

### An exact arithmetic pairing shows what the real phase misses

At each root, pair its positive unit predecessors in increasing order of
their valuation exponents. Consecutive legal unit exponents differ by two
or four, and the resulting involution \(\mathcal S_q\) pairs

\[
x\longleftrightarrow4x+1
\quad\hbox{or}\quad
x\longleftrightarrow16x+5.
\tag{12}
\]

Each pair has opposite nonzero residues modulo three and the same forward
image. It also has **exactly the same shifted binary phase**:

\[
\{\log_2(x+1/3)\}
=\{\log_2(\mathcal S_qx+1/3)\}.
\tag{13}
\]

Indeed, \(4x+1+1/3=4(x+1/3)\), and the other factor is \(16\).
The unshifted phases differ by \(O(1/x)\). Therefore the existing real
phase equidistribution cannot by itself distinguish the competing canonical
branches that are separating in (8).

For a direct information cost, compare a row with its image under this
involution and then project to the first ternary digit. Data processing gives

\[
D_{\rm KL}\!\left(K(q_{j+1},\cdot)
\,\middle\Vert\,(\mathcal S_{q_{j+1}})_*K(q_{j+1},\cdot)\right)
\ge(1-2\epsilon_j)
\log\frac{1-\epsilon_j}{\epsilon_j}.
\tag{14}
\]

The mean cumulative cost, divided by \(N\log N\), has lower limit at
least one, by (8) and \(\eta_J\to0\). The full countable divergence may
be infinite; the displayed two-digit lower bound is finite at every root.
This compares arithmetic siblings in the same actual row, not the two
different canonical kernels compared in PR180. Applying the involution at
every time is not asserted to produce another consistent forward path.

### The exact missing inference

Let \(\pi_N=N^{-1}\sum_{j<N}\delta_{q_{j+1}}\). Equations (7)--(10)
show that the laws \(\Xi_*\pi_N\) escape every bounded interval of
\(\mathbb R\). Hence **tightness of this one scalar canonical log-odds
along the retained ordinary time law would exclude escape**. This asks for
less than identifying every compact inverse row or an entire finite positive
compact density. No such tightness has been proved here.

Pointwise positivity of both branches does not supply it. Neither does the
real phase statement (13). Dropping the clock and mixing the roots can also
average two almost deterministic opposite residues into a balanced marginal;
that operation does not bound (8). The failed step in the attempted entropy
closure is precisely the passage from the known canonical trace to tightness
of (6) on these moving ordinary roots.

## 3. A complete trace profile across the original-source clock

For an integer offset \(s\) and \(j+s\ge0\), define

\[
f_j(s)=K^{j+s}g(q_j)
=\frac{D_{j+s+1}(q_j)}{F(q_j)}.
\tag{15}
\]

Retracing from \(q_{j+k}\) to \(q_j\) has probability
\(d_{j+k}/d_j\). Conditioning on that event and using \(0\le g\le C_g\)
gives, for every allowed \(s\),

\[
|f_{j+k}(s)-f_j(s)|
\le C_g(1-d_{j+k}/d_j).
\]

There is consequently a single bounded bilateral profile
\(f_\infty:\mathbb Z\to[0,C_g]\), with the uniform estimate

\[
\boxed{\sup_{s\ge-j}|f_j(s)-f_\infty(s)|
\le C_g(1-d_\infty/d_j).}
\tag{16}
\]

Its negative end vanishes. Retrace to \(q_L\) to obtain

\[
0\le f_\infty(-L)
\le g(q_L)+C_g(1-d_\infty/d_L)\longrightarrow0,
\tag{17}
\]

because \(F(q_L)\sim u_\infty q_L\to\infty\). More generally,

\[
\lim_{L\to\infty}\sup_{\substack{j,m\ge0\\j\ge m+L}}
\frac{D_{m+1}(q_j)}{F(q_j)}=0.
\tag{18}
\]

This follows by replacing \(L\) in the preceding retrace estimate by
\(j-m\) and taking the supremum over the tail.

The positive end has the opposite mean behavior. The exact moving trace
theorem from PR175 is

\[
\lim_{R\to\infty}\sup_j\frac1R\sum_{s=0}^{R-1}|f_j(s)-1|=0.
\]

Letting \(j\to\infty\) for each finite sum, using (16), yields

\[
\boxed{\lim_{R\to\infty}\frac1R
\sum_{s=0}^{R-1}|f_\infty(s)-1|=0.}
\tag{19}
\]

There is no claim of pointwise convergence at the positive end. The
distinction between (17) and (19) is tied to one fixed original source; it
cannot be removed by shifting the onset convention. The profile is compatible
with every supplied fixed-root and moving-clock mean theorem.

## 4. The bounded-corrector completion fails on actual finite paths

A tempting exactness argument would solve

\[
(I-K)\psi=g-1
\tag{20}
\]

with a bounded \(\psi\). Telescoping would then give
\(\sup_q|\sum_{m<M}(K^m g(q)-1)|\le2\|\psi\|_\infty\),
incompatible with the pre-source plateau (18).

This premise is stronger than the Collatz question. Under the same supplied
full positive-unit trace, explicit finite ordinary paths already refute it,
without assuming an escaping orbit.

For every positive even \(N\), put

\[
p_N=2^{N+1}-1,\qquad
q_{N,i}=3^i2^{N+1-i}-1\quad(0\le i\le N).
\tag{21}
\]

All these numbers are positive odd ternary units. For \(i<N\), the exact
valuation is one and \(U(q_{N,i})=q_{N,i+1}\). Harmonicity and positivity
therefore give

\[
F(q_{N,N})\ge(3/2)^N F(p_N)\ge\alpha(3/2)^N.
\tag{22}
\]

The positive operator satisfies \(P\mathbf1\le2\), hence
\(D_{m+1}\le2^{m+1}\). At the actual endpoint
\(q_{N,N}=2\cdot3^N-1\), equations (4) and (22) imply

\[
\boxed{K^m g(q_{N,N})
\le\frac2\alpha\,2^m(2/3)^N.}
\tag{23}
\]

Choose any fixed \(0<c<\log_2(3/2)\) and
\(M_N=\lfloor cN\rfloor\). The right side tends to zero uniformly for
\(0\le m<M_N\). Consequently

\[
\sum_{m<M_N}(K^m g(q_{N,N})-1)
=-M_N(1+o(1)),
\tag{24}
\]

contradicting the bounded-corrector conclusion. These are changing **finite**
ordinary witnesses; (21) does not construct a single infinite all-ones
valuation sequence. The argument uses the full positive-unit trace operator,
including any periodic vertices it may contain, rather than claiming that
every witness lies in the nonperiodic killed domain.

Thus a global bounded Poisson primitive, or uniform-in-root exactness strong
enough to imply it, is an unavailable closing premise. A successful argument
must use the retained positive ordinary source in a way that these finite
paths cannot imitate. The remaining substantive target in this lane is the
scalar canonical log-odds tightness after (14); neither that target nor full
escape exclusion has been established.
