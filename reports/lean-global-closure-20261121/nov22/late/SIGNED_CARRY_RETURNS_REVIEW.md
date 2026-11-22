# Scoped review of the late signed-carry return integration

Date: 2026-11-22. Verdict: **VERIFIED at the displayed statement scope.**

Reviewed source:
`research/lean-global-closure-20261121/CollatzGlobalClosure/SignedCarryReturns.lean`,
SHA256 `0af50217b1da102d8fdaf7f9d61fedcdaad75cbf059452d02dcd8b82b59fe5d7`.

The integrating reviewer read the complete new module and independently
compared the odd-source cap and nine-lattice proof with PR177 commit
`2efabba9a341839b67ed011d6b878b23730ee51d`,
`research/lean-exact-witness-global-20261121/lean/Collatz/LowGapGlobal.lean`.
The exact source and blob hashes are in
[signed-carry-returns-sources.json](signed-carry-returns-sources.json).

## Checked interfaces and reasoning

- `IntervalHyp` retains arbitrary powered complete child certificates and
  the same strict multiset grade. It is not an odd-source-only substitute.
- The odd-source cap advances the actual nonterminal source once. The
  target ceiling becomes exactly `3*q+2`; source one is handled by a
  kernel-decidable finite proof through twelve.
- The nine-lattice port splits the odd source modulo four. Dividing the
  target by four, or by two followed by the actual odd child, puts the
  recursive query inside the correctly funded cap. The even-powered-child
  alternative is excluded by the actual parity of that child.
- The three absorbing guards are sufficient inequalities and congruences
  for the actual positive target. The power-two guard uses signed debt
  congruent to one modulo four, so `9*q-debt` has the required phase.
- `compiled_return_rule` obtains the literal retained suffix from the
  all-word compiler, restricts the original induction hypothesis by the
  proved strict prefix deletion, and transports the resulting basin
  statement back along the actual target orbit.
- The first-gap-one, first-prefix-two-one, and valuation-one psi conclusions
  agree with the credited PR177 scope. They do not assert unconditional
  closure for every convergent source.
- The explicit complete source `17:[2,3,4]` fails every enlarged prefix
  guard and ends with target `668`. This prevents interpreting the
  integration as a universal successful stopping theorem.

The previous frozen vendor remains unchanged. The port introduces no
new source axiom and no assumed return-cone theorem: the credited proofs
are present in full.

## Evidence boundary

The source author supplied a strict development compilation with eleven
axiom reports. This semantic review does not relabel that execution as an
independent run. The integrating clean-checkout build, its source hashes,
and full audit are recorded separately when executed.

No verdict here extends to a universal stopping policy, later upstream
commits, all PR177 files, or the analytic arguments on neighboring branches.
