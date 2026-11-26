# An unconditional lower tail for total finite-gate flux

**Status.** A matching pressure scale from ordinary finite paths for the transfer factor in [the short-history sieve](../renewal/GATE_PROXIMITY.md). This lower bound concerns total flux; it does not require that its constructed gates miss the sieve.

For $s>2$ the ordinary first-exit weights of [OP-G1](EXIT_GATES.md) satisfy, uniformly at every sufficiently large integer cutoff,
$$
                 \|J_{s,X}\|_1\ge c_s X^{-\log_3(2^s-1)} .
$$
The exponent is strictly smaller than $s-1$ because $2^s-1<3^{s-1}$ for $s>2$ (divide by $3^{s-1}$ and use strict decrease past $2$, or strict convexity of $2^{-s}(1+3^{s-1})$). Thus a universal deflation at the direct single-step scale $X^{1-s}$ is false in this range even before any issue concerning a fixed infinite trajectory. Also for every $s>1$,
$$
                      \|J_{s,X}\|_\infty\ge c_s X^{-s\log_3 2}.
$$

Fix $0<\eta<1/4$ and choose $q=\lfloor\log_3 X\rfloor-B$ with $B$ fixed sufficiently large. Each residue modulo $3^q$ has some representative $y\in[X,(1+\eta)X]$. Consider reversed native words ending exactly at their $q$th odd letter and satisfying $3^{q_j}/2^j>1+\eta$ at every nonempty initial reverse prefix. The whole word specifies a single admissible residue modulo $3^q$, by the inverse branches $E(y)=2y,\ O(y)=(2y-1)/3$. For an explicit check, the rank-$k$ carry congruence reduces modulo the first $3$ to legality at the first reversed odd, then cancels to the shorter congruence. There is no constraint at an even inverse letter. All reversed intermediate states are positive integers, and a nonempty prefix of incoming slope $C_j$ has predecessor at most $y/C_j<X$. Hence each selected representative gives a true first exit to $y$, with weight $(3^q/(2^ky))^s\gg_{s,B}2^{-sk}$. Distinct word-representative pairs cannot double-count an identical start even at different lengths, because its first-exit time, gate, and entire script are deterministic.

Decompose a word at its successive odd letters, with intervening waiting lengths $e_i\ge1$ including the terminal odd. The unrestricted sum of weights $2^{-s\sum e_i}$ at grade $q$ is $(2^s-1)^{-q}$. Under its normalized law the native bits are Bernoulli-$p$ stopped on their $q$th success, $p=1-2^{-s}$. For $s>2$, $p>3/4>\log_3 2$, so $\log(3^{q_j}/2^j)$ has positive drift. A fixed initial run of odd letters makes the probability of staying above $\log(1+\eta)$ at all nonempty times bounded below uniformly in $q$. Indeed the strong law implies the infimum over the entire future walk is finite almost surely, so a sufficiently large fixed initial buffer succeeds with positive probability. This event up to stopping has at least that probability. Summing the valid first exits proves the total lower bound.

For the maximum, take the single all-odd reverse word of length $q$. Its required residue is $y=-1\bmod3^q$ and its unique start has form $x=2^q(y+1)/3^q-1$. Here $x\asymp X^{\log_3 2}$ and the exact charge $(3^q/(2^qy))^s\gg_sX^{-s\log_3 2}$ enters a single gate. No infinite ordinary path is required.
