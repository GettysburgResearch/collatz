# Independent review of the two fourth-gap-five bypasses

Reviewer: `/root/five_transport`. Review date: 2026-11-21 (Asia/Jerusalem).

## Exact scope

Reviewed CB1–CB4 in `C5_CERTIFIED_BYPASSES.md`, SHA256
`dc846bbce7fa74f1235cab5049a8ac7fd269bab666abde656c51c86c977cb258`,
and the associated `check_c5_certified_bypasses.py`, SHA256
`0437e87b861c17423706eca4b994181460a108f173baef121112b2004fd4b805`.
The review applies to those file bodies, not later edits or other claims
in their source branches.

**Verdict: VERIFIED for the two stated infinite ordinary parameter
classes and their stated certificate and least-failure consequences.**
No full Collatz theorem or universal bypass coverage is established.

## Independent reconstruction

I reconstructed the two parent prefixes directly from
X(k)=128k+1 and Y(k)=64k+1 on k=14 modulo 32. They give

- source word (2,2,2,5), ending at (81k+2)/16;
- target word (2,2,2,1,2), ending at (243k+14)/8.

I then wrote and actually executed a separate exact-rational affine
replayer containing the two displayed child words and parameter tables.
It did not import or invoke the supplied checker. At every odd step it
checked the exact valuation on the base integer and proved that the
coefficient of the nonnegative parameter remains positive and even.
Thus the replay proves the branches for all nonnegative integer lifts,
not merely sampled starts. The independently recovered shared endpoints
were:

| Rule | Source endpoint | Target endpoint |
|---|---|---|
| A | 9565938t+8537309 | 57395628t+51223855 |
| B | 9565938t+6057251 | 57395628t+36343507 |

The child source uses 14 odd inputs, compared with the parent's 4. The
child target uses 15, compared with 5. Their respective shortcut-clock
increases are 14 for A and 15 for B.

The direct parameter formulas give positive eligible child indices and
strict decrease: k-k' is 1365280t+1218471 in A and840992t+532525 in B.
This verifies the ordinary component equivalences in CB1 without assuming
convergence of either leg. The implication equivalence CB2 follows
propositionally from the two separate component equivalences.

## Other proof checks

1. The formal fifteenth odd contribution in the source correction is
   used only algebraically. From Cs=3C14+2^(S+1), the displayed formula
   for X(k') gives the endpoint (P/2-1)/3 after the actual 14-step word.
   It does not assert that the formal final exponent one is physical.
2. The identity Cs=2Ct+3^15+2^S gives the target endpoint P-1 after
   its physical 15-step word. This matches the parent endpoint.
3. All forced states and shared endpoints exceed1. Therefore a genuine
   first-hit certificate contains the full forced prefix. Replacing
   prefixes gives the claimed arbitrary-certificate transformation,
   while preserving any later terminal loops if they were supplied.
4. The Mersenne specialization has z=(2^(e-1)-1)/3 and m=2^e-1.
   Thus the child source first-hit certificate is its 14-step prefix
   followed by exponent e-1, of exact odd rank 15.
5. I separately checked the two modular powers modulo 3^15 and their
   membership in e=119 modulo 162. The order 2*3^14 follows from the
   elementary valuation identity stated in the note. Consequently the
   two exponent progressions are complete for the two displayed rules.
6. The two progressions are disjoint. Their combined relative density
   is 2/59049 both within the parent index class and within the specified
   Mersenne exponent progression.
7. The least-failure conclusion uses smaller upper height, not smaller
   certificate rank. The ten extra odd inputs therefore do not create
   an induction gap. No assumption that all smaller integers converge
   is used in the underlying paired equivalence.

The note correctly distinguishes its new explicit paired descents from
the latest PR146 theorem that already produces some least-failure-excluded
subprogression inside every Mersenne exponent progression. Its exclusions
remain limited to the two displayed parameter classes, and are compatible
with the earlier unbounded predecessor-depth obstruction.

## Execution limits

The review executed the independent affine replay and modular-power
checks described above. It did not rerun a giant Mersenne trajectory,
prove convergence of either entire progression, rebuild external source
theorems, or run a proof assistant. The finite all-lift arithmetic checks
have their mathematical force because every intermediate affine state
and guard was reconstructed symbolically on the full parameter class.

The independent code is preserved as `review_c5_affine.py`, with actual
stdout in `c5-independent-report.json`. It was also executed as a saved
script with `python3 -X utf8 -B review_c5_affine.py`; the result was PASS.
