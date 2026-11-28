# Exact first-stop records under an ordinary counted merger

[StoppedRecord.lean](StoppedRecord.lean) proves the finite native arithmetic used in the [stopped-clock symmetry](../cycles/STOPPED_CLOCK_SYMMETRY.md) and [unrestricted almost-prime sampling](../cycles/ALL_SEMIPRIME_COMPONENTS.md) arguments. It imports the existing ordinary shortcut map, its actual finite iterates and its actual odd-input count. It does not import a synchronization frequency estimate, a density theorem, a sieve theorem or a limiting law.

Let $T(n)=n/2$ for even $n$ and $T(n)=(3n+1)/2$ for odd $n$. Write $k_s(n)$ for the number of odd inputs before shortcut date $s$. A counted merger at date $t$ means both
$$
 T^t x=T^t y,\qquad k_t(x)=k_t(y).
$$
These equalities persist at every later common date. For a stopping set $A\subseteq\{0,\ldots,B\}$, the formal predicate `FirstAt A x s` says that the actual state at date $s$ is in $A$ and that all earlier states are outside $A$.

The elementary native bound $n\le2^jT^j n$ proves height clearance. If
$$
                2^{t+\ell}B<\min(x,y),
$$
then neither source enters $A$ through date $t+\ell$. Under a counted merger by date $t$, `full_first_record` proves that an actual first hit from $x$ at any date $s$ is also the first hit from $y$ at that same date; their odd counts, landing states and the final $\ell$ actual parity bits all agree. The proof obtains $t+\ell<s$ from the source-height hypothesis and uses the common future beginning at date $s-\ell$. The separate `first_at_iff` and `never_hits_iff` cover both directions and misses. No existence of a stop is assumed implicitly.

The native real mark is
$$
 b_s(n)=\frac{3^{k_s(n)}n}{2^sT^s n}.
$$
For every positive source it is exactly the finite product of $3z/(3z+1)$ over its odd inputs $z$ before date $s$; even edges contribute one. `product_mark_calibration` and `native_mark_eq_product` prove this identity, and `native_mark_bounds` proves $0<b_s(n)\le1$. This is the unshifted mark appearing in the stopping manuscripts, distinct from the earlier shifted-cofactor survival product.

For sources $x$ and $x+d$ that counted-merge by $t\le s$, the module proves
$$
 b_s(x+d)x=b_s(x)(x+d),\qquad
 0\le b_s(x+d)-b_s(x)\le\frac d{x+d}.
$$
Thus the exact real mark varies continuously under nearby-source comparisons in the stated quantitative sense. The real coordinate is controlled by bounded-Lipschitz tests in the written transfer theorems. The finite estimate does not assert total variation on its exact atoms, which can retain the source itself.

Strict standalone compilation passed with the pinned Lean and Mathlib, warnings as errors, no implicit variables and no proof holes. The checkpoint replay audits all public, private and generated declarations transitively. The analytic rate at which native counted mergers occur remains an explicitly cited external input.
