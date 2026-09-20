## Continuation of #126; programme #121

**AUA-001--006 are PROPOSED pending independent mathematical review. No complete
Collatz proof, successful universal selector, or external priority claim.**

Parent: `7e996feb24cc5d8579d75b39e0b909ffc03b3bcb`.
This draft has not been published by its authoring session. The publisher
must append the actual child commit/tree and a separate publication receipt.

### Strongest source-level extension

For every k>=1 and s>=2, an explicit infinite family is rejected by the
exact previous selector at an odd H parameter, but the shorter odd-spine
companion merges directly. Put n=8^k u-5, Z=3^(2k-1)u, require
v2(Z+1)=s+3, b=(Z+1)/2^(s+3), and 3^s b=5 mod8. Then

    T^(3k+s+5)(n)=T^(2k+s+4)(2^(2k-1)u-1).

The old selector uses v=5 mod16 and reaches H((3^s b-1)/4), whose parameter
is odd and therefore outside its return guard. The new shadow bypasses this
entire all-parameter failure family. For k>=24 the entire original forward
arm stays above n. The new source is below n/2^(k+1), and a CRT specialization
has 3|n, hence no smaller pure ancestor at any depth.

Example: n=136948628003219711197179, m=4081387162304511,
T^79(n)=T^54(m)=487946288509306056429779, every displayed original iterate
exceeds n, and 2^25*m<n. A second d=3 resonance gives compression 2^(k+3).

### Systematic interfaces

A fixed-gap compiler supplies an explicit nonempty merging residue class
for EVERY positive integer gap in O(log gap) stages. Consequently every
finite parity word has a certified smaller-shadow subfamily. This does not
force a prescribed fixed input to satisfy the newly constructed guard.

An elementary universal merge-or-H entry retains the original smaller
source for every positive input. A complete countable affine-pair grammar
records every subsequent synchronous transition, including orientation swaps.
Neither is a finite-state termination proof. Core phase controls are retained.

The finite atlas completely classifies synchronous meetings through 18 tail
steps for shifts -5..11, with 12,270 uniform cylinder leaves, 52 isolated
positive meeting entries, and all frontiers retained. This is the whole
admissible odd-shadow menu for the k<=6 grid, not all shadows at arbitrary k.
Unequal-clock individual tail meetings are outside this atlas's completeness
claim; original prefix clocks remain independent throughout.

### Evidence

Generator/check passed normally and optimized. The separately implemented
verifier passed normally, -O and -OO, with -S isolation. It reconstructs
whole-word affine numerators, exact source cylinders, every uniform leaf and
isolated meeting; its gap compiler goes forward and its CRT solves for b.
It imports no generator/kernel/repository module. Twenty-four resealed
corruptions, five malformed witnesses and four invalid gap inputs are rejected.
An additional direct trajectory replay checks all 16,368 valid bounded pairs
in a smaller complete atlas and finds exact agreement on all first meetings.

The corpus includes 420 resonance families, 112 strict escape families,
267 gap cases, 505 arbitrary-prefix cases, 8,191 universal entries and 18,913
chart-row checks. All original-grid outcomes are retained. Compared on the
same 24,576 sources, the union with #126 has 18,197 certificates, adding
4,004 while preserving all 14,193 old successes; 6,379 remain unresolved.
This is not a convergence census or a comparison against every project rule.
The parent generator's exact blob and canonical grid hash are checked.

No full-checkout repository validator, remote CI, Lean build or independent
mathematical review was run. A combined-command time-limit interruption is
recorded separately from the subsequent successful individual reruns.
The semantic payload SHA-256 is
`ecc307df24e9e7efe2a745cd9a1fa36cc7fa6ebc897b3a7ce4dc6ff4db6d2183`.

All changes are additive research, experiments and reports. No parent bytes,
canonical mathematical status, main, licensing, settings or workflow change.
