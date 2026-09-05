# X-ASTRA-005 — shared-remainder rank cancellation

**Exact finite support; mathematical claims PROPOSED pending independent review.**
No complete Collatz proof or complete merging cover is certified. The proofs,
all-height scope, and failed synchronization strengthening are in
[REMAINDER_CANCELLATION.md](../../research/astra-critical-mass/REMAINDER_CANCELLATION.md).

## What this experiment reconstructs

For the shortcut map and global integer rank

    P(n)=(2n+1)^2/3^v3(2n+1),        including depth-zero positive sources,

an exact pair of length-j words with equal shifted remainder B and an
odd-count difference of two certifies

    x=(n-4)/9, T^j(x)=T^j(n), P(x)=P(n)/9,

on its dyadic source cylinder and n=4 modulo 9. The written proof covers every
eligible ternary depth, not only the depths substituted in the tests.

The generator enumerates all 65,535 odd-starting words of lengths 1 through
16 using affine composition. The verifier independently obtains those words
by physical shortcut iteration from every odd source residue at each length.
It computes B from the source and endpoint, rather than the B recurrence.
Every source guard, odd count, shared remainder, and prefix exclusion is exact.

The compiler returns **425 prefix-free rules**. At modulus 2^16 they cover
3260 of 32768 odd classes. Exactly 391 of the covered classes are 11 modulo
16, covering 391/4096 of the dyadic factor of the previous five depth-two
residual progressions. This is finite completeness within the stated word
search, not completeness for all integers or for all merging diagrams.

## Actual checks and what their counts mean

* Every rule is replayed at exact ternary depths 2, 3, and 12, both unit residues,
  and two positive lifts: **5100 ordinary merging certificates**. Depth-zero
  cheaper witnesses are transferred to the old section with a further strict
  rank decrease, by physical replay.
* Global normalization is checked for every n<=65536: 43,690 depth-zero
  forward reductions, 14,563 depth-one reductions, 3,641 even high-depth merges,
  359 homogeneous cancellations, one base state, and **3,282 unresolved lift
  obligations**. A lower-rank quotient without a proved merge is never labelled
  a certificate. These counts do not assert all 65,536 sources converge.
* Twenty-six members of the earlier five depth-two progressions receive
  homogeneous certificates in this finite range. This is not a priority claim
  against every previous merging tile or the wider literature.
* Twenty-one CRT cases cover L in {1,2,4,8,16,32,64}, H=3L, and three positive
  lifts. Their **381 forward steps** all satisfy the exact rank-barrier bound,
  while each seven-step two-sided diagram divides the starting rank by nine.
* The pairs (13,1) and (859,95) are checked through their finite stopping times.
  Their opposite eventual two-cycle phases refute a universal synchronous
  quotient rule; they do not refute ordinary asynchronous merging.
* Eight deliberately altered reports are rejected after their digests are
  recomputed: false global scope, smaller search depth, smaller basis count,
  changed B, changed parity word, omitted coverage row, wrong merger time, and
  removal of unresolved labels.

Both implementations have the same author. This is implementation independence,
**not independent mathematical review or formal verification**. The symbolic
arguments supply the all-parameter conclusions. No data are extrapolated.

## Replay

From the repository root:

```bash
python experiments/X-ASTRA-005-remainder-cancellation/run.py \
  --check experiments/X-ASTRA-005-remainder-cancellation/results/canonical.json
python experiments/X-ASTRA-005-remainder-cancellation/verify.py \
  experiments/X-ASTRA-005-remainder-cancellation/results/canonical.json --self-test
```

Both commands passed locally. The semantic SHA-256 is

    c38d5d5e96dd00b5201b760b0f0b7412d43273bb2b720b26e86e6bcccef8aff1

The compact report includes the full reconstructed payload digest:

    46261ae0e3d714e2c9a32ebd3a9a4c6e9ea3cf8f5c99934b41fd169192acb12c

Materialize every one of the 425 rules and the forward-barrier witnesses with
`--full-output /tmp/astra-remainder-full.json` on the generator command.
The compact report also preserves separate digests of the full rule list,
the global normalization rows, and the ordinary rule-replay cases.

No external mathematical input, external large computation, Lean build,
full-repository structural validator, or workflow is part of the checker.
All earlier X-ASTRA artifacts and proof texts remain unchanged.
