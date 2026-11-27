# Complete-denominator windows and limits of bounded repair catalogues

**Collatz remains OPEN. This is an incomplete final proof proposal.** The
re-evaluation supplies an exact local characterization of the whole cycle
denominator, a source-dependent ordinary descent family, a concrete Lean
countercontrol to a broad anchor strategy, two S-unit finiteness theorems,
and a quantitative zero range on the original integer trace. The missing
universal inference remains visible in the final Lean theorem.

Use the ordinary shortcut map
\[
 T(n)=\begin{cases}n/2&2\mid n,\\(3n+1)/2&2\nmid n.\end{cases}
\]
`Good n` means that an actual finite iterate equals 1. `FirstTower w r`
chooses the least positive base supporting a bad power of three, then the
first bad exponent on that base. Smaller bases support good towers and
earlier powers on the same base are good. These are the original pinned
ordinary definitions, unchanged in this pass.

## What was proved and where it stops

| Result | Mathematical content | Evidence and boundary |
|---|---|---|
| Whole denominator from local windows | For a supplied bounded-cycle rank word, two families of small decoded residues are equivalent to complete denominator divisibility. Each failing word has a certificate fixing only `O(log p)` rank letters. | Finite algebra kernels in Lean; the full criterion and asymptotic bounds are written and independently reconstructed. Universal failure of every nontrivial admissible word is open. |
| Native descent from phase +1 | Every phase-1 anchor transfer into a strictly smaller ternary base already has a forward endpoint below the original base. Explicit progressions exist at every initial exponent and positive exponent gain. | Lean. The progression varies the base; it does not cover a supplied arbitrary base. |
| A convergent source outside the anchor catalogue | `3645=3^6·5` reaches 1 at clock 31, but its full immediate lower cone cannot be reached by a phase-1 positive anchor or a negative periodic phase of magnitude at most 136, with any preperiod or lap count. | Lean, including the unrestricted terminal powers of two and earlier same-base exponents. The phase +2 extension of native descent is not claimed. |
| Finite signed-phase reach | At a fixed odd base, a fixed finite set of signed integer periodic target phases provides immediate lower-cone certificates at only finitely many ternary exponents, allowing arbitrary anchors, preperiods, laps and final halvings. | Written consequence of Evertse–Schlickewei–Schmidt, with scale lemmas in Lean. Further odd moves or unrestricted chains are outside this statement. |
| Finite template-bank reach | At a fixed odd base, a finite bank of nonempty parity templates used in a bounded number of powered blocks reaches the lower cone at only finitely many exponents. Repetition counts are unrestricted, and rational or zero template centers are allowed. | Written S-unit proof; ordinary affine and telescoping identities in Lean. The block count must be fixed. |
| Integer trace zero range | `E_b(eps)=0` for `b≥2^278` and `9/50≤eps<1`. A hypothetical nontrivial cycle's previous residual shell narrows to one binary digit. | Reconstructed simple-path census and exact rational computation, with finite kernels in Lean. The explicit floor and endpoint cap use Bařina's external exhaustive computation. The small-threshold range remains open. |

## The whole-denominator mechanism

For coprime odd-period and shortcut-clock counts `p,h`, put
`D=2^h−3^p>0`. A candidate rank word supplies a rational array
\[
 (S^h-3)Z=c,\qquad S^p=2I,
\]
where `S` advances the sorted rank and doubles at its seam. Physical letters
are `c_r=2^(2−k_r)`, with `k_r` in `{0,1,2}`. For a physically legal word,
integrality of `Z` is exactly the complete ordinary cycle denominator test.

Take neighboring rational approximants on opposite sides of `h/p`, with
offsets `v_1,v_2`. Their exact identity is
\[
 q_2v_1+q_1v_2=p.
\]
The two finite differences `(S^v_i−I)^m_i Z` remove the large nearly
geometric part. Their residues can be decoded from short past windows. If
every decoded value lies in the proved small interval, every edge congruence
is an integer equality and the entire difference array is integral.

The seam identity is the arithmetic step that makes two filters sufficient.
In the quotient by `D`, the two difference operators generate the unit
ideal, because their shift product equals 2 and hence differs from 1 by a
unit. Their positive powers also generate the unit ideal. Integrality of
both differences therefore recovers integrality of the original array,
including when `D` is composite. Passing one filter alone is insufficient.

Wu–Wang's logarithmic-form bound allows `O(sqrt(log p))` parallel windows,
each of that length, using `O(log p)` letters in total. The windows can be
separated by `exp(O(sqrt(log p)))` temporal steps; this is not a claim of one
contiguous short window. A new argument would have to force a failed window
in every nontrivial ordinary least-disagreement candidate. The pair of
filtered values need not distinguish all ranks, so a naive counting argument
does not supply that inference. [Full criterion](cycle/README.md)

The [wide rational controls](cycle/WIDE_CONTROLS.md) have both actual circle
orders, width between three and four, and positive mismatch density at every
nonzero shift, at arbitrarily large upper convergents. They have denominators
greater than one. Thus those order and mismatch properties cannot alone
shrink the cycle to the narrow bands excluded in PR209.

## What the anchor and S-unit results rule out

For a positive anchor `a` with `T^h(a)=1`, the standard lift has
\[
 x=a+2^h4^dt,\qquad y=a+2^h3^dt,
 \qquad T^{h+2d}(x)=T^h(y).
\]
If `x=3^r w` and `y=3^s b` with `b≤w`, the arithmetic and actual anchor
clock imply `3^r<w`. If `b<w`, the common endpoint itself is below `w`.
For a negative anchor reaching periodic magnitude `C`, the corresponding
necessary bound is `3^r≤Cw`.

These bounds cover arbitrary preperiods but need separate treatment of the
zero-preperiod case if the destination has unrestricted powers of two. The
S-unit equation theorem supplies that treatment and yields the finite-phase
result. The concrete source 3645 strengthens the diagnostic: it converges,
yet the specified whole immediate anchor catalogue misses it. This failure
of a proposed catalogue is not a counterexample to Collatz.
[Ordinary results and complete phase theorem](closure/README.md) ·
[Closed full-cone control](closure/AnchorControl.lean)

For successive forward blocks, the [bounded-template theorem](formal/BOUNDED_TEMPLATE.md)
uses a different sparse equation. After dividing by the cumulative
multiplier, the endpoint identity has boundedly many S-unit terms. A minimal
vanishing subsum containing `w3^r` remains nondegenerate after normalization.
Every other term has its 3-adic valuation bounded above, while the source
valuation grows with `r`. Finitely many projective ratios therefore allow
only finitely many exponents. This covers arbitrary repetitions of a fixed
number of templates, including templates with nonintegral fixed points.
It leaves unbounded block complexity and general two-arm meetings open.

## The retained-source trace estimate

On one simple ordinary path above `2^71`, an exact parity-tail recurrence
gives a sum of reciprocals of odd departures below
`593690/10^6 < 3/5`. It counts each low-odd-count site through its own actual
later endpoint, and charges at most the finite clock length for sites too
near the end. There is no independent resampling after a stopping time.

The bound makes relative carry smaller than `9/50`. Bařina's published
coverage below `2^71` and shortcut peak below `2^139` imply that a path ending
above that peak avoids the entire lower interval. The exact statistic
`E_b` starts its terminal sum at `ceil(sqrt b)`, giving the stated
`b≥2^278` onset. Only the cited maximum-holder trajectory, not the exhaustive
interval computation, was replayed here. The recurrence and zero-range upper
do not use the source-qualified renewal floor F.

An escaping unit `a` would force the earlier positive lower bound at
`eps=1/(3a+1)`. That can be far below `9/50`. Raising the certified floor
indefinitely would require bounded forward orbits for every new smaller
gate, which is part of the unresolved question. Restarting farther along the
same hypothetical ray does not remove inverse paths through its original
gate. [Proof, exact recurrence and external-input boundary](diagonal/README.md)

## Final Lean proposal and reproducibility

[FinalProposal.lean](formal/FinalProposal.lean) contains the closed anchor
countercontrol and the all-exponent physical descent progressions. Its final
universal theorem explicitly takes `remaining : FrontierMerger`. The
unchanged predicate asks for an actual ordinary merger at each surviving
frontier. This hypothesis has not been established. Importing the independent
cycle and trace kernels does not prove it.

The fresh root run rebuilt ten project modules, including four unchanged
dependencies, and checked 83 selected transitive axiom inventories: 35 in
the six new modules and 48 in their dependencies. All used only `propext`,
`Classical.choice` and `Quot.sound`. The project cache started empty; pinned
Mathlib/package binaries were reused. The external analytic developments,
asymptotic applications, full S-unit proofs and exhaustive computation were
not rebuilt. [Exact formal scope](formal/README.md) ·
[Source ledger](SOURCES.json) ·
[Root review](../../../reports/astra-global-closure-20261124/round11/ROOT_REVIEW.md)

From a complete checkout with the pinned Lean 4.34.1 and Mathlib revision:

```sh
python -B research/astra-global-closure-20261124/round11/check_lean.py \
  --lean /absolute/path/to/lean \
  --mathlib /absolute/path/to/mathlib4 \
  --report-dir /absolute/path/to/lean-reports
python -B research/astra-global-closure-20261124/round11/check_controls.py \
  --report-dir /absolute/path/to/control-reports
python -X utf8 -B tools/validate.py --receipt /outside/checkout/validation.json
```

The three finite arithmetic programs were replayed in normal and optimized
Python, with byte-identical outputs. Repository validation requires a clean
complete checkout and checks repository integrity, not the open theorem.
The [intake](../../../reports/astra-global-closure-20261124/round11/INTAKE.md)
pins the new PR192, PR197, PR208 and PR209 sources and distinguishes the
168-PR metadata inventory from selected mathematical review.
