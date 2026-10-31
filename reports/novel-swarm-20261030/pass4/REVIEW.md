# Pass 4 self-audit and execution boundary

**PROPOSED, self-audited only.** The verifier is a second implementation by the
same author. No independent AI-agent or external mathematical review is claimed.
Base: `6bee3183ff7f29f2e20ca88ab94bc7745c1af602`, PR #140.

## Claim-by-claim audit

**W1--W3: translated packing.** The map is the raw shortcut on positive
integers. The recurrence applies to finite SIMPLE trajectory segments, not
to their many-to-one predecessor basins. Removing the last k states makes
T^k injective into that same segment. The source 5 control retains the failure
without this removal: 5 and 1 are distinct members of 5,8,4,2,1 but merge at
clock 4. The q=0 word, k=32 induction boundary, all high-tail words, rational
image widths, and very large positive interval offsets are retained. The
constant 16 is conservative and may exceed the trivial finite count. The
written induction is the all-width proof; the 229 clock checks are not a
substitute for induction. This is a reconstruction of an established
compression idea, not a new sparsity-exponent priority claim.

**P4-1: pressure averaging.** Each source contributes at most x^-2 per target;
its distinct targets in a fixed window lie in a finite simple prefix. Tonelli
therefore bounds the FULL infinite source sum by the translated packing count.
Cyclic sources are allowed, with first hits counted once. The conclusion is
uniform spatial averaged decay and zero upper Banach density of superlevels,
not pointwise decay. No equidistribution of a fixed source was presumed.

**P4-2: full-pressure counterexample to monotonicity.** All odd sources through
65535 were literally followed to 1. Four exact first-hit sums plus the entire
reciprocal-square tail certify the two strict inequalities. The verifier uses
raw shortcut clocks and reconstructs every source, rather than trusting an
accelerated transcript or the old profile. This is a finite certificate about
four infinite sums. It says nothing about monotonicity of the different
D-normalized transported ledger from pass 3.

**P4-3/P4-4: source-persistent variation and its limit.** Old first-hit sources
remain old along a NONPERIODIC orbit. On a cycle their first arrivals may occur
earlier, so the cohort equation is not asserted there. The finite reciprocal
budget makes downward variation summable; bounded F then bounds upward
variation. The ordinary V(n)=3n example retains both averaged decay and bounded
variation while its pointwise component limit is positive. It blocks that
abstract shortcut, not a future argument specific to 3n+1.

**R4-1--R4-4: record packing.** Every record source is a state of the original
simple no-descent segment. The short distortion window has width O(n^beta),
and a SECOND use of the translated trajectory bound gives O(n^(beta^2)) actual
records. The record set is not treated as a new forward orbit; there is no
beta^3 iteration. The conditional stopping proof preserves the original clock
and includes descent OR repetition. The unconditional finite extraction keeps
its minus-one endpoint correction. The explicit threshold (320/3)^20 is very
large and is not a practical verification threshold.

The no-descent test grid has only one record per source; multiple-record
no-descent behavior would encounter the still-unproved Coefficient Stopping
Time conjecture. We added a separately labeled full-simple-prefix grid that
may descend, with up to 16 records, to test the partition arithmetic without
claiming it realizes the difficult no-descent case. Finite-path exact rational
windows are not the global transcendental window.

## Actual final-byte execution

Five final executions completed with exit code zero under Python 3.13.5:
producer normal parallel, normal serial, optimized parallel; verifier normal
and optimized. The three 579,332-byte producer outputs are byte-identical,
SHA-256 `e2d1cfcba3911bfa6fb814cf98ed69d495b8e4166e7eed419dd8360fc07a6475`.
The two 480-byte verifier outputs are byte-identical,
SHA-256 `1169e537463e09cfdd92671ebab6b5b151417caac04891b3c0ad052c04af19a7`.
The exact commands, measured durations, timestamps and source hashes are in
receipt.json. Checks use explicit exceptions and remain active under -OO.

Coverage: 8,190 complete binary words of lengths 1--12; 24,570 positive lifts;
3,200 window cases and 14,288 labelled image groups; nine exact integer
inequalities and 229 binomial clock rows; five failed 5x+1 upper-tail controls;
8,191 no-descent sources (28,457 raw steps including their exit) and 511 full
simple prefixes; 32,768 pressure sources (1,195,565 odd steps and 2,379,157
raw shortcut steps in the separate replay); 4,096 exact V(n)=3n target values.

The separate verifier reconstructs the fixed inventories, alternate affine
constant sums, located rational image endpoints, direct distortion products,
complete raw-clock source bank, and geometric control values. It rejects
12 direct semantic/schema/duplicate-JSON corruptions in each mode. These are
NOT resealed full-corpus mutation tests. No verifier is claimed complete
against every possible malformed JSON object, and no finite census is a
formal proof of the infinite statements.

The final Python files passed AST parsing, and new relative Markdown targets
were checked in the partial workspace. Those narrow structural checks are
separate from a full repository validator. A streaming-exec attempt was
refused by the environment before it executed; the five actual final runs
were subsequently performed synchronously and are the recorded evidence.

## What was not run or proved

This runtime contains a PARTIAL workspace extracted from the previous packets,
not a clean complete repository checkout. Direct Git transport failed DNS.
No `tools/validate.py`, repository regression bundle, remote CI, external
proof-assistant build or Windows replay is claimed. No older execution receipt
is silently extended to this head. A plugin search found no callable independent
agent launcher; four workers here means four computational processes.

Cycle-word explorations and apparent balanced-word patterns were not promoted
to new theorems; their underlying cycle constraints have prior literature and
no universal exclusion was obtained. The pointwise pressure-decay inference
was tested against and blocked by the explicit ordinary model. The finite
profile monotonicity shortcut was refuted with full-tail certificates.

A full solution still needs a 3x+1-specific exclusion of sparse nonperiodic
pressure spikes, or universal source-specific stopping/merging coverage, and
appropriate cycle control. None is established. There is no claim to have
recovered the missing original swarm packet or retroactively validated its
old independence claims. Prior proof files and acceptance statuses are intact.
