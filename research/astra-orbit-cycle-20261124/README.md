# Orbit occupation, cyclic factors, and ordinary mergers

2026-11-24. **Collatz remains OPEN.** This packet gives new necessary conditions on a hypothetical exceptional orbit, exact restrictions on positive cycles, and smaller ordinary merger constructions. The written proofs were independently reconstructed within the agent team. The scope of the Lean results is narrower and is stated below.

Use the shortcut map

\[
T(n)=\begin{cases}n/2&2\mid n,\\(3n+1)/2&2\nmid n.\end{cases}
\]

For the accelerated odd map, write its actual states as \(q_i\), its gaps as \(a_i=v_2(3q_i+1)\), and \(\ell=\log_2 3\). The canonical digits \(b_i\in\{1,2,3\}\) and nonnegative carries \(c_i\) come from the **actual** discounted scalar, with the exact relation \(a_i+c_{i+1}=b_i+3c_i\). A symbolic candidate and an actual ordinary source are kept distinct throughout.

## 1. Necessary conditions on the same infinite orbit

[Carry occupation and critical mechanical separation](occupation/CARRY_OCCUPATION.md) contains four written results.

**Lossless occupation transfer.** Put \(K_n=\sum_{i<n}c_i\), \(d_n=n\ell-\sum_{i<n}b_i\), \(P_n=2^{d_n}\), and let \(F(Y)\) count actual odd states at most \(Y\) on one injective orbit. The complete identity is

\[
\log_2 q_n+2K_n=d_n+c_n-c_0+\log_2(q_0E_n),
\qquad E_n=\prod_{i<n}\left(1+\frac1{3q_i}\right).
\]

At ordinary clocks where \(c_n\le2K_n+c_0\), the physical height is bounded by a fixed multiple of \(P_n\). At every other selected clock the accumulated carry satisfies \(K_{n+1}\ge3K_n+1\). The number of exceptions below a fixed multiplier threshold is therefore only double logarithmic. The resulting bound transfers the physical count, including its logarithmic saving:

\[
\#\{n:P_n\le X\}=O_q\!\left(\frac{X^\theta}{\sqrt{1+\log X}}\right),
\qquad\theta=H_2(\log_3 2)=0.949955527\ldots.
\]

The proof also gives a version uniform over actual suffixes after scaling by their initial ordinary height. It does not assert summability at the endpoint exponent \(\theta\).

**A finite window inequality.** If an injective prefix has length \(N\), and \(m\ge1\) is least with \(3^m>\max_{j<N}q_j\), then

\[
N\le m+(m+1)K_N+p_b(m),
\]

where \(p_b(m)\) counts canonical factors of length \(m\). A clean past word fixes its endpoint modulo \(3^m\); the height bound makes that residue determine the endpoint exactly. Carries mark the remaining windows. Polynomial factor complexity \(p_b(m)=O(m^u)\) consequently forces

\[
\max_{j\le N}P_j\ge 2^{cN^{1/\max(2,u)}}
\]

at every sufficiently large horizon. This part needs only the elementary harmonic correction bound, not the global counting theorem.

**Square-root separation from the critical mechanical language.** For

\[
u_i(\rho)=1+\lfloor(i+1)(\ell-1)+\rho\rfloor-\lfloor i(\ell-1)+\rho\rfloor,
\]

let \(e_N\) be the minimum Levenshtein distance from the first \(N\) actual symbols to any finite mechanical word, allowing any intercept and length. For every positive odd source,

\[
\liminf\frac{e_N^{\rm physical}}{\sqrt N}\ge\sqrt\ell,
\qquad
\liminf\frac{e_N^{\rm canonical}}{\sqrt N}\ge\frac{2\sqrt\ell}{3}.
\]

The same constants hold for the minimum number of independent mechanical fragments or exceptional singletons needed to partition the prefix. Intercepts and decompositions can change with the horizon. Periodic ordinary trajectories are handled separately and have a linear lower bound. The nonperiodic proof uses the finite residue-window inequality.

**An explicit irrational exclusion beyond a superpolynomial test.** Change the first baseline digit 2 at or after each cubic position \(k^3\) into 1. The resulting irrational phase has \(P_n=2^{n^{1/3}+O(1)}\), so its canonical expansion is superpolynomial. Nevertheless its edit distance is only \(O(N^{1/3})\); it cannot be the actual canonical phase or actual physical gap sequence of any positive ordinary source. This excludes every admissible integer translate of the phase. The construction still has quadratic factor complexity.

**Remaining obligation:** no theorem forces every hypothetical nonperiodic ordinary orbit into the excluded approximation or complexity/growth regimes.

## 2. Restrictions on the complete cycle denominator

[Rotational exclusion](cycles/ROTATIONAL_EXCLUSION.md) compares arbitrary rotations of one whole period; it needs no equal-clock block dictionary.

Let a primitive positive rational cycle have bit period \(A\), odd count \(p\), common reduced denominator \(d\), and \(D=2^A-3^p>0\). If two different rotations share a cyclic interval of length \(L\), cut after that interval and call the complementary carries \(C_v,C_{v'}\). With \(m=A-L\) and common complementary odd count \(q\),

\[
\frac{D}{\gcd(D,C_v-C_{v'})}\mid d,
\qquad
D\le d|C_v-C_{v'}|\le d(2^{m-q}-1)(3^q-2^q)<d3^m.
\]

This retains the whole numerical denominator after cancellation. A source-qualified two-power estimate, using Matveev's explicit theorem plus exact finite/Farey certificates, gives the all-period consequence:

> Every primitive nonstandard positive ordinary cycle has distinct cyclic factors of length \(\lceil A/2\rceil-1\) at every starting position. Every nonidentity rotation differs in at least four parity bits.

The small-period range is exhaustive. The large-period logarithmic estimate is a written application of an external theorem; it is not Lean-formalized here. A second elementary result gives a full reduced-denominator divisor for a two-position transposition of equal-clock blocks, without requiring coprime block counts or displacement.

PR193 independently obtains the same asymptotic repeated-factor threshold through a bound retaining factor complexity at each scale. Its high-complexity rational examples explain why neither estimate covers all candidate integer cycles. Our contribution at this interface is the explicit divisor for each rotational pair and the certified all-period exclusion. See the [comparison review](../../reports/astra-review-20261124/ADDENDUM_PR193.md).

**Remaining obligation:** force every hypothetical nonstandard ordinary cycle to violate a denominator or repetition restriction. Arbitrary high-complexity candidates remain outside these exclusions. Cycle exclusion would still leave divergence to address.

## 3. A sharp inverse-clock barrier and an ordinary escape

[Two-anchor mergers](mergers/TWO_ANCHOR_MERGERS.md) proves the following statements for actual positive ordinary sources. Let \(p_t(x)\) count odd inputs in the first \(t\) shortcut steps.

**Unrestricted competitor clock.** If \(n>1\), \(2^H\mid n+1\), \(3^A\mid n-1\), and \(H,A\ge1\), every \(0<x<n\) meeting \(T^h(n)\) at any clock \(t\), for \(0\le h\le H\), satisfies

\[
p_t(x)\ge h+A+1.
\]

If \(H=v_2(n+1)\ge2\), the same excess bound extends to forward clock \(H+1\). The inverse clock is unbounded in this theorem. For a fixed odd excess \(s\) and an all-odd target prefix, every eligible witness lies on the finite diagonal \(h+s\le t\le h+2s-1\), giving a complete search of that layer.

**Unbounded additive overhead at clock zero.** For any fixed \(E\ge1\), put \(M_E=\lfloor2(3/2)^E-1\rfloor\) and let \(D_E\) be the maximum odd count before the first visit to 1 among the positive \(z\le M_E\) that reach 1. If \(A\ge5D_E+4E+3\) and \(3^A\mid n-1\), every smaller predecessor reaching \(n\) needs more than \(A+E\) odd steps. This uses a finite maximum over the convergent subset; it assumes nothing about the other anchors. The bound is not an effective general algorithm for \(D_E\). For \(E=16\), an exact finite replay gives \(M_E=1312\), \(D_E=66\), and the sufficient cutoff \(A=397\).

**Half-size ordinary selector.** Write \(n+1=2^HM\) with \(M\) odd. If \(3^HM\equiv1\pmod4\), then

\[
T^{H+1}\!\left(\frac{n-1}{2}\right)=T^{H+2}(n)=\frac{3^HM-1}{4},
\qquad
p_{H+1}\!\left(\frac{n-1}{2}\right)=p_{H+2}(n)=H.
\]

This covers half of the odd integers in natural density. The guarded histories and their exact odd counts are Lean-checked; positivity and the elementary comparison \(0<(n-1)/2<n\) for odd \(n>1\) are stated in the written application. The adjacent-Mersenne special case is credited to PR146.

A CRT construction supplies arbitrarily large marked inputs with both an expensive predecessor at clock zero and this zero-excess partner exactly at clock \(H+2\). Thus the earlier obstruction is not vacuous. For \(n=5923\), the unique minimum-odd-count clock-zero witness is \(4679\), reaching it in six steps with four odd inputs. The half-size source \(2961\) meets \(5923\) at \(3332\), using three versus four steps and two odd inputs on each arm.

**Remaining obligation:** cover the complementary class \(3^HM\equiv3\pmod4\), or prove every relevant fixed source eventually acquires a smaller partner through another exact construction. The new interval synchronization theorem in PR193 leaves the least member of each fiber unresolved and does not supply this pointwise coverage.

## 4. What Lean actually checked

The fresh strict replay covers **83 theorem declarations including helpers** in eleven files. Every printed transitive axiom set is a subset of `propext`, `Classical.choice`, and `Quot.sound`; no `sorryAx` or additional mathematical axiom occurs.

| Files | Declarations | Formal scope |
| --- | ---: | --- |
| Eight [audited prior kernels](audited_lean/) | 66 | Finite carry, phase, repetition, substitution, residue and packing kernels from PR182 rounds 11/12 and PR187–191. |
| [CarryOccupation.lean](occupation/CarryOccupation.lean) | 6 | Exceptional carry growth and finite marked-window/dictionary counting. The orbit application and asymptotics remain written. |
| [RotationalExclusion.lean](cycles/RotationalExclusion.lean) | 4 | Finite affine composition and whole-denominator divisibility. The uniform analytic estimate and all-period classification remain written. |
| [HalfSource.lean](mergers/HalfSource.lean) | 7 | Guarded trace helpers, exact half-size merger histories, and the full clock-zero valuation barrier. Positive-clock and additive-overhead extensions remain written. |

**A real upstream compiler failure was repaired.** PR182 round 12's original `PhasePacking.lean` fails with the pinned compiler because `mul_le_mul_right₀` is unavailable. The checked copy repairs those proofs without changing their statements. `CarryCocycle.lean` also needed proof-script cleanup for warnings-as-errors. The other six copies retain their original proof bodies with narrower imports and explicit axiom reports. The source diffs, original-file outcomes, final source hashes and actual compiler output are in the [execution report](../../reports/astra-review-20261124/README.md).

The retained historical “not compiled” comments in copied files describe their original checkpoints. The dated exact-hash receipts supersede that status **only for these checked copies**. They do not retroactively certify other source bytes or all the prose in an upstream PR.

## Reproduce and review

Use Lean 4.34.1, compiler commit `5045d0056413266e57c625dcd7c365b10e377c52`, and Mathlib commit `d13f23b723b8a846827a245b89c10fc7d3f11612`. From a shell with this toolchain on `PATH`:

```sh
python -B research/astra-orbit-cycle-20261124/replay_checked.py /absolute/path/to/mathlib
```

The script checks the toolchain commits, each source hash and all 66 prior-kernel axiom lists. For the three new files, from the pinned Mathlib checkout run `lake env lean -j1 -DwarningAsError=true -DautoImplicit=false` followed by each absolute source path. `CarryOccupation.lean` is Std-only and can also be checked with standalone `lean`.

Run `occupation/carry_controls.py`, `cycles/controls.py`, and `mergers/check_two_anchor.py` in normal and optimized Python. Exact commands and paired outputs are in the reports. These bounded controls are supplementary evidence, not proofs of the infinite statements. The complete checkout gate is `python -X utf8 -B tools/validate.py`.

The [frontier review](../../reports/astra-review-20261124/FRONTIER_REVIEW.md) distinguishes the latest source claims and their first unsupported global steps. Internal [proof reconstruction](../../reports/astra-review-20261124/INDEPENDENT_REVIEW.md), the [merger extension review](../../reports/astra-review-20261124/MERGER_ADDENDUM_REVIEW.md), and late PR192/193 comparison notes retain their exact source boundaries. No external referee acceptance is claimed.
