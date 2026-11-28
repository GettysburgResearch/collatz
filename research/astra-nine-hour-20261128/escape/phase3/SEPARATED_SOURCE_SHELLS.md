# Two fixed source intervals recover the total escape mass

For real \(X\to\infty\) choose the uniform positive integer source separately on
\[
            I_X=[X,21X/20],\qquad J_X=[5X,21X/4]=5I_X.
\]
Write \(\mu_{I,t},\mu_{J,t}\) for the resulting entire laws of the genuine shortcut endpoint \(T^t n\), with the **same** integer clock. If \((t-\mu\log X)/b_X\to+\infty\) then, on the cited ordinary-source inputs,
\[
           \lim_{X\to\infty}\|\mu_{I,t}-\mu_{J,t}\|_{\rm TV}
                         = d_{\rm esc}.                                \tag{1}
\]
Here \(d_{\rm esc}\) is the total ordinary density of escaping sources and total variation uses the probability convention. The two explicit source intervals have fixed positive proportional widths. No unknown component or phase profile appears in the finite test. This result does not need the marked local limit, atomlessness, or the compact-null support of full correction products.

## A finite separation

For two positive starts \(x,y\), suppose \(T^t x=T^t y\). Write \(a,b\) for the respective numbers of odd departures and \(u,v\ge1\) for their true correction products, i.e. the products of \(1+1/(3z)\) at odd departures. The exact common-endpoint equation is
\[
                             3^a x u=3^b y v.
\]
For any positive rational \(c\) with \(3cx\le y\) and \(cy\le9x\), one has \(u\ge c\) or \(v\ge c\). If \(a\le b+1\), the left side with \(u<c\) is strictly below \(3^b y\). If \(a\ge b+2\), the right side with \(v<c\) is strictly below \(3^a x\). These prove the two alternatives. All clocks, including zero, are covered. For \(4x\le y\le6x\) this gives \(\max(u,v)\ge4/3\). At exactly \(y=5x\) it gives the stronger \(5/3\) floor.

Every state on any escaping trajectory exceeds the published verified floor \(2^{68}\). Each finite prefix is simple. Weaver's rational bound (23) on **any** finite simple segment above that floor gives \(\log u\le0.21645\), hence \(u<4/3\), on such a trajectory. For example \(\log(4/3)\ge1/4>0.21645\) by integrating \(1/x\) on \([1,4/3]\). All pairs \(x\in I_X,y\in J_X\) satisfy \(4x\le y\le6x\). Therefore the sets of physical endpoints from escaping inputs in the two intervals are disjoint at every common date, even before an asymptotic limit. If a pair meets, its common tail is bounded. This argument uses the externally supplied finite certificate above the verified floor. [Weaver 175 v1, §11, equations (20)–(23), including Bařina verification attribution](https://rstation.ai/problems/collatz/papers/175/v1)

The Lean kernel proves the rational cone theorem on literal shortcut trajectories, including the fivefold \(5/3\) specialization. Its geometric hypotheses and actual meeting time are explicit, with no imported certificate about \(2^{68}\). Independent rational controls check 74,496 affine product identities and 439,378 actual equal-clock dates among 1,614,080 candidate pair dates, including 3,154 fivefold meetings. The same control checks the profile periodization integral symbolically on 716 pieces for 360 rational marks. The ordinary asymptotic assertions above remain written deductions. [Finite Lean theorem](NonresonantMerge.lean) · [Exact finite controls](check_nonresonant_merge.py)

## The part of the population on bounded components

Every fixed proportional source interval has the same limiting ordinary component masses as the prefix source, by differencing its two endpoints and dividing by the interval length. The same operation applies to convergence in total variation of the restriction to periodic endpoints. Indeed each fixed multiple \(cX\) has the same supercritical normalization, since \(\log(cX)-\log X\) is constant. PR213's periodic-phase law therefore gives the identical limit on \(I_X\) and \(J_X\), namely \(\sum_{C\ {\rm bounded}}d_C\operatorname{Unif}(\Gamma_C)\) on the actual cycles. Countable component coverage yields total bounded input mass tending to \(\sum_{C\ {\rm bounded}}d_C\) on each interval. Thus the bounded-source endpoint measure converges in total variation to that same limit: the bounded transients carry mass tending to zero. [PR213, native endpoint atom and periodic-phase result](https://github.com/GettysburgResearch/collatz/blob/a743bd04d33945b15a1ec91deaca4a82c0261a07/research/astra-global-rigidity-20261128/mass/NATIVE_ENDPOINT_ATOMS.md) · [Full population coverage](https://github.com/GettysburgResearch/collatz/blob/a743bd04d33945b15a1ec91deaca4a82c0261a07/research/astra-global-rigidity-20261128/mass/FINITE_COMPONENT_PARTITION.md)

The escaping-source measures in the two windows each have mass tending to \(d_{\rm esc}\). Their supports are disjoint from all bounded components and disjoint from each other by the finite separation. Half their summed masses is their contribution to total variation. The bounded contribution tends to zero. This proves (1).

More generally, fixed positive proportional intervals all of whose cross-ratios lie inside \([3c,9/c]\) have this same conclusion if \(\log c>0.21645\). The exact finite affine kernel also treats a specified lag by comparing the true homogeneous factors of the two different clocks. A fixed nonresonant dilation cannot be produced by a parity-cylinder identity at equal clock: comparison of the cylinder lift slopes forces a ratio which is a power of three. Existence of arbitrary bounded prefixes, translated initial-trit mixing, and positive ordinary predecessor density do not provide convergence to zero in (1). [Primary finite affine meeting criterion, Proposition 1](https://rstation.ai/problems/collatz/papers/204/v1)
