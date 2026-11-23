# Constructing the missing witness and testing the analytic closure

23 November 2026. **Full Collatz remains OPEN.**

This continuation attacks the missing universal construction in the
preceding triadic convergence theorem, the actual-source collision
upper, and unrestricted positive cycles. It uses the latest inspected
PR180 and PR182 source heads and primary literature on the p-adic
Subspace Theorem, finite-rank unit equations, coupling, and formal-series
conjugacies. It adds eighteen Lean-checked finite theorems and separately
reviewed written deductions. No missing closure statement is assumed
as an axiom.

Start with the [triadic construction](arithmetic/TRIADIC_CONSTRUCTION_ATTEMPT.md).
The other three attacks are the [coalescence calculation](dynamics/COALESCENCE_AND_CRITICAL_COLLISIONS.md),
the [unit-equation height attempt](cycles/UNIT_EQUATION_HEIGHT_ATTACK.md),
and the [carry and real/2-adic construction](transfer/REAL_ADIC_TRANSFER_ATTEMPT.md).

## 1. A candidate stream tied to the original positive integer

Fix the actual shortcut orbit `x_K=T^K(n)`, `n>0`, its parity `e_K`,
and its odd/even counts `p_K,b_K`. The complementary affine carry is

\[
D_0=0,\qquad D_{K+1}=3^{1-e_K}D_K+(1-e_K)2^K.
\]

The preceding [finite triadic certificate](../global-closure-20261123/duality/TRIADIC_RANK.md)
implies convergence if a supplied candidate `a/3^r` matches the actual
complementary prefix for at least

\[
H(n,a,r)=8\operatorname{bl}(n)+(9r+8)
  \operatorname{bl}(\max(1,|a|,3^r))+2
\]

steps. Here `bl(m)` is the least positive `L` with `m<2^L`. Constructing
such a candidate for every fixed positive input was the direct target.

The new stream uses the appropriate complementary standard-cycle state
at its terminal clock:

\[
\boxed{\eta_K=\frac{2^K(1+e_K)-D_K}{3^{b_K}}.}
\]

Every candidate has the correct complementary prefix through `K+1`
parity bits. If the actual orbit enters `1,2`, the stream becomes exactly
constant. Its increment is supported only on failures of alternation.
With the analogous original-coordinate approximation `xi_K`, every
such defect obeys

\[
(\xi_{K+1}-\xi_K)(\eta_{K+1}-\eta_K)
=-\left(\frac43\right)^{K+1}.
\]

The remaining denominator now has an exact interpretation. Pull the
terminal state backwards through the complementary prefix. Once a
positive power of three appears in the reduced denominator, no earlier
backward step cancels it. If the first failure of integrality is at
index `j`, the final reduced denominator exponent is exactly `b_(j+1)`.
The required cancellation therefore amounts to a sufficiently long
integral terminal suffix, together with control of the reduced numerator.

The attempt to force this from the original source's affine identity
returns an identity rather than a new valuation saving. The alternative
Subspace-Theorem calculation keeps all places and all denominators:
its product is `D_K |D_K+3^b_K alpha|_2`, where `alpha=Omega(n)`.
Even at `n=1`, this tends to one along the even clocks. It supplies no
negative power of height, and the required algebraicity of `alpha`
is itself unproved. These two hypotheses cannot be inferred by naming
the external theorem.

**Open closing inequality:** after reducing `eta_K=a_K/3^r_K`, prove
that some actual clock satisfies `H(n,a_K,r_K)<=K`, or construct a
different witness with the same finite guarantee. The packet does not
establish this inequality.

A final [failure-position calculation](arithmetic/FAILURE_POSITION_RESETS.md)
tests a possible descent directly. Every even-even transition resets
the candidate to its full denominator; an odd-odd transition also
destroys existing cancellation unless it starts from the full-denominator
case. The actual source `3` rules out monotone decrease of the backward
failure position. Complete denominator cancellation at selected clocks
of source `27` still leaves an oversized numerator horizon. These finite
controls leave favorable later clocks possible and sharpen the need for
a coupled saving. In particular, the horizon condition requires
`r_K < sqrt(K/(9 log_2(3)))`, together with the numerator bound.

## 2. Exact source comparison and whole-mass profile escape

Under the pinned actual-component hypotheses, let `q_j` be one escaping
ordinary odd-unit orbit, `v_j=nu(q_j)` increase to `C`, and `K` be the
legal inverse kernel. For

\[
\eta_N=\frac1N\sum_{j<N}\delta_{q_j},\qquad
\zeta_{N,r}=\frac1N\sum_{j<N}K^r(q_{j+r},\cdot),
\]

the new calculation gives

\[
\boxed{\|\zeta_{N,r}-\eta_N\|_{\rm TV}
 =\frac1N\sum_{j<N}\left(1-\frac{v_j}{v_{j+r}}\right),}
\qquad
\sup_r\|\zeta_{N,r}-\eta_N\|_{\rm TV}
 =\frac{\mathbb E\min(\tau,N)}N\longrightarrow0.
\]

Here `tau` is the actual whole-path coalescence clock. The supremum is
over finite inverse depths; the same error controls arbitrary
deterministic clocks chosen separately for each original time label.
In particular, PR180's trace bound `F(q_j)>=c q_j` implies

\[
\boxed{\inf_r\zeta_{N,r}\{F>B_N\}\longrightarrow1
\quad\text{for every nonnegative }B_N=o(N).}
\]

This strengthens the positive retained high-profile fraction to
asymptotically the entire measure. A fixed low-profile estimate controls
a vanishing portion of this actual target law.

The sharp elementary comparison used here is

\[
\left|\sqrt{\operatorname{Col}_Q(P)}-
       \sqrt{\operatorname{Col}_Q(P')}\right|
\le\sqrt2\,\|P-P'\|_{\rm TV}.
\]

At the ordinary-diagonal-compatible scale `Q` comparable to
`N^(1/theta)`, a sufficient negligible source error is
`E min(tau,N)=o(sqrt(N))`. A fixed absolutely continuous tilt on the
same hypothetical ordinary path space preserves the enumerated flow,
path, and new boundary-dimension properties while making this error
as slow as `1/log(N)`, or a prescribed slower tail. Thus a rate proof
for the distinguished canonical law must use a property not preserved
by that tilt. No actual-source collision upper is proved here.

## 3. Compressing cycle edges to a fixed-arity unit equation

An actual odd edge satisfies `(-3n_i)+(2^a_i n_(i+1))=1`. If the
multiplicative rank generated by the actual odd states of a primitive
cycle is `t`, the source-qualified Beukers--Schlickewei bound gives

\[
\boxed{p\le2^{16t+24}.}
\]

The same encoding forces unbounded multiplicative rank along every
infinite nonperiodic ordinary orbit. No upper bound on that rank is
proved, so this is not unrestricted cycle exclusion.

The stronger attempt uses the small-height-neighborhood theorem of
Evertse--Schlickewei--Schmidt with the fixed divisible group generated
by two and three. For every ordinary `n>=2` prime to six and every
factorization `(-3n,3n+1)=gamma eta` in that setup, the note proves

\[
\frac{h(\eta)}{1+h(\gamma)}
\ge\frac{\log n}{1+\log(3n+1)+2\log n}>\frac18.
\]

This exceeds the theorem's allowed error by a wide margin. The proof
retains finite-place contributions even in the full algebraic divisible
closure. A small real correction is not a small arithmetic height.
The obstruction is to this proposed application, not to Collatz cycles.

## 4. Ordinary carries and a concrete real/2-adic control

The q-analog attempt keeps the ordinary binary carry polynomial `R_n`.
For the parity-preserving conjugacy `h_q` to Monks' map with multiplier
`1+q`, and the binary digit polynomial `P_n`, it obtains

\[
h_q(n)+P_n
=\sum_{j:e_j=1}\frac{q^{j+1}}{(1+q)^{p_{j+1}}}R_{T^j(n)}(q).
\]

The sum exists q-adically, but no finite family of coefficient sections,
rationality, or required polynomiality has been proved. Christol's
finite-automaton hypothesis cannot be replaced by computability.

Testing a proposed real-to-2-adic shortcut produced a concrete control.
Start `z_0=3/2` and select `z/2` for `z>=2`, and `(3z-1)/2` for `z<2`.
The resulting forced word is aperiodic, has odd lower density at least
`log(2)/log(5/2)`, and its real Bernstein series equals `-3/2`.
The same series has a 2-adic limit in `Z_2`, so the limits differ.
Prepending one digit gives real value `-4/3`, again unequal to the
2-adic limit, this time with an odd reduced denominator.

This explicitly refutes the intermediate even-denominator assertion in
López--Stoll, arXiv:2101.12747v1, Section 2, and prevents importing the
corresponding transfer. It does not show that their final Theorem 1 is
false, decide the rationality of the constructed 2-adic limit, or supply
a positive ordinary Collatz counterexample.

## Evidence and source boundary

| Lane | New formal scope | Other evidence |
| --- | --- | --- |
| Arithmetic | 10 finite recurrence and numerator theorems | Independent written review; exact full Subspace product |
| Dynamics | No new Lean theorem | Independent written review from pinned, source-qualified actual-path hypotheses |
| Cycles | No new Lean theorem | Independent height/rank review; primary external theorem statements |
| Carries and transfer | 8 finite recurrence theorems | Independent carry-series, limits, aperiodicity, and primary-source review |

All eighteen new authored theorem declarations were explicitly audited.
Only `propext`, `Classical.choice`, and `Quot.sound` occur; no `sorryAx`
or new closure axiom occurs. The two module pairs were compiled both
by their authors and independently, with `autoImplicit=false` and
warnings as errors, using Lean 4.34.1 and the pinned mathlib runtime.
These finite checks do not formalize the entire written packet.

The [reports directory](../../reports/2026-11-23-profound-step/README.md)
records exact source heads, review targets, compiler output, and the
file manifest. This pass refreshed the latest thirty open PR records,
the owned branch and `main`, and read the selected changed source files.
The previous broad repository inventory is retained; the old proof
corpus was not replayed. The required clean-checkout integrity gate is
reported on the publication PR separately from mathematical evidence.
