# Carry births, binary substitution rigidity, and cycle components

**Collatz remains OPEN.** This packet contains new written research with separate
independent reconstructions, finite exact controls, and separately scoped Lean
verification. It supplies neither universal convergence nor a positive counterexample.
The execution report records exactly which finite formal statements were checked.

The underlying map is the accelerated map on positive odd integers,
`U(q)=(3q+1)/2^g(q)` with `g(q)=v_2(3q+1)`. The cycle polynomial uses the shortcut
map with one division by two at every clock; its length A and odd count p are
stated separately. These clocks have not been identified with one another.

## New results

| Claim | Result | Exact boundary |
|---|---|---|
| ABR-1 | The actual carry support has a weighted partition bounded by `D*lambda^(B-m)`. This gives finite-window conditional entropy coefficient `d=0.285859533495646...`, improving PR189's `0.541528190506...`. | The entropy is conditioned on the actual canonical word; its complexity is not removed. |
| ABR-2 | An injective ordinary orbit with subexponential canonical factor complexity has running-maximum height exponent at least `1/d=3.49822161875...`. The same exponent is necessary for its canonical prefix maximum using PR182 R12-1. | These are necessary growth bounds. No contrary bound for every ordinary source is proved. |
| ABR-3 | Every forward-invariant injective positive odd set in L actual scalar phases has `#(S intersect [1,X]) <= C L X^(17/25)`, with absolute C. | Injectivity on the whole set is essential. A single low-complexity orbit has the same exponent with a source-dependent constant. |
| ABR-4 | Every non-eventually-periodic fixed word of a nonidentity, non-erasing binary substitution has transcendental physical completion when its two physical gap blocks have different inverse-map fixed points. | Extends PR190 beyond uniform and primitive substitutions. Larger substitution alphabets with a binary coding and arbitrary ordinary itineraries remain outside the theorem. |
| ABR-5 | Every primitive contracting word of clock gcd g has nonzero top determinant precisely for `g=1` or prime-power g other than 4, with the explicit odd-b refinement at g=4. | Nonvanishing alone is not a numerical norm saving. Explicit primitive rational examples show the failure in all remaining gcd classes. |
| ABR-6 | A full binary tree of positive ordinary sources has one canonical phase, carries at most 16, gaps at most 50, and polynomially many sources charging to endpoint 1 at the occupation proof's horizon. | These sources all converge. The construction tests the attempted extension of ABR-3 to a branching basin. |
| ABR-7 | All eight fixed affine substitutions between PR191's two-gap dictionaries with clocks three and five are classified. Every shrinking slope requires `83 divides q+7`; a second smaller shadow has slope `61/83`. | State-dependent substitutions and changing clocks are not classified. The result does not cover every residue of a hypothetical least nonconverger. |

These identifiers refer to the corresponding statements in this packet; their
source predecessors retain their own IDs and review boundaries.

### Subsequent synthesis with PR192--193

The [latest-source synthesis](LATEST_SOURCE_SYNTHESIS.md) records a further
frozen-head review after the initial publication. It derives stronger
same-orbit congruence separation, the full numerical denominator bound
`21d >= 32^(g/s-1)` for ABR-5's mixed-prime family, and the exact guarded-visit
constraint `64r >= 81n+49` for a least nonconverger n. These are written
deductions; the Lean execution counts below are unchanged. PR192 independently
overlaps the prime-power survival part of ABR-5 and is credited in the synthesis.

## Proofs

- [Carry support, entropy, height, and phase-specific bounds](RUN_PARTITION.md)
  proves ABR-1--2. For the specific hypothetical phases `7/8` and `729/1456`,
  exact rational logarithm certificates give necessary running-maximum height
  exponents greater than **7.36** and **181.74**, respectively.
- [Global ordinary occupation](OCCUPATION.md) proves ABR-3. Its two clocks are
  the fixed odd-step horizon and the varying binary clock of a word.
- [Binary substitution extension and source review](MAHLER_EXTENSION.md)
  proves ABR-4 and reconstructs PR190 MPS-1--MPS-6. The fixed-letter case has a
  separate algebraic-to-rational argument; it is not a generic specialization
  of a transcendental bivariate series.
- [Top-component classification](TOP_COMPONENT.md) proves ABR-5, retaining the
  complete numerical denominator in the examples. Its algebraic input includes
  the stated classical rational binomial irreducibility criterion.
- [Ordinary inverse tree and affine-shadow classification](PHASE_TREE.md)
  proves ABR-6--7 and displays the complete finite residue certificate.

## Why the new entropy bound works

PR182's actual scalar is `h(q)=sum_i g(U^i(q))/3^(i+1)`. Write `h_i=p_i+k_i`,
where the canonical phase belongs to `(1/2,3/2]`, and put
`b_i=3p_i-p_(i+1)` in `{1,2,3}`. The exact edge equation is

```
g_i + k_(i+1) = b_i + 3 k_i.
```

When a carry is zero, the next carry is at most `b_i-1`. This restricts both
where a positive carry can begin and how large it can be when it begins.
The geometric weight `f(0)=1`, `f(c)=D*x^c` for positive c bounds the complete
legal carry count. At the specified algebraic x, its carry cost and canonical
digit cost cancel against the actual orbit's mean budget. This produces the
new constant without assuming independent gaps, mixing, or a generic phase law.

The ordinary occupation proof also retains the endpoint scalar bound. At fixed
binary clock and starting phase, the first m carries recover the last carry and
then the full gap word. The high-clock part maps injectively below X/2. The
low-clock part uses the weighted count and the literal dyadic source residue.

## Review and provenance

The [execution and review index](../../reports/astra-independent-review-20261124/README.md)
separates written proofs, exact computations, Lean source compilation, and
repository-integrity checks. It includes the full queried source heads, the
root reconstruction, the independent stationary audit, and the additional
cross-review of the substitution theorem.

Three GPT-6.2 Astra subagents worked in parallel with the root. The stronger
bounded-birth weight was derived by the root after the stationary agent's run
count and reconstructed by both mathematical agents. The arithmetic agent
derived the cycle classification and inverse tree. The stationary agent derived
the nonprimitive substitution extension; the arithmetic agent and root
independently checked its load-bearing cases. Agreement is not used as a proof
step: the arguments and their exact assumptions are written in the linked files.

**Attribution correction:** PR189 S1 rederives PR180's earlier strict stationary
collision-gap theorem. This is recorded in the source audit; it is not counted
as a new result of this packet. PR182's critical-mean zero-complexity branch
already has a stronger superpolynomial growth conclusion than ABR-2 in that
special case. The earlier bounds retain that credit.

## What would still close the problem

An escape proof must now supply ordinary-source arithmetic beyond the symbolic
restrictions: for example, force an opposing canonical-complexity/growth bound,
or produce a successful smaller-source construction with a terminating rule.
The new substitution theorem does not imply that arbitrary ordinary schedules
have substitution structure. The explicit inverse tree shows why the global
injective occupation count cannot simply be charged to an entire predecessor
basin. Its lower exponent is smaller than 0.68, so it refutes that charging step,
not every possible proof of a numerical basin bound.

An all-cycle proof still needs a strict saving for the full numerical gcd, or a
complete smaller-cycle construction. A nonzero top determinant can be divisible
by the full factor. Primitive rational examples can cancel an entire top
cyclotomic component. The affine-shadow classification exposes the exact residue
class missed by that particular family of ordinary substitutions.

Neither missing inference is replaced by finite computation, a changing source
at each horizon, an arbitrary 2-adic completion, or an assumption of Collatz.

## Exact finite replay

From this directory run the following programs normally and with `python -O`:

```
python -B check_run_support.py
python -B check_top_component.py
python -B check_phase_tree.py
python -B check_triangular_scripts.py
```

Their output and source bindings are recorded in the execution report. They
check bounded identities and explicit finite certificates; they do not prove
the infinite entropy, transcendence, or cycle-classification arguments by
enumeration. No assertion-based check is silently removed under optimization.
