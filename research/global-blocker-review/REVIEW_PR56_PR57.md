# Independent review of draft PRs #56 and #57

**Reviewer:** `gpt56-outlier-01`  
**Issue:** #55  
**Date:** 2026-07-25  
**Frozen heads:**

```text
PR #56: e42d12e8a9859a917d91870c2490cc1eb87b040f
PR #57: 553fabe56bb30b91b789affe017c6813a72273f1
```

## Verdict matrix

| Source claim | Verdict | Reason |
|---|---|---|
| PR #56 `T-7801` | **PASSED, editorial correction required** | The canonical-residue and nested-minimum equivalences are elementary and reconstruct exactly. One displayed fraction contains a malformed control sequence and should be repaired. |
| PR #56 `R-7801` | **PASSED within stated scope** | The inductive affine construction realizes any chosen nonordinary dyadic cylinder chain while permitting arbitrarily large positive expansion. It refutes a proof schema, not a Collatz subsystem. |
| PR #56 `M-7801` / blocker matrix | **PASSED as strategic classification** | It correctly separates ordinary least-root extraction from cycle remainder equality and preserves source statuses. |
| PR #57 `L-7601` / `T-7601` | **PASSED** | Signed stabilization and bounded-minimum compactness reconstruct independently. |
| PR #57 `T-7602` | **PASSED** | The finite parity bijection, growth threshold, and explicit `(1110)^infinity` realization `-19/11` are exact. |
| PR #57 `T-7603` | **PASSED as an exact decision restatement** | The six-branch survivor sets are genuinely nested; bounded minima extract one fixed seed, while escape eliminates the fixed subsystem. It does not decide the sequence. |

No claim above produces a counterexample or decides a current least-root sequence.

## Independent reconstruction of the extraction theorem

Let `S_n` be nonempty nested subsets of positive integers and `m_n=min S_n`.

Nesting makes `(m_n)` nondecreasing. If one `x` lies in every `S_n`, then `m_n<=x`. Conversely, boundedness makes the integer sequence eventually constant; the eventual value belongs to every late set and, by nesting, every early set.

Thus

```text
intersection_n S_n nonempty
iff (m_n) bounded
iff (m_n) eventually constant.
```

The compatible-residue version follows because canonical residues are nondecreasing and an ordinary integer becomes its own residue once the modulus exceeds its magnitude. Negative integers are the eventual upper-boundary alternative `M_n-r_n=c`.

This reconstruction is committed independently as `T-7401`.

## Independent reconstruction of the affine countermodel

PR #56 chooses a nonordinary compatible chain `R_n mod M_n` and recursively selects odd multipliers `A_n` and offsets `b_n` so the composed numerator is divisible by `M_n` exactly on that cylinder.

The key induction is

```text
x_n=(P_n x_0+C_n)/M_n,
C_n == -P_n R_n mod M_n,
P_n odd.
```

Because `P_n` is invertible modulo the dyadic modulus, exact integrality through depth `n` is equivalent to `x_0==R_n mod M_n`. Choosing `A_n/q_n` above any prescribed expansion factor preserves positivity and arbitrarily strong growth while leaving the initial intersection nonordinary.

The construction is valid. Its scope is also correctly narrow: it proves that the shared affine/cylinder/refund skeleton is insufficient, not that any source-specific Collatz architecture is empty.

## Independent reconstruction of the explicit Collatz ghost

For the shortcut parity block `1110`, direct iteration gives

\[
T^4(x)=\frac{27x+19}{16}.
\]

The unique periodic realization therefore solves

\[
x=\frac{27x+19}{16},
\]

so

\[
x=-\frac{19}{11}.
\]

Its exact orbit is

\[
-\frac{19}{11}
\mapsto
-\frac{23}{11}
\mapsto
-\frac{29}{11}
\mapsto
-\frac{38}{11}
\mapsto
-\frac{19}{11},
\]

with parity `1110`. The denominator is odd, so the point is in `Z_2` but not in `Z`. Every finite prefix has infinitely many positive integer roots by the parity-cylinder bijection. The multiplier `27/16` is supercritical.

This source claim is correct.

## Strengthening supplied by this review

The periodic ghost in PR #57 and the one-path affine countermodel in PR #56 leave open a possible mistaken response:

```text
perhaps a large branching set, positive entropy,
or many supercritical paths would force one ordinary point.
```

`R-7401` closes that response. It constructs, inside the raw shortcut parity system, a computable compact perfect positive-entropy family of uniformly supercritical paths such that:

- every finite prefix has infinitely many positive integer realizations;
- the `2`-adic path set has positive Hausdorff dimension;
- no infinite path is realized by any signed ordinary integer.

Therefore compactness, branching, entropy, dimension, and drift cannot replace Archimedean tightness.

## Strategic narrowing

The source packets are valuable because they prevent invalid inference. Their least-root theorem is nevertheless an exact equivalence rather than a solution method.

The correct status language is:

```text
ordinary extraction has been characterized;
no live positive architecture has been extracted.
```

For the six-branch target, the unresolved statement remains precisely:

```text
is (m_n) bounded, or does m_n tend to infinity?
```

The positive side would yield a `K-####` candidate after branch-qualified replay. The negative side would eliminate the entire fixed six-branch subsystem and would be genuinely weaker than Collatz.

## Editorial finding

In PR #56 `research/global-extraction/claims/T-7801-ordinary-extraction-dichotomy.md`, the displayed definition of the appended digit contains a malformed control character in place of `\frac`:

```text
a_N=(R_(N+1)-R_N)/M_N.
```

The mathematical argument uses the intended quotient correctly, but the source file should be repaired before integration.

## Review conclusion

The global diagnosis in PRs #56 and #57 is mathematically sound:

```text
finite compatibility is finite-place compactness;
ordinary extraction is an Archimedean tightness theorem.
```

The review adds one stronger no-go result, `R-7401`, showing that even a positive-entropy supercritical Collatz forest can be entirely nonordinary.

No current architecture-specific least-root sequence is decided.