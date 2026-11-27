# Coordinator's mathematical and execution review

**Partial results accepted for publication; universal Collatz closure not
established.** The accepted manuscript uses the ordinary shortcut map
throughout. The review separates finite kernel statements, written
deductions, imported hypotheses, and finite controls.

## Claims checked

1. The coordinator reconstructed the actual inverse progression, the
   recentering algebra, and the basin transfer. FinalProposal composes
   the two independently built map definitions through an explicit
   equality lemma. Its source positivity, strict smaller-multiple bound,
   divisibility and meeting all hold for every natural parameter. The
   final cover predicate remains an explicit argument of the conditional
   Collatz theorem. The printed equivalence confirms its full strength.
   [Independent review](critical/PROGRESSION_REVIEW.md)

2. The ballot proof uses the very same word that supplies the carry,
   rather than a separate abstract walk. The initial odd step survives
   reflection after the first positive barrier. The off-by-one term is
   b-h-1 among 2b-1 remaining positions. Equality at h=b gives no path.
   One word and fixed endpoint determine at most one source. The entropy
   bound has a strict rate below 1/32 in the stated range; its known
   lower witnesses have exponent at most 341/352, below 351/352.
   [Independent count](arithmetic/ROW_REVIEW.md)

3. In the three-band cycle argument the quarter-grid spacing compensates
   for the largest difference of additive corrections. Equality of the
   images would repeat a normalized successor, so order is strict. The
   least full odd cycle gives a single rank rotation and the exponent
   corrections telescope. The physical/normalized distinction is retained
   in the rational countercontrol and mixed-band polynomial. The full
   geometric assembly is written, with only its specified rank, arithmetic
   and ordinary-prefix lemmas claimed as kernel checked.
   [Scope audit](arithmetic/KERNEL_SCOPE_REVIEW.md)

4. The Evertse application uses collective primitive content and a positive
   signed row with no proper vanishing subsum. In the prefix, content
   divides the fixed n after the first odd step. In a completion it is a
   power of two dividing t, so the outside-prime product is exactly the
   claimed one. The complete literal carry absorbs its own outside
   primes; neither finiteness nor positivity makes this factor small.
   Constants are fixed before passing to a uniform limiting statement.

5. The first-hit minimum paragraph was corrected during independent
   review: a suffix with additional 1-to-2-to-1 laps must first be
   truncated at the first hit of 1. If that prefix has no odd input,
   its minimum odd input is undefined; the separate three-coordinate
   argument handles the asymptotic exclusion. The finite-search
   description example now checks the common merger clock as well as
   both hitting times.

6. The inverse composition search has an explicit coefficient cap that
   covers arbitrarily large even gaps at each of the sixteen odd depths.
   Its necessary ternary classes are a superset of all sources obeying
   the specified seventeen-predecessor height test. A separate ordinary
   progression proves sufficiency of the retained class. Neither the
   height cutoff nor the fixed terminal is dropped.
   [Independent enumeration](rows/DEPTH_REVIEW.md)

7. The escaping-path entropy estimate counts distinct ordinary states
   below one binary precision. It bounds the running height maximum,
   not a uniform spatial occupation count. It is consistent with slow
   superlinear escape and critical limiting odd frequency. The two
   factor-complexity estimates distinguish an all-clock subexponential
   height hypothesis from a sparse return subsequence.

The final literature comparison also computes the Vandermonde determinants
on the actual affine lift family. Both scale by the same set of parameter
differences, leaving only the known coefficient ratio. This elementary
calculation explains the missing saving in that particular determinant
attempt; it is not a no-go theorem for all arithmetic geometry.

The late fixed-center consequence was checked against the exact
RationalBasin source. Its color is membership in the 283/13 cycle
component, not convergence of rational numbers to ordinary 1. Congruence
modulo \(3^{K+1}\) transfers the legality and final ternary divisibility
of every inverse word of at most K odd steps. At the rational anchor
positivity and the proved minimality force its affine slope above one,
or above two for a terminal multiple. Increasing the ordinary center
then preserves the required exclusions. The compatible binary class
\(s\equiv379\bmod1024\) nevertheless gives
\(T^{11}(2s+1)=(729s+1213)/1024<(3s+1)/4\).
The quantifier is every K admits arbitrarily large centers, not one
center for all K. This written result was not added to the local Lean
theorem count.

## Reproducible root execution

The [Lean receipt](lean/receipt.json) is PASS. It contains exact source,
compiler, runtime library, runner and output hashes. The flags are
warnings-as-errors and one compiler thread. All eight project modules
were rebuilt into a new temporary directory. Five modules are new and
three are pinned dependencies. There are 43 new and 33 upstream selected
axiom reports. All reported dependencies are a subset of propext,
Classical.choice and Quot.sound. The failed draft of run_add was corrected
before the retained successful run; no failed log is used as proof evidence.
Existing Mathlib/package objects were reused at the recorded revision.

The [finite receipt](control-replay.json) is PASS. Each of five programs
ran normally and with optimization enabled, retained explicit guards and
matched its expected output byte-for-byte. These ten runs include:

* 7,813,124 eligible reverse exponent compositions through odd depth 16;
* all 125,476 balanced first-odd words through the recorded cutoff;
* an independent 125,476-composition count and 1,740 endpoint-threshold tests;
* 1,688 physical carry rows and 23,632 nonempty proper subsum checks;
* 8,191 binary words with 98,305 prefix-truncation checks;
* 2,272 small-source clock cells and 862 explicit row sources.

Counts describe finite test universes, not bounds on all Collatz starts.
The full symbolic claims have their separately stated proofs and
hypotheses. Additional targeted upstream checks are documented in the
late intake reports, without upgrading the sources' analytic conclusions.

## Scope and priority

The late heads contain overlapping finite-survivor, cycle-order and
one-octave results. The manuscripts now credit these. The concrete
ordinary progression is compared against specified earlier sufficient
anchors; no claim of a search through all possible prior certificates
is made. Source versions and current open premises are frozen in
[INTAKE.md](INTAKE.md).

The largest unresolved step remains pointwise. A different convergent
representative at every precision does not place the original exceptional
integer in the basin. A family of large rows at a decreasing threshold
does not refute an estimate at each fixed threshold. A high-endpoint
upper cannot oppose a lower family whose endpoints are eventually
smaller. The publication makes none of these substitutions.
