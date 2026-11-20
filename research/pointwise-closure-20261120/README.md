# Ordinary trajectories: sparse visits, local mergers, and stopping burden

**PROPOSED research; Collatz remains unresolved.** This packet develops three
ordinary-integer routes against the source heads frozen on 20 November 2026.
It proves narrower statements in writing, supplies finite arithmetic replays,
and identifies the inference still missing from each proposed global closure.
The separate agent reconstructions are evidence for these scoped arguments;
they are not formal verification, external peer acceptance, or an extension
of the repository's accepted baseline.

The strongest trajectory estimate is elementary: for every fixed
`0<c<1/sqrt(2)`, among any `N` **distinct consecutive odd states**, all but

\[
O_c\!\left(N2^{-\delta_c\sqrt{\log_2 N}}\right)
\]

have more than `c sqrt(log_2 N)` set bits, for some `delta_c>0`. A complementary
fixed-cap argument gives `O_S(N^(1-1/S))` visits to at most `S` set bits. These
are upper bounds on sparse visits, not a mechanism forcing a visit to 1.

## Maps and clocks

The shortcut map is

\[
T(n)=\begin{cases}n/2&n\text{ even},\\(3n+1)/2&n\text{ odd},\end{cases}
\qquad
U(n)=\frac{3n+1}{2^{v_2(3n+1)}}\quad(n\text{ positive odd}).
\]

Write `s(n)` for binary popcount. On a source already known to reach 1,
`d(n)` is the first-hit shortcut clock and `a(n)` is its number of odd
inputs. The merger note calls this same odd count `p(n)`. No first-hit
count is assigned to a source whose convergence has not been established.
The occupancy theorems count states in odd-event time. They require
distinctness; infinitely many repeated laps of a cycle are outside their
scope.

## Results and the remaining global step

| Result | Exact advance relative to the frozen source packets | Dependency and first unsupported step |
|---|---|---|
| [Sparse return spectra](SPARSE_RETURN_SPECTRUM.md), SR-1–SR-4 | The possible exponents joining two homogeneous values of bounded popcount form a finite set, uniformly in the source. This yields `O_S(N^(1-1/S))` occupancy without logarithmic losses. The cases `S=2,3` have explicit elementary bounds. | General spectrum finiteness imports a published S-unit theorem; the carry and window arguments are reconstructed locally. No lower frequency of sparse visits or global rule for replacing a closed carry cut is proved. |
| [Growing binary complexity](GROWING_COMPLEXITY.md), equation (1) and Section 2 | An elementary all-`N` inequality gives the threshold `c sqrt(log_2 N)` for every `c<1/sqrt(2)`. This doubles the limiting coefficient of the **popcount consequence** of PR #145's existing run theorem. | Uses exact powers of three modulo powers of two, a fixed-source carry cut, and a binomial-tail inequality. It does not improve the run-count theorem itself or bound complexity from above. |
| [Local affine merger membership](LOCAL_CERTIFICATE_GRADE.md), LC-1–LC-3 | Gives an exact criterion and constructor for a fixed-word merger certificate on a binary class containing a **specified ordinary parameter whose arms converge**. Infinite convergent families lie outside every such certificate for `(t,3t)`. | Requires finite first-hit paths for the specified arms. It does not infer their convergence at unverified parameters or cover the ordinary residual set by another method. |
| [Stopping burden of the inverse potential](STOPPING_BURDEN.md), SB1–SB5 | Identifies `W(1)` with an exact supremum over first-hit scores and proves that its finiteness is equivalent to a uniform logarithmic odd-event bound with bounded additive error throughout the convergent basin. | The [local reciprocal budget](LOCAL_DISTORTION.md), LD1–LD2, makes the reduction self-contained. Neither the bounded supremum nor convergence outside the known basin is proved. |

### 1. Sparse returns retain the original source

For a fixed cap `S`, let

\[
E_S=\{h\ge0:\exists u>0\text{ odd},\ s(u),s(3^h u)\le S\}.
\]

The spectrum is finite. A minimal vanishing subsum of the two binary
expansions puts the problem into a finite family of fixed S-unit equations, whose
coefficients do not change with `u`. An explicit bound on `|E_S|` is
given; it is **not** a numerical bound on `max E_S`.

A long gap in an actual source splits it into disjoint upper and lower
blocks for a guarded number of odd events. While that original cut
survives, sparse returns have times in `E_(S-1)`. Counting short-gap
integers and disjoint guarded windows gives, for all integers `S>=2`,
`L>=1`, and `N>=1`,

\[
\#\{j<N:s(x_j)\le S\}
\le\sum_{r=1}^S(2L)^{r-1}+|E_{S-1}|\left\lceil\frac NL\right\rceil.
\]

The trajectory `257 -> 193 -> 145 -> 109 -> 41` is retained as an exact
counterexample to extending the guarded spectrum past the life of its cut.
Re-selecting a different cut changes the upper source and needs a new
global argument.

### 2. Ordinary membership is stricter than dense certificates

Set `kappa(n)=d(n)-2a(n)` on convergent sources and
`w(b)=v_2(b)+2v_3(b)` on positive integer slopes. For finitely many affine
arms `x_i=b_i t_0+c_i>0`, all known to reach 1, a fixed-word local merger
certificate through the ordinary integer `t_0` exists exactly when

\[
\frac{b_i}{2^{v_2(b_i)}3^{v_3(b_i)}}\quad\text{and}\quad
\kappa(x_i)-w(b_i)
\]

are each independent of `i`. The proof constructs the certificate by
padding first-hit paths with complete `1 -> 2 -> 1` cycles. For `(t,3t)`
the condition becomes `kappa(3t)-kappa(t)=2`.

For example,

\[
T^{12}(15+4096k)=T^{12}(45+12288k)=1+243k\qquad(k\ge0).
\]

In contrast, every parameter `2^r` and every parameter `5*2^r` fails this
local criterion, although both arms converge. The second family even
synchronizes in clock and odd count. Thus neither ordinary meeting nor
density of successful binary subclasses gives an exhaustive certificate
cover. This does not rule out a broader proof that also uses induction,
doubling, or another ordinary rule.

### 3. The inverse bound contains a quantitative stopping assertion

For the legal unit inverse words of PR #149, put `delta=8-5 log_2 3>0`.
Then

\[
W(1)=\sup_{\substack{n>0\text{ odd},\ 3\nmid n\\n\to1}}
        \bigl(8a(n)-5d(n)\bigr),
\]

and the local simple-path budget yields

\[
W(1)<\infty\quad\Longleftrightarrow\quad
\sup_{\substack{n>0\text{ odd},\ 3\nmid n\\n\to1}}
\left(a(n)-\frac5\delta\log_2n\right)<\infty.
\]

The leading constants are `5/delta = 66.5004188...` for odd events and
`8/delta = 106.4006701...` for shortcut steps. A known valid bound on
`W(1)` would also give an exact integer deadline for basin membership.
The finite experiments supply no such all-source bound. This reduction
does not assert that qualitative Collatz and the quantitative condition
are logically inequivalent; that would require a separate argument.

## Source and review boundaries

Main was frozen at `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`.
The following source files supply the definitions, antecedents, and
comparisons used here. Each new proof states precisely what it imports.

| PR and full head | Path and claim used |
|---|---|
| #141 — `5025ef464d4b6d4f4a412a3e33c3477de68dfa8b` | `research/ay-persistent-20261031/PROOF.md`, HC-1–HC-3; separated-source arithmetic and the bounded-popcount core. |
| #145 — `dd245a712f985909f541590e3f6c179b7ba011e4` | `research/binary-run-occupancy/README.md`, Sections 1–4; fixed and growing run occupancy. |
| #146 — `561d48a4d3a793a59b1cdf0406062ae1a6d47515` | `research/upper-bit-mergers/AFFINE_RAYS.md`, slope classification; `THREE_RAY.md`, global merger and defect-count implications. |
| #149 — `92c0129e794dde3ec55ceec470a12d51ba3f7e2f` | `research/forward-inverse-defect/CLOSURE_BOUNDARY.md`, definition of `W` and closure boundary; `research/persistent-defect-classes/README.md`, Section 1, stopping defect. |
| #148 — `6ff18e4f63be8f3bece76215fcfe44d83b001d7f` | Prior opposite-sign stopping grade, as credited explicitly in the frozen #149 source. No additional result is imported from this PR. |
| #140 — `fe2247fcd7730c15430941a7b6e011d006d41d84` | `research/novel-swarm-20261030/pass4/WINDOWS.md`, W1–W3; stronger historical reciprocal budget, comparison only. The present proof uses LD1–LD2. |

The two external S-unit inputs are cited directly, with theorem numbers
and primary links, in [SR-1 and SR-1Q](SPARSE_RETURN_SPECTRUM.md).
No external priority claim is made for these applications or for the
general orbit-sparsity mechanism.

See the [execution and review report](../../reports/2026-11-20-pointwise-closure/README.md)
for exact file hashes, four cross-route proof reconstructions, bounded
replay output, controls, and the repository validation receipt. The
[finite three-ray defect attempt](../../reports/2026-11-20-pointwise-closure/FINITE_THREE_DEFECT_BLOCKER.md)
records the additional five-ray identity that the attempted strengthening
did not establish.

## Handoff

The common missing step is pointwise global control. Sparse occupancy
allows complexity to keep growing; local merger certificates leave an
ordinary residual set; the inverse reduction leaves its uniform score
bound unproved. A complete proof must supply one of these missing
implications or a different architecture that handles every positive
integer. These results cannot be composed into that implication merely
by sharing a trajectory or a source packet.
