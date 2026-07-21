# External-theorem applicability audits

## A1. Automatic frequencies versus the two-base Cobham theorem

**Native target:** `CLAUDE/T-0003`.

**Located theorem actually needed.** If a letter frequency exists in a `k`-automatic sequence, it is rational. Cobham established this in the theory of uniform tag sequences; Allouche–Shallit–Yassawi state it explicitly as a nonautomaticity test.

**Local reduction.** Let

```text
beta = log_64(81),
alpha = 1/(beta-1) - 17.
```

Unique factorization makes `beta` irrational. If it were algebraic, Gelfond–Schneider applied to `64^beta=81` would make `81` transcendental, so `beta` is transcendental. The inverse Möbius relation `beta=1+1/(alpha+17)` makes `alpha` transcendental. Therefore any finite-alphabet schedule whose relevant letter frequency exists and equals `alpha` is not `k`-automatic for any integer base `k≥2`.

**Verdict:** **KNOWN — COROLLARY**, after the schedule and its frequency are defined exactly.

**Correction:** This step is not an application of the famous theorem that simultaneous automaticity in two multiplicatively independent bases forces eventual periodicity. Cite the rational-frequency result instead.

**Non-consequence:** Nonautomaticity does not prove that the only remaining class is Sturmian or Ostrowski, nor that an Ostrowski-computable schedule satisfies the regeneration equations.

## A2. Primitive substitutions

A primitive substitution has an integer incidence matrix. Its letter-frequency vector, when normalized from the Perron–Frobenius eigenvector, has algebraic coordinates. A transcendental target frequency therefore rules out a **fixed primitive substitution** with that frequency.

**Verdict for the corresponding sentence in `H64.md`:** **KNOWN — COROLLARY** with the primitive/frequency-existence hypotheses stated.

**Non-consequence:** This does not exclude nonprimitive morphisms in every coding, S-adic directive sequences, fusion rules, or a grammar whose relevant density is not a letter frequency.

## A3. Skolem–Mahler–Lech

**Native target:** `CLAUDE/T-0006`.

Suppose the unsteered coincidence equation is exactly

```text
u_m = c1*(81^18)^m + c2*(81^9)^m + c3.
```

The bases have pairwise quotients `81^9`, `81^18`, and `81^-9`, none roots of unity. If all present coefficients are nonzero, this is a nondegenerate characteristic-zero power sum. Skolem–Mahler–Lech says its zero set is a finite set plus finitely many arithmetic progressions; nondegeneracy forbids an infinite progression, hence the zero set is finite.

**Verdict:** **KNOWN — COROLLARY, native reduction pending audit**.

Required native checks:

1. derive the displayed power sum as an equality in a characteristic-zero field;
2. display `c1,c2,c3` and handle every zero-coefficient case;
3. rule out the identically zero sequence;
4. distinguish equality in `Z_2` from congruence to growing finite depth;
5. state that SML is ineffective here and gives no numerical last coincidence.

The word “S-unit” in `PR3/T-0004` does not itself invoke the classical S-unit equation theorem.

## A4. Fatou–Pólya integral denominators in skeleton rigidity

**Native target:** `CLAUDE/T-0020`, Step 4.

The needed chain is:

1. an integer-valued sequence that is an exponential polynomial has finite Hankel rank;
2. because its Hankel matrix has rational entries, it has a recurrence over `Q` and a rational generating function over `Q`;
3. a rational series in `Z[[z]]` can be written `P(z)/Q(z)` with `P,Q∈Z[z]`, `Q(0)=1`;
4. hence every reciprocal pole, equivalently every characteristic base in a minimal representation, is an algebraic integer.

This is the Fatou–Pólya integer-coefficient power-series principle. The label “Kronecker criterion” is unnecessary and potentially misleading.

**Local dominant-base requirement.** The exp-polynomial representation must first be made minimal by combining equal bases and deleting zero polynomials. With positive real bases, the quotient of consecutive terms tends to the largest surviving base unless the sequence is eventually zero. The skeleton recurrence then identifies that base with `(N/M)^U`, a rational noninteger. That contradicts algebraic integrality.

**Verdict:** the external dependency is **KNOWN — COROLLARY** and a complete replacement proof is supplied in `LIT-KTHM-0007`; this audit does not independently verify every earlier step of `T-0020`.

## A5. Mahler and FLP

**Native target:** `CLAUDE/Q-0002`, `MINIMAL.md` M2.

Mahler's Z-numbers satisfy a real condition on all fractional parts of `ξ(3/2)^n`. FLP generalize this to `ξ(p/q)^n` and prove that, for every `ξ>0`, the difference between limiting supremum and limiting infimum of the fractional parts is at least `1/p`.

The repository's object is a 2-adic attractor defined by digit admissibility for an affine `81/64` system. It is a useful **analogue**, but no located theorem identifies it with the classical Z-number problem. FLP's lower bound is about Euclidean interval length, not Haar measure in `Z_2`. The comparison `1/32 > 1/81` therefore does not show that an FLP theorem fails by a threshold; it only notes that a naive numerical analogy points the wrong way.

**Verdict:** classical statements **KNOWN — EXACT**; native equivalence claim **MISAPPLIED if read literally**, acceptable after wording as “2-adic analogue.”

## A6. Fourier decay

**Native targets:** `CLAUDE/T-0011`, `CLAUDE/T-0012`, `CLAUDE/Q-0003`, and the claim in `MINIMAL.md` that modern results apply to “exactly this shape.”

Li–Sahlsten consider a fixed finite family of contractions on `R` and a fixed self-similar measure. Solomyak considers parameter families of fixed real self-similar measures and proves generic power decay. In contrast, the repository's normalized counting measure changes with `K`, lives naturally on `Z/64^K Z`, includes modular inverses of powers of `81`, and is tested on a `K`-dependent archimedean frequency window.

No direct identification with the hypotheses of either theorem was located.

**Verdict:** **PARTIAL OVERLAP / HYPOTHESES NOT YET ESTABLISHED**. Replace “apply to exactly this shape” by “provide nearby stationary real models and techniques.”

Potential bridge theorem to seek: a uniform renewal/Fourier estimate for a triangular array of affine products whose contraction data and modulus vary with depth, with constants uniform in the required frequency range.

## A7. Measure rigidity

Rudolph's theorem concerns jointly `×p`/`×q` invariant ergodic measures with positive entropy. Shmerkin and Wu prove dimension/intersection results for real invariant sets and measures. `V∞∩Z` asks whether one countable archimedean subset meets one coded 2-adic set.

**Verdict for `CLAUDE/Q-0005`:** meaningful research analogy, **no direct theorem application located**. Before invoking measure rigidity, the repository would need to construct a relevant invariant measure or real invariant set and prove that an integer witness induces an object satisfying the source hypotheses.

## A8. Backward trees versus forward collision fibers

Applegate–Lagarias and Krasikov–Lagarias count inverse images that eventually reach a target or congruence class. A collision fiber in PR #3 is a set of distinct forward parity cylinders whose affine outputs agree after one fixed depth and weight.

**Verdict for `PR3/T-0005`:** classical parity coordinates are **KNOWN — EXACT**; backward-tree results give **PARTIAL OVERLAP** only. No exact source for the signature-pigeonhole/odd-tail amplification theorem was located.

## A9. Generalized undecidability and rewriting

Yolcu–Aaronson–Heule provide a direct standard-Collatz rewrite equivalence. Kurtz–Simon, building on Conway, prove `Π^0_2`-completeness for a generalized family.

**Verdict:** both sources are genuine, but they support different statements. Generalized undecidability must never be summarized as undecidability of the ordinary `3x+1` conjecture.
