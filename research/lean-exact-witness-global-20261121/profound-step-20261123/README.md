# Ordinary entrance laws, finite trial mass, and adaptive integer descent

23 November 2026. **Full Collatz, the original residue-512 implication,
and FloorIntervalStep remain OPEN.** This checkpoint starts from PR177
at `92e7aaf602a0d4f0442556a133ae8e882e1fe93f` and attacks the actual
closing estimates using primary literature and three parallel lanes.

[Coordinating connection](COMMON_DISPLACEMENT_AND_FREE_ENERGY.md) ·
[Execution and review report](../../../reports/lean-exact-witness-global-20261121/profound-step-20261123/README.md) ·
[Source ledger](../../../reports/lean-exact-witness-global-20261121/profound-step-20261123/SOURCES.json)

## What changed

| Route | New result | Remaining universal step |
|---|---|---|
| Ordinary inverse pressure | An exact killed ordinary bridge, a same-source entrance law with centered lifetime, finite total root variation, and a finite-support free-energy identity | Construct finite ordinary trial sets whose absolute transport cost is small enough to contradict the preceding root-summability theorem |
| Integer ranks and cycle templates | Adaptive descent using each source's actual repetition lattice, including unbounded defects and independently changing rational fixed points with the full center change paid | Select paid actual macros for every remaining ordinary trajectory, and retain the nontrivial-cycle condition at any integral template center |
| Fixed-sibling integer repair | Exact primitive denominators and simultaneous real/2-adic errors for every upper sibling power; the specified mixed-place product is at least 7/3; signed extrapolation identifies the same displacement as the rank theorem | Construct a different legal integer repair or a new approximation with an actual subcritical arithmetic estimate |

The three new modules contain **28 public Lean declarations**. Their
finite scopes are stated below. The infinite analytic results and the
mixed-place obstruction are written proofs; no external deep theorem
is inserted as a research axiom.

## 1. The potential transform retains an ordinary endpoint

On one hypothetical escaping component of positive odd ternary units,
retain the ordinary weight `r(n)=Lambda_infinity(n)/n`, the complete
inverse operator `P_s`, and its Green potential `Z_s`, for `s>1`.
Write

\[
A_s(q)=\sum_{n\in\operatorname{Pred}_U(q)}r(n)^s
      =r(q)^sZ_s(q),\qquad M_s=\sum_{n\in E}r(n)^s.
\]

The [ordinary entrance-law theorem](pressure/ORDINARY_ENTRANCE_LAW.md)
constructs a killed kernel

\[
K_s(q,v)=(3/2^e)^s\frac{Z_s(v)}{Z_s(q)}\quad(Uv=q),
\qquad K_s(q,\dagger)=1/Z_s(q).
\]

The killing term is essential. From any root `q`, the final ordinary
state `N_q` and its inverse-edge lifetime have the exact law

\[
\Pr_q(N_q=n,\tau_q=k)=\frac{r(n)^s}{A_s(q)}
\]

at the unique ordinary ancestor depth `k`. The probabilities sum to one,
so this inverse sampler terminates almost surely. This is a theorem
about the new sampler, not forward Collatz termination.

For `q_j=U^j(q_0)`, the endpoint laws `nu_j` converge to the fixed
ordinary probability `mu_s(n)=r(n)^s/M_s`. More precisely,

\[
\operatorname{TV}(\nu_j,\mu_s)=1-A_s(q_j)/M_s\longrightarrow0.
\]

For each ordinary source `n` in this component there is a well-defined
integer phase `h(n)=k-m` whenever `U^k n=q_m`. Consequently

\[
\tau_j-j=h(N_j),\qquad
\mathcal L(N_j,\tau_j-j)\longrightarrow\mathcal L(N,h(N))
\]

in total variation, with the same explicit error. In a natural coupling,
the sampled ordinary endpoint eventually stays equal to one fixed `N`
almost surely. Its lifetime then increases as `j+h(N)`.

The preceding complete-capacity theorem also gives

\[
\sum_j\|\nu_{j+1}^{1/s}-\nu_j^{1/s}\|_{\ell^s}<\infty.
\]

At `s=2`, this is finite total Hellinger length. The complete first-entry
code has finite Renyi entropy of order `1/s`, including every ray atom
and every inverse side branch. Neither conclusion bounds the numerical
time labels by itself.

### The exact free-energy target

For the complete balanced ordinary bijection `Phi_j` from ancestors of
`q_j` to ancestors of the unchanged sibling `Sq_j=64q_j+21`, let `Delta_j`
be its signed exponent cost and `R_j=Z_s(Sq_j)/Z_s(q_j)`. Then

\[
R_j=\mathbb E_{\nu_j}2^{-s\Delta_j},\qquad
\frac{d\widehat\nu_j}{d\nu_j}=\frac{2^{-s\Delta_j}}{R_j},
\]

\[
\boxed{
-\log R_j=\inf_{\sigma\text{ finite ordinary support}}
\left[s\log2\,\mathbb E_\sigma\Delta_j+
\operatorname{KL}(\sigma\Vert\nu_j)\right].
}
\]

All sources and the sibling are retained. No Haar or fresh random-word
law substitutes for `nu_j`. The infimum identity is proved by finite
tilted restrictions; it does not assume finite expected cost on the
whole tree.

The [coordinating finite certificate](COMMON_DISPLACEMENT_AND_FREE_ENERGY.md#2-a-finite-trial-law-is-an-actual-finite-set-of-ordinary-ancestors)
provides an explicit trial. For a nonempty finite ordinary ancestor set
`F`, put `W_F=sum_(n in F) Phi_j(n)^(-s)` and
`sigma_F(n)=Phi_j(n)^(-s)/W_F`. Using only the proved constant
`c_*=exp(-160/3)`, its objective is at most

\[
\boxed{
\log\frac{s}{s-1}-s\log(64c_*)-\log W_F.
}
\]

Thus a candidate finite source set and its actual paths can certify an
upper bound without evaluating infinite weights. Constructing such sets
at the required scale remains open.

The normalized-law issue is tested exactly: even the empty-address
zero-cost anchor, total-variation convergence, Hellinger affinity tending
to one, and uniformly integrable transported densities can coexist with
a vanishing partition function in an abstract two-part control. Absolute
arithmetic cost must still be bounded. This control is not claimed as a
Collatz realization or a counterexample to the desired Green inequality.

## 2. Every macro can pay its own lattice and center

For actual shortcut word data

\[
F_u(x)=\frac{Px+C}{Q},\qquad d=Q-P\ne0,
\]

and a following arbitrary defect `t` with data `(R,S,B)`, let
`E=dB-(S-R)C`. Literal ordinary repetition `u^k` forces
`Q^k | (dx-C)`. The new [adaptive theorem](arithmetic/ADAPTIVE_LATTICE_DESCENT.md)
uses that particular source lattice directly:

\[
\boxed{RP^k+|E|<SQ^k}
\quad\Longrightarrow\quad
dx-C\ne0\Longrightarrow |dy-C|<|dx-C|.
\]

There is no common cutoff, contracting-base assumption, or target-lattice
premise. If each actual macro pays its own inequality, a fixed point is
hit within `|dx_0-C|` macros. For a contracting base, every finite defect
has an individual cutoff, so defect lengths may be unbounded.

In particular every literal positive all-time path

\[
(10)^{k_0}t_0(10)^{k_1}t_1\cdots,
\qquad k_j\ge2\max(1,|t_j|),
\]

reaches 1 within `x_0-1` macrosteps. No uniform defect-length bound is
used. The explicit `2|t|` calculation is credited to the prior packet;
the new theorem allows it to vary at every macro.

### Independently changing rational fixed points

The bases themselves may change. Let `c_j/d_j`, `d_j>0`, be a rational
fixed point of the actual base word, so
`d_j C_j=(Q_j-P_j)c_j`. Put

\[
z_j=d_jx_j-c_j,\qquad
F_j=d_{j+1}(R_jc_j+d_jB_j)-S_jd_jc_{j+1}.
\]

The complete paid condition is

\[
\boxed{
R_jP_j^{k_j}d_{j+1}+|F_j|
<S_jQ_j^{k_j}d_j.
}
\]

It forces strict decrease of the same nonnegative integer `|z_j|`
until a center is hit, by at most `|z_0|` macros. All bases, denominators,
defects and exponents may vary. An integral positive hit reaches the
actual cycle of its legal base word. A nonintegral or nonpositive center
cannot be hit by an ordinary positive source. Arbitrary integral centers
retain their separate nontrivial-cycle obligation.

The full cross-carry prevents an unpaid change of rank. For example,
`5 -> 8 -> 4` reduces distance to center 1 from 4 to 3, but switching
the next center to 0 resets that distance to 4. The new condition becomes
`3+1<4` and correctly refuses the purported strict descent. A universal
selector of paid macros has not been constructed.

## 3. The canonical adelic repair was tested at every place

The [repair theorem](repair/ADELIC_INTEGER_REPAIR.md) treats every upper
sibling power. Put

\[
h_b=(64^b-1)/3,\qquad \nu_b=1+v_3(b),\qquad c_b=h_b/3^{\nu_b}.
\]

The canonical rational pullbacks satisfy

\[
y_j^{(b)}-q_0
=h_b\frac{2^{A_{j+1}}q_{j+1}}{3^j},\qquad
y_{j+1}^{(b)}-y_j^{(b)}
=h_b\frac{2^{A_{j+1}}}{3^{j+1}}.
\]

For `j>nu_b`, the reduced denominator is exactly `3^(j-nu_b)`, and
the binary precision to `q_0` is exactly `A_(j+1)`. On an escaping ray
the real limit exists, but it is not identified with the 2-adic limit.

For the explicitly displayed Subspace-Theorem forms at infinity, 2 and
3, the primitive-pair product satisfies

\[
\boxed{\Pi_j^{(b)}\ge c_b/3\ge7/3.}
\]

The required negative power of height therefore fails for those forms
and approximants, even provisionally assuming the real limit algebraic.
This does not rule out other approximants or ordinary integer repairs.
The actual alternative `75 -> 113 -> 85` remains a finite control
against such an overstatement.

Signed periodic extrapolation does produce an exact cancellation, but
its error is

\[
H_j+q_0=\frac{2^{A_j}}{3^j}
       \frac{(Q-P)q_j-C}{Q-P}.
\]

Thus its gained binary precision is precisely the adaptive source
displacement lattice. The coordinating proof retains the distinction
between a convergent periodic model and the actual nonperiodic tail.
Neither enough paid repetitions nor a different universal repair follows
from this identity.

## 4. Literature use and verification

The relevant primary texts were read at their actual interfaces:
Vigon's potential transforms (with a local printed denominator corrected
by direct telescoping), Adamczewski--Bugeaud's exact Subspace inequality
and periodic approximants, Gouezel's Ancona hypotheses, Sarig's recurrence
criterion, Krasikov--Lagarias predecessor growth, and the
Applegate--Lagarias multiplicative semigroup. Author/conference summaries
of size-change termination and transition invariants supplied orientation;
they are not advertised as full-paper imported proofs.

The source ledger and lane reports separate direct theorem reconstruction,
abstract/scope inspection, inherited results and new deductions. The new
PR178 full numerical-gcd packet was inspected at its frozen changed head;
its unbounded coprime-packet result is not duplicated here.

| Module | New audited statements | Formal boundary |
|---|---:|---|
| `arithmetic/AdaptiveLattice.lean` | 13 | Source-lattice and changing-center descent, first-hit clocks, literal ordinary-word consumers |
| `pressure/EntranceLaw.lean` | 9 | Finite merger phases, transformed-path telescoping, killing and row normalization |
| `repair/AdelicRepair.lean` | 6 | Cleared pullback and extrapolation arithmetic |

All 28 passed fresh strict root compilation with Lean 4.34.1. All three
exact checkers passed normally and under optimization with identical
paired output. Internal reviews bind the exact final science hashes and
disclose shared inputs. No countable probability, real convergence,
external Subspace theorem, or universal selector is silently included in
those finite Lean statements. See the linked execution report for the
actual commands, primary-source scope, and publication gate.
