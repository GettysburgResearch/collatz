# Mixed-radix rewriting: exact source boundary and a newly located barrier packet

**Status: SOURCE-QUALIFIED literature note.** The public source repositories were
read at the pins below. The supplied finite 22-witness checker was replayed.
The Nashida paper's general nonexistence arguments have not been independently
proved in this pass, and its Lean project was not rebuilt here.

## 1. The original source is Yolcu--Aaronson--Heule

Emre Yolcu, Scott Aaronson, and Marijn J. H. Heule, *An Automated Approach to the
Collatz Conjecture*, Journal of Automated Reasoning 67, article 15 (2023),
DOI [10.1007/s10817-022-09658-8](https://doi.org/10.1007/s10817-022-09658-8),
earlier preprint [arXiv:2105.14697](https://arxiv.org/abs/2105.14697).

The official reproducibility repository was frozen at
[`8a4dfda60f97a6d33ff0a24fdfa7a172d4bec340`](https://github.com/emreyolcu/rewriting-collatz/commit/8a4dfda60f97a6d33ff0a24fdfa7a172d4bec340).
Its [exact 11 rules](https://github.com/emreyolcu/rewriting-collatz/blob/8a4dfda60f97a6d33ff0a24fdfa7a172d4bec340/rules/collatz-T.srs), in the source's ASCII alphabet, are:

```text
ad -> d     bd -> gd
ae -> ea    af -> eb    ag -> fa
be -> fb    bf -> ga    bg -> gb
ce -> cb    cf -> caa   cg -> cab
```

The symbols `a,b` are binary digits, `e,f,g` ternary digits, and `c,d` the
boundaries. These are the boundary-coupled Collatz rules. The value-preserving
base swaps alone are not the Collatz termination problem. The journal theorem
3.17 establishes the equivalence of full termination and Collatz convergence;
that is inherited prior art, already recognized by this project.

The original unary matrix-interpretation obstruction is also not a statement
that every possible order on the mixed-radix system is impossible. Any proposed
order must identify its alphabet semantics, permitted contexts, well-founded
domain, and exact rule orientation obligations.

## 2. Nashida's October 2026 paired preprints

Two relevant source repositories were located through the Collatz Conjecture
Challenge's literature catalog. Both describe revision r3, October 2, 2026.

| Source | Exact read pin | DOI |
|---|---|---|
| Hiroyuki Nashida, *Expanding cycles are not enough: a dichotomy for termination certificates of generalized Collatz maps* | [a138adb7c7efaec8addd06722f40f015c7f2d9be](https://github.com/harappa/collatz-termination-certificate-dichotomy/commit/a138adb7c7efaec8addd06722f40f015c7f2d9be) | [10.5281/zenodo.23081447](https://doi.org/10.5281/zenodo.23081447) |
| Hiroyuki Nashida, *Dimension-free barriers for matrix interpretations of the Collatz rewriting system, and the maximal one-class weakenings of the modulo-8 conjectures of Yolcu, Aaronson and Heule provable by finite abstractions* | [8e7d6da6319c1c1b36ce3549fe06e00d0586a025](https://github.com/harappa/collatz-matrix-interpretation-barriers/commit/8e7d6da6319c1c1b36ce3549fe06e00d0586a025) | [10.5281/zenodo.23081491](https://doi.org/10.5281/zenodo.23081491) |

The primary README texts distinguish their formalized results from the paper-only
claims. Both also disclose substantial Claude assistance and the absence of
independent human mathematical review. These facts are reasons to preserve
exact proof scope, not reasons to accept or reject the mathematics by authorship.

### Claimed barriers: narrower than “all matrix orders fail”

Part I concerns generalized maps branching on residues modulo powers of two,
with odd affine numerators. Its finite abstraction distinguishes components
that combine an expanding cycle with branching from those that do not. It
claims a dichotomy for its specified staged certificates, built from size,
valuation information at finitely many rational periodic points, and finite
state weights. It further claims barriers for specified positive/arctic or
primitive-dominant-block weighted automata with positive growth.

Part II applies this to the 11-rule YAH system. Its abstract's dimension-free
claim retains substantive hypotheses: nonnegative affine matrix
interpretations weakly orienting all rules, and an exponentially growing
dominant relevant block whose semigroup contains a positive matrix. It also
states a restriction for relevant diagonal pairs in upper triangular
interpretations and a local-window additive-rank barrier.

This is not a license to state that arbitrary matrices, ordinal orders,
unbounded-state methods, strategy-specific orders, or all nonlinear arithmetic
ranks have been ruled out. The paper-only barrier proofs were not available as
Lean theorems in the supplied source; those claims remain SOURCE-QUALIFIED here.

### What the authors say is formalized

Part I's repository formalizes the soundness of a finite certificate checker and
five generalized-map termination examples. Its README explicitly excludes its
classification completeness, nonexistence arguments, and automaton barriers
from the Lean formalization.

Part II formalizes seven weakened residue-hitting claims for a hypothetical
nonconvergent positive shortcut orbit. For example, such an orbit is claimed to
hit one of `5 mod 8`, `7 mod 8`, and `4089 mod 16384`. This has an exception set;
it does not prove an orbit must converge. Its README explicitly says the matrix
barriers and the maximality theorem are not formalized. The source and stated
axiom reports were inspected; this pass did not rerun Lean or inherit an
independent formal-review verdict.

## 3. Exactly what was replayed

From Part II at the pin above, the following two files were fetched and executed
in scratch without modification to their content:

| File | Git blob SHA |
|---|---|
| `computations/check_theorem83.py` | `55c86d69192031d60bfa1040051b85ed9ecb2ff5` |
| `computations/theorem83_witnesses.csv` | `0a7c74f49af854298ea324ab1e6fd123c6b8ef7b` |

The invocation was `python -B check_theorem83.py`, with its directory as the
working directory. It completed with exit code zero, reported 22 witness rows,
zero failures, and `ALL OK`. Its four nontrivial minimal-forbidden-word counts
were 7, 5, 3 and 7 for the respective YAH conjectures. The replay verifies the
author's finite table checks. It does not independently validate the general
entanglement theorem on which the maximality argument also depends.

No third-party source is needed by the new `rank_envelope.py`. The temporary
Nashida checker copies are not part of the proposed original-code deliverable.

## 4. Consequence for this research pass

Repeated finite-dimensional searches need a more careful rationale in light of
these sources. Before scaling one, establish that its certificate class lies
outside the claimed obstruction or independently audit the barrier it would
challenge. An inconclusive SAT search does not establish nonexistence.

The constructed envelope in [RANK_ENVELOPE.md](RANK_ENVELOPE.md) instead uses an
input-dependent finite computation over actual prefixes and future positions.
It is not a fixed finite observation dictionary. Its purpose is also different:
bounded transport with preserved rank counts, followed by an explicit remaining
contact-return inequality. It makes no claim to orient all 11 rewriting rules,
so it does not purport to refute any YAH or Nashida barrier theorem.

The strongest useful next audit of the Nashida source would reconstruct the
claimed Terras-preimage typicality argument and the precise reduction from a
mixed-radix matrix interpretation to a value-level ranking function. The
existing Lean files cannot, by themselves, settle that audit.
