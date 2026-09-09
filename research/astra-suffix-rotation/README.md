# Backward prefix rotation and a common integer rank

**No complete Collatz proof was obtained. ASR-001--008 are PROPOSED pending
independent mathematical review.** This is a new research attempt after the
review of PR106, not an amendment of its frozen proofs or an integration change.

The forward actual-prefix rank Gamma can spike when the selected displacement
is odd. Instead of requiring the next repetition of the word, this packet
rotates a suffix BACKWARD through an actual ordinary predecessor and uses
one new rank throughout:

    Psi(n)=(n+1)Gamma(n), Psi(1)=0.

[PROOF.md](PROOF.md) supplies the statements, proofs, failure cases and exact
unproved completion. [The experiment](../../experiments/X-ASR-001-suffix-rotation/README.md)
contains a finite implementation and a separately written reconstruction.

## Main theorem: a physical backward certificate without future repetition

Suppose w is an actual minimizing nonzero Gamma prefix at n, with displacement
d. Let v be a suffix of length r containing a odd steps, with affine map
T_v(x)=(3^a x+A_v)/2^r. If v3(d)>=a, then

    x=(2^r n-A_v)/3^a

is automatically a positive ordinary source and T^r(x)=n. Moreover

    Psi(x) <= (8^r/9^a) Psi(n).

Thus 9^a>8^r certifies strict common-rank reduction. This is an ALL-INPUT
sufficient guard, not a construction choosing a new source with a favorable
future. It handles odd displacements as well as even ones. The proof checks
integrality, positivity, physical parity and every competing Gamma candidate
through a rigorous upper bound; it does not assume that the rotated candidate
must itself minimize at x.

In particular every minimizing prefix ending in an odd step and with
3 dividing d has the actual predecessor x=(2n-1)/3 and an 8/9 reduction.
Together with the even baseline rule, EVERY source with a length-one
minimizer is covered. Longer high-odd-density suffixes are also covered.

Example: T(11)=17. Gamma rises from 36 at 17 to 48 at its backward witness 11,
but the SAME Psi falls from 648 to 576. Convergence of the witness would imply
convergence of the source through the displayed physical edge.

## A whole spike family is bypassed

For every H>=1,

    n=2*3^H-1, y=T(n)=3^(H+1)-1,
    Gamma(n)=4*3^H, Gamma(y)>n^(11/10),
    x=4*3^(H-1)-1, T(x)=n, Psi(x)<=(8/9)Psi(n).

Both the original source and its spiking successor are prime to 3. Removing
multiples of 3 therefore does not remove Gamma spikes. The new backward rule
does handle every member of this family immediately. It does not establish
that every resulting witness converges.

## The attempted universal normalizer is explicitly refuted

The bounded normalizer tests all forward endpoints through the baseline
Gamma evaluation window and all suffixes of all minimizing words. Every
accepted step lowers Psi; every call is finite. On 2..8192 it finds 7470 forward
reductions and 303 additional backward-only reductions, leaving 418 inputs.
These are local certificate counts, NOT a convergence census or percentage
of Collatz solved.

The failure is not only finite: for every L>=2 the input 2^L-1 has its unique
Gamma minimum at the baseline, and EVERY first L-1 forward step increases Psi
above its initial value. This exact normalizer returns UNRESOLVED on the
entire family. The proof controls all Gamma candidates, including the
unprescribed future. It does not exclude other merging diagrams or longer
adaptive rules.

Naively combining old and new ranks is also false: the old Gamma-decreasing
edge 11->17 and the new Psi-decreasing reverse edge 17->11 form a two-cycle.
All accepted transitions in this packet use Psi, without such mixing.

## What would complete the proof

ASR-008 gives the least-Psi exceptional-component argument: a finite physical
lower-Psi merger for EVERY n>1 would prove Collatz, including cycle exclusion.
The tested normalizer does not provide that coverage. **ASR-Q1 remains OPEN:**
construct complementary guarded reductions and prove their successful
selection, not merely termination of a search that can return UNRESOLVED.

The rank also has cubic-scale sublevels and summability threshold s>1/3.
This is bookkeeping for the new rank, not an improved survivor exponent.
No transported-mass or unsafe-return estimate is claimed here.

## Exact source and review boundaries

- Main base: `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`.
- Gamma source: PR106, `7b7471ea0e7b359a2ac46fb1e6aff269331509c3`,
  `research/astra-linear-frontier/prefix-rank/PROOF.md`, APR-001--003;
  blob `4b1a3c5f22bdae7fd901d408c878361aa28c335c`.
- Independent parent review: PR114,
  `65235530e9cf4dda1c5850421b16b7189a491f36`,
  `reports/post-integration-2026-09-08/CLAIM_MATRIX.md`.
- PR116's pending integration is not changed or assumed merged.

Necessary Gamma arguments are rederived in PROOF.md. No external theorem,
formalization or large certificate is a premise; no external priority claim
is made. Both checking implementations have the same author. The new packet
needs independent proof review and does not inherit the parent verdict.
