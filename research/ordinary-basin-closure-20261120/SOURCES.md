# Frozen sources and scope

All results in this packet are PROPOSED research. Existing source results are
used only at the exact revisions below. The new identities are proved directly
in their local notes; the full-conjecture equivalence and the analytic route's
implication toward eventual periodicity retain their source qualifications.

| Source | Full commit | Path and claim used |
|---|---|---|
| [PR146](https://github.com/GettysburgResearch/collatz/pull/146) | `6863d298187af8b2619efbf78cc4b0aa8e627393` | `research/upper-bit-mergers/THREE_RAY_ONE_SIDED.md`: equivalence of full Collatz with the one-sided implication on `16k+1,32k+1`. |
| PR146, same pin | `6863d298187af8b2619efbf78cc4b0aa8e627393` | `research/upper-bit-mergers/THREE_RAY_UPPER.md`: actual finite-cylinder pair process and the square-root logarithmic upper bound, not a fixed-source random law. |
| PR146, same pin | `6863d298187af8b2619efbf78cc4b0aa8e627393` | `research/upper-bit-mergers/AFFINE_RAYS.md`: compatible-slope finite-list synchronization and component prescription, if used for the finite repetition construction. |
| [PR156](https://github.com/GettysburgResearch/collatz/pull/156) | `c5cb84502c7289705d59a8781a65fd845b9b6b14` | `research/global-rigidity-20261120/Q_SECTION_GUARDS.md`, QG1--QG4: the original least-failure floor, physical orientation, exact transducer, and finite-horizon signed shadow. |
| PR156, same pin | `c5cb84502c7289705d59a8781a65fd845b9b6b14` | `research/global-rigidity-20261120/SMOOTHING_BOUNDARY.md`, SM4--SM5: exact all-word trace, least positive odd representatives, and critical perpetuity. These are source results, not discoveries of this packet. |
| PR156, same pin | `c5cb84502c7289705d59a8781a65fd845b9b6b14` | `research/global-rigidity-20261120/ORDINARY_ESSENTIAL_SPECTRUM.md`, OE5 and section 7: the particular-vector moment interface and the source-qualified ordinary reciprocal-budget comparison. No uniform spectral gap is assumed. |
| [PR155](https://github.com/GettysburgResearch/collatz/pull/155) | `92f499b9d340d1ff8cc643c3eef3477d61b477c1` | `research/gemini-dirichlet-global-20261120/ORDINARY_DIRICHLET_COERCIVITY.md`: the previously published ordinary coercivity theorem. The current pair upper estimate does not supply its missing power-saving boundary bound. |

PR154 at `fe40bb6f88e8094290ef01207d9bf7c4798d35d0` was inspected as a
possible alternative architecture, especially its restricted-five-ray and
prime-height arguments. No theorem of that source is used as an unstated
closing lemma here.

The earlier Gemini packets were not treated as evidence for any universal
closure. This pass follows the ordinary-source proof obligations identified
after their assessment. It does not claim priority for standard affine word
identities, inverse-column expansions, or the underlying open conjecture.

## Later heads observed during publication

The initial pins above remain the exact dependency boundary. A final remote
check also found the following concurrent work, which was read to prevent
overstating the contribution of this pass:

- **PR146 `0410811710af2f7da71522ec67233528048adb9a`:**
  [BASIN_PHASE.md](https://github.com/GettysburgResearch/collatz/blob/0410811710af2f7da71522ec67233528048adb9a/research/upper-bit-mergers/BASIN_PHASE.md)
  contains the depth-two Mersenne family and the phase obstruction to lifted
  mergers. [BOUNDED_RANK_TRANSFER.md](https://github.com/GettysburgResearch/collatz/blob/0410811710af2f7da71522ec67233528048adb9a/research/upper-bit-mergers/BOUNDED_RANK_TRANSFER.md)
  gives a general finite deadline for testing lifted mergers from a known odd
  depth. [RANK_THREE_MERSENNE.md](https://github.com/GettysburgResearch/collatz/blob/0410811710af2f7da71522ec67233528048adb9a/research/upper-bit-mergers/RANK_THREE_MERSENNE.md)
  encodes every exponent at least 819, with a separate finite check below that
  threshold. [REVERSE_BASIN.md](https://github.com/GettysburgResearch/collatz/blob/0410811710af2f7da71522ec67233528048adb9a/research/upper-bit-mergers/REVERSE_BASIN.md)
  also proves a reverse one-sided criterion, leaving its premise open.
  These descriptions are source-qualified comparisons, not an independent
  full review of the later head or a replay of its Lean and finite certificates.
- **PR157 `64361ecca770092d6c8242dc6211e38818af2e50`:** the PR statement and
  [closing-attempts.md](https://github.com/GettysburgResearch/collatz/blob/64361ecca770092d6c8242dc6211e38818af2e50/research/global-closure-20261120/closing-attempts.md)
  were read. They retain the physical forward-five basin law and the actual
  occupation upper bound as open. Neither is assumed here.

The depth-two classification in CERTIFICATE_CARRY is an independently
reconstructed proof also present in the concurrent PR146 source. The partial
compiler is not claimed to supersede that source's general bounded-rank test
on the original one-sided family. The two explicit guard-surviving Q-return
macros and their switching analysis are the principal additional result of
this packet; no exhaustive priority claim is made.

## External context for the normalized ceiling map

M. Andrieu, S. Eliahou and L. Vivion, *A Normality Conjecture on Rational
Base Number Systems*, [arXiv:2510.11723v2](https://arxiv.org/html/2510.11723v2),
7 April 2026, Conjecture 1.6. The primary text was opened and its precise
ceiling-map equidistribution statement checked. It is used only to identify
the unproved nature of a possible external closing input. No equidistribution
or normality claim is assumed in TWO_MACRO_NORMALIZATION.md.
