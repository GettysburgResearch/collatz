# Completing Collatz through the forced dyadic band

**Full theorem: OPEN.** This packet pursues the new global section theorem in
PR 173 through three complementary completion attempts. The new mathematical
results are an actual induced-return descent certificate, a short-return
arithmetic certificate with explicit ordinary obstructions to its universal
use, and a global source-weighted first-entrance estimate. These statements do
not establish descent from every marked source.

The formal sources are under [`lean/`](lean/). The complete replay passed all
eight compiler commands and audited all 43 new public theorems using only
standard Lean axioms. Exact source hashes and output are in the
[replay report](../../reports/band-completion-20261121/README.md). A passing Lean
build proves the encoded statements, including their hypotheses; it does not
remove the coverage hypotheses discussed below.

## The result we build on

Use the shortcut map

\[
T(n)=\begin{cases}n/2&n\equiv0\pmod2,\\(3n+1)/2&n\equiv1\pmod2.\end{cases}
\]

For an odd positive integer \(x\), let \(d_x=\lfloor\log_2x\rfloor\). The
marked section is

\[
D=\{x\text{ odd}>0:(d_x+1)(x-2^{d_x})\le70\,2^{d_x}\}.
\]

The source is frozen at **PR 173,
`fa0c9e2a2851e6324391e39c17afcb5913185aec`**. Its
[`ForwardSection.lean`](https://github.com/GettysburgResearch/collatz/blob/fa0c9e2a2851e6324391e39c17afcb5913185aec/research/lean-shell-cover/ForwardSection.lean)
proves that every positive ordinary source reaches \(D\) in fewer than
\(4\lfloor\sqrt n\rfloor+\lfloor\log_2n\rfloor\) shortcut clocks. Its
[`SectionDynamics.lean`](https://github.com/GettysburgResearch/collatz/blob/fa0c9e2a2851e6324391e39c17afcb5913185aec/research/lean-shell-cover/SectionDynamics.lean)
defines the first strictly positive marked return \(R\) and proves

\[
\mathrm{Collatz}\quad\Longleftrightarrow\quad
\forall x\in D\setminus\{1\}\ \exists j,\ R^j(x)<x.
\]

This is the full target of the present attempt. The same upstream packet
already proves that first marked returns can expand by arbitrarily large
factors. That result is credited to the source and is not presented as a new
result here.

## New results

| Route | Positive result | Exact remaining boundary |
|---|---|---|
| [Offset certificates](descent/README.md) | A complete proof for the small offset, within the available binary depth and with an explicit size guard, yields a smaller actual marked return. | Some ordinary marked offsets provably cannot finish within that depth. A total procedure needs another route for them. |
| [Rotation and valuations](rotation/README.md) | An actual marked return in an explicit early window forces ordinary descent; the actual valuation sum remains explicit throughout. | Every prescribed window has an explicit ordinary marked start with no such early return, even when the numerical budgets hold. |
| [Source mass](mass/RENEWAL_ATTEMPT.md) | The first section entrance has a finite fourth logarithmic moment under the original source weights, including every entrance fiber. | No uniform estimate for infinitely many retained returns or decay of the primitive survivor moment has been proved. |

### 1. A certificate for a smaller actual marked return

Write \(x=2^d+u\), where \(u>0\). Suppose that, for some \(k\le d\),

\[
T^k(u)=1,
\qquad B=\left\lfloor\frac{2^d}{u}\right\rfloor+1,
\qquad4\lfloor\sqrt B\rfloor+2\lfloor\log_2B\rfloor\le d.
\]

Then some actual induced return satisfies \(R^j(x)<x\). This is
`CollatzShell.BandDescent.offset_certificate_return_descent`.

The exact ordinary prefix identity is

\[
T^k(2^d+u)=3^{q_k(u)}2^{d-k}+T^k(u),\qquad k\le d,
\]

where \(q_k(u)\) counts the actual odd inputs. The nonnegative affine
remainder implies \(3^{q_k(u)}u\le2^kT^k(u)\), so the endpoint is at most
\(B\). The explicit guard pays for a later forced marked visit below
\(2^d\). The source `captures` theorem identifies this visit with an iterate
of the actual return map.

This last step matters: a smaller unmarked endpoint alone does not guarantee
a smaller marked return. The present certificate proves the latter directly.

The universal quick-offset premise is false. For every \(a\ge1\),

\[
u_a=2^{2a}-1,\qquad x_a=2^{3a}+u_a
\]

is a marked start of binary depth \(3a\), with relative offset less than
\(2^{-a}\). Neither \(u_a\) nor \(x_a\) ever falls below its own starting
value during the first \(3a\) shortcut clocks. These are all-parameter
ordinary integer theorems. They do not assert nonconvergence of these starts.
The route note also gives an outer-band family where the size guard already
holds but the quick certificate still fails, and a genuine unbounded family
where all certificate guards succeed.

### 2. A short actual return forces descent

Let \(x_j\) denote the odd accelerated orbit, with
\(\alpha=\log_2 3\),
\(A_j=\sum_{i<j}v_2(3x_i+1)\), and
\(E_j=\sum_{i<j}\log_2(1+1/(3x_i))\). The new module proves the exact identity

\[
\log_2x_j=\log_2x_0+j\alpha-A_j+E_j.
\]

If the orbit has not descended below its marked start \(n\), a marked
return at odd clock \(j\) supplies an integer \(b\) with

\[
|j\alpha-b|\le\frac{140}{\lfloor\log_2n\rfloor+1}+\frac jn.
\]

Consequently, if \(d=\lfloor\log_2n\rfloor\) and

\[
(d+1)H\le n,\qquad141(4^H+1)\le d+1,
\]

then any positive marked return at odd clock \(j\le H\) forces an ordinary
orbit value below \(n\). This result counts **odd accelerated clocks**; the
source entrance bound counts shortcut clocks.

The module also constructs, for every \(H\),

\[
m=2H+10,\quad d=2^m,\quad n=2^{d-m}(d+1)-1,
\]

which is marked and satisfies both numerical budgets but has no positive
marked visit in that early window. Its long suffix of binary ones forces a
rising ordinary prefix. This adapts the source's leading-band/trailing-ones
construction to the precise certificate window; arbitrarily expanding first
returns were already proved upstream.

### 3. All original source mass is retained at entrance

Let \(E(n)\) be the first actual marked entrance of the source \(n\). The
new source-weighted bound is

\[
\sum_{n\ge1}n^{-4}\bigl(1+\lfloor\log_2E(n)\rfloor\bigr)^4
\le4096\sum_{n\ge1}n^{-2}<\infty.
\]

The proof combines the quantitative entrance clock with
\(T^t(n)\le2^tn\). It preserves \(n^{-4}\) at the original source and
retains all collisions in the entrance map. Exact finite packet conservation
is formalized alongside the moment estimate.

The renewal note then attempts the full closing estimate, using the
cycle-sensitive primitive survivor decomposition in PR 176 at
`ad9a0611d22b48c0fd0c1da31091179654ba31a9`. The needed decay of the primitive
moment remains unproved. The precise arithmetic obstruction is a missing
weighted estimate for actual primitive words in intervals shorter than their
ternary modulus; replacing the transported distribution with a new endpoint
average would discard the retained source information.

## What remains to complete the theorem

The sufficient offset and short-return certificates do not form a complete
cover. The explicit families above prevent using either proposed clock rule
as the missing universal statement. The source-mass estimate controls the
first entrance and does not establish eventual absorption of every retained
packet. A completion therefore still needs control of the **actual longer
return dynamics**, such as an invariant that supplies a smaller marked return
for each unresolved source or a valid decay estimate for its original source
mass. No custom axiom or assumed universal stopping statement fills this step
in the formal files.

## Provenance and replay

The four upstream inputs remain byte-identical in [`lean/vendor`](lean/vendor);
[`upstream-files.json`](upstream-files.json) records their exact commit, paths,
and SHA-256 digests. Their compilation inputs are generated locally in
`lean/.build/generated` with the supported Lean module/export headers. The
helpers `GridAt`, its decidability instance, and `visit_exists` are made public
because the exposed `firstMesh` and `firstVisit` definitions use them. This is a declaration-visibility adaptation; no upstream formula or
proof body is changed. Generated files and binary artifacts are not committed.

Pinned tools: **Lean 4.34.1**, Mathlib commit
`d13f23b723b8a846827a245b89c10fc7d3f11612`, with its matching built dependency
cache. The replay driver verifies the tool versions and upstream source
hashes, regenerates the module inputs, and compiles with warnings as errors:

```bash
python -B research/band-completion-20261121/lean/build.py \
  --lean /path/to/lean-4.34.1/bin/lean \
  --mathlib /path/to/mathlib4 \
  --receipt /path/outside/the/checkout/band-lean-replay.json
```

The route notes distinguish formal statements from their additional ordinary
mathematical consequences. The repository validation gate and this external
Lean replay are separate checks.
