# T-6807 — Acyclic first-crossing failures are at least two-thirds-scale far from mechanical

**Claim ID:** `T-6807`  
**Status:** **PROPOSED / SOURCE-QUALIFIED**  
**Agent:** `gpt56-positive-entropy-01` (`GPT-5.6 Pro`)  
**Issue:** #75  
**Date:** 2026-07-31  
**Dependencies:** `L-6808`; PR #82 `L-6605` bank--displacement uncertainty; the quoted Rhin bound  
**Scope:** unbounded acyclic canonical first-crossing target-failure families

## 1. Statement

Let \(v_j\) be coefficient-first-crossing words of lengths \(j\to\infty\).
Assume:

1. the least positive parity-cylinder representative does not descend at the
   crossing; and
2. the represented segment contains no repeated physical state.

Let

\[
I_j
\]

be the exact adjacent-swap distance from \(v_j\) to the corresponding
upper-mechanical extremizer.

Then

\[
\boxed{
\liminf_{j\to\infty}
\frac{I_j}{j^{2/3}}
\ge
\left(\frac{\alpha}{2}\right)^{2/3},
\qquad
\alpha=\frac{\log2}{\log3}.
}
\tag{1}
\]

Numerically, the constant is

```text
0.4634120707...
```

for orientation only.

This strengthens the square-root lower bound of PR #82 `T-6610`.

## 2. Imported return uncertainty

PR #82 `L-6605`, using the exact return barrier and the Rhin lower bound,
proves

\[
(I_j+1)
\left(
B_j+\alpha+14.3\log_3j+\log_3(3/2)
\right)
>
\frac{\alpha(j-2)}2,
\tag{2}
\]

where \(B_j\) is the maximum proper-prefix coefficient bank.

## 3. Eliminate the bank

`L-6808` gives

\[
B_j<\sqrt{I_j}+1.
\tag{3}
\]

Combining `(2)--(3)`,

\[
\boxed{
(I_j+1)
\left(
\sqrt{I_j}+1+\alpha+14.3\log_3j+\log_3(3/2)
\right)
>
\frac{\alpha(j-2)}2.
}
\tag{4}
\]

This is an explicit all-length necessary inequality.

## 4. Asymptotic extraction

If \(I_j/j^{2/3}\) is unbounded, `(1)` is automatic.  Otherwise pass to a
subsequence on which

\[
\frac{I_j}{j^{2/3}}\longrightarrow t<\infty.
\]

Divide `(4)` by \(j\).  The logarithmic terms are negligible compared with
\(j^{1/3}\), and the left side tends to \(t^{3/2}\).  Therefore

\[
t^{3/2}\ge\frac{\alpha}{2},
\]

which is equivalent to `(1)`.

## 5. Structural consequence

The remaining acyclic Box-2 obstruction is not merely outside every fixed or
polylogarithmic repair class.  It must carry integrated mechanical
displacement on the scale

\[
\boxed{I_j=\Omega(j^{2/3}).}
\]

Together with `T-6806`, every surviving first-crossing obstruction is now:

```text
nonmechanical;
a genuine modulus wrap;
outside the short-return and narrow-corridor certificates;
and at least two-thirds-scale far from the remainder extremizer.
```

## 6. Gap audit

- The theorem remains source-qualified at Rhin's logarithmic-form bound.
- \(j^{2/3}\)-scale and larger displacement families remain open.
- A repeated physical state is the positive-cycle alternative.
- The theorem does not control the complete-denominator residue of the
  displacement numerator.
- It does not prove Box 2 or Collatz.
