# Independent reconstruction of the two-light descent grammar

**VERIFIED at the scope of theorem two_light_descent.** Source research/astra-global-closure-20261124/round3/descent/TwoLight.lean has SHA-256 fdddc3ede29502691ea2a27354abdd8b09faee98fc0f338bb3b970c9cf141964. I rebuilt both imported project modules into a new empty olean directory and compiled the frozen source against them with Lean 4.34.1, -j1 and warningAsError enabled. All three processes exited zero. The theorem reports propext, Classical.choice and Quot.sound. CycleShadows.lean has SHA-256 05ef6b77b2ce9d571c598e5a0e4a526be3412b844349476ec72408b0bf145e99 and ResidualDescent.lean has SHA-256 b5f149855866419b771e49127bdaabd1cb5749ec7d6f3b6091f3fb54bf1ccc98.

The hypotheses provide one infinite chain of odd natural boundaries $q_i$ on the ordinary shortcut map. The actual L and P bit words are $101$ and $11000$, with affine triples $(2^a,3^k,C)=(8,9,7),(32,9,5)$. Each numerical edge forces its literal bit word by the odd multiplier and divisibility by $2^a$. On L the intermediate odd point is $(3q_i+1)/4$, and on P it is $(3q_i+1)/2$. The two grammar predicates prohibit PPP and PLP everywhere. They allow unlimited consecutive light letters.

At a starting LL pair the identity $64(q_{i+2}+7)=81(q_i+7)$ and oddness of $q_{i+2}$ give $128\mid q_i+7$. Thus $F_i=(183q_i+1)/128$ is an integer exceeding two. A ready LL position returns to another ready position across L, LLP or LLPP. These cases exhaust the next letters by the two grammar predicates. For a raw triple $(A,M,C)$, the target carry is $(183C+A-M)/128$. I recomputed the chronological target words and triples.

| Raw tile | Target bits | Target $(A,M,C)$ |
|---|---|---|
| L | 011 | $(8,9,10)$ |
| LLP | 10110011100 | $(2048,729,1999)$ |
| LLPP | 1011011100001100 | $(65536,6561,32999)$ |

The successive ready positions progress by positive target clocks. Since every endpoint exceeds two, no intervening target iterate can hit one, whose entire forward orbit is $\{1,2\}$. The raw chain also has all boundaries greater than two, by oddness and either edge. This gives nonconvergence for both the raw boundaries and the ready comparison states.

From a boundary beginning P, LP or LLP the next end of that prefix is a smaller positive odd nonconverger below both the raw boundary and its first odd intermediate. The respective affine triples are $(32,9,5),(256,81,103),(2048,729,1391)$. The remaining case begins LLL, so $q_i=1024t-7$ with $t\ge1$ by the same light congruence one place later. Then $F_i=2(732t-5)$ gives an actual odd successor $m=732t-5<768t-5=(3q_i+1)/4<q_i$. This proves the requested strictness at each physical boundary. An infinite raw itinerary is required throughout. The argument supplies neither a total selector for arbitrary inputs nor a restriction on words containing PPP or PLP.
