# Full numerical separation for arbitrarily many cyclic packets

Read [FULL_NUMERICAL_SEPARATION.md](FULL_NUMERICAL_SEPARATION.md).

This extends the prior PR185 two-packet coefficient family to arbitrarily
many disjoint congruence packets and arbitrary embedding parameters. It
proves a bound on the **whole numerical gcd** after complete polynomial
cancellation. For all permitted parameters,
`gcd(D_pol,Q_0(3)) | (2^(ar)-3^(br))(3^b-2^b)`, independently of the
individual pairwise coprime packet periods. The final reduced denominator
is greater than `sqrt(D_pol)`; its surviving logarithmic fraction tends
to one as the total packet length parameter grows.

The family has unbounded packet count and primitive period, polynomial
cancellation of proportion tending to one, and an arbitrary-floor
near-critical version. Every member is excluded from being an integer
cycle. The source family and its exact polynomial cancellation are credited.
No reduction of arbitrary Collatz cycles to this family is supplied.

The full numerical arithmetic core, including derivation of factor
coprimality from the base and index hypotheses, is formalized in
[HomogeneousRepunits.lean](../rigidity/lean/HomogeneousRepunits.lean) and
[PacketGCD.lean](../rigidity/lean/PacketGCD.lean). The construction,
primitive-word argument, and complete polynomial gcd remain written proofs.

[check_full_numerical_separation.py](check_full_numerical_separation.py)
replays nine selected examples, with three direct complete polynomial gcds,
6,268 rational shortcut steps and 6,268 ordinary finite-realizer steps. A
shared-prime control checks that the proof retains overlapping prime powers;
outside-domain controls show where the coprime and disjoint-support
hypotheses matter. Normal and optimized Python outputs agree exactly.
