# Ternary dimension of stationary inverse-word laws at nonpositive real drift

**PROPOSED.** Let (a_i) be any stationary ergodic process of positive integer inverse Syracuse valuations with finite mean b and entropy rate H in natural logarithms. Its ternary target is

    π(a) = Σ_(i≥1) 3^{i−1}/2^{A_i},          A_i=a_1+...+a_i.

The series converges in the ternary integers for every label sequence. The lower and upper pointwise dimensions of its law ν are the liminf and limsup of −log ν(z+3^q Z₃)/(q log 3). For ν-almost all z they satisfy

    min(1,H/log3) ≥ upper dimension ≥ lower dimension
             ≥ max(0,(H−max(0,b log2−log3))/log3).               (1)

In particular the law is exact-dimensional of dimension H/log3 whenever b≤log₂3. This includes dependent processes; no independence of letters is assumed. For independent geometric letters P(a=j)=2^{-j}, H=2 log2 and b=2, both bounds in (1) give one. This last example recovers full dimension by elementary collision counting; absolute continuity of that example follows separately from Tao's stronger mixing estimate.

## Counting ambiguous prefixes

The q-letter prefix requires the ternary congruence 2^{A_q} z≡C_q mod 3^q, where

    C_q = Σ_(i=1)^q 3^{i−1} 2^{A_q−A_i}.

Distinct words of the same total A_q give distinct positive C_q. For q≥2, C_q−3^{q−1}=2^{a_q} C_(q−1), with C_(q−1) odd. Extract the last letter by dyadic valuation and recover the first using the total. For q=1 the total already specifies the word.

By the ergodic theorem A_i=bi+o(i) almost surely. Hence max_{i≤q}|A_i−bi|=o(q) and

    C_q/3^q ≤ (q/3) exp(q max(0,b log2−log3)+o(q)).

On a set where this bound and A_q≤(b+1)q hold with fixed exponential tolerance δ for every q≥q_0, the number of its prefixes mapping to any particular q-cylinder is at most exp(q[max(0,b log2−log3)+2δ]) for large q. Indeed for each of O(q) totals the admissible C_q occupy one residue class modulo 3^q. The estimate uses the size of the actual integer numerator; distinct words can occupy the same ternary cylinder.

## Dimension of the pushed-forward measure

The one-letter entropy is finite, since among positive integer laws with given finite mean the geometric law maximizes entropy (or compare against a fixed geometric distribution using the entropy inequality). The Shannon–McMillan–Breiman theorem for the countable generating partition gives cylinder probabilities exp(−qH+o(q)) along almost every sequence. Thus the ternary cylinder containing a typical image has mass at least exp(−q(H+δ)) for every q sufficiently large, giving its upper dimension bound. The ambient bound of one for upper pointwise dimension almost everywhere also follows directly: q-cylinders of mass below 3^{-q(1+δ)} have total mass at most 3^{-qδ}, summable in q.

For the lower bound restrict the original law to sequences satisfying the preceding counting bounds and cylinder probability ≤exp(−q(H−δ)) simultaneously for every q≥q_0. The masses of these restrictions increase to one as q_0 increases. Each restricted image has mass at most exp(−q[H−max(0,b log2−log3)−3δ]) on each q-cylinder for all sufficiently large q. This bound transfers to the unrestricted local dimension almost everywhere on that restricted image: the ratios of the restricted and unrestricted masses on nested cylinders converge to the Radon–Nikodym derivative, positive almost everywhere for the restricted measure. Let q_0 increase and δ decrease to zero. This proves (1).

## Ordinary-orbit scope

In a forward ordinary odd orbit, the residue of the state after q or more odd steps is determined modulo 3^q by its last q valuation labels in reverse chronological order. Thus when an orbit has empirical frequencies for every finite reversed word given by such a process (including exhaustion of the mass at each fixed length), its empirical ternary state distribution is precisely ν. A nonperiodic ordinary orbit with a finite limiting average b has b≤log₂3, by the [distinct-orbit correction bound](../integrated/orbitwise-boundaries/README.md). Equation (1) then identifies the dimension whenever its empirical word law is ergodic and has that mean. It imposes no genericity assumption on arbitrary Collatz trajectories and does not establish that a particular positive source has one of these statistical laws.

For independent geometric letters, an earlier full entropy-dimension formula min(1,H/log3) is reported and used in rStation paper 135, which further studies the law at its critical parameter. The counting argument here treats arbitrary ergodic dependence at b≤log₂3; it does not strengthen that earlier independent-law formula. [Prior tilted-law work](https://rstation.ai/problems/collatz/papers/135/v1)
