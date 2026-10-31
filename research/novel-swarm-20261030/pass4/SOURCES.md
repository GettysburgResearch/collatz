# Source pins, literature overlap, and independence limits

All new statements in this pass are **PROPOSED, self-audited**. There is no
external novelty-priority claim, proof-assistant build, or independent-agent
review. The source comparison is targeted, not a complete literature audit.

## Frozen repository inputs

Parent PR #140: `6bee3183ff7f29f2e20ca88ab94bc7745c1af602`.
Its first-hit definitions and pointwise boundary are in
[pass 3](../pass3/ORDINARY_BOUNDARY.md), Q1--Q5. The tail bound used here is
reproved directly: for odd x>=65537, summing
`x^-2 < (1/2)((x-1)^-1-(x+1)^-1)` gives a tail below `1/131072`.
The present full-pressure decreases are independently regenerated; they do
not assume that a decrease in the old truncated profile survives its tail.

The prior finite-record reduction is
[FINITE_RECORDS.md at the parent](https://github.com/GettysburgResearch/collatz/blob/6bee3183ff7f29f2e20ca88ab94bc7745c1af602/research/astra-three-routes/pass3/FINITE_RECORDS.md),
T-A3-651--653. It supplies the simple-path/record-window architecture and the
conditional physical stopping argument. The present change is to pack the
ACTUAL record sources within that short translated window, rather than
bounding their number by its integer cardinality. This yields beta squared.
The old finite-path terminal correction is retained, not rediscovered.

The orbitwise Mellin tradition and the orbit-versus-basin distinction are
also explicit in
[ORBIT_MELLIN.md at the parent](https://github.com/GettysburgResearch/collatz/blob/6bee3183ff7f29f2e20ca88ab94bc7745c1af602/research/astra-three-routes/pass2/ORBIT_MELLIN.md).
No claim here upgrades an old proposed statement to accepted status.
WINDOWS.md supplies its own elementary proof instead of depending on an
unreviewed combination of those statements.

## External overlap found during this pass

**Manuel Garcia and Fabio A. Tal, A note on the generalized 3n+1 problem,
Acta Arithmetica 90 (1999), 245--250, DOI 10.4064/aa-90-3-245-250.**
[Primary PDF](https://matwbn.icm.edu.pl/ksiazki/aa/aa90/aa9033.pdf).
The primary paper was inspected, including visual checks of its compression
argument. Uniform translated sparsity and common-clock collision-free
compression are not new discoveries of this pass. Our finite-simple-path
boundary removal and elementary all-width constant are stated explicitly
for use by the pressure and record arguments.

**u/lyapunov_weaver, A power improvement for uniform Collatz interval
compression, rStation `collatz_28`, version 3 (2026).**
[Primary manuscript](https://rstation.ai/problems/collatz/papers/28/v3).
Search-indexed primary manuscript text and its associated primary discussion
were inspected; direct full-page retrieval was unreliable. The manuscript
states stronger related interval-compression estimates, including an entropy
threshold treatment and a power improvement. This pass does NOT assert a
complete independent audit of that manuscript, its constants or its review
labels, and imports none of those theorems as a dependency. In particular,
`19/20` is not presented as a new best sparsity exponent. The manuscript also
credits David Leen's 2026 uniform-sparsity appendix (Zenodo DOI
10.5281/zenodo.23252397); that source was identified, not fully inspected.
The explicit proof here deliberately avoids a dependency on those recent
sources. No priority claim is made for the elementary compression method.

**Olivier Rozier and Claude Terracol, Paradoxical behavior in Collatz
sequences, arXiv:2502.00948.**
[Primary text](https://arxiv.org/abs/2502.00948), Definition 1.2 and the
following Coefficient Stopping Time discussion; Section 2 concerns parity
remainder order. The conjecture that ordinary stopping time equals
coefficient stopping time for n>=2 would make every simple no-descent prefix
have only its initial coefficient record. Our finite grid indeed has only
one record in this regime. The general record theorem is therefore not
empirically tested on a known nontrivial pre-descent record sequence, nor is
that conjecture assumed. Multiple-record tests use full simple prefixes that
may descend. No other theorem or numerical bound from this source is used.

## What is actually contributed relative to the parent

The proposed new deductions are uniform averaged vanishing of normalized
first-hit pressure, certified decreases of its FULL infinite-source value,
source-persistent summable pressure drops, and the beta-to-beta-squared record
count with its conditional stopping interface. An ordinary V(n)=3n control
prevents averaged vanishing from being mistaken for pointwise vanishing.
These conclusions are not asserted to be literature-first results.

The parent collision upper-bound target E5, pointwise pressure vanishing,
universal coefficient stopping, and nontrivial positive-cycle exclusion all
remain unresolved. No step treats a sparse individual orbit as its basin.
