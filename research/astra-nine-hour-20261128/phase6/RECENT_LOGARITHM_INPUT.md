# A recent logarithm theorem that changes the cycle comparison

The new cycle argument in [Fourfold odd spread](../cycles/phase6/FOURFOLD_ODD_SPREAD.md)
uses a specific recent external theorem. Its mathematical statement, the author's
formal evidence, and this pass's incomplete independent replay have different
statuses. The distinction is material because this input crosses the coding
threshold, whereas the older effective bound does not.

## The exact imported statement

Gregory V. Chudnovsky, *Irrationality exponents of logarithmic numbers: Values,
quotients, and graded approximation*, arXiv:2610.28079v1, was submitted on
20 October 2026. Theorem 11.1 states that for multiplicatively independent
positive rational numbers a,b, the ordinary irrationality exponent of
log(a)/log(b) is between two and three. In particular, for gamma=log(3)/log(2),
every epsilon>0 admits a positive, generally ineffective constant c_epsilon with

    |gamma − A/p| >= c_epsilon p^(−3−epsilon)

for every integer A and positive integer p. Equivalently, its Corollary 11.5
gives the homogeneous two-logarithm exponent 2+epsilon on the coefficient
height. Multiplying or dividing by p changes the exponent by one; the two
conventions must not be interchanged.

[Primary version and submission history](https://arxiv.org/abs/2610.28079v1)
· [Theorem 11.1 and its proof](https://arxiv.org/html/2610.28079v1#S11)
· [Source distribution](https://arxiv.org/src/2610.28079v1)

For comparison, the earlier Bondareva–Luchin–Salikhov 2018 theorem has the
effective exponent 4.116201 for the linear form in log(2), log(3), and an integer
constant. Setting that constant to zero gives the ratio exponent 5.116201.
The actual printed theorem, rather than the paper's title about log(3), was
checked. The older bound remains appropriate where effective constants matter.
[Publisher's primary record and full text](https://www.mathnet.ru/eng/cheb619)

Chudnovsky's further preprint arXiv:2611.30820v1, submitted 23 November 2026,
states an ineffective exponent n+epsilon for an integer constant plus n
multiplicatively independent rational logarithms. Its homogeneous specialization
at n=2 supplies the same exponent needed here. It develops the October
two-torus argument, so it is not treated as an independent replication of that
input. It does not assert the conjectural homogeneous two-logarithm exponent
1+epsilon. [Primary November statement](https://arxiv.org/abs/2611.30820v1)

## Why this makes a new cycle conclusion possible

The actual two-grade cycle code has a mixed product alphabet: a disjoint pair
of chronological coordinates has three permitted letters and seven ordered
differences; a singleton has two letters and three differences. Elementary
prefix shortening gives the rate d with

    0.5248 < d < 0.5249,
    3.0196 < gamma/d < 3.0198.

Consequently an infinite family with odd width bounded by any fixed R<4 would
give rational approximants to gamma of exponent strictly above 3.0196. The
October theorem excludes that family. This yields finiteness at each such
fixed width and a limit inferior of at least four along every sequence of
distinct cycles. The coding proof and exact rational numerical certificate are
in the linked cycle note. Neither the ineffective logarithm constant nor the
asymptotic coding argument gives a finite period cutoff in this pass.

## Statement and source review of the formal supplement

The downloaded source archive has SHA-256

    2b37bfa6f04a1316eead45f1b6ba2ad660eef6a02f00b31476d603a7e55de69e

The root independently read the actual source of both public endpoints:

- `QuadraticPi.rationalLogRatio_irrationalityExponent_bounds` in
  `QuadraticPi/RationalLogRatioTheorem.lean`. Its assumptions are positive
  rational bases, a nonzero logarithm of the denominator base, and their
  multiplicative independence. It calls the proved interpolation endpoint;
  it does not take that interpolation conclusion as a theorem parameter.
- `QuadraticPi.rationalTwoLog_linearForm_lowerBound` in
  `QuadraticPi/RationalTwoLogLinearForm.lean`. Its positive constant precedes
  the quantification over all nonzero integer coefficient pairs, including
  pairs with a zero coordinate. The written source absorbs finite exceptional
  rational approximants and treats unreduced denominators explicitly.

The two source hashes are, respectively,

    981e0414ec5cecee694fcd185428ada352b5be8016f8048da0f1ab5a1b4255ff
    b83494d7b88478c052c9144042bba62f9a375dcf6663ac8b05dd92b0349fe489

The author's retained audit prints exactly these types and reports only
`propext`, `Classical.choice`, and `Quot.sound` for these endpoints. Its
October 19 audit log has SHA-256

    f00cf324e083c13fdf59b1a9c2552b47e4a6769d21cc1fcf481ff027da25668b

Those are **author-supplied audit records**, inspected here, rather than a new
kernel run by this pass. The broader manuscript distinguishes direct endpoints
from applications with named classical theorem parameters; its count of 62
reviewed statements does not erase those parameters. The particular rational
ratio endpoint above has the displayed ordinary mathematical assumptions only.

## Independent replay attempt and its limit

[replay_log_ratio.py](replay_log_ratio.py) constructs the complete local import
closure from the unchanged source and rebuilds it in fresh storage. The two
requested endpoint modules have 1,002 local dependencies: 840 OAI modules and
162 QuadraticPi modules, plus 373 distinct external imports. Its compiler and
Mathlib pins match this packet: Lean 4.34.1 at
`5045d0056413266e57c625dcd7c365b10e377c52`, and Mathlib at
`d13f23b723b8a846827a245b89c10fc7d3f11612`.

The attempt successfully rebuilt three unchanged modules with strict warnings
and standard trust settings. The fourth stopped because the local pinned
Mathlib cache lacks `Mathlib.Analysis.MeanInequalities.olean`. The requested
endpoints and their recursive axiom audit were **not reached**. The failed
receipt is retained separately; it is not counted among this packet's successful
Lean modules. No external proof was patched and no missing hypothesis was
supplied as an axiom.

Thus the new asymptotic cycle conclusion is a written, source-qualified use of
Theorem 11.1, together with independently reviewed finite combinatorics. The
local Lean kernels and the author's substantially larger external proof have
not been conflated.
