# X-AEM-005: universal shadow atlas

Python standard library only. All operations are exact integer operations;
no assertion-based verification and no floating point participates in acceptance.

From the repository root:

```sh
python -B -S experiments/X-AEM-005-universal-shadow-atlas/run.py --check experiments/X-AEM-005-universal-shadow-atlas/results/canonical.json
python -B -S experiments/X-AEM-005-universal-shadow-atlas/verify.py experiments/X-AEM-005-universal-shadow-atlas/results/canonical.json --self-test
python -O -B -S experiments/X-AEM-005-universal-shadow-atlas/verify.py experiments/X-AEM-005-universal-shadow-atlas/results/canonical.json --self-test
python -B -S experiments/X-AEM-005-universal-shadow-atlas/run.py --source 291
python -B -S experiments/X-AEM-005-universal-shadow-atlas/run.py --gap 37
python -B -S experiments/X-AEM-005-universal-shadow-atlas/run.py --full aua-full.json
python -B -S experiments/X-AEM-005-universal-shadow-atlas/compare_parent.py --new-full aua-full.json --write aua-comparison.json
```

`--source` uses the finite atlas and the unbounded resonance guard on inputs
of the 8^k u-5 odd-u form. Other inputs receive the universal ENTRY identity,
which is deliberately not labelled a successful reduction. A NO_CERTIFICATE
output is a bounded-language miss, never a divergence claim.

The full artifact contains every finite input outcome, the uniform rules,
the isolated points and all family witnesses. Frontier hashes and counts
are bound by the canonical payload; rebuilding the atlas reconstructs every
frontier cell. The atlas budget is 18 simultaneous tail steps, with shifts
-5 through 11. That covers the whole admissible odd-shadow exponent menu
for k<=6, not for arbitrary k. It does not classify unequal-tail-clock
individual meetings or other source formulas.

The generator propagates affine endpoint functions in parameter cells.
The standalone verifier instead reconstructs whole-word numerators and odd
counts, checks uniform identities and exact source legality, and separately
checks all isolated positive meetings. Its gap compiler accumulates forward
congruences; its family construction solves CRT in the odd quotient b.
Neither implementation's agreement is independent mathematical acceptance.

`compare_parent.py` checks the parent's exact source Git blob before importing
it and requires its whole replayed grid hash to match the parent's canonical
artifact. This is a separate computational comparison, not a premise of the
new proof or an independent re-review of the parent. All prior files remain
unchanged; the cumulative union is reported, not installed into parent code.

The canonical envelope uses exact key sets and canonical typed JSON equality,
so Python's bool/int/float numeric aliases are not silently accepted. Self-tests
reject 24 resealed corruptions, five direct malformed witnesses, and four bad
gap inputs. The raw phase pair (2,1) remains a control against treating entry
or a closed transition grammar as synchronous successful coverage.
