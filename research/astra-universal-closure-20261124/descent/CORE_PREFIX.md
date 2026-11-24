# A smaller base after a short singleton, at every ternary exponent

**PROPOSED positive descent.** Suppose \(T^h(3^r v)=1\) for a
positive ordinary base \(v\). For every \(t>0\), let
\[
               w=v+4\cdot2^h t,\qquad w'=v+3\cdot2^h t.
\]
Then \(0<w'<w\) and
\[
                     T^{h+2}(3^r w)=T^h(3^r w').
\]
The exponent \(r\) stays fixed, even when it is arbitrarily large.
In the notation of the [minimum-core theorem](../global/SmoothCore.lean),
this is a physical certificate of the kind required by FrontierMerger
for each such input. It needs no assumption on the convergence of either
lifted orbit.

To prove it, let \(p\) count the odd inputs in the specified \(h\)
clocks from \(3^r v\), and set \(D=3^{p+r}t\). The high-bit affine
formula gives \(T^h(3^r w)=1+4D\) and
\(T^h(3^r w')=1+3D\). Two more ordinary steps from \(1+4D\) give
\(1+3D\). Consequently an actual first bad tower at \((w,r)\) forces
every positive lower binary prefix \(v=w\bmod 2^s<w\) to have first
hitting time \(H(3^r v)>s-2\) for \(s\ge2\): the lower tower makes
the reference good, and any earlier hit would give this contradiction.
The two-step lift is the same elementary mechanism used on two arms in
[PR192](../../astra-minimum-source-20261124/descent/README.md).
Here the comparison stays at the same ternary exponent in the new rank.

**Examples for every exponent on the remaining short-run branch.**
Fix \(r\ge2\). Choose a sufficiently large even \(k\) for which
\[
       2^{k+2}\equiv7+3^{r+2}\pmod {3^{r+3}} .
\]
Such \(k\) exist because \(4\) generates the subgroup
\(1\bmod3\) modulo \(3^{r+3}\). Indeed \(4-1=3\), and cubing
a number equal to 1 modulo 3 raises the 3-adic valuation of its
difference from 1 by exactly one. Thus the order of 4 is
\(3^{r+2}\), the full subgroup size. Add multiples of this order to
\((k+2)/2\) to make \(k\) arbitrarily large.

Put \(n_0=(2^{k+2}-7)/9=3^r v\). The congruence makes \(v\) an
odd positive unit at 3. The first two clocks from \(n_0\) give the
odd value \((3n_0+1)/4=(2^k-1)/3\); its next clock reaches
\(2^{k-1}\). Hence \(T^{k+2}n_0=1\). For every \(t>0\) apply the
merger above using \(h=k+2\) and the parameter \(3t\):
\[
 w=v+12\cdot2^{k+2}t,\qquad w'=v+9\cdot2^{k+2}t .
\]
Here \(w\) is still a unit at 2 and 3. Every \(n=3^r w\) is
\(113\bmod512\), since \(9\cdot113\equiv-7\pmod{512}\).
Thus \(n\equiv1\pmod8\), and its first maximal odd run has length
one and a singleton exit. The four small-base high-exit classes cannot
settle this input because \(2^1\le3^r\) and the associated odd part
\((n+1)/2\) exceeds \(w\). The class \(85\bmod512\) does not
apply. Both witness clocks above use the original \(n\) and its one
specified smaller tower.

[Lean proofs of the merger and the minimum contradiction](CorePrefix.lean).
The progression construction is a written proof. [Integer replay](check_prefix.py).
The open case includes towers whose lower positive reference prefixes all
take too long to reach 1 for this argument.
