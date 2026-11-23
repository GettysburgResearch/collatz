# The closing step: common displacement and ordinary free energy

23 November 2026. **Written coordinating deductions. Full Collatz and the
residue-512 implication remain OPEN.** This note connects the three new
attacks without replacing their missing hypotheses by one another.

The previous checkpoint is PR177 at
`92e7aaf602a0d4f0442556a133ae8e882e1fe93f`. Its sparse-basin and complete
inverse-kernel theorems concern one unchanged hypothetical escaping
ordinary component. The present arithmetic identities also hold for the
displayed finite actual traces, without an escaping-orbit assumption.

## 1. Periodic extrapolation measures the exact integer displacement

Let `q_j` be a positive odd orbit, let `a_(j+1)>=1` be its exact odd
valuation, and put

\[
A_j=\sum_{i=1}^j a_i,\qquad z_j=2^{A_j}/3^j,\qquad
D_j=\frac13\sum_{i=0}^{j-1}z_i.
\]

The actual affine identity is

\[
z_jq_j=q_0+D_j. \tag{CF1}
\]

For a block of `r>=1` odd steps with complete affine data

\[
F_w(x)=\frac{Px+C}{Q},\qquad P=3^r,\quad Q=2^a,
\]

write `rho=Q/P`. Its actual contribution to the partial sum is

\[
z_{j+r}=\rho z_j,\qquad
D_{j+r}=D_j+z_j C/P. \tag{CF2}
\]

Since `P` and `Q` are positive powers of different primes, `P!=Q`.
Define the rational periodic extrapolant

\[
H_j=D_j+\frac{z_j C}{P-Q}.
\]

If `rho<1`, the second summand is the real sum of the geometric tail
obtained by repeating this block forever. For `rho>1` the same expression
is still a rational periodic-completion candidate; it is not a convergent
real-tail sum.

Substituting CF1 gives the exact identity

\[
\boxed{
H_j+q_0
=z_j\left(q_j-\frac{C}{Q-P}\right)
=\frac{z_j}{Q-P}\bigl((Q-P)q_j-C\bigr).
} \tag{CF3}
\]

Consequently, when the displacement is nonzero,

\[
\boxed{
v_2(H_j+q_0)
=A_j+v_2\bigl((Q-P)q_j-C\bigr).
} \tag{CF4}
\]

Here `Q-P` is odd and the denominator `3^j` is a 2-adic unit.
If the actual block repeats `k` times, the source-lattice theorem gives

\[
Q^k\mid (Q-P)q_j-C.
\]

Thus the extra binary precision of the periodic extrapolant is exactly
the lattice used by the adaptive ordinary descent proof. It is not an
independent source of precision obtained by dropping the carry. The
zero-displacement case is processed before taking a valuation: then
`H_j=-q_0` and `q_j=C/(Q-P)` is an actual positive integer fixed point
of the legal block.

The adaptive theorem permits a different reduced rational fixed point
`c_j/d_j` at each macro, but charges the entire change of center. Its
single integer rank is `|d_j x_j-c_j|`. The cross-carry term in that
theorem is the exact cost of changing the extrapolant's center. A Padé
argument and a changing-center rank therefore cannot each treat the
other one's center change as free.

These statements connect
[adaptive ordinary descent](arithmetic/ADAPTIVE_LATTICE_DESCENT.md) to the
repair lane's rational-shadow calculations. Universal word coverage and
a same-sibling integer repair are still separate unproved assertions.

## 2. A finite trial law is an actual finite set of ordinary ancestors

Retain the escaping-component weight

\[
r(n)=\frac{\Lambda_\infty(n)}n,\qquad
A_s(q)=\sum_{n\in\operatorname{Pred}_U(q)}r(n)^s,
\qquad s>1.
\]

Put `q'=Sq=64q+21`, and let `Phi` be the complete balanced inverse-tree
bijection. It maps every actual unit ancestor `n` of `q` to one actual
unit ancestor `n'=Phi(n)` of **the same fixed sibling** `q'`. If its
signed exponent cost is `Delta(n)`, the exact weight relation is

\[
r(\Phi(n))^s=64^{-s}2^{-s\Delta(n)}r(n)^s. \tag{CF5}
\]

Use the unchanged ordinary terminal law

\[
\nu_q(n)=r(n)^s/A_s(q),\qquad V(n)=s\log(2)\Delta(n).
\]

The [entrance-law theorem](pressure/ORDINARY_ENTRANCE_LAW.md) proves

\[
-\log R_s(q)
=\inf_{\sigma\text{ finite support}}
\left\{\mathbb E_\sigma V+
\operatorname{KL}(\sigma\Vert\nu_q)\right\},
\quad R_s(q)=\frac{Z_s(Sq)}{Z_s(q)}.
\tag{CF6}
\]

Every trial distribution in this infimum is supported on actual ordinary
ancestors. The exact weights still contain infinite products and
normalizers; the finite upper certification below avoids evaluating them.
The variational identity alone is not an upper estimate for its infimum.

For a nonempty finite set `F` of such ancestors, put

\[
B_F=\sum_{n\in F}r(\Phi(n))^s.
\]

Then the exact optimum over trials supported on `F` is

\[
\boxed{
\inf_{\operatorname{supp}\sigma\subseteq F}
\left\{\mathbb E_\sigma V+
\operatorname{KL}(\sigma\Vert\nu_q)\right\}
=\log A_s(q)-s\log64-\log B_F.
} \tag{CF7}
\]

**Proof.** For `n in F`, CF5 gives

\[
e^{-V(n)}\nu_q(n)
=64^s r(\Phi(n))^s/A_s(q).
\]

Normalize these positive weights on `F` to obtain
`tau_F(n)=r(Phi(n))^s/B_F`. Expanding the finite relative entropy gives

\[
\mathbb E_\sigma V+\operatorname{KL}(\sigma\Vert\nu_q)
=\operatorname{KL}(\sigma\Vert\tau_F)
  +\log A_s(q)-s\log64-\log B_F.
\]

Relative entropy is nonnegative, with equality at `sigma=tau_F`.
This proves CF7.

For a genuinely finite upper certificate, the proved ordinary bounds give
`A_s(q)<=zeta(s)<=s/(s-1)` and `r(n')>=c_*/n'`, where
`c_*=exp(-160/3)`. Therefore

\[
\boxed{
\inf_{\operatorname{supp}\sigma\subseteq F}
\left\{\mathbb E_\sigma V+
\operatorname{KL}(\sigma\Vert\nu_q)\right\}
\le \log\frac{s}{s-1}-s\log(64c_*)
     -\log\sum_{n\in F}\Phi(n)^{-s}.
} \tag{CF7-F}
\]

The displayed right side uses the finite list of transported ordinary
integers and universal constants. Their ancestor paths can be checked
exactly; no infinite `r`, `Z_s` or normalized probability has to be
evaluated to certify this upper bound. Its usefulness for the desired
scale still depends on constructing a sufficiently large finite inverse
power sum at the unchanged sibling.

There is also an explicit trial attaining this upper certificate. Put
`W_F=sum_(n in F) Phi(n)^(-s)` and
`sigma_F(n)=Phi(n)^(-s)/W_F` on `F`. For any finite trial, CF5 rewrites
its objective as

\[
\log A_s(q)-s\log64
+\sum_{n\in F}\sigma(n)
 \log\frac{\sigma(n)}{r(\Phi(n))^s}.
\]

Substitute `r(Phi(n))>=c_*/Phi(n)` and the displayed `sigma_F`.
Every logarithm left in the finite sum is `-log W_F-s log c_*`,
which proves the CF7-F bound for this specific trial. Thus the
certificate need not choose the unknown exact tilted probabilities.

In particular a one-point trial has exactly

\[
V(n)-\log\nu_q(n)
=\log A_s(q)-s\log64-s\log r(\Phi(n)). \tag{CF8}
\]

The atomic trial is therefore precisely a controlled actual-ancestor
construction. A many-point trial can gain entropy by collecting many
actual transported sources; it must pay their full height-dependent
weights. This explains exactly how a predecessor-growth theorem would
have to enter the closing argument.

## 3. What an absolute free-energy estimate would finish

Along the unchanged escaping ray let `q=q_j`. The preceding checkpoint
proves `sum_j R_s(q_j)^(1/s)<infinity`. If finite ordinary trials could
be constructed, for every `j` in a set `I`, with `g(j)>0` and

\[
\mathbb E_{\sigma_j}V_j+
\operatorname{KL}(\sigma_j\Vert\nu_{q_j})
\le C+s\log g(j),\qquad
\sum_{j\in I}\frac1{g(j)}=\infty,
\tag{CF9}
\]

then CF6 would give
`R_s(q_j)^(1/s)>=exp(-C/s)/g(j)`, a contradiction. The desired
construction remains **OPEN**. The new variational formulation makes
both the candidate finite trial and its exact cost explicit; it does
not assert that the needed trials exist.

A useful normalization check is exact. Replace every cost `V` by `V+c`.
Its partition function is multiplied by `exp(-c)`, but its normalized
tilted terminal law is unchanged. Thus even identical normalized laws
(zero relative entropy, Hellinger affinity one) can coexist with
arbitrarily small partition functions. A continuity or coupling theorem
for normalized terminal laws must also provide an **absolute cost
calibration** before it can imply CF9. This is why finite Hellinger
length in the new entrance-law theorem is useful structure but is not
itself a lower Green comparison.

The actual balanced compiler has zero cost at the empty address, so the
constant-shift calculation is an abstract normalization test, not an
alternative actual compiler. The pressure manuscript also retains this
zero-cost anchor in an explicit probability control: its anchor has mass
`t^2`, its other weight is multiplied by `t`, and its partition function
is `t+t^2-t^3`. The normalized laws approach one another in total
variation with uniformly integrable densities even while this partition
function tends to zero. That control concerns those probabilistic
hypotheses only; it is not claimed to realize an escaping Collatz orbit.

## 4. Primary literature tested at these interfaces

### Green geometry and unbounded branches

Gouezel, *Martin boundary of random walks with unbounded jumps in
hyperbolic groups*, Annals of Probability 43 (2015), Theorem 1.2, gives
Ancona inequalities for an admissible measure on a nonelementary
hyperbolic group, with property `Anc*` and superexponential tails.
Theorem 1.1 shows that merely exponential tails can allow pathological
Martin boundaries even in that group setting.

Primary text inspected: introduction and Theorems 1.1--1.2,
<https://gouezel.pages.math.cnrs.fr/webpage/articles/infinite_ancona.pdf>.

Our inverse kernel is directed, includes killing, and has no reverse
reachability between arbitrary ancestors. Forgetting its direction does
not establish admissibility or the required Green comparison. For example,
the actual odd roots 5 and 341 have the same successor 1. The inverse
Green kernel has a positive diagonal term from 5 to 5, while its kernel
from 341 to 5 is zero: the forward orbit of 5 stays in `{5,1}`. Their
distance two in the undirected graph cannot produce a positive Harnack
comparison for these kernels. This exact reachability control does not
refute a separate inequality for the summed potentials `Z_s`.

The new killed terminal-law construction identifies the object on which
a boundary theorem would have to act, including its original endpoint,
phase and density. No Ancona theorem is imported as an unconditional
Collatz result.

### Predecessor growth and finite trial mass

Krasikov--Lagarias, *Bounds for the 3x+1 Problem using Difference
Inequalities*, Acta Arithmetica 109 (2003), prove a lower predecessor
count with exponent 0.84 for a fixed eligible target, beyond a
target-dependent threshold. The author-hosted primary text states this
scope explicitly:
<https://websites.umich.edu/lagarias/doc/krasikov.pdf>.

Such a count is relevant to `B_F` in CF7. It does not, by itself,
calibrate that mass uniformly as the target varies through `Sq_j`.
Furthermore the exact pressure pool here contains odd ternary-unit
ancestors; a theorem counting all shortcut predecessors needs its
projection and any lost multiplicity stated before it is used there.
We do not insert the general predecessor exponent into CF7 without
those steps. No newer source-qualified predecessor exponent is needed
for the new deductions in this packet.

### Multiplicative descent and ordinary paths

Applegate--Lagarias, *The 3x+1 Semigroup*, Theorem 1.1 and Section 2,
prove the global multiplicative-semigroup classification using a
multiplier-assisted descent. Primary text:
<https://arxiv.org/pdf/math/0411140v2>.

The classification supplies products of generators; the paper explicitly
allows products that are not a single ordinary orbit. The prior packet's
multiplier-transport theorem already rules out uniformly bounded merger
clocks for the wild prime multipliers. This pass does not present that
old result as new. An unbounded ordinary merger construction remains a
possible route, and must preserve actual source and endpoint legality.

### Subspace estimates and adaptive ranks

The repair lane computes the actual mixed-place product for the bounded
rational sibling leaves and for signed extrapolation. The arithmetic
lane proves a rank theorem using their complete displacement lattice.
CF3--CF4 identify their common variable. A useful deeper arithmetic
import would need to control that variable for arbitrary actual words,
or produce a new approximation with all required places and coefficient
fields checked. The current proof does not establish either universal
property.

## 5. Exact remaining work

The finite-source variational problem and the common integer displacement
are concrete objects on the original ordinary dynamics. Completing the
pressure route needs an absolute trial-cost estimate such as CF9;
completing the adaptive arithmetic route needs a legal selector of paid
macros for every remaining ordinary path. The signed extrapolants do not
already provide either selector. Full cycles outside the certified
languages and the unrestricted source-tuple construction for the original
residue-512 implication remain open.
