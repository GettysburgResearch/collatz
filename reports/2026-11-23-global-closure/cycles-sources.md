# Cycle lane: frozen sources and evidence

Date: 23 November 2026. Lane: unrestricted positive integer-cycle exclusion.

## Authored packet

- `research/global-closure-20261123/cycles/README.md`
- `research/global-closure-20261123/cycles/INTEGRAL_MAHLER_CLOSURE_ATTEMPT.md`

The lane worked in the shared checkout based on
`2169884b64871b448cda16c7d74a0d5914ed870b`.
It made no Git commits, GitHub writes, branch updates or PR edits.
Publication and the repository gate belong to the coordinating root agent.

## Exact source inspections

All paths below were read at the listed full commit, through the GitHub
connector. Their mathematical statements remain attributed to the source;
this table does not claim a replay or independent verification of an entire
PR.

| PR | Full head | Exact path |
|---|---|---|
| 185 | `2ac1f63b5f8d51ab4b472307b52cc89c9ef6df9d` | `research/central-closure-20261123/PRIMITIVE_DENOMINATOR_GROWTH.md` |
| 185 | `2ac1f63b5f8d51ab4b472307b52cc89c9ef6df9d` | `research/central-closure-20261123/PRINCIPAL_FIBER_CONTROL.md` |
| 176 | `ff3e068fa44eb85bb918580b2e10e18c027a18e6` | `research/lean-global-resolvent-20261121/overview/longshot/cycles/IDENTITY_ATOM_ATTEMPT.md` |
| 175 | `8870528daa6a13cc941d602e578e35c8bfa4bf4f` | `research/lean-global-closure-20261121/risk23/ALL_WORD_POLYNOMIAL_ATTACK.md` |
| 182 | `aa12c13601cacec2c8496f1349b4947457dc1b45` | `research/high-variance-20261123/CYCLE_IDEAL.md`, opening theorem and construction through the primitivity argument |

The current PR185 and PR182 PR bodies were also read to locate the new
claims. The parent supplied the wider repository refresh.

Local entry sources read include `AGENTS.md`, `README.md`,
`docs/RESEARCH_MAP.md`, `research/integrated/ERRATA.md`, relevant
cycle entries of `research/RESULTS_CATALOG.md`, the previous
`research/high-variance-20261123/cycles/` packet,
`research/band-return-20261121/README.md`, and the common-source
repetition argument in
`research/global-synthesis-20261122/ARITHMETIC_CLOSURE.md`.
No old Lean corpus was rebuilt for this lane.

## Primary literature inspected

### Adamczewski--Bell

B. Adamczewski and J. P. Bell, *A problem about Mahler functions*,
Ann. Sc. Norm. Super. Pisa Cl. Sci. (5), XVII (2017), 1301--1355.

- [Journal article](https://journals.sns.it/index.php/annaliscienze/article/view/574)
- [Primary journal PDF](https://journals.sns.it/index.php/annaliscienze/article/download/574/560/792)
- Exact scope read: Definition 1.1, displayed equation (1.3), Theorem 1.3,
  and its introductory discussion, printed pp. 1303 and 1306.
- Use: conditional-on-the-published-theorem inference that a nonrational
  2-Mahler series cannot also be 3-Mahler. Characteristic zero and
  multiplicative independence of 2 and 3 are explicit.
- No claim to have reconstructed the full proof or formalized it in Lean.

### Corvaja

P. Corvaja, *Upper bound for the gcd(u-1,v-1), u,v S-units,
generalisations and applications*, RIMS Kokyuroku 1710 (2010), 1--6.

- [Primary author lecture PDF](https://www.kurims.kyoto-u.ac.jp/~kyodo/kokyuroku/contents/pdf/1710-01.pdf)
- Exact scope read: the fixed-data gcd and power-sum quotient statements
  in Theorems 2--4, with the adjacent qualifications.
- Use: check of whether the cited machinery already supplies the
  word-uniform, growing-support estimate. It does not supply that
  statement as written. No new gcd theorem is asserted.

The current rStation paper *Sparse block-sum and ordered-state complexity
in positive Collatz cycles*,
[version 3](https://rstation.ai/problems/collatz/papers/22/v3),
was inspected for its abstract, scope and pointers to the gcd literature.
No theorem from that paper is imported into the authored derivations.

## Claim and evidence boundaries

| Item | Evidence and scope |
|---|---|
| Nonrationality of a nonzero finite linear combination of distinct odd dyadic rays | Complete elementary written proof by disjoint support, unbounded zero gaps and the recurrence of a rational series |
| Absence of an independent 3-Mahler equation for that series | SOURCE-QUALIFIED application of Adamczewski--Bell Theorem 1.3 to the preceding proof |
| Exact torus semiconjugacy and minimal degree `D/gcd(C,D)` | Complete elementary integer-character calculation, for every positive word; no denominator factor omitted |
| Degree one iff ordinary integer cycle closure | Exact full-divisibility equivalence, not an exclusion theorem |
| Full positive-cycle exclusion | OPEN |
| Universal convergence | OPEN; escape is a separate lane |
| Lean additions in this lane | None; no imported statement declared as an axiom |
| New bounded word enumeration | None |
| Repository gate | Not run by this lane; root records the actual published validation |

The packet does not count the dyadic elimination from PR175 as new. It
does not claim that identifying an unfulfilled hypothesis resolves the
conjecture. The next unproved mathematical statement is exactly the
all-word degree-one exclusion (19) in the attempt note.
