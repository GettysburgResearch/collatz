# Escape gaps and successive comparison types

**PROPOSED research, not a complete Collatz proof.** Continuation of PR #125
at `081dd4fb8af75b3b237a5eb4cef28b84bb5329be`; the previous chat packet is
already published there and is preserved unchanged.

Start with [the proof](PROOF.md). The main addition is a constructive theorem
for every integer gap, then a finite balanced-shadow compiler for every
eligible affine type. Every 4-adic escape exponent and every companion-ladder
depth now has explicit whole-class merger gates. This does not cover every
parameter of those types. The exact 65536-input comparison adds 99 successes,
from 4366 to 4465, with all 61071 remaining OUTSIDE outcomes retained.

## Replay

From this branch's repository root, using Python's standard library:

```sh
python -B experiments/paired-comparison/escape-gaps/run.py --full /tmp/escape-full.jsonl --check experiments/paired-comparison/escape-gaps/canonical.json
python -B experiments/paired-comparison/escape-gaps/verify.py /tmp/escape-full.jsonl --summary experiments/paired-comparison/escape-gaps/canonical.json --self-test
python -O -B experiments/paired-comparison/escape-gaps/verify.py /tmp/escape-full.jsonl --summary experiments/paired-comparison/escape-gaps/canonical.json --self-test
```

On Windows replace `/tmp/escape-full.jsonl` with a writable local path and use
`py -3` where appropriate. This is syntax guidance, not a Windows test receipt.
For a smaller procedure census use `--limit N --output temporary-summary.json`
and verify against that generated summary; the symbolic/original family corpus
is unchanged. Do not compare a smaller grid against the committed canonical.

`run.py` constructs physical word certificates, not conjectural stopping-time
estimates. `verify.py` imports no generator or other repository module and
checks full input preservation as well as positive witnesses and whole-cylinder
identities. The full rows are generated rather than committed. Their digest,
counts, and representative original-root examples are in `canonical.json`.

The full 78278-row artifact includes 12300 gap cylinders, 378 affine cylinders,
64 original certificates and all 65536 comparison classifications. Ten of the
original witnesses have a further equal-clock companion below n/3. There are
also 8998 bounded exact checks of the one-odd-each contracting-window lemma.

[Execution receipt](../../../reports/paired-comparison-escape-gaps/validation.json)
records precisely the tests performed. Same-author independent implementation
is not independent mathematical acceptance. The parent publisher's tests do
not extend automatically to this branch. No source PR is merged and no
canonical scientific status, workflow, license, or repository setting changes.

## Review priorities

Check the all-g gap recursion and polynomial modulus inequality; physical
integrality of both inverse words after restricting the progression modulo 3;
why the a-th signed even step is reached without a negative-convergence
assumption; the slope balancing identity and actual gate, including even u;
the Q-type intercept in normalization; original-root clocks after exchanged
arms; and the quantifier difference between every type and every parameter.

The immediate next task is control of the actual failed guards using a
companion switch or a common rank, not a larger finite success count.
