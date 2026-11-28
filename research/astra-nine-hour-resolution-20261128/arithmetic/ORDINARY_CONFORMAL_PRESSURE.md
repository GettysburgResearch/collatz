# Ordinary atoms and two independent branch weights

**PROPOSED written results, with the specified nonlocal inputs.** Use the positive shortcut map \(T(2n)=n,\ T(2n+1)=3n+2\). For positive real weights \(u,v\), let \(m(n)\) be the masses of a finite complex measure supported on the positive ordinary integers. Impose
\[
                 m(2n)=u m(n),\qquad m(2n+1)=v m(3n+2).
                 \tag{1}
\]
The odd equation includes \(n=0\). Finiteness means absolute summability. Every source has exactly one forward image, so the absolute masses also satisfy (1). We use nonnegative masses below.

## An excluded neighborhood of the critical hyperbola

There is an absolute \(c>0\) such that every nonzero solution must satisfy \(0<u<1\) and, writing \(\theta=\log(2u)\),
\[
      \log(4uv/3)\le -c\min(\theta^2,|\theta|),\qquad uv<3/4.
      \tag{2}
\]
This excludes an open region inside the product boundary at every \(u\ne1/2\). Existence on the other side is open in general.

Here is the sole inverse-distribution input. At every sufficiently large odd depth \(r\), every positive odd unit target \(y\) (unit means prime to three), and every integer \(s\) in \(|s-2r|\le\sqrt r\), at least
\[
                  c_0\, 2^s/(3^r\sqrt r)                         \tag{3}
\]
distinct positive odd unit sources \(x\) have the specified \(r\) odd transitions to \(y\) at exact shortcut clock \(s\). Constants and onset are uniform in \(y\). Use the fixed-total inverse-word floor in Weaver 202, input (2), with one extra ternary digit prescribed to make the terminal inverse source a unit. Prescribe its residue \(1\bmod3\), so the inverse intercept has the unique class \(y-3^r2^{-s}\bmod3^{r+1}\), which is a unit. The integral inverse words are positive and physically injective at fixed depth. The factor \(1/3\) for the extra digit is absolute. This uses the written outside result without a local formal rebuild. [Weaver 202](https://rstation.ai/problems/collatz/papers/202/v1) · [Ordinary reconstruction at the pinned PR215 head](https://github.com/GettysburgResearch/collatz/blob/4f33ecc2de6f0ccf605a68c28da5abea0348e47b/research/astra-nine-hour-20261128/machinery/ARITHMETIC_PROGRESSION_FLOOR.md).

A nonzero (1) has positive finite total mass on odd units. From any positive-mass site, follow actual steps through the first odd departure and halve to the next odd state. This yields an odd unit because the numerator of an odd transition is \(1\bmod3\). Positivity is preserved in both directions along every edge. The dyadic lifts of one such site prove \(u<1\).

The mass of any source in (3) is \(u^{s-r}v^r m(y)\). Distinct total clocks at fixed odd depth give disjoint source rows at \(y\). Rows for different targets are disjoint since the odd forward map is deterministic. Sum over the positive odd unit targets \(y\), and compare with the entire odd unit source mass. After division by that mass,
\[
        1\ge {c_0\over\sqrt r}(4uv/3)^r
           \sum_{|s-2r|\le\sqrt r}(2u)^{s-2r}.                    \tag{4}
\]
With either sign of \(\theta\), at least \(c_1\sqrt r\) summands are at least \(\exp(|\theta|\sqrt r/2)\) for all sufficiently large \(r\). Thus for an absolute \(C>1\),
\[
         r\log(4uv/3)+\tfrac12|\theta|\sqrt r\le C.               \tag{5}
\]
For small \(|\theta|>0\), take \(r=\lceil(4C/|\theta|)^2\rceil\), increasing \(C\) once for the onset. This gives a fixed negative multiple of \(\theta^2\) in (2). For \(|\theta|\) bounded below, a fixed sufficiently large \(r\) in (5) gives a negative multiple of \(|\theta|\).

At \(\theta=0\), (4) gives \(\log(4uv/3)\le0\). To exclude equality, pick one positive-mass nonperiodic odd unit target in the component. If the supplied unit is periodic, the legal exponents among \(1,\ldots,6\) include two giving distinct unit preimages: choose \(2^e y\equiv4,7\bmod9\). At most one is on the cycle. No ordinary source visits a nonperiodic target twice under the odd map. Use \(s=2r\) in (3) and sum over all large \(r\). At \(uv=3/4\) the disjoint source masses lower-bound the total by a positive constant times \(\sum_r r^{-1/2}\). This also directly excludes \(uv\ge3/4\) for all weights.

## The positive slope family on the ordinary diagonal

Set \(u=2^{-p}\) and \(v=(3/2)^p\) for \(p>0\). In this family the finite measures in (1) admit an exact classification.

* For \(0<p\le1\) the only finite ordinary solution is zero.
* For every \(p>1\), a nonzero finite ordinary solution exists if and only if some positive orbit escapes. Every solution is a componentwise multiple of the measure below, subject to absolute summability across components.

On an escaping component \(B\) put
\[
 H(n)=n\prod_{x\in O(n),\ x\ {\rm odd}}(1+1/(3x)).
\]
On escape all states are distinct. The elementary uniform orbit-packing bound \(\#(O(n)\cap[1,Y])\ll Y^\eta\), \(\eta<1\), gives \(n\le H(n)\le C_*n\) by partial summation. The weights telescope to \(H(Tn)=H(n)/2\) at even sources and \(H(Tn)=3H(n)/2\) at odd sources. This is Weaver's corrected height. The squared-weight ordinary atomic construction already appears in PR215. [Weaver 207, corrected height](https://rstation.ai/problems/collatz/papers/207/v1) · [PR215, atom construction and nonordinary fixed laws](https://github.com/GettysburgResearch/collatz/blob/4f33ecc2de6f0ccf605a68c28da5abea0348e47b/research/astra-nine-hour-20261128/escape/phase9/ATOMIC_ADELIC_CONFORMAL_LAWS.md).

On any positive cycle the product of affine slopes is strictly below one. The positive additive contribution on an odd departure is necessary to return the starting value to itself. Equation (1) therefore makes the mass vanish throughout every cyclic component. On an escaping component \(m(n)H(n)^p\) is constant along each edge. Conversely an arbitrary multiple of \(\mathbf1_B H^{-p}\) satisfies (1). It is finite for \(p>1\) by the ordinary \(p\)-series. For \(p\le1\), (2) excludes it. A separate proof uses only positive lower density of a fixed-unit predecessor set in every component, taking the full-map target twice a shortcut unit. Since \(H(n)\le C_*n\), partial summation gives divergence for \(p\le1\). This justification can replace the clock floor (3) for the classification. [Mazur, Theorem 1.1](https://www.proofatlas.ai/papers/positive-lower-density-collatz-predecessors/paper-v1.pdf).

Normalize the \(H^{-p}\) masses of a single hypothetical escaping component to total one. As \(p\downarrow1\), the denominator diverges, while every fixed finite set has bounded unnormalized mass. Thus the endpoint exclusion can coexist with finite ordinary probabilities at every \(p>1\) by loss of all mass on fixed finite sets.

## The unresolved comparison

The tilt in (2) comes from shifts of a physical clock within (3). A separate change of \(u,v\) need not preserve summability on an escaping component. In the positive-slope family near \(p=1+\epsilon\), \(\log(4uv/3)=-\epsilon\log(4/3)\) while \(\theta=-\epsilon\log2\). The linear gap lies outside the narrow quadratic exclusion proved here. An exclusion at even one \(p>1\) in this family would remove escape. Additional finite cycles would still require their own argument.
