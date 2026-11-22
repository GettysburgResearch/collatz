# Ordinary channels, multiplicative returns, and the critical five trace

**Status:** one new unconditional Lean theorem family, and a written composition
of explicitly source-qualified analytic inputs. No global five-merger existence,
finite five-energy estimate, escape exclusion, or full Collatz proof is claimed.

The late source inspected here is PR183 at
`68345f60a4f757acb42a69a4ac95910f8ce26163`, relative to
`907a540943090968bc683b1b9246208e9053c1f8`. The actual delta has a mathematical
commit `84a76f0d81839494e17a0de5fea207ea96da5f87` and a receipt-only follow-up.
This note uses the new ordinary-channel and asynchronous-residue arguments;
it does not repeat the upstream validation or certify every analytic import.

## 1. What the new channel theorem contributes

Write

\[
T(n)=\begin{cases}n/2,&n\equiv0\pmod2,\\(3n+1)/2,&n\equiv1\pmod2,\end{cases}
\qquad U(q)=\frac{3q+1}{2^{v_2(3q+1)}}.
\]

Let \(\mathcal O^*=\{q>0:q\text{ odd},\ 3\nmid q\}\), and let
\(N\subseteq\mathcal O^*\) exclude the points themselves on periodic orbits.
The operator \(L\) transports actual masses by \(U\), killing them upon
leaving \(N\). Its imported reference has

\[
L\nu=\nu,\qquad 0<\gamma/q\le\nu(q)\le A<\infty\quad(q\in N).       \tag{1}
\]

The population and canonical-envelope hypotheses in PR185 remain attached to
this input. No such analytic assumption is added to the new Lean module.

The new [Wold-channel note][wold], equations W4–W11, identifies one bilateral
shift for each actual escaping ordinary component \(C\). Every synchronous
class in that component has mass

\[
C_C=\lim_{j\to\infty}\nu(U^j x)\in(0,A],\qquad x\in C.
\]

The coordinate \(h_C\) retains the difference between meeting clocks:
\(h_C(Ux)=h_C(x)+1\). At frequency zero, however, the Abel boundary residue
of a finitely supported signed source depends on its **total component mass**:

\[
\lim_{r\uparrow1}(1-r^2)\mathcal E_\nu
 \left(\sum_{k\ge0}r^kL^k a\right)
=\sum_{C\ \mathrm{escaping}}\frac{|\sum_{x\in C}a(x)|^2}{C_C},
\quad \mathcal E_\nu(b)=\sum_{q\in N}\frac{|b(q)|^2}{\nu(q)}.       \tag{2}
\]

This retains asynchronous ordinary mergers. For example, if \(U^i x=U^j y=z\)
is the first common tail point, the cross term of two unit-source resolvents is

\[
r^{i+j}(1-r^2)\sum_{k\ge0}\frac{r^{2k}}{\nu(U^kz)}
\longrightarrow\frac1{C_C}.                                    \tag{3}
\]

For \(\delta_x-\delta_y\) in the same escaping component, the two diagonal
limits and this cross term cancel as \(1/C_C+1/C_C-2/C_C=0\), even when
\(i\ne j\). Dropping the cross term would incorrectly charge sources that
really merge. The full derivation and the separate cycle pole are in the
[asynchronous-residue note][async].

The bilateral summands are not eliminated by their classification: a bilateral
shift can be weakly stable while retaining the boundary residue in (2).

## 2. An unconditional odd-count bound for a return

The new core-only module `OddReturnClock.lean` proves the following. Suppose
\(n>0\), \(T^h(mn)=n\), and \(a\) is the number of odd inputs among these
\(h\) shortcut steps. If \(2^h\ne m3^a\), then

\[
\boxed{n<m9^a.}                                                \tag{4}
\]

The nonresonance hypothesis follows whenever \(m\) has a divisor \(d>1\)
coprime to two. In particular,

\[
T^h(5n)=n\quad\Longrightarrow\quad n<5\,9^{\operatorname{odds}(h,5n)}.
                                                                    \tag{5}
\]

There is no restriction on \(h\) or on any individual halving run. For the
accelerated odd map this gives the written corollary

\[
U^j(5n)=n\quad\Longrightarrow\quad n<5\,9^j.                    \tag{6}
\]

Here the segment realizing \(j\) accelerated steps has exactly \(j\) odd
inputs. Equation (6) is a return to the particular original source \(n\);
it is not a bound on an arbitrary downstream meeting of the two orbits.

**Proof of (4).** The exact affine identity and nonnegative correction give
\(2^h\ge m3^a\). Positivity of \(n\) and nonresonance strengthen this to
\(2^h\ge m3^a+1\). The already checked normalized-quotient theorem gives

\[
v:=\left\lfloor\frac n{3^a}\right\rfloor
 =\left\lfloor\frac {mn}{2^h}\right\rfloor.
\]

Consequently

\[
(m3^a+1)v\le2^hv\le mn<m3^a(v+1),
\]

so \(v<m3^a\), hence \(v+1\le m3^a\). Finally
\(n<3^a(v+1)\le m9^a\). If a divisor \(d>1\) of \(m\) is coprime to
two, equality \(2^h=m3^a\) would imply \(d\mid2^h\), a contradiction.
All of this proof, including the general multiplier version and the
contrapositive odd-budget exclusion, is kernel checked.

The four audited declarations are `return_odd_count_bound`,
`coprime_factor_return_odd_count_bound`, `five_return_odd_count_bound`, and
`no_five_return_within_odd_budget`. The namespace is `CollatzOddReturnClock`.
The author's source and exact development compiler record are bound by the
[odd-return receipt](../../reports/lean-global-closure-20261121/nov22/late/ODD_RETURN_CLOCK_REPLAY.json).

The earlier affine-merger theorem concerns two independent shortcut clocks:
if \(T^i n=T^j(5n)\) with \(i,j\le H\), then \(n+2^H\le3^H\).
Thus an all-source five-merger result necessarily permits clocks growing
with the source. The new theorem instead controls cancellation at the
original source in an odd-clock resolvent. Neither necessary bound constructs
a meeting.

## 3. The correct critical trace takes the boundary source by source

For completeness define the actual initial projection used by [the new
transport note][async]. Remove all powers of two from \(n\) to obtain
\(o(n)\), and put

\[
\pi(n)=\begin{cases}o(n),&3\nmid o(n),\\U(o(n)),&3\mid o(n).\end{cases}
\]

This is an actual orbit point, preserves the ordinary component, and is at
most \(2n\). In general one must not replace \(\pi(5n)\) by \(5\pi(n)\).
On the five-energy domain \(n\in\mathcal O^*\), both simplify exactly:
\(\pi(n)=n\) and \(\pi(5n)=5n\).

Fix an escaping component \(C\), and let \(\chi_C\) be its invariant
indicator on all positive integers. Use the signed source on \(N\)

\[
b_{n,C}=\chi_C(n)\delta_{\pi(n)}
       -\chi_C(5n)\delta_{\pi(5n)},                            \tag{7}
\]

where a term with coefficient zero is omitted; no Dirac mass outside the
specified domain is introduced. Equations (2)–(3) give, for every fixed \(n\),

\[
R_{n,C}:=\lim_{r\uparrow1}(1-r^2)\mathcal E_\nu(B_r b_{n,C})
=\frac{|\chi_C(n)-\chi_C(5n)|^2}{C_C},
\qquad B_r=\sum_{k\ge0}r^kL^k.                               \tag{8}
\]

Therefore the sourcewise-boundary harmonic trace is exactly

\[
\boxed{\mathfrak T_C:=\sum_{n\in\mathcal O^*}\frac{R_{n,C}}n
=\frac{E_5(1;\chi_C)}{C_C},\qquad
E_5(1;f)=\sum_{n\in\mathcal O^*}\frac{|f(5n)-f(n)|}{n}.}        \tag{9}
\]

The equality uses \(|u-v|^2=|u-v|\) for Boolean labels. The boundary limit
is taken **for each fixed original source first**, followed by the
nonnegative extended sum. No interchange of these operations is asserted.
Likewise, signed sources indexed by different \(n\) must retain their
original labels: summing them before squaring permits unrelated component
mismatches to cancel.

Under the separately source-qualified [finite-five-energy rigidity
corollary][rigidity], finite \(E_5(1;f)\) forces every ordinary invariant
metric label \(f\) to be constant. Its explicit analytic dependency ledger
includes the harmonic profile limit, the five-to-tripling comparison, and
the positive lower logarithmic predecessor-density argument. Those inputs
have not been replaced by (1) or by a Lean axiom here. Since an escaping
component excludes the component of one, (9) implies

\[
C\text{ escaping}\quad\Longrightarrow\quad\mathfrak T_C=+\infty
\quad\text{under that imported rigidity theorem}.             \tag{10}
\]

A proved finite bound on this particular trace would consequently exclude
that component. Neither the Wold theorem nor the affine identities supply
such a bound.

One can retain cycles as well. Let \(\widehat L\) kill only at one, and use
the reference of [the transport note][async], equation A22:

\[
w(q)=\nu(q)\ (q\in N),\qquad w(q)=1
\quad(q\text{ on a nontrivial cycle}),\qquad w(q)\le A_*:=\max(A,1).
\]

For \(n\in\mathcal O^*\), omit any atom at the killed point one and put
\(b_n=\delta_n-\delta_{5n}\). The limit

\[
R_n=\lim_{r\uparrow1}(1-r^2)\mathcal E_w(\widehat B_r b_n),
\qquad \widehat B_r=\sum_{k\ge0}r^k\widehat L^k,              \tag{11}
\]

is zero when the two ordinary sources lie in the same component. For
different components its value is the sum of \(1/C_D\) over the escaping
components touched by the pair, unless a nontrivial cycle component is
touched, in which case it is infinite. The component of one contributes
zero. To check the same-cycle case directly, the tail difference has the
form \((r^i-r^j)/(1-r^p)\) at each cycle position; it remains bounded as
\(r\uparrow1\), so its normalized energy tends to zero. In the unmatched
cycle case the uncancelled \((1-r)^{-2}\) energy pole survives.

In particular, for the indicator \(\chi_1\) of the basin of one,

\[
R_n\ge A_*^{-1}|\chi_1(n)-\chi_1(5n)|.                       \tag{12}
\]

Thus, under the same imported rigidity theorem, the precise cycle-sensitive
closing estimate would be

\[
\mathfrak T:=\sum_{n\in\mathcal O^*}\frac{R_n}{n}<\infty.     \tag{13}
\]

It would imply that \(\chi_1\) is constant, hence every positive source
reaches one. If Collatz holds, every fixed pair in (11) is killed in finite
time and \(\mathfrak T=0\). These are implications identifying the missing
estimate, not a proof of its finiteness.

## 4. The fixed-radius whole-source trace is always infinite

Replacing the sourcewise limit in (13) by a sum at fixed \(r<1\) cannot
give the closing estimate: even if all orbits converge, that sum diverges.
The following quantitative calculation works on every odd ternary unit
\(n>1\); it does not assume that all sufficiently large sources are
nonperiodic or use a density assertion about nonperiodic points.

Fix \(0<r<1\) and an integer \(J\ge0\). For \(n\ge5\,9^J\), (6)
excludes a return \(U^t(5n)=n\) at any \(t\le J\). Inspect the single
coordinate \(n\) of \(\widehat B_r b_n\):

* If \(n\) is not periodic, its own source contributes one. The other source
  contributes zero if it never reaches \(n\), and \(r^t\) at its unique visit
  if it does.
* If \(n\) is periodic with period \(p\), its own source contributes
  \(1/(1-r^p)\). The other source contributes zero or
  \(r^t/(1-r^p)\), with \(t\) its first hitting time.

In either case that coordinate is at least \(1-r^{J+1}\). Since
\(w(n)\le A_*\),

\[
\mathcal E_w(\widehat B_r b_n)
\ge\frac{(1-r^{J+1})^2}{A_*}
\qquad(n\in\mathcal O^*,\ n\ge5\,9^J).                       \tag{14}
\]

For a finite cutoff \(X\), this already gives

\[
(1-r^2)\sum_{\substack{n\in\mathcal O^*\\5\,9^J\le n\le X}}
\frac{\mathcal E_w(\widehat B_r b_n)}n
\ge\frac{(1-r^2)(1-r^{J+1})^2}{A_*}
\sum_{\substack{n\in\mathcal O^*\\5\,9^J\le n\le X}}\frac1n.   \tag{15}
\]

The last sum diverges: \(\mathcal O^*\) consists of the positive integers
congruent to one or five modulo six. Hence

\[
\boxed{\sum_{\substack{n\in\mathcal O^*\\n>1}}
\frac{(1-r^2)\mathcal E_w(\widehat B_r b_n)}n=+\infty
\quad\text{for every fixed }0<r<1.}                           \tag{16}
\]

The basic divergence also follows from the initial atom and the elementary
fact \(5n\ne n\), giving the weaker lower bound \(1-r\). The contribution
of (6) is the quantitative arbitrary-window cutoff in (14)–(15): for any
prescribed \(J\), the source atom cannot be cancelled during the first
\(J\) odd steps once \(n\ge5\,9^J\). The new theorem is not needed merely
to establish divergence in (16).

This calculation explains why a bound for (13) must concern sourcewise
boundary values or a justified subtraction or cutoff. A uniform bound on
the unsubtracted fixed-radius trace is false, including under full Collatz.

## 5. Remaining arithmetic step and overlap with the late carry work

The new PR183 packet handles independent fixed cycle blocks, exact ordinary
channels, asynchronous source collisions, and arbitrary finite carry. Its
[carry note][carry], AC1–AC2, already writes the all-word complement identity
using \(S(b)=b/2\) on even inputs and \(S(b)=(3b-1)/2\) on odd inputs.
That overlaps the present branch's signed-carry calculus and must receive
its own source credit. Neither version supplies a universal decreasing
selection rule merely by allowing arbitrarily large initial debt.

The combined arithmetic results are necessary conditions and exact
identities. They still do not establish an actual merger of \(n\) with
\(5n\) for every positive source, nor the harmonic summability of component
mismatches in (9) or (13). The analytic channel theorem identifies those
mismatches and their clock-correct boundary weights. It does not force
cross-component equality under multiplication by five.

The next global estimate must therefore control these actual boundary
amplitudes while retaining the original source labels. It cannot follow
from fixed-clock affine identities alone, from a generic spectral statement,
or from the false fixed-radius bound ruled out by (16).

## Frozen source ledger

| Source | Pin and use |
|---|---|
| PR183 ordinary channels | `68345f60a4f757acb42a69a4ac95910f8ce26163`, `research/profound-step-20261122/operator/WOLD_CHANNELS.md`, W1–W11 |
| PR183 all-clock and cycle residues | Same pin, `research/profound-step-20261122/transport/ASYNCHRONOUS_RESIDUE.md`, A2, source-pair kernels, actual projection, A21–A24 |
| PR183 finite carry | Same pin, `research/profound-step-20261122/mergers/ARBITRARY_DEBT.md`, AC1–AC2 and scope of paid padding |
| PR185 reference | `276be8154f4e867acc0230466b34d9cb224aacf5`, `research/whole-repo-closure-20261122/ORDINARY_HARMONIC_FLOW_AND_COLLISIONS.md`, as explicitly imported by PR183 |
| PR180 finite-energy rigidity | `d0349de2108abb7c8fb8393c086610e3372df116`, `research/lean-ordinary-closure-20261121/REPOSITORY_RIGIDITY_COROLLARY.md`, harmonic theorem and its dependency ledger |
| PR163 five-to-tripling comparison | `051237135a34ae7d4b973ee5fcf5da04ded6f0fc`, `research/deep-reverse-closure-20261120/FIVE_SLICE_ENERGY.md`, FE1, via PR180 |
| This branch's finite arithmetic | `CollatzGlobalClosure.InverseBudget.normalized_quotient`, `CollatzGlobalClosure.MergerClockRigidity`, and the new `OddReturnClock.lean`; exact source hashes and fresh dependency compilation in the attached receipt |

[wold]: https://github.com/GettysburgResearch/collatz/blob/68345f60a4f757acb42a69a4ac95910f8ce26163/research/profound-step-20261122/operator/WOLD_CHANNELS.md
[async]: https://github.com/GettysburgResearch/collatz/blob/68345f60a4f757acb42a69a4ac95910f8ce26163/research/profound-step-20261122/transport/ASYNCHRONOUS_RESIDUE.md
[carry]: https://github.com/GettysburgResearch/collatz/blob/68345f60a4f757acb42a69a4ac95910f8ce26163/research/profound-step-20261122/mergers/ARBITRARY_DEBT.md
[rigidity]: https://github.com/GettysburgResearch/collatz/blob/d0349de2108abb7c8fb8393c086610e3372df116/research/lean-ordinary-closure-20261121/REPOSITORY_RIGIDITY_COROLLARY.md
