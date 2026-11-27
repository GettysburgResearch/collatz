# Closing audit: why the combined estimates still do not force convergence

This last audit uses the fixed source and the entire determinant explicitly.
It records two exact obstructions to the attempted escape proof and a
denominator-aware rational control for the cycle proof. These are written
arguments, not further Lean declarations or additional root-replayed programs.

## 1. The rational witness attached to a record moves with its whole past

Let an actual native prefix start at a fixed positive integer `x₀`, end at
`p`, have clock `k`, odd count `j`, and carry `A`. Thus

\[
2^k p=3^j x_0+A.
\]

Suppose its principal multiplier exceeds one, as at a strict coefficient
record, and put `H=3ʲ−2ᵏ>0`. Periodizing the literal word gives its genuine
negative rational fixed point `z=−A/H`. Since `H` is coprime to 6,

\[
\begin{split}
p-z&=\frac{3^j(p-x_0)}{H},\\
z-x_0&=-\frac{2^k(p-x_0)}{H},\\
\operatorname{den}(z)&=\frac{H}{\gcd(H,p-x_0)}.
\end{split}
\]

In particular `v₃(p−z)=j+v₃(p−x₀)` and
`v₂(z−x₀)=k+v₂(p−x₀)`. The same rational point carries the deep ternary
contact at the current record and the deep dyadic contact at the source.
Its reduced denominator is an exact function of that entire prefix.
The formulas follow by subtraction and `gcd(H,2ᵏ)=1`; they do not use
an equidistribution assumption.

The cofactor theorems fix their rational phase set before taking the orbit
limit. They do not bound this sequence of moving denominators. Compactness
can select a fixed limit at each prescribed number of digits, but does not
give a rate proportional to the growing integer height. Nor does it force
the limit to be rational or algebraic. A fixed rational witness with the
required precision would instead give a nonzero integer `dp−a` divisible
by a power of 3 larger than its absolute value. The absent step is precisely
an argument producing that fixed witness, or controlling the moving one.

The thin critical gate set is not itself such an argument. At precision
`b`, its allowable labels still grow exponentially in `b`. The return-tail
bound for one fixed nonperiodic phase is only `O(1+N/b)`. A direct union
bound across all critical labels loses the desired saving. At bounded
precision, the forced `b` digits are negligible relative to `log p` and
are compatible with nearly full outside-prime cofactors.

### An explicit rational target in the actual critical trace

There is an even more literal witness. Start from an odd `x₀` and let
`qᵢ` be a strict global odd coefficient record after `kᵢ` odd steps and
`sᵢ` native clocks. For its actual complete prefix `wᵢ`, put

\[
r_i=F_{w_i}(-1)
    =q_i-\frac{3^{k_i}}{2^{s_i}}(x_0+1).
\]

The reversed prefix is critical at every depth because the endpoint is
a strict global coefficient record. Appending infinitely many backward
gaps equal to one keeps it critical, and that tail codes `−1`. Thus
`rᵢ` lies in the actual ternary trace `R`, not a replacement set.
Its distance to `qᵢ` is at most `3^(−kᵢ)`. On a fixed escape the bounded
distortion gives `qᵢ≪(3/2)^(kᵢ)`, hence precisely the gate-scale bound
`|qᵢ−rᵢ|₃≪qᵢ^(−γ)` with `γ=log 3/log(3/2)`.

Put `b=v₂(x₀+1)`. For `sᵢ>b`, the reduced denominator of `rᵢ` is
exactly `2^(sᵢ−b)`. It is then not dyadically integral. The primitive
integral polynomial `fᵢ(X)=2^(sᵢ−b)(X−rᵢ)` satisfies

\[
f_i(q_i)=3^{k_i}\frac{x_0+1}{2^b}.
\]

Its part outside the single prime 3 is therefore the same fixed integer
at every such record. The fixed-polynomial theorem does not apply
uniformly to this sequence of changing linear polynomials. The exact
identity shows why a uniform extension in the moving target's coefficient
height would be a new and substantial assertion. It does not supply an
escaping ordinary trajectory.

## 2. The most direct two-coordinate Subspace product has a positive floor

Assume a fixed escaping ordinary trajectory and write

\[
L(x)=x\prod_{\text{future odd departures }q}
\left(1+\frac1{3q}\right).
\]

The inherited reciprocal moment makes this product finite. It is the
same homogeneous height used in [EXIT_GATES.md](operator/EXIT_GATES.md).
For an odd-to-odd prefix from `x₀` to `p` with at least one odd step,
put `r=L(x₀)−x₀`. Exact telescoping gives

\[
r3^j-A=2^k(L(p)-p).
\]

The vector `(3ʲ,A)` is primitive: the final odd endpoint is a 3-unit,
so `A` is a 3-unit. Consider the two real forms `(u,ru−v)`, the two
dyadic forms `(u,x₀u+v)`, and the two ternary coordinate forms `(u,v)`.
Their full local product on this vector is exactly

\[
\begin{split}
&(3^j\,2^k(L(p)-p))\,(2^{-k})\,(3^{-j})\\
&\hspace{35mm}=L(p)-p\ \ge\ \frac13.
\end{split}
\]

The last inequality already follows from the correction at the current
odd state. Thus even if the unknown real constant `r` were algebraic,
these natural forms would not produce a negative power of the vector's
height. The remaining forward correction is exactly the positive residual.
This rejects this particular two-coordinate closing argument. It does not
rule out a different choice of arithmetic observables or additional forms.

## 3. Nonlinear prime complexity persists on large-denominator rational cycles

The elementary resultant argument is not exclusive to denominator one.
Let `xᵢ=aᵢ/d` be a genuine positive rational native cycle in reduced form,
with its common odd denominator. Fix an irreducible integral polynomial
`f` of degree `h≥2`, and set `F(X,Y)=Yʰ f(X/Y)`.
For a word with slope data `A=3ᵇ`, `B=2ˡ` and carry `C`, put
`G(X,Y)=F(AX+CY,BY)`. The nonzero integer

\[
R=\operatorname{Res}\bigl(f(X),B^h f((AX+C)/B)\bigr)
\]

has `log|R|=O_f(l)`, by the same proof as
[POLYNOMIAL_COFACTORS.md](renewal/POLYNOMIAL_COFACTORS.md).
Homogenizing the integral Sylvester adjugate, and then doing the same
with reversed polynomials, gives

\[
R X^{2h-1},\ R Y^{2h-1}\ \in (F,G)\subset\mathbb Z[X,Y]
\]

up to irrelevant signs. At the starting numerator/denominator pair,
`G(aᵢ,d)=BʰF(aⱼ,d)`. Since `gcd(aᵢ,d)=1`, the two identities imply

\[
\gcd(F(a_i,d),F(a_j,d))\mid R.
\]

There is no denominator loss, even at primes dividing `2d`. Therefore
the prime-valuation tails and fixed-rank coset counting apply to these
cleared integral polynomial values as well.

The coprime near-critical family of
[CYCLE_INDEX.md, section 3.1](adelic/CYCLE_INDEX.md), with its denominator
tolerance fixed at most `1/2`, has `log d` bounded below by
`(log 2)N/2`, and every real
phase tends to infinity. Hence `log|F(aᵢ,d)|` is bounded below by a
positive multiple of `N`. The weak-tail count, now with threshold
proportional to `N`, leaves at most `O_f,ε(r+r log(2r))` exceptional
phases against one adaptive `r`-prime pool. These same cycles have the
disjoint perturbation arcs proved in
[DYADIC_CYCLE_CONTROLS.md](adelic/DYADIC_CYCLE_CONTROLS.md), increasing
minimum, real separation and the stated growing prime exclusions.

This is a denominator-aware control, not a sequence of integer states
and not the literal integer assertion about `f(xᵢ)`. Its reduced
denominator is deliberately **exponential**, so it does not also pass
the separate subexponential-denominator filter of the coherent family.
Conversely, the two small-denominator coherent fixtures fail the integer
interval test. No single family meeting every proposed filter is claimed.

The use of primitive coordinates is essential. For an ordinary cycle,
writing its phase as `Aᵢ/D` with the unreduced full determinant gives
`Aᵢ=D xᵢ`. When `D>1`, the pair `(Aᵢ,D)` is not primitive. Inserting it into
the two Sylvester identities introduces its large common factor and
does not recover the strong denominator-free gcd bound. Reducing the
pair to `(xᵢ,1)` restores the theorem but removes `D`. This mechanism
cannot reintroduce the full determinant as a free extra prime divisor.

## 4. The unresolved inference

The actual escape estimates still need to use one source to force decay
of weighted mass on the critical gate sieve. Fixed-target cofactor bounds,
abstract trace dimension, and moving-target approximation do not supply
that inference by themselves. The cycle estimates still need the whole
denominator-one equation, with the known cycle retained. This audit finds
no completed argument for either conclusion.
