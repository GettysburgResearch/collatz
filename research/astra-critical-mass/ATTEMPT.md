# Attempt log and exact end-to-end gap

**Status:** completed research attempt, not a completed Collatz proof.
All new theorem claims remain PROPOSED pending independent review.

## What was actually attempted

The starting objective was the ordinary survivor-mass bottleneck from PRs #87
and #88, not a new finite Collatz census. I first removed an avoidable
odd-core logarithmic loss and retained the critical exponent with a little-o
or logarithmic-mass target. I then specified the first-passage map, derived
its exact affine endpoint fibers, and tested the proposed source/endpoint
anticorrelation rather than assuming it.

The pilot initially appeared to show overrepresentation of future survivors.
Much of that comparison was explained by a deterministic support effect:
first passages from above Y land in (Y/2,Y], not uniformly in [1,Y]. After
correcting the baseline, the displayed finite-horizon biases are mostly close
to one. That is ordinary mixing behavior, not the additional polynomial
anticorrelation the current exponent-race recurrence requires. No
asymptotic disproof follows from these finite observations.

## Direct global-certificate attack

A positive summable weight satisfying Lw<w would prove Collatz by summing over
any hypothetical backward-invariant exceptional set. This route does not
require an external predecessor bound. I tried to construct such a weight.

The first candidate, n^(-s) times bounded-above-and-below or subpower corrections, is ruled out
by long *ordinary* all-odd paths from 2^k b-1 to 3^k b-1. This is an exact
pointwise obstruction, not a failed numerical search.

I then used the arithmetic weight

    w0(n) = 3^v3(n+1)/(n+1)^2.

It is summable and gives exact contraction on endpoint classes 0 and 2 modulo
3. It fails on class 1 because the even inverse can acquire arbitrarily large
3-adic valuation. To repair that failure, I summed every even inverse ray:

    W_a(y) = sum_{j>=0} a^j w0(2^j y),   1<a<2.

This is still summable and handles *every* even edge exactly. It is therefore
a genuine infinite-arithmetic-state repair, not another fixed residue table.

The repair nevertheless fails on the explicit positive ordinary family

    u_h = (3^(4h+2)-1)/8,
    z_h = T(u_h) = (3^(4h+3)+5)/16.

The inverse branch contributes mass of order 1/z_h, while W_a(z_h)=o(1/z_h).
The ratio L W_a/W_a is unbounded. The same phenomenon survives every fixed
block length and every fixed verification floor. The proof in T-ASTRA-005 is
a new all-length statement about this candidate family; it does not refute
all possible arithmetic weights.

## What remains of the original full-proof attempt

Instead of stopping at the failed two-part repair, I retained every transported
inverse history in the killed Green series

    V_K = sum_{j=0}^K (65/64)^j L^j w0,
    G_K = sum_{y>=2} V_K(y).

A uniform bound on G_K is sufficient for a complete proof. The source weight
has an elementary analytic tail bound, so finite-time G_K can be enclosed
including *all* positive integer starts, not just an enumerated range.
The exact computation encloses G_256 in (8.6140,8.9619).

This is the point where the attempt stops: I have not proved a bound uniform
in K. The finite-time source-tail enclosure grows with K at a fixed source
cutoff. The apparently stable finite-source contribution is not a proof of
uniform stability of the infinite-source Green series.

## Q-ASTRA-001 — next concrete theorem to attack

Prove, for the explicit w0 and lambda=65/64, that

    sup_K G_K < infinity.

The working numerical target G_K<=16 for every K is open. Any finite uniform
bound is enough. A sufficient, stronger tail estimate is a summable bound on

    (65/64)^k * sum_{n>=2, tau(n)>k} w0(n).

The time-dependent survivor condition must be physical, not a replacement by
an independently sampled parity sequence. Such a bound has not been supplied
by the first-passage pilot, the power-like weight, or the dyadic envelope.

A promising next construction would aggregate transported affine forms rather
than only v3(n+1) and even rays. The failed family identifies the first missing
form: after an odd inverse, terms of the form 2^j(2y-1)+3 appear. Repeated
transport changes both the offset and the modulus. A finite set of forms may
again be insufficient; any truncation must have a proved summable remainder.

The exact compiler in FIRST_PASSAGE.md provides a way to test these candidates
without pretending that endpoint residues alone preserve ordinary mass.
An alternative route remains the critical little-o/logarithmic-mass estimate
from T-ASTRA-001, conditional on the imported predecessor theorem.

## Review order and strongest uncertainties

Read PROOF.md Sections 2, 4, 5, and 6 first: the killed boundary at 1,
nonnegative summation, the elementary source-tail bound, valuation stability
on the ordinary ray, and the fixed-block extension are load-bearing. Then
check the critical endpoint theorem and the endpoint fiber compiler.

The exact finite checks have two separately written implementations, but both
were authored in this session. This is implementation independence, not an
independent research-agent or human mathematical review. No full Lean build,
external large certificate, broad repository validator, or new workflow was run.

No general external priority claim is made. The elementary critical-exponent
bridge may be familiar; the pointwise and valuation-envelope obstructions
need a dedicated literature comparison before novelty is asserted.

## Integration boundary

The branch starts directly from main at
9704bcf1ff33cc9e2b729e0c40137a1e55b95397. It is not stacked on the unmerged
Mazur import. External and source-PR references are pinned in SOURCES.md.
Only a new research directory and a new bounded experiment directory are
added. No canonical registry status, existing source claim, main-branch file,
workflow, repository setting, or another contributor's PR is modified.
