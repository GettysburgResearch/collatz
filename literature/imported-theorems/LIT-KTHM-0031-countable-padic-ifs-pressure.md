# LIT-KTHM-0031 — Countable separated `2`-adic IFS and the H-ghost exponent

**Type:** self-contained ultrametric theorem, literature-positioned by countable IFS and `p`-adic path-set theory.  
**Sources for context:** Mauldin--Urbański; Abram--Lagarias.  
**Maps to:** `H/L-9502`, `H/L-9503`, and `H/T-9501` in PR #19.

## General H-ghost system

For `r>=0`, define

```text
ell_r = 3r+2,
phi_r(x) = 2^(ell_r) * 3^(-(2r+1)) * (x-1).
```

Let `G` be the set of limits of infinite compositions

```text
phi_(r_0) o phi_(r_1) o ... (0),
```

or equivalently the compact set coded by all infinite H block itineraries.

Then:

1. `G subset 4 Z_2`;
2. `G = union_(r>=0) phi_r(G)`;
3. every point of `phi_r(G)` has exact valuation `ell_r`, so the branch images are pairwise disjoint;
4. if
   ```text
   N(K)=#(G mod 2^K),
   ```
   then
   ```text
   N(1)=1, N(2)=1, N(3)=2,
   N(K)=N(K-2)+N(K-3)  for K>=4;
   ```
5. if `rho` is the positive real root of
   ```text
   rho^3=rho+1,
   ```
   then
   ```text
   N(K)=Theta(rho^K),
   dim_H(G)=log_2(rho)=0.405685231...;
   ```
6. the number of positive ordinary H-survivors at most `X` is
   ```text
   O(X^(log_2 rho)).
   ```

## Proof

Each map has `2`-adic contraction ratio `2^(-ell_r)`, at most `1/4`, so every infinite composition converges. The image is divisible by `4`, proving `G subset 4 Z_2`.

If `x in G`, then `x-1` is odd. Hence

```text
v_2(phi_r(x))=ell_r=3r+2.
```

Distinct branches have distinct valuations, so their images are disjoint.

Fix `K`. If `ell_r>=K`, the whole image `phi_r(G)` is `0 mod 2^K`; all such tail branches contribute one common residue. If `ell_r<K`, multiplication by the odd unit `3^(-(2r+1))` and the translation `x -> x-1` identify the residues of `phi_r(G) mod 2^K` with `G mod 2^(K-ell_r)`. Different `r` remain disjoint by valuation. Thus

```text
N(K)=1+sum_(3r+2<K) N(K-(3r+2)).                 (1)
```

The initial values follow directly. Subtracting `(1)` at `K-3` from `(1)` at `K` gives

```text
N(K)=N(K-2)+N(K-3).
```

Its characteristic equation is `rho^3=rho+1`, so positivity of the recurrence gives `N(K)=Theta(rho^K)`.

For the Hausdorff dimension, put

```text
s=log_2 rho.
```

Then

```text
sum_(r>=0) (2^(-ell_r))^s
 = 2^(-2s)/(1-2^(-3s))
 = 1
```

exactly because `rho^3=rho+1`. At level `n`, the cylinder diameters are products of the branch ratios. For every `t>s`, the sum of their `t`th powers is

```text
[sum_r 2^(-t ell_r)]^n -> 0,
```

so `dim_H(G)<=s`. For the reverse inequality, assign branch probability

```text
p_r=2^(-s ell_r).
```

The probabilities sum to one. A cylinder of diameter `2^(-L)` receives mass `2^(-sL)`. Pairwise ultrametric separation and the stopping-line decomposition give a Frostman bound

```text
mu(B(x,2^(-K))) <= C 2^(-sK).
```

Hence `dim_H(G)>=s`.

Finally, a positive ordinary H-survivor supplies an infinite itinerary and therefore lies in the corresponding ghost residue set, with the additional mod-`3` legality condition. Choose `K` with `2^K>X`. Every class modulo `2^K` contains at most one integer in `[1,X]`, so

```text
#survivors(X) <= N(K) <= C rho^K <= C' X^s.
```

∎

## Native crosswalk

The recursive branch formula is exactly the infinite version of `H/L-9502`:

```text
alpha((r)v)
 = 2^(3r+2) 3^(-(2r+1)) (alpha(v)-1)
```

at compatible finite precision. `H/L-9503` identifies positive integer survivors with stabilized least representatives of these cylinders.

## Consequence for the current H packet

After independent verification of the branch orientation, this theorem strengthens the proposed survivor count

```text
X exp(-c sqrt(log X))
```

to the power bound

```text
O(X^0.405686).
```

The result is still an upper bound on a hypothetical exceptional set. It neither constructs a survivor nor proves that the set is empty.