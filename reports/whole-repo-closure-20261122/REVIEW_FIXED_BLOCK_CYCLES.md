# Independent review: effective fixed-block cycle theorem

Reviewed source: `EFFECTIVE_FIXED_BLOCK_CYCLES.md`.
SHA256: `7c581f9a622bafd37bb0b67ab834376a65cde6e0150d8014a3c71afc77f71a63`.
Review type: independent mathematical proof inspection, not a compiler replay.

The main theorem is sound within its stated one-parameter fixed-block scope.
I checked the following critical points.

1. The fixed rotation after a minimal prefix product among the proper prefixes
   makes every rotated prefix at least the total multiplier Lambda, including
   the wrap. Hence every suffix multiplier is at most one. Constant blocks
   (lambda=1) cause no exception.
2. The repeated-block affine formula and the suffix-product numerator formula
   are exact. The bound B uses absolute fixed-point coefficients, so expanding
   blocks and negative fixed points do not invalidate it.
3. After the complete multiplier is at most1/2, every positive integral cycle
   source lies in the finite range1..floor(2B). The full denominator remains
   present; no individual-factor divisibility inference occurs.
4. Grouping equal positive rational exponential bases gives either an exact
   identity or an effective dominant-root exclusion after a finite cutoff.
   Two distinct identity starting values for one nonconstant schema would
   force the complete multiplier to be identically one, so at most one occurs.
5. Final integrality forces the actual shortcut parity word: a first illegal
   parity creates an odd numerator over a positive power of two, and later
   formal branches cannot cancel that denominator. Positive starting values
   keep every legitimate intermediate state positive.
6. Unique two/three factorization excludes Lambda=1 when a nonempty block
   varies. The entirely empty parameter case and constant schemas are handled
   separately. Rotating a genuine cycle loses no positive ordinary realization.

I found no unsupported implication in this written classification argument.
The result does not show that arbitrary cycles or a nonperiodic carry program
belong to finitely many fixed schemas. It therefore cannot alone close the
unbounded carry dispatcher studied in this parallel lane.
