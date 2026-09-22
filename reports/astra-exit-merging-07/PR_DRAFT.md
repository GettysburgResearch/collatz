# research: actual escape restarts with a common contracting parameter

Continuation of #132; credits #129 R/valuation mechanisms and #125 original
companions. **AER-001–004 PROPOSED pending independent mathematical review.
No complete Collatz proof or global successful selector.**

Parent: `7687eec1ac364009d644cb8d015f1fe3b28730cc`.
Only additions under the three new research/experiment/report directories.
No earlier proof, canonical status, workflow, setting, license or main edit.

## Mathematics

The positive comparison K(E)=(9E-10,E) has an exhaustive two-step table. Its
E=2 mod4 row returns to R(D)=(3D-4,D), giving an actual R restart on
D=13 mod16. Two further R returns cover D=23 mod32 and D=191 mod32768.
The last passes through an expanding eleven-step return, then contracts only
when the next four-step return's guard holds. G alone is not a rank decrease.

Together with the credited D=2 mod4 return, all four rules satisfy
`0<=D_next-2<=(6/7)(D-2)`. Thus arbitrary ACTUAL interleaving terminates
unconditionally in O(log D) stages at a merger or an explicit failed guard.
It does not choose new parameter digits or reset separate valuation ranks.

Every finite word in these four rules has one exact successful cylinder when
followed by the six-step merger on D=12 mod64. Words starting with any new
rule lift to entire H classes rejected immediately by the exact #129 selector.
A first cylinder is C=7759+8192t:

```
T^13(9C+2)=T^13(C)=2187t+2072.
```

CRT lifts give original companions m=(N-3)/4<N/4 and, for sufficiently long
first odd runs, no descent anywhere on the original arm. The divisible-by-3
specialization also has no smaller pure ancestor at any backward depth:

```
N=499228671, m=124807167;
T^28(N)=T^26(m)=2161541018;
min_{1<=j<=28}T^j(N)=748843007>N.
```

## Evidence and unresolved boundary

135,584 deterministic rows include all 65,535 R normalizations on D=2..65536,
4,095 K rows, 386 whole finite-word cylinders, 24 original lifts, and both
classifications on every C=1..65536. The old 5,082 #129 certificates are
preserved exactly; 173 more are supplied, 54 at C=2 mod3. There remain 60,281
OUTSIDE outcomes. This is NOT a comparison against all later #130/#131 gates,
a convergence census, or a fraction of Collatz resolved.

The independent verifier imports no kernel/generator/project module and
reconstructs every selector outcome from raw states, including OUTSIDE. It
checks whole affine progressions, exact experiment coverage, original clocks,
all-state bounds and the core controls. Its self-test rejects 23 direct
semantic witness mutations, four inventory mutations and five JSON/type
controls, not separately resealed full-corpus mutations. See validation.json
for actual normal/optimized execution and separate packet-application evidence.

No independent mathematical review, root complete-checkout validator, Lean
build or remote CI was run by the author. Fresh publisher evidence belongs in
separate receipts. The other K rows and remaining R/H exits are still open;
C=17 and C=71 remain failures of this selected language despite actual isolated
mergers. The fixed H(2) pair remains permanently out of phase synchronously.

Read `research/astra-exit-merging/escape-restarts/PROOF.md` first, then the
experiment README and original-source/negative-control boundaries.
