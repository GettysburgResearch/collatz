# Fixed-height forward power saving: exact target, partial theorems, and the remaining obstruction

> **Status: THEOREM DEVELOPMENT.** `MZ-FH-001`, `MZ-FH-002`, and `MZ-FH-003` below have complete elementary proofs in this note but remain pending independent repository review. The requested fixed-height power-saving theorem itself is **OPEN**. Collatz is not claimed proved.

## 1. Target

For odd `N`, let

\[
\operatorname{Syr}(N)=\frac{3N+1}{2^{\nu_2(3N+1)}}.
\]

For `H>=1`, `C>0`, and `X>=1`, put

\[
B_H(X;C)=
\#\left\{
N\le X:
N\text{ odd and }
\operatorname{Syr}^m(N)>H
\text{ for every }0\le m\le \lfloor C\log N\rfloor
\right\}.
\]

The desired theorem is

\[
B_H(X;C)=O_H(X^\beta)
\]

for one common `C>0` and one `beta<0.901` (or, in a longer two-sided program, any `beta<1` paired with inverse exponents tending to one).

The two imported Mazur papers do **not** prove this. The predecessor paper supplies the inverse exponent `0.901`. The natural-density paper supplies

\[
B_H(X;C_{\rm Syr})\le C_d X(\log H)^{-d}
\qquad(0<d<5/143),
\]

whose exponent in `X` is still one for fixed `H`.

## 2. `MZ-FH-001` — one-floor counterexample lower bound

### Statement

Assume the following inverse hypothesis for some `gamma>0`:

> for every positive `b` with `3` not dividing `b`, there is `c_b>0` such that
> \[
> \pi_b(X)\ge c_bX^\gamma
> \]
> eventually, where `pi_b` counts positive sources for the one-division Collatz map that eventually reach `b`.

If Collatz is false, then there is a constant `c>0` such that, for **every** fixed `C>0`,

\[
\boxed{
B_1(X;C)\ge
\frac{cX^\gamma}{1+\lfloor\log_2X\rfloor}
}
\]

eventually.

Consequently, an upper bound

\[
B_1(X;C)=O(X^\beta),\qquad \beta<\gamma,
\]

already proves Collatz. It is unnecessary to prove a separate estimate for every fixed `H`.

With the imported constant-factor predecessor theorem, `gamma=0.901`.

### Proof

Assume that some positive orbit does not reach `1`. Move forward until the orbit is odd and call that odd value `a`. Put

\[
b=\operatorname{Syr}(a).
\]

Then `b` is odd, it lies on the same nonconvergent orbit, and `3` does not divide `b`: the numerator `3a+1` is one modulo three, and division by a power of two preserves a nonzero residue modulo three.

For large `X`, at least `c_bX^\gamma` positive integers `n<=X` reach `b`. Write every such source uniquely as

\[
n=2^r m,\qquad m\text{ odd}.
\]

The odd core `m` also reaches `b`. A fixed odd `m<=X` has at most

\[
1+\lfloor\log_2X\rfloor
\]

dyadic multiples at most `X`. Hence at least

\[
\frac{c_bX^\gamma}{1+\lfloor\log_2X\rfloor}
\]

distinct odd cores at most `X` reach `b`.

None of these odd cores can reach `1`. If one did, its deterministic forward orbit would enter the `1,2` cycle; it could not also reach the nonconvergent point `b`. Thus its Syracuse orbit never equals `1`. Since every Syracuse iterate is a positive odd integer, every iterate is strictly greater than `1`. The core is therefore counted by `B_1(X;C)` for every finite clock. This proves the bound.

If `B_1(X;C)=O(X^\beta)` with `beta<gamma`, then

\[
X^{\gamma-\beta}/\log X\longrightarrow\infty
\]

contradicts the two bounds. `□`

### Monotonicity

For every `H>=1`,

\[
B_H(X;C)\le B_1(X;C).
\]

Thus `H=1` is the largest and decisive fixed-floor bad set. This is a sharper target than the earlier every-`H` bridge.

## 3. `MZ-FH-002` — an unconditional entropy saving for coefficient-supercritical prefixes

This theorem reaches a genuine endpoint power saving, but only for the resident Lane-A prefix condition. It does not cover arbitrary starts that stay above `1`.

Use the shortcut map

\[
T(n)=
\begin{cases}
n/2,&n\equiv0\pmod2,\\
(3n+1)/2,&n\equiv1\pmod2.
\end{cases}
\]

Let `v_i(n)` be the parity of `T^i(n)`, let

\[
q_j(n)=\sum_{i=0}^{j-1}v_i(n),
\qquad
\alpha=\frac{\log2}{\log3},
\]

and put `k=floor(log_2 X)`. Define

\[
A(X)=
\left\{
1\le n\le X:
3^{q_j(n)}\ge2^j
\text{ for every }1\le j\le k
\right\}.
\]

Let

\[
h_2(p)=-p\log_2p-(1-p)\log_2(1-p)
\]

be binary entropy and set

\[
\vartheta=h_2(\alpha)
=0.9499555271883306\ldots.
\]

### Statement

\[
\boxed{\#A(X)\le2X^\vartheta.}
\]

### Proof

Every binary word of length `k` is realized by exactly one residue class modulo `2^k`. Since

\[
2^k\le X<2^{k+1},
\]

each residue class modulo `2^k` has at most two representatives in `[1,X]`.

Membership in `A(X)` implies, at the final prefix,

\[
q_k(n)\ge\alpha k.
\]

Therefore

\[
\#A(X)
\le
2\sum_{q=\lceil\alpha k\rceil}^k {k\choose q}.
\]

For any `p>1/2`, put `z=p/(1-p)>1`. Then

\[
\sum_{q=\lceil pk\rceil}^k{k\choose q}
\le
z^{-pk}(1+z)^k
=
2^{kh_2(p)}.
\]

Taking `p=alpha` and using `2^k<=X` gives

\[
\#A(X)\le2^{1+k\vartheta}\le2X^\vartheta.
\]

`□`

### Exact limitation

The exponent is above `0.901`:

\[
0.9499555271\ldots>0.901.
\]

The unique `p_*>1/2` satisfying `h_2(p_*)=0.901` is

\[
p_*=0.6830805152\ldots,
\]

whereas coefficient supercriticality forces only

\[
\alpha=0.6309297535\ldots.
\]

A pure terminal-frequency argument would therefore need a uniform odd-frequency gain of about

\[
p_*-\alpha=0.0521507616\ldots.
\]

The proof deliberately discards the earlier-prefix restrictions. No exponential improvement from retaining them is proved here; obtaining one would require additional Archimedean/2-adic information rather than terminal Hamming weight alone.

## 4. Why the imported natural-density theorem does not iterate to the target

The source theorem contains two quantitatively different estimates:

1. a moving-scale scheduled no-hit estimate
   \[
   O(x^{-1/32000});
   \]
2. a natural-versus-harmonic passage transport estimate
   \[
   O((\log x)^{-d}),\qquad d<5/143.
   \]

The geometric trace sends a large source through decreasing moving scales and ends at a fixed floor. Near the final fixed scales, `x^{-1/32000}` is only a constant depending on the floor. The passage errors sum to a constant multiple of `(\log H)^{-d}`. Neither term becomes `X^{-\delta}` when `H` is fixed.

There is also an invariance obstruction to obtaining contraction from total-variation transport alone. Let `E` be the set of odd starts that never reach `1`. On every successful first passage,

\[
N\in E
\quad\Longleftrightarrow\quad
\operatorname{Pass}_x(N)\in E.
\]

The no-hit sentinel is `1`, which is outside `E`. Thus successful passage preserves membership in `E`; any loss is confined to the scheduled no-hit and comparison errors. The present bounds do not turn that loss into a fixed-floor endpoint power. A power saving needs a new estimate on endpoint fibers, survivor-conditioned arithmetic, or another mechanism that is not present in the current `L^1` comparison.

This is an audit of the displayed proof chain, not an impossibility theorem for refinements.

## 5. A quantitative barrier in the existing `*`-density pullback iteration

In Inselmann's natural-density trajectory framework, one scale pullback has a density-exponent loss bounded above by

\[
D\longmapsto \rho D,
\qquad
\rho=\frac12\log_2 3
=0.792481250360578\ldots,
\]

up to additional strict losses. The scale exponent is iterated as

\[
X\longmapsto X^q
\]

with `q>rho`.

To reach a fixed scale requires

\[
r\sim\frac{\log\log X}{|\log q|}.
\]

The surviving density exponent is at most `D_0 rho^r`, and hence

\[
D_0\rho^r\log X
=
D_0(\log X)^{
1-|\log\rho|/|\log q|
}.
\]

Because `q>rho`, the displayed exponent is negative and this quantity tends to zero. Therefore literal iteration of those quantitative exponent-transfer lemmas down to a fixed floor does not yield `X^{-D}` for any fixed `D>0`.

Again, this is a bookkeeping boundary for the displayed iteration. A survivor-specific correlation gain could alter the recurrence.

## 6. `MZ-FH-003` — a killed-pullback criterion that would prove power saving

The following elementary lemma isolates the exact kind of new estimate required.

### Statement

Let `B(X)` be nondecreasing. Suppose there are constants

\[
0<\rho<1,\quad
\delta_0>0,\quad
\delta>0,\quad
A\ge1
\]

such that, for all sufficiently large `X`,

\[
\boxed{
B(X)
\le
A X^{1-\delta_0}
+
A X^{1-\rho-\delta}B(X^\rho).
}
\tag{KP}
\]

If `beta` satisfies

\[
\beta>1-\delta_0
\]

and

\[
\delta>(1-\rho)(1-\beta),
\]

then

\[
\boxed{B(X)=O(X^\beta).}
\]

### Proof

Put

\[
\eta_0=\beta-(1-\delta_0)>0,
\qquad
\eta_1=\delta-(1-\rho)(1-\beta)>0.
\]

If inductively `B(Y)<=K Y^beta` for smaller arguments, then `(KP)` gives

\[
B(X)
\le
A X^{\beta-\eta_0}
+
AK X^{\beta-\eta_1}.
\]

For sufficiently large `X`, the first term is at most `(K/2)X^beta` after increasing `K` to cover the finite initial range, and the second is at most `(K/2)X^beta`. Strong induction over integer endpoints proves the claim. `□`

### Numerical target at the random-walk scale

At

\[
\rho=\frac12\log_2 3,
\qquad
\beta=0.901,
\]

the survivor-fiber gain required by the second condition is

\[
(1-\rho)(1-\beta)
=
0.0205443562143027\ldots.
\]

The first condition simultaneously requires a one-block exceptional exponent

\[
\delta_0>0.099.
\]

The current moving-scale no-hit exponent `1/32000=0.00003125` is far below that direct-crossing target. For merely *some* power saving, a much smaller pair of gains would suffice, but neither survivor-conditioned gain is presently proved.

### Interpretation

The factor `X^(1-rho)` is the average compression multiplicity when `X` sources are sent to a range of size `X^rho`. The extra `X^(-delta)` in `(KP)` is a **bad-set-specific fiber saving**. It cannot be replaced by ambient first-passage typicality, because a hypothetical nonconvergent component is forward and backward invariant.

## 7. Smallest credible next theorem

The shortest remaining target is now:

> For the single invariant floor `H=1`, prove a killed-pullback inequality of the form `(KP)` with parameters crossing `beta=0.901`, or prove an equivalent transfer-operator/spectral estimate.

A proof must include all of the following:

1. one ordinary counting endpoint, not only harmonic mass;
2. conditioning on the actual survivor set or a rigorously larger set;
3. a scale-uniform endpoint-fiber or correlation saving;
4. error terms whose exponents do not collapse over `O(log log X)` scale reductions;
5. exact treatment of the `1,2` cycle and the Syracuse/raw normalization.

Plausible implementations are:

- an augmented residue/height transfer operator with a certified spectral radius;
- a density-increment dichotomy showing that saturation forces finite-state or periodic structure, then invoking the complete-denominator firewall;
- a cylinder-conditioned passage theorem whose distortion is paid by a strict survivor-mass loss;
- a joint forward/inverse linear program whose dual certificate directly proves `gamma>beta`.

## 8. Evidence and review boundary

The accompanying `check_fixed_height.py` recomputes the numerical constants, checks the entropy-tail inequality for a finite regression range, and verifies the exponent arithmetic in `(KP)`. It is not proof evidence for the symbolic theorems.

The source-qualified inputs are:

- Mazur's `0.901` predecessor theorem;
- Mazur's natural-density/logarithmic-time fixed-target and transport statements;
- the stated exponent-transfer lemmas from Inselmann's arXiv v3 paper.

The elementary proofs `MZ-FH-001` through `MZ-FH-003` are new local deductions and require independent review before promotion. The full fixed-height power saving remains open.
