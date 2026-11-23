# Scoped review: direct ordinal interpretations

Date: 23 November 2026. Reviewer: cycle lane, independently reconstructing
the coordinating root's written argument.

**Verdict: VERIFIED for the two interpretation obstructions and the
termination of the two-rule subsystem in Section 2, at the file hash below.**
This is a written mathematical review, not a Lean build or a verification
of the full Collatz rewriting equivalence.

## Frozen subject

- Path: `research/global-closure-20261123/ORDER_CONSTRUCTION_ATTEMPT.md`
- SHA-256: `89dbbfd7009b869fae54a60ac7cf1db999e05bf809a12bf2614e2096d0a03f0e`
- Claim scope: Section 2's direct strictly increasing interpretations on
  one nonempty total well-order; its weakly monotone simple variant; and
  the termination of the subsystem consisting only of
  `bd -> gd` and `cg -> cab`.

## Independent reconstruction

For a strictly increasing self-map \(a:L\to L\) of a well-order, suppose
\(a(y)<y\) for a least such \(y\). Set \(z=a(y)\). Minimality gives
\(a(z)\ge z=a(y)\), whereas strict increase at \(z<y\) gives
\(a(z)<a(y)\). This contradiction proves \(a(y)\ge y\) everywhere.

Under the stated convention \([uv](x)=[u]([v](x))\), weak orientation of
`cg -> cab` gives
\[
c(g(y))\ge c(a(b(y))).
\]
Strict increase of \(c\) on a total order reflects this inequality, so
\[
g(y)\ge a(b(y))\ge b(y).
\]
Choosing any \(x\in L\), which uses nonemptiness, and setting \(y=d(x)\)
contradicts strict orientation of `bd -> gd`. Neither the ordinal
height nor a finite-dimensional restriction was used.

For the second version, simplicity supplies \(a(t)\ge t\), and weak
monotonicity of \(c\), together with strict orientation of
`cg -> cab`, implies \(g(y)>a(b(y))\). Indeed, the reverse weak order
would force the reverse weak order after applying \(c\).
This again contradicts `bd -> gd`. The argument requires the stated
single total order and simplicity; it is not a result about all
well-founded partial orders or arbitrary extended algebras.

The two-rule subsystem does terminate. Every original occurrence of
\(c\) can be used by `cg -> cab` at most once: the created immediate
right neighbour \(a\) cannot be removed or changed by either of these
two rules. No rule creates a new \(c\). If the original word has \(c_0\)
copies of \(c\), then the number of `cg -> cab` uses is at most
\(c_0\). Each such use creates one \(b\); `bd -> gd` consumes one.
If the initial \(b\)-count is \(b_0\), there can be at most \(b_0+c_0\)
uses of `bd -> gd`. Thus every reduction has at most \(b_0+2c_0\)
steps.

## Correction and boundaries

A minor first-rule/second-rule naming ambiguity in the count paragraph was
reported. The author replaced the count labels with the actual rule names;
the hash above binds that corrected wording. No mathematical premise or
conclusion needed repair.

The verdict does not extend the two-rule termination proof to the full
eleven-rule system. Other rules can move or change neighbouring letters,
so the two-rule permanent-neighbour argument cannot be transferred
unqualified. It also does not verify the imported Aaronson--Yolcu--Heule
simulation theorem or the earlier PR141 certificates.

The global construction remains open: an interpretation outside the
excluded direct class, or a source-dependent arithmetic rank with an
all-time supplied annotation, would require its own update and existence
proof. The obstruction is consistent with termination of the displayed
subsystem and makes no claim against Collatz convergence.
