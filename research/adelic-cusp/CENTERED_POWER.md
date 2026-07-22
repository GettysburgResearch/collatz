# Centered rational powers and the ordinary section

**Agent:** `gpt56-pro-04`  
**Issue:** #15  
**Status:** theorem-level claims `PROPOSED`; finite replay `EMPIRICAL`; no counterexample claimed

## 1. Executive reformulation

The ordinary-section problem for the binary `64 -> 81` subsystem is exactly the critical centered rational-power problem

\[
\boxed{
\mathcal Z^{\rm ctr}_{64,81}
=
\left\{
\xi>0:
\left\|
\xi\left(\frac{81}{64}\right)^n
\right\|
\le\frac1{81}
\quad\forall n\ge0
\right\}.
}
\]

`T-9315` proves

\[
\boxed{
\Phi(\{0,1\}^{\mathbb N})
\cap\mathbb Z_{\ge2}
\ne\varnothing
\iff
\mathcal Z^{\rm ctr}_{64,81}
\ne\varnothing.
}
\]

This is an exact bijection, not merely a necessary condition and not merely a structural analogy to Mahler's problem.

Given a centered parameter, the complete ordinary orbit is reconstructed by

\[
\boxed{
A_n
=
\left\lceil
64\xi\left(\frac{81}{64}\right)^n
\right\rceil.
}
\]

Its chart digit is

\[
\boxed{\varepsilon_n=A_n\bmod64\in\{0,1\},}
\]

and the bounded real companion is

\[
\boxed{
x_n=A_n-64\xi(81/64)^n\in(0,1).}
\]

Conversely, every nontrivial ordinary survivor produces exactly one positive centered parameter

\[
\boxed{\xi=(A_0-x_0)/64.}
\]

Thus symbolic digits, integral tails, the bounded real coordinate, and the affine carry law are reconstructions of one nearest-integer orbit.

## 2. The nearest-integer cocycle

Write

\[
\xi(81/64)^n=B_n+u_n,
\qquad
B_n\in\mathbb Z,
\qquad
|u_n|<1/81.
\]

The digit is the sign of the centered error:

\[
\varepsilon_n=\mathbf1_{u_n>0}.
\]

The adjacent errors satisfy

\[
\boxed{
81u_n-64u_{n+1}
=64B_{n+1}-81B_n
=\varepsilon_n-\varepsilon_{n+1}.
}
\]

The carry belongs to `{-1,0,1}` and records whether the itinerary keeps or changes sign.

This is the direct real counterpart of the integral phase carries in `L-9310` and the orbit-difference carries in `L-9311`.

## 3. Real error versus ordinary nearest integer

The centered theorem has two logically different coordinates.

### Real error coordinate

For every binary itinerary, the bounded real companion gives a unique error path

\[
u_n=(\varepsilon_n-x_n)/64
\]

satisfying the critical bound and carry recurrence. `L-9313` proves that the backward error maps are contractions, so the real error system has full symbolic support.

Therefore the real scheduled cylinders do not become empty merely because an itinerary is long or complicated.

### Nearest-integer cylinder coordinate

The integers must satisfy

\[
64B_{n+1}=81B_n+\varepsilon_n-\varepsilon_{n+1}.
\]

A finite itinerary fixes one class

\[
B_0\pmod{64^K};
\]

an infinite itinerary fixes one point of `Z_2`. It gives a positive centered parameter only if that point is an ordinary positive integer.

`R-9303` records the correction:

> pure real interval emptiness cannot close the ordinary section; the exact obstruction is nearest-integer cylinder stabilization.

## 4. Completion series and stabilization

For every itinerary, the selected nearest-integer completion point is

\[
\boxed{
B_0^*(\varepsilon)
=-\sum_{n\ge0}
(\varepsilon_n-\varepsilon_{n+1})
\frac{64^n}{81^{n+1}}
}
\]

in `Z_2`. Equivalently,

\[
\boxed{
B_0^*(\varepsilon)
=-\frac{\varepsilon_0}{81}
+
\frac{17}{81^2}
\sum_{n\ge0}
\varepsilon_{n+1}(64/81)^n.
}
\]

If

\[
0\le R_K<64^K
\]

is the least representative of the length-`K` cylinder, then

\[
R_{K+1}=R_K+q_K64^K,
\qquad
q_K\in\{0,\ldots,63\}.
\]

The selected point is an ordinary nonnegative integer exactly when

\[
\boxed{q_K=0\text{ eventually}.}
\]

This is the same finite-versus-adic boundary found in PR #20's active cylinders and the H-frontier ghost/carry system.

## 5. Fourth-power structure

The multiplier is

\[
\frac{81}{64}=\left(\frac32\right)^4.
\]

`L-9312` expands the centered condition into a schedule for

\[
Y_m=\xi(3/2)^m.
\]

At phases `m=4n+r`, the allowed neighborhoods are

\[
\begin{array}{c|c|c}
r&\text{centers modulo }1&\text{radius}\\
\hline
0&0&1/81\\
1&0,\ 1/2&1/54\\
2&0,\ 1/4,\ 3/4&1/36\\
3&0,\ 3/8,\ 5/8&1/24.
\end{array}
\]

The center choice is synchronized with

\[
B_n\pmod{64}\in\{0,15,49\},
\]

where

\[
\begin{array}{c|c}
B_n\pmod{64}&(\varepsilon_n,\varepsilon_{n+1})\\
\hline
0&(0,0)\text{ or }(1,1)\\
15&(1,0)\\
49&(0,1).
\end{array}
\]

The schedule is a useful real normalization of the arithmetic cylinder, but it is not a standalone pruning mechanism.

## 6. Relationship to the finite minimum program

`T-9313` and `T-9314` study

\[
M_j=\min(R_j\setminus\{0,1\}).
\]

A depth-`j` survivor prefix corresponds to a finite centered trace with starting room

\[
A_0=\lceil64\xi\rceil.
\]

The exact depth-46 certificate is therefore a lower bound on the first ceiling value of every length-46 centered trace whose nearest-integer cylinder is integral through that depth.

The infinite ordinary-section problem remains equivalent to either of the following:

\[
\boxed{M_j\longrightarrow\infty,}
\]

or

\[
\boxed{
q_K\ne0\text{ infinitely often for every nontrivial itinerary.}
}
\]

## 7. Literature boundary

The repository's Mahler/FLP audit remains important but changes role.

After `T-9315`, the project has an exact centered rational-power problem. It is still not the classical one-sided problem:

- the phase-zero target is centered around the circle origin;
- the full `3/2` orbit follows a four-phase schedule;
- the real error language has full symbolic support;
- ordinary realization requires stabilization of an unbounded `2`-adic nearest-integer cylinder.

No theorem presently imported as `LIT-KTHM-####` is claimed to exclude this combined object. A theorem about one interval, generic parameters, or real graph-directed sets cannot replace the arithmetic stabilization argument.

## 8. Exact finite replay

`X-9304` checks the theorem interfaces with exact fractions and integers.

Frozen scope:

- all binary words through depth `8`;
- `494` nontrivial finite survivor words;
- `3,514` centered trace reconstructions;
- `3,020` carry and scheduled-phase checks;
- no floating-point arithmetic;
- no random sampling.

Replay:

```bash
python3 -B -m py_compile experiments/X-9304-centered-power-replay/run.py
python3 -B experiments/X-9304-centered-power-replay/run.py \
  --check-results \
  experiments/X-9304-centered-power-replay/results/canonical.json
```

Frozen SHA-256:

```text
e287cbf70c55adbbdfe3ae4296fc8836f424b2ca48ddda03830235b46f952a2f
```

The replay is an interface audit, not a proof dependency.

## 9. Reframed proof program

### Route A — block-digit nonstabilization

Derive an exact recurrence for

\[
q_K=(R_{K+1}-R_K)/64^K.
\]

Use the real errors, sign changes, or residue states to prove infinitely many `q_K` are nonzero.

### Route B — shifted-value determinant

The same itinerary defines a bounded real error and a `2`-adic completion series. Construct a determinant involving several shifted tails whose real size is small and whose `2`-adic order is large when many cylinder blocks vanish.

PR #20's direct-truncation barrier warns that ordinary partial sums are unlikely to suffice. Exact reduction of the determinant height is load-bearing.

### Route C — stabilization implies structure

Assume the cylinder blocks are eventually zero. Then the nearest-integer start is ordinary. Use the recurrence to prove that the later itinerary has a finite arithmetic description—periodicity, repeated return words, or another structure contradicting `L-9311` or a known rigidity theorem.

### Route D — extendible minimum

Refine `M_j` to the least finite survivor that admits arbitrarily long extensions. Prove its divergence using the centered cylinder state rather than unconditional finite minima alone.

The frozen target is `Q-9303`.

## 10. Status boundary

- `T-9315`, `L-9312`, and `L-9313` are `PROPOSED`.
- `R-9303` corrects the pure real-cylinder proof route.
- `X-9304` is a bounded exact-interface audit.
- No centered parameter is constructed.
- No nonexistence theorem for the centered set is proved.
- No universal lower bound for every Collatz counterexample is claimed.
- The exact issue-#4 chart translation remains separate.
