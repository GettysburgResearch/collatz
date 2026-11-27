# Opposing estimates must resolve the real carry inside the exact clock

**Status.** Written deduction, conditional on the exact-clock floor F. Universal convergence and the needed carry-restricted upper estimate are OPEN.

For positive odd q prime to three and a word w of b outward Syracuse gaps with total 2b, put
$$
 L_b(q)= (3/4)^b \#\{w:\beta(w)\equiv q\pmod {3^b},\;x=(4/3)^b(q-\beta(w))\text{ is an ordinary unit}\}.
$$
Under the independent geometric-letter law, this is the scaled mass of the exact row with the indicated unit-source restriction. Each such word has probability exactly $4^{-b}$. Let $L_b^{\ge\epsilon}(q)$ restrict this same sum to $\beta(w)\ge\epsilon q$.

**Claim.** Under F there is $c>0$ with $L_b(q)\ge c/\sqrt b$ simultaneously for every ordinary unit $q>1$ and all sufficiently large b. Thus even on retained terminals $b/64<q\le ((3/2)^b-1)/\epsilon$, no exponential upper bound on the entire exact-clock mass can certify the required source bound through this mass majorant.

Indeed, use the PR205 annulus lemma with total $2b$, radius 1 and deficit $K=1$. Choose the fine residue
$$
 r=q-3^b4^{-b}\pmod {3^{b+1}}.
$$
It is a unit. The lemma supplies at least $c(4/3)^b/\sqrt b$ words after absorbing the fixed extra factor three. Each has $0<\beta\le1<q$, and $4^b(q-\beta)/3^b\equiv1\bmod3$. Its positive integer source is odd since the numerator is the difference of an even integer and an odd integer. Successively reducing the outward affine numerator modulo three verifies each inverse step, and the positive odd source fixes the word uniquely. This proves the claim. All these specific witnesses have $\beta/q\le1/q$, so at $q>1/\epsilon$ they contribute zero to the carry-restricted sum.

PR201's lower count $2^{\lceil b/32\rceil}$ at a retained terminal would give $L_b^{\ge\epsilon}(q)\ge (3/4)^b2^{\lceil b/32\rceil}$. The latter decays exponentially, whereas the entire row's mass at each such terminal is at least a constant times $b^{-1/2}$. Consequently neither a uniform boundedness estimate nor sharper polynomial upper bounds for the entire row at that terminal can supply the opposing count via positivity alone. Cancellation or a separate upper bound after the real cutoff would be additional mathematics. This does not refute such an upper bound.

Dependencies: [PR201 exact row and retained-terminal alternative at 2978d84f8a1fda9083593b26c6bf724d5976d859](https://github.com/GettysburgResearch/collatz/tree/2978d84f8a1fda9083593b26c6bf724d5976d859) and [PR205, JOINT_REAL_FLOOR, annulus (1) at 32d722c5d5597846da5dad842c8ea15742abc176](https://github.com/GettysburgResearch/collatz/blob/32d722c5d5597846da5dad842c8ea15742abc176/research/astra-fixed-target-closure-20261124/analytic/JOINT_REAL_FLOOR.md). F is a source-qualified input from [Weaver and Wren, paper 48 v2, Lemma 7](https://rstation.ai/problems/collatz/papers/48/v2). No independent validation of its analytic proof is claimed.
