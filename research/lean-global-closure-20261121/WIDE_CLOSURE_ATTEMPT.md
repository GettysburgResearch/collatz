# Whole-repository attack: exact continuations and the remaining global step

**Full Collatz convergence remains OPEN.** This continuation attempted three
global closing arguments in parallel. It produced complete arithmetic
interfaces for actual inverse histories and certificate rewrites, together
with a uniform pressure-tail estimate. It did not obtain a complete recursive
dispatcher, a smaller partner for every source, or an upper bound excluding
all survivors.

After this source checkpoint, a further live refresh found new work in
PR177, PR180, PR183, and PR185. The subsequent
[literature continuation](LITERATURE_CLOSURE_ATTEMPT.md) derives a new
global weighted bound for the canonical inverse potential under its pinned
population hypotheses, and develops a typed interval continuation. Its
written proofs and independent review are separate from the compiled core
packet described below; no full closing implication is claimed.

## What was examined

The starting inventory contains all 143 pull requests returned by the
repository's all-state, updated-time listing, observed on 2026-11-21 at
21:50 UTC. It includes older PRs with recent commits. The complete metadata
snapshot is [preserved in the report](../../reports/lean-global-closure-20261121/wide/pr-inventory.json).
The resident research map, results catalog, proof guides, open obligations,
and scoped errata were read before selecting the source families.

This is an inventory of every PR and a targeted investigation of the
mathematical interfaces, **not** a claim to have independently checked every
proof in every branch. The three detailed notes identify actual source files
and full frozen commits:

| Global route | Inspected source families | New result and remaining question |
|---|---|---|
| Complete supplied-certificate induction | PR146,147,164,174,177,181 | Arbitrary asynchronous source/target words can preserve the complete supplied tail and decrease one common multiset. A successful rule must still be chosen for every comparison. |
| Smaller ordinary merging partner | PR146,182,184, plus the prior PR175 foundation | Exact inverse extraction continues after the ternary reserve is exhausted. The complete canonical reserve menu is characterized by actual binary-horizon mergers. A smaller partner is not guaranteed. |
| Source-dependent pressure or survivor bound | Resident orbitwise Mellin results; PR143,144,155,163,176,178,180 | The entire infinite ordinary pressure tail is exponentially small after its first positive period. The moving low-source core still needs an upper bound; cycles remain a separate issue for this route. |

The new forced section is retained as a valid upstream input. The previous
band work remains in [BAND_ATTACK.md](BAND_ATTACK.md); its proof and scope are
not replaced by this wider comparison. In particular, a marked visit can
overshoot its original source, and a changing family of successful marked
sources does not produce a smaller partner for a fixed earlier integer.

## 1. Every actual inverse history has an exact carry continuation

Use the shortcut map and let \(a_t(x)\) count its odd inputs before time
\(t\). The new core Lean proof establishes the exact identity

\[
\left\lfloor\frac{T^t(x)}{3^{a_t(x)}}\right\rfloor
=\left\lfloor\frac{x}{2^t}\right\rfloor
\qquad(x,t\in\mathbb N).
\]

Suppose an actual history satisfies \(T^t(x)=3^P v+y\), and write
\(a=a_t(x)\). Define

\[
d=(a-P)_+,\qquad
W=3^{(P-a)_+}\left\lfloor\frac{v}{3^d}\right\rfloor,
\qquad Y=3^P(v\bmod3^d)+y.
\]

There is a nonnegative ordinary \(u\) with

\[
x=2^tW+u,\qquad a_t(u)=a,\qquad T^t(u)=Y.
\]

The converse reconstruction is also proved. Thus the formula covers **all**
actual inverse histories, including \(a>P\), with the exact ternary remainder
retained. It does not replace the missing high-count cases by a modular
point. The nonnegative source is constructed by subtraction only after the
quotient theorem proves that subtraction is legal.

The retained coefficient is positive exactly when
\(3^{(a-P)_+}\le v\). When it vanishes, the residual endpoint is the entire
original endpoint and the extracted source is the original source. The
continuation is still exact, but then supplies no descent by itself.

## 2. The canonical reserve menu has a complete physical characterization

For fixed clocks \(h,t\), the complete reserved-splice relation is equivalent
to

\[
T^t(x)=T^h(n),\qquad 2^h\le n,\qquad 2^t\le x.
\]

This is an iff for every ordinary input and both clocks. The proof constructs
the source decomposition
\(n=2^h3^s v+r\) with \(r<2^h3^s\) and
\(v=\lfloor n/(2^h3^s)\rfloor>0\); the child is an actual inverse of
\(T^h(r)\) with the corresponding odd-count budget. Hence allowing the
maximal quotient and canonical remainder loses no merger within the two
binary horizons.

The further [maximal-reserve theorem](MAXIMAL_RESERVE_REDUCTION.md) collapses
that complete parameter menu to **one reserve per source clock**. Choose the
unique \(s\) with
\(3^s\le\lfloor n/2^h\rfloor<3^{s+1}\). Its canonical quotient is one or two.
The proof shows that every partner satisfying its binary horizon necessarily
has an odd count within this maximal reserve. `single_reserve_complete`
proves existence, uniqueness, and completeness for every positive source
quotient. Scanning smaller ternary reserves is unnecessary within this
precise covered class.

The theorem provides completeness within its exact domain. It does not assert
that every \(n>1\) has a smaller partner within that domain. That unmodified
universal premise already fails for small ordinary inputs. A later smaller
history can be valid while having zero retained coefficient.

There is also an exact accounting identity for inverse padding. If
\(T^k(M)=n\) and \(a=a_k(M)\), then

\[
2^{k+h}\le M\quad\Longleftrightarrow\quad3^a2^h\le n.
\]

Thus prepending a large ordinary ancestor cannot repair a meeting clock
already beyond the original source's binary horizon. The extra clocks do
not create free precision.

See [INVERSE_CARRY_CONTINUATION.md](INVERSE_CARRY_CONTINUATION.md) and the
formal modules [InverseBudget](CollatzGlobalClosure/InverseBudget.lean) and
[ReservedMergerCompleteness](CollatzGlobalClosure/ReservedMergerCompleteness.lean).
The total one-reserve construction is in
[MaximalReserve.lean](CollatzGlobalClosure/MaximalReserve.lean).

## 3. A complete-certificate compiler with arbitrary parent phases

The source comparison uses \(\psi(S)=2S-1\), a known source
\(S=2^e q\), and its supplied complete certificate for \(q\). The new compiler
allows three arbitrary finite words: a child-source word \(W\), a child-target
word \(V\), and an actual parent-target word \(P\). Neither target clock is
required to equal the source clock, and the parent path may cross its initial
odd run.

The exact count, clock, and affine-correction identities force every child
division to be legal. If every gap of \(W\) is at most \(e\), the child
retains the entire original tail and replaces the initial even grade
\(2e+1\) by finitely many grades at most \(2e\). PR177's common multiset order
therefore decreases, regardless of the new word's length or the child's
ordinary size.

This is an unbounded rule compiler, not a finite list of extra residue
classes. It still needs an actual successful selector. The investigation
also checked why two tempting completions do not work: prepending inverse
words does not change an interior reset endpoint, and a ratio-five paired
path is not automatically a psi-comparison path.

### The entire power-of-two terminal case is now covered in the induction

[TerminalReset.lean](CollatzGlobalClosure/TerminalReset.lean) supplies a direct
rule for every power-of-two source, including every supplied gap-two padding
tail at one. For \(e\ge4\), replace \(S=2^e\) by
\(M=3\cdot2^{e-1}\). The explicit certificate \((1,4)\) for three gives the
complete child certificate with initial even run \(e-1\), followed by
\((1,4)\), followed by the unchanged supplied terminal tail. Its new grades
are

\[
2e-1,\quad2,\quad8,
\]

all strictly below the removed grade \(2e+1\). Meanwhile
\(T(2^{e+1}-1)=3\cdot2^e-1=2M-1\), so the lower-ranked child psi query
reconstructs the parent target. The four cases \(e=0,1,2,3\) close by literal
ordinary trajectories.

The checked theorem `terminal_case` therefore covers **every** terminal
power-of-two source in the common induction. The child has larger ordinary
size and a longer supplied convergence certificate; the multiset still
decreases. This removes a whole infinite terminal family from the dispatch
obligations. It is an induction step that uses the smaller-certificate
hypothesis, not a stand-alone proof that every Mersenne number converges.

The initial-odd-run specialization has a proved all-word limitation at
source eight; the scope is specifically that odd-child specialization, not
all possible powered-child rules or all Collatz proofs. The general compiler
has an explicit checked example beyond the initial parent phase. The exact
finite search is retained as discovery evidence, not as a premise of any
universal theorem.

See [ASYNC_CLOSURE_ATTEMPT.md](ASYNC_CLOSURE_ATTEMPT.md) and
[AsynchronousReset.lean](CollatzGlobalClosure/AsynchronousReset.lean).

The subsequent [general dispatcher attempt](NONTERMINAL_DISPATCH_ATTEMPT.md)
keeps an entire nested target as one recursive query, so that no newly
returned certificate is silently reused without a rank bound. It derives
exact positive-context rules, the remaining `(6s+1,s)` comparison, and the
zero-context carry that still lacks a decreasing rank. The fixed general
powered-child extension is disproved by the certified source `2^4*7`.
These follow-on identities are written mathematics, not additional Lean
declarations counted in the 16-unit build.

## 4. The infinite pressure tail is controlled; the core remains open

For the accelerated odd map \(U\), let \(J_q(x)\) be the derivative of the
actual \(q\)-step branch. PR144's pinned positive inverse-population tables
give an exact trace for

\[
D_q=\sum_{x>0\text{ odd}}\frac{J_q(x)^4}{U^q(x)^2}.
\]

Let \(B_q\) be the part using the first positive odd representative of each
residue modulo \(3^q\). A nonnegative telescoping estimate gives

\[
0\le D_q-B_q\le\tfrac12(3/5)^q.
\]

The rational finite weighted kernel and the exact scaling are proved in
core Lean. The infinite-sum passage and the application of the older
population identities are written deductions, not imported Lean axioms.
The detailed note keeps this distinction explicit.

A sharper localization connects this estimate to the inverse-history
theorem. If \(L_q(x)\) is the total shortcut time of the first \(q\) accelerated
odd steps, the exact quotient identity gives

\[
U^q(x)\ge3^q\quad\Longleftrightarrow\quad x\ge2^{L_q(x)}.
\]

The contribution of this entire unexhausted-source part satisfies the written
all-source estimate

\[
\sum_{\substack{x>0\text{ odd}\\x\ge2^{L_q(x)}}}
\frac{J_q(x)^4}{U^q(x)^2}
\le\tfrac32(3/5)^q.
\]

The formal rational kernel includes the corresponding head-plus-tail bound.
The population substitution, increasing-limit passage, and identification
of the accelerated clock are explicit written steps. The complementary
part has exactly the exhausted quotient that stops the constructive reserve
reduction, so the two routes isolate the same source precision boundary.

This does not bound \(B_q\) by \(O(q^2)\), the proposed estimate that would
exclude divergent ordinary trajectories in that pressure program. Every
fixed source eventually contributes inside the moving core, so the tail
bound does not discard a hypothetical fixed exceptional input. Excluding
additional positive cycles is also not supplied by that proposed estimate.

See [FULL_SOURCE_TRACE_ATTEMPT.md](FULL_SOURCE_TRACE_ATTEMPT.md) and
[PeriodicTraceTail.lean](CollatzGlobalClosure/PeriodicTraceTail.lean).

## Reproduction and status

All new formal modules, including the arithmetic foundation port, use core
Lean 4.34.1. The eight PR177 dependencies are copied without source edits and
are checked against both SHA-256 and their source Git blob identifiers.

```sh
python -B build_wide.py --lean /path/to/lean-4.34.1/bin/lean \
  --output /fresh/lean-output --receipt /fresh/build.json
```

The compiler uses fresh project output, warnings as errors, and explicit
axiom reports. It does not use `sorry`, custom axioms, `native_decide`, or
unsafe proof evaluation. Repository integrity checking is a separate gate.
The successful execution records belong in the accompanying report, with
the actual source hashes and commit boundary.

The next closing target is a successful comparison dispatcher that can
consume a genuine part of a known source certificate, or an ordinary upper
estimate controlling the exhausted core. Neither is presumed true as an
input to this checkpoint. No theorem of full Collatz convergence has been
proved here, and no scholarly priority claim is made for the arithmetic
identities without a separate literature comparison.
