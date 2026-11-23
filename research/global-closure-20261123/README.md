# Global closure: triadic rank, actual collisions, and full cycle denominators

**23 November 2026. Full Collatz remains OPEN.** This checkpoint pursues the
closing implications themselves. Its strongest positive result is a complete
well-founded termination argument for a supplied triadic parity dual of one
positive ordinary source, together with an explicit finite arithmetic
certificate. The universal construction of those certificates is still open.

This continues PR178 from
[2169884b64871b448cda16c7d74a0d5914ed870b](https://github.com/GettysburgResearch/collatz/commit/2169884b64871b448cda16c7d74a0d5914ed870b).
The preceding [high-variance packet](../high-variance-20261123/README.md)
is preserved.

## Step back across the repository

The refresh retrieved metadata and bodies for all **145 PR records**, including
122 open PRs. Main was at
ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a.
The [snapshot](SOURCE_SNAPSHOT.json) freezes every head and distinguishes
that inventory from proof review. Reading the relevant current proof files
does not amount to auditing all proofs in all branches.

PR176 advanced again during this work. The [late refresh](LATE_REFRESH.md)
pins its new head c82e3c1be894f655b40dcb61bf6d309a8f664e67 and records
the two additional pressure and band proof files read before publication.

Six peer branches had advanced since the previous checkpoint: PR175, PR176,
PR177, PR180, PR182 and PR185. The resulting choice of attacks was:

| Closing target | New source that changes the question | This checkpoint |
|---|---|---|
| One ordinary source reaches 1 | Previous PR178 rational-dual certificate; current PR177 complete source boundary and PR176/180 all-length source attempts | Construct a well-founded rank for **triadic** complementary trajectories, then seek their universal existence |
| Escape exclusion | PR185's square-root improvement in the critical collision lower bound; PR177's ordinary atomic pressure eigenmeasures | Derive an actual pressure off-diagonal upper and calculate the exact cost of transferring it to the required endpoint law |
| All nontrivial positive cycles | PR185's residual polynomial denominator growth; PR176's identity atom; PR175's invariant polynomial; PR182's rational controls | Test independent-base Mahler rigidity and retain the complete numerical denominator in an integral torus normalization |
| Global termination order | The older PR141 finite Hamming cores and source-persistent guarded orders | Attempt a nonlocal ordinal extension and identify why the direct single-carrier interpretation must be replaced |

Three agents pursued the first three rows in parallel; the coordinating
agent revisited the fourth. The proof files and reviews identify the
particular statements inspected, the dependencies retained and the
first unsupported inference. Verification focuses on the new proof files
and the required repository integrity gate.

## 1. A global terminating rank once a triadic dual is supplied

Read [TRIADIC_RANK.md](duality/TRIADIC_RANK.md) and the
[Lean source](duality/lean/TriadicDualClosure.lean).

For the shortcut map
\[
T(x)=
\begin{cases}
x/2,&x\equiv0\pmod2,\\
(3x+1)/2,&x\equiv1\pmod2,
\end{cases}
\]
pair the actual positive ordinary trajectory with a rational trajectory
whose parity is opposite at every step. Write the latter as \(w/3^r\),
with \(w\in\mathbb Z\), \(r\in\mathbb N\). Reduction to lowest terms
is unnecessary. Its exact updates are:

| Actual original state | Complementary numerator and exponent |
|---|---|
| \(x\) odd, so \(w\) even | \(x'=(3x+1)/2,\ w'=w/2,\ r'=r\) |
| \(x\) even and \(r>0\), so \(w\) odd | \(x'=x/2,\ w'=(w+3^{r-1})/2,\ r'=r-1\) |
| \(x\) even and \(r=0\), so \(w\) odd | \(x'=x/2,\ w'=(3w+1)/2,\ r'=0\) |

For nonzero \(w\) and \(x>1\), the lexicographic natural-number rank
\[
\boxed{\left(r,\;2x|w|+\mathbf1_{w=1}\right)}
\]
strictly decreases at every admissible step. Denominator reduction pays
for the second row. At fixed denominator, the product decreases, except
for the integral transition \(w=1\to2\), which is paid by the final
indicator. This handles negative as well as positive complementary
numerators.

An all-time positive ordinary pair cannot have zero numerator: that would
force an all-odd original tail, implying divisibility of one fixed
positive integer \(x+1\) by every power of two.

The resulting Lean theorem keeps a **single initial ordinary integer**,
a **single finite triadic candidate**, and the actual deterministic paired
updates. It proves that all-time opposite parity forces the original orbit
to reach 1. It assumes neither absence of nontrivial cycles nor an
unproved drift estimate.

### A finite arithmetic target for the construction

The written proof also supplies a finite certificate. For \(n>0\),
\(a\in\mathbb Z\), \(r\ge0\), set
\[
N=\operatorname{bitlength}(n),\quad
B=\max(1,|a|,3^r),\quad L=\operatorname{bitlength}(B),
\]
and
\[
\boxed{H=8N+(9r+8)L+2.}
\]

Let \(b_H\) be the number of even original steps in the actual
\(H\)-step prefix, and let \(D_H\) be its complementary affine carry,
with the exact recurrence given in the note. The sufficient condition is
\[
\boxed{2^H\mid 3^{b_H}a+3^rD_H.}
\]

This one endpoint congruence enforces the whole complementary parity
prefix. The explicit bound then forces the original orbit to reach 1.
The finite horizon and congruence theorem are written mathematics; the
formal inventory separately records which all-time closing and
trajectory-algebra statements are checked in Lean.

The remaining universal statement is precise: **for every positive \(n\),
construct some finite \(a,r\) satisfying this condition at their own
height-dependent horizon \(H\)**. Choosing a matching residue at an
arbitrary fixed precision does not prove that inequality-dependent
self-consistency. The direct carry construction was attempted and the
missing ordinary-height saving is exposed in the note.

In the language of the classical autoconjugacy \(\Omega\), this route seeks
\(\Omega(n)\in\mathbb Z[1/3]\) for every \(n>0\). The note credits the
Monks--Yazinski framework and distinguishes this stronger closing
condition from the previous rational-dual candidate decider.

## 2. The pressure estimate is real, and the law-transfer cost is explicit

Read [PRESSURE_COLLISION_ATTACK.md](escape/PRESSURE_COLLISION_ATTACK.md).

For the same hypothetical escaping ordinary component, PR177's pressure
measure has atom weights at most \(n^{-s}\), \(s>1\). The new elementary
off-diagonal estimate is
\[
\boxed{
\sum_{\substack{n\ne k\\n\equiv k\;(\mathrm{mod}\;Q)}}
\mu_s(\{n\})\mu_s(\{k\})
\le 2\zeta(s)^2Q^{-s}.
}
\]
The ordinary diagonal is retained separately; the full collision of this
atomic measure does not tend to zero.

The endpoint law needed by PR185 is
\[
\zeta_{M,r}
=\frac1{M+1}\sum_{j=0}^{M}K^r(q_{r+j},\cdot).
\]
It retains the actual atoms \(q_j\) with mass at least \(c_0/(M+1)\),
uniformly in the inverse clock. Consequently its density relative to
the normalized pressure measure has an unavoidable growing \(L^p\)
norm for every \(p>1\). Its relative entropy has lower growth
\((s-1)\log(M+1)\).

Probability normalization improves the direct transfer from a quadratic
to a linear density-norm cost. Even this sharper estimate, combined with
the actual maximum-height atom and PR185's fresh critical height bound,
cannot deliver the desired critical same-law collision upper. The failure
is uniform in the pressure exponent, including exponents approaching one. This
conclusion concerns that specific upper estimate, not the actual
off-diagonal collision and not every possible pressure argument.

The alternative route through repeated words also requires more
arithmetic. The Lean-checked source \(41\) contains different four-gap
words \((1,1,2,1)\) and \((1,1,1,3)\), both below the critical total-gap
budget, ending at \(425\) and \(911\), both \(20\bmod81\).
The previously established universal repeated-block divisibility theorem
is retained and checked in a self-contained specialization;
equal endpoint residues do not furnish its repeated-block premise.

The remaining target is a **nonuniform bilinear bound for the actual
endpoint law**, exploiting where its large densities occur in the
ordinary residue classes. No such bound is claimed.

## 3. Independent-base rigidity retains a full-denominator obstruction

Read the [cycle attempt](cycles/INTEGRAL_MAHLER_CLOSURE_ATTEMPT.md).

The natural dyadic lift of a finite positive cycle polynomial is a
nonzero finite combination of
\[
f(z^m)=\sum_{j\ge0}z^{m2^j},\qquad m\ \text{positive and odd}.
\]
The supplied elementary proof shows that every such nonzero combination
is nonrational. The primary Adamczewski--Bell theorem therefore implies
that this 2-Mahler series cannot also be 3-Mahler. This includes the known
cycle \(\{1,2\}\). The proposed independent-base equation is not available
for this auxiliary series.

A two-variable construction retains the additive carry instead. For a
complete word put
\[
C=\sum_i2^{d_i}3^{p-1-i},\quad D=2^A-3^p>0,\quad
g=\gcd(C,D).
\]
The exact torus map
\[
\Phi_w(x,y)=(x^{3^p},x^Cy^{2^A})
\]
diagonalizes through
\[
H_w(x,y)=(x,x^{C/g}y^{D/g}).
\]
The minimal degree of this triangular isogeny is exactly
\[
\boxed{D/\gcd(C,D),}
\]
the **full numerical reduced denominator**. Degree one is equivalent to
ordinary integer cycle closure. The available character identities occur
at every degree, so they do not exclude the degree-one case.

This uses all words and all denominator factors. It adds no fixed-prime
census and claims no new integer-cycle exclusion. PR175's earlier
dyadic elimination is explicitly credited rather than counted again.

## 4. Global-order attempt and mathematical status

[ORDER_CONSTRUCTION_ATTEMPT.md](ORDER_CONSTRUCTION_ATTEMPT.md) records the
attempt to go beyond PR141's guarded orders with ordinal machinery.
Its narrow two-rule obstruction explains why simply choosing a larger
ordinal in a direct strictly monotone single-carrier interpretation
cannot work. It does not exclude the paired arithmetic rank above,
relative termination methods, or other encodings.

The new work has three distinct evidence levels:

- The actual triadic paired-trajectory closing theorem and the finite
  pressure/repetition core are checked in Lean.
- The finite triadic certificate, pressure-measure estimates and torus
  normalization are written proofs, with scoped internal reconstruction
  reviews.
- The Mahler consequence imports an explicitly stated primary theorem.
  No external analytic claim has been installed as a Lean axiom.

The [execution and review record](../../reports/2026-11-23-global-closure/README.md)
contains the exact formal inventory, source hashes, commands and review
boundaries. The clean-checkout repository gate is recorded separately
from mathematical verification.

**First unsupported global steps:** construct the triadic certificate
for every positive source, establish the actual same-law collision upper,
or exclude degree one for every nontrivial primitive positive word.
This checkpoint proves none of those universal assertions.
