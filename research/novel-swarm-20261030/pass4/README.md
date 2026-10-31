# Pass 4: uniform averaged pressure decay and sparse coefficient records

**PROPOSED. Collatz remains unresolved.** This pass advances two concrete
interfaces beyond pass 3, with exact negative controls. It does not merely
increase the convergence census or claim that averaged decay is pointwise.
All earlier files remain unchanged.

## Read the mathematics

[WINDOWS.md](WINDOWS.md) reconstructs translated simple-path packing with the
explicit all-width bound `16 K^(19/20)`. The source interval location, odd-step
labels, and terminal-boundary removal are retained. Uniform sparsity and its
entropy exponent already have substantial literature; this is a self-contained
input, not a claimed new best exponent. See [SOURCES.md](SOURCES.md).

[PRESSURE.md](PRESSURE.md) proves, for the first-hit pressure F of pass 3,

    sup_(a>=1) (1/K) sum_(a<=t<a+K) F(t) <=20 K^(-1/20) ->0.

This is unconditional and includes the full infinite sum of source weights.
It forces every positive pressure superlevel to have zero upper Banach density,
not to be finite. The same file proves summable drops along any nonperiodic
orbit and certifies two decreases of the FULL pressure:

    F(263)-F(395)>1/3000000,
    F(251)-F(377)>1/1500000.

Thus the normalized pressure is not a globally increasing rank. These are
not unqualified partial-profile drops: the whole uninspected source tail is
included. The ordinary map V(n)=3n supplies averaged decay and bounded variation
with nonzero pointwise limits, exposing the missing inference explicitly.

[RECORDS.md](RECORDS.md) gives the general transfer

    translated packing exponent beta
        => coefficient-record count O(n^(beta^2))

on one actual simple no-descent segment from n. With beta=19/20 the exponent
is 361/400=0.9025. A finite coefficient-stopping certificate on the associated
near-source window then forces physical descent or repetition within R*N
steps, where R is the improved record budget. That stopping hypothesis is
NOT proved. This exponent is a record count, not a density of counterexamples.

## Checks actually executed

The [producer](../../../experiments/novel-swarm-20261030/pass4/run.py) uses four
CPU processes, not independent AI agents. The
[separate verifier](../../../experiments/novel-swarm-20261030/pass4/verify.py)
imports neither the producer nor another repository module. Normal parallel,
normal serial and optimized parallel producer runs give identical full JSON;
normal and optimized verifier runs give identical summaries.

The fixed inventories contain 8,190 parity words, 24,570 positive lifts,
3,200 translated windows including 256-bit offsets, nine exact integer
constant certificates, 229 binomial clock rows, 8,191 first-descent prefixes,
511 complete simple prefixes, and 32,768 pressure sources. The pressure
verifier uses 2,379,157 raw shortcut steps. Twelve direct corruptions are
rejected per verifier mode. These are bounded tests and implementation checks,
not proofs by enumeration or independent mathematical review.

An important limit: the 8,191 no-descent prefixes all have only one record.
The 511 full simple prefixes exercise up to 16 records, but may descend.
The difficult hypothetical multiple-record no-descent case is not claimed
to have been observed or computationally settled.

Replay from the repository root (standard-library Python):

```sh
python -B experiments/novel-swarm-20261030/pass4/run.py --output /tmp/pass4.json
python -B experiments/novel-swarm-20261030/pass4/run.py --serial --output /tmp/pass4-serial.json
python -OO -B experiments/novel-swarm-20261030/pass4/run.py --output /tmp/pass4-oo.json
python -B experiments/novel-swarm-20261030/pass4/verify.py /tmp/pass4.json --output /tmp/pass4-verify.json
python -OO -B experiments/novel-swarm-20261030/pass4/verify.py /tmp/pass4-oo.json --output /tmp/pass4-verify-oo.json
```

Full producer output SHA-256:
`e2d1cfcba3911bfa6fb814cf98ed69d495b8e4166e7eed419dd8360fc07a6475`.
It is regenerated rather than committed as a 579,332-byte payload.
[Receipt](../../../reports/novel-swarm-20261030/pass4/receipt.json) and
[self-audit](../../../reports/novel-swarm-20261030/pass4/REVIEW.md) record scope.

## The first unsupported step

Uniform averaged decay still permits a fixed ordinary orbit to follow sparse
nonzero pressure spikes forever. No 3x+1-specific theorem here prohibits it.
The record route still lacks universally available coefficient crossings;
its finite-set budget is not a total termination algorithm. Nontrivial
positive cycles are not excluded. The inherited E5 collision target remains
open. No full-checkout validator, remote CI or external formal build is claimed.
