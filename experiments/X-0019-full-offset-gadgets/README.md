# X-0019 — Full-offset collision gadgets and correlated selectors

Experiment ID: `X-0019`  
Issue: `#2`  
Agent: `gpt56-pro-01`  
Status: `EMPIRICAL` exact finite certificate for `O-0012` and `T-0041`

## Questions

1. Among weight-`b` parity words of length `6b`, does one collision signature contain every normalized offset modulo `3^b`?
2. Does this hold through the largest practical exact standard-library census in the packet?
3. Can the resulting gadget correct every member of the dyadic-prefix family by correlation rather than Cartesian concatenation?
4. Do the correlated words collide modulo `3^(2b)`?
5. Do their inverse roots project bijectively modulo `2^b`?
6. How long is the shortest common odd tail making each finite selector supercritical?

## Method

For every `1 <= b <= 6`, `run.py` exhaustively enumerates all

```text
binomial(6b,b)
```

weight-`b` words. It computes `B(w) modulo 3^(2b)`, groups by the low signature modulo `3^b`, and represents the high normalized lift by a Python integer bitset.

For the first complete signature it freezes one lexicographically first word for every high offset. It then:

- builds all `2^b` dyadic-prefix words from `L-0010`;
- chooses the unique suffix offset prescribed by `T-0041`;
- verifies one common constant modulo `3^(2b)`;
- checks complete inverse-root projection modulo `2^b`;
- computes the shortest common all-odd supercritical tail.

No repository implementation is imported.

## Replay

```bash
python3 -m py_compile experiments/X-0019-full-offset-gadgets/run.py
python3 experiments/X-0019-full-offset-gadgets/run.py
```

Expected output:

```text
full-offset gadget and correlated-selector checks passed
b=1 signature=1 complete=2 represented=6 branches=2 core=8 tail=9 final=17
b=2 signature=2 complete=1 represented=46 branches=4 core=16 tail=17 final=33
b=3 signature=20 complete=1 represented=430 branches=8 core=24 tail=25 final=49
b=4 signature=65 complete=1 represented=4042 branches=16 core=32 tail=34 final=66
b=5 signature=11 complete=4 represented=38269 branches=32 core=40 tail=42 final=82
b=6 signature=20 complete=90 represented=352411 branches=64 core=48 tail=50 final=98
semantic_sha256=dcef1b6e1e34b640ae817cdd4e760cc75228c78e42348d440a5c655bc5fe2f0d
```

The authoring replay completes in a few seconds in the available Python environment. Timing is informational only.

## Limitations

- Exhaustive validity through `b=6` is not an all-`b` theorem.
- The experiment certifies low-bit selector geometry, not causal placement around the refund one-counter map.
- A complete selector still erases its branch at the common collision output; orientation and top-boundary regeneration remain open.
- No positive Collatz counterexample is claimed.