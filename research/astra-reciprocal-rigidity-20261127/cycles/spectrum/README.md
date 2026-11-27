# Collective lag and word-distance bounds

The positive Collatz problem remains open. This continuation of [the cycle arithmetic packet](../README.md) concerns the chronological shortcut parity word of an actual primitive positive cycle.

| Claim | Scope | Evidence |
|---|---|---|
| Strict all-shift inequality from the two physical numerator recurrences, at every proper shift | Any primitive cycle cut at its minimum, in the shared integer coordinates $X_i=N_i+d$ | End-to-end Lean declaration primitive_cycle_bound in [CyclicAllShift.lean](CyclicAllShift.lean), building on [AllShift.lean](../AllShift.lean). The standard rational-word formula identifies the common reduced $d$ in the written note. |
| At most $3(\log_23)k^2$ shifts with at most $k$ mismatches when $n\ge2k(1+\log_2(d(m+1)))$ | Any primitive positive rational cycle | [Finite Cayley graph and dyadic spacing proof](COLLECTIVE.md). The same note proves a linear lower quantile for ordinary cycles, and constructs critical rational controls with many shifts of at most four mismatches. |
| At least $\sqrt{n/\log_2 3}-O(\log n)$ insertions, deletions or substitutions from every finite mechanical factor | Entire ordinary period, arbitrary slope, intercept, cut and input length | [Written proof with denominator and source pins](MECHANICAL_DISTANCE.md). The clean-window cardinality, collision at actual integer states and numerical cutoff arithmetic compile in [FactorRigidity.lean](FactorRigidity.lean). |
| At least 522498 physical band crossings in every translated factor-three height grid | Any hypothetical nontrivial positive ordinary cycle | [Written transfer of the published threefold residence theorem](BAND_CROSSINGS.md). Its two numerical cutoff certificates compile in FactorRigidity.lean. |

The ordinary edit floor is 369788 uniformly in the period, rising to 894200757095011 from $n=2^{100}$. At the one critical period and weight treated by Weaver 223/v1, its larger fixed-count threshold transfers to arbitrary edits. The written proofs specify the imported Diophantine and finite-computation inputs. Neither the full Levenshtein alignment formalism, the Cayley packing argument nor the external first-exit theorem is imported as a Lean axiom.

Run the exact finite controls from this directory.

    python -B check_spectrum.py
    python -OB check_spectrum.py

The checker enumerates 585 primitive positive rational necklaces of length at most 12, verifies 1633 small-shift subgroup bounds and 1755 optimal edit alignments, and tests five long rational controls whose periods range from 45 to 9295. The checks certify the two pairs of explicit numerical cutoffs. The growing rough-denominator construction has a written proof. Bounded tests do not prove any asymptotic statement.

For a fresh Lean replay use the parent packet's driver with the modules CyclicAllShift and FactorRigidity, Lean 4.34.1 and mathlib d13f23b723b8a846827a245b89c10fc7d3f11612. Both modules passed with warnings as errors and autoImplicit disabled. The displayed proofs use only propext, Classical.choice and Quot.sound.
