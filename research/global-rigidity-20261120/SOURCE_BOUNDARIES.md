# Source boundaries and a correction to the previous comparison

**Research status: PROPOSED; Collatz remains OPEN.** This pass starts from
main `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`. The following branches are
external, frozen inputs, not silently incorporated into the accepted
baseline. A source's mathematical claim and a successful execution of its
code are different evidence events.

## Corrected comparison with PR145

PR150 at `ef4022fa5ae43dd943ecca0b7c84d69af624c5c9` contains an elementary
growing-popcount theorem: for every `0 < c < 1/sqrt(2)`, almost all of `N`
pairwise distinct consecutive positive odd orbit states have more than
`c sqrt(log_2 N)` set bits, with
the stated quantitative exceptional bound. Its comparison doubled the
coefficient of an **elementary consequence in PR145's README**. It must
not be read as the strongest asymptotic threshold in that entire branch.

At PR145's frozen head `dd245a712f985909f541590e3f6c179b7ba011e4`, the
following stronger, non-elementary routes already appear:

| Exact source | Relevant statement | Consequence for the comparison |
| --- | --- | --- |
| [MANTISSAS.md](https://github.com/GettysburgResearch/collatz/blob/dd245a712f985909f541590e3f6c179b7ba011e4/research/binary-run-occupancy/MANTISSAS.md) | A published two-logarithm bound yields power-rate mantissa discrepancy and allows a leading-word length proportional to `log N`, with the proportionality restricted by that bound. Its binomial counting argument then gives a logarithmically growing run threshold. | The elementary square-root-logarithm threshold is not an improvement over every prior threshold. |
| [MELLIN_PHASE.md](https://github.com/GettysburgResearch/collatz/blob/dd245a712f985909f541590e3f6c179b7ba011e4/research/binary-run-occupancy/MELLIN_PHASE.md) | Summable ordinary drift gives an asymptotic irrational rotation on a hypothetical escape; quantitative discrepancy is developed using the stated logarithmic-form and orbit-counting inputs. | Neither the existence of the limiting phase nor its quantitative use is new in this pass. |

The primary agent inspected these exact files. The comparison sentence in
[PR150](https://github.com/GettysburgResearch/collatz/pull/150) was corrected
on 2026-11-20 and read back exactly. Its commit and tree were not changed.
This is a qualification of the comparison, not a retraction of the
elementary theorem or a claim to have newly proved the imported
transcendence estimates. The earlier source text remains preserved at its
frozen commit.

## Current merger input is stronger than the previous head

PR146 was inspected at `7d04c4dd756cfe495eb3eee78eba35a99085cd2a`,
particularly `research/upper-bit-mergers/THREE_RAY.md` and
`THREE_RAY_SMALLER.md`.
That head already closes the earlier finite odd tripling-defect
propagation obstruction. In particular it contains a bypass based on

\[
T^2(3(16s+1))=4(27s+2),\qquad T(18s+1)=27s+2.
\]

Its stated multiplicative-window criterion and failure-count lower
bounds must not be presented as new results here. The new merger work
starts instead with a two-arm ordinary section, checks which arm carries
the hypothetical least nonconverger, and retains actual physical clocks.
The same frozen `THREE_RAY_SMALLER.md` already proves the absence of a
uniform ordinary-edge bound in its smaller-tripling proof graph. The
new horizon theorem concerns its explicitly specified two-arm floor,
meeting, section, and immediate-halving interface; a generic claim to
have newly discovered every bounded-clock obstruction is not made.
The new packet's local written arguments and finite replays do not amount
to a fresh execution of PR146's external formal build.

## Operator normalization and prior work

The operators in this pass act on `l2` of **all positive odd ordinary
integers**, including multiples of three. They use the accelerated odd
map and its exact derivative weights. No source is killed. The proof
identifies the operators with those of PR143 and PR144 at their exact
heads; it does not transfer a conclusion from a different space by
analogy.

| Source | Inspected scope | Boundary |
| --- | --- | --- |
| PR143 `41a408e5e617fb4e65142485f6f3ff3e6ef6c408`, `research/pressure-decay-20261031/PROOF.md` and `ENERGY.md` | Ordinary weighted-composition operator and fixed-space/energy route. | The new approximate-spectrum construction does not exclude actual fixed vectors on unknown components. |
| PR144 `df756794e1d8de5cabff148ef433df505e3b68b4`, `research/pressure-diagonal-20261031/PROOF.md` and `DISSIPATION.md` | Fourth-order diagonal moment and proposed dissipation estimate. | Essential spectrum at the unit circle does not refute the particular moment-decay target. |
| PR149 `92c0129e794dde3ec55ceec470a12d51ba3f7e2f`, `research/asymptotic-inverse-operator/ASYMPTOTIC_OPERATOR.md` | A physical inverse-tail operator and its finite-time norm obstruction. | Its space, weights and claim differ from the ordinary derivative-weighted operators here. No blanket superiority claim is made. |
| [Neklyudov, arXiv:2106.11859](https://arxiv.org/abs/2106.11859) | The primary paper's analytic-function operators, fixed/eigenfunction examples and index discussion. | Hardy/Bergman and monomial-pushforward statements are not substituted for the present ordinary weighted composition operator. |
| [Leventides and Poulios, arXiv:2010.12987](https://arxiv.org/abs/2010.12987) | The primary paper's shortcut-map Koopman setup and sequence-space formulation. | Composition-operator language and column-fiber norm calculations are established methods. No general priority claim is made for them. |
| [Béhani, arXiv:2303.03203](https://arxiv.org/abs/2303.03203) | Primary abstract: hypercyclicity of specified weighted Bergman operators independently of Collatz. | Abstract-level comparison only; its full proof is not imported or newly reviewed. |

## Rational witnesses and ordinary sources

Real density of rational periodic points is classical:
[Misiurewicz and Rodrigues, *Real 3x+1*, Theorem 4.2](https://doi.org/10.1090/S0002-9939-04-07696-8).
Both the arithmetic author and the primary agent inspected the
[author-uploaded full text](https://www.researchgate.net/publication/346000553_Real_31),
including the explanation that these periodic points obey the parity
rule. The new notes claim the explicitly proved joint local tuning and
denominator estimates, not the underlying one-coordinate density fact.

The comparison with PR149's
`research/forward-inverse-defect/RATIONAL_CYCLES.md`, at the head above,
is similarly narrow. That source combines binary/ternary observations
with a lower floor for every cycle phase and a bounded maximum gap after
fixing the observations. The new construction prescribes an arbitrarily
small real neighborhood and can add finitely many prime-power tests;
its maximum gap is unbounded. Neither theorem is asserted to dominate
every feature of the other.

No changing family of rational cycles is an ordinary divergent orbit.
No finite rational certificate, ordinary trajectory census, source audit,
independent AI reconstruction, or repository validation establishes the
universal Collatz conjecture.
