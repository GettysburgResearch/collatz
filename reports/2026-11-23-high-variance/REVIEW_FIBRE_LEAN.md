# Independent reconstruction: finite fibre algebra

Date: 2026-11-23. Reviewer: `analytic_gluing`, different from the Lean author.

**Verdict: VERIFIED at the two finite real-algebra statements below.** This
is a source/proof reconstruction. The compiler execution and transitive
axiom evidence are recorded separately in `lean-check.json` and
`lean-build.log`; the reviewer did not rerun the compiler.

## Exact reviewed bytes

| File | SHA256 |
|---|---|
| `research/high-variance-20261123/lean/FibreReconstruction.lean` | `d81acc83862914d097261ef92753ef1455bded005e291db3088a0b1c46a71cec` |
| `research/high-variance-20261123/lean/FibreAudit.lean` | `91af2030f41f788084fdc5bbc503f00e7238e71679caea63c73b01d4f5c65076` |

The audit imports the proof module and names exactly its two public
theorems. The private weighted-variance lemma is not counted as a public
declaration. This review does not extend to later source bytes.

## 1. `coherent_edge_increment`

The hypotheses are real numbers satisfying `p*q' = 3*q+1`,
`p*a' = 3*a`, with `a` and `p` nonzero. Cancelling the common nonzero
factor `p` gives

\[
 q'/a'=(3q+1)/(3a).
\]

Subtracting `q/a` proves the exact increment `1/(3*a)`. The hypotheses
also force `a'` nonzero, although the chosen cancellation lemma handles
the intermediate quotient directly. The body uses this cancellation,
field normalization and a polynomial identity. Its required denominator
hypotheses are present.

For the written ordinary-orbit application, `p=2^e` and `a,a'` are the
positive homogeneous multipliers. The theorem deliberately works for
any nonzero real scale. It neither asserts an integer orbit exists nor
proves that the supplied edges are selected by parity.

## 2. `finite_fibre_reconstruction`

The statement retains an arbitrary finite set, real weights `w`, real
coordinates `z`, their given total weight one, and their given weighted
mean `m`. It assumes that every used `z`, `m`, and `b` is nonzero.

The three conclusions reconstruct as follows:

1. Summing `w*z/m` gives `m/m=1`.
2. `1-(1-z/b)=z/b`; each reciprocal-fibre summand therefore equals
   `(b/m)*w`, and the sum is `b/m`.
3. The tilted first moment equals
   `1-(sum w*z^2)/(b*m)`. Expanding the original weighted squared
   deviations using the supplied total and mean gives
   `sum w*(z-m)^2 = sum w*z^2-m^2`. Subtraction yields the displayed
   variance quotient.

These are algebraic identities even for signed weights. The final
docstring correctly states that a probability-law interpretation also
requires nonnegative weights and positive coordinates and mean;
the formal statement does not assert those additional inequalities.
The physical fibre application also has a positive scale and coordinates
bounded above by that scale, which put the fibre in `[0,1)`.
Likewise, strict positivity of the variance gap is not a conclusion of
this theorem. The written infinite application supplies its own
positive law and proves nonconstancy separately.

## Scope and adjustments

The initial docstring described the probability application without
explicitly separating positivity from the actual formal hypotheses.
That wording was clarified during review; no statement or proof body
was altered. An unused tactic import was removed. The hashes above
bind the final documentation and import changes.

The finite declarations support the coherent-coordinate and size-bias
algebra in `ANALYTIC_GLUING.md`. They do not certify construction of the
canonical measure, the infinite conditional change of measure, fibre
limits, perfect or full-dimensional support, the routing input,
entropy comparisons, or Collatz convergence. No `sorry`, admitted
lemma, custom conjectural axiom, or native decision shortcut occurs in
the reviewed source.
