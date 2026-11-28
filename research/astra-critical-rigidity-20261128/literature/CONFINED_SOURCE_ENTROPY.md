# Matching source counts for positive Collatz trajectories confined below a factor of four

Fix a real \(2<R<4\), put \(\gamma=\log_2 3\), \(\alpha=\gamma-1\), \(e=2-\gamma\), and define
\[
                 w=\log_2(R/2),\qquad h(w)=w-e(w-\alpha)_+ .
\]
Let \(A(M,n;R)\) count the odd positive integers \(x\) whose next \(n\) Syracuse iterates, as well as \(x\) itself, belong to the *same physical band* \([M,RM]\). If \(n\to\infty\) and \(M/3^n\to\infty\), then
\[
                  A(M,n;R)=\frac{M}{3^n}\,2^{h(w)n+o(n)}.              \tag{1}
\]
This includes \(n=\lfloor\lambda\log_3 M\rfloor\) for every fixed \(0<\lambda<1\), giving exponent \(1-\lambda+\lambda h(w)/\gamma\) in \(M\). It also includes \(n/\log_3 M\to1\) with \(\log_3 M-n\to\infty\), giving exponent \(h(w)/\gamma\). For \(n=\log_3 M+O(1)\) the upper bound is still \(A\le M^{h(w)/\gamma+o(1)}\). In particular **every chronological segment of distinct positive odd states confined to \([M,RM]\)** has at most \(M^{h(w)/\gamma+o(1)}\) states. At \(R=3\) this exponent is \(1-\log_3 2=0.36907024\ldots\). The matching lower bound in (1) counts actual starts which survive the stated logarithmic deadline. It does not assert a matching maximum length on one orbit.

## Which binary choices preserve the positive divisions?

For a real phase \(t\) and a tolerance \(0<s<1\), define \(W_i=\lfloor t+i\gamma\rfloor\), \(\theta_i=\{t+i\gamma\}\). On dates \(1\le i\le n\) the allowed cumulative division choices are \(W_i-b_i\), where \(b_i\) is zero unless \(\theta_i\le s\), and otherwise is zero or one. Require that successive cumulative divisions increase by at least one. The increment \(W_i-W_{i-1}\) is either one or two. At an incoming increment two, both available endpoint bits may be chosen freely. At an incoming increment one only \((b_{i-1},b_i)=(0,1)\) is forbidden. This restriction can matter only if \(\theta_i\in[\alpha,s]\): the incoming increment is one exactly for \(\theta_i\ge\alpha\), and in this case \(\theta_{i-1}=\theta_i-\alpha\). Whenever the current bit is optional, the previous bit is then optional too. The assertion for the first date may instead involve a prescribed initial value. Incoming unit increments cannot occur on consecutive edges, since \(\alpha>1/2\).

Thus among \(a\) optional positions and \(b\) internal constrained edges there are exactly \(2^{a-2b}3^b\) configurations, prior to imposing the initial condition. It can be imposed for a lower bound by fixing the first bit to zero when \(W_0=0\); this costs at most a factor three. Uniform distribution of the irrational rotation, uniformly in its starting phase, gives
\[
         a=sn+o(n),\qquad b=(s-\alpha)_+n+o(n).
\]
Endpoint ties have bounded multiplicity. The estimates remain valid for tolerances tending to a fixed \(s\), by bounding between fixed arcs. Consequently the log base two of the number of choices is \(h(s)n+o(n)\). In particular, when \(R\le3\) the physical width gives \(h(w)=w\).

For the upper bound use equation (4) of the [near-doubling residence argument](NEAR_DOUBLING_RESIDENCE.md). With \(z=\log_2(x/M)\), the actual cumulative divisions satisfy exactly the above necessary options at \(t=z+n/(3M\ln2)\), \(s=w+n/(3M\ln2)\). The interval of starting phases divides into \(O(n)\) open cells and singletons on which all options and actual increment constraints are fixed, including \(W_0\) if needed. There are consequently at most \(2^{h(w)n+o(n)}\) possible words. Every word has \(A_n=n\gamma+O_R(1)\). A fixed word lives on one residue class modulo \(2^{A_n+1}\): its native binary word consists of an odd step and \(a_i-1\) even steps for each \(i\), then one prescribed final odd input. Iterating the affine rule on a fixed parity branch identifies every binary word of length \(A_n+1\) with exactly one class modulo \(2^{A_n+1}\). Each contributing word therefore has at most \(O_R(1+M/3^n)\) sources in the band. This proves both upper bounds and hence the stated bound for a distinct segment after adding its final \(n\) states.

## Realizing the choices on ordinary integers

For \(0<\eta<\min(w/3,1/8)\) set \(z_0=1/2\), \(t_-=z_0-\eta\), \(s_-=w-2\eta\). Use the allowed words at this phase and tolerance with \(A_0=0\). Their homogeneous logarithmic coordinates satisfy
\[
              \eta\le z_0+i\gamma-A_i\le 1+w-\eta\qquad(0\le i\le n).
\]
The preceding count gives \(2^{h(s_-)n+o(n)}\) distinct legal division words. For each word keep the ordinary starts in its exact dyadic class whose initial coordinate \(z=\log_2(x/M)\) is in \([z_0-\eta/4,z_0+\eta/4]\). This is an integer interval of length \(\asymp_\eta M\), whereas the modulus is \(O_R(3^n)\). Thus it contains at least \(c_{R,\eta}M/3^n\) representatives for all sufficiently large \(M/3^n\). Words give disjoint sets of representatives, since the true odd valuation itinerary is unique.

Every retained representative remains inside the physical band through date \(n\). Indeed, if the preceding states have stayed above \(M\), their accumulated positive correction in (4) is at most \(n/(3M\ln2)<\eta/4\) for large \(M\). The initial real deviation from \(z_0\) is at most \(\eta/4\); the displayed interior margin gives the induction step at both ends. This proves a lower exponent \(h(w-2\eta)\) after dividing the count by \(M/3^n\). Letting \(\eta\downarrow0\) proves (1).

At the upper edge \(w\uparrow1\), the intrinsic word exponent \(h(1)/\gamma=4-\gamma-3/\gamma=0.5222482385\ldots\) is the known height-one raw word rate. Weaver's Paper 145 obtains a stronger uniform exponent \(0.4333973955\ldots\) for confined chronological residence throughout the band below four using a *longer* source deadline, about \((4/3)\log_3 M\). At moderate fixed widths one may use the smaller of that bound (with its arbitrarily small exponent loss) and the width-specific bound here. The population lower bound proved here has \(3^n=o(M)\), which leaves many genuine integer lifts in each prescribed interior slice. Weaver's exact strict factor-two confinement characterization is separate. [Weaver 145, Theorems 1 and 6](https://rstation.ai/problems/collatz/papers/145/v1) · [Weaver 222, Theorem 1](https://rstation.ai/problems/collatz/papers/222/v1)
