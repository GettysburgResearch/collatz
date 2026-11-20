# Frozen inputs and attempted closure

Inspected on 2026-11-20. The checkout base is main at
ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a. These are snapshots; later
changes to the same pull requests do not inherit the review below.

| PR | Full head | Use in this packet |
|---|---|---|
| [146](https://github.com/GettysburgResearch/collatz/pull/146) | 6863d298187af8b2619efbf78cc4b0aa8e627393 | One-sided convergence criterion, thin adjacent classes, directed return paths and prior directed counting bounds. |
| [151](https://github.com/GettysburgResearch/collatz/pull/151) | 02a9f6ad17e5f1904cb4ff806fd0217d199e8437 | Previous recursive ordinary merger work; its successful families do not give universal coverage. |
| [152](https://github.com/GettysburgResearch/collatz/pull/152) | 2391a9c1e4a7f77233b951d2eb6da92e76652e7c | Actual source-weight transport, sign reversal and the open occupation estimate. No fresh-input averaging is used here. |
| [153](https://github.com/GettysburgResearch/collatz/pull/153) | eb04a5d79020cefa0ba46794095b5766c5ff66a4 | Finite binary-run cores and their cap-exit limitation. |
| [154](https://github.com/GettysburgResearch/collatz/pull/154) | fe40bb6f88e8094290ef01207d9bf7c4798d35d0 | Prime-height gcd estimate, dispersion and earlier elementary prime-support consequences. |
| [155](https://github.com/GettysburgResearch/collatz/pull/155) | 92f499b9d340d1ff8cc643c3eef3477d61b477c1 | Ordinary Dirichlet coercivity OD1--OD4 and the endpoint logarithmic loss. |
| [156](https://github.com/GettysburgResearch/collatz/pull/156) | c5cb84502c7289705d59a8781a65fd845b9b6b14 | Ordinary essential spectrum, source-dependent arithmetic obligations and bounded two-arm guard obstructions. |

The sources are linked at their exact full heads in the individual notes.
Their claims retain their proposed or source-qualified status. We have not
rerun their historical Lean builds or large computations.

## Final refresh of PR146

Before publication we fetched and inspected the newer PR146 head
`e238c63a5d57f96bb063b7472498d1977df51951`, updated during this session.
It adds reverse-basin criteria, Mersenne certificate reductions and stronger
bounded-rank restrictions. Its depth-two classification overlaps our
independent derivation. The [refresh comparison](LATEST_146_COMPARISON.md)
records the exact overlap and why the new source does not close either the
prime-creation or finite-boundary-moment gap. The earlier directed-return
and coercivity dependencies remain pinned to the original heads above.
No refreshed Lean build is represented as executed by this packet.

## Primary comparison for prime support

The authors' versions of [Paper137](https://rstation.ai/problems/collatz/papers/137),
[Paper138](https://rstation.ai/problems/collatz/papers/138), and
[Paper159](https://rstation.ai/problems/collatz/papers/159) were read.
Paper138 already contains consecutive prime-power charging and coordinate
maximum deletion. They are explicitly credited and rederived where needed.
Paper137 treats the stronger parameter of multiplicative rank; the new height
scale is compared only on the prime-support subclass. No external numerical
cycle exclusion or verification range is used in our peak theorem.

The first exploratory tail improvement duplicated this prior work and was
not promoted as new. The retained synthesis uses short windows at a maximum,
where the actual division total is affordable.

## What did not close

1. A spectral-gap proof is already obstructed by convergent ordinary states
   in PR156. Weak convergence or finite clocks cannot be exchanged with
   the missing strong or all-time conclusion.
2. PR152's fixed source measure has an actual positive drift at a later
   return despite negative initial drift. Replacing transported mass by a
   fresh sample would omit the identified covariance.
3. The new circulation is a weighted sum of valid finite directed cycles.
   It gives exact balance, not absence of a separating cut. The available
   permanent-failure upper bound gives a divergent endpoint majorant.
4. Known convergence depth two does not control the paired target clock.
   The residual Mersenne family is an exact ordinary problem and remains
   unproved for all parameters here.
5. The stabilized-label laws at arbitrary large exponent J have not been
   shown to imply the small-exponent laws. Dividing an input by three can
   lose ordinary integrality; the existing inverse-cone compiler has a
   different source quantifier.
6. The prime-support lower requirement, binary-run growth and a
   multiplicative-energy upper bound are compatible. None supplies the
   opposite bound needed for a contradiction. Shifted factors n+1 obey
   different return identities and cannot inherit the unshifted estimate.

## External density and moment inputs

The one-sided functional Liouville specialization at exponent 0.84 uses
the published Krasikov--Lagarias predecessor count as pinned by PR146.
The general circulation and the elementary peak theorem do not require it.

We also checked the stated scope of Mazur's
[positive lower-density predecessor theorem](https://www.proofatlas.ai/formalizations/positive-lower-density-collatz-predecessors/):
it concerns each fixed positive target prime to three and does not prove
density-one convergence to 1. Its proposed endpoint consequence is already
credited in PR146. It is not a new dependency or theorem of this packet,
and no external formalization was rebuilt in this session.
