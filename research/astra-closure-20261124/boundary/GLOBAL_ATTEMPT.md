# Two attempts on the remaining ordinary obstruction

**OPEN.** Neither argument gives vanishing of the PR192 moment or summable convergence-color mismatch on PR201's surviving profiles. Both concern the same positive ordinary starting integer throughout. No new asymptotic theorem is claimed here.

## Reversing a permanent departure

Fix an integer ceiling $M$. If $q\le M$ and $T^t(q)>M$ for every $t\ge1$, then, for every positive original source $n$, its permanent departure from this ceiling has label $q$ **if and only if** it visits $q$. Indeed the visit is itself the final exit, and any exit with that departure label contains the visit. This is an exact equality of source sets before taking any limit. A bounded orbit can have a permanent departure from a *particular* low ceiling if its eventual cycle lies entirely above that ceiling.

For a hypothetical escaping positive orbit, a permanent departure exists at every ceiling above its initial value: determinism gives an injective path escaping every finite interval. Its label therefore carries the entire predecessor set of the initial point. At a positive ternary-unit seed of the orbit the fixed-target predecessor input gives that set positive lower natural density. This is the mass whose disappearance must actually be proved. Reverse traversal of the edge produces the *inverse* predecessor path. Its law depends on predecessors of $q$ and is not the forward first-downward landing law. [The same-source counterexample](CROSSINGS.md) proves that the latter does not even transport summability to the final upward crossing on convergers. Those crossings return below the ceiling, so the counterexample leaves the permanent-departure question open.

## PR201's additive reduction on a mesoscopic profile

At the selected ordinary common clock in [PR201, KG9, head `3c9e444e3f2f2e457b25cd827dc9a29f981e9de2`](https://github.com/GettysburgResearch/collatz/blob/3c9e444e3f2f2e457b25cd827dc9a29f981e9de2/research/killed-green-head-closure-20261124/README.md), orient the actual values as $Y=3^s X+D$. Here $H^{1/8}<s\ll\sqrt{H\log H}$ and $|D|/3^s\le H^4$. Let $E$ be the first shortcut time at which the path from $X$ has used $s$ odd inputs. Positive integers have another odd input after finitely many halvings, so $E$ is finite. Put $W=T^E(X)$ and use the exact binary-prefix carry $C$. Then
$$
 2^E W=3^s X+C=Y+(C-D).
$$
Thus the convergence colors of the original pair equal the colors of the genuinely additive pair $(Y,Y+C-D)$, even when the two original clocks differ. On the event $C=D$ the colors already agree.

The candidate next inference was to apply the uniform additive fusion tail at offset $C-D$ after exposing this prefix, obtaining fresh cancellation at the remaining clock. The exact source congruences show why this does not follow:
$$
 Y+C-D\equiv 0\pmod{2^E},\qquad Y\equiv D-C\pmod{2^E}.
$$
On a specified prefix the displacement is fixed **and the starting residue of the additive pair is prescribed**. Leen's grid estimate is an average over all binary residues at the available depth for a fixed displacement. Conditioning that average on the displayed single cylinder can cost $2^E$ even before accounting for the earlier profile selection. In the next $E$ paired steps the padded arm makes $E$ compulsory halvings to $W$. The signed difference of the two newly accumulated odd counts at that time is exactly the number of odd inputs on $Y$'s own $E$ steps, up to orientation. No uniform bound making this difference small on the selected physical source law has been obtained. The missing estimate must retain the joint law of $C-D$ and its prescribed source cylinder, or avoid this padding. [Uniform additive fusion and finite source grids, equation (1)](https://rstation.ai/problems/collatz/papers/13/v1)

## The adelic boundary and the shifted moment

For $s>1$ write $P_s(e=j)=(2^s-1)2^{-sj}$ and $D_s=\sum_{x\text{ positive odd}}x^{-s}$. Let $\mu_s$ be the law of the infinite *actual* odd-gap word when $x$ is chosen with probability $x^{-s}/D_s$. On the finite word $w$ its likelihood relative to the iid word law is
$$
 L_N(w)=\mu_s([w])/P_s^{\otimes N}(w).
$$
These likelihoods form a nonnegative mean-one martingale. The infinite law $\mu_s$ is concentrated on countably many individual words, while every such word has iid probability zero since each factor is at most $1-2^{-s}<1$. Consequently the full likelihood martingale cannot be uniformly integrable: a uniformly integrable limit would give an iid-absolutely-continuous measure with the same cylinder probabilities as $\mu_s$, contradicting singularity. This conclusion holds regardless of Collatz's truth value.

Brofferio's rational-affinity theorem identifies measured Poisson boundary coordinates at the contracting places. For the iid affine maps $z\mapsto(3z+1)/2^e$ the expected ternary log multiplier is $-\log 3$, the dyadic one is $\mathbb E[e]\log 2>0$, and the real one is $\log3-\mathbb E[e]\log2$, with $\mathbb E[e]=2^s/(2^s-1)$. The real coordinate enters only for a negative real drift. The affine maps with exponents one and two do not commute, and the geometric tail gives the finite first moment in the affine gauge since each step's logarithmic height is $O(e+1)$. That theorem treats the independent right random walk; reversing a finite word preserves its iid law, and does not identify the chronologically nested prefixes of a fixed physical orbit with sample paths of that right random walk. Even when an iid boundary distribution is nonatomic, it gives no bound on the surviving physical atoms just described. [Brofferio, *The Poisson boundary of random rational affinities*, Theorem 5.1](https://www.numdam.org/article/AIF_2006__56_2_499_0.pdf)

In [PR192's exact shifted moment, head `045be43632f274dd64faf15714e42cc8de27a2e9`](https://github.com/GettysburgResearch/collatz/blob/045be43632f274dd64faf15714e42cc8de27a2e9/research/astra-high-variance-20261124/CENTRAL_CLOSURE.md), a fixed positive odd $x$ already on the least lift gives precisely $x^{-s}$ at every depth with terminal value above one. The first unsupported inference would be that iid boundary nonconcentration makes the *killed*, reweighted mass on those words vanish. Full-likelihood singularity supplies no such bound. The [updated rational-shell calculation](https://github.com/GettysburgResearch/collatz/blob/5720732b9c83361f5cded4f8bfac24e36f469937/research/astra-universal-step-20261124/moment.md) controls noninteger tails at exact denominator $3^d$ for $d\ge1$. Its congruence repair changes an endpoint by a sibling exponent in one class modulo $3^d$; mere existence of the class gives no small real-height cost. Denominator $d=0$ retains the original fixed positive source. Neither the escape nor the additional-cycle contribution to that term is bounded here.
