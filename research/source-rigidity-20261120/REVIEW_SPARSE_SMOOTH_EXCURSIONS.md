# Independent review of sparse shifted-smooth excursions

**Verdict: VERIFIED, with the stated S-unit dependency.** The finite
incidence bound, its asymptotic consequence for nonperiodic trajectories,
and the treatment of hypothetical nontrivial cycles are valid at the
frozen hash below. No correction is requested. This review is separate
from the SS1–SS4 review and does not extend that earlier content pin.

Reviewer: the independent merger agent. Review date: 2026-11-20.

## Frozen scope

| File | Bytes | SHA-256 |
|---|---:|---|
| `SPARSE_SMOOTH_EXCURSIONS.md` | 5206 | `d35f40218ff261ef2ddd58561abfe4d8d9977004edaa9c4e58ea7f89628afcba` |

The source directory was
`/workspace/scratch/46eba7b29f50/agent-analytic-remains/`.
The load-bearing dependencies are:

| Dependency | Interface | SHA-256 |
|---|---|---|
| `SHIFTED_CORE_TRANSITIONS.md` | SC1 for ordered core pair `(1,1)`, and the elementary defect clock | `f53846e08e1522058797c6cab57111cf9c7ed4385f39b0e055ab05264f7acb71` |
| `SHIFTED_SMOOTH_CYCLES.md` | SS2 excludes nontrivial cycles entirely within the shifted two-prime class | `e3db28e9e944a36dacd54f661cda8a1856664bfac3d248caefdf23b1a9875c60` |

Those interfaces were reconstructed in the companion independent
`REVIEW_SHIFTED_SMOOTH_CYCLES.md`, SHA-256
`4d0926f9f209e7aaab1f27a315e171d91ea5a13d59109b4e3a793489f64416bc`.
In particular, the external coefficient-uniform S-unit theorem is
retained as an external dependency; the elementary cycle theorem has
no such dependency. No PR145 compressed-word assertion is needed.

## SE1: finite incidence and the endpoint convention

Use one fixed positive odd ordinary source and its actual accelerated
trajectory `n_j`. For a prefix ending at `N`, `D_N` counts defect
transitions at indices `0<=j<N`, while `C_N` counts outside-class
vertices at indices `0<=j<=N`. The latter is a count of occurrences,
not a count of different arithmetic cores.

Assume all `N+1` states are distinct. Distinct source states yield
distinct ordinary transitions. SC1 then bounds the number of defect
transitions with ordered core pair `(1,1)` by `B_2`.

Every remaining defect transition touches at least one outside-class
vertex. Count incidences between those transitions and such vertices.
Every remaining edge contributes at least one incidence, and every
outside vertex has degree at most two in this finite path. Hence the
number of remaining defect edges is at most `2C_N`. This proves

\[
D_N\le B_2+2C_N.
\]

The simple-prefix hypothesis is used for the S-unit bound on distinct
transitions, not for the elementary incidence count. It cannot be
discarded and replaced with an arbitrary number of repeated traversals
of a cycle.

The endpoint `N` must be included. In the literal one-edge segment
`17 -> 13`, the first shifted core is 1 and the last is 7. The defect
edge touches an outside vertex only at the endpoint. Omitting that
endpoint would invalidate the local incidence estimate.

The factor two is optimal for this local argument. Direct evaluation
gives

\[
3\cdot17+1=52=2^2\cdot13,
\qquad
3\cdot13+1=40=2^3\cdot5.
\]

The three shifted cores are `1,7,1`. Both defect edges touch the same
outside vertex, so there are two such edges and one outside visit.
This is a precise local saturation control; it does not assert that
the final universal constant or additive bound is globally optimal.

The source clock follows from

\[
N<R_{D_N+1}\le\frac{h_0}{\gamma}
                       (\alpha^{D_N+1}-1),
\qquad
\alpha=\log_2 3>1,\quad\gamma=\alpha-1>0.
\]

Taking logarithms and using the integer value of `D_N` gives

\[
D_N\ge\left\lfloor\log_\alpha
                    (1+\gamma N/h_0)\right\rfloor.
\]

This remains correct when the logarithm is itself an integer, because
the source inequality is strict. Combining this bound with the
incidence inequality proves the author's finite bound (4), including
its factor one-half and its additive constant `B_2/2`.

## SE2: both possible types of counterexample are covered

For a deterministic ordinary trajectory, either all states are
distinct or an actual state repeats and the orbit is eventually
periodic. These cases exhaust an orbit that never reaches 1. A repeat
before a supposed later first arrival at 1 would instead trap the
orbit in an earlier cycle, so every finite first-arrival path is
simple as stated.

In the nonperiodic case the finite bound applies for every `N`.
Because `n_0` is fixed, `h_0` is constant. Therefore

\[
\log_\alpha(1+\gamma N/h_0)
=\frac{\log N}{\log\alpha}+O_{n_0}(1).
\]

The floor and the fixed constant `B_2` contribute only bounded errors.
Dividing by the natural logarithm of `N` proves

\[
\liminf_{N\to\infty}\frac{C_N}{\log N}
\ge\frac{1}{2\log\alpha}.
\]

All clocks here count accelerated odd transitions. No replacement by
shortcut time or by a count over varying initial integers occurs.

If a nonconvergent orbit is eventually periodic, its positive odd
cycle cannot contain 1. SS2 therefore implies that some cycle state
has an outside prime in its shift. If the cycle has period `p` and
`r>=1` such states, each whole period contributes exactly `r` outside
visits. The finite initial segment changes the count by a bounded
amount, giving

\[
C_N=(r/p)N+O_{n_0}(1).
\]

Thus the ratio to `log N` tends to infinity in this case. This use of
SS2 is necessary: the finite-prefix S-unit count alone cannot be
iterated through repeated states.

Every possible counterexample consequently satisfies the stated
lower limit. Its contrapositive proves the strict-threshold
convergence condition. The strict inequality matters; the argument
does not exclude equality at the threshold. In particular,
`C_N=o(log N)` is sufficient. Eventual confinement has bounded
`C_N` and is a special case.

## Exact controls executed

I executed the ordinary segment `17 -> 13 -> 5` independently using
literal multiplication, addition, and repeated exact division by two.
The recorded first two exponents were `(2,3)`, and removing powers of
2 and 3 from the three shifted values gave `(1,7,1)`.

The one-edge truncation verifies the necessity of including the final
vertex; the two-edge path saturates the local factor two. The control
receipt is `review-sparse-smooth-controls.json`, SHA-256
`70d9477409a37a9f7815af63c677d8812ff6268708144a152098a6f66691afa8`,
in `/workspace/scratch/46eba7b29f50/agent-merger-remains/`.

No larger orbit census was needed. These local controls test the exact
incidence conventions; the unbounded-frequency conclusion is proved
by the finite inequality and limiting argument above. Neither the
astronomical S-unit bound nor an infinite trajectory was tested by
computation.

## What remains unproved

The result is a necessary arithmetic behavior of every hypothetical
counterexample and a corresponding sufficient condition for a fixed
source. It supplies no upper bound on `C_N` for an arbitrary source.
In particular, zero ordinary density of outside visits would not be
enough to invoke the logarithmic threshold. The author also correctly
avoids claiming an actual convergent orbit with infinitely many
outside visits: after its finite first hit at 1, all shifted values
are 2 and the visit count is eventually constant.

The proposed source-persistent upper estimate remains the unsupported
all-source step. Exits, reciprocal-height charge bounds, and the
number of different cores do not by themselves prove that estimate.
The note's stated publication boundary is accurate.
