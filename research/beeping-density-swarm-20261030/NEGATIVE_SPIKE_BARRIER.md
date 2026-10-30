# Negative reference spikes and positive-source bounds

**Status: PROPOSED elementary theorems with proofs, including a fixed-positive-source bound; a uniform or summable transported bound remains OPEN.** These statements concern the auxiliary ternary residue law used in inverse counting. They neither construct a positive counterexample nor rule out stronger actual predecessor-density theorems.

## 1. Reference law and normalization

Let \(A_1,A_2,\ldots\) be independent positive integers with
\(\Pr(A_i=a)=2^{-a}\). For \(q\ge1\), put

\[
Y_q=\sum_{j=1}^q 3^{j-1}2^{-(A_1+\cdots+A_j)}
\pmod {3^q},\qquad
\rho_q(y)=3^q\Pr(Y_q=y).
\tag{1}
\]

Thus the mean of \(\rho_q\) over the full group \(\mathbb Z/3^q\mathbb Z\) is 1. This is Lau's normalization. Mazur's corresponding density is \((2/3)\rho_q\); multiplying by that constant changes none of the critical exponents below. The law is compatible under reduction of residues, because all later summands contain the appropriate power of 3.

## 2. The unavoidable spike

### DSP-001. A negative fixed point forces exponential density height

For every \(q\ge1\),

\[
\rho_q(-1\bmod3^q)\ge(3/2)^q.
\tag{2}
\]

**Proof.** The event \(A_1=\cdots=A_q=1\) has probability \(2^{-q}\). On this event,

\[
Y_q=\frac12\sum_{j=0}^{q-1}(3/2)^j=(3/2)^q-1
\equiv-1\pmod{3^q}.
\]

Multiplication by \(3^q\) yields (2). The ordinary negative value \(-1\) is fixed by the affine branch \((3x+1)/2\); this is the arithmetic source of the spike. No asymptotic mixing theorem is used.

In particular, **no uniform global \(L^\infty\) bound for the reference densities is possible**. A proposed improvement that relies on such a bound is false even before any positive-orbit counting issue arises.

### DSP-002. Explicit obstruction exponent for an integrable tail bound

Define

\[
E_q(U)=3^{-q}\sum_{y\bmod3^q}(\rho_q(y)-U)_+,
\qquad
\delta_* = \frac{\log2}{\log(3/2)}.
\tag{3}
\]

If \(k\ge1\), \(q\ge k\), and \(U\le(3/2)^k/2\), then

\[
E_q(U)\ge2^{-k-1}.
\tag{4}
\]

Indeed, the ball \(B_k=\{y:y\equiv-1\pmod{3^k}\}\) has Haar mass \(3^{-k}\), and (1) gives it probability at least \(2^{-k}\), independently of \(q\ge k\). Summing \((\rho_q-U)_+\ge\rho_q-U\) on this ball gives
\(E_q(U)\ge2^{-k}-U3^{-k}\), which implies (4).

Consequently there is an absolute \(c_*>0\) such that, for every \(U\ge1\) and all sufficiently large \(q\),

\[
E_q(U)\ge c_* U^{-\delta_*}.
\tag{5}
\]

For example choose \(k=\lceil\log_{3/2}(2U)\rceil\). Then \(2^{-k-1}\ge\frac14(2U)^{-\delta_*}\), so \(c_*=2^{-\delta_*-2}\) works. Therefore a uniform polynomial tail estimate \(E_q(U)\le C U^{-\delta}\), for all \(U\) and arbitrarily large \(q\), cannot hold with \(\delta>\delta_*\approx1.709511\).

### DSP-003. Failure of the critical strong moment

Let

\[
p_*=1+\delta_*=\frac{\log3}{\log(3/2)}.
\tag{6}
\]

Then for every \(Q\ge1\),

\[
3^{-Q}\sum_{y\bmod3^Q}\rho_Q(y)^{p_*}
\ge Q\,2^{1-2p_*}.
\tag{7}
\]

Thus the reference densities have no bounded global strong \(L^{p_*}\) norm; the obstruction includes the endpoint, not just larger moments.

**Proof.** For each \(0\le k<Q\), consider the event
\(A_1=\cdots=A_k=1\), \(A_{k+1}=2\), with all later variables unrestricted. Its probability is \(2^{-k-2}\), and

\[
Y_Q+1\equiv \frac{5\,3^k}{2^{k+2}}\pmod{3^{k+1}}.
\]

It therefore lies in the annulus \(v_3(y+1)=k\), whose Haar mass is \(2\,3^{-k-1}\). The annuli are disjoint. Jensen's inequality on the \(k\)-th annulus gives a contribution at least

\[
\frac{(2^{-k-2})^{p_*}}{(2\,3^{-k-1})^{p_*-1}}
=2^{1-2p_*},
\]

because \(3^{p_*-1}=2^{p_*}\). Sum over \(k=0,\ldots,Q-1\). This proves (7). It does not rule out a suitable weak endpoint bound, and it does not prove one.

## 3. Consequence for one specific census mechanism

The inverse counting arguments under discussion have a global clipping step of the schematic form

\[
Z\le A U W+B R E_q(U),\qquad
\#\{\text{sources in a shell of scale }X\}\ge\frac XR W,
\tag{8}
\]

where \(R\) is a fixed positive root, \(W\) is its retained unmarked weight, \(Z\ge z_0>0\) is a retained marked mass, and \(A,B,z_0>0\) are constants independent of \(R\). The clipping height is fixed for this root before \(q\to\infty\). Here a height-\(U\) approximant to \(\rho_q\) is paid for by a nonnegative error. Such an error necessarily dominates \((\rho_q-U)_+\), so DSP-002 applies to any uniform global use of this procedure.

If one has an upper bound \(E_q(U)\le C U^{-\delta}\), selecting \(U\) large enough to make the error at most \(z_0/2\) gives \(U\asymp R^{1/\delta}\), hence a guaranteed density on the scale

\[
R^{-(1+1/\delta)}.
\tag{9}
\]

DSP-002 therefore forbids obtaining an exponent strictly below

\[
1+\frac1{\delta_*}=\frac{\log3}{\log2}=\log_2 3\approx1.584963
\tag{10}
\]

**solely by improving a global polynomial tail in this clipping/source-charge mechanism**. More directly, for any fixed clipping height that makes the subtracted global error in (8) smaller than \(z_0\), (5) forces \(U\gtrsim R^{1/\delta_*}\); the lower bound extracted just from (8) is then at most a constant times \(R^{-\log_2 3}\).

This is a limitation of the stated certificate mechanism, not an upper bound on the true predecessor density. It assumes the marked lower bound remains on a root-independent constant scale; a stronger root-dependent lower bound, a different counting argument, or a source-conditioned error estimate is outside its scope. Lau's current source-qualified target exponent \(25/11\) is above this barrier. The theorem does not claim that the barrier is achievable, or that improving that exponent would resolve Collatz.

## 4. The positive-source escape hatch

The preceding obstruction comes from allowing every ternary residue, including the completion \(-1\). A fixed positive integer has a finite, exactly computable budget for that initial all-one run.

### DSP-004. Exact source-conditioned run cap

Let \(t\) be a positive odd integer. The inverse branch with valuation 1 is
\(I_1(t)=(2t-1)/3\). A length-\(r\) initial run of these branches is an integral positive odd inverse path if and only if

\[
3^r\mid t+1.
\tag{11}
\]

When it exists, its endpoint is

\[
I_1^r(t)+1=\left(\frac23\right)^r(t+1).
\tag{12}
\]

For \(r=0\) the statement is tautological. For \(r\ge1\), iterate the affine identity \(I_1(t)+1=(2/3)(t+1)\). Integrality is equivalent to the displayed divisibility. If it holds, \((t+1)/3^r\) is a positive even integer, so the final value \(2^r(t+1)/3^r-1\) is positive and odd; the same applies to every prefix. The exact valuation is 1 because \(3I_1(u)+1=2u\) and \(u\) is odd.

Thus

\[
r\le v_3(t+1)\le\log_3(t+1),
\tag{13}
\]

whereas \(-1\) supports runs of every length. The examples \(t=2\cdot3^r-1\) show why no target-independent finite cap exists: their length-\(r\) run ends at \(2^{r+1}-1\). This is elementary branch arithmetic, not a newly claimed Collatz theorem.

One can make the conditioning explicit in the reference recurrence. Set \(\rho_0=1\), \(v=v_3(t+1)\), and \(t_r=I_1^r(t)\) for \(r\le v\). Partition words by their first exponent different from 1. Then, for \(q\ge1\),

\[
\begin{aligned}
\rho_q(t)
={}&\mathbf1_{q\le v}(3/2)^q\\
&+\sum_{r=0}^{\min(v,q-1)}(3/2)^r
\sum_{\substack{a\ge2\\3\mid2^a t_r-1}}
\frac3{2^a}\,
\rho_{q-r-1}\!\left(\frac{2^a t_r-1}{3}\right).
\end{aligned}
\tag{14}
\]

The sums are nonnegative and convergent at every fixed \(q\); the identity follows by repeated use of the first-letter transfer. Formula (14) removes the fictitious *unlimited initial* negative run at a fixed positive target. It does not control later long runs: their parent endpoint changes under the other inverse branches, and their valuation budget may grow.

**Next precise obligation.** Bound the accumulated, source-conditioned contribution of these later near-negative runs on the actual transported family, retaining the root and every intermediate positive endpoint. A bound that simply replaces those endpoint budgets by the supremum over all residues reintroduces DSP-002. No surviving global budget of this type is proved here.

## 5. A pointwise bound that genuinely uses positive integers

### DSP-005. Reference density grows at most linearly in depth at a fixed positive source

For every positive odd integer \(t\) and every \(q\ge1\),

\[
\rho_q(t)\le6qt+(64/81)^q.
\tag{15}
\]

Unlike the negative spike, this is a bound for one fixed positive ordinary integer, at every depth. It needs neither convergence of that integer nor a no-return assumption.

**Proof.** A valuation word \(w=(a_1,\ldots,a_q)\), interpreted from the root outwards, has total valuation \(A=\sum a_i\), weight \(w_A=3^q2^{-A}\), and an affine inverse source \(x\). A nonempty residue fiber at the positive odd root \(t\) forces each inverse step to be an integral positive odd step. Its exact affine identity has the form

\[
w_Ax+\beta=t,\qquad \beta>0.
\tag{16}
\]

At fixed \(q\), different legal words have different sources: the actual deterministic Syracuse orbit of a source fixes all its valuations in reverse order. This statement remains true when \(t\) is periodic, because the depth is fixed. A no-return condition is needed only if one tries to combine arbitrary different depths without accounting for multiplicity.

For a fixed total valuation \(A\), (16) puts all these distinct positive integer sources below \(t/w_A\). There are at most \(t/w_A\) of them, so their total weight is at most \(t\). The possible integers \(q\le A\le6q\) number at most \(6q\), giving the first term of (15).

For \(A>6q\), discard all residue and integrality restrictions. The total weight is at most

\[
3^q\Pr(A_1+\cdots+A_q>6q).
\]

The geometric law has \(\mathbb E(3/2)^{A_i}=3\). Markov's inequality therefore bounds this last display by

\[
3^q\,\frac{3^q}{(3/2)^{6q}}=(64/81)^q.
\]

This proves (15). The constant 6 is chosen for a short exact argument, not claimed optimal.

### Corollary: different resolvent radii at positive and negative ordinary points

Put \(\rho_0(t)=1\). For every fixed positive odd \(t\) and \(0\le z<1\),

\[
\sum_{q\ge0}z^q\rho_q(t)
\le1+\frac{6tz}{(1-z)^2}
+\frac{(64/81)z}{1-(64/81)z}<\infty.
\tag{17}
\]

Thus the depth generating series has radius of convergence at least 1 at each fixed positive odd integer. At \(-1\), DSP-001 makes its radius at most \(2/3\). This is an exact analytic distinction between positive ordinary sources and the negative fixed-point completion. It is a statement about **weighted inverse histories**, not termination of a forward trajectory. No finite value at the critical point \(z=1\) is proved.

The pointwise bound (15) removes the exponential-in-depth pathology at fixed positive \(t\), but grows with depth and with the endpoint. In the actual transported family, endpoints vary. Substituting (15) without summing its endpoint factor would therefore lose the root-independent census estimates. The useful remaining question is whether these positive-source bounds can be averaged with their actual transported weights while retaining a bounded or summable budget.

## 6. Why a vanishing-loss reference mask alone does not remove the barrier

Let \(\widetilde\mu_q\le\mu_q\) be a selected subprobability reference law with discarded mass \(\varepsilon_q\to0\), and put \(\widetilde\rho_q=3^q\widetilde\mu_q\). Its clipping error satisfies

\[
\widetilde E_q(U)\ge E_q(U)-\varepsilon_q,
\tag{18}
\]

because positive-part clipping is 1-Lipschitz and the mean loss of density is exactly \(\varepsilon_q\). For **each fixed** \(U\), first choose finite \(k\) as in DSP-002 and then let \(q\to\infty\). Equations (4) and (18) retain the same obstruction exponent. Thus conditioning on an asymptotically full-probability collection of typical reference words does not establish a uniform global tail exponent beyond DSP-002 in this order of limits.

This does **not** rule out moving truncation heights \(U_q\to\infty\) with losses comparable to \(U_q^{-\delta_*}\). Such a mask can remove progressively deeper spikes at vanishing total mass. Its growing height must then be paid in the census; it does not by itself yield a fixed positive density for a fixed target. A successful use of this possibility needs a separate argument controlling that cost.

## 7. Evidence and source boundary

Definitions (1) and the clipping/counting setting come from the primary papers:

* Lech Mazur, supplied v2.1 paper, Sections 2 and 5: <https://www.proofatlas.ai/papers/positive-density-log-time-collatz/Mazur_Explicit_Positive_Density_Collatz_Convergence_in_Logarithmic_Time_v2.pdf>.
* Kenny Lau, Hexagon `2610.00249v2`, reference density in Section 2.3 and census in Section 6.5: <https://hexagonmath.org/pdf/2610.00249v2>.

DSP-001--005 are proved directly above, independently of the papers' analytic mixing or Lean checks. The companion `check_negative_spikes.py` checks exact finite residue identities, ordinary source caps, fixed-depth source injectivity, and the positive pointwise bound; it is a bounded replay of those identities, not a proof of the open transported budget or of Collatz.

The exact replay completed through reference level 6 (the infinite geometric sums are evaluated by their finite modular periods, not truncated). It checked 21 clipping inequalities, 21 annulus inequalities, 3,006 instances of (15), 5,001 positive odd source caps, and the arbitrary-length positive finite-witness family through length 512. It also enumerated all total-valuation-at-most-12 words through depth 4 for the 51 positive odd targets at most 101, checking source injectivity and each valuation layer's mass bound. Exact counts and reference-law fractions are in `negative_spikes_report.json`.
