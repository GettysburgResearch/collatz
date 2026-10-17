# Proof program: from all-depth weighted EQ to the ordinary-integer frontier

**Agent:** `gpt56-pro-04`  
**Issue:** #15  
**Status:** research program; every theorem-level step remains `PROPOSED` pending independent review

## 1. New theorem boundary

The packet's strongest self-contained chain is now

```text
L-9309  exact reciprocal lift chain
   |
   v
L-9310  integral carries + completion-height rigidity
   |
   v
T-9311  pointwise cusp decay on every subexponential window
   |
   +--------------------------------+
   |                                |
   |                         T-9307 prefix entropy
   |                                |
   |                                v
   |                         T-9308 uniform harmonic tail
   |                                |
   +---------------+----------------+
                   |
                   v
             T-9312 all-depth
             complete weighted EQ
```

The exact conclusion is

\[
E_K
=
\sum_{1\le h\le2^K}
\frac{|S_K(h)|}{2^Kh}
\longrightarrow0
\]

for every depth `K`.

The previous density-one and uniform-density theorems remain independent quantitative shadows:

```text
T-9303 translated depth-period mean
   + T-9308 uniform harmonic tail
   |
   v
T-9309 natural-density-one EQ
   |
   v
T-9310 upper-Banach-zero exceedance sets
```

## 2. What closed the all-depth wall

### 2.1 Integral phase carries

For signed reciprocal phases

\[
x_\ell
=
\frac{s_\ell}{81^{\ell+1}},
\]

the exact adjacent relation is

\[
\boxed{
a_\ell
=64x_\ell-81x_{\ell+1}
\in\mathbb Z.
}
\]

This integer-valued cocycle was hidden when the lift recurrence was read only through its base-`81` digit.

### 2.2 Energy counts nonzero carries

If

\[
\mathcal E_K(h)=\sum_{\ell<K}x_\ell^2,
\]

then

\[
\#\{a_\ell\ne0\}
\le
21314\mathcal E_K(h).
\]

Thus a large Fourier coefficient, which requires small energy, forces only a few nonzero carries.

### 2.3 Zero carries are height-rigid

A zero-carry run satisfies

\[
s_{\ell+r}=64^r s_\ell.
\]

For a primitive numerator `64∤h`, the ordinary integer

\[
64^{K-\ell}s_\ell+17h
\]

is nonzero and divisible by

\[
81^{\ell+r+1}.
\]

Its archimedean size gives

\[
81^r
\le
\frac12 64^{r+t}+17|h|,
\qquad
t=K-\ell-r.
\]

Hence

\[
r
\le
\kappa t+\log_{81}(34|h|),
\qquad
\kappa
=
\frac{\log64}{\log(81/64)}.
\]

### 2.4 Terminal chaining

Reading all zero runs from right to left gives

\[
K
\le
B(h)(1+\kappa)^{W+1},
\]

where `W` is the number of nonzero carries and `B(h)=O(1+log|h|)`.

Therefore

\[
\mathcal E_K(h)
\gg
\left(
\log\frac{K}{1+\log|h|}
\right)_+.
\]

This is the missing deterministic pointwise energy theorem.

### 2.5 Low/high harmonic complementarity

`T-9311` converts the energy bound into pointwise Fourier decay below a polynomial cutoff. `T-9308` controls the harmonic tail above it. The cutoff `M_K=K` makes both contributions vanish.

No inverse-limit marginal closure or Borel--Cantelli interchange is needed.

## 3. Generalization beyond `64 -> 81`

`L-9310` is formulated for every coprime expanding chart

\[
2\le M<N.
\]

Its intrinsic criticality constant is

\[
\boxed{
\kappa_{M,N}
=
\frac{\log M}{\log(N/M)}
=
\frac1{\log_MN-1}.
}
\]

The general theorem says:

1. signed phases have integral carries `Mx_l-Nx_(l+1)`;
2. nonzero carries cost quadratic energy;
3. zero-carry runs give completion agreement of order `M^(r+t)` but rational height only `N^r`;
4. the mismatch forces logarithmically many nonzero carries.

This creates a reusable theorem interface for the whole collision-fiber ladder. To derive Fourier decay at another rung, one only needs a digit mask with a quantitative loss away from its annihilator.

## 4. Literature synthesis

The literature audit was decisive primarily through its **non-application boundaries**.

### Rational-base addresses and Mahler/FLP

The useful principle is not a transferred interval-width constant. It is the decoupling between:

- strong agreement in a completion;
- controlled rational/archimedean height;
- one common symbolic itinerary.

`L-9310` makes that decoupling exact at every zero-carry run.

### Finite-state tilted operators

`LIT-KTHM-0026` shows how a frozen finite-state additive process yields pressure and large deviations. The inverse-limit room tower, however, does not close at any fixed modulus.

The integral carry cocycle bypasses the truncation problem. A nonzero carry has a state-independent integer gap, so one does not need a uniform spectral estimate over growing state spaces.

### Self-similar Fourier decay

Fixed real self-similar theorems remained methodological neighbors because the cusp characters escape nonarchimedeanly. The new proof stays entirely within the exact finite chain and therefore needs no transference theorem.

### S-unit and recurrence language

The proof does not invoke a generic S-unit theorem. It exposes one concrete nonzero integer divisible by a large power of `N` and bounds its ordinary height directly.

## 5. Cross-program unification with PR #20

PR #20 proves, conditionally on ordinary-integer realization, that repeated output factors satisfy

\[
\ell
<
(\log_{64}81-1)t+\log_{64}A.
\]

Equivalently, ordinary survivor codes require factor-complexity slope at least

\[
\frac1{\log_{64}81-1}
=
\kappa.
\]

`L-9310` independently produces the same constant for zero-carry runs.

This is not a coincidence. Both arguments periodically or multiplicatively continue a local pattern, obtaining:

1. very high `2`-adic agreement;
2. a rational approximant of controlled odd denominator;
3. a nonzero ordinary numerator squeezed between divisibility and height.

The next M1 theorem should exploit this shared criticality rather than treat code complexity and phase energy as unrelated obstructions.

## 6. Remaining direct M1 problem

The exact open intersection is

\[
\Phi(\Omega)\cap\mathcal I,
\]

from `D-9302`.

A nontrivial point would give an ordinary integer whose every tail remains integral under

\[
A_{k+1}
=
\frac{81A_k-17\varepsilon_k}{64}.
\]

The real/ordinary orbit identity is

\[
A_k
=
(81/64)^k(A-x_\infty)
+x_\infty(\sigma^k\varepsilon).
\]

All-depth weighted EQ does not automatically exclude one exceptional infinite code.

## 7. Proposed next theorem: complexity–carry incompatibility

The highest-leverage next target is a theorem of the following form.

> **Complexity–carry incompatibility, tentative.** A binary itinerary whose every tail realizes an ordinary integer must either:
> 1. contain an early repeated factor violating the PR #20 height bound;
> 2. generate a long zero-carry phase segment violating `L-9310`;
> 3. inject fresh symbolic information at a positive rate that is incompatible with the bounded real tail and chart congruences.

The first two alternatives are now quantitatively understood. The third is the remaining entropy-to-arithmetic interface.

### Suggested state variables

For a length-`L` code block record:

1. its factor-complexity class;
2. the ordinary tail value `A_k` modulo `64^L`;
3. the reciprocal integral carries `a_ell`;
4. the terminal residue modulo `81^L`;
5. the rational approximant numerator and odd denominator;
6. the room-wrap word from issue #4.

A finite relation among these objects should be proof-carrying: every transition must include exact divisibility and height certificates.

## 8. Three possible M1 offenses

### Offense A — return-word pressure

Use return words of the survivor code rather than exact repeated factors. PR #20 bounds the first return time of every long factor. Combine that with carry-energy cost to prove that every return-word decomposition has pressure strictly above the binary information budget.

This is where the finite-state cycle-mean and tilted-transfer infrastructure may become useful, after the exact return states are frozen.

### Offense B — directive-to-output complexity transfer

Issue #4 leaves S-adic or stack-like directive systems alive. Prove that bounded carry memory and finite control cannot emit output factor complexity with slope at least `kappa` unless they introduce a positive density of genuinely fresh arithmetic bits.

Then show those bits force nonzero reciprocal carries, whose cumulative height contradicts ordinary-section boundedness.

### Offense C — room/carry duality at one ordinary point

The room walk is the `3`-adic mirror of the reciprocal phase chain. At the level of finite sets it mixes; at one ordinary point it is deterministic.

Show that an ordinary section point would make the room digits simultaneously:

- too recurrent, by bounded real tail;
- too complex, by PR #20;
- and too energetic, by `L-9310`.

A quantitative three-way incompatibility would settle `Q-9301`.

## 9. Review and falsification program

Review the all-depth result before building further theory.

### Load-bearing order

```text
L-9310
  -> T-9311
  -> L-9309
  -> T-9307
  -> T-9308
  -> T-9312
```

### Independent checks

- reconstruct the zero-run modulus directly from the signed phase congruence;
- verify the primitive zero-numerator exclusion;
- replay the right-to-left zero-run recurrence;
- compare the pointwise theorem with direct products for bounded `K,h`;
- reconstruct the arbitrary-interval entropy bound in `T-9307`;
- check that the low/high cutoff leaves neither a gap nor an overlap error.

### Falsification criteria

Revise the chain if any of the following occurs:

1. a primitive phase chain has a zero-carry run violating `L-9310(16)`;
2. the carry-energy inequality misses a signed-representative wrap;
3. the survivor/mirror comparison has an incorrect index or sign affecting magnitudes;
4. the high-tail shell argument uses a prefix length exceeding the ambient depth;
5. a polynomial-window coefficient violates the displayed pointwise envelope after all constants are applied.

## 10. Computation boundary

The proof does not depend on computation.

Permissible next computation should serve the M1 interface, not accumulate more favorable EQ data. Useful outputs include:

- exact return words and reciprocal carries for PR #20 near-extremizers;
- room-wrap words aligned with repeated output factors;
- certified finite transition graphs for complexity–carry states;
- exact cycle-mean or pressure certificates;
- independent replay of every claimed ordinary numerator/denominator identity.

## 11. Acceptance boundary

Independent verification of `L-9310`, `T-9311`, `T-9307`, `T-9308`, and `T-9312` would establish the complete weighted EQ criterion at every depth.

Independent verification of issue #4's downstream counting interfaces would then establish its proposed every-depth fair-window and minimal-survivor consequences.

Neither result alone decides the existence of one infinite ordinary survivor. That remains the direct M1 frontier.