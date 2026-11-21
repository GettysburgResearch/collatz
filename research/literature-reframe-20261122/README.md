# Literature-led global attempt: ordinary moments, arithmetic budgets, and physical mergers

**Full Collatz convergence remains OPEN.** This continuation of PR178
uses primary literature to pursue the global step left by the marked-band
work. Its strongest analytic reduction is a critical first-moment target
for actual orbit minima. It also checks a fixed-source parity-window budget
in Lean, obtains an all-parameter lower bound on merger continuation clocks,
and identifies the exact probability law behind square pressure.

The work is on
[`research/lean-global-20261121`, draft PR178](https://github.com/GettysburgResearch/collatz/pull/178).
It builds on the [previous reframe packet](../reframe-20261121/README.md).
The [execution report](../../reports/2026-11-22-literature-reframe/README.md)
distinguishes actual Lean execution, semantic paper reviews, and conditional
global assertions. No open premise is installed as a Lean axiom.

## 1. The strongest global closing target from this pass

Let \(U\) be the accelerated Collatz map on positive odd integers, and put

\[
m(n)=\min_{j\ge0}U^j(n),\qquad
\mathcal M(X)=\frac1{\log X}
\sum_{\substack{n\le X\\n>0\text{ odd},\ 3\nmid n}}\frac{m(n)}n.
\]

The minimum exists for every positive source, without assuming its orbit
converges. The [ordinary-renewal note](ORDINARY_RENEWAL.md) derives the
following implication under its explicit uniform predecessor-density
premise PDU:

\[
\boxed{\liminf_{X\to\infty}\mathcal M(X)<\infty
\quad\Longrightarrow\quad
\text{every ordinary orbit is eventually periodic}.}
\]

The proof extracts disjoint off-orbit predecessor basins from one
hypothetical nonperiodic orbit. Taking the least unit source in each basin
keeps a lower bound on the entire future minimum of every source in that
basin. PDU makes every such basin contribute a fixed positive amount to
the displayed first moment. Infinitely many basins force the moment to
diverge.

This is a written conditional theorem. **The required first-moment bound
is not proved here, and nontrivial positive cycles remain a separate
alternative.** PDU is the source-qualified population assertion from
PR180 at `d0349de2108abb7c8fb8393c086610e3372df116`; it is not treated as a
formalized or independently established result of this packet. The note
also gives an additive survivor-tail inequality and the exact weighted
first-passage transport error that would have to be controlled to establish
the moment bound. Tao's published first-passage theorem is used with its
actual source law and quantifiers, not strengthened into this missing bound.

## 2. Arithmetic control that survives changes of word

For the shortcut map \(T\), suppose two distinct states \(T^i(n),T^j(n)\),
at times \(i,j\le K\), have the same next \(L\) parity symbols. The new
Lean module proves

\[
\boxed{2^{L+K}<3^K(n+1).}
\]

Thus an actual repetition crossing this explicit budget forces equality of
the two states. In particular, a doubled initial parity block of length
\(2L\) with \((4/3)^L\ge n+1\) forces \(T^L(n)=n\).
The words and their positions may vary in every application; the original
ordinary source stays in the bound. The asymptotic complexity consequence
is credited to Dubickas's existing theorem.

The [arithmetic note](ARITHMETIC_WORDS.md) also applies
Beukers--Schlickewei's classical two-variable unit-equation theorem. If a
prefix of \(N\) distinct accelerated odd sources uses only \(s\) primes,
including two and three, then

\[
N\le2^{16s+8}.
\]

This is a written deduction, valid for arbitrary valuation switches.
Finite prime support is therefore equivalent to eventual periodicity of
an ordinary orbit. The note tests how this rank budget interacts with the
parity-window budget and records why the available height envelope does
not yet bound the newly introduced primes. No novel priority is claimed
for the classical complexity or unit-equation mechanisms.

## 3. A physical constraint on any complete prefix-merger selector

Monks's theorem gives an actual representative of every ordinary merger
component in every nonconstant arithmetic progression. The
[physical-merger note](PHYSICAL_MERGERS.md) reconstructs the binary-modulus
case and retains the real-height cost of its inverse path.

It then proves in Lean a simultaneous separation theorem. If

\[
A=3^rB,\quad r\ge1,\quad B\text{ odd},\quad
2^H\mid A+1,\quad B>6^H,
\]

then \(T^a(A-1)\ne T^b(B-1)\) for **all** \(0\le a,b\le H\).
Unequal clocks and all positive erasure depths are allowed.

A written cofinal construction places these inputs in the shrinking marked
band. For its subfamily of binary height \(d=12H+16\), every physical
merger to an erased rising prefix needs

\[
\max(a,b)>\frac{d-16}{12}
\]

extra clocks after the two complete rising runs. All proper erased
prefixes are themselves smaller marked integers. The original sources also
have no forward descent through their entire binary-height horizon.
This removes a uniformly bounded continuation dictionary as a completion
strategy; it leaves an unbounded-clock selector and other merger
architectures open. It is not a family of Collatz counterexamples.

## 4. The exact probability law behind pressure

The [critical-tilt note](CRITICAL_TILT.md) gives the exact finite-word
relation between Tao's geometric law and the adjoint of square pressure:

\[
p(a)=2^{-a},\qquad q(a)=3/4^a,\qquad
q(w)=\frac{3^r}{2^{A_r(w)}}p(w).
\]

The derivative likelihood is a mean-one martingale under \(p\), but
converges to zero almost surely. Under \(q\), its logarithmic drift is
positive. The note proves a sharp exponential event-transfer threshold
and an exact bounded stopping identity at source exhaustion.

It also constructs the unique ternary stationary law of square pressure.
That law is singular with respect to Haar measure, with a full-measure
carrier of dimension at most
\(8\log2/(3\log3)-1<1\). On almost every point for that law, the finite
pressure columns grow exponentially and the Green function is infinite.
Every positive ordinary unit has a finite Green value. This identifies
the precise change of law and arithmetic transfer needed to use the
probabilistic literature in the pressure route.

The associated real random affine series has every positive moment below
one and no first moment. This is an exact model calculation. It does not
establish the corresponding first-moment statement about the ordinary
minimum \(m(n)\); that is the unresolved target in section 1.

## 5. Evidence map and next universal step

| File | Evidence in this packet | First unproved global input |
|---|---|---|
| `lean/SourceCollision.lean` | Seven public Lean theorems on actual shortcut windows and source heights | A forced collision crossing the budget; resulting cycles still require classification |
| `lean/PhysicalTailBarrier.lean` | Four public Lean theorems on shifted affine histories and bounded-clock separation | An unbounded successful smaller-marked-partner selector, or another complete rank |
| `ARITHMETIC_WORDS.md` | Written literature deductions; independently reviewed at a pinned file hash | A source-only restriction coupling prime growth and parity complexity |
| `ORDINARY_RENEWAL.md` | Written source-preserving antichain, tail, and moment criteria with PDU explicit | The critical ordinary first moment or its sufficient weighted transport estimate |
| `CRITICAL_TILT.md` | Written likelihood, stationary-law, entropy, and moment proofs; independently reviewed | An ordinary estimate after source exhaustion; random-law identities alone do not supply it |
| `PHYSICAL_MERGERS.md` | Primary backtracing reconstruction and written marked realizations of the checked barrier | Actual merger membership within the original source's height and rank budget |

The current Lean entry point is `lean/LiteratureAudit.lean`; its build
checks the two new modules and only their three necessary local imports.
The prior 25-statement packet and older packets retain their original
receipts. The primary papers are cited at the exact theorem interfaces in
each note. The [source refresh](../../reports/2026-11-22-literature-reframe/SOURCE_REFRESH.json)
records the later repository heads, without extending prior reviews to
unread later statements.

These attempts move the global question to explicit arithmetic or
source-preserving analytic inequalities. None of those missing inequalities
has been declared proved, and no finite search is used as a substitute for
the universal theorem.
