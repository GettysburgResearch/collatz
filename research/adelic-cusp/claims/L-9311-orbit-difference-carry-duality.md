# L-9311 — Orbit-difference carry duality

**Claim ID:** L-9311  
**Title:** Repeated itinerary factors are exactly zero-carry chains in the difference of two ordinary tail orbits  
**Status:** PROPOSED  
**Authoring agent:** `gpt56-pro-04`  
**Reviewing agents:** none  
**Created:** 2026-07-21  
**Last updated:** 2026-07-21  
**Dependencies:** `D-9302`; elementary integer divisibility  
**Scope:** ordinary `64 -> 81` survivor itineraries and the cross-program interface with PR #20  
**Related counterexample candidates:** none

## 1. Setup

Let

\[
A=\Phi(\varepsilon)\ge2
\]

be an ordinary integer in the survivor attractor, and put

\[
A_k=\Phi(\sigma^k\varepsilon)\in\mathbb Z_{>0}.
\]

By `D-9302`,

\[
\boxed{
64A_{k+1}=81A_k-17\varepsilon_k.
}
\tag{1}
\]

Every tail state is at least `2`, and for `s>=1`,

\[
\boxed{
\left(\frac{81}{64}\right)^s(A_k-1)+1
\le A_{k+s}
\le
\left(\frac{81}{64}\right)^sA_k.
}
\tag{2}
\]

The lower bound makes the orbit strictly increasing.

## 2. Exact difference chain

Suppose equal binary factors of length `ell>=1` begin at positions

\[
0\le r<t,
\qquad
\varepsilon_{r+i}=\varepsilon_{t+i}
\quad(0\le i<\ell).
\tag{3}
\]

Put

\[
s=t-r,
\qquad
D_i=A_{r+i}-A_{t+i}
\quad(0\le i\le\ell).
\tag{4}
\]

Subtracting `(1)` at the two starts gives, for every `0<=i<ell`,

\[
\boxed{
64D_{i+1}=81D_i.
}
\tag{5}
\]

Since the `D_i` are ordinary integers and `gcd(64,81)=1`, equation `(5)` forces

\[
64\mid D_i
\]

at every step before the end of the common factor. Iterating gives one nonzero integer `u` such that

\[
\boxed{
D_i=64^{\ell-i}81^i u
\qquad(0\le i\le\ell).
}
\tag{6}
\]

The integer `u` is nonzero because `(2)` implies

\[
A_t>A_r.
\]

Thus an exact repeated factor is not merely a symbolic coincidence: it is an exact length-`ell` **zero-carry chain** for the integral orbit-difference cocycle

\[
\boxed{
b_i=64D_{i+1}-81D_i.}
\tag{7}
\]

All `ell` carries `b_i` vanish.

If the next digits differ, then

\[
\varepsilon_{r+\ell}\ne\varepsilon_{t+\ell},
\]

and the first nonzero difference carry is exactly

\[
64D_{\ell+1}-81D_\ell
=-17(\varepsilon_{r+\ell}-\varepsilon_{t+\ell})
\in\{\pm17\}.
\tag{8}
\]

## 3. Local repetition-height bound

Equation `(6)` gives

\[
64^\ell\le |D_0|=A_t-A_r.
\tag{9}
\]

Apply the upper bound in `(2)` from the tail state `A_r` across `s=t-r` steps:

\[
A_t\le
\left(\frac{81}{64}\right)^sA_r.
\]

Because `A_r>0`,

\[
A_t-A_r<A_t.
\]

Consequently

\[
\boxed{
64^\ell
<
\left(\frac{81}{64}\right)^sA_r.
}
\tag{10}
\]

Writing

\[
\delta=\log_{64}81-1,
\]

we obtain

\[
\boxed{
\ell
<
\delta(t-r)+\log_{64}A_r.
}
\tag{11}
\]

This is the local copied-factor bound proposed independently as PR #20's `T-9403`. The proof here does not use an eventually periodic approximant: it follows directly from ordinary tail integrality and the exact zero-carry difference chain.

## 4. Criticality duality

The reciprocal-character theorem `L-9310` studies a different integral cocycle,

\[
a_i=64x_i-81x_{i+1}\in\mathbb Z,
\]

and bounds long runs with `a_i=0` by the completion-height constant

\[
\kappa
=
\frac{\log64}{\log(81/64)}
=
\frac1{\log_{64}81-1}.
\tag{12}
\]

Equations `(5)`--`(11)` show why PR #20 obtains the same constant. The repetition theorem and the reciprocal-phase carry theorem are two applications of one algebraic mechanism:

1. an integral sequence obeys the exact zero-carry relation `64z_(i+1)=81z_i` over a long interval;
2. completion divisibility grows like `64^ell` or `81^ell`;
3. the ordinary height grows only by the competing ratio `81/64`;
4. a nonzero ordinary numerator prevents indefinite equality.

The constants therefore agree by necessity, not by coincidence.

## 5. Dependency audit

- `D-9302` supplies ordinary integrality of every tail, recurrence `(1)`, and growth bound `(2)`.
- All difference-chain statements are obtained by subtraction and coprime divisibility.
- No PR #20 theorem is imported as a dependency; equation `(11)` is independently reconstructed.
- No Fourier theorem, computation, automaticity theorem, or generic Diophantine theorem is used.

## 6. Gap audit

- The lemma does **not** exclude an ordinary survivor. It identifies the exact coupling that any proposed complexity--carry contradiction must use.
- High factor complexity and many nonzero reciprocal carries are not contradictory by themselves. Both are compatible with avoiding long zero-carry chains.
- The orbit-difference cocycle and the reciprocal-character cocycle live on different variables. A final ordinary-section theorem needs an invariant coupling them through the same fixed room or nested cylinder.
- Equation `(11)` is strict because `A_t-A_r<A_t`, not because of a denominator estimate.

## 7. Adversarial tests

1. Overlapping repeated factors are allowed; subtraction of the two tail recurrences remains valid.
2. If the common factor continued forever, `(5)` would force an eventually periodic ordinary survivor. Strict orbit growth excludes equality of the two tail states for `A>=2`.
3. The all-one code is excluded by the hypothesis `A>=2`; it gives the trivial fixed state `1`.
4. A repeated factor late in the orbit is charged against the local height `A_r`, not only the initial height.

## 8. Consequence for the proof program

The hoped-for contradiction

> “factor complexity is at least `kappa`, while zero-carry criticality is at most `kappa`”

cannot be obtained by comparing the two numerical constants. The repeated-factor bound is itself a zero-carry completion-height theorem. The missing ingredient must control a genuinely new quantity: fixed-room coherence, least-representative stabilization, or an active-cylinder block tail.
