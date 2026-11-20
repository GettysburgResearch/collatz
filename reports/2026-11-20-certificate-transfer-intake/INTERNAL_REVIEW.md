# Scoped internal reconstruction reviews

These are independent argument reconstructions within the current agent
team, not human referee acceptance or formal proof-assistant verification.
The active mathematical packet stays PROPOSED. The root reviewer read all
three proof manuscripts and applied only the identified scope clarifications.

## Density proof

The analytic reviewer authored `DENSITY_ONE.md` from the supplied PDF.
A separate closure reviewer checked its excursion potential, bounded
optional stopping and Fatou steps, conditional suffix bound, holding-time
costs, finite-set recurrence, absorbing-word trials, and density passage.
The reviewed SHA-256 was
`4a0c699d423666fa1f4f9aa349e1a78e9262a0c10d2abb8361cee65cc828ce06`.
The exact rational majorant was independently evaluated as less than
53.335 and hence less than 54.

The reviewer requested the explicit convention `v2(0)=+infinity` for
zero offsets at nonzero levels. That clarification was applied; the root
re-read the affected holding-time argument. The resulting file hash is
`94c46e3731cbd9f062699741fa9a8bb1898ffbfc2c0e0e1e0d9698ae272bf16b`.
There was no change to the stochastic theorem or its proof mechanism.

## Exceptional family

The closure reviewer authored `EXCEPTIONAL_FAMILY.md`. The analytic
reviewer independently reconstructed the exhaustive rank-four source
family, all clocks and odd counts, the phase inequality, and both power
progressions. It also checked the distinction from PR163's global-minimum
argument. The file was approved at SHA-256
`639f2e4e83908f107f104b0ba875dea8fb0ec0fc9532ea36b49e8fd40c67aa78`,
without a subsequent mathematical edit. A separate bounded replay checked
the source certificate and single/double checkpoints for `s=1,...,5`;
the active checker has its own larger explicitly recorded finite sample.

## Forward phase and landing analysis

The root authored `LANDING_AND_PHASE.md`. The closure reviewer checked
the phase criterion, local normal form, product bound, distinct-prefix
hypothesis, and expanding two-odd-step family at SHA-256
`bf61cb72c7010288bd82568d90fab2ed31397d8ac90c1c6d581f31b9e06a00f7`.
It requested that LP1 explicitly say the affine families are integer
affine families at the same integer parameter. The root applied and
re-read that scope clarification. The resulting hash is
`7974ba70eded455868f898e4d9b6784ea9075923f0f284d6cd7bdb4a8d83347d`.

## Handoff and source comparison

The analytic reviewer read the pinned PR163 least-failure, kernel and
energy manuscripts and PR162's occupation material, and checked
`HANDOFF.md` at SHA-256
`e2510880c15cd8c7944baadcccd94b4d1092082007562406bb60a8bcc727ba1c`.
Two scope fixes were applied: the carry obstruction is limited to the
specified canonical mixed-base controller; the harmonic rigidity
consequence retains the separately source-qualified PD hypothesis.
The final root-checked handoff hash is
`b5161bab6e0181ed581bf650e10bcfc073294d448cdf77a5e62aabe20d425284`.

The earlier source reviews are retained as
[PDF analytic review](pdf-analytic-review.md) and
[PDF certificate review](pdf-certificate-review.md).
They are reviews of the uploaded PDF, not blanket approvals of later
repository revisions. The [main report](README.md) distinguishes narrow
verified assertions, repaired wording, and open targets.
