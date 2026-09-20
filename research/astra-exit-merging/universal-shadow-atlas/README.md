# Universal shadow atlas and strict escape families

**PROPOSED pending independent mathematical review. No complete Collatz proof.**
Parent: PR #126, `7e996feb24cc5d8579d75b39e0b909ffc03b3bcb`.
Programme: #121. Read [the complete statement and proof](PROOF.md).

## Strongest new source-level result

For arbitrary k>=1 and s>=2, there is an explicit infinite family of inputs
n=8^k u-5 for which the exact previous selector ALWAYS returns OUTSIDE_RETURN,
but the shorter odd-run companion m=2^(2k-1)u-1 merges directly. Its guard is

    Z=3^(2k-1)u, v2(Z+1)=s+3,
    b=(Z+1)/2^(s+3), 3^s b=5 mod8.

Then T^(3k+s+5)(n)=T^(2k+s+4)(m). The previous selector's H parameter is the
odd number (3^s b-1)/4. The new comparison bypasses it; it does not claim to
continue that failed pair. For k>=24, the entire displayed original arm stays
above n, and m<n/2^(k+1). The family has a CRT specialization n=3 mod12,
so no smaller pure ancestor exists at any depth.

Example: n=136948628003219711197179, m=4081387162304511, clocks 79/54,
meeting 487946288509306056429779; the entire original forward arm exceeds n.
The full theorem also has a second d=3 resonance, with compression 2^(k+3).

## More systematic tools, with their different quantifiers

* Every positive source has an elementary finite entry to a merger or H(C)
  while retaining a smaller ORIGINAL source. This repackages an existing
  odd-run identity; it does not prove successful continuation of H.
* A complete **countable**, not finite-state, grammar describes the next step
  of pairs (3^d y+b,y), including exchanges and isolated numerical equality.
* Every fixed positive gap has a constructive residue class on which the
  pair merges, with O(log gap) tail length. The generated guard need not hold
  at an arbitrary failed pair.
* Every finite parity word admits an explicit smaller-shadow SUBFAMILY.
  This is template-complete construction, not coverage of every source.
* The finite atlas classifies every synchronous meeting through 18 steps
  for the declared shifts d=-5,...,11, retaining both whole cylinders and
  isolated positive meetings. Every frontier is retained. No all-time
  completeness or universal successful selector is inferred.

These interfaces make the remaining failure conditions explicit without
turning the universal coverage problem into a proved statement.

## Evidence and relation to the previous selector

The atlas contains 12,270 uniform cylinder leaves and 52 isolated meeting
entries across 17 shifts. The new kernel gives 10,481 successes on the
24,576-input comparison grid. It is not meant to replace the previous kernel:
keeping all old successes and adding the new ones yields **18,197** successful
certificates, **4,004 additional**, with **6,379** still unresolved by this
union. This is not a convergence census or a comparison against every other
programme in the repository.

See [comparison receipt](../../../reports/astra-exit-merging-05/comparison.json)
and [experiment instructions](../../../experiments/X-AEM-005-universal-shadow-atlas/README.md).
The new mathematical corpus includes 420 resonant families, 112 strict-escape
families, 267 fixed gaps, 505 arbitrary-prefix cases, all entries from 2 to
8192, and bounded checks of every affine-chart row. Large controls include
k=200, s=128, 256-bit gaps, and nonperiodic words.

The independent implementation does not import the generator/kernel.
Typed artifacts and deliberately resealed corruptions are checked. Same-author
implementation diversity is not independent mathematical review. Full-checkout
validation, external Lean and remote CI are not claimed.

## Next question

Can the exact failure constraints for several different original shadows be
shown incompatible for a least exceptional root? A larger atlas is useful
only when it helps formulate and prove such a statement. Universal entry,
finite cylinder completeness and finite successful examples do not establish
that incompatibility.
