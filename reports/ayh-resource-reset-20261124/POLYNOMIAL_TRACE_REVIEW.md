# Independent review of the 41-to-161 polynomial obstruction

**Verdict.** Verified for the usual componentwise weak order on a positive
natural cone of dimension one, two, or three, with strict comparison
requiring in addition a strict increase in the first coordinate. The
binary-zero operation has nonzero coordinate polynomials with nonnegative
integer coefficients. Each other letter may have an arbitrary self-map
of the cone that preserves both comparisons. No one of the eleven full
mixed-base rules can be uniformly strict when all are weakly oriented.

## Contents reviewed

| Source path at review | SHA-256 of the exact file |
|---|---|
| `research/ayh-resource-reset-20261124/SelfEmbedding.lean` | `52359f2a73f0d7f4f641b8947fef972bd01316b6ddd9abf6fb102b0b4cb5ff8a` |
| Agent draft `agent_global/PolynomialPump.lean`, to be integrated under the packet directory | `5da0e085baedfd4ed5b78c5b961021a1a06e3713934531fd4885dd12fd3a8fce` |

I ran both exact files separately with Lean 4.34.1 and
`-DwarningAsError=true`. Both exited successfully. The trace declaration
`certificate41` printed no axioms and `no_strict_rule_of_zero_stutter`
printed only `propext` and `Quot.sound`. This review checks the mathematical
bridge joining the two files. It does not cover later source edits.

## Polynomial comparison

Let \(u_n=F^n(x)\). On strictly positive inputs every monomial containing a
variable \(x_i\), with coefficient at least one, is at least \(x_i\).
Consequently an occurrence of coordinate i in output j gives
\(u_{n,i}\le u_{n+1,j}\). Each output is nondecreasing separately in its
used variables and independent of the remaining ones. These statements
also hold for the expression representation in the Lean file after
zero-coefficient terms are omitted.

First-coordinate strictness forces the first polynomial to use the first
variable. Otherwise the positive states (1,1,1) and (2,1,1) separate its
required strict outputs but give identical values. It follows that
\(u_{n,0}\le u_{n+1,0}\) at every step. The argument permits this
variable to occur only in a mixed or higher-power monomial.

For either of the two other coordinates, call it y and the remaining one z.
If y uses itself, y is nondecreasing. If y and z use each other, following
the two dependency edges gives \(y_n\le y_{n+2}\) for every n. Otherwise,
if y does not use z or itself, it depends only on the first coordinate
and is nondecreasing after the first iteration. In the remaining case,
y uses z and z does not use y. Then z either uses itself, giving
\(z_1\le z_3\), or depends only on the first coordinate, also giving
\(z_1\le z_3\). Comparing y's input at times 1 and 3 therefore proves
\(y_2\le y_4\). Exchanging y and z yields \(F^2(x)\le F^4(x)\)
componentwise. Dimensions one and two embed by adding unused
constant-one coordinates. This proof does not impose a degree bound.

## Rewrite comparison

I independently replayed the 32 rule indices from `used41` using the
ASCII rules in the authors’ published companion repository. At every
step the specified left-hand side had exactly one occurrence. The
zero-based positions in the successive words were

```text
5 4 3 2 1 0  5 4 3 2 1 0  5 4 3 2 1 0  6 5 4 3 2 1 0  6 5 4 3 2 1 0
```

The endpoints were `cabaabd` and `cabaaaabd` and the used indices were
exactly 0 through 10. With the implicit leading binary one, those
endpoints denote 41 and 161. In the left-outermost convention they have
the common context `cab` before the affected block and `bd` after it.
The comparison for \(F^2\) and \(F^4\) gives weak **increase** from
the first word to the second. Weak orientation of all the rules gives
the opposite comparison, and any single uniformly strict rule gives a
strict decrease along this very trace. Thus there is no first removable
rule in this class. [Authors’ rule list](https://github.com/emreyolcu/rewriting-collatz/blob/main/rules/collatz-T.srs)

The proof requires all intermediate states in this comparison to belong
to the positive cone. It does not cover identically zero coordinates
which send the interpretation outside that cone, weak-only symbol maps
in a marked top-termination system, arbitrary ordered algebras, or all
dimensions. The 32-step witness starts and ends at distinct integers
and provides no Collatz cycle.
