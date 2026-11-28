# A certifying semiprime representative for every ordinary source

**SOURCE-QUALIFIED total reduction; finite witnesses independently replayable.**
This is a constructive consequence of the sparse transfer theorem. It does
not assume Collatz convergence. Every positive integer can be assigned an
easily factorable semiprime together with two finite genuine paths to a
common ordinary value. The search has no proved practical or polynomial
bound. Its mathematical termination uses the same named analytic inputs as
[semiprime sufficiency](SEMIPRIME_SUFFICIENCY.md).

## 1. A family with an entirely integer membership test

Let \(b(n)=1+\lfloor\log_2 n\rfloor\), the binary length. Put

\[
 \mathcal B=\{n=pq:\ p<q\text{ prime},\quad b(n)\ge4,
                         \quad b(n)<p,\quad4p\le b(n)^2\}.
                                                               \tag{1}
\]

All conditions in (1) are exact integer conditions. The smaller prime can
be found by at most \(b(n)^2/4\) trial divisions. The verifier may use any
correct deterministic primality method; the supplied finite consumer uses
ordinary trial division and makes no efficiency claim for that choice.

This family lies inside the earlier sufficient family \(\mathcal S\).
Indeed \(\log n<b(n)\log2<b(n)<p\). Also \(n\ge2^{b(n)-1}\), and
\(\log2>2/3\) gives

\[
 \log n\ge(b(n)-1)\log2\ge b(n)/2\qquad(b(n)\ge4).
\]

Hence \(p\le b(n)^2/4\le(\log n)^2\). The elementary inequality
\(\log2>2/3\) follows, for example, from strict convexity of \(1/x\) in
its integral on \([1,2]\).

Containment alone would not make \(\mathcal B\) sufficient. The necessary
extra check is that **every semiprime supplied by the original
Matomäki–Teräväinen interval theorem belongs to \(\mathcal B\) eventually**:
its smaller factor is between \((\log x)^{1.09}\) and
\((\log x)^{1.1}\), whereas \(b(n)\asymp\log x\). Both strict lower and
upper inequalities in (1) follow as \(x\to\infty\). The per-binary-residue
upper bound for \(\mathcal S\) also bounds its subset \(\mathcal B\).
The complete incidence proof therefore runs unchanged with \(\mathcal B\)
as the target population. No unproved uniformity in the interval theorem
has been added.

In particular every fixed positive target \(v\) prime to three has
\(\gg_v X/\log X\) predecessors in \(\mathcal B\) through \(X\). The
fixed-target version of the transfer, rather than only its component-union
version, is used: the source prefixes stay above \(v\) until their actual
merger, so later visitation of \(v\) transfers exactly. Positive predecessor
density comes from the original ordinary-map theorem at target \(2v\).

## 2. The total mathematical procedure

Given \(n>0\), first follow the actual shortcut map while the current value
is divisible by three. Repeated halving eventually exposes an odd value;
its next shortcut value is prime to three. This produces a finite certified
path \(n\to v\) with \(3\nmid v\), without assuming convergence.

Now dovetail the following finite searches for \(k=1,2,\ldots\):

1. Enumerate and factor all members \(s\in\mathcal B\) with \(s\le2^k\).
2. Replay each such source for \(k\) shortcut steps.
3. Stop at the first verified visit of \(v\).

The preceding theorem supplies some fixed \(s\in\mathcal B\) and some
finite visit time \(t\). For every \(k\ge\max(b(s),t)\), this witness is
among the inspected candidates and dates. Thus the search halts. It outputs

\[
             n\longrightarrow v\longleftarrow s=pq,
             \qquad s\in\mathcal B,                            \tag{2}
\]

with both displayed paths finite and actual. This is an ordinary integer
certificate, not a residue match, a generic two-adic merger, or a simulated
fresh parity stream. It is compatible with the Haar-null multiplier theorem:
the representative is found by a source-dependent arithmetic search, with
no bounded word-cell or uniform clock promise.

The implementation exposes a bounded search so experiments terminate with
an explicit unresolved list when limits are insufficient. The unbounded
dovetail above is the total mathematical procedure; a bounded failure is
not a failure of its existence theorem. The candidate, visit-time and onset
bounds are not controlled uniformly in the input by this argument.

## 3. Why this is a full-proof reduction

If every member of \(\mathcal B\) reaches one, the representative \(s\)
in (2) reaches one. Its future state \(v\) also reaches one, because the
known cycle is forward invariant. The original \(n\) then reaches one.
The converse is immediate. Therefore

\[
 \boxed{\quad\text{Collatz}\quad\Longleftrightarrow\quad
                   \text{every }s\in\mathcal B\text{ reaches one}.\quad}
\]

The same sparse-transfer argument gives the upper-relative-density-one
version within \(\mathcal B\). The reduction identifies a precise family
on which a new dynamical theorem would settle the conjecture. It does not
prove convergence on that family. Its factorization is already easy; the
remaining work is orbit closure.

## 4. Finite certificate consumer

[semiprime_representative.py](semiprime_representative.py) checks primality,
the exact product and binary-length inequalities, every positive ordinary
step, both path origins, and their common endpoint. The finite command
records all actual states in its JSON output, so an independent consumer
can replay each certificate directly.

The receipt records the chosen source and step limits. These examples test
the finite interface; they neither prove the source-qualified existence
theorem nor turn the search into a polynomial-time algorithm.

## 5. Prior sufficient sets and the scope of this construction

Sufficiency by actual orbit merging is an established notion. [Monks, Monks, Monks and Monks, arXiv:1204.3904v2](https://arxiv.org/abs/1204.3904v2) construct sufficient sets of arbitrarily low asymptotic density and recall the earlier sufficiency of every arithmetic progression. The recent [Paper 227 (November 25)](https://rstation.ai/problems/collatz/papers/227/v1) gives a different decidable sparse family of directed tripling implications; the selected implications remain unproved. This note does not claim that sparse sufficient sets or terminating finite merger searches are new in general. Its specific input is the explicitly factorable semiprime family in (1), its RH-free short-interval supply and positive relative predecessor density, and the actual two-arm certificates obtained from that supply.

## 6. Fresh finite Lean interface

[SemiprimeRepresentative.lean](SemiprimeRepresentative.lean) proves seven public roots: forward preservation of reaching one, iterate preservation, transport across an actual two-clock merger, positivity of family members, the precise universal-convergence equivalence under the explicit representative-existence argument, five exact semiprime memberships, and the seven actual merger witnesses. The witnesses use kernel decision, without native evaluation or an added axiom.

The existence theorem in Sections1–2 is supplied as an argument to the logical consumer; it has not been silently postulated as a Lean axiom. Its analytic proof remains source-qualified and written. All seven roots were freshly compiled and then imported into a separate full type/axiom audit using Lean4.34.1 and pinned Mathlibd13f23b723b8a846827a245b89c10fc7d3f11612. Only Classical.choice, Quot.sound and propext occur. The [runner](check_semiprime_representative.py) and [receipt](../../reports/astra-collision-factor-bridge-20261128/semiprime-representative-lean.json) record the exact hashes. Pinned compiled dependencies were reused; no cold dependency build or LeanChecker replay is claimed.
