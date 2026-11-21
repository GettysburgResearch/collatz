# Independent mathematical review of the mixed-base attempt

**Verdict: the reviewed ordinary arithmetic, grammar, rank, and conditional
induction arguments passed. The universal blocked-erasure merger cover
remains OPEN.**

The arithmetic lane independently reconstructed the following material on
2026-11-21. This is an internal mathematical review, separate from the Lean
compilation and the integrated axiom audit.

## Reviewed base versions

| File | SHA-256 |
|---|---|
| `CONSTRUCTIVE_NORMAL_FORM.md` | `d1227adf06e0721cacf5b5d24c24567ed9e79a42a88f4dc96112706f82c3cc43` |
| `MixedBaseNormalForm.lean` | `f1a650673ce63e6a2ead331b9d8ce263457b377c1922faab6676be0ca390095a` |

The reviewer checked:

- The numeric interpretations of all ten retained rules, including their
  exact zero or one ordinary shortcut clocks.
- The complete written irreducible grammar, its necessity and sufficiency,
  and the distinction between that written characterization and Lean's
  necessary blocked-suffix theorem.
- The rightmost ternary suffix formula
  \(n=3^k(6q+1)+r\), with \(q\ge1\) and \(0\le r<3^k\).
- Every required affine rank difference, recomputed from the five supplied
  matrices. Each required first-coordinate difference is strictly
  positive and each second-coordinate difference is nonnegative.
- Strict ordinary-value and same-rank decreases for erasure in arbitrary
  finite mixed contexts.
- Positivity of canonical representations and representation of every
  positive ordinary input.
- The strong induction using that one rank to prove
  `BlockedErasureCover ↔ Universal`, with the merger hypothesis retained.
- The displayed numerical traces and their exact ordinary clocks.

No mathematical or ordinary-quantifier gap was found in that scope. A
wording correction was accepted: the final open obligation now refers to
“one blocked-erasure candidate,” because the cover permits any blocked pair,
whereas the displayed numerical formula is for the rightmost pair with a
ternary suffix.

## Subsequently reviewed constructive extension

The arithmetic reviewer separately checked the added arbitrary-prefix
`f11` merger and its odd-length all-ones suffix extension.

For every finite mixed prefix with value \(q\ge1\), set

\[
n=18q+4,\qquad m=6q+1.
\]

The first is even, the second odd, and

\[
T(n)=9q+2=T(m).
\]

Erasing the blocked ternary digit from `pre ++ [f,o,o]` gives exactly
`pre ++ [f,o]`, so the previously reviewed ordinary-value and rank
inequalities apply. The new formal statement
`terminal_double_one_merger` supplies the common endpoint.

For a rightmost suffix \(1^k\) with odd \(k\ge1\), the reviewer also
checked

\[
r=\frac{3^k-1}{2}\text{ is odd},\qquad
m=2q\,3^k+r\text{ is odd},\qquad
n=3^k(6q+1)+r=3m+1.
\]

Thus \(n\) is even and the same merger clocks \(a=b=1\) work. This
written extension makes no claim about other ternary suffixes.

## Final assembled files and separate execution evidence

After the reviewed extension and wording correction, the only Lean proof
changes were compilation fixes: naming the surviving dependent-case index,
unfolding the concrete pair order when deciding its two numerical
inequalities, and removing one unused simp argument. The theorem statements
reviewed above were unchanged by these fixes.

| Final assembled file | SHA-256 |
|---|---|
| `MixedBaseNormalForm.lean` | `41b74fb820e3523aff493c9826186d4a06e6ce222bb42ac398d6258601424a0e` |
| `CONSTRUCTIVE_NORMAL_FORM.md` | `d3b7afca3e48125bb679963fe3c9c2cd1879add8ef1d4639db3a270621f8fe0d` |

The merger lane's focused Lean 4.34.1 command used `-j 1` and
`-DwarningAsError=true`. It completed with exit zero, no diagnostics, and
25 public theorem declarations. The compiled `MixedBaseNormalForm.olean`
has SHA-256
`d2f6a7c8c341c81b1839ac7fd0d41dc3c0eb0526fe48f535af8c5a2f77cbb996`.
The integrated build receipt supplies the packet's separate axiom-audit
status.

The independent reviewer did not run Lean for this review and did not audit
the external literature's theorem statements. The review does not convert
the conditional cover into an unconditional Collatz proof.
