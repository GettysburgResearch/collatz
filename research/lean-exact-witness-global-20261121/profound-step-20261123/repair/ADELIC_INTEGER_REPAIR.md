# Fixed-sibling integer repair and its exact adelic cost

23 November 2026. **PROVED finite identities and a written obstruction to
one specified Subspace-Theorem application. The unrestricted integer repair,
the residue-512 implication, and Collatz remain OPEN.**

The preceding checkpoint found real-bounded rational sources whose original
inverse word ends at the fixed sibling `64q_j+21`. This note pursues the
arithmetic operation that would turn them into small ordinary integer
ancestors. The main new calculation retains every place: the tempting
canonical approximants have a Subspace product bounded **below** by `7/3`.
The result covers every upper sibling power, not only the first one.
It does not exclude other rational approximants or unrestricted word edits.

Signed periodic extrapolation can cancel a real tail. Its exact new error
is the same integral block displacement used by the companion arithmetic
lane, so it supplies a connection between the Diophantine and lattice
routes, rather than a second independent closing argument.

## 1. The unchanged ordinary source and its rational pullbacks

Use the positive odd map

\[
3q_i+1=2^{a_i}q_{i+1},\qquad a_i\ge1,
\quad A_0=0,\quad A_j=\sum_{i<j}a_i,
\]

where every `q_i` is positive, odd, and not divisible by three. Put

\[
z_j=\frac{2^{A_j}}{3^j},\qquad
D_j=\frac13\sum_{i<j}z_i=z_jq_j-q_0.
\tag{AR1}
\]

The identity is the complete ordinary carry identity, divided by `3^j`.
For `b>=1`, set

\[
h_b=\frac{64^b-1}{3},\qquad
S^b(q)=64^bq+h_b.
\]

Apply the **same complete inverse word** of length `j` to `S^b(q_j)`.
Its rational source is

\[
\begin{aligned}
y_j^{(b)}
 &=64^bq_0+3h_bD_j+h_bz_j\\
 &=q_0+h_bz_j(3q_j+1)\\
 &=q_0+h_b\frac{2^{A_{j+1}}q_{j+1}}{3^j}.
\end{aligned}
\tag{AR2}
\]

In particular the physical target is fixed at `S^b(q_j)`; no nearby root
or changed source projection is substituted. The inverse calculation is
rational. Its denominators are precisely the obstacle to ordinary legality.

Subtracting the formulas at consecutive indices gives the especially
simple identity

\[
\boxed{y_{j+1}^{(b)}-y_j^{(b)}=h_bz_{j+1}>0.}
\tag{AR3}
\]

This is true on every finite ordinary unit-odd segment, including segments
of convergent trajectories. It requires no hypothetical escaping example.

On an injective escaping ray, the inherited ordinary reciprocal bound
makes `sum z_i` finite. Consequently these rational sources increase to

\[
L_b=64^bq_0+3h_bD_\infty.
\tag{AR4}
\]

The same series converges in the 2-adic metric to `D_infty=-q_0`.
Thus `y_j^(b)` converges 2-adically to `q_0`, while its real limit is
strictly larger. This two-place statement does not identify the limits.

The root lane's ordinary companion is `d(q_0)=D_infty` in the **real**
metric. With its pressure weight `r(q_0)=1/(q_0+d(q_0))`, the first-sibling
limit is `L_1=q_0+63/r(q_0)=64q_0+63d(q_0)`. These are the same objects.

## 2. Primitive denominator and exact binary precision

Let

\[
\nu_b=v_3(h_b)=1+v_3(b),\qquad c_b=h_b/3^{\nu_b}.
\tag{AR5}
\]

Here `c_b` is positive, odd, and not divisible by three. The valuation
formula follows by the binomial/LTE identity
`v_3(64^b-1)=2+v_3(b)`; it is also the source of the preceding checkpoint's
unaltered-word integrality criterion.

For `j>nu_b`, write

\[
Q_j=3^{j-\nu_b},\qquad
P_j=Q_jq_0+c_b2^{A_{j+1}}q_{j+1}.
\tag{AR6}
\]

Then `y_j^(b)=P_j/Q_j`, with `gcd(P_j,Q_j)=1`, since the second summand
in `P_j` is a ternary unit. Therefore the reduced denominator is exactly
`3^(j-nu_b)`, and

\[
\boxed{
|P_j-q_0Q_j|_2=2^{-A_{j+1}},\quad
|P_j|_3=1,\quad |Q_j|_3=3^{-(j-\nu_b)}.
}
\tag{AR7}
\]

The binary precision is an equality, not merely a lower estimate. It
uses the oddness of `c_b q_(j+1)` and retains the complete next odd gap.

For the first sibling, `h_1=21`, `nu_1=1`, and `c_1=7`. In particular,
every `j>=2` gives a nonintegral source of reduced denominator `3^(j-1)`.

## 3. Test the Subspace Theorem at its actual inequality

The primary literature selected here is Adamczewski--Bugeaud,
*On the complexity of algebraic numbers I. Expansions in integer bases*,
[arXiv:math/0511674v1](https://arxiv.org/pdf/math/0511674), Section 4,
Theorem E, pp. 7--8. Their stated number-field Subspace Theorem includes
independent forms at the finite places and the precise height-normalized
product inequality. The same section constructs approximants by periodic
completion; that construction motivates Section 4 below.

Suppose provisionally that the real limit `L_b` is algebraic. This
supposition does not follow from the integer source. Use the forms

| Place | Two independent forms |
|---|---|
| infinity | `X-L_b Y`, `Y` |
| 2 | `X-q_0 Y`, `Y` |
| 3 | `X`, `Y` |

At the primitive pair `(P_j,Q_j)`, their unnormalized product is exactly

\[
\begin{aligned}
\Pi_j^{(b)}
 &=\prod_{v\in\{\infty,2,3\}}
       |L_{1,v}(P_j,Q_j)L_{2,v}(P_j,Q_j)|_v\\
 &=Q_j\,(L_b-y_j^{(b)})\,2^{-A_{j+1}}.
\end{aligned}
\tag{AR8}
\]

For primitive integer pairs, the height-normalized theorem would require
this quantity to decay as a negative fixed power of their height. But
AR3 retains the first omitted **positive** term, giving

\[
L_b-y_j^{(b)}
 =h_b\sum_{i\ge j+1}z_i
 \ge h_b\frac{2^{A_{j+1}}}{3^{j+1}}.
\]

Hence

\[
\boxed{\Pi_j^{(b)}\ge \frac{c_b}{3}\ge\frac73.}
\tag{AR9}
\]

For the last inequality, `64^b-1>=63b` and `3^v_3(b)<=b` imply
`c_b=(64^b-1)/(9*3^v_3(b))>=7`.

This is an exact obstruction to **these forms on these approximants**.
Their apparent simultaneous real and 2-adic convergence does not meet the
deep theorem's hypothesis, even if real algebraicity were supplied.
Adding the 3-adic denominator to the product has already been paid for
in AR8. The conclusion also holds with any finite `y_J^(b)`, `J>=j+1`,
in place of `L_b`; this gives an exact finite implementation control.

No transcendence or algebraicity claim about `L_b` follows from AR9.
Nor does it prove that all possible Subspace-Theorem applications fail.

## 4. Signed block extrapolation: a concrete attempt to beat the product

Use the simpler partial sum `D_j` of AR1. Let a supplied actual block
starting at `q_j` contain `r>=1` odd steps, total gap `a`, and full carry
`C`. Set

\[
P=3^r,\quad Q=2^a,\quad
Pq_j+C=Qq_{j+r},\quad \rho=Q/P,\quad c=C/P.
\]

Then

\[
D_{j+r}=D_j+z_jc.
\tag{AR10}
\]

When `Q<P`, periodic repetition of that block is a convergent real
geometric series for the inverse sum. Its exact extrapolant is

\[
H_j=D_j+\frac{z_jc}{1-\rho}
    =D_j+\frac{z_jC}{P-Q}.
\tag{AR11}
\]

It exactly sums the periodic model's geometric tail by a signed affine
combination of the partial sums. Its error against the actual nonperiodic
real limit is not bounded here. The complete error to the rational 2-adic value is

\[
\boxed{
H_j+q_0
 =z_j\frac{(Q-P)q_j-C}{Q-P}.
}
\tag{AR12}
\]

Thus the numerator is precisely the integral affine displacement

\[
\Delta_w(q_j)=(Q-P)q_j-C=Q(q_j-q_{j+r}).
\tag{AR13}
\]

If the block is actually repeated `k` times, the exact block relations
`Q Delta_w(q_(j+(ell+1)r))=P Delta_w(q_(j+ell*r))`, for `0<=ell<k`,
force `Q^k | Delta_w(q_j)`.
That is the earlier integer precision mechanism and the companion
arithmetic lane's displacement rank. The denominator `Q-P` is odd and
a ternary unit, so it contributes no hidden binary or ternary gain.

This signed operation can improve the simultaneous approximation on
repeating blocks. It does **not** make the extrapolant a positive integer
ancestor of the same sibling. Neither the existence of enough suitable
actual repeats nor an unrestricted nonperiodic cancellation mechanism
has been established. The integer source's computability is not a bound
on factor complexity or a periodic-completion hypothesis.

## 5. Other literature interfaces and the actual missing operation

Krasikov--Lagarias, [*Bounds for the 3x+1 Problem using Difference
Inequalities*](https://arxiv.org/abs/math/0205002), gives predecessor-count
lower bounds. Monks--Monks--Monks--Monks,
[*Strongly sufficient sets and the distribution of arithmetic sequences
in the 3x+1 graph*](https://arxiv.org/pdf/1204.3904v2), studies back tracing
into arithmetic progressions and sufficient sets. Those facts concern
available ancestors or orbit intersections; they do not by themselves
give the `O(j^d)` same-sibling source-height bound needed here. No such
height-uniform theorem was imported from their statements.

The sought repair remains: for one fixed hypothetical escaping source,
construct an actual positive integer `n_j` whose trajectory visits the
unchanged root `64q_j+21`, with `n_j=O((j+1)^d)` for some `d<800/799`,
or provide an equally strong actual-law mass comparison. Its contradiction
with the previous sparse-minimum theorem is already proved.

The present calculations identify what a useful construction must change:
it must alter the complete inverse word or obtain a new controlled signed
cancellation. Keeping the canonical truncation, merely choosing a farther
upper sibling, or treating a rational extrapolant as an ordinary source
does not perform that operation.

The finite control `75 -> 113 -> 85` is deliberately retained: the root
`85=S(1)` has an ordinary ancestor although the canonical pullbacks from
longer prefixes have nontrivial ternary denominators. AR9 is not a
nonexistence theorem for integer repairs.

## 6. Formal and computational boundaries

`AdelicRepair.lean` proves the cleared pullback identity, next-edge
identity, numerator recurrence, primitive-numerator algebra, signed
extrapolation identity, and its actual endpoint displacement. The
Subspace Theorem is not added as an axiom. The infinite convergence,
valuation calculation, primitive reduction, and AR9 are written scope.

`check_adelic_repair.py` uses exact fractions and literal finite forward
paths. It checks the primitive denominator, exact binary precision,
finite product lower bound, block extrapolation, and a genuinely ordinary
alternative repair, together with rejected damaged identities. Its
convergent examples are controls for finite formulas, not experiments
claiming to observe an escaping orbit.
