# What a Følner clock filter removes, and what it preserves

**Status:** written deductions from the source-qualified ordinary Wold-channel
theorem at PR183 `68345f60a4f757acb42a69a4ac95910f8ce26163`; no new global
energy bound. This supplements, without changing, `LATE_CHANNEL_FIVE_TRACE.md`.
All references to ordinary components, \(N\), \(\nu\), \(C_C\), and the
unitary projection use [that frozen channel source][wold]. Cycles remain
outside this killed-domain calculation and retain the separate treatment
in the preceding note.

## 1. An exact formula for every normalized clock filter

Let \(g\in\ell^2(\mathbb N)\) have norm one, extend it by zero to
\(\mathbb Z\), and let \(\sigma\) be bilateral translation on
\(\ell^2(\mathbb Z)\). For a finitely supported physical source mass \(a\)
on \(N\), define

\[
\mathcal F_g a=\sum_{k\ge0}g(k)L^k a.                         \tag{F1}
\]

This is well defined in collision norm even when \(g\notin\ell^1\).
For one source \(x\), the surviving orbit has no repetitions and
\(\nu(U^kx)\ge\nu(x)\), so

\[
\mathcal E_\nu(\mathcal F_g\delta_x)
 =\sum_{k\text{ before killing}}\frac{|g(k)|^2}{\nu(U^kx)}
 \le\frac1{\nu(x)}.
\]

Finite sums follow by the norm triangle inequality. Denote the Wold unitary
projection on masses by \(\mathcal P_u a=\nu\Pi_u(a/\nu)\). It is an
orthogonal projection for \(\mathcal E_\nu\).

Fix an escaping component \(C\). For every original source
\(n\in\mathcal O^*=\{n>0:n\text{ odd},3\nmid n\}\), retain its own
signed pair

\[
b_{n,C}=\chi_C(n)\delta_n-\chi_C(5n)\delta_{5n},
\]

omitting zero-coefficient terms. If both points are in \(C\), let
\(d_n=h_C(5n)-h_C(n)\), their actual odd-clock lag. Then

\[
\boxed{\mathcal E_\nu(\mathcal P_u\mathcal F_g b_{n,C})
 =\frac{|\chi_C(n)-\chi_C(5n)|}{C_C}
 +\frac{\mathbf1_{\{n,5n\in C\}}}{C_C}
       \|g-\sigma^{d_n}g\|_2^2.}                            \tag{F2}
\]

**Proof.** A unit atom at \(x\in C\) projects to the mass profile concentrated
at synchronous height \(h_C(x)\), with density \(1/C_C\) throughout that
class. After (F1), its class density at height \(h\) is
\(g(h-h_C(x))/C_C\). Each class has \(\nu\)-mass \(C_C\), so its total
squared norm is \(\|g\|_2^2/C_C=1/C_C\). Two atoms in the same component
produce the difference of the two translated profiles. An unmatched atom
produces a single norm-one profile. This gives (F2).

The physical norm decomposes orthogonally into this quantity and a
nonnegative contribution from the unilateral part. In particular,

\[
\mathcal E_\nu(\mathcal F_g b_{n,C})
 \ge\frac{|\chi_C(n)-\chi_C(5n)|}{C_C}                       \tag{F3}
\]

for **every** normalized clock filter, without a Følner assumption. A
time filter can suppress a lag between two sources already in the same
component. It cannot suppress an unmatched ordinary component source.

## 2. Fejér and Poisson filters give explicit lag costs

For the flat filter
\(g_J(k)=J^{-1/2}\mathbf1_{0\le k<J}\),

\[
\mathcal F_{g_J}=\sqrt J\,\mathcal C_J,
\quad\mathcal C_J=J^{-1}\sum_{k<J}L^k,
\quad\|g_J-\sigma^d g_J\|_2^2=2\min(1,|d|/J).               \tag{F4}
\]

For the one-sided geometric filter
\(g_r(k)=\sqrt{1-r^2}\,r^k\),

\[
\mathcal F_{g_r}=\sqrt{1-r^2}\,B_r,
\qquad\|g_r-\sigma^d g_r\|_2^2=2(1-r^{|d|}).                 \tag{F5}
\]

These are exact identities for the unitary contribution, not asymptotic
estimates that ignore different meeting clocks. Their limits eliminate the
second term of (F2) for every fixed physical pair and preserve its first term.

More generally, assume \(\|g_j\|_2=1\) and
\(\|g_j-\sigma g_j\|_2\to0\). Then the same holds for each fixed integer
translation, and the \(\ell^2\)-mass of \(g_j\) in any fixed finite set of
clock indices tends to zero. For a fixed physical atom in \(C\), split
its norm sum into a finite initial segment and the tail on which
\(1/\nu(U^kx)\) is uniformly close to \(1/C_C\). This proves
\(\mathcal E_\nu(\mathcal F_{g_j}\delta_x)\to1/C_C\).

For two sources whose first common endpoint is \(z\), reached at clocks
\(p,q\), their entire cross term is

\[
\sum_{k\ge0}
 \frac{g_j(p+k)\overline{g_j(q+k)}}{\nu(U^kz)}.               \tag{F6}
\]

The same finite-tail split, Cauchy–Schwarz, and translation invariance of
the filters make (F6) tend to \(1/C_C\). Therefore the full physical
norm, including its orthogonal remainder, satisfies

\[
\mathcal E_\nu(\mathcal F_{g_j}b_{n,C})
 \longrightarrow\frac{|\chi_C(n)-\chi_C(5n)|}{C_C}
\quad\text{for each fixed }n.                               \tag{F7}
\]

This proof uses finite physical sources and actual common tails. It does
not assume the corresponding normalized limit for arbitrary Hilbert-space
vectors in the unilateral summand.

## 3. A source cutoff compatible with the critical five graph

There is an explicit finite exhaustion with vanishing critical five-boundary
cost. Write each \(n\in\mathcal O^*\) uniquely as \(n=5^k m\), where
\(5\nmid m\), and let

\[
\eta_{M,K}(5^km)=\mathbf1_{\{m\le M,\ 0\le k\le K\}},
\qquad H_M=\sum_{\substack{m\le M\\\gcd(m,30)=1}}\frac1m.
\]

The exact harmonic mass and five-edge boundary are

\[
\sum_{n\in\mathcal O^*}\frac{\eta_{M,K}(n)}n
 =\frac54(1-5^{-K-1})H_M,
\qquad
\sum_{n\in\mathcal O^*}
 \frac{|\eta_{M,K}(5n)-\eta_{M,K}(n)|}{n}=5^{-K}H_M.          \tag{F8}
\]

Only the last edge in each retained five-power ray crosses the boundary.
Since \(H_M\to\infty\), choosing
\(K(M)=\lceil2\log_5(1+H_M)\rceil\) makes the second quantity tend
to zero while the first tends to infinity, and the cutoffs converge
pointwise to one. This is a concrete weighted Følner exhaustion for the
five-edge Dirichlet form. It is not a claim that multiplication by five
preserves the discrete measure \(1/n\).

Such a cutoff removes a genuine five-edge boundary term: for bounded
\(f\), the elementary product estimate gives

\[
E_5(1;\eta f)
\le\sum_{n\in\mathcal O^*}\frac{\eta(5n)|f(5n)-f(n)|}{n}
 +\|f\|_\infty E_5(1;\eta).                                 \tag{F9}
\]

However, \(\eta f\) is generally not an ordinary invariant label even if
\(f\) is. Ordinary transport introduces the exact additional commutator

\[
\bigl[L(\eta a)-\eta La\bigr](q)
 =\sum_{Ux=q}(\eta(x)-\eta(q))a(x).                          \tag{F10}
\]

Nothing in (F8) bounds (F10), or the original mismatch term in (F9).
Consequently a five-graph cutoff cannot simply be inserted into an
ordinary-invariance or finite-energy rigidity theorem.

## 4. What diagonal source and clock cutoffs would have to prove

Let \(\eta_j\) be any finite source cutoffs in \([0,1]\) tending pointwise
to one, for example (F8). Let \(g_j\) be any normalized clock filters, and
form the finite quantities

\[
Q_{j,C}=\sum_{n\in\mathcal O^*}\frac{\eta_j(n)}n
              \mathcal E_\nu(\mathcal F_{g_j}b_{n,C}).        \tag{F11}
\]

Equations (F3) and nonnegative Fatou give, without requiring any comparison
between the growth rates of the two cutoffs,

\[
\boxed{\liminf_{j\to\infty}Q_{j,C}
       \ge\frac{E_5(1;\chi_C)}{C_C}.}                       \tag{F12}
\]

Thus a proved uniform finite bound on a diagonal family would be a valid
way to control the sourcewise-boundary trace. Unlike the infinite fixed
radius sum, each quantity in (F11) is finite. But every real component
mismatch survives unchanged, for every choice of normalized clock weights.
Under the source-qualified finite-five-energy rigidity theorem used in the
preceding note, an escaping component has \(E_5(1;\chi_C)=\infty\), so
\(Q_{j,C}\to\infty\) along every exhausting source cutoff. Time averaging
and the vanishing five-boundary of (F8) do not by themselves produce the
missing finite bound.

An actual proof using this route must therefore estimate the ordinary
commutator or the physical mismatch sum. The formulas specify the estimate
and preserve original-source labels; they do not replace it by amenability
of an unrelated operator.

## 5. Why an odd-count return bound must not be used as a merger bound

The new Lean theorem in `OddReturnClock.lean` controls a return
\(U^j(5n)=n\). The analogous bound for arbitrary downstream mergers is
false, even with uniformly bounded odd clocks.

For every \(k\ge1\), put \(h=6k+4\) and

\[
n_k=\frac{2^h-7}{9}.
\]

These are positive odd integers. Exact arithmetic gives

\[
U(n_k)=\frac{2^{h-2}-1}{3},\qquad U^2(n_k)=1,
\]

and

\[
U(5n_k)=\frac{5\cdot2^{h-5}-1}{3},\qquad
U^2(5n_k)=5,\qquad U^3(5n_k)=1.                             \tag{F13}
\]

The first halving exponents are exactly two and five; the second are
\(h-2\) and \(h-5\). The first nontrivial example is \(n_1=113\).
Thus the pair merges after two and three odd steps for arbitrarily large
sources, while its shortcut clocks grow with \(h\). The algebra in (F13)
holds for every \(k\ge1\), but the odd-unit five-energy domain requires
\(k\equiv0\) or \(1\pmod3\): \(k=2\), for example, gives the nonunit
\(n_2=7281\). Restricting to \(k=3j+1\), \(j\ge0\), supplies an
explicit infinite family within \(\mathcal O^*\). On this subfamily,
a clock filter shifted past these odd steps kills both atoms at one.
This is compatible with the
return-to-\(n\) lower bound and illustrates why total shortcut clocks,
odd clocks, common-tail lags, and source returns must remain distinct.

[wold]: https://github.com/GettysburgResearch/collatz/blob/68345f60a4f757acb42a69a4ac95910f8ce26163/research/profound-step-20261122/operator/WOLD_CHANNELS.md
