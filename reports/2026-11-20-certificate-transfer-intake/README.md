# Review of the supplied certificate-transfer material

This report records a mathematical and computational review of the two
user-supplied ZIPs, the separate unfinished PDF, and relevant results from
the preceding discussion. **No full Collatz proof is claimed.** The
scientific reconstruction remains PROPOSED for further review; the
verdicts below apply to the named narrow assertions in the supplied bytes.

## Sources and scope

Originals and the updated ZIP's 15 extracted members are preserved in
[the source archive](../../archive/certificate-transfer-intake-20261120/README.md).
[source-manifest.json](source-manifest.json) supplies original names,
sizes, and SHA-256 hashes. The PDF hash is
`edd35e567658c48803b43e78011c81644f153fcd73112de42f991b6d4dbaf99e`;
the updated ZIP hash is
`b96d4e38b46c7594c34ccd4c98e85d9c2e5934e147ff85294514872b0d12d5f4`.

Main was frozen at `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`.
Relevant source heads are:

| Source | Exact head | Relevant paths and claims |
| --- | --- | --- |
| PR146 | `e238c63a5d57f96bb063b7472498d1977df51951` | `research/upper-bit-mergers/THREE_RAY_UPPER.md` general absorption estimate; `BASIN_PHASE.md` exact phase criterion; `BOUNDED_RANK_TRANSFER.md` lifted-merger decision bound; `DEEP_REVERSE_BASIN.md` full-equivalent reverse criterion and rank-four layer. |
| PR162 | `2279da37ac612dbe049777354cdedb3c0aa03282` | `research/creative-closure-20261120/README.md` source-qualified overview; physical five blocks, signed Hardy flows, and first-hit versus repeated-time limits. |
| PR163 | `051237135a34ae7d4b973ee5fcf5da04ded6f0fc` | `research/deep-reverse-closure-20261120/README.md`; `LEAST_FAILURE_HEIGHT.md`, H1--H5, especially H4's exclusion of rank four as the globally least failure. |

[repo-snapshot.json](repo-snapshot.json) preserves the selected latest PR
metadata. Enumeration is not a review of every file on those branches.
No inherited Lean proof was rebuilt here. The
[initial discussion review](initial-review-and-problem-key.txt) is kept
at its original earlier cutoff; the active handoff has a separate update.

## Narrow mathematical verdicts

| Source assertion | Verdict | Reconstruction or correction |
| --- | --- | --- |
| PDF Lemma 1, pp2--3: exponential certificates are exactly odd convergent starts | VERIFIED | Integrality follows one suffix at a time from coprimality with powers of two; parity then makes each division exponent exact. The empty tuple represents 1 only. |
| PDF Lemma 2, pp3--4: equal-slope merger permits a certificate splice | VERIFIED WITH EXPLICIT CLOCK CONVENTIONS | Continue around the terminal cycle if necessary. Compare the same odd index, and finish the halvings from an even common value before splicing. |
| PDF Lemmas 3--5, pp5--6: type transitions, finite holding times, recurrent move walk | VERIFIED | The next driving parity is fair conditional on each finite binary cylinder; the two arms' literal input digits are not identified with their parity histories. |
| PDF Proposition 6, pp7--8: excursion contraction with coefficient `(3-sqrt(3))/2` | VERIFIED WITH LOCALIZATION MADE EXPLICIT | Reconstruct the nonnegative stopped supermartingale, use Fatou rather than assume uniform integrability, and bound the additive series by exact rational enclosures. |
| PDF Lemma 7 and Proposition 8, pp8--9: reachability and almost-sure absorption | VERIFIED | Explicit shrinking gap words plus recurrence to a finite gap set suffice. No fixed positive integer is declared generic. |
| PDF Theorem 1, pp9--10: natural-density-one relative coverage | VERIFIED | Each finite absorbed cylinder union has its exact natural density; increasing its depth makes the lower density tend to one. |
| PDF pp1,10: exceptional pairs are "unrelated" and no identity links their trajectories | REJECTED AS WRITTEN | `129` and `65` are exceptional and still meet. The valid claim excludes a merger of the prescribed affine families on a binary neighborhood, not all identities or certificate relations. |
| PDF p1: the positive exceptional set is infinite | PROOF NOT SUPPLIED THERE; REPAIRED HERE | The new explicit rank-four family lies entirely outside its coalescent set, without assuming target convergence. |
| PDF p10: its method cannot handle exceptions by any means | OVERSTATED | The particular coalescence mechanism does not cover them. A different positive-integer argument can handle particular exceptions; the negative control does not prohibit all extensions. |
| PDF p12: actual-integer depth is "about 4.8 B" | EMPIRICAL/UNSPECIFIED | No sampling protocol or universal complexity theorem supports that sentence. It is not used in the reconstruction. |
| Forward ZIP: local normal form and explicit affine merger classes | VERIFIED AS FINITE-WORD IDENTITIES | Their extension to every parameter comes from forced parity and affine equality, not from sampling many lifts. |
| Forward ZIP: universal landing envelope and sign law | CONDITIONAL / EMPIRICAL | A distinct-prefix product proof yields the bound; repeated-cycle prefixes are not covered. The sign census does not prove a universal sign theorem. |
| Updated ZIP: `problem2.py` splice and two-transfer consequence | VERIFIED AT STATED SCOPE | Successful returned certificates replay; a capped `None` is UNRESOLVED. The second-transfer consequence uses the open law twice. |

The detailed proposed proofs are in
[the scientific packet](../../research/certificate-transfer-intake-20261120/README.md).
These internal reconstructions are not external referee acceptance.

## Original program replay

The original forward scripts were executed during the preceding review.
The updated ZIP leaves those scripts byte-for-byte unchanged. The new
three programs were executed in this intake. Exact original stdout is
retained in the accompanying replay files when available; the earlier
review's observations remain identified as earlier observations.

| Program and scope | Actual outcome |
| --- | --- |
| Original `verify.py` | Dictionary passes through `k=60000`; absorption/phase comparison has zero mismatches through `k=6000`; seven infinite affine classes have matching forms and their sampled lifts pass. |
| Original `research3.py` | Two printed false negatives at `A=3,5`; all other printed failure counts zero. Correct fixed-clock replay passes all 100002 eligible cases. |
| Original `dstat 3000000` | `D=0`: 1154981; `D>0`: 1080541; `D<0`: 764478. All pairs in the census actually converge. |
| Original `landing 3000000` | Zero reported bound violations and sign mismatches; `a` ranges from -44 to 27. The real-valued bound check uses floating point. |
| Updated `problem2.py` | 5,215 successful transfers among 15,000 eligible indices through `m=20000`; all returned certificates valid. The specified odd-q family has 14,998 successes in 30,000 tested q values and zero reported failures. Samples `s=1,2,3` of the double-transfer identities pass. |
| Updated `conv 3000000` | 2,250,000 eligible indices: 887,639 structural mergers, 796,535 already-landed cases, 565,826 still-running cases; zero sign mismatches. |
| Updated `conv_dfs 28 9` | At depth 28 in the program's parameter `k=4m` (depth 26 in `m`), exact-prefix coverage in the three input classes is approximately 5.8833%, 56.4167%, 22.0760%, respectively. These are finite-depth dyadic measures of certified infinite progressions. |

The forward C trajectory audit checked all six million trajectories with
pre-multiplication overflow guards; its maximum intermediate value was
474637698851092, below `2^49`. The new reverse sweep's guarded maximum
was 825525149213608, below `2^50`. This validates integer width for those
specific runs, not arbitrary command arguments or all inputs.

The source's Monte Carlo and large-depth advertised figures were not
all rerun. Truncated excursion samples exclude capped runs, so their
empirical means are not proofs of unconditional excursion moments.
The PDF's reported 12,000 long Monte Carlo paths and every plot point
are not claimed as independently reproduced.

## Corrections to retain when using the sources

1. **A successful process exit does not guarantee every printed check passed.**
   Several originals print failure counts and still exit successfully.
   The active checker uses explicit failures and reports bounded search
   exhaustion as unresolved.
2. **First visit and fixed clock differ.** The consecutive-number
   checker records only the first visit to 1 and asks for a target's first
   occurrence. That causes its two false negatives; continuing the
   intended finite clock proves the stated identity.
3. **Parity bits are not literal digits.** The forward `verify.py`
   comment "bits of k then zeros" is inaccurate for its actual driver.
   The implementation uses the current physical arm's parity.
4. **Completed phase counts assume convergence.** `D` and `iota` based
   on stopping counts classify already completed certificates. They
   cannot be evaluated on a hypothetical divergent target and then used
   to infer its convergence.
5. **Failure of affine coalescence is not nonconvergence.** This includes
   positive examples 17/33 and 129/65 and the infinite family proved here.
   For 129/65, the first common shortcut value is 20; 5 is their first
   common odd/Syracuse value. The negative pair -127/-63 is a control
   showing failed merger, not a counterexample to the literal positive
   certificate implication, whose antecedent is false for negative inputs.
6. **The PDF appendix is not a complete reproduction bundle.** Its text
   contains printed line wrapping and does not include every listed
   checker or a complete plotting script for every numerical claim. Text
   extraction alone must not be treated as an original executable. The active
   Python checker is an independently named reconstruction, not claimed
   as a byte-exact supplied executable.

The PDF's cited historical verification threshold `2^71` agrees with
David Barina's [2025 primary paper](https://doi.org/10.1007/s11227-025-07337-0)
and [project log](https://pcbarina.fit.vut.cz/). It is used only to check
that bibliographic statement; that large computation was not replayed
and is not a dependency of our proposed proofs.

## Publication and execution

See [VALIDATION.md](VALIDATION.md) for actual commands, receipts, exact
published commit/tree, and their limits. Required repository validation
is performed in a complete clean checkout. Scientific replay is finite
evidence; the probability and all-parameter statements depend on their
written proofs. No remote CI or Lean success is inferred from a push.
