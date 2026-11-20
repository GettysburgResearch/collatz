# Critical boundary attack

**Collatz remains unresolved.** This packet pursued the critical exponent
one and an analytic continuation of the new single-factor-five merger
reduction. It includes an independent review of that reduction.

## Main result and dependency boundary

[CRITICAL_SINGULARITY.md](CRITICAL_SINGULARITY.md) proves the following
source-qualified synthesis. If a nonempty proper ordinary invariant set
\(K\) exists, then

\[
D_K(1+\epsilon)\asymp_K\epsilon^{-1},\qquad
B_K(1+\epsilon)\to\infty,\qquad
B_K(1+\epsilon)=O(\epsilon^{-1/2}).
\]

Here \(B_K\) is its actual tripling-boundary Dirichlet series. Thus both
series have abscissa one and diverge there, while
\(B_K/D_K=O_K(\sqrt\epsilon)\to0\). A normalized critical component
population loses both every fixed ordinary source and its separating
boundary. This is not a contradiction; it identifies the missing
source-persistent information in that proposed normalization.

The positive lower density input is the explicitly named September 2026
Mazur theorem, used as a source-qualified external dependency. The
advertised proof supplement has not been rebuilt here. The ordinary
tripling upper bound and the harmonic profile limit are separately pinned
to PR146 and PR155. The binary harmonic-divergence consequence was already
present in PR146; the note credits it rather than claiming a new endpoint
closure. Its metric-label and directed-energy statements are extensions
of that same mechanism.

## Single-slice continuation

[SINGLE_SLICE_ENERGY.md](SINGLE_SLICE_ENERGY.md) proves an exact two-query
comparison for the smaller defect \(d(f(5x),f(x))\) on odd ternary units.
It controls the adjacent classes \(4,19\pmod{45}\), with a fully accounted
harmonic odd-part sum. Extending this to all adjacent comparisons with
finite weighted multiplicity is still open. The conditional root descent
does not supply that extension by itself.

One exact ordinary transport also covers the two full classes
\(j\equiv2,4\pmod5\) of the sparse target \(a=54j+1\). The
remaining three classes retain their open propagation boundary.

During this pass, concurrent PR157 at
`64361ecca770092d6c8242dc6211e38818af2e50` supplied the stronger
[one-sided forward-five basin criterion](https://github.com/GettysburgResearch/collatz/blob/64361ecca770092d6c8242dc6211e38818af2e50/research/global-closure-20261120/merger.md).
The neighboring two-sided M5 proof is retained as a small independently
checked conditional proof, with no claim to be the latest strongest
merger requirement. The critical singularity theorem and local weighted
bridges here are separate statements; neither silently supplies the
physical forward-five premise.

[M5_REVIEW.md](M5_REVIEW.md) independently verifies M5-001 through M5-003
at the recorded SHA-256 pins and records two completed runs of its exact
all-cell checker. It does not verify the missing physical M5 mergers.

Run the local finite interface check with:

```sh
python -X utf8 -B research/closure-attacks-20261120/critical/check_single_slice_energy.py
```

The [receipt](single_slice_energy_receipt.json) records the affine cells,
source hashes and exact weight constants. The infinite analytic arguments
are the written proofs, not a conclusion of the checker.
