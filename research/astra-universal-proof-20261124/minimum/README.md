# The running minimum and unbounded surviving exits

**PROPOSED obstruction to a bounded descent clock. The least bad triple remains OPEN.** Let $T(2u)=u$ and $T(2u+1)=3u+2$. A good positive integer reaches 1. Let $q$ be an odd source and $n=3q$. In the minimum argument, $q$ is the least odd source with different basin membership on its two arms. It is then good, $n$ is bad, and all smaller positive multiples of 3 are good. [PR192 minimum theorem, frozen source](https://github.com/GettysburgResearch/collatz/tree/26f070c38ad9edd21ed7dac6efaab6554550c2a3/research/astra-minimum-source-20261124)

**Arbitrary finite strings of expanding whole runs with a convergent lower arm.** Fix any integers $K,h\ge1$. There are infinitely many positive odd $q$ such that $q$ reaches 1, $v_3(3q)=h$, and the ordinary trajectory of $3q$ begins with at least $K$ copies of `11110`, where 1 marks an odd shortcut input. Throughout the first $5K$ steps its values are at least $3q$. At each of the first $K$ run exits, writing its input as $2^m a-1$ with $a$ odd gives $m=4$ and $3^m a=3\bmod4$. Each exit is followed by a new odd run.

*Upper arm.* For $x=32u+15$, the first five input parities are `11110`. Direct substitution gives
\[
       T^5x=81u+40=(81x+65)/32,\qquad
       49T^5x+65=81(49x+65)/32 .
\]
Each of the first four steps increases the current value, and $81u+40>32u+15$. Put $d=5(K+1)$ and prescribe $147q+65=0\bmod2^d$, a unique odd dyadic class. While $32\mid49x+65$, reduction modulo 32 gives $x=15\bmod32$, so the displayed five actual steps spend exactly five factors of 2 from this divisibility. Starting at $x=3q$ gives at least $K+1$ blocks. Within each of the first $K$ blocks the endpoint is odd by the next block, so the even state $3^4a-1$ just before it is $2\bmod4$. This proves the exit assertion.

*Lower arm.* Take the positive representative $r\le2^d$ of the chosen class and follow its own $d$ steps. Write $s$ for the number of odd inputs and $E=T^d r$. The affine lift of a fixed parity prefix gives
\[
                    T^d(r+2^d t)=E+3^s t\quad(t\ge0).
\]
This follows by applying each shortcut to the two sources, halving the difference and multiplying it by 3 at odd steps. Since $r$ is odd, $s\ge1$. After its first odd step the value is a ternary unit, and subsequent odd or even steps preserve being a unit, hence $3\nmid E$.

Choose $t_0\bmod3^h$ so that $r+2^d t_0=3^{h-1}\bmod3^h$. For $t=t_0+3^h j$, the endpoints $E+3^s t$ fill an arithmetic progression of difference $3^{s+h}$ starting at a unit. Every unit class modulo $3^e$ contains arbitrarily large powers of 2: the order of 2 is $2\cdot3^{e-1}$, since $v_3(4^{3^i}-1)=i+1$ by cubing and factoring, and reduction modulo 3 forces even order. Select any such power above the start of the progression. The corresponding $q=r+2^d t$ reaches it after $d$ steps, hence reaches 1. Increasing the exponent by an arbitrary multiple of the order gives infinitely many distinct $q$.

**Separate finite clocks on both arms.** The same family can additionally avoid every physical meeting between $q$ and $3q$ with both clocks at most $5K$. Evaluate the prescribed lower and upper parity prefixes at the rational parameters $q_*=-65/147$ and $3q_*=-65/49$, using the parity of the numerator of a fraction with odd denominator. The upper arm cycles through numerators $-65,-73,-85,-103,-130$ over denominator 49. After its first step the lower arm has successive numerators $-8,-4,-2,-1,23$ over 49 and stays positive thereafter. Including $q_*$ itself, the two rational traces are disjoint. For each clock up to $5K$, the rational trace and an ordinary lift of the prescribed class share their parity prefix: congruence modulo $2^d$ loses at most one binary digit at each step. Consequently each proposed pair of clocks gives two rational affine functions of $q$ whose values at $q_*$ differ. Equality excludes at most one ordinary $q$ per clock pair. Remove these finitely many values from the infinite family above. This tests direct meetings of the two supplied arms, with no restriction on the unobserved tail.

The use of powers of 2 to populate a specified cylinder has an antecedent in the repository. The construction above imposes the upper-arm whole-run prefix and an exact ternary valuation simultaneously. [Earlier convergent-lower-arm construction](../../astra-global-resolution-20261124/arithmetic/RESIDUAL_GHOST.md)

**First unsupported step.** The fixed integers $h=3$ and $m=4$ already permit any preassigned number of consecutive increasing blocks on candidates with a genuinely convergent lower arm. A bound on the number of whole runs before visiting the known good interval cannot follow from just these valuations, the exit orientations and lower-arm convergence. Also, $3q$ itself has only the predecessors $2^j3q$, since an odd step always lands in a ternary unit. A smaller representative in its component must merge strictly forward of $3q$. Minimality supplies additional information about other integers. The construction neither satisfies nor refutes that additional premise, and proves no all-time survival. A complete descent still requires an adaptive smaller-source merger or a proof that every fixed ordinary candidate eventually leaves the surviving configuration in a way that forces convergence.

The one fixed periodic parity word above cannot itself realize an infinite positive trajectory: infinite repetition would require $2^{5K}\mid147q+65$ for every $K$, impossible for fixed positive $q$. The unresolved all-time quantifier permits aperiodic itineraries.

[RunClock.lean](RunClock.lean) proves the five physical steps, the equivalence between $K$ expanding blocks and $32^K\mid49x+65$, and finite exit at each fixed source. The simultaneous lower-arm interpolation is a written proof. [Exact replay of the construction](check.py)

The [independent cycle-occupation review](CYCLE_REVIEW.md) checks the moving-octave capacity and the interaction with the bounded-cycle alternative.
