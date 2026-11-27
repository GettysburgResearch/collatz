# Simultaneous ternary escape from polynomial-height rational anchors

Let n be any positive odd integer and x_i=U^i(n), where 2^{e_i}x_(i+1)=3x_i+1 and e_i≥1. An anchor t=p/q is any positive rational in reduced form. Its height is max(p,q). Its address depth at x is v₃(x+p/q), measuring proximity to the **negative** rational −t. This valuation is finite. It equals v₃(qx+p) when 3∤q. An anchor with 3|q has negative depth and can be omitted when maximizing over all rationals of bounded height, since the anchor 1 has nonnegative depth. For a nonempty finite anchor set A let V_A(x) be the maximum of these depths. All logarithms in estimates may use a fixed base greater than one.

## One shallow clock in each window

**Theorem 1.** There is an absolute effective C with the following properties.

1. Fix H≥1 and let A be the set of all positive rational anchors of height at most H. Starting directly at n, some j≤1+⌊log₂[H²(n+1)]⌋ satisfies

   V_A(x_j) ≤ C log(2H) log(3+log[H(n+1)]).

2. If (4/3)^J>(n+1)H², then some j∈[J,2J] satisfies

   V_A(x_j) ≤ C log(2H) log(3+J+log(n+1)).

3. On any primitive positive ordinary cycle of odd period P, some state x satisfies

   V_A(x) ≤ C log(2H) log(3+P).

There is no cardinality hypothesis in these assertions. In particular every sufficiently late dyadic window of every supplied positive orbit has a clock simultaneously shallow for **all** positive rationals of height at most (2J)^b, with depth O_b((log J)^2). For a fixed finite set of anchors the corresponding bound is O(log J). No assumption that the trajectory eventually repeats is needed.

### Exact relations at two adjacent positive phases

Select a maximizing anchor with denominator prime to three at every clock in a window; break remaining ties arbitrarily. Write p/q and u/v for two successive choices and let e=e_i. The signed transition is exact if

2^e q u = v(3p−q).

For a transition discrepancy let D=2^e q u−v(3p−q)≠0. The ordinary recurrence gives the identity

D=2^e q[v x_(i+1)+u]−3v[q x_i+p].

Consequently 3^m divides D for m=min(V_A(x_i)+1,V_A(x_(i+1))). The absolute-value bound gives the elementary m log₂3≤e+2log₂H+log₂3. The stronger bound needed for the theorem is

m ≤ C log(2H) log(max(3,e)).                                              (1)

To see this, put A₀=q u and B₀=v(3p−q). B₀ is a nonzero 3-adic unit because q,v are units. If 3|A₀ then 3∤D. Otherwise apply Kunrui Yu's Theorem 1 to the two rational 3-adic units 2 and A₀/B₀, with exponents e and 1, in the field of rational numbers. The logarithmic form is D/B₀, nonzero by the definition of discrepancy. The field hypothesis holds since 3≡3 mod4. The degree, residue degree and ramification index are all one. The logarithmic Weil height of A₀/B₀ is at most log(4H²), including when B₀<0. The lower height cutoff is log 3 and the exponent cutoff is max(3,e). Yu's bound therefore gives (1) with an absolute effective constant. His Theorem 1 imposes no multiplicative-independence condition here. With natural logarithms, the explicit displayed consequence on printed p. 337 yields C=1,200,000,000,000 in (1). Indeed (20√3)^6=1200³; h₁=ln 3 and h₂≤2ln(2H). After cancellation, the coefficient is at most 19·1200³·6·(5+ln2)/ln3 < 1,200,000,000,000. Thus for a concrete window ending by clock T one may use the fully specified bound C ln(2H) ln(max(3,⌈2+T log₂(3/2)+log₂(n+1)⌉)). The large effective constant reflects this general published estimate. This paper uses the published theorem as an external input. [Yu, *p-adic logarithmic forms and group varieties II*, Acta Arith. 89 (1999), Theorem 1, pp. 337–339](https://matwbn.icm.edu.pl/ksiazki/aa/aa89/aa8944.pdf)

### A matching interval has a finite dyadic budget

Suppose k consecutive transitions from clock i have exact signed transitions and total division exponent E. The paired positive/negative affine maps give

2^E q_i[q_(i+k)x_(i+k)+p_(i+k)] = 3^k q_(i+k)[q_i x_i+p_i].

This follows by multiplying the adjacent identities and cancelling positive denominators, or by induction on k. Therefore 2^E divides q_(i+k)[q_i x_i+p_i], giving 2^k≤H²(x_i+1). If all selected denominators are odd, already 2^E divides q_i x_i+p_i and the bound sharpens to H(x_i+1). For reduced odd/odd anchors with denominator prime to three, the denominators remain constant on every exact edge: gcd(3p−q,q)=1 and e=v₂(3p−q), giving the next reduced numerator (3p−q)/2^e over the same q. The dyadic bound concerns the state and rational at the **start** of the interval.

The elementary growth inequality x_i+1≤(3/2)^i(n+1) now rules out J exact edges between J and 2J under the stated size condition. It also rules out 1+⌊log₂[H²(n+1)]⌋ exact edges from clock zero. Moreover 2^{e_i}≤3x_i+1, hence e_i≤2+i log₂(3/2)+log₂(n+1). Apply (1) to the forced discrepancy. At least one of its two adjacent clocks has V_A≤m. This proves the first two assertions.

For a cycle, choose the same maximizing anchor whenever the state repeats. If all P transitions matched, the product identity would force 2^E=3^P because the positive initial and terminal sums and denominators agree. This is impossible for P>0. Also 2^E=∏[(3x_i+1)/x_i]≤4^P, so each e_i≤2P. Applying (1) to one discrepancy proves the third assertion.

### A comparison to smaller positive ordinary phases

The same window statement permits **signed** rational anchors |p|,q≤H if the starting state x_i exceeds H. Use the true depth v₃(x_i+p/q), allowing +∞ at an exact equality. The condition x_i>H guarantees a nonzero starting displacement even for the maximizing signed anchor. Its absolute value is at most H(x_i+1). On any discrepant edge the identity still gives (1), so at least one of its two endpoints has finite shallow depth even if the other equals a rational anchor exactly. The zero anchor has numerator 0; if chosen on the right then A₀=0 and D=−B₀ is a 3-adic unit. Denominators divisible by three have negative depth as before.

In particular, for H<n, within 1+⌊log₂[H²(n+1)]⌋ accelerated steps of n there is a clock shallow relative to **all positive and negative rational numbers** of height at most H. On a primitive cycle, either its maximum is at most H or at least one clock has the same signed shallow bound C log(2H)log(3+P). In the latter case start the closed-lap argument at a state above H. The rational roots actually compared by a toric lag need not satisfy a polynomial height cutoff.

## Many shallow clocks on one orbit

**Theorem 2, source-qualified to Lyapunov Weaver's Paper 15 v2.** Fix 0≤θ<1 and b≥0. For every sufficiently large N, let A_N be any nonempty set of at most C₀(2+N)^θ reduced positive odd/odd rational anchors with denominators prime to three and height H_N≤C₀(2+N)^b. The sets may change arbitrarily between horizons; nesting is unnecessary. On a fixed non-eventually-periodic positive orbit, among the clocks 0,…,N there are at least c_θ log N loglog N distinct clocks satisfying

V_(A_N)(x_i) ≤ C log(2H_N) log(3+N+log(n+1)).                             (2)

The threshold may depend on n, b and C₀. For every sufficiently large primitive positive ordinary cycle of odd period P, for sets A_P under the same bounds there are at least c_θ log P loglog P distinct cyclic clocks satisfying V_(A_P)(x_i)≤C log(2H_P)log(3+P).

For an eventually periodic supplied orbit, all its positive states have some finite maximum X_n. Then V_(A_N)(x_i)≤log₃[H_N(X_n+1)] at **every** clock. This handles positive cycles that could be represented by the varying dictionaries in the orbit part, without applying a theorem beyond its stopping rule.

### Encoding exact transitions with a charged dictionary

For this section fix a set of M distinct reduced odd/odd anchors of height at most H, all denominators prime to three. Form its finite directed graph using *only* exact signed transitions of positive exponent. Each vertex has at most one outgoing edge: if 3p−q≤0 there is none, and otherwise e=v₂(3p−q) is forced because p,q,u,v are odd. The next rational (3p−q)/(2^e q) is then fixed. Its reduced form agrees with the selected next vertex if an edge exists. All edge exponents are at most log₂(3H²). Each connected component consists of a directed cycle with incoming trees or a sink with incoming trees.

Fix ε>0. We construct one dictionary W_A of positive exponent words for the whole graph. Its total division budget is

B(W_A) ≤ C_ε M^(1+ε) log(2H),                                              (3)

and **every finite directed path**, with arbitrary entrance vertex, length and terminal cut, has a decomposition using at most C_ε counted pieces. Pieces follow the conventions of Paper 15: any factor of an infinite repetition of a dictionary word is one counted piece, each singleton exponent ≥2 may count as a piece, and a string of ones is free.

Put L=max(2,⌈M^ε⌉). For every nonterminal transient vertex w let d(w) be its number of edges to its first cyclic vertex or sink. Distances decrease by one before termination. Set C₀ to all these transient vertices. After selecting C_l by one residue of d(w) modulo L^l, choose the **least occupied** of its L refining residues modulo L^(l+1) to define C_(l+1). Then |C_l|≤M/L^l. The first K with L^K>M has C_K empty; K≤1+⌈1/ε⌉.

For each w∈C_l, 0≤l<K, store its labeled forward path to the first vertex of C_(l+1), or to the terminal cycle/sink if reached first. If w already lies in C_(l+1), the stored path is empty. Distances traverse consecutive integers, so this path contains at most L^(l+1) edges even when the chosen refining residue is absent from part of the graph. The weighted cost for layer l is at most M L log₂(3H²). Store one full word for each directed cycle, of total cost at most M log₂(3H²) over all cycles. Omit empty and all-one words; add the one-letter word (2) if required for a nonempty dictionary. Removing duplicates decreases the budget. With L≤2M^ε this proves (3).

Now follow any actual graph path. At each layer use its stored word, or its prefix if the path terminates inside that word. If the current vertex already belongs to the next layer, advance the layer without consuming any edge. On reaching a cycle, all remaining edges through any number of laps and any final cut constitute a single factor of its repeated word, or a free string of ones. At most K+1 counted pieces are used. The procedure follows the supplied vertex sequence throughout.

### Application of the external complexity estimate

Let D be the number of discrepancies for the chosen maximizing anchors across one N-step prefix. The D+1 exact stretches have their preceding decompositions. Each discrepant transition is a singleton or a free one. Therefore its actual exponent word has piece cost at most (K+2)(D+1).

Choose ε such that θ(1+ε)<1. Since log(2H_N)=O(log(2+N)), (3) gives B(W_A)≤N^β for some fixed β<1 and every sufficiently large N. Paper 15's Theorem 9, equation (A1), gives minimum piece cost ≫_β log N loglog N for a fixed non-eventually-periodic positive source and any such dictionary. Its stopping condition is satisfied since this source never enters 1 or any positive rational cycle represented by the dictionary. This yields D≫_θ log N loglog N. For each discrepancy, (1) and the actual bound on e_i give (2) at one endpoint. Each clock is adjacent to at most two discrepant edges, so at least D/2 distinct clocks qualify.

For a primitive positive ordinary P-cycle of sufficiently large odd period P, (3) gives B<P. No dictionary word can represent this positive cycle since that word would have to contain a multiple of P odd steps and have length at least P. Paper 15's adaptive cycle estimate (C6) with denominator one and B≤P^β gives cyclic piece cost ≫_β log P loglog P. Cutting the cyclic phase assignment at an arbitrary vertex costs at most a bounded extra piece in the upper construction; alternatively repeat the good-stretch argument around the cycle, starting at any discrepancy. Together with e_i≤2P this proves the cyclic assertion. [Lyapunov Weaver, *Height and periodic-dictionary complexity for rational Collatz trajectories*, Paper 15 v2, (C6) and Theorem 9](https://rstation.ai/problems/collatz/papers/15)

## What a missing global argument must force

Theorem 1 applies to all positive rational anchors of polynomial height simultaneously. Theorem 2 counts the shallow clocks for any smaller family with sublinear power cardinality. Neither result forces a given orbit to stay deep at all clocks of a late window. They are compatible with an orbit that nearly always stays shallow and never meets a smaller ordinary source. The toric lag discrepancy B_i−u compares two positive trajectory windows and does not supply a deep negative rational anchor at those clocks. Converting lag rigidity into such a forced address pattern, or obtaining an actual ordinary merger when the pattern is absent, remains open.

The nearby PR193 checkpoint 795cfa38fbd6a2436285edfe82580680df4f9b0d studies the Farey current, primitive modular markers for rational-cycle denominators, and symbolic complexity of invariant colorings across intervals of **distinct starting integers**. Those are different observables from adjacent accelerated phases on one supplied source. This comparison covers the named checkpoint files and does not establish publication priority beyond the examined sources.
