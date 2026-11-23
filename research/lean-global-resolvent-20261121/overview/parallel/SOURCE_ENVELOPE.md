# Exact source envelopes for complete certificates

## Result and remaining obligation

`lean/Collatz/SourceEnvelope.lean` proves an exact, attained maximum over **all literal prefix deletions of a supplied complete source certificate, with any replacement initial even run that strictly decreases the existing PR177 multiset rank**. The construction permits deleting an arbitrarily long prefix in one handoff. The target need not fit the intermediate source intervals.

An independent-clock merger theorem then lets any positive partner inside this maximal interval pay for the target, even when the partner and target reach their meeting value at different ordinary shortcut times. This enlarges the source interval available to the physical merger interface in PR180.

The complete `LowIntervalStep` is **not proved**. The final theorems retain an explicit universal merger or forward-entry selector as their hypothesis. They do not add an axiom or assume a new convergence witness for the source.

The new module has 25 public theorems. It and the audit compile under Lean 4.34.1 with `-j1 -DwarningAsError=true`. All 25 public theorem audits use only the standard axioms `propext`, `Classical.choice`, and `Quot.sound`, or no axioms. There is no `sorryAx`, custom axiom, or `native_decide` in this addition.

## Frozen inputs

The source induction and certificate language come from PR177, commit
`a0a0d76f91b4e3846c1b1f0706cad56cb6098317`, under
`research/lean-exact-witness-global-20261121/lean/Collatz/`.

The exact transitive dependency closure contains 14 project modules, plus the Lean-core import `Init.Data.Nat.Coprime`. `DEPENDENCIES.json` lists their paths, byte hashes, and build order. All 14 local dependency sources were compared byte for byte with that frozen git object. They are scaffolding for the new module; there is no need to copy the rest of PR177's branch history.

PR180's comparison interface was read at commit
`bfba8feaefb3d0910456cdd92d2afcf9e8785b4d`, specifically
`research/lean-wide-pass-20261122/lean/WitnessSynthesis.lean` and
`WITNESS_SYNTHESIS.md`. This new module has no Lean import from PR180 and does not alter it.

## Mathematical construction

Let the supplied complete certificate be

\[
q=q_0\xrightarrow{a_1}q_1\xrightarrow{a_2}\cdots
\xrightarrow{a_r}q_r=1,
\qquad 3q_{i-1}+1=2^{a_i}q_i,
\]

with every gap positive. The powered source is \(S=2^e q\), with \(e\ge1\).
PR177's rank is the multiset/list order on

\[
G(e,A)=\bigl(\{2e+1\}\text{ if }e>0\bigr)
\mathbin{\uplus}\{2a:a\in A\}.
\]

At the largest grade where the multiplicities differ, a strictly smaller multiplicity gives the smaller rank.

For a nonempty literal prefix \(W=(a_1,\ldots,a_k)\), define

\[
F_e(W)=\max\bigl(e,a_1-1,\ldots,a_k-1\bigr).
\]

Deleting that prefix leaves the **actual** suffix certificate of \(q_k\).
The maximal payable initial exponent of this suffix is exactly \(F_e(W)\).
For the empty-prefix option the maximal strictly smaller initial exponent is \(e-1\).

The envelope is therefore

\[
E(e,q,A)=\max\left(
2^{e-1}q,\quad
\{2^{F_e(A_{\le k})}q_k:1\le k\le r\}
\right).
\]

In Lean, `boost` computes \(F_e\), `crest` takes the maximum including a current source, and `envelope` replaces its empty-prefix option by the source halving. The recursive definitions use exact natural quotients at supplied certificate edges. The certificate hypotheses prove those quotients are the actual successors.

### Why the rank payment is exact

If the original exponent \(e\) is retained, deleting any nonempty prefix already gives a strict rank drop. If a deleted gap \(a\) pays for a larger exponent, the new initial grade is at most \(2(a-1)+1<2a\), below the removed odd-gap grade. Repeating this one-step argument proves every chosen maximal cut decreases the original complete rank.

Conversely, cancel the common literal tail from the rank comparison. If a proposed replacement exponent \(f\) exceeded \(F_e(W)\), its new grade \(2f+1\) would exceed both the removed initial grade and every removed gap grade. Its positive multiplicity at that largest changed grade would contradict a strict decrease. This is `literal_cut_run_bound`.

The key theorems are:

- `envelope_witness`: some literal split of the **original supplied word** attains \(E\), carries its actual complete suffix certificate, and strictly decreases the original rank.
- `envelope_maximal`: every other rank-decreasing literal cut with any replacement exponent has powered source at most \(E\).
- `literal_cut_interval_iff`: a target lies in the interval of some paid literal cut if and only if it is at most \(2E+1\).
- `low_envelope_witness`: if the original exponent is at most three and all source gaps are at most four, the maximizing suffix still has gaps at most four and initial exponent at most three. Exponent zero and an empty suffix are allowed.

The maximum is finite because the supplied word is finite; there is no bound on its length. It does not rely on enumerating all words or on checking a bounded set of residue classes.

**Scope of maximality:** the optimized class is literal prefix deletion followed by changing the initial even run. It does not include arbitrary inverse-prefix replacements, shortening an individual odd gap while retaining part of it, high-gap cofinal rewrites, or every possible lower-ranked source certificate. Those other rules can still enlarge a combined dispatcher's coverage.

## Target-changing transfer

Let \(T\) be the ordinary shortcut map,

\[
T(n)=\begin{cases}n/2,&n\text{ even},\\(3n+1)/2,&n\text{ odd}.\end{cases}
\]

The source-side induction hypothesis is exactly PR177's
`Hyp Interval (grades e word)`: every activated child comparison with a strictly smaller complete source rank is already available.

Under this hypothesis, `envelope_interval_rule` proves every positive integer at most \(2E+1\) belongs to the basin. Thus `envelope_merger_rule` accepts

\[
0<x\le2E+1,\qquad T^L(x)=T^R(t),
\]

and concludes that the target \(t\) belongs to the basin. The clocks \(L,R\) are independent. The partner may be even. Taking \(L=0\) gives ordinary target entry into the maximal interval.

The pointwise propositions are exactly:

```lean
def TargetHitsEnvelope (e q : Nat) (word : List Nat) (target : Nat) : Prop :=
  ∃ R, 0 < run target R ∧ run target R ≤ 2 * envelope e q word + 1

def TargetMergesEnvelope (e q : Nat) (word : List Nat) (target : Nat) : Prop :=
  ∃ partner L R,
    0 < partner ∧ partner ≤ 2 * envelope e q word + 1 ∧
    run partner L = run target R
```

`run` is ordinary shortcut iteration. No accelerated-clock equality is silently substituted for a physical merger.

## Concrete improvement: source 26 and target 31

The certificate \(13\xrightarrow{3}5\xrightarrow{4}1\) with \(e=1\) has source \(S=26\). The full list of maximally paid literal-cut sources is:

| Cut | Remaining odd core | Initial exponent | Powered source |
| --- | ---: | ---: | ---: |
| Empty prefix, halve source | 13 | 0 | 13 |
| Delete gap 3 | 5 | 2 | 20 |
| Delete gaps 3,4 | 1 | 3 | 8 |

Therefore \(E=20\), and the paid interval reaches 41. Target 31 closes immediately under the source induction hypothesis, using the actual child certificate \((e=2;[4])\). No target step is necessary.

This resolves the previously recorded failure of a particular synchronized payment calculation for this pair. That earlier failure did not rule out all source cuts. `example_envelope` and `example_interval_closes` check the exact computation and the induction transfer in Lean.

## Correction to the preceding carry-budget note

The previous checkpoint's `CYCLE_DEFICIT_FAMILIES.md`, section 7.1, treated
\(\max(e,\max W)-1\) as a necessary upper bound for the new even exponent. That is too restrictive when the old exponent \(e\) is retained.

For a **nonempty** removed prefix, the exact bound is

\[
f\le\max\bigl(e,\max_{a\in W}(a-1)\bigr).
\]

Consequently, if a synchronized construction prescribes
\(f=e+B-C\), its rank-budget requirement is

\[
C\ge B+e-\max\bigl(e,\max_{a\in W}(a-1)\bigr).
\]

The stronger earlier inequality remains a sufficient budget, but must not be described as necessary for every literal cut or as a global obstruction. The empty-prefix case separately requires \(f<e\). The q13/t31 calculation still shows that its specified synchronized route can fail; the new attained envelope proves another paid route succeeds.

## Exact open selector

`LowEnvelopeMerger` asks for a merger witness only for states satisfying all of:

1. `Certificate q word`.
2. \(1\le e\le3\), and every gap in `word` is at most four.
3. The target is odd and \(2^e q+1<t\le2(2^e q)+1\).
4. The target lies above the newly paid interval: \(2E(e,q,word)+1<t\).

It then asks for `TargetMergesEnvelope e q word t`. `LowEnvelopeEntry` asks for the stronger forward-entry witness instead.

The final proved chain is

\[
\texttt{LowEnvelopeEntry}
\Longrightarrow\texttt{LowEnvelopeMerger}
\Longrightarrow\texttt{LowIntervalStep}
\Longrightarrow\forall n>0,\ \texttt{Basin}\ n.
\]

The selector definitions impose no source-size bound, word-length bound, or orbit-clock bound. Neither selector is asserted as a theorem. Existing prefix, retained-even, boundary, and cofinal rules can continue to discharge parts of this domain; this new module does not encode all their exclusions into its selector.

The unresolved step is now target arithmetic: for every remaining complete low-word source and target above the exact paid envelope, construct a finite target entry or an actual bounded-partner merger, or supply an additional source rewrite. The source maximization theorem does not itself establish that such a target witness always exists.

## Verification receipt

- Version: Lean 4.34.1, commit `5045d0056413266e57c625dcd7c365b10e377c52`.
- Project dependency sources: 14, byte-identical to the frozen PR177 object.
- New Lean source: `lean/Collatz/SourceEnvelope.lean`.
- Public declarations audited: 25 theorems in `lean/AuditSourceEnvelope.lean`.
- New module build: exit 0, `-j1 -DwarningAsError=true`.
- Public audit build: exit 0 with the same flags.
- Actual commands, outputs and source hashes: the committed
  [fresh checkpoint-8 receipt](../../../../reports/2026-11-22-parallel-global/checkpoint8-lean.json).
- Build order and dependency hashes: [DEPENDENCIES.json](DEPENDENCIES.json).

The integrated fresh replay compiles all 14 exact source dependencies,
this module and its audit, and the three other new proof modules. Its
44 theorem audits include the 25 source-envelope theorems.
